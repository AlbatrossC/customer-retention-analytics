# SQLite Database — Schema & Architecture

## Overview

Everything in the dashboard comes from one file: **`database/customer_retention.db`** (~23 MB).

It's a self-contained SQLite database — no server installation needed, no configuration, no passwords. The Flask app just opens the file and queries it.

### What's Inside

| Table | Rows | What It Stores |
|---|---|---|
| `customers` | **10,000** | Who the customer is — name, age, segment, products, value |
| `customer_snapshots` | **53,040** | Monthly behavioral data — 1 to 6 snapshots per customer |
| `model1_predictions` | **10,000** | Model 1 churn probability and risk level for every customer |
| `model1_risk_factors` | **50,000** | Top 5 SHAP risk factors per customer (5 × 10,000) |
| `model2_predictions` | **3,803** | Model 2 reason, urgency, and action (High + Medium + borderline Low) |
| `model2_evidence` | **15,385** | Individual evidence citations from Model 2 (1–10 per customer) |

---

## How the Tables Connect

```
                        customers (10,000)
                     ┌───────┼──────────────────────────┐
                     │       │                          │
                     │       │ FK: customer_id          │
                     ▼       ▼                          ▼
          customer_snapshots    model1_predictions    model2_predictions
          (up to 6 per          (exactly 1 per         (1 per customer
           customer)             customer)              IF risk ≠ Low)
                                     │                       │
                                     ▼                       ▼
                           model1_risk_factors        model2_evidence
                           (exactly 5 per             (1–10 per
                            customer)                  customer)
```

**Everything joins on `customer_id`.** If you `LEFT JOIN` from `customers`, Low-risk customers will have `NULL` values for Model 2 fields (because they weren't analyzed).

---

## Table Schemas

### 1. `customers` — Customer Profiles

One row per customer. Static information taken from the latest snapshot.

| Column | Type | Description | Example |
|---|---|---|---|
| `customer_id` | TEXT (PK) | Unique customer identifier | `C10042` |
| `customer_name` | TEXT | Full name | `Priya Sharma` |
| `age` | INTEGER | Age in years | `34` |
| `tenure_months` | INTEGER | Months with the bank | `54` |
| `customer_segment` | TEXT | `salary`, `pension`, `farmer`, `vendor`, `business` | `salary` |
| `income_regularity` | TEXT | `regular`, `irregular`, `seasonal` | `regular` |
| `customer_yearly_value` | REAL | Annual revenue to the bank (₹) | `48500.0` |
| `loyalty` | REAL | Hidden simulation score (not used by models) | `0.73` |
| `products_count` | INTEGER | Banking products held (1–7) | `3` |
| `has_credit_card` | INTEGER | 1 = yes, 0 = no | `1` |
| `has_loan` | INTEGER | 1 = yes, 0 = no | `1` |
| `branch_code` | TEXT | Branch identifier | `BR-121` |
| `card_colour` | TEXT | Card tier (deliberate noise decoy) | `gold` |

---

### 2. `customer_snapshots` — Monthly Time-Series Data

One row per customer per month. This is the core behavioral data — what the customer was doing each month.

| Column | Type | Description |
|---|---|---|
| `id` | INTEGER (PK) | Auto-incremented row ID |
| `customer_id` | TEXT (FK) | Links to `customers` |
| `snapshot_date` | TEXT | Month this row represents (e.g., `2026-03-01`) |
| `days_since_last_transaction` | INTEGER | Days since last transaction (higher = more inactive) |
| `balance_change_30d` | REAL | % change in account balance (negative = dropping) |
| `transaction_change_30d` | REAL | % change in transaction count |
| `card_spend_change_30d` | REAL | % change in card spending |
| `app_login_change_30d` | REAL | % change in mobile app logins |
| `salary_missing_days` | REAL | Days salary credit is delayed (NULL for non-salaried) |
| `external_transfer_change_30d` | REAL | % change in money sent to other banks (positive = bad) |
| `upi_share_of_spend` | REAL | Fraction of spending via UPI (0.0 – 1.0) |
| `fd_maturing_in_30d` | INTEGER | Fixed deposit maturing within 30 days (0 or 1) |
| `products_dropped_90d` | INTEGER | Products closed in last 90 days |
| `complaints_30d` | INTEGER | Complaints filed this month |
| `unresolved_complaints` | INTEGER | Complaints still unresolved |
| `failed_transactions_30d` | INTEGER | Failed transactions this month |
| `avg_resolution_time_hrs` | REAL | Hours to resolve complaints (0 if no complaints) |
| `emi_bounce_30d` | INTEGER | Loan EMI payment bounced (0 or 1) |
| `complaint_text` | TEXT | Actual complaint text (NULL if no complaint) |
| `churn_flag` | INTEGER | 1 = churned this month, 0 = stayed |

---

### 3. `model1_predictions` — XGBoost Churn Predictions

One row per customer. Every customer gets scored.

| Column | Type | Description | Example |
|---|---|---|---|
| `customer_id` | TEXT (PK) | Links to `customers` | `C10015` |
| `churn_probability` | REAL | Calibrated churn probability (%) | `34.82` |
| `raw_churn_probability` | REAL | Raw model output before calibration | `68.45` |
| `probability_mode` | TEXT | Calibration method used | `sigmoid` |
| `risk_score` | REAL | Composite risk score (0–100) | `78.4` |
| `churn_prediction` | TEXT | Binary: `Yes` or `No` | `Yes` |
| `risk_level` | TEXT | `High`, `Medium`, or `Low` | `High` |

---

### 4. `model1_risk_factors` — SHAP Feature Importance

Five rows per customer. The top 5 features pushing toward churn, ranked by SHAP contribution.

| Column | Type | Description | Example |
|---|---|---|---|
| `id` | INTEGER (PK) | Auto-incremented row ID | |
| `customer_id` | TEXT (FK) | Links to `customers` | `C10015` |
| `factor_rank` | INTEGER | Rank: 1 (strongest) to 5 | `1` |
| `factor_name` | TEXT | Feature name | `latest_days_since_last_transaction` |
| `factor_value` | REAL | Actual value for this customer | `19.0` |
| `factor_message` | TEXT | Human-readable explanation | `"Customer has gone longer without transacting."` |
| `contribution` | REAL | SHAP contribution (higher = more churn influence) | `0.842` |

---

### 5. `model2_predictions` — LLM Reason & Action Analysis

One row per analyzed customer. **Only 3,803 rows** — High risk (2,142) + Medium risk (973) + borderline Low risk (688). Low-risk customers without Model 2 analysis will have NULL if you `LEFT JOIN`.

| Column | Type | Description | Example |
|---|---|---|---|
| `customer_id` | TEXT (PK) | Links to `customers` | `C10042` |
| `primary_reason` | TEXT | Main churn driver | `SERVICE_DISSATISFACTION` |
| `reasoning_summary` | TEXT | LLM-generated explanation | `"Customer experienced 2 unresolved complaints..."` |
| `recommended_action` | TEXT | What the bank should do | `COMPLAINT_ESCALATION` |
| `urgency` | TEXT | `HIGH`, `MEDIUM`, or `LOW` | `HIGH` |
| `secondary_reasons` | TEXT | Additional reasons (comma-separated) or NULL | `COMPETITOR_MIGRATION` |
| `raw_text` | TEXT | Full raw JSON from the LLM (for debugging) | `{"primary_reason": ...}` |

---

### 6. `model2_evidence` — Supporting Evidence Items

Variable rows per customer (1–10). Each row is one piece of evidence the LLM cited.

| Column | Type | Description | Example |
|---|---|---|---|
| `id` | INTEGER (PK) | Auto-incremented row ID | |
| `customer_id` | TEXT (FK) | Links to `customers` | `C10042` |
| `evidence_rank` | INTEGER | Order of the evidence (1-based) | `1` |
| `evidence_text` | TEXT | Exact citation string | `unresolved_complaints=2` |

---

## Database Indexes

Three indexes are created for fast lookups:

```sql
-- Fast monthly snapshot retrieval for a customer
CREATE INDEX idx_snapshots_customer_date ON customer_snapshots(customer_id, snapshot_date);

-- Fast risk factor lookup by customer
CREATE INDEX idx_risk_factors_customer ON model1_risk_factors(customer_id);

-- Fast evidence lookup by customer
CREATE INDEX idx_evidence_customer ON model2_evidence(customer_id);
```

---

## Database Management Scripts

| Script | What It Does | Command |
|---|---|---|
| `build_db.py` | **Rebuild from scratch.** Drops and recreates all tables, loads data from `customers.csv` and JSON output files. | `python database/build_db.py` |
| `insert_low_risk_model2.py` | **Add borderline Low-risk data.** Inserts Model 2 results from `top_low_risk_customers.json` into existing DB. | `python database/insert_low_risk_model2.py` |
| `check_db.py` | **Verify integrity.** Prints row counts, risk distributions, and reason breakdowns. | `python database/check_db.py` |
| `schema.sql` | **Reference DDL.** The exact `CREATE TABLE` statements (with indexes and foreign keys). | Read-only reference |

---

## Useful SQL Queries

### Full Customer 360 View

```sql
SELECT c.customer_id, c.customer_name, c.customer_segment,
       c.customer_yearly_value,
       m1.churn_probability, m1.risk_level,
       m2.primary_reason, m2.urgency, m2.recommended_action,
       m2.reasoning_summary
FROM customers c
JOIN model1_predictions m1 ON c.customer_id = m1.customer_id
LEFT JOIN model2_predictions m2 ON c.customer_id = m2.customer_id
WHERE c.customer_id = 'C10015';
```

### High-Value Customers at High Risk (Priority Queue)

```sql
SELECT c.customer_id, c.customer_name, c.customer_segment,
       c.customer_yearly_value,
       m1.churn_probability,
       m2.primary_reason, m2.recommended_action
FROM customers c
JOIN model1_predictions m1 ON c.customer_id = m1.customer_id
JOIN model2_predictions m2 ON c.customer_id = m2.customer_id
WHERE m1.risk_level = 'High'
  AND c.customer_yearly_value >= 40000
ORDER BY c.customer_yearly_value DESC;
```

### Monthly Complaint History for a Customer

```sql
SELECT snapshot_date, complaints_30d, unresolved_complaints,
       avg_resolution_time_hrs, complaint_text
FROM customer_snapshots
WHERE customer_id = 'C10002'
ORDER BY snapshot_date;
```

### Top Churn Drivers Across All High-Risk Customers

```sql
SELECT m2.primary_reason,
       COUNT(*) AS customer_count,
       ROUND(AVG(m1.churn_probability), 2) AS avg_churn_prob
FROM model2_predictions m2
JOIN model1_predictions m1 ON m2.customer_id = m1.customer_id
WHERE m1.risk_level = 'High'
GROUP BY m2.primary_reason
ORDER BY customer_count DESC;
```

### Revenue at Risk by Segment

```sql
SELECT c.customer_segment,
       COUNT(*) AS high_risk_count,
       ROUND(SUM(c.customer_yearly_value), 0) AS revenue_at_risk
FROM customers c
JOIN model1_predictions m1 ON c.customer_id = m1.customer_id
WHERE m1.risk_level = 'High'
GROUP BY c.customer_segment
ORDER BY revenue_at_risk DESC;
```
