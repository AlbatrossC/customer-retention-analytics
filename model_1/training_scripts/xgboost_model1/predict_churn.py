import json
from pathlib import Path
import sys
from typing import Any

import joblib
import numpy as np
import pandas as pd
import xgboost as xgb
from xgboost import XGBClassifier


SCRIPT_ROOT = Path(__file__).resolve().parents[1]
if str(SCRIPT_ROOT) not in sys.path:
    sys.path.insert(0, str(SCRIPT_ROOT))

from prediction_input import normalize_prediction_input, prepare_feature_row


ARTIFACT_DIR = Path(__file__).resolve().parent / "artifacts"
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
            f"XGBoost artifacts not found: {missing}. "
            "Run python model_1/training_scripts/xgboost_model1/train_xgboost.py"
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


def _risk_level(probability: float, risk_bands: dict) -> str:
    if probability >= float(risk_bands["medium"]):
        return "High"
    if probability >= float(risk_bands["low"]):
        return "Medium"
    return "Low"


def _risk_score(probability: float) -> float:
    probability = min(max(float(probability), 0.0), 1.0)
    if probability < 0.10:
        score = (probability / 0.10) * 30
    elif probability < 0.20:
        score = 30 + ((probability - 0.10) / 0.10) * 40
    else:
        score = 70 + ((probability - 0.20) / 0.80) * 30
    return round(min(max(score, 0.0), 100.0), 2)


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
    threshold = float(metadata["threshold"] if threshold is None else threshold)

    customer_data = normalize_prediction_input(customer_data, features)
    _validate_input(customer_data, features)
    row = prepare_feature_row(customer_data, metadata)

    raw_probability = float(model.predict_proba(row)[0, 1])
    model_probability = float(calibrator.predict([raw_probability])[0])
    is_churn = model_probability >= threshold

    return {
        "churn_probability": round(model_probability * 100, 2),
        "risk_score": _risk_score(model_probability),
        "churn_prediction": "Yes" if is_churn else "No",
        "risk_level": _risk_level(model_probability, metadata["risk_bands"]),
        "top_risk_factors": _top_risk_factors(model, row, customer_data),
    }
