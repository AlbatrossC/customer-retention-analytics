# Customer Retention Analytics — SQLite Database

This folder contains a local SQLite database that stores all customer data, monthly behavioral snapshots, and the outputs from both ML models used in the retention analytics pipeline.

**Database file:** `customer_retention.db` (~19 MB)

**To rebuild from scratch:**
```bash
python database/build_db.py
```

---

## Overview

We have **10,000 customers** tracked over **6 months** (Jan–Jun 2026). Each customer has monthly behavioral snapshots. Two models process this data:

1. **Model 1 (XGBoost)** — Predicts churn probability and assigns a risk level (High / Medium / Low) for every customer.
2. **Model 2 (Fine-tuned LLM)** — Analyzes High and Medium risk customers (3,115 total) to explain *why* they might churn and *what action* to take. Low-risk customers were not processed by Model 2 (their fields will be `NULL`).

The database has **6 tables**:

```
customers                  10,000 rows   (one per customer)
customer_snapshots         53,040 rows   (one per customer per month)
model1_predictions         10,000 rows   (one per customer)
model1_risk_factors        50,000 rows   (5 per customer)
model2_predictions          3,115 rows   (only high/medium risk)
model2_evidence           ~13,225 rows   (1–10 per model2 customer)
```

---

## Table Details

### 1. `customers`

**One row per customer.** Stores who the customer is and their profile. Taken from the latest available monthly snapshot.

| Column | Type | Description |
|--------|------|-------------|
| `customer_id` | TEXT | Unique customer ID (e.g. `C10000`). **Primary key.** |
| `customer_name` | TEXT | Full name of the customer. |
| `age` | INTEGER | Customer's age in years. |
| `tenure_months` | INTEGER | How many months the customer has been with the bank. |
| `customer_segment` | TEXT | Business category: `business`, `farmer`, `pension`, `salary`, or `vendor`. |
| `income_regularity` | TEXT | How regular their income is: `regular`, `irregular`, or `seasonal`. |
| `customer_yearly_value` | REAL | Estimated yearly revenue the customer brings to the bank. |
| `loyalty` | REAL | A loyalty score (can be negative for disloyal customers). |
| `products_count` | INTEGER | Number of bank products the customer holds (accounts, cards, loans, etc.). |
| `has_credit_card` | INTEGER | `1` if the customer has a credit card, `0` if not. |
| `has_loan` | INTEGER | `1` if the customer has a loan, `0` if not. |
| `branch_code` | TEXT | The bank branch code (e.g. `BR-133`). |
| `card_colour` | TEXT | Card tier: `black`, `blue`, `gold`, `green`, or `silver`. |

---

### 2. `customer_snapshots`

**One row per customer per month.** This is the core time-series data — it captures what the customer was doing each month. If the customer filed a complaint that month, the text is stored here; otherwise `complaint_text` is `NULL`.

| Column | Type | Description |
|--------|------|-------------|
| `id` | INTEGER | Auto-generated row ID. |
| `customer_id` | TEXT | Links to `customers.customer_id`. |
| `snapshot_date` | TEXT | The month this snapshot represents (e.g. `2026-01-01`). |
| `days_since_last_transaction` | INTEGER | How many days since the customer last transacted. Higher = less active. |
| `balance_change_30d` | REAL | % change in account balance over the last 30 days. Negative = balance dropping. |
| `transaction_change_30d` | REAL | % change in transaction count over 30 days. Negative = fewer transactions. |
| `card_spend_change_30d` | REAL | % change in card spending over 30 days. |
| `app_login_change_30d` | REAL | % change in mobile app logins over 30 days. Negative = less engagement. |
| `salary_missing_days` | REAL | Days since expected salary credit was missed. `NULL` if not applicable (e.g. non-salaried customers). |
| `external_transfer_change_30d` | REAL | % change in money transferred out to other banks. Positive = sending more money out. |
| `upi_share_of_spend` | REAL | Fraction of total spending done via UPI (0.0 to 1.0). |
| `fd_maturing_in_30d` | INTEGER | Number of fixed deposits maturing in the next 30 days. |
| `products_dropped_90d` | INTEGER | Number of bank products closed/dropped in the last 90 days. |
| `complaints_30d` | INTEGER | Number of complaints filed in the last 30 days. `0` if none. |
| `unresolved_complaints` | INTEGER | Number of complaints still unresolved. |
| `failed_transactions_30d` | INTEGER | Number of failed transactions in the last 30 days. |
| `avg_resolution_time_hrs` | REAL | Average time (in hours) to resolve complaints. `0.0` if no complaints. |
| `emi_bounce_30d` | INTEGER | Number of EMI/loan payments that bounced in the last 30 days. |
| `complaint_text` | TEXT | The actual complaint text filed by the customer. **`NULL` if no complaint that month.** |
| `churn_flag` | INTEGER | Actual churn label: `1` = customer churned that month, `0` = stayed. |

---

### 3. `model1_predictions`

**One row per customer.** The output from Model 1 (XGBoost churn prediction model). Every customer gets a prediction.

| Column | Type | Description |
|--------|------|-------------|
| `customer_id` | TEXT | Links to `customers.customer_id`. **Primary key.** |
| `churn_probability` | REAL | Calibrated churn probability as a percentage (e.g. `4.56` means 4.56% chance of churning). |
| `raw_churn_probability` | REAL | Raw model output before calibration (e.g. `36.73`). |
| `probability_mode` | TEXT | The calibration method used. Currently always `sigmoid`. |
| `risk_score` | REAL | Overall risk score (0–100). Higher = more likely to churn. |
| `churn_prediction` | TEXT | Binary prediction: `Yes` (will churn) or `No` (will stay). |
| `risk_level` | TEXT | Risk category: `High`, `Medium`, or `Low`. |

---

### 4. `model1_risk_factors`

**Five rows per customer.** The top 5 features (from XGBoost SHAP analysis) that most influenced the churn prediction for each customer. Ranked by importance.

| Column | Type | Description |
|--------|------|-------------|
| `id` | INTEGER | Auto-generated row ID. |
| `customer_id` | TEXT | Links to `customers.customer_id`. |
| `factor_rank` | INTEGER | Rank from `1` (most important) to `5` (least important). |
| `factor_name` | TEXT | The feature name (e.g. `latest_days_since_last_transaction`, `sum_failed_transactions_30d_3m`). |
| `factor_value` | REAL | The actual value of that feature for this customer. |
| `factor_message` | TEXT | A human-readable explanation (e.g. `"Customer has gone longer without transacting."`). |
| `contribution` | REAL | SHAP contribution score. Higher = this feature pushed the prediction more toward churn. |

---

### 5. `model2_predictions`

**One row per customer (High and Medium risk only).** The output from Model 2 (fine-tuned LLM). This model explains the *reason* behind the churn risk and recommends an *action*.

3,115 customers were processed (2,142 High + 973 Medium risk). Low-risk customers don't have a row here — if you `LEFT JOIN` from `customers`, their Model 2 fields will be `NULL`.

| Column | Type | Description |
|--------|------|-------------|
| `customer_id` | TEXT | Links to `customers.customer_id`. **Primary key.** |
| `primary_reason` | TEXT | The main reason for churn risk. One of: `SERVICE_DISSATISFACTION`, `FEE_DISSATISFACTION`, `FINANCIAL_STRESS`, `COMPETITOR_MIGRATION`, `DIGITAL_FRICTION`, `LOW_ENGAGEMENT`, `PRODUCT_MISMATCH`, `UNKNOWN`. |
| `reasoning_summary` | TEXT | A short LLM-generated explanation of why this reason was chosen. |
| `recommended_action` | TEXT | What the bank should do. One of: `COMPLAINT_ESCALATION`, `SERVICE_RECOVERY`, `FEE_WAIVER_REVIEW`, `FINANCIAL_GUIDANCE`, `LOAN_REVIEW`, `PRODUCT_REVIEW`, `RE_ENGAGEMENT`, `RM_CALLBACK`, `MONITOR`. |
| `urgency` | TEXT | How urgent the action is: `HIGH`, `MEDIUM`, or `LOW`. |
| `secondary_reasons` | TEXT | Additional churn reasons if any, stored as comma-separated values (e.g. `COMPETITOR_MIGRATION`). `NULL` if there are no secondary reasons. Most customers have `NULL` here. |
| `raw_text` | TEXT | The raw JSON response from the LLM. Kept for debugging purposes. |

---

### 6. `model2_evidence`

**Variable rows per customer (1–10).** Each piece of evidence the LLM cited to support its prediction. These are typically feature values or observations.

| Column | Type | Description |
|--------|------|-------------|
| `id` | INTEGER | Auto-generated row ID. |
| `customer_id` | TEXT | Links to `customers.customer_id`. |
| `evidence_rank` | INTEGER | Order of the evidence item (1-based). |
| `evidence_text` | TEXT | The evidence string (e.g. `complaints_30d=6`, `avg_resolution_time_hrs=118.1`). |

---

## Relationships

```
customers (10,000)
  ├── customer_snapshots      (up to 6 per customer — monthly)
  ├── model1_predictions      (exactly 1 per customer)
  ├── model1_risk_factors     (exactly 5 per customer)
  ├── model2_predictions      (1 per customer if High/Medium risk, absent if Low — 3,115 total)
  └── model2_evidence         (1–10 per customer, only if model2 was run)
```

Everything links back to `customers.customer_id`.

---

## Common Queries

**Get a full customer view with risk info:**
```sql
SELECT c.customer_id, c.customer_name, c.customer_segment,
       m1.churn_probability, m1.risk_level,
       m2.primary_reason, m2.recommended_action, m2.urgency
FROM customers c
JOIN model1_predictions m1 ON c.customer_id = m1.customer_id
LEFT JOIN model2_predictions m2 ON c.customer_id = m2.customer_id
ORDER BY m1.risk_score DESC;
```

**Get all High-risk customers with their top risk factor:**
```sql
SELECT m1.customer_id, c.customer_name, m1.churn_probability,
       rf.factor_name, rf.factor_message
FROM model1_predictions m1
JOIN customers c ON m1.customer_id = c.customer_id
JOIN model1_risk_factors rf ON m1.customer_id = rf.customer_id AND rf.factor_rank = 1
WHERE m1.risk_level = 'High'
ORDER BY m1.risk_score DESC;
```

**Get monthly complaint history for a customer:**
```sql
SELECT snapshot_date, complaints_30d, unresolved_complaints, complaint_text
FROM customer_snapshots
WHERE customer_id = 'C10002'
ORDER BY snapshot_date;
```

---

## Source Files

| File | What it provides |
|------|-----------------|
| `model_1_v2/data/customers.csv` | Customer profiles + monthly snapshots + complaint text |
| `pre_processing/outputs/model_1_v2_customer_outputs.json` | Model 1 XGBoost predictions + risk factors |
| `pre_processing/outputs/devang_model2_pipeline_outputs.json` | Model 2 LLM analysis (first batch — 1,558 customers) |
| `pre_processing/outputs/remaining_high_medium_risk_customers.json` | Model 2 LLM analysis (remaining batch — 1,557 additional customers) |
