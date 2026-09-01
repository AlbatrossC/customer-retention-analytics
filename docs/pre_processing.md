# Preprocessing & Batch Processing Pipeline

## What This Module Does

In production, you don't run Model 1 and Model 2 on-the-fly for every dashboard page load. Instead, you **precompute everything offline** in batch:

1. Score all 10,000 customers through Model 1 → get churn probabilities
2. Take the high-risk and medium-risk customers → run them through Model 2 → get reasons and actions
3. Store all results in JSON files → load into the SQLite database

The Flask dashboard then reads directly from the pre-populated database, giving instant response times.

---

## Pipeline Flow

```
model_1_v2/data/customers.csv  (10,000 customers × 6 months)
                │
                │  run_model_1_v2.py
                │  (Loads XGBoost model, builds features, runs SHAP)
                ▼
outputs/model_1_v2_customer_outputs.json  ← All 10,000 scored
                │
                │  Filters: risk_level = "High" or "Medium"
                │
        ┌───────┴──────────────────────┐
        │                              │
        ▼                              ▼
run_devang_pipeline.py          run_top_low_risk_pipeline.py
(High + Medium risk)            (Top 10% of Low risk)
        │                              │
        ▼                              ▼
remaining_high_medium_risk_     top_low_risk_customers.json
customers.json                  (688 borderline low-risk)
(3,115 customers)                      │
        │                              │
        └──────────────┬───────────────┘
                       │
                       ▼
              database/build_db.py
              database/insert_low_risk_model2.py
                       │
                       ▼
              customer_retention.db  (ready for dashboard)
```

---

## Preprocessing Scripts

| Script | What It Does | Customers Processed | Approx. Runtime |
|---|---|---|---|
| `run_model_1_v2.py` | Runs Model 1 (XGBoost ensemble + SHAP) on every customer. Computes calibrated churn probability, risk tier, and top 5 risk factors. | All **10,000** | ~16 minutes |
| `run_devang_pipeline.py` | Runs Model 2 (LLM via Ollama) on High and Medium risk customers. Uses 6 parallel worker threads. | **3,115** (High + Medium) | ~1.9 hours |
| `run_top_low_risk_pipeline.py` | Runs Model 2 on the top 10% highest-probability customers within the Low Risk band (early warning tier). | **688** (borderline Low) | ~1.1 hours |
| `run_05b_v2_pipeline.py` | Alternative pipeline using the 0.5B quantized GGUF model for low-compute environments. | Configurable | Varies |

---

## Output Files — Detailed Breakdown

All output files are stored in `pre_processing/outputs/`. These are the source-of-truth data that gets loaded into the database.

### 1. `model_1_v2_customer_outputs.json`

**Size:** ~59.9 MB | **Created:** 2026-08-31 at 17:34

Model 1 XGBoost predictions and top 5 SHAP risk factors for the **entire customer base**.

| Stat | Value |
|---|---|
| Total customers processed | **10,000** |
| Success rate | **100%** (0 failures) |
| Processing time | 940 seconds (~15.6 minutes) |

**Risk Distribution:**

| Risk Level | Count | Percentage |
|---|---|---|
| 🔴 **High Risk** | **2,142** | 21.4% |
| 🟡 **Medium Risk** | **973** | 9.7% |
| 🟢 **Low Risk** | **6,885** | 68.9% |

**What each customer record contains:**
- `customer_id`
- `churn_probability` (sigmoid-calibrated percentage)
- `raw_churn_probability` (raw XGBoost output)
- `risk_score` (0–100 composite score)
- `churn_prediction` ("Yes" or "No")
- `risk_level` ("High", "Medium", or "Low")
- `top_risk_factors` (5 items, each with factor name, value, SHAP contribution, and human-readable message)

---

### 2. `devang_model2_pipeline_outputs.json`

**Size:** ~35.9 MB | **Created:** 2026-08-31 at 19:42

First batch of Model 2 LLM reasoning, covering the initial half of the high/medium risk cohort.

| Stat | Value |
|---|---|
| Customers selected | **1,558** |
| Success rate | **100%** (0 failures) |
| Skipped (low risk) | 3,442 |
| Processing time | 6,824 seconds (~1.9 hours, 6 workers) |
| Breakdown | 1,071 High + 487 Medium |

---

### 3. `remaining_high_medium_risk_customers.json`

**Size:** ~71.7 MB | **Created:** 2026-08-31 at 22:23

The **complete** Model 2 output covering **ALL** High and Medium risk customers (including the 1,558 from the first batch).

| Stat | Value |
|---|---|
| Total in scope | **3,115** |
| Successfully processed | **3,115** (100%) |
| Skipped (already processed in batch 1) | 1,558 |
| Processing time | 6,937 seconds (~1.9 hours, 6 workers) |
| Breakdown | 2,142 High + 973 Medium |

**This file contains:**
- All fields from `devang_model2_pipeline_outputs.json` plus:
- `primary_reason`, `secondary_reasons`, `evidence[]`, `urgency`, `recommended_action`, `reasoning_summary`
- Full raw LLM response text (for debugging)

---

### 4. `top_low_risk_customers.json`

**Size:** ~15.8 MB | **Created:** 2026-09-01 at 23:45

Model 2 intelligence for **borderline low-risk customers** — the top 10% with the highest churn probability within the Low Risk band.

| Stat | Value |
|---|---|
| Customers selected | **688** |
| Success rate | **100%** (0 failures) |
| Processing time | 3,998 seconds (~1.1 hours, 6 workers) |
| Tier description | "Tier 5 Low Risk (Top 10% highest churn probability in Low Risk)" |

These are customers the model flagged as technically "Low Risk" but who are closest to the Medium threshold — catching them early before they drift into higher risk.

---

## Aggregate Statistics Across All Output Files

After all preprocessing runs, the database contains **3,803 customers** analyzed by Model 2.

### What's Making Customers Leave? (Primary Reason Distribution)

| Reason | Count | Share | Interpretation |
|---|---|---|---|
| `SERVICE_DISSATISFACTION` | **2,127** | 55.9% | More than half of at-risk customers are frustrated with service quality |
| `FINANCIAL_STRESS` | **798** | 21.0% | 1 in 5 at-risk customers face cashflow issues (salary delays, bounced EMIs) |
| `DIGITAL_FRICTION` | **332** | 8.7% | App crashes, UPI failures, login problems |
| `FEE_DISSATISFACTION` | **283** | 7.4% | Unhappy with charges, penalties, minimum balance fines |
| `UNKNOWN` | **200** | 5.3% | Genuinely ambiguous — model correctly says "I don't know" |
| `COMPETITOR_MIGRATION` | **26** | 0.7% | Actively moving money to rival banks |
| `PRODUCT_MISMATCH` | **26** | 0.7% | Wrong account type for their needs |
| `TEMPORARY_SEASONAL_CHANGE` | **6** | 0.2% | Normal cyclical dip (e.g., farmer off-season) |
| `LOW_ENGAGEMENT` | **5** | 0.1% | Just stopped using the bank entirely |

### What Should the Bank Do? (Recommended Action Distribution)

| Action | Count | Share | Who Handles It |
|---|---|---|---|
| `COMPLAINT_ESCALATION` | **1,623** | 42.7% | Senior Branch Escalation Cell |
| `FINANCIAL_GUIDANCE` | **719** | 18.9% | Credit & Loan Advisory Desk |
| `SERVICE_RECOVERY` | **708** | 18.6% | Customer Experience & Care Unit |
| `RE_ENGAGEMENT` | **260** | 6.8% | Digital Marketing & CRM Team |
| `MONITOR` | **254** | 6.7% | Automated Watchlist Queue |
| `FEE_WAIVER_REVIEW` | **108** | 2.8% | Operations / Billing Approvals |
| `PRODUCT_REVIEW` | **68** | 1.8% | Account Portfolio Managers |
| `RM_CALLBACK` | **39** | 1.0% | Dedicated Relationship Managers |
| `LOAN_REVIEW` | **23** | 0.6% | Retail Lending Officers |
| `CARD_REVIEW` | **1** | <0.1% | Cards & Rewards Team |

### How Urgent Is It? (Urgency Distribution)

| Urgency | Count | Share | Response Window |
|---|---|---|---|
| 🔴 **HIGH** | **1,109** | 29.2% | Immediate — same day or 24–48 hours |
| 🟡 **MEDIUM** | **2,479** | 65.2% | Within 7 business days |
| 🟢 **LOW** | **215** | 5.7% | Routine monitoring |

---

## How to Run the Full Pipeline

```powershell
# 1. Score all 10,000 customers through Model 1
python pre_processing/run_model_1_v2.py

# 2. Run Model 2 on High + Medium risk customers (requires Ollama running)
python pre_processing/run_devang_pipeline.py

# 3. (Optional) Run Model 2 on borderline Low Risk customers
python pre_processing/run_top_low_risk_pipeline.py

# 4. Build the SQLite database from JSON outputs
python database/build_db.py

# 5. (Optional) Add low-risk Model 2 results to database
python database/insert_low_risk_model2.py

# 6. Verify everything loaded correctly
python database/check_db.py
```

> **Prerequisites:** Model 1 requires the XGBoost model artifacts in `model_1_v2/training_scripts/xgboost_model1_v2/artifacts/`. Model 2 requires Ollama running with the `retention-0.5bv2` or `devang-model2-q4` model loaded.
