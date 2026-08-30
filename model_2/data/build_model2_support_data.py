import argparse
import json
from pathlib import Path

import pandas as pd


REPO_ROOT = Path(__file__).resolve().parents[2]
SOURCE_CUSTOMERS = REPO_ROOT / "model_1_v2" / "data" / "customers.csv"
OUTPUT_DIR = REPO_ROOT / "model_2" / "data"
OUTPUT_CUSTOMERS = OUTPUT_DIR / "customers.csv"
OUTPUT_COMPLAINTS = OUTPUT_DIR / "complaint_texts_with_customer_id.json"


def clean_value(value):
    if pd.isna(value):
        return None
    if hasattr(value, "item"):
        return value.item()
    return value


def build_support_data(source_path=SOURCE_CUSTOMERS, output_dir=OUTPUT_DIR):
    output_dir.mkdir(parents=True, exist_ok=True)
    df = pd.read_csv(source_path)
    df.to_csv(output_dir / "customers.csv", index=False)

    complaint_rows = df[df["complaint_text"].notna() & (df["complaint_text"].astype(str).str.strip() != "")]
    records = []
    for record in complaint_rows.to_dict(orient="records"):
        records.append(
            {
                "customer_id": clean_value(record["customer_id"]),
                "customer_name": clean_value(record["customer_name"]),
                "snapshot_date": clean_value(record["snapshot_date"]),
                "complaints_30d": clean_value(record["complaints_30d"]),
                "unresolved_complaints": clean_value(record["unresolved_complaints"]),
                "complaint_text": clean_value(record["complaint_text"]),
            }
        )

    (output_dir / "complaint_texts_with_customer_id.json").write_text(
        json.dumps(records, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    return len(df), len(records)


def main():
    parser = argparse.ArgumentParser(description="Copy Model 2 support data with customer-linked complaints.")
    parser.add_argument("--source", default=str(SOURCE_CUSTOMERS), help="Source customers.csv path.")
    parser.add_argument("--output-dir", default=str(OUTPUT_DIR), help="Output directory.")
    args = parser.parse_args()

    customer_count, complaint_count = build_support_data(Path(args.source), Path(args.output_dir))
    print(f"Wrote customers.csv with {customer_count:,} rows")
    print(f"Wrote complaint_texts_with_customer_id.json with {complaint_count:,} complaint rows")


if __name__ == "__main__":
    main()
