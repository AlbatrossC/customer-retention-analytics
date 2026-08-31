"""
Build the customer_retention.db SQLite database from source CSV/JSON files.

Sources:
  - model_1_v2/data/customers.csv             -> customers, customer_snapshots
  - pre_processing/outputs/model_1_v2_customer_outputs.json -> model1_predictions, model1_risk_factors
  - pre_processing/outputs/devang_model2_pipeline_outputs.json -> model2_predictions, model2_evidence
"""

import json
import math
import sqlite3
import sys
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DB_DIR = ROOT / "database"
DB_PATH = DB_DIR / "customer_retention.db"
SCHEMA_PATH = DB_DIR / "schema.sql"

CUSTOMERS_CSV = ROOT / "model_1_v2" / "data" / "customers.csv"
MODEL1_JSON = ROOT / "pre_processing" / "outputs" / "model_1_v2_customer_outputs.json"
MODEL2_JSON = ROOT / "pre_processing" / "outputs" / "devang_model2_pipeline_outputs.json"
MODEL2_REMAINING_JSON = ROOT / "pre_processing" / "outputs" / "remaining_high_medium_risk_customers.json"


def clean(value):
    """Convert NaN/NaT/pd.NA to None for SQLite."""
    if value is None:
        return None
    if isinstance(value, float) and math.isnan(value):
        return None
    try:
        if pd.isna(value):
            return None
    except (ValueError, TypeError):
        pass
    return value


def load_customers_csv() -> pd.DataFrame:
    """Load the base customers CSV with monthly snapshots."""
    df = pd.read_csv(CUSTOMERS_CSV)
    print(f"  Loaded {len(df):,} rows, {df['customer_id'].nunique():,} unique customers from customers.csv")
    return df


def load_model1_json() -> list[dict]:
    """Load Model 1 v2 output JSON."""
    with open(MODEL1_JSON, "r", encoding="utf-8") as f:
        data = json.load(f)
    customers = data["customers"]
    print(f"  Loaded {len(customers):,} customers from model_1_v2_customer_outputs.json")
    return customers


def load_model2_json() -> list[dict]:
    """Load Model 2 output from both JSON files, deduplicating by customer_id."""
    with open(MODEL2_JSON, "r", encoding="utf-8") as f:
        data1 = json.load(f)
    customers1 = data1["customers"]
    print(f"  Loaded {len(customers1):,} customers from devang_model2_pipeline_outputs.json")

    with open(MODEL2_REMAINING_JSON, "r", encoding="utf-8") as f:
        data2 = json.load(f)
    customers2 = data2["customers"]
    print(f"  Loaded {len(customers2):,} customers from remaining_high_medium_risk_customers.json")

    # Merge: first file wins for overlapping customer_ids
    seen = set(c["customer_id"] for c in customers1)
    new_customers = [c for c in customers2 if c["customer_id"] not in seen]
    merged = customers1 + new_customers
    print(f"  Merged: {len(merged):,} unique Model 2 customers ({len(customers2) - len(new_customers):,} duplicates skipped)")
    return merged


def insert_customers(conn: sqlite3.Connection, df: pd.DataFrame) -> int:
    """Insert into `customers` table — one row per customer (latest snapshot)."""
    df_sorted = df.sort_values(["customer_id", "snapshot_date"])
    latest = df_sorted.groupby("customer_id").last().reset_index()

    rows = []
    for _, row in latest.iterrows():
        rows.append((
            row["customer_id"],
            row["customer_name"],
            clean(row.get("age")),
            clean(row.get("tenure_months")),
            clean(row.get("customer_segment")),
            clean(row.get("income_regularity")),
            clean(row.get("customer_yearly_value")),
            clean(row.get("loyalty")),
            clean(row.get("products_count")),
            clean(row.get("has_credit_card")),
            clean(row.get("has_loan")),
            clean(row.get("branch_code")),
            clean(row.get("card_colour")),
        ))

    conn.executemany(
        "INSERT INTO customers VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)",
        rows,
    )
    return len(rows)


def insert_snapshots(conn: sqlite3.Connection, df: pd.DataFrame) -> int:
    """Insert into `customer_snapshots` table — one row per customer per month."""
    rows = []
    for _, row in df.iterrows():
        rows.append((
            row["customer_id"],
            row["snapshot_date"],
            clean(row.get("days_since_last_transaction")),
            clean(row.get("balance_change_30d")),
            clean(row.get("transaction_change_30d")),
            clean(row.get("card_spend_change_30d")),
            clean(row.get("app_login_change_30d")),
            clean(row.get("salary_missing_days")),
            clean(row.get("external_transfer_change_30d")),
            clean(row.get("upi_share_of_spend")),
            clean(row.get("fd_maturing_in_30d")),
            clean(row.get("products_dropped_90d")),
            clean(row.get("complaints_30d")),
            clean(row.get("unresolved_complaints")),
            clean(row.get("failed_transactions_30d")),
            clean(row.get("avg_resolution_time_hrs")),
            clean(row.get("emi_bounce_30d")),
            clean(row.get("complaint_text")),
            clean(row.get("churn_flag")),
        ))

    conn.executemany(
        "INSERT INTO customer_snapshots "
        "(customer_id, snapshot_date, days_since_last_transaction, "
        "balance_change_30d, transaction_change_30d, card_spend_change_30d, "
        "app_login_change_30d, salary_missing_days, external_transfer_change_30d, "
        "upi_share_of_spend, fd_maturing_in_30d, products_dropped_90d, "
        "complaints_30d, unresolved_complaints, failed_transactions_30d, "
        "avg_resolution_time_hrs, emi_bounce_30d, complaint_text, churn_flag) "
        "VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
        rows,
    )
    return len(rows)


def insert_model1(conn: sqlite3.Connection, customers: list[dict]) -> tuple[int, int]:
    """Insert into `model1_predictions` and `model1_risk_factors`."""
    pred_rows = []
    factor_rows = []

    for c in customers:
        cid = c["customer_id"]
        out = c.get("model_1_output")
        if not out:
            continue

        pred_rows.append((
            cid,
            out.get("churn_probability"),
            out.get("raw_churn_probability"),
            out.get("probability_mode"),
            out.get("risk_score"),
            out.get("churn_prediction"),
            out.get("risk_level"),
        ))

        for rank, factor in enumerate(out.get("top_risk_factors", []), start=1):
            factor_rows.append((
                cid,
                rank,
                factor.get("factor"),
                factor.get("value"),
                factor.get("message"),
                factor.get("contribution"),
            ))

    conn.executemany(
        "INSERT INTO model1_predictions VALUES (?,?,?,?,?,?,?)",
        pred_rows,
    )
    conn.executemany(
        "INSERT INTO model1_risk_factors "
        "(customer_id, factor_rank, factor_name, factor_value, factor_message, contribution) "
        "VALUES (?,?,?,?,?,?)",
        factor_rows,
    )
    return len(pred_rows), len(factor_rows)


def insert_model2(conn: sqlite3.Connection, customers: list[dict]) -> tuple[int, int]:
    """Insert into `model2_predictions` and `model2_evidence`."""
    pred_rows = []
    evidence_rows = []

    for c in customers:
        cid = c["customer_id"]
        m2_out = c.get("model2_output")
        if not m2_out:
            continue
        prediction = m2_out.get("prediction")
        if not prediction:
            continue

        secondary = prediction.get("secondary_reasons", [])
        secondary_str = ",".join(secondary) if secondary else None

        pred_rows.append((
            cid,
            prediction.get("primary_reason"),
            prediction.get("reasoning_summary"),
            prediction.get("recommended_action"),
            prediction.get("urgency"),
            secondary_str,
            m2_out.get("raw_text"),
        ))

        for rank, evidence in enumerate(prediction.get("evidence", []), start=1):
            evidence_rows.append((
                cid,
                rank,
                evidence,
            ))

    conn.executemany(
        "INSERT INTO model2_predictions VALUES (?,?,?,?,?,?,?)",
        pred_rows,
    )
    conn.executemany(
        "INSERT INTO model2_evidence "
        "(customer_id, evidence_rank, evidence_text) "
        "VALUES (?,?,?)",
        evidence_rows,
    )
    return len(pred_rows), len(evidence_rows)


def print_counts(conn: sqlite3.Connection) -> None:
    """Print row counts for all tables."""
    tables = [
        "customers",
        "customer_snapshots",
        "model1_predictions",
        "model1_risk_factors",
        "model2_predictions",
        "model2_evidence",
    ]
    print("\n--- Row Counts ---")
    for table in tables:
        count = conn.execute(f"SELECT COUNT(*) FROM {table}").fetchone()[0]
        print(f"  {table}: {count:,}")


def main() -> None:
    print("Building customer_retention.db...")
    print()

    # Delete existing DB
    if DB_PATH.exists():
        DB_PATH.unlink()
        print(f"  Deleted existing {DB_PATH.name}")

    # Load sources
    print("Loading source data...")
    df = load_customers_csv()
    model1_customers = load_model1_json()
    model2_customers = load_model2_json()
    print()

    # Create DB and apply schema
    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON")
    conn.execute("PRAGMA journal_mode = WAL")
    schema_sql = SCHEMA_PATH.read_text(encoding="utf-8")
    conn.executescript(schema_sql)
    print(f"  Created {DB_PATH.name} with schema")

    # Insert data
    print("Inserting data...")

    n = insert_customers(conn, df)
    print(f"  customers: {n:,} rows")

    n = insert_snapshots(conn, df)
    print(f"  customer_snapshots: {n:,} rows")

    n_pred, n_factors = insert_model1(conn, model1_customers)
    print(f"  model1_predictions: {n_pred:,} rows")
    print(f"  model1_risk_factors: {n_factors:,} rows")

    n_pred, n_evidence = insert_model2(conn, model2_customers)
    print(f"  model2_predictions: {n_pred:,} rows")
    print(f"  model2_evidence: {n_evidence:,} rows")

    conn.commit()
    print_counts(conn)
    conn.close()

    size_mb = DB_PATH.stat().st_size / (1024 * 1024)
    print(f"\nDone. Database: {DB_PATH} ({size_mb:.1f} MB)")


if __name__ == "__main__":
    main()
