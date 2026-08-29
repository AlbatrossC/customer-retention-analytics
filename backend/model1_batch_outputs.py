import argparse
import json
import sys
from pathlib import Path
from typing import Any

import joblib
import numpy as np
import pandas as pd
import xgboost as xgb
from xgboost import XGBClassifier


ROOT = Path(__file__).resolve().parents[1]
MODEL1_SCRIPT_ROOT = ROOT / "model_1" / "training_scripts"
if str(MODEL1_SCRIPT_ROOT) not in sys.path:
    sys.path.insert(0, str(MODEL1_SCRIPT_ROOT))

CUSTOMERS_CSV = ROOT / "model_1" / "data" / "customers.csv"
ARTIFACT_DIR = ROOT / "model_1" / "training_scripts" / "xgboost_model1" / "artifacts"
MODEL_PATH = ARTIFACT_DIR / "xgboost_model.json"
CALIBRATOR_PATH = ARTIFACT_DIR / "isotonic_calibrator.joblib"
METADATA_PATH = ARTIFACT_DIR / "model_metadata.json"
OUTPUT_CSV = ROOT / "backend" / "outputs" / "model1_customer_outputs.csv"


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


def require_file(path: Path) -> None:
    if not path.exists():
        raise FileNotFoundError(f"Missing file: {path}")


def load_artifacts():
    for path in [CUSTOMERS_CSV, MODEL_PATH, CALIBRATOR_PATH, METADATA_PATH]:
        require_file(path)

    metadata = json.loads(METADATA_PATH.read_text(encoding="utf-8"))
    calibrator = joblib.load(CALIBRATOR_PATH)
    model = XGBClassifier()
    model.load_model(MODEL_PATH)
    return model, calibrator, metadata


def risk_level(probability: float, risk_bands: dict[str, Any]) -> str:
    if probability >= float(risk_bands["medium"]):
        return "High"
    if probability >= float(risk_bands["low"]):
        return "Medium"
    return "Low"


def risk_score(probability: float) -> float:
    probability = min(max(float(probability), 0.0), 1.0)
    if probability < 0.10:
        score = (probability / 0.10) * 30
    elif probability < 0.20:
        score = 30 + ((probability - 0.10) / 0.10) * 40
    else:
        score = 70 + ((probability - 0.20) / 0.80) * 30
    return round(min(max(score, 0.0), 100.0), 2)


def prepare_feature_frame(df: pd.DataFrame, metadata: dict[str, Any]) -> pd.DataFrame:
    features = metadata["features"]
    frame = df[features].copy()

    for feature in metadata["categorical_features"]:
        frame[feature] = frame[feature].astype("category")

    for feature in metadata["numerical_features"]:
        frame[feature] = pd.to_numeric(frame[feature], errors="raise")

    return frame


def top_risk_factors_from_values(
    feature_names: list[str],
    shap_values: np.ndarray,
    customer_data: dict[str, Any],
    top_n: int = 5,
) -> list[dict[str, Any]]:
    positive = [
        (feature, float(value))
        for feature, value in zip(feature_names, shap_values)
        if value > 0
    ]
    positive.sort(key=lambda item: item[1], reverse=True)
    return [
        {"factor": feature, "value": json_safe(customer_data.get(feature))}
        for feature, _ in positive[:top_n]
    ]


def batch_top_risk_factors(
    model: XGBClassifier,
    feature_frame: pd.DataFrame,
    records: list[dict[str, Any]],
    top_n: int = 5,
) -> list[str]:
    dmatrix = xgb.DMatrix(feature_frame, enable_categorical=True)
    contributions = model.get_booster().predict(dmatrix, pred_contribs=True)
    shap_values = np.asarray(contributions)[:, :-1]
    feature_names = feature_frame.columns.tolist()

    return [
        json.dumps(top_risk_factors_from_values(feature_names, row_values, record, top_n))
        for row_values, record in zip(shap_values, records)
    ]


def latest_customer_rows(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["snapshot_date"] = pd.to_datetime(df["snapshot_date"])
    return (
        df.sort_values(["customer_id", "snapshot_date"])
        .groupby("customer_id", as_index=False)
        .tail(1)
        .sort_values("customer_id")
        .reset_index(drop=True)
    )


def predict_batch(
    model: XGBClassifier,
    calibrator: Any,
    metadata: dict[str, Any],
    prediction_df: pd.DataFrame,
) -> pd.DataFrame:
    threshold = float(metadata["threshold"])
    feature_frame = prepare_feature_frame(prediction_df, metadata)
    records = prediction_df[metadata["features"]].to_dict("records")

    print("Predicting churn probabilities...", flush=True)
    raw_probabilities = model.predict_proba(feature_frame)[:, 1]
    probabilities = calibrator.predict(raw_probabilities)

    print("Finding top risk factors...", flush=True)
    factor_json = batch_top_risk_factors(model, feature_frame, records)

    return pd.DataFrame(
        {
            "churn_probability": [round(float(probability) * 100, 2) for probability in probabilities],
            "risk_score": [risk_score(float(probability)) for probability in probabilities],
            "churn_prediction": [
                "Yes" if float(probability) >= threshold else "No"
                for probability in probabilities
            ],
            "risk_level": [
                risk_level(float(probability), metadata["risk_bands"])
                for probability in probabilities
            ],
            "top_risk_factors": factor_json,
        }
    )


def build_outputs(use_all_rows: bool, output_csv: Path) -> pd.DataFrame:
    print("Loading Model 1 artifacts...", flush=True)
    model, calibrator, metadata = load_artifacts()

    print("Reading customers.csv...", flush=True)
    df = pd.read_csv(CUSTOMERS_CSV)
    prediction_df = df.copy() if use_all_rows else latest_customer_rows(df)

    print(f"Rows to predict: {len(prediction_df):,}", flush=True)
    outputs = predict_batch(model, calibrator, metadata, prediction_df)

    result = pd.concat([prediction_df.reset_index(drop=True), outputs], axis=1)
    output_csv.parent.mkdir(parents=True, exist_ok=True)
    print("Saving CSV...", flush=True)
    result.to_csv(output_csv, index=False)
    return result


def print_counts(result: pd.DataFrame) -> None:
    total = len(result)
    risk_counts = result["risk_level"].value_counts().reindex(["High", "Medium", "Low"], fill_value=0)
    prediction_counts = result["churn_prediction"].value_counts().reindex(["Yes", "No"], fill_value=0)

    print("")
    print("Model 1 batch output saved.")
    print(f"Total predicted rows/customers: {total:,}")
    print("")
    print("Risk level counts:")
    for level, count in risk_counts.items():
        percent = (count / total) * 100 if total else 0
        print(f"- {level}: {count:,} ({percent:.2f}%)")

    print("")
    print("Churn prediction counts:")
    for label, count in prediction_counts.items():
        percent = (count / total) * 100 if total else 0
        print(f"- {label}: {count:,} ({percent:.2f}%)")

    print("")
    print(f"Average churn probability: {result['churn_probability'].mean():.2f}%")
    print(f"Average risk score: {result['risk_score'].mean():.2f}")


def main():
    parser = argparse.ArgumentParser(description="Generate Model 1 outputs for customers.csv.")
    parser.add_argument(
        "--all-rows",
        action="store_true",
        help="Predict every monthly row instead of only the latest row for each customer.",
    )
    parser.add_argument(
        "--output",
        default=str(OUTPUT_CSV),
        help="Output CSV path.",
    )
    args = parser.parse_args()

    result = build_outputs(use_all_rows=args.all_rows, output_csv=Path(args.output))
    print_counts(result)
    print("")
    print(f"CSV path: {Path(args.output)}")


if __name__ == "__main__":
    main()
