# Model 2 — Retention Reason Analysis

Model 2 is the **structured-reasoning component** of a bank customer-retention
pipeline. Given a customer's profile, recent behavioral signals, service
history, and the churn-risk output of an upstream XGBoost model (Model 1),
Model 2 determines:

- **Why** the customer is at risk (primary and secondary reasons),
- **How urgent** the situation is,
- **What retention action** to take, and
- **What evidence** supports the decision.

All outputs are structured JSON, validated against a strict schema with
approved value lists.

---

## Where Model 2 Fits

```
customers.csv
    ↓
Model 1 / XGBoost           ← churn probability, risk level, top factors
    ↓
Model 1 outputs
    ↓
construct Model 2 input JSONL
    ↓
Qwen2.5-3B-Instruct + model2_v2_finetuned   ← THIS COMPONENT
    ↓
Model 2 structured output
    ↓
clustering                   ← group customers by reason/urgency patterns
    ↓
dashboard                    ← human-facing retention intelligence UI
```

For the demo/prototype, this pipeline is designed to be **precomputed offline**
for the customer population, with results stored for the dashboard to consume.
Nothing in the current artifacts supports a claim of real-time production
inference.

---

## V1 vs V2

| | V1 (checkpoint-145) | V2 (model2_v2_finetuned) |
|---|---|---|
| **Base model** | Qwen2.5-3B-Instruct | Qwen2.5-3B-Instruct |
| **Training** | SFTTrainer, 1 epoch, lr=2e-4 | Custom PyTorch loop, 1 epoch, lr=4e-5 |
| **Training data** | 2,306 examples | 828 examples (targeted refinement) |
| **LoRA rank** | 16 | 16 |
| **Status** | Historical / reference only | **Final selected model** |

**V2 is the default runtime.** checkpoint-145 (V1) is not required for standard
inference and is kept only as historical reference.

### Why V2 Was Created

V2 was created through targeted LoRA refinement to address specific,
data-driven error patterns found in V1's evaluation:

1. **PRODUCT_MISMATCH** recall was 0.43 on 30 support cases — the model
   consistently leaked these into 3+ other reason classes.
2. **UNKNOWN** recall was 0.44 on 34 support cases.
3. **COMPETITOR_MIGRATION ↔ LIFE_STAGE_CHANGE** confusion occurred in 5 of 52
   (9.62%) true COMPETITOR_MIGRATION cases.
4. **HIGH urgency downgraded to MEDIUM** in 21 of 257 (8.17%) true-HIGH cases.
5. **MONITOR action** recall was 0.60 on 42 support cases, leaking mainly into
   SERVICE_RECOVERY (over-escalation).

The refinement dataset contained **828 examples**: 276 targeted correction
examples (drawn from real error patterns in the 466-case validation results) +
552 retained original training examples (386 High/Medium-risk, 166 Low-risk),
seed=42. Confirmed zero overlap with validation/test case_ids.

Training used a custom PyTorch loop (not SFTTrainer, not HuggingFace Trainer):
LoRA r=16, alpha=32, dropout=0.05, gradient accumulation steps=8, lr=4e-5,
1 epoch, 104 optimizer steps, final avg_loss=0.018283. All 504/504 LoRA tensors
changed vs checkpoint-145; max absolute weight change was 2.394e-03.

---

## Model 2 Input Schema

The complete input contract (all fields required unless noted):

```json
{
  "customer_context": {
    "age": "int",
    "tenure_months": "int",
    "customer_segment": "string: salary | pension | farmer | vendor | business",
    "income_regularity": "string: regular | irregular | seasonal",
    "customer_yearly_value": "float",
    "products_count": "int",
    "has_credit_card": "0 or 1",
    "has_loan": "0 or 1"
  },
  "behavior": {
    "days_since_last_transaction": "int",
    "balance_change_30d": "float (percent)",
    "transaction_change_30d": "float (percent)",
    "card_spend_change_30d": "float (percent)",
    "app_login_change_30d": "float (percent)",
    "salary_missing_days": "int or null",
    "external_transfer_change_30d": "float (percent)",
    "upi_share_of_spend": "float 0-1",
    "fd_maturing_in_30d": "0 or 1",
    "products_dropped_90d": "int",
    "emi_bounce_30d": "int"
  },
  "service_evidence": {
    "complaints_30d": "int",
    "unresolved_complaints": "int",
    "failed_transactions_30d": "int",
    "avg_resolution_time_hrs": "float",
    "complaint_text": "string or null (free text, may be non-English)"
  },
  "model1": {
    "churn_probability": "float",
    "churn_prediction": "\"Yes\" or \"No\"",
    "risk_level": "\"Low\" | \"Medium\" | \"High\"",
    "top_risk_factors": [
      {"factor": "string (feature name)", "value": "number"}
    ]
  },
  "eligible_actions": ["subset of APPROVED_ACTIONS"]
}
```

System prompt used verbatim in training:

> You are a banking retention analyst. Given a customer retention case, identify
> the most supported reason for risk, cite evidence, assign urgency, and select
> exactly one eligible retention action.

See `examples/model2_input_example.json` for a complete example.

---

## Model 2 Output Schema

```json
{
  "primary_reason": "one of APPROVED_REASONS",
  "secondary_reasons": ["zero or more of APPROVED_REASONS, excluding primary_reason"],
  "evidence": ["short strings citing specific field=value evidence"],
  "urgency": "LOW | MEDIUM | HIGH",
  "recommended_action": "one of APPROVED_ACTIONS, must be in eligible_actions",
  "reasoning_summary": "short free-text paragraph explaining the decision"
}
```

### Approved Value Lists

**APPROVED_REASONS**: `SERVICE_DISSATISFACTION`, `COMPETITOR_MIGRATION`,
`FEE_DISSATISFACTION`, `LOW_ENGAGEMENT`, `PRODUCT_MISMATCH`,
`DIGITAL_FRICTION`, `FINANCIAL_STRESS`, `LIFE_STAGE_CHANGE`,
`TEMPORARY_SEASONAL_CHANGE`, `UNKNOWN`

**APPROVED_ACTIONS**: `MONITOR`, `SERVICE_RECOVERY`, `COMPLAINT_ESCALATION`,
`FEE_WAIVER_REVIEW`, `RM_CALLBACK`, `PRODUCT_REVIEW`, `CARD_REVIEW`,
`LOAN_REVIEW`, `RE_ENGAGEMENT`, `FINANCIAL_GUIDANCE`

**APPROVED_URGENCY**: `LOW`, `MEDIUM`, `HIGH`

### Low-Confidence Fallback

When the model cannot determine a clear reason, it falls back to
`(UNKNOWN, MEDIUM, MONITOR)`. The notebook tracks this rate explicitly.

### Validation Rules

- `primary_reason` ∈ APPROVED_REASONS
- Each entry in `secondary_reasons` ∈ APPROVED_REASONS and ≠ `primary_reason`
- `urgency` ∈ APPROVED_URGENCY
- `recommended_action` ∈ APPROVED_ACTIONS **AND** `recommended_action` ∈ that
  record's `eligible_actions`

See `examples/model2_output_example.json` for a complete example.

---

## Model 1 → Model 2 Integration

Model 1 is a separate XGBoost component. Model 2 consumes these fields from
Model 1's output:

| Field | Type | Description |
|---|---|---|
| `churn_probability` | float | Predicted churn probability |
| `churn_prediction` | string | `"Yes"` or `"No"` |
| `risk_level` | string | `"Low"`, `"Medium"`, or `"High"` |
| `top_risk_factors` | list of objects | Each: `{"factor": "<feature name>", "value": <number>}` |

These map directly into the `model1` object of the input schema.

See `examples/model1_output_example.json` for a complete example.

### Stable ID Requirement

A stable identifier must travel through every stage — Model 1 → Model 2 →
clustering → dashboard — so results always trace back to the correct customer.
In the notebook's training/evaluation data, this identifier is `case_id`.
Your pipeline must maintain this tracing convention, though the exact column
name may differ in Model 1's raw output.

---

## Installation

```bash
# Clone the repository
git clone <repo-url>
cd model2-finetune-devang

# Create and activate a virtual environment (recommended)
python -m venv venv
source venv/bin/activate    # Linux/Mac
# or: venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt
```

**Requirements**: Python 3.10+, CUDA-capable GPU with ≥8 GB VRAM (for 4-bit
quantized inference).

---

## Obtaining the Base Model

The base model (`Qwen/Qwen2.5-3B-Instruct`) is downloaded automatically from
Hugging Face Hub on first run. No manual download is needed. If you are in a
restricted environment, you can pre-download it:

```bash
python -c "from transformers import AutoModelForCausalLM; AutoModelForCausalLM.from_pretrained('Qwen/Qwen2.5-3B-Instruct')"
```

---

## Loading the V2 Adapter

The V2 LoRA adapter (`model2_v2_finetuned`) is **not committed to Git** to keep
the repository lightweight. To set it up:

1. Obtain the adapter ZIP from the project's shared artifact location.
2. Extract it into the `model/model2_v2_finetuned/` directory.
3. Verify the adapter files are present (see
   `model/model2_v2_finetuned/ADAPTER_REFERENCE.md` for the file list).

Alternatively, if the adapter has been uploaded to Hugging Face Hub, update
`ADAPTER_PATH` in `src/config/settings.py` to the Hub repo id and it will be
downloaded automatically.

---

## Single-Record Inference

### Python API

```python
import json
from src.inference import Model2Engine

# Load model (downloads base model on first run)
engine = Model2Engine()

# Load an input record
with open("examples/model2_input_example.json") as f:
    case_input = json.load(f)

# Run inference
result = engine.predict(case_input)

if result["ok"]:
    print(json.dumps(result["parsed"], indent=2))
else:
    print(f"Error: {result['error']}")

# Free GPU memory when done
engine.unload()
```

### CLI

```bash
python scripts/run_inference.py --input examples/model2_input_example.json --output result.json
```

---

## Batch Inference

### Python API

```python
from src.inference import Model2Engine

engine = Model2Engine()
summary = engine.predict_batch(
    input_path="data/model2_inputs.jsonl",
    output_path="data/model2_outputs.jsonl",
    id_column="case_id",
)
print(summary)  # {"total": ..., "ok_count": ..., "error_count": ..., "mean_latency_s": ...}
engine.unload()
```

### CLI

```bash
python scripts/run_batch.py \
    --input data/model2_inputs.jsonl \
    --output data/model2_outputs.jsonl \
    --id-column case_id
```

Results are written incrementally (streaming) to avoid loading all outputs into
memory.

---

## Precomputed Demo Workflow

For the demo/prototype, the retention pipeline is precomputed offline:

1. **Run Model 1** on the customer population → produces churn predictions.
2. **Preprocess** → combine customer data + Model 1 output into Model 2 input
   JSONL (see `src/preprocessing/`).
3. **Run Model 2 batch inference** → produces structured retention analysis for
   each customer.
4. **Cluster** the Model 2 outputs by reason/urgency patterns.
5. **Store** the results for the dashboard to consume.

This is an offline, batch workflow. It is not a real-time inference service.

---

## Evaluation Results

See [`evaluation/RESULTS.md`](evaluation/RESULTS.md) for the complete evaluation
documentation. Summary of available results:

### V1 (checkpoint-145), 499-Case Test Set

*(Reused from a prior run, not re-executed in the notebook.)*

| Metric | Value |
|---|---|
| primary_reason_exact_match | 0.8557 |
| recommended_action_exact_match | 0.8918 |
| urgency_exact_match | 0.8697 |
| json_valid_rate | 0.9920 |

### V1 (checkpoint-145), Full 466-Case Validation Set

*(Loaded from a pre-computed results file, not re-executed in the notebook.)*

| Metric | Value |
|---|---|
| reason accuracy | 0.8562 |
| action accuracy | 0.8884 |
| urgency accuracy | 0.8970 |

### V1 vs V2, 100-Case Stratified Screening

*(Fresh V2 inference on 100 of 466 validation cases; V1 reused.)*

| Metric | V1 | V2 |
|---|---|---|
| Reason accuracy | 0.82 | 0.84 |
| Action accuracy | 0.85 | 0.85 |
| Urgency accuracy | 0.78 | 0.81 |
| JSON valid rate | 0.98 | 1.00 |
| Invalid action rate | 0.02 | 0.00 |

25/100 cases changed: 12 improvements, 8 regressions, 5 neutral.

### Unexecuted Evaluations

- **Full 466-case V2 validation**: Not evaluated in the current run.
- **499-case V2 test evaluation**: Not evaluated in the current run.

These evaluations need to be executed before V2 can be considered fully
benchmarked.

---

## Clustering / Dashboard Handoff

Model 2's structured output is designed to feed directly into downstream
clustering and dashboard components:

- The **primary_reason** and **urgency** fields enable grouping customers by
  retention risk category.
- The **evidence** list provides transparency for human reviewers.
- The **recommended_action** drives the retention workflow.
- The **stable identifier** (case_id) allows tracing each result back to the
  original customer through every pipeline stage.

The clustering and dashboard components are separate from this repository.

---

## Repository Structure

```
├── README.md
├── .gitignore
├── requirements.txt
├── src/
│   ├── inference/         # Single + batch inference using base model + V2 LoRA
│   ├── preprocessing/     # Build Model 2 input JSONL from Model 1 output + customer data
│   ├── schema/            # Input/output JSON schema + validation
│   └── config/            # Model id, adapter location, approved value lists, paths
├── notebooks/
│   └── model2_refinement_fresh_runtime_final.ipynb  # Reproducibility reference (unmodified)
├── model/
│   └── model2_v2_finetuned/   # Adapter reference doc (actual files obtained externally)
├── examples/
│   ├── model1_output_example.json
│   ├── model2_input_example.json
│   └── model2_output_example.json
├── evaluation/
│   └── RESULTS.md         # All available metrics with source/status labels
└── scripts/
    ├── run_inference.py   # Single-record inference CLI
    ├── run_batch.py       # Batch inference CLI
    └── validate_schema.py # Schema validation CLI
```

---

## Notebook Reference

The notebook (`notebooks/model2_refinement_fresh_runtime_final.ipynb`) is
included **unmodified** as a reproducibility/reference artifact. It documents
the complete V2 refinement process.

### Execution Status (from the notebook)

**Executed cells:**
- Dataset/schema validation (train=2,306, validation=466, test=499)
- Loading Qwen2.5-3B-Instruct + checkpoint-145 for inference only
- Loading V1's existing 499-case test metrics (reused, not re-run)
- V1 error analysis on the 499-case test results
- Deriving error patterns from the already-computed 466-case validation results
  file (loaded, not re-run)
- Building the 828-example refinement set
- A 5-step LoRA smoke test (no save)
- The full 828-example / 1-epoch refinement run (produced and saved the V2 adapter)
- Verifying the saved V2 adapter loads and diffing its weights vs checkpoint-145
- The 100-case V1-vs-V2 stratified screening

**Not executed (present as unrun cells):**
- The final 499-case test evaluation for V2
- The final V1-vs-V2 selection-decision cell
- The scorecard-saving cell
- The final packaged inference/demo function
- The final report cell

Standard inference does **not** depend on running the notebook.
