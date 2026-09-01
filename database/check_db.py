import os
import sqlite3

def check_database():
    db_path = os.path.join(os.path.dirname(__file__), 'customer_retention.db')
    if not os.path.exists(db_path):
        print(f"Error: Database file not found at {db_path}")
        return

    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    print("=" * 50)
    print("CUSTOMER RETENTION SQLITE DATABASE REPORT")
    print("=" * 50)

    tables = [
        'customers',
        'customer_snapshots',
        'model1_predictions',
        'model1_risk_factors',
        'model2_predictions',
        'model2_evidence'
    ]

    for table in tables:
        cur.execute(f"SELECT COUNT(*) FROM {table}")
        count = cur.fetchone()[0]
        print(f"• {table:<25}: {count:>8,d} rows")

    print("\n--- Model 1 Risk Distribution ---")
    cur.execute("SELECT risk_level, COUNT(*) FROM model1_predictions GROUP BY risk_level ORDER BY COUNT(*) DESC")
    for risk, count in cur.fetchall():
        print(f"  - {risk:<10}: {count:>6,d} customers")

    print("\n--- Model 2 Top Reasons Diagnosed ---")
    cur.execute("SELECT primary_reason, COUNT(*) FROM model2_predictions GROUP BY primary_reason ORDER BY COUNT(*) DESC")
    for reason, count in cur.fetchall():
        print(f"  - {reason:<28}: {count:>6,d} customers")

    print("\n--- Model 2 Urgency Breakdown ---")
    cur.execute("SELECT urgency, COUNT(*) FROM model2_predictions GROUP BY urgency ORDER BY COUNT(*) DESC")
    for urgency, count in cur.fetchall():
        print(f"  - {urgency:<10}: {count:>6,d} customers")

    print("=" * 50)
    print("All checks passed successfully.")
    conn.close()

if __name__ == '__main__':
    check_database()
