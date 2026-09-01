"""
Build the customer_retention.db SQLite database from real source CSV/JSON files.

Sources:
  - model_1_v2/data/customers.csv                              -> customers, customer_snapshots
  - pre_processing/outputs/model_1_v2_customer_outputs.json    -> model1_predictions, model1_risk_factors
  - pre_processing/outputs/devang_model2_pipeline_outputs.json -> model2_predictions, model2_evidence
  - pre_processing/outputs/remaining_high_medium_risk_customers.json -> model2_predictions, model2_evidence
  - K-Means Behavioral Clustering                              -> customer_clusters, cluster_profiles
"""

import json
import math
import shutil
import sqlite3
import sys
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

ROOT = Path(__file__).resolve().parents[1]
DB_DIR = ROOT / "database"
DB_PATH = DB_DIR / "customer_retention.db"
SCHEMA_PATH = DB_DIR / "schema.sql"

CUSTOMERS_CSV = ROOT / "model_1_v2" / "data" / "customers.csv"
MODEL1_JSON = ROOT / "pre_processing" / "outputs" / "model_1_v2_customer_outputs.json"
MODEL2_JSON = ROOT / "pre_processing" / "outputs" / "devang_model2_pipeline_outputs.json"
MODEL2_REMAINING_JSON = ROOT / "pre_processing" / "outputs" / "remaining_high_medium_risk_customers.json"
MODEL2_LOW_RISK_JSON = ROOT / "pre_processing" / "outputs" / "top_low_risk_customers.json"

CLUSTERING_FEATURES = [
    "balance_change_30d",
    "transaction_change_30d",
    "days_since_last_transaction",
    "external_transfer_change_30d",
    "complaints_30d",
    "app_login_change_30d",
    "card_spend_change_30d",
    "failed_transactions_30d",
    "unresolved_complaints",
    "emi_bounce_30d",
]


def clean(value):
    """Convert NaN/NaT/pd.NA to None for SQLite."""
    if value is None:
        return None
    if isinstance(value, (float, np.floating)) and (math.isnan(value) or np.isnan(value)):
        return None
    try:
        if pd.isna(value):
            return None
    except (ValueError, TypeError):
        pass
    if isinstance(value, (np.integer, int)):
        return int(value)
    if isinstance(value, (np.floating, float)):
        return round(float(value), 4)
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
    """Load Model 2 output from all JSON files, deduplicating by customer_id."""
    with open(MODEL2_JSON, "r", encoding="utf-8") as f:
        data1 = json.load(f)
    customers1 = data1["customers"]
    print(f"  Loaded {len(customers1):,} customers from devang_model2_pipeline_outputs.json")

    with open(MODEL2_REMAINING_JSON, "r", encoding="utf-8") as f:
        data2 = json.load(f)
    customers2 = data2["customers"]
    print(f"  Loaded {len(customers2):,} customers from remaining_high_medium_risk_customers.json")

    seen = set(c["customer_id"] for c in customers1)
    new_customers = [c for c in customers2 if c["customer_id"] not in seen]
    merged = customers1 + new_customers
    print(f"  Merged (high+med): {len(merged):,} unique Model 2 customers ({len(customers2) - len(new_customers):,} duplicates skipped)")

    # Add top low-risk customers with model2 output
    if MODEL2_LOW_RISK_JSON.exists():
        with open(MODEL2_LOW_RISK_JSON, "r", encoding="utf-8") as f:
            data3 = json.load(f)
        customers3 = data3["customers"]
        print(f"  Loaded {len(customers3):,} customers from top_low_risk_customers.json")
        seen = set(c["customer_id"] for c in merged)
        new_low = [c for c in customers3 if c["customer_id"] not in seen]
        merged = merged + new_low
        print(f"  Final merged: {len(merged):,} unique Model 2 customers (+{len(new_low)} low-risk)")
    else:
        print(f"  (Skipping low-risk model2 — {MODEL2_LOW_RISK_JSON.name} not found)")

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
            clean(out.get("churn_probability")),
            clean(out.get("raw_churn_probability")),
            out.get("probability_mode"),
            clean(out.get("risk_score")),
            out.get("churn_prediction"),
            out.get("risk_level"),
        ))

        for rank, factor in enumerate(out.get("top_risk_factors", []), start=1):
            factor_rows.append((
                cid,
                rank,
                factor.get("factor"),
                clean(factor.get("value")),
                factor.get("message"),
                clean(factor.get("contribution")),
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


def perform_clustering_and_insert(
    conn: sqlite3.Connection,
    snapshots_df: pd.DataFrame,
    n_clusters: int = 5,
) -> tuple[int, int]:
    """Perform real K-Means clustering on customer behavioral features and insert into DB."""
    print("Performing real K-Means behavioral clustering...", flush=True)

    # 1. Latest snapshot features per customer
    latest_snapshots = (
        snapshots_df
        .sort_values(["customer_id", "snapshot_date"])
        .groupby("customer_id")
        .last()
        .reset_index()
    )

    cluster_data = latest_snapshots[["customer_id"] + CLUSTERING_FEATURES].copy().fillna(0)

    # 2. Standardize features
    scaler = StandardScaler()
    feature_matrix = scaler.fit_transform(cluster_data[CLUSTERING_FEATURES])

    # 3. Fit K-Means
    kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
    cluster_labels = kmeans.fit_predict(feature_matrix)
    cluster_data["cluster_id"] = cluster_labels

    # 4. Determine domain persona names based on cluster centroids
    centers = cluster_data.groupby("cluster_id")[CLUSTERING_FEATURES].mean()
    assigned = {}

    # EMI bounce highest -> Loan Default & Financial Strain
    emi_c = centers["emi_bounce_30d"].idxmax()
    assigned[emi_c] = "Loan Default & Financial Strain"

    # Complaints highest -> High Friction & Escalated Complaints
    comp_c = centers.drop(index=list(assigned.keys()))["complaints_30d"].idxmax()
    assigned[comp_c] = "High Friction & Escalated Complaints"

    # External transfer highest -> Severe Capital Outflow & Attrition
    ext_c = centers.drop(index=list(assigned.keys()))["external_transfer_change_30d"].idxmax()
    assigned[ext_c] = "Severe Capital Outflow & Attrition"

    # Balance growth highest -> High Engagement & Growing
    grow_c = centers.drop(index=list(assigned.keys()))["balance_change_30d"].idxmax()
    assigned[grow_c] = "High Engagement & Growing"

    # Remaining -> Stable & Moderate Activity
    rem_c = centers.drop(index=list(assigned.keys())).index[0]
    assigned[rem_c] = "Stable & Moderate Activity"

    cluster_data["cluster_label"] = cluster_data["cluster_id"].map(assigned)

    # Load Model 1 and Model 2 outputs from DB to compute cluster profiles
    m1_df = pd.read_sql_query("SELECT customer_id, churn_probability, risk_score, risk_level FROM model1_predictions", conn)
    m2_df = pd.read_sql_query("SELECT customer_id, primary_reason, recommended_action FROM model2_predictions", conn)

    # 5. Build cluster profiles
    cluster_profiles = []
    for cid_val in range(n_clusters):
        members = cluster_data[cluster_data["cluster_id"] == cid_val]
        member_ids = set(members["customer_id"])
        m1_members = m1_df[m1_df["customer_id"].isin(member_ids)]
        m2_members = m2_df[m2_df["customer_id"].isin(member_ids)]

        profile = {
            "cluster_id": int(cid_val),
            "cluster_label": assigned.get(cid_val, f"Cluster {cid_val}"),
            "customer_count": len(members),
            "avg_churn_probability": round(float(m1_members["churn_probability"].mean()), 2) if len(m1_members) else 0.0,
            "avg_risk_score": round(float(m1_members["risk_score"].mean()), 2) if len(m1_members) else 0.0,
        }

        # Average of clustering features
        for feat in CLUSTERING_FEATURES:
            col_name = f"avg_{feat}"
            profile[col_name] = round(float(members[feat].mean()), 2) if feat in members.columns else 0.0

        # Risk distribution
        profile["high_risk_count"] = int((m1_members["risk_level"] == "High").sum())
        profile["medium_risk_count"] = int((m1_members["risk_level"] == "Medium").sum())
        profile["low_risk_count"] = int((m1_members["risk_level"] == "Low").sum())

        # Dominant Model 2 outputs (from evaluated at-risk customers)
        if len(m2_members) > 0 and not m2_members["primary_reason"].dropna().empty:
            profile["dominant_primary_reason"] = m2_members["primary_reason"].mode().iloc[0]
            profile["dominant_recommended_action"] = m2_members["recommended_action"].mode().iloc[0]
        else:
            profile["dominant_primary_reason"] = "STABLE_ENGAGEMENT"
            profile["dominant_recommended_action"] = "MONITOR"

        cluster_profiles.append(profile)

    # 6. Create cluster tables & insert
    conn.executescript("""
        CREATE TABLE IF NOT EXISTS customer_clusters (
            customer_id TEXT PRIMARY KEY REFERENCES customers(customer_id),
            cluster_id INTEGER NOT NULL,
            cluster_label TEXT
        );

        CREATE TABLE IF NOT EXISTS cluster_profiles (
            cluster_id INTEGER PRIMARY KEY,
            cluster_label TEXT,
            customer_count INTEGER,
            avg_churn_probability REAL,
            avg_risk_score REAL,
            avg_balance_change_30d REAL,
            avg_transaction_change_30d REAL,
            avg_days_since_last_transaction REAL,
            avg_external_transfer_change_30d REAL,
            avg_complaints_30d REAL,
            avg_app_login_change_30d REAL,
            avg_card_spend_change_30d REAL,
            avg_failed_transactions_30d REAL,
            avg_unresolved_complaints REAL,
            avg_emi_bounce_30d REAL,
            high_risk_count INTEGER,
            medium_risk_count INTEGER,
            low_risk_count INTEGER,
            dominant_primary_reason TEXT,
            dominant_recommended_action TEXT
        );

        CREATE INDEX IF NOT EXISTS idx_clusters_cluster_id
            ON customer_clusters(cluster_id);
    """)

    # Insert customer cluster assignments
    cluster_assignments_rows = [
        (row["customer_id"], int(row["cluster_id"]), row["cluster_label"])
        for _, row in cluster_data.iterrows()
    ]
    conn.executemany(
        "INSERT INTO customer_clusters VALUES (?,?,?)",
        cluster_assignments_rows,
    )

    # Insert cluster profiles
    cluster_profiles_df = pd.DataFrame(cluster_profiles)
    cluster_profiles_df.to_sql("cluster_profiles", conn, if_exists="append", index=False)

    return len(cluster_assignments_rows), len(cluster_profiles)


def print_counts(conn: sqlite3.Connection) -> None:
    """Print row counts for all tables."""
    tables = [
        "customers",
        "customer_snapshots",
        "model1_predictions",
        "model1_risk_factors",
        "model2_predictions",
        "model2_evidence",
        "customer_clusters",
        "cluster_profiles",
    ]
    print("\n--- Row Counts ---")
    for table in tables:
        count = conn.execute(f"SELECT COUNT(*) FROM {table}").fetchone()[0]
        print(f"  {table}: {count:,}")


def main() -> None:
    print("Building customer_retention.db from real processed source files...")
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
    print("Inserting real data...")

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

    n_clusters, n_profiles = perform_clustering_and_insert(conn, df)
    print(f"  customer_clusters: {n_clusters:,} rows")
    print(f"  cluster_profiles: {n_profiles:,} rows")

    conn.commit()
    print_counts(conn)
    conn.close()

    size_mb = DB_PATH.stat().st_size / (1024 * 1024)
    print(f"\nDone. Database: {DB_PATH} ({size_mb:.1f} MB)")


if __name__ == "__main__":
    main()
