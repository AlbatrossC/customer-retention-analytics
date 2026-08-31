-- Customer Retention Analytics - SQLite Schema
-- 6 tables: customers, customer_snapshots, model1_predictions,
--           model1_risk_factors, model2_predictions, model2_evidence

PRAGMA foreign_keys = ON;

------------------------------------------------------------------------
-- Table 1: customers - One row per customer (static/latest profile)
------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS customers (
    customer_id             TEXT PRIMARY KEY,
    customer_name           TEXT NOT NULL,
    age                     INTEGER,
    tenure_months           INTEGER,
    customer_segment        TEXT,
    income_regularity       TEXT,
    customer_yearly_value   REAL,
    loyalty                 REAL,
    products_count          INTEGER,
    has_credit_card         INTEGER,
    has_loan                INTEGER,
    branch_code             TEXT,
    card_colour             TEXT
);

------------------------------------------------------------------------
-- Table 2: customer_snapshots - One row per customer per month
------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS customer_snapshots (
    id                              INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id                     TEXT NOT NULL REFERENCES customers(customer_id),
    snapshot_date                   TEXT NOT NULL,
    days_since_last_transaction     INTEGER,
    balance_change_30d              REAL,
    transaction_change_30d          REAL,
    card_spend_change_30d           REAL,
    app_login_change_30d            REAL,
    salary_missing_days             REAL,
    external_transfer_change_30d    REAL,
    upi_share_of_spend              REAL,
    fd_maturing_in_30d              INTEGER,
    products_dropped_90d            INTEGER,
    complaints_30d                  INTEGER,
    unresolved_complaints           INTEGER,
    failed_transactions_30d         INTEGER,
    avg_resolution_time_hrs         REAL,
    emi_bounce_30d                  INTEGER,
    complaint_text                  TEXT,
    churn_flag                      INTEGER,
    UNIQUE(customer_id, snapshot_date)
);

------------------------------------------------------------------------
-- Table 3: model1_predictions - XGBoost churn prediction per customer
------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS model1_predictions (
    customer_id             TEXT PRIMARY KEY REFERENCES customers(customer_id),
    churn_probability       REAL,
    raw_churn_probability   REAL,
    probability_mode        TEXT,
    risk_score              REAL,
    churn_prediction        TEXT,
    risk_level              TEXT
);

------------------------------------------------------------------------
-- Table 4: model1_risk_factors - Top 5 risk factors per customer
------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS model1_risk_factors (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id     TEXT NOT NULL REFERENCES customers(customer_id),
    factor_rank     INTEGER NOT NULL,
    factor_name     TEXT NOT NULL,
    factor_value    REAL,
    factor_message  TEXT,
    contribution    REAL,
    UNIQUE(customer_id, factor_rank)
);

------------------------------------------------------------------------
-- Table 5: model2_predictions - LLM analysis per customer
------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS model2_predictions (
    customer_id             TEXT PRIMARY KEY REFERENCES customers(customer_id),
    primary_reason          TEXT,
    reasoning_summary       TEXT,
    recommended_action      TEXT,
    urgency                 TEXT,
    secondary_reasons       TEXT,
    raw_text                TEXT
);

------------------------------------------------------------------------
-- Table 6: model2_evidence - Evidence items per customer
------------------------------------------------------------------------
CREATE TABLE IF NOT EXISTS model2_evidence (
    id              INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id     TEXT NOT NULL REFERENCES customers(customer_id),
    evidence_rank   INTEGER NOT NULL,
    evidence_text   TEXT NOT NULL,
    UNIQUE(customer_id, evidence_rank)
);

------------------------------------------------------------------------
-- Indexes
------------------------------------------------------------------------
CREATE INDEX IF NOT EXISTS idx_snapshots_customer_date
    ON customer_snapshots(customer_id, snapshot_date);

CREATE INDEX IF NOT EXISTS idx_risk_factors_customer
    ON model1_risk_factors(customer_id);

CREATE INDEX IF NOT EXISTS idx_evidence_customer
    ON model2_evidence(customer_id);
