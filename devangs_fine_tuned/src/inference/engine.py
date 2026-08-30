"""
Model 2 inference engine — single-record and batch prediction.

Loads the Qwen2.5-3B-Instruct base model and the model2_v2_finetuned LoRA
adapter (V2), constructs chat-template prompts matching the training-time
serialization, and parses + validates the structured JSON output.

Default runtime: base model + V2 adapter.
checkpoint-145 (V1) is optional/historical and never required here.
"""

import gc
import json
import re
import time
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import torch
from peft import PeftModel
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig

from src.config.settings import (
    ADAPTER_PATH,
    APPROVED_ACTIONS_SET,
    APPROVED_REASONS_SET,
    APPROVED_URGENCY_SET,
    BASE_MODEL_ID,
    DEFAULT_MAX_LENGTH,
    DEFAULT_MAX_NEW_TOKENS,
    FALLBACK_TRIPLE,
    SYSTEM_PROMPT,
)
from src.schema.validators import validate_model2_output


class Model2Engine:
    """
    Inference engine for Model 2 (Qwen2.5-3B-Instruct + V2 LoRA adapter).

    Parameters
    ----------
    base_model_id : str
        Hugging Face model id for the base model.
    adapter_path : str
        Path to the LoRA adapter directory (or HF Hub id).
    load_in_4bit : bool
        Whether to use 4-bit quantization (reduces memory, recommended for
        inference on consumer GPUs).
    device_map : str
        Device placement strategy passed to ``from_pretrained``.
    """

    def __init__(
        self,
        base_model_id: str = BASE_MODEL_ID,
        adapter_path: str = ADAPTER_PATH,
        load_in_4bit: bool = True,
        device_map: str = "auto",
    ):
        self.base_model_id = base_model_id
        self.adapter_path = adapter_path

        # Determine compute dtype
        compute_dtype = (
            torch.bfloat16 if torch.cuda.is_bf16_supported() else torch.float16
        )

        # Quantization config
        if load_in_4bit:
            bnb_config = BitsAndBytesConfig(
                load_in_4bit=True,
                bnb_4bit_quant_type="nf4",
                bnb_4bit_use_double_quant=True,
                bnb_4bit_compute_dtype=compute_dtype,
            )
        else:
            bnb_config = None

        # Load tokenizer
        self.tokenizer = AutoTokenizer.from_pretrained(
            adapter_path, use_fast=True
        )
        if self.tokenizer.pad_token is None:
            self.tokenizer.pad_token = self.tokenizer.eos_token
        self.tokenizer.padding_side = "left"

        # Load base model
        model_kwargs = {
            "device_map": device_map,
            "torch_dtype": compute_dtype,
        }
        if bnb_config is not None:
            model_kwargs["quantization_config"] = bnb_config

        base_model = AutoModelForCausalLM.from_pretrained(
            base_model_id, **model_kwargs
        )
        base_model.config.use_cache = True  # inference only

        # Load V2 LoRA adapter
        self.model = PeftModel.from_pretrained(base_model, adapter_path)
        self.model.eval()

    # ── prompt construction ──────────────────────────────────────────────

    @staticmethod
    def _canonical_user_json(case_input: Dict[str, Any]) -> str:
        """Serialize user content identically to training-time format."""
        return json.dumps(
            case_input,
            ensure_ascii=False,
            sort_keys=True,
            separators=(",", ":"),
            allow_nan=False,
        )

    def _build_prompt(self, case_input: Dict[str, Any]) -> str:
        """Build the full chat-template prompt (system + user, no assistant)."""
        messages = [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": self._canonical_user_json(case_input)},
        ]
        return self.tokenizer.apply_chat_template(
            messages, tokenize=False, add_generation_prompt=True
        )

    # ── JSON extraction ──────────────────────────────────────────────────

    @staticmethod
    def _extract_json_object(text: str) -> str:
        """Extract the first complete JSON object from model output text."""
        text = text.strip()
        if text.startswith("```"):
            text = re.sub(r"^```(?:json)?", "", text.strip(), flags=re.IGNORECASE).strip()
            text = re.sub(r"```$", "", text.strip()).strip()
        start, end = text.find("{"), text.rfind("}")
        if start == -1 or end == -1 or end <= start:
            raise ValueError(f"Could not find JSON object in model output: {text[:400]}")
        return text[start : end + 1]

    # ── single prediction ────────────────────────────────────────────────

    @torch.no_grad()
    def predict(
        self,
        case_input: Dict[str, Any],
        max_new_tokens: int = DEFAULT_MAX_NEW_TOKENS,
        max_length: int = DEFAULT_MAX_LENGTH,
    ) -> Dict[str, Any]:
        """
        Run inference on a single Model 2 input record.

        Parameters
        ----------
        case_input : dict
            A Model 2 input record (Section 5 schema).
        max_new_tokens : int
            Maximum tokens to generate.
        max_length : int
            Maximum total sequence length (prompt + generation).

        Returns
        -------
        dict with keys:
            - ``raw_text``: the raw decoded model output
            - ``parsed``: the parsed dict (or None if parsing failed)
            - ``ok``: bool, True if valid output was produced
            - ``error``: error message string (or None)
            - ``latency_s``: inference latency in seconds
        """
        prompt = self._build_prompt(case_input)
        model_inputs = self.tokenizer(
            prompt, return_tensors="pt", truncation=True, max_length=max_length
        ).to(self.model.device)

        t0 = time.perf_counter()
        outputs = self.model.generate(
            **model_inputs,
            max_new_tokens=max_new_tokens,
            do_sample=False,
            num_beams=1,
            pad_token_id=self.tokenizer.pad_token_id,
            eos_token_id=self.tokenizer.eos_token_id,
        )
        latency_s = time.perf_counter() - t0

        input_len = model_inputs["input_ids"].shape[-1]
        raw_text = self.tokenizer.decode(
            outputs[0][input_len:], skip_special_tokens=True
        ).strip()

        result: Dict[str, Any] = {
            "raw_text": raw_text,
            "parsed": None,
            "ok": False,
            "error": None,
            "latency_s": latency_s,
        }

        try:
            json_str = self._extract_json_object(raw_text)
            parsed = json.loads(json_str)
            errors = validate_model2_output(
                parsed, eligible_actions=case_input.get("eligible_actions")
            )
            if errors:
                raise ValueError("; ".join(errors))
            result["parsed"] = parsed
            result["ok"] = True
        except Exception as e:
            result["error"] = str(e)

        return result

    # ── batch prediction ─────────────────────────────────────────────────

    def predict_batch(
        self,
        input_path: str,
        output_path: str,
        id_column: str = "case_id",
        max_new_tokens: int = DEFAULT_MAX_NEW_TOKENS,
        max_length: int = DEFAULT_MAX_LENGTH,
    ) -> Dict[str, Any]:
        """
        Run batch inference on a JSONL file of Model 2 inputs.

        Reads records one-by-one, runs prediction, and writes results
        incrementally to avoid holding all outputs in memory.

        Parameters
        ----------
        input_path : str
            Path to input JSONL (one Model 2 input per line).
        output_path : str
            Path to write output JSONL (results written incrementally).
        id_column : str
            Column name for the stable identifier.
        max_new_tokens : int
            Maximum tokens to generate per record.
        max_length : int
            Maximum total sequence length.

        Returns
        -------
        dict
            Summary statistics: total, ok_count, error_count,
            mean_latency_s.
        """
        Path(output_path).parent.mkdir(parents=True, exist_ok=True)

        total = 0
        ok_count = 0
        error_count = 0
        total_latency = 0.0

        with open(input_path, "r", encoding="utf-8") as fin, \
             open(output_path, "w", encoding="utf-8") as fout:

            for line_num, line in enumerate(fin, start=1):
                line = line.strip()
                if not line:
                    continue

                try:
                    record = json.loads(line)
                except json.JSONDecodeError as e:
                    error_result = {
                        "line": line_num,
                        "ok": False,
                        "error": f"Invalid JSON: {e}",
                    }
                    fout.write(json.dumps(error_result, ensure_ascii=False) + "\n")
                    error_count += 1
                    total += 1
                    continue

                # Preserve stable identifier
                stable_id = record.get(id_column)

                # Build the input payload (strip the id_column for inference)
                case_input = {
                    k: v for k, v in record.items() if k != id_column
                }

                result = self.predict(
                    case_input,
                    max_new_tokens=max_new_tokens,
                    max_length=max_length,
                )

                output_record = {
                    id_column: stable_id,
                    "ok": result["ok"],
                    "prediction": result["parsed"],
                    "error": result["error"],
                    "latency_s": round(result["latency_s"], 4),
                }

                fout.write(json.dumps(output_record, ensure_ascii=False) + "\n")

                total += 1
                total_latency += result["latency_s"]
                if result["ok"]:
                    ok_count += 1
                else:
                    error_count += 1

        return {
            "total": total,
            "ok_count": ok_count,
            "error_count": error_count,
            "mean_latency_s": round(total_latency / max(total, 1), 4),
        }

    # ── cleanup ──────────────────────────────────────────────────────────

    def unload(self) -> None:
        """Release model and tokenizer from memory."""
        del self.model
        del self.tokenizer
        gc.collect()
        if torch.cuda.is_available():
            torch.cuda.empty_cache()
