"""
Insert Model 2 output from top_low_risk_customers.json into both databases.
Only inserts into model2_predictions and model2_evidence tables.
Does NOT modify any other tables (customers, customer_snapshots, model1_predictions, model1_risk_factors, customer_clusters, cluster_profiles).
"""

import json
import sqlite3
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DB_PATH = ROOT / "database" / "customer_retention.db"
LOW_RISK_JSON = ROOT / "pre_processing" / "outputs" / "top_low_risk_customers.json"


def insert_low_risk_model2(db_path: Path):
    """Insert model2 predictions and evidence for top low-risk customers."""
    print(f"\n--- Processing: {db_path.name} ---")

    # Load JSON
    with open(LOW_RISK_JSON, "r", encoding="utf-8") as f:
        data = json.load(f)

    customers = data["customers"]
    print(f"  JSON contains {len(customers)} low-risk customers")

    conn = sqlite3.connect(db_path)
    conn.execute("PRAGMA foreign_keys = ON")

    # Check current state
    existing_m2 = conn.execute("SELECT COUNT(*) FROM model2_predictions").fetchone()[0]
    existing_ev = conn.execute("SELECT COUNT(*) FROM model2_evidence").fetchone()[0]
    print(f"  Current model2_predictions rows: {existing_m2}")
    print(f"  Current model2_evidence rows: {existing_ev}")

    # Get existing model2 customer_ids to avoid duplicates
    existing_ids = set(
        row[0] for row in conn.execute("SELECT customer_id FROM model2_predictions").fetchall()
    )

    # Also verify these customers exist in the customers table
    all_customer_ids = set(
        row[0] for row in conn.execute("SELECT customer_id FROM customers").fetchall()
    )

    pred_rows = []
    evidence_rows = []
    skipped_existing = 0
    skipped_not_in_db = 0
    skipped_no_output = 0

    for c in customers:
        cid = c["customer_id"]

        # Skip if already has model2 prediction
        if cid in existing_ids:
            skipped_existing += 1
            continue

        # Skip if customer doesn't exist in the customers table
        if cid not in all_customer_ids:
            skipped_not_in_db += 1
            continue

        m2_out = c.get("model2_output")
        if not m2_out or not m2_out.get("ok"):
            skipped_no_output += 1
            continue

        prediction = m2_out.get("prediction")
        if not prediction:
            skipped_no_output += 1
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

    print(f"  Skipped (already in model2): {skipped_existing}")
    print(f"  Skipped (not in customers table): {skipped_not_in_db}")
    print(f"  Skipped (no valid model2 output): {skipped_no_output}")
    print(f"  New model2_predictions to insert: {len(pred_rows)}")
    print(f"  New model2_evidence to insert: {len(evidence_rows)}")

    if pred_rows:
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
        conn.commit()

    # Verify final state
    final_m2 = conn.execute("SELECT COUNT(*) FROM model2_predictions").fetchone()[0]
    final_ev = conn.execute("SELECT COUNT(*) FROM model2_evidence").fetchone()[0]
    print(f"  Final model2_predictions rows: {final_m2} (+{final_m2 - existing_m2})")
    print(f"  Final model2_evidence rows: {final_ev} (+{final_ev - existing_ev})")

    # Show coverage breakdown
    print(f"\n  Model2 coverage after update:")
    for row in conn.execute('''
        SELECT m1.risk_level, 
               COUNT(*) as total,
               SUM(CASE WHEN m2.customer_id IS NOT NULL THEN 1 ELSE 0 END) as with_m2,
               SUM(CASE WHEN m2.customer_id IS NULL THEN 1 ELSE 0 END) as without_m2
        FROM model1_predictions m1 
        LEFT JOIN model2_predictions m2 ON m1.customer_id = m2.customer_id 
        GROUP BY m1.risk_level
    '''):
        print(f"    {row[0]}: {row[2]}/{row[1]} have model2 ({row[3]} without)")

    conn.close()
    print(f"  Done: {db_path.name}")


def main():
    print("=" * 60)
    print("Inserting Model 2 outputs for top low-risk customers")
    print("=" * 60)

    if not LOW_RISK_JSON.exists():
        print(f"ERROR: JSON file not found: {LOW_RISK_JSON}")
        return

    # Process main database
    insert_low_risk_model2(DB_PATH)

    print("\n" + "=" * 60)
    print("All done! customer_retention.db updated.")
    print("=" * 60)


if __name__ == "__main__":
    main()
