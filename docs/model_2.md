# Model 2 — Retention Reason & Action Recommendation

## What Model 2 Does

Model 1 tells you **who** is at risk. Model 2 tells you **why** and **what to do about it**.

Given a customer's profile, their recent behavioral signals, complaint history, and Model 1's churn prediction — Model 2 produces a structured decision:

| Question | Example Answer |
|---|---|
| **Why is this customer at risk?** | `SERVICE_DISSATISFACTION` — unresolved complaints + slow resolution |
| **How urgent is it?** | `HIGH` — needs action within 24–48 hours |
| **What should the bank do?** | `COMPLAINT_ESCALATION` — escalate to senior branch manager |
| **What's the evidence?** | `unresolved_complaints=2`, `avg_resolution_time_hrs=74.5` |

All outputs are **structured JSON**, validated against strict approved taxonomy lists. No free-form guesswork.

---

## How It Works (Simple Version)

```
 Customer Profile + Behavioral Deltas + Complaint Text
                    +
          Model 1 Churn Output
          (probability, risk level, top SHAP factors)
                    +
          Eligible Actions List
                    │
                    ▼
  ┌──────────────────────────────────────────┐
  │  Fine-Tuned LLM                          │
  │  Base: Qwen2.5-3B-Instruct              │
  │  Adapter: model2_v2_finetuned (LoRA)     │
  │                                          │
  │  System Prompt: "You are a banking       │
  │  retention analyst..."                   │
  │                                          │
  │  + Decision Rules for evidence,          │
  │    urgency, reason routing,              │
  │    and action selection                  │
  └──────────────────────────────────────────┘
                    │
                    ▼
         JSON Schema Validator
         (checks reason, action, urgency
          against approved lists)
                    │
                    ▼
         Structured Output:
         {
           "primary_reason": "SERVICE_DISSATISFACTION",
           "urgency": "HIGH",
           "recommended_action": "COMPLAINT_ESCALATION",
           "evidence": ["unresolved_complaints=2", ...],
           "reasoning_summary": "Customer faced..."
         }
```

---

## The Model Behind It

| Detail | Value |
|---|---|
| Base Model | `Qwen/Qwen2.5-3B-Instruct` (3 billion parameters) |
| Fine-Tuning Method | LoRA (Low-Rank Adaptation) — only adapts ~0.5% of weights |
| LoRA Rank | 16 |
| LoRA Alpha | 32 |
| LoRA Dropout | 0.05 |
| Selected Adapter | `model2_v2_finetuned` (V2 — the production version) |
| Quantized Formats | GGUF Q4_K_M (for Ollama local), FP16 (for GPU inference) |
| Context Window | 2,048 tokens |

---

## V1 → V2: Why a Second Version Was Needed

The first fine-tuned model (V1, `checkpoint-145`) worked well overall, but detailed error analysis on 466 validation cases revealed specific failure patterns:

| Problem Found in V1 | What Went Wrong | How V2 Fixed It |
|---|---|---|
| `PRODUCT_MISMATCH` recall was only 43% | Model kept leaking these into 3+ other reason classes | 276 targeted correction examples included |
| `UNKNOWN` recall was only 44% | Model over-assigned specific reasons when evidence was truly ambiguous | Explicit ambiguous-case training examples |
| `HIGH` urgency downgraded to `MEDIUM` in 8.2% of cases | Model was too conservative on urgency | Urgency boundary examples added |
| `MONITOR` action recall was only 60% | Model over-escalated passive accounts to `SERVICE_RECOVERY` | Action calibration examples included |

### V2 Training Details

- **Training Data:** 828 curated examples (276 targeted corrections + 552 anchor cases from original training set)
- **Training Method:** Custom PyTorch loop (not HuggingFace Trainer)
- **Duration:** 1 epoch, 104 optimizer steps
- **Learning Rate:** 4 × 10⁻⁵
- **Final Loss:** 0.01828
- **All 504 LoRA tensors changed** vs V1; max weight change was 2.394 × 10⁻³

---

## What Goes In (Input)

Model 2 receives a structured JSON payload with four sections:

### 1. Customer Context
```json
{
  "age": 42,
  "tenure_months": 54,
  "customer_segment": "salary",
  "income_regularity": "regular",
  "customer_yearly_value": 48500.0,
  "products_count": 3,
  "has_credit_card": 1,
  "has_loan": 1
}
```

### 2. Recent Behavior (30-Day Deltas)
```json
{
  "days_since_last_transaction": 19,
  "balance_change_30d": -35.0,
  "transaction_change_30d": -28.0,
  "card_spend_change_30d": -34.0,
  "app_login_change_30d": -15.0,
  "salary_missing_days": 4,
  "external_transfer_change_30d": 44.0,
  "upi_share_of_spend": 0.65,
  "fd_maturing_in_30d": 0,
  "products_dropped_90d": 0,
  "emi_bounce_30d": 0
}
```

### 3. Service Evidence
```json
{
  "complaints_30d": 2,
  "unresolved_complaints": 2,
  "failed_transactions_30d": 1,
  "avg_resolution_time_hrs": 74.5,
  "complaint_text": "ATM debited my account but did not dispense cash. Branch executive did not resolve."
}
```

### 4. Model 1 Output
```json
{
  "churn_probability": 34.82,
  "churn_prediction": "Yes",
  "risk_level": "High",
  "top_risk_factors": [
    {"factor": "latest_days_since_last_transaction", "value": 19.0},
    {"factor": "latest_balance_change_30d", "value": -35.0},
    {"factor": "latest_external_transfer_change_30d", "value": 44.0}
  ]
}
```

Plus an **`eligible_actions`** list — the set of retention actions available for this customer:
```json
["COMPLAINT_ESCALATION", "SERVICE_RECOVERY", "RM_CALLBACK", "MONITOR"]
```

---

## What Comes Out (Output)

```json
{
  "primary_reason": "SERVICE_DISSATISFACTION",
  "secondary_reasons": ["COMPETITOR_MIGRATION"],
  "evidence": [
    "unresolved_complaints=2",
    "avg_resolution_time_hrs=74.5",
    "external_transfer_change_30d=44.0",
    "balance_change_30d=-35.0"
  ],
  "urgency": "HIGH",
  "recommended_action": "COMPLAINT_ESCALATION",
  "reasoning_summary": "Customer faced 2 unresolved complaints with a prolonged 74.5-hour turnaround and an unresolved ATM cash dispute. Funds are actively moving to other institutions (+44.0% transfer increase). Urgent management escalation is required to rectify the service failure and retain the account."
}
```

---

## Approved Taxonomies

Model 2 can ONLY output values from these pre-approved lists. Anything else is rejected.

### 10 Approved Churn Reasons

| Reason Code | When It Applies | Real-World Signal |
|---|---|---|
| `SERVICE_DISSATISFACTION` | Bad customer service, slow complaint resolution | `unresolved_complaints > 0` + `avg_resolution_time_hrs ≥ 48` |
| `FINANCIAL_STRESS` | Cash flow problems, missed salary, bounced EMI | `salary_missing_days > 0` + `emi_bounce_30d = 1` |
| `DIGITAL_FRICTION` | App glitches, failed UPI, login issues | `failed_transactions_30d > 0` + `app_login_change_30d < -20%` |
| `FEE_DISSATISFACTION` | Unhappy with bank charges and penalties | Complaint text mentions fees/charges |
| `COMPETITOR_MIGRATION` | Moving money to a rival bank | `external_transfer_change_30d > 0` + `balance_change_30d < 0` |
| `LOW_ENGAGEMENT` | Just stopped using banking services | `days_since_last_transaction` high + `transaction_change_30d < 0` |
| `PRODUCT_MISMATCH` | Wrong account/product for their needs | `products_dropped_90d > 0` + mismatched credit limits |
| `LIFE_STAGE_CHANGE` | Retirement, relocation, career shift | Drastic behavior pattern changes |
| `TEMPORARY_SEASONAL_CHANGE` | Normal cyclical dip (e.g., farmer's lean season) | Seasonal segment with recovering indicators |
| `UNKNOWN` | Genuinely ambiguous — no clear signal | Fallback when nothing above is supported |

### 10 Approved Retention Actions

| Action Code | What the Bank Actually Does | Typical Target |
|---|---|---|
| `COMPLAINT_ESCALATION` | Fast-track to senior branch manager | Unresolved complaints > 48 hours |
| `SERVICE_RECOVERY` | Apology outreach + resolution package | Severe service delays |
| `RM_CALLBACK` | Relationship Manager phone call | High-value, long-tenure customers |
| `FEE_WAIVER_REVIEW` | Refund or waive disputed charges | Fee complaints |
| `FINANCIAL_GUIDANCE` | Restructure EMI, provide overdraft grace | Missed salary, bounced EMIs |
| `RE_ENGAGEMENT` | Promotional offers, cashback, feature demos | Inactive digital users |
| `PRODUCT_REVIEW` | Migrate to a better-suited account type | Mismatched product tier |
| `CARD_REVIEW` | Credit limit adjustment, tier upgrade | High UPI spend replacing card use |
| `LOAN_REVIEW` | Rate concession, top-up loan offer | FD maturing, potential borrower |
| `MONITOR` | Watch and wait — no intrusive outreach | Low risk, mixed/unclear signals |

### 3 Urgency Levels

| Urgency | Trigger Conditions | Bank Response Time |
|---|---|---|
| **HIGH** | Model 1 risk = High, OR unresolved complaints + slow resolution (≥48 hrs), OR bounced EMI + missing salary | Same day / 24–48 hours |
| **MEDIUM** | Everything that doesn't qualify as HIGH or LOW | Within 7 business days |
| **LOW** | Model 1 risk = Low AND all service fields are zero AND no behavior worse than -20% | Routine monitoring |

---

## Evaluation Results

All benchmarks come from the official evaluation documented in `devangs_fine_tuned/evaluation/RESULTS.md`.

### V1 (checkpoint-145) — 499-Case Test Set

| Metric | Value |
|---|---|
| Primary reason exact match | **85.57%** |
| Recommended action exact match | **89.18%** |
| Urgency exact match | **86.97%** |
| JSON valid rate | **99.20%** |
| Invalid/hallucinated action rate | **0.00%** |
| Mean inference latency | 17.71 seconds |

### V1 — 466-Case Validation Set (by Risk Level)

| Risk Level | n | Reason Accuracy | Action Accuracy | Urgency Accuracy |
|---|---|---|---|---|
| Low | 247 | 78.14% | 82.59% | 88.26% |
| Medium | 87 | 93.10% | 93.10% | 91.95% |
| High | 132 | 94.70% | 97.73% | 90.91% |

### V1 vs V2 — 100-Case Stratified Screening

| Metric | V1 | V2 (Production) |
|---|---|---|
| Reason accuracy | 82% | **84%** ✓ |
| Action accuracy | 85% | **85%** |
| Urgency accuracy | 78% | **81%** ✓ |
| JSON valid rate | 98% | **100%** ✓ |
| Invalid action rate | 2% | **0%** ✓ |

Of 100 cases: 12 improved, 8 regressed, 5 neutral changes.

> **Note:** Full 466-case and 499-case V2 evaluations have not yet been completed. The 100-case screening is a preliminary directional signal.

---

## System Prompt Used During Training & Inference

```
You are a banking retention analyst. Given a customer retention case, identify
the most supported reason for risk, cite evidence, assign urgency, and select
exactly one eligible retention action.
```

This exact text was used verbatim in all training data and is injected as the system message during inference.
