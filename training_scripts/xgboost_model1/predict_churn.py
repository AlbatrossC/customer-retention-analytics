import json
from pathlib import Path
from typing import Any

import joblib
import numpy as np
import pandas as pd
import xgboost as xgb
from xgboost import XGBClassifier


ARTIFACT_DIR = Path(__file__).resolve().parent / "artifacts_candidate"
MODEL_PATH = ARTIFACT_DIR / "xgboost_model.json"
CALIBRATOR_PATH = ARTIFACT_DIR / "isotonic_calibrator.joblib"
METADATA_PATH = ARTIFACT_DIR / "model_metadata.json"

FORBIDDEN_INPUT_FIELDS = {
    "customer_id",
    "customer_name",
    "snapshot_date",
    "loyalty",
    "customer_yearly_value",
    "complaint_text",
    "churn_flag",
}


def _json_safe(value: Any) -> Any:
    if value is None or pd.isna(value):
        return None
    if isinstance(value, np.integer):
        return int(value)
    if isinstance(value, np.floating):
        return float(value)
    return value


def _load_artifacts():
    missing = [path for path in [MODEL_PATH, CALIBRATOR_PATH, METADATA_PATH] if not path.exists()]
    if missing:
        raise FileNotFoundError(
            f"Candidate artifacts not found: {missing}. "
            "Run python training_scripts/xgboost_model1/train_xgboost.py"
        )

    metadata = json.loads(METADATA_PATH.read_text(encoding="utf-8"))
    calibrator = joblib.load(CALIBRATOR_PATH)
    model = XGBClassifier()
    model.load_model(MODEL_PATH)
    return model, calibrator, metadata


def _validate_input(customer_data: dict, features: list[str]) -> None:
    input_fields = set(customer_data)
    missing = sorted(set(features) - input_fields)
    unknown = sorted(input_fields - set(features))
    forbidden = sorted(input_fields & FORBIDDEN_INPUT_FIELDS)

    if missing:
        raise ValueError(f"Missing required model input fields: {missing}")
    if forbidden:
        raise ValueError(f"Forbidden leakage fields are not valid prediction inputs: {forbidden}")
    if unknown:
        raise ValueError(f"Unknown prediction input fields: {unknown}")


def _prepare_row(
    customer_data: dict,
    features: list[str],
    categorical_features: list[str],
    numerical_features: list[str],
) -> pd.DataFrame:
    values = {
        feature: np.nan if customer_data[feature] is None else customer_data[feature]
        for feature in features
    }
    row = pd.DataFrame([values])
    for feature in numerical_features:
        row[feature] = pd.to_numeric(row[feature], errors="raise")
    for feature in categorical_features:
        row[feature] = row[feature].astype("category")
    return row


def _risk_level(probability: float, risk_bands: dict) -> str:
    if probability >= float(risk_bands["medium"]):
        return "High"
    if probability >= float(risk_bands["low"]):
        return "Medium"
    return "Low"


def _top_risk_factors(model: XGBClassifier, row: pd.DataFrame, customer_data: dict, top_n: int = 5) -> list[dict]:
    dmatrix = xgb.DMatrix(row, enable_categorical=True)
    contributions = model.get_booster().predict(dmatrix, pred_contribs=True)
    shap_values = np.asarray(contributions)[0, :-1]
    positive = [
        (feature, float(value))
        for feature, value in zip(row.columns.tolist(), shap_values)
        if value > 0
    ]
    positive.sort(key=lambda item: item[1], reverse=True)
    return [
        {"factor": feature, "value": _json_safe(customer_data[feature])}
        for feature, _ in positive[:top_n]
    ]


def predict_churn(customer_data: dict, threshold: float | None = None) -> dict:
    model, calibrator, metadata = _load_artifacts()
    features = metadata["features"]
    categorical_features = metadata["categorical_features"]
    numerical_features = metadata["numerical_features"]
    threshold = float(metadata["threshold"] if threshold is None else threshold)

    _validate_input(customer_data, features)
    row = _prepare_row(customer_data, features, categorical_features, numerical_features)

    raw_probability = float(model.predict_proba(row)[0, 1])
    calibrated_probability = float(calibrator.predict([raw_probability])[0])
    is_churn = calibrated_probability >= threshold

    return {
        "churn_probability": round(calibrated_probability * 100, 2),
        "churn_prediction": "Yes" if is_churn else "No",
        "risk_level": _risk_level(calibrated_probability, metadata["risk_bands"]),
        "top_risk_factors": _top_risk_factors(model, row, customer_data),
    }
