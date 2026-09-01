# Backend — Model Serving & API Architecture

## Why the Backend Exists

The Flask dashboard shows **precomputed** results from the SQLite database. But someone has to **run the models** to generate those results in the first place. That's the backend's job.

The backend serves two purposes:
1. **Batch preprocessing** — Score all 10,000 customers through Model 1 and Model 2 offline, then store results in JSON files → database.
2. **Live inference API** — Accept a single customer's data via HTTP, run Model 1 and/or Model 2 in real time, and return a prediction (used for demos, testing, and real-time use cases).

---

## Backend Files

```
backend/
├── retention_api_server.py       # Main FastAPI server (Port 8000)
│                                  #   Runs Model 1 (XGBoost) + Model 2 (LLM) together
│                                  #   Can use Ollama or llama-cpp-python for Model 2
│
├── devang_api_server.py           # Dedicated Model 2 FastAPI server (Port 8001)
│                                  #   Optimized for Ollama backend only
│                                  #   Includes decision rules & prompt injection
│
├── colab_api.ipynb                # Google Colab notebook
│                                  #   Runs models on free cloud GPU (T4/A100)
│                                  #   Exposes API via ngrok tunnel
│
├── model1_batch_outputs.py        # Batch inference script for Model 1
│                                  #   Processes all 10k customers sequentially
│
├── export_model1_outputs_json.py  # Serializer for Model 1 JSON output payloads
│
├── model2_recovery_schemas.json   # Fallback schema definitions (~18 KB)
│                                  #   Used to self-correct malformed LLM responses
│
└── outputs/                       # (Directory for batch run results)
```

---

## How Model 2 Inference Works (Step by Step)

When the backend receives a customer case for Model 2 analysis:

```
1. Validate input JSON against schema
   (checks all required fields, approved enum values)
        │
2. Select 3–5 eligible actions based on customer profile
   (e.g., COMPLAINT_ESCALATION only if complaints exist)
        │
3. Construct full prompt:
   System Prompt + Decision Rules + Customer Case JSON
        │
4. Send to Ollama (local) or llama-cpp-python (direct)
   Model: devang-model2-q4 (GGUF Q4_K_M quantized)
   Temperature: 0.3, Top-P: 0.9, Repeat Penalty: 1.08
        │
5. Parse LLM response → extract JSON block
        │
6. Validate output:
   • primary_reason ∈ APPROVED_REASONS?
   • recommended_action ∈ APPROVED_ACTIONS?
   • recommended_action ∈ eligible_actions for this customer?
   • urgency ∈ {HIGH, MEDIUM, LOW}?
   • UNKNOWN not in secondary_reasons?
   • Evidence items cite real field=value from the case?
        │
7. If validation fails → retry (up to 3 attempts)
   If all retries fail → use recovery schema fallback
        │
8. Return structured JSON response
```

---

## Exact Prompts Used by Model 2

### System Prompt

This exact text is used in training data and during all inference calls:

```
You are a banking retention analyst. Given a customer retention case, identify
the most supported reason for risk, cite evidence, assign urgency, and select
exactly one eligible retention action.
```

### Decision Rules (Injected After System Prompt)

These rules constrain the LLM's reasoning to prevent hallucinations and ensure compliance:

**Evidence Rules:**
- Every evidence item must be `field=value` copied **verbatim** from the customer case. Never flip a sign, never round toward a worse value, never invent a field.
- Only cite **non-zero, non-null** signals. A field equal to 0 or null is the ABSENCE of evidence.
- Never cite your own output fields as evidence.
- `model1.top_risk_factors` lists the features that INCREASED churn risk, ordered strongest first. Look each one up in the case data and cite the actual value.

**Urgency Rules** (check HIGH first, then LOW, then fall through to MEDIUM):
- **HIGH:** `model1.risk_level` is `"High"`, OR `unresolved_complaints > 0` AND `avg_resolution_time_hrs ≥ 48`, OR `emi_bounce_30d > 0` AND `salary_missing_days > 0`.
- **LOW:** `model1.risk_level` is `"Low"` AND every service field is 0/null AND no behavior dropped worse than -20%.
- **MEDIUM:** Everything else. Do not default to MEDIUM without ruling out HIGH and LOW.

**Action Rules:**
- When risk is High or prediction is "Yes", `MONITOR` is NOT acceptable unless every service field is 0 and no behavior is alarming.
- `eligible_actions` is the final authority. If the ideal action isn't available, pick the closest lower-severity eligible action.
- `MONITOR` only as last resort.

**Reason Routing:**
| If the evidence shows... | Assign reason... |
|---|---|
| Fees, charges, penalties wrongly levied | `FEE_DISSATISFACTION` |
| Repeat complaints, no callback, slow fix | `SERVICE_DISSATISFACTION` |
| App/UPI/login failures, failed transactions | `DIGITAL_FRICTION` |
| EMI vs salary timing, bounces, missed salary | `FINANCIAL_STRESS` |
| Funds leaving (`external_transfer > 0` AND `balance < 0`) | `COMPETITOR_MIGRATION` |
| Inactivity: high `days_since_last_transaction` + drops in txns/logins | `LOW_ENGAGEMENT` |
| Product doesn't fit customer's cashflow | `PRODUCT_MISMATCH` |
| Seasonal/cyclical dip that's already recovering | `TEMPORARY_SEASONAL_CHANGE` |
| No reason above is supported by any non-zero signal | `UNKNOWN` |

**Coherence Constraints:**
- `UNKNOWN` must never appear in `secondary_reasons`.
- If `primary_reason` is `UNKNOWN`, `secondary_reasons` must be empty.
- `secondary_reasons` must never repeat `primary_reason`.
- `reasoning_summary` must name the action actually chosen and quote specific evidence values.

---

## API Endpoints

### `retention_api_server.py` (Port 8000)

| Method | Endpoint | What It Does |
|---|---|---|
| `POST` | `/predict/model1` | Run Model 1 only → churn probability + SHAP factors |
| `POST` | `/predict/model2` | Run Model 2 only → reason + action + evidence |
| `POST` | `/predict/full` | End-to-end: Model 1 → construct Model 2 input → Model 2 → unified response |
| `GET` | `/health` | Check model artifact readiness and Ollama connectivity |

### `devang_api_server.py` (Port 8001)

Dedicated high-concurrency Model 2 server. Same schema validation and retry logic, optimized for Ollama backend with the `devang-model2-q4` model.

---

## Running Models Locally

### Option A: Local Ollama (Recommended)

1. Install [Ollama](https://ollama.com/)
2. Create the model from the GGUF file:
   ```powershell
   ollama create retention-0.5bv2 -f Modelfile
   ```
3. Start the backend:
   ```powershell
   python backend/retention_api_server.py
   ```

The `Modelfile` in the repo root configures:
```
FROM "model_2/model 2 demo/model2_retention_0.5bv2.gguf"
PARAMETER temperature 0.3
PARAMETER top_p 0.9
PARAMETER repeat_penalty 1.08
```

### Option B: Google Colab (Free GPU)

Open `backend/colab_api.ipynb` in Google Colab:
1. Mounts Google Drive for model artifacts
2. Installs FastAPI + llama-cpp-python with CUDA
3. Starts ngrok tunnel → gives you a public HTTPS URL
4. Paste that URL into local config to use cloud GPU for batch processing

This is useful when you don't have a local GPU but need to process thousands of customers through Model 2.
