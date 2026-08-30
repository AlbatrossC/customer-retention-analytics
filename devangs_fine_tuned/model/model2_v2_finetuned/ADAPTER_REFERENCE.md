# Model 2 V2 Adapter — External Artifact Reference

This directory is a **pointer** to the Model 2 V2 LoRA adapter.

## Artifact Details

| Field | Value |
|---|---|
| **Base model** | `Qwen/Qwen2.5-3B-Instruct` |
| **Adapter name** | `model2_v2_finetuned` |
| **PEFT type** | LoRA |
| **Rank (r)** | 16 |
| **Alpha** | 32 |
| **Dropout** | 0.05 |
| **Bias** | none |
| **Task type** | CAUSAL_LM |
| **Target modules** | `down_proj`, `q_proj`, `k_proj`, `up_proj`, `o_proj`, `v_proj`, `gate_proj` |
| **Adapter size** | ~114–115 MB (`adapter_model.safetensors`) |

## Files in the Adapter Directory

When the adapter is downloaded/extracted, it should contain:

- `adapter_model.safetensors` (~114–115 MB)
- `adapter_config.json`
- `tokenizer_config.json`
- `tokenizer.json`
- `vocab.json`
- `merges.txt`
- `added_tokens.json`
- `special_tokens_map.json`
- `chat_template.jinja`
- `README.md`

## How to Obtain

The adapter is distributed as a ZIP file (`model2_v2_finetuned.zip`) outside
of Git to keep the repository lightweight.

**Option A — Download from the shared project storage:**

1. Obtain `model2_v2_finetuned.zip` from the project's shared artifact location
   (team drive, GitHub Release asset, or Hugging Face Hub — ask the project lead).
2. Extract it into this directory:
   ```bash
   unzip model2_v2_finetuned.zip -d model/model2_v2_finetuned/
   ```
3. Verify the files listed above are present.

**Option B — Hugging Face Hub (if uploaded):**

If the adapter has been pushed to a Hugging Face Hub repo, update
`ADAPTER_PATH` in `src/config/settings.py` to the Hub repo id
(e.g., `"your-org/model2-v2-finetuned"`) and PEFT will download it
automatically at load time.

## Verification

After placing the files, you can verify the adapter loads correctly:

```python
from src.inference import Model2Engine

engine = Model2Engine()
print("Model loaded successfully.")
```
