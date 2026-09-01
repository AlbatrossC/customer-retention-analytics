# Model 1 (v2) — Churn Risk Prediction

## What Model 1 Does

Model 1 answers one question:

> **"Is this customer likely to churn next month?"**

It looks at each customer's banking behavior over the past 3–6 months — their transaction frequency, balance trends, app usage, complaints, salary deposits, transfers to other banks — and predicts a **churn probability** between 0% and 100%.

It also explains **why** it thinks so, by showing the top 5 features (risk factors) that pushed the prediction toward churn using SHAP values.

---

## How It Works (Simple Version)

```
Step 1: Take raw monthly snapshots from customers.csv (up to 6 months per customer)
           │
Step 2: Engineer 69 time-aware features
        (rolling averages, trends, drop counts, max spikes over 3M and 6M)
           │
Step 3: Feed into XGBoost (gradient-boosted decision trees)
        Three models trained with different random seeds → average their predictions
           │
Step 4: Calibrate raw probability using a sigmoid calibrator
        (makes the numbers match real-world churn rates)
           │
Step 5: Classify into risk tier:
        • Probability ≥ 25%  → HIGH risk
        • 12% ≤ Prob < 25%   → MEDIUM risk
        • Probability < 12%  → LOW risk
           │
Step 6: Run SHAP TreeExplainer to find the top 5 features
        driving each customer's risk score
```

---

## What Goes In (Input)

For each customer, the model receives their **profile** and **time-series snapshots**:

**Profile fields used:**
- `tenure_months` — how long they've been a customer
- `customer_segment` — salary / pension / farmer / vendor / business
- `income_regularity` — regular / irregular / seasonal
- `products_count`, `has_credit_card`, `has_loan`

**Monthly behavioral fields (per snapshot):**
- `days_since_last_transaction`, `balance_change_30d`, `transaction_change_30d`
- `card_spend_change_30d`, `app_login_change_30d`, `salary_missing_days`
- `external_transfer_change_30d`, `upi_share_of_spend`, `fd_maturing_in_30d`
- `products_dropped_90d`, `complaints_30d`, `unresolved_complaints`
- `failed_transactions_30d`, `avg_resolution_time_hrs`, `emi_bounce_30d`

**Fields explicitly BLOCKED** (to prevent data leakage or bias):
- `customer_id`, `customer_name`, `snapshot_date` (would cause memorization)
- `churn_flag` (that's the answer — obviously can't use it)
- `loyalty`, `customer_yearly_value` (hidden simulation variables)
- `complaint_text` (reserved for Model 2's LLM reasoning)
- `age`, `branch_code`, `card_colour` (fairness / deliberate noise decoys)

---

## What Comes Out (Output)

For every customer, Model 1 produces:

```json
{
  "customer_id": "C10015",
  "churn_probability": 34.82,
  "raw_churn_probability": 68.45,
  "probability_mode": "sigmoid",
  "risk_score": 78.4,
  "churn_prediction": "Yes",
  "risk_level": "High",
  "top_risk_factors": [
    {
      "factor_rank": 1,
      "factor_name": "latest_days_since_last_transaction",
      "factor_value": 19.0,
      "factor_message": "Customer has gone longer without transacting (19 days).",
      "contribution": 0.842
    },
    {
      "factor_rank": 2,
      "factor_name": "latest_balance_change_30d",
      "factor_value": -35.0,
      "factor_message": "Severe account balance drop in the last 30 days (-35.0%).",
      "contribution": 0.615
    }
  ]
}
```

| Output Field | What It Means |
|---|---|
| `churn_probability` | Calibrated churn chance, e.g., `34.82` = 34.82% chance of leaving next month |
| `raw_churn_probability` | Raw XGBoost output before sigmoid calibration (higher range, used internally) |
| `probability_mode` | Calibration method applied. Currently `sigmoid` |
| `risk_score` | Composite 0–100 risk score |
| `churn_prediction` | Binary: `"Yes"` (will likely churn) or `"No"` |
| `risk_level` | Business tier: `"High"`, `"Medium"`, or `"Low"` |
| `top_risk_factors` | Top 5 SHAP-ranked features with human-readable messages |

---

## Risk Level Thresholds

| Risk Level | Calibrated Probability | Customers in DB | % of Total | What the Bank Does |
|---|---|---|---|---|
| **High** | ≥ 25% | **2,142** | 21.4% | Immediate outreach — RM callback, complaint escalation, priority action |
| **Medium** | 12% to 25% | **973** | 9.7% | Proactive engagement — fee reviews, guidance, re-engagement campaigns |
| **Low** | < 12% | **6,885** | 68.9% | Routine monitoring — automated nurture tracks |

---

## The 69 Engineered Features

The model doesn't see raw monthly snapshots directly. Instead, a feature engineering pipeline (`build_features.py`) computes **69 signals** across three time horizons:

### Latest 30-Day Snapshot (15 features)
The most recent month's values. Example: `latest_days_since_last_transaction`, `latest_balance_change_30d`, `latest_complaints_30d`.

### 3-Month Rolling Aggregates (18 features)
Averages, maximums, and cumulative sums over the last 3 months. Example: `avg_balance_change_30d_3m`, `max_salary_missing_days_3m`, `sum_complaints_30d_3m`.

### 6-Month Rolling Aggregates (18 features)
Same statistics but over the full 6-month history. Example: `avg_transaction_change_30d_6m`, `sum_failed_transactions_30d_6m`.

### Drop/Spike Counters (11 features per window)
How many months in a row a metric moved in a bad direction. Example: `count_balance_drop_3m` (number of months with negative balance growth in the last 3 months).

### Trend Slopes (7 features)
Linear regression slope over available monthly history. Example: `balance_change_30d_trend_6m` — is the balance consistently falling month-over-month?

### Latest vs. Historical Average (6 features)
Is this month **worse than their own average**? Example: `latest_vs_avg_balance_change_30d_available_history`.

---

## Training Configuration

| Parameter | Value |
|---|---|
| Algorithm | XGBoost (`binary:logistic`) |
| Tree method | `hist` (histogram-based, fast) |
| Evaluation metric | PR-AUC (`aucpr`) — the right metric for rare events |
| Ensemble | 3 models with seeds `42`, `7`, `13` → averaged |
| Max tree depth | 4 (prevents overfitting) |
| Number of trees | 1,200 per model |
| Learning rate | 0.03 |
| Class weight | `scale_pos_weight = 14.19` (compensates for 6% churn imbalance) |
| Regularization | L1 = 0.1, L2 = 2.5, gamma = 0.2 |
| Subsample | 90% of rows, 85% of columns per tree |
| Calibration | Sigmoid (post-hoc via `calibrator_v2.joblib`) |

---

## Evaluation Results

### Why NOT to Report Accuracy

With only ~6% churn, a model that says "nobody will churn" scores **94% accuracy** while catching **zero** departing customers. That's useless.

Instead, we focus on **ROC-AUC**, **PR-AUC**, and **Recall** — metrics that actually measure ability to identify rare churners.

### Metrics on the Test Set (1,448 customers, 6,417 rows)

**Sigmoid-calibrated probability (production mode):**

| Metric | Value | What It Means |
|---|---|---|
| **ROC-AUC** | **0.7802** | 78% chance a true churner is ranked higher than a non-churner |
| **PR-AUC** | **0.2929** | ~4.5× better than random guessing baseline (0.066) |
| **Accuracy** | **85.10%** | Overall correct rate (including true negatives) |
| **Precision** | **24.00%** | Of those flagged as churning, 24% actually churned |
| **Recall** | **57.65%** | Of actual churners, 57.65% were correctly identified |

**Validation set (for hyperparameter selection):**

| Metric | Value |
|---|---|
| Best Model PR-AUC | **0.3631** |
| Validation ROC-AUC | **0.8326** |
| Sigmoid Precision | 22.67% |
| Sigmoid Recall | 55.87% |

> **Note:** The raw (uncalibrated) model achieves 100% recall on both validation and test sets (every churner is flagged), but at very low precision (~6.5%). The sigmoid calibrator trades some recall for much higher precision, producing actionable risk tiers where the High-risk queue contains genuinely high-conviction cases.

---

## SHAP Explainability

Model 1 is **not** a black box. For every prediction, SHAP (SHapley Additive exPlanations) calculates how much each of the 69 features contributed to the churn score — positively or negatively.

The top 5 positive contributors are extracted and shown to bank officers with human-readable labels:

| Internal Feature Name | Dashboard Label |
|---|---|
| `latest_days_since_last_transaction` | Prolonged Account Inactivity (Days) |
| `latest_balance_change_30d` | Severe Account Balance Drop (30D) |
| `avg_external_transfer_change_30d_3m` | Avg External Outflow Delta (3-Month) |
| `sum_unresolved_complaints_3m` | Unresolved Escalated Complaints (3M) |
| `latest_salary_missing_days` | Delayed Salary / Income Inflow |

This means a branch manager sees **"Prolonged Account Inactivity (19 days)"** instead of `latest_days_since_last_transaction = 19`.

---

## How to Retrain Model 1

From the repository root:

```powershell
# Step 1: Build the 69-feature training table
python model_1_v2\training_scripts\xgboost_model1_v2\build_features.py

# Step 2: Train the XGBoost ensemble
python model_1_v2\training_scripts\xgboost_model1_v2\train_xgboost_v2.py

# Step 3: (Optional) Diagnose probability calibration
python model_1_v2\training_scripts\xgboost_model1_v2\diagnose_probabilities_v2.py

# Step 4: (Optional) Run a sample prediction
python model_1_v2\training_scripts\xgboost_model1_v2\test_prediction_v2.py
```

Trained model artifacts are saved to:
```
model_1_v2/training_scripts/xgboost_model1_v2/artifacts/
├── xgboost_model_v2.json         # Primary model (seed 42)
├── xgboost_model_v2_seed7.json   # Ensemble member (seed 7)
├── xgboost_model_v2_seed13.json  # Ensemble member (seed 13)
├── calibrator_v2.joblib           # Sigmoid probability calibrator
├── metrics_v2.json                # Full evaluation metrics (~30 KB)
└── model_metadata_v2.json         # Feature list, hyperparams, blocked columns
```
