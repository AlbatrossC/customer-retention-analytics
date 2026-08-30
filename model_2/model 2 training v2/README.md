# Model 2 Training v2 — Improved Dataset & Training Pipeline

This directory contains an improved iteration of the customer retention LLM fine-tuning pipeline. This version focuses on refined dataset preparation and streamlined training with updated data formats and system prompts.

## Overview

Model 2 Training v2 fine-tunes compact language models (Qwen 2.5) to generate structured banking customer-retention recommendations. Given a customer record and churn probability, the model outputs JSON containing:

- **`why`**: An explanation of the recommendation grounded in customer data
- **`next_actions`**: A dictionary mapping recommended actions to justifications

### Supported Actions

Recommendations are constrained to the following action prefixes:
- `rm_call` — Initiate relationship manager contact
- `rate_offer` — Offer competitive rates or renewal incentives
- `fee_waiver` — Waive or reduce fees
- `complaint_escalation` — Escalate customer complaints
- `do_nothing` — No immediate action required

## Datasets

This directory contains three modified JSONL files with a total of 1,200 records:

| File | Records | Purpose |
| --- | ---: | --- |
| `train_modified.jsonl` | 960 | Training set for supervised fine-tuning |
| `val_modified.jsonl` | 120 | Validation set for epoch-end checkpointing |
| `test_modified.jsonl` | 120 | Held-out test set for final evaluation |

### Dataset Format

Each line is a JSON object with a `messages` list following the Qwen instruction format:

```json
{
  "messages": [
    {
      "role": "system",
      "content": "You are a banking retention AI. Analyze the customer data and output strict JSON containing 'why', a churn probability field, and 'next_actions' as an object mapping each recommendation to an explanation."
    },
    {
      "role": "user",
      "content": {
        "analysis_type": "individual",
        "customer_data": {
          "profile": { "age": ..., "customer_segment": "...", "customer_yearly_value": ... },
          "financial_activity_30d_trend": { "balance_change": ..., "external_transfer_change": ..., "fd_maturing_in_30d": "..." },
          "friction_signals": { "app_login_change": ..., "complaints_30d": ..., "failed_transactions_30d": ..., "recent_complaint_text": "..." }
        },
        "churn_probability": 0.X
      }
    },
    {
      "role": "assistant",
      "content": {
        "why": "...",
        "next_actions": { "action_type": "explanation", ... }
      }
    }
  ]
}
```

**Key Changes from v1:**
- Churn probability is explicitly included in the user input to guide model reasoning
- `next_actions` is now a dictionary mapping actions to their justifications (not a list)
- System prompt explicitly instructs the model to reference the churn probability field in outputs
- Data cleaning pipeline handles type consistency for `role` and `content` fields

## Training Notebook

`LLMFineTuning.ipynb` implements the complete fine-tuning pipeline across 21 cells:

### Notebook Workflow

1. **Cells 1-2: Environment setup**
   - Install dependencies (transformers, peft, bitsandbytes, trl, accelerate, datasets)
   - Import required libraries

2. **Cell 3: Configuration**
   - Define data paths and allowed action prefixes
   - Configure model candidates (currently 0.5B only)

3. **Cells 4-5: Data loading & validation**
   - Load JSONL files with schema cleaning
   - Validate message structure
   - Print dataset statistics

4. **Cells 6-7: Training & evaluation functions**
   - Define `train_one_model()` for SFT with LoRA
   - Define `evaluate_model()` for test-set metrics

5. **Cell 8: Training loop**
   - Train model(s) on data
   - Evaluate on test set
   - Print results and free GPU memory

6. **Cells 9-10: Workspace archiving**
   - Zip trained artifacts for download

7. **Cells 11-13: Model merging & GGUF conversion setup**
   - Install llama.cpp dependencies
   - Merge LoRA adapters into base weights
   - Prepare for quantization

8. **Cells 14-20: GGUF export pipeline**
   - Fix tokenizer config if needed
   - Convert merged model to GGUF (f16)
   - Quantize to Q4_K_M
   - Download final artifacts

### Base Models

Currently configured to train:
- **Qwen/Qwen2.5-0.5B-Instruct** (model tag: `0.5b`) — Lightweight model optimized for lower-latency, lower-memory deployments

The notebook can be extended to include the 1.5B candidate by adding another entry to `MODEL_CANDIDATES`:
```python
{"name": "Qwen/Qwen2.5-1.5B-Instruct", "tag": "1.5b", "out_dir": "model2-1.5b-lora"}
```

### Training Configuration

| Setting | Value |
| --- | --- |
| Method | Supervised Fine-Tuning (SFT) with LoRA |
| Epochs | 3 |
| Training records | 960 |
| Validation records | 120 |
| Per-device batch size | 4 |
| Gradient accumulation | 4 steps |
| Effective batch size | 16 examples per update |
| Learning rate | 2e-4 |
| Max sequence length | 1024 tokens |
| Quantization | 4-bit NF4 (QLoRA) |
| Compute dtype | bfloat16 |
| Logging frequency | Every 10 steps |
| Validation/checkpointing | End of each epoch |
| Random seed | 42 |

**Training steps per epoch:** ~60 steps (960 training records ÷ effective batch size of 16)

### LoRA Configuration

Low-Rank Adaptation reduces trainable parameters while preserving base model weights:

$$
W' = W + \Delta W, \quad \Delta W = BA
$$

Where $A$ and $B$ have rank $r \ll \text{rank}(W)$.

Configuration:
- **Rank (r)**: 16
- **LoRA scaling (alpha)**: 32 → effective scale = 2
- **Dropout**: 0.05
- **Target modules**: `q_proj`, `k_proj`, `v_proj`, `o_proj` (attention), `gate_proj`, `up_proj`, `down_proj` (MLP)
- **Bias adaptation**: Disabled
- **Task type**: Causal language modeling

## Running the Notebook

### Prerequisites

- Jupyter environment or Google Colab (for free GPU access)
- GPU with ≥16GB VRAM recommended (T4 or better)
- Python 3.9+

### Runtime Estimates

On a Google Colab T4 GPU:
- **Training phase:** ~15–20 minutes (3 epochs × ~60 steps/epoch)
- **Evaluation phase:** ~5 minutes (120 test records)
- **Model merging & GGUF export:** ~10 minutes
- **Total:** ~30–35 minutes for full pipeline

### On Google Colab (Recommended)

1. Open the notebook on Colab
2. Activate T4 GPU: **Runtime → Change runtime type → T4 GPU**
3. Upload the three JSONL files to the Colab session:
   - `train_modified.jsonl` (960 records)
   - `val_modified.jsonl` (120 records)
   - `test_modified.jsonl` (120 records)
4. Run cells top to bottom
5. Download the generated GGUF file and other artifacts at the end

**Note:** File paths in the notebook are set to `/content/` (Colab's default upload directory). If using a different location, update paths in cell 3.

### On Local Machine

1. Ensure CUDA 11.8+ is installed and PyTorch is configured for GPU
2. Place the JSONL files in the notebook's working directory
3. Install dependencies:
   ```bash
   pip install -q transformers peft bitsandbytes trl accelerate datasets
   ```
4. Update paths in cell 3 if needed:
   ```python
   TRAIN_PATH = "train_modified.jsonl"
   VAL_PATH = "val_modified.jsonl"
   TEST_PATH = "test_modified.jsonl"
   ```
5. Run the notebook

## Evaluation Metrics

The notebook computes four primary metrics on the 120 held-out test records:

| Metric | Meaning | Method |
| --- | --- | --- |
| **JSON validity rate** | % of outputs that parse as valid JSON with `why` (list) and `next_actions` (list) fields | Try to parse and validate schema |
| **Prefix validity rate** | % of outputs whose action prefixes all belong to `{rm_call, rate_offer, fee_waiver, complaint_escalation, do_nothing}` | Check prefix of each action string |
| **Grounding rate** | % of outputs whose numeric evidence in `why` overlaps with input record numbers | Extract numbers from both input and explanation |
| **Average latency** | Mean generation time per test example (in seconds) | Measure wall-clock time for generation |
| **Composite score** | Weighted combination emphasizing JSON/prefix correctness | `0.5 × JSON validity + 0.3 × prefix validity + 0.2 × grounding` |

**Important:** The composite score is a development diagnostic, not a production metric. It does not verify:
- Whether explanations are causally correct
- Whether actions are contextually appropriate
- Whether outputs are safe for customer-facing workflows

### Test Results

Results from evaluation on the 120 held-out test records:

| Metric | Score | Notes |
| --- | ---: | --- |
| **JSON Validity** | 97.5% | 117/120 outputs parsed successfully |
| **Prefix Validity** | 62.0% | Valid action prefixes from recognized set |
| **Grounding Rate** | 98.3% | Numeric evidence grounded in input data |
| **Mean Latency** | 0.432s | Per-example generation time on test hardware |
| **Composite Score** | 87.0% | Weighted: 0.5 × JSON + 0.3 × prefix + 0.2 × grounding |

**Key Observations:**
- High JSON validity indicates the model reliably produces parseable structured output
- Grounding rate of 98.3% shows strong evidence of referencing customer data in explanations
- Prefix validity of 62% suggests some actions fall outside expected action types or contain unexpected fields (e.g., `do_nothing_explanation`, `churn_probability`, `cc_to_self`, `rm_email` in outputs)
- Latency of ~430ms per example is suitable for batch processing and batch recommendations

### Test Generation Settings

- **Max new tokens:** 300
- **Temperature:** 0.3 (controlled randomness)
- **Sampling:** Enabled (top-k/top-p defaults)

## Outputs

After successful training, the notebook generates:

### Adapter Output
```
model2-0.5b-lora/
├── adapter_config.json         # LoRA configuration
├── adapter_model.safetensors   # Trained adapter weights
├── chat_template.jinja         # Chat template for inference
├── tokenizer.json
├── tokenizer_config.json
├── README.md
└── checkpoint-{step}/          # Checkpoints at validation epochs
    ├── adapter_config.json
    ├── adapter_model.safetensors
    ├── trainer_state.json
    ├── optimizer.pt
    ├── scheduler.pt
    └── ...
```

### Merged Model & GGUF Export
The notebook also merges the LoRA adapters into the base model weights and exports to GGUF format:

```
merged_0.5b/                                # Merged model (full weights)
├── config.json
├── model.safetensors
├── tokenizer.json
└── ...

model2_retention_0.5b.gguf                  # Quantized model for inference
model2_retention_0.5b_f16.gguf              # Full-precision GGUF (intermediate)
```

**GGUF Quantization:** Q4_K_M (4-bit quantization, highly compressed, suitable for CPU/edge deployment)

## Differences from Model 2 Training v1

| Aspect | v1 | v2 |
| --- | --- | --- |
| **Total dataset size** | 1,000 records (802/99/99) | 1,200 records (960/120/120) |
| **Dataset format** | Raw JSON | Cleaned & type-validated |
| **Churn probability** | Not in input | Included in user content |
| **next_actions schema** | List of strings | Dictionary with explanations |
| **Data cleaning** | Minimal | Robust message schema validation |
| **System prompt** | Generic | Explicit churn probability instruction |
| **Model candidates** | 0.5B and 1.5B (both) | 0.5B (focused, 1.5B optional) |
| **Export format** | GGUF not included | GGUF export with Q4_K_M quantization |

## Next Steps

1. **Run the notebook end-to-end** on Colab or local GPU
2. **Review training logs** in the notebook output cells and `trainer_state.json` files
3. **Analyze test metrics** printed at the end of the training loop
4. **Download artifacts:**
   - `model2_retention_0.5b.gguf` — Quantized model for inference with llama.cpp
   - `merged_0.5b/` — Merged full-weights model (for fine-tuning further or direct inference)
   - `model2-0.5b-lora/` — Adapter weights (for loading with peft)
5. **Benchmark latency** on target inference hardware (CPU/GPU)
6. **Validate on production data** before deployment
7. **(Optional) Extend to 1.5B candidate** by adding to `MODEL_CANDIDATES` if quality gain justifies the latency/memory cost

## Production Deployment Recommendations

### Using the GGUF Model
```bash
# With llama.cpp (CPU or GPU)
./main -m model2_retention_0.5b.gguf \
  -p "prompt..." \
  -n 300 \
  --temperature 0.3 \
  --top-k 40 --top-p 0.9
```

### Using the Merged Model
```python
from transformers import AutoModelForCausalLM, AutoTokenizer

model = AutoModelForCausalLM.from_pretrained("merged_0.5b", torch_dtype="bfloat16")
tokenizer = AutoTokenizer.from_pretrained("merged_0.5b")

# Generate recommendations...
```

### Using the Adapter (LoRA)
```python
from peft import PeftModel
from transformers import AutoModelForCausalLM, AutoTokenizer

base = AutoModelForCausalLM.from_pretrained("Qwen/Qwen2.5-0.5B-Instruct")
model = PeftModel.from_pretrained(base, "model2-0.5b-lora")

# Generate recommendations...
```

## References

- [Qwen2.5 Model Card](https://huggingface.co/Qwen/Qwen2.5-0.5B-Instruct)
- [LoRA Paper](https://arxiv.org/abs/2106.09685)
- [QLoRA Paper](https://arxiv.org/abs/2305.14314)
- [Hugging Face TRL Documentation](https://huggingface.co/docs/trl/)

## Author Notes

This version focuses on dataset robustness and explicit churn grounding. For production use, validate on representative customer data and monitor for hallucinations or unsafe recommendations.
