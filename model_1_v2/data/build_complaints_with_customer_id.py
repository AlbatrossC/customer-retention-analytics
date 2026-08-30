import argparse
import json
from pathlib import Path

import pandas as pd


DATA_DIR = Path(__file__).resolve().parent
SOURCE_CUSTOMERS = DATA_DIR / "customers.csv"
OUTPUT_COMPLAINTS = DATA_DIR / "complaint_texts_with_customer_id.json"


def clean_value(value):
    if pd.isna(value):
        return None
    if hasattr(value, "item"):
        return value.item()
    return value


def build_complaints(source_path=SOURCE_CUSTOMERS, output_path=OUTPUT_COMPLAINTS):
    df = pd.read_csv(source_path)
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

    output_path.write_text(json.dumps(records, indent=2, ensure_ascii=False), encoding="utf-8")
    return len(records)


def main():
    parser = argparse.ArgumentParser(description="Create customer-linked complaint JSON for Model 1 v2 data.")
    parser.add_argument("--source", default=str(SOURCE_CUSTOMERS), help="Source customers.csv path.")
    parser.add_argument("--output", default=str(OUTPUT_COMPLAINTS), help="Output JSON path.")
    args = parser.parse_args()

    count = build_complaints(Path(args.source), Path(args.output))
    print(f"Wrote {count:,} complaint rows to {args.output}")


if __name__ == "__main__":
    main()
