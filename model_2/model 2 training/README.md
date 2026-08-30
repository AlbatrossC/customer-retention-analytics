# Retention Intelligence LLM Fine-Tuning

This project fine-tunes compact instruction-following language models to produce structured banking customer-retention recommendations. The dataset and record format are documented separately in [Dataset Info.md](Dataset%20Info.md).

Given a system instruction and a customer record, the model is trained to return JSON containing:

- `why`: a list explaining the recommendation using evidence from the customer record.
- `next_actions`: a list of operational actions.

The permitted action prefixes are `rm_call`, `rate_offer`, `fee_waiver`, `complaint_escalation`, and `do_nothing`.

The main experiment is in [LLMFineTuning.ipynb](LLMFineTuning.ipynb).

## Models

Two Qwen instruction models were compared:

| Candidate | Base model | Intended role | Adapter location |
| --- | --- | --- | --- |
| 0.5B | `Qwen/Qwen2.5-0.5B-Instruct` | Lower-memory and lower-latency deployment | `content/model2-0.5b-lora/` |
| 1.5B | `Qwen/Qwen2.5-1.5B-Instruct` | Higher-capacity quality candidate | `content/model2-1.5b-lora/` |

Both candidates use the same task format, LoRA configuration, learning rate, batch configuration, and nominal three-epoch training schedule. This makes the comparison approximately controlled: the main variable is model capacity.

## Training configuration

| Setting | Value |
| --- | --- |
| Training method | Supervised fine-tuning (SFT) |
| Nominal epochs | 3 |
| Per-device batch size | 4 |
| Gradient accumulation | 4 steps |
| Effective batch size | 16 examples per optimizer update, assuming one device |
| Learning rate | `2e-4` |
| Sequence length | 1024 tokens |
| Logging | Every 10 steps |
| Validation/checkpoint strategy | End of each epoch |
| Compute loading | 4-bit NF4 quantization with double quantization |
| Compute dtype | `bfloat16` |
| Random seed | 42 |

The training loop loads `model2_train.jsonl`, `model2_validation.jsonl`, and `model2_test.jsonl`. The current dataset contains 1,000 synthetic records: 802 training examples, 99 validation examples, and 99 held-out test examples. See [Dataset Info.md](Dataset%20Info.md) for the schema, composition, risk groups, and output expectations.

## LoRA configuration

LoRA, or Low-Rank Adaptation, freezes the original model weights and learns small trainable low-rank update matrices. For a weight matrix $W$, the adapted weight can be represented as:

$$
W' = W + \Delta W, \qquad \Delta W = B A
$$

where $A$ and $B$ have a much smaller rank than $W$. This substantially reduces trainable parameters, optimizer state, memory use, and adapter size while preserving the base model for reuse.

This experiment uses:

- Rank `r=16`.
- LoRA scaling `alpha=32`, giving an effective scale of `alpha/r = 2`.
- Dropout `0.05`.
- No bias adaptation.
- Causal language-model task type.
- Attention projections `q_proj`, `k_proj`, `v_proj`, and `o_proj`.
- MLP projections `gate_proj`, `up_proj`, and `down_proj`.

The base models are loaded with 4-bit NF4 quantization and prepared for k-bit training. This is a QLoRA-style memory-saving setup: quantization is used for the frozen base model while LoRA parameters are trained in higher precision. The saved directories primarily contain adapter weights, tokenizer files, and checkpoint state rather than complete standalone base models.

## Persisted training evaluation

The notebook itself has no recorded executions in this workspace, but the saved `trainer_state.json` files contain training logs. The following values are therefore persisted training-run evidence, not results freshly reproduced by this README.

| Model | Epoch | Steps | Train loss | Validation loss | Validation token accuracy |
| --- | ---: | ---: | ---: | ---: | ---: |
| 0.5B | 1 | 51 | 0.2859 | 0.2719 | 90.69% |
| 0.5B | 2 | 102 | 0.2331 | 0.2361 | 91.70% |
| 0.5B | 3 | 153 | 0.2179 | 0.2301 | 91.84% |
| 1.5B | 1 | 51 | 0.2715 | 0.2587 | 90.98% |
| 1.5B | 2 | 102 | 0.2230 | 0.2263 | 91.88% |

### Interpretation

The 1.5B model has a small validation advantage at epoch 2, while the 0.5B model has a completed three-epoch run and only a small validation improvement from epoch 2 to epoch 3. The 0.5B validation loss decreased from 0.2719 to 0.2301 across training, with token accuracy rising from 90.69% to 91.84%. The 1.5B run should not be described as a completed three-epoch comparison from the current artifacts because its epoch-3 checkpoint and final trainer state are absent.

Token accuracy and language-model loss measure next-token prediction, not whether a recommendation is operationally correct. They should be treated as optimization diagnostics. For deployment selection, the notebook's held-out test evaluator is the more relevant measure.

## Generation-based evaluation

The notebook defines an evaluation function that generates up to 300 new tokens per test record with sampling enabled (`temperature=0.3`). It reports:

| Metric | Meaning |
| --- | --- |
| JSON validity rate | Fraction of responses that parse as JSON and contain list-valued `why` and `next_actions` fields |
| Prefix validity rate | Fraction of responses whose action prefixes all belong to the allowed vocabulary |
| Grounding rate | Fraction of checked responses whose numeric evidence overlaps with numbers in the input record |
| Average latency | Mean generation time per test example |
| Composite score | `0.5 * JSON validity + 0.3 * prefix validity + 0.2 * grounding` |

The test JSONL files are now present, but no test-set metric values are recorded because the notebook cells have not been executed in this workspace. The composite score also has an important limitation: invalid JSON receives no prefix or grounding credit, and grounding only checks numeric overlap. It does not verify whether the explanation is causally correct, whether an action is suitable, or whether the output is safe for a customer-facing workflow.

For a defensible model decision, run both candidates on the same untouched test set and report the complete metric table, test-set size, latency hardware, and several representative failure cases. Prefer the 1.5B model only if its quality improvement is meaningful relative to its additional memory and latency; otherwise the 0.5B model is the more practical deployment candidate.

## Libraries and their roles

- **PyTorch**: tensor operations, GPU execution, inference, and memory cleanup.
- **Transformers**: loads Qwen models and tokenizers, applies chat templates, and performs text generation.
- **PEFT**: defines and attaches LoRA adapters, prepares quantized models, loads adapters, and merges them into base weights.
- **bitsandbytes**: provides 4-bit NF4 quantized model loading.
- **TRL**: provides `SFTTrainer` and `SFTConfig` for supervised fine-tuning.
- **Datasets**: converts JSON records into Hugging Face datasets and maps them into formatted training text.
- **Accelerate**: supports device placement and efficient distributed or mixed-precision training infrastructure.
- **llama.cpp**: converts the merged Hugging Face model to GGUF and quantizes it to `Q4_K_M` for lightweight inference.
- **Python standard library**: JSONL loading, regular expressions for numeric checks, timing, randomness, garbage collection, and filesystem operations.

## Export workflow

The notebook includes a merge-and-export path:

1. Load the original base model in `bfloat16`.
2. Load the saved LoRA adapter with PEFT.
3. Merge the adapter into the base weights with `merge_and_unload()`.
4. Convert the merged model to F16 GGUF using `llama.cpp`.
5. Quantize the GGUF to `Q4_K_M`.

In the current notebook, only the 0.5B model is actually passed to `merge_and_save`, and only the 0.5B GGUF conversion commands are active. The 1.5B merge loop is commented out. Therefore, the repository should not be described as containing exported GGUF files for both models unless those steps are run and the files are added.

## Reproduction

Use a Colab or local GPU environment with the required packages:

```bash
pip install transformers peft bitsandbytes trl accelerate datasets
```

Place the three JSONL datasets in the notebook's working directory, then run the notebook from top to bottom. For a fair comparison, keep the same data split and generation settings for both models. Record the printed `results` dictionary, including `json_valid_rate`, `prefix_valid_rate`, `grounding_rate`, `avg_latency_sec`, and `composite_score`.

## Limitations and next steps

- Add the train, validation, and test JSONL files or document their source and schema.
- Complete the 1.5B epoch-3 run before comparing final checkpoints.
- Save test metrics and per-example failures as a reproducible evaluation artifact.
- Add exact action-label accuracy and semantic grounding checks against gold outputs.
- Use deterministic decoding for repeatable benchmark results, or report multiple seeds when sampling is intentional.
- Evaluate malformed JSON, unsupported actions, contradictory customer evidence, and missing fields.
- Add safeguards and human review before using recommendations in real retention decisions.