"""
Paraphrase Model 2's seed why/next_actions text using a local Ollama model
============================================================================

WHY THIS EXISTS
----------------
The 500-record seed dataset (model2_training_data.jsonl) has factually
correct why/next_actions text, but it was built from a fixed phrase bank,
so many records share near-identical sentence structure. Fine-tuning
directly on that teaches the model to imitate the templates, not to reason.

This script sends each record's why/next_actions through a local LLM
(qwen2.5:3b via Ollama) with a strict "reword only, don't change facts"
prompt, then validates that every number mentioned in the original text
still appears in the paraphrase before accepting it. Anything that fails
validation is kept as the original (never silently dropped) and flagged
in a report at the end so you can spot-check it.

PREREQUISITES
-------------
1. Ollama running locally:      ollama serve
2. Model pulled:                ollama pull qwen2.5:3b   (you already have this)
3. Python deps:                 pip install requests tqdm

USAGE
-----
    python paraphrase_dataset.py --dry-run        # test on 5 records first
    python paraphrase_dataset.py                  # run on all 500
    python paraphrase_dataset.py --resume         # continue after interruption

The script writes incrementally to the output file, so it's safe to stop
and resume — it won't reprocess records already done.
"""

import argparse
import json
import os
import re
import time
from pathlib import Path

import requests
from tqdm import tqdm

OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL = "qwen2.5:3b"

SCRIPT_DIR = Path(__file__).resolve().parent
INPUT_PATH = SCRIPT_DIR / "model2_training_data.jsonl"
OUTPUT_PATH = SCRIPT_DIR / "model2_training_data_paraphrased.jsonl"
FAILED_LOG_PATH = SCRIPT_DIR / "paraphrase_failures.jsonl"

PARAPHRASE_SYSTEM_PROMPT = """You are a text editor. You will receive a JSON object with two arrays: "why" and "next_actions".

Your ONLY job is to reword each string in both arrays so they read naturally and don't sound templated, while:
- Keeping every number, percentage, day count, and named fact EXACTLY the same (do not round, change, add, or drop any number).
- Keeping the same number of items in each array.
- Keeping any "category:" prefix at the start of next_actions items exactly as-is (e.g. "rm_call:", "complaint_escalation:", "rate_offer:", "fee_waiver:", "do_nothing:") — only reword the text AFTER the colon.
- Keeping any direct quotes (text in double quotes inside a why item) EXACTLY unchanged, word for word.
- Not adding new claims, not removing existing claims, not changing the meaning.

Return ONLY a valid JSON object of the exact form {"why": [...], "next_actions": [...]}. No explanation, no markdown, no code fences."""


def call_ollama(payload_json, max_retries=3):
    user_prompt = json.dumps(payload_json, ensure_ascii=False)
    for attempt in range(max_retries):
        try:
            resp = requests.post(
                OLLAMA_URL,
                json={
                    "model": MODEL,
                    "messages": [
                        {"role": "system", "content": PARAPHRASE_SYSTEM_PROMPT},
                        {"role": "user", "content": user_prompt},
                    ],
                    "format": "json",       # ask Ollama to constrain to valid JSON
                    "stream": False,
                    "options": {"temperature": 0.4},
                },
                timeout=60,
            )
            resp.raise_for_status()
            content = resp.json()["message"]["content"]
            return json.loads(content)
        except (requests.RequestException, json.JSONDecodeError, KeyError) as e:
            if attempt == max_retries - 1:
                return None
            time.sleep(1.5 * (attempt + 1))
    return None


def extract_numbers(text_list):
    nums = set()
    for t in text_list:
        for m in re.findall(r"-?\d+\.?\d*", t):
            try:
                nums.add(abs(round(float(m))))
            except ValueError:
                pass
    return nums


def extract_quotes(text_list):
    quotes = set()
    for t in text_list:
        quotes.update(re.findall(r'"([^"]+)"', t))
    return quotes


def extract_action_prefixes(action_list):
    prefixes = []
    for a in action_list:
        if ":" in a:
            prefixes.append(a.split(":", 1)[0].strip())
        else:
            prefixes.append(None)
    return prefixes


def validate_paraphrase(original, candidate):
    """Returns (is_valid, reason_if_not)."""
    if not isinstance(candidate, dict) or "why" not in candidate or "next_actions" not in candidate:
        return False, "missing keys"
    if not isinstance(candidate["why"], list) or not isinstance(candidate["next_actions"], list):
        return False, "wrong types"
    if len(candidate["why"]) != len(original["why"]):
        return False, "why length changed"
    if len(candidate["next_actions"]) != len(original["next_actions"]):
        return False, "next_actions length changed"

    orig_nums = extract_numbers(original["why"] + original["next_actions"])
    new_nums = extract_numbers(candidate["why"] + candidate["next_actions"])
    missing_nums = orig_nums - new_nums
    if missing_nums:
        return False, f"dropped numbers: {missing_nums}"

    orig_quotes = extract_quotes(original["why"])
    new_quotes = extract_quotes(candidate["why"])
    if orig_quotes and not orig_quotes.issubset(new_quotes):
        return False, f"altered/dropped quoted complaint text: {orig_quotes - new_quotes}"

    orig_prefixes = extract_action_prefixes(original["next_actions"])
    new_prefixes = extract_action_prefixes(candidate["next_actions"])
    if orig_prefixes != new_prefixes:
        return False, f"action category prefixes changed: {orig_prefixes} -> {new_prefixes}"

    return True, None


def load_done_ids(path):
    done = set()
    if os.path.exists(path):
        with open(path, encoding="utf-8") as f:
            for line in f:
                try:
                    rec = json.loads(line)
                    key = rec.get("customer_id") or rec.get("cohort_id")
                    done.add(key)
                except json.JSONDecodeError:
                    pass
    return done


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true", help="Only process 5 records, print results, write nothing.")
    parser.add_argument("--resume", action="store_true", help="Skip records already in the output file.")
    args = parser.parse_args()

    with open(INPUT_PATH, encoding="utf-8") as f:
        records = [json.loads(l) for l in f]

    if args.dry_run:
        records = records[:5]

    done_ids = load_done_ids(OUTPUT_PATH) if args.resume else set()
    if done_ids:
        print(f"Resuming — {len(done_ids)} records already done, skipping those.")

    out_mode = "a" if args.resume else "w"
    fail_mode = "a" if args.resume else "w"

    n_ok, n_fallback = 0, 0
    with open(OUTPUT_PATH if not args.dry_run else os.devnull, out_mode, encoding="utf-8") as out_f, \
         open(FAILED_LOG_PATH if not args.dry_run else os.devnull, fail_mode, encoding="utf-8") as fail_f:

        for rec in tqdm(records, desc="Paraphrasing"):
            key = rec.get("customer_id") or rec.get("cohort_id")
            if key in done_ids:
                continue

            original_output = rec["output"]
            candidate = call_ollama(original_output)

            if candidate is not None:
                is_valid, reason = validate_paraphrase(original_output, candidate)
            else:
                is_valid, reason = False, "ollama call failed / bad JSON"

            new_rec = dict(rec)
            if is_valid:
                new_rec["output"] = candidate
                new_rec["_paraphrased"] = True
                n_ok += 1
            else:
                # keep the original text — never lose data, just flag it
                new_rec["_paraphrased"] = False
                new_rec["_paraphrase_failure_reason"] = reason
                n_fallback += 1
                fail_f.write(json.dumps({"id": key, "reason": reason, "original": original_output, "candidate": candidate}, ensure_ascii=False) + "\n")

            if args.dry_run:
                print(f"\n--- {key} ---")
                print("ORIGINAL:", json.dumps(original_output, ensure_ascii=False))
                print("PARAPHRASE VALID:", is_valid, f"({reason})" if not is_valid else "")
                print("RESULT:", json.dumps(new_rec["output"], ensure_ascii=False))
            else:
                out_f.write(json.dumps(new_rec, ensure_ascii=False) + "\n")

    print(f"\nDone. Paraphrased successfully: {n_ok}  |  Kept original (failed validation): {n_fallback}")
    if n_fallback:
        print(f"See {FAILED_LOG_PATH} for what failed and why — worth a quick skim before fine-tuning.")


if __name__ == "__main__":
    main()
