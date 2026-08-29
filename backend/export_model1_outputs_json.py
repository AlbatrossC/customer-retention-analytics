import argparse
import json
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
MODEL1_OUTPUT_CSV = ROOT / "backend" / "outputs" / "model1_customer_outputs.csv"
MODEL1_OUTPUT_JSON = ROOT / "backend" / "outputs" / "model1_customer_outputs.json"
METADATA_PATH = (
    ROOT
    / "model_1"
    / "training_scripts"
    / "xgboost_model1"
    / "artifacts"
    / "model_metadata.json"
)

MODEL1_OUTPUT_COLUMNS = {
    "churn_probability",
    "risk_score",
    "churn_prediction",
    "risk_level",
    "top_risk_factors",
}


def json_safe(value: Any) -> Any:
    if value is None:
        return None
    try:
        if pd.isna(value):
            return None
    except Exception:
        pass
    if isinstance(value, np.integer):
        return int(value)
    if isinstance(value, np.floating):
        return float(value)
    return value


def load_model_features() -> list[str]:
    metadata = json.loads(METADATA_PATH.read_text(encoding="utf-8"))
    return metadata["features"]


def parse_top_risk_factors(value: Any) -> list[dict[str, Any]]:
    if not isinstance(value, str) or not value.strip():
        return []
    try:
        parsed = json.loads(value)
    except json.JSONDecodeError:
        return []
    if not isinstance(parsed, list):
        return []
    return parsed


def row_to_customer_json(row: pd.Series, model_features: list[str]) -> dict[str, Any]:
    record = row.to_dict()

    customer_data = {
        key: json_safe(value)
        for key, value in record.items()
        if key not in MODEL1_OUTPUT_COLUMNS
    }
    model1_input = {
        feature: json_safe(record.get(feature))
        for feature in model_features
    }
    model1_output = {
        "churn_probability": json_safe(record.get("churn_probability")),
        "risk_score": json_safe(record.get("risk_score")),
        "churn_prediction": json_safe(record.get("churn_prediction")),
        "risk_level": json_safe(record.get("risk_level")),
        "top_risk_factors": parse_top_risk_factors(record.get("top_risk_factors")),
    }

    return {
        "customer_id": json_safe(record.get("customer_id")),
        "customer_name": json_safe(record.get("customer_name")),
        "snapshot_date": json_safe(record.get("snapshot_date")),
        "customer_data": customer_data,
        "model1_input": model1_input,
        "model1_output": model1_output,
    }


def export_json(input_csv: Path, output_json: Path) -> list[dict[str, Any]]:
    if not input_csv.exists():
        raise FileNotFoundError(f"Missing CSV file: {input_csv}")

    print("Reading Model 1 CSV output...", flush=True)
    df = pd.read_csv(input_csv)
    model_features = load_model_features()

    print(f"Converting {len(df):,} customers to JSON...", flush=True)
    customers = [
        row_to_customer_json(row, model_features)
        for _, row in df.iterrows()
    ]

    output_json.parent.mkdir(parents=True, exist_ok=True)
    print("Saving JSON...", flush=True)
    output_json.write_text(
        json.dumps(customers, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    return customers


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Convert Model 1 customer CSV output into clean JSON."
    )
    parser.add_argument("--input", default=str(MODEL1_OUTPUT_CSV))
    parser.add_argument("--output", default=str(MODEL1_OUTPUT_JSON))
    args = parser.parse_args()

    customers = export_json(Path(args.input), Path(args.output))
    print("")
    print("JSON export saved.")
    print(f"Customers exported: {len(customers):,}")
    print(f"JSON path: {Path(args.output)}")


if __name__ == "__main__":
    main()
