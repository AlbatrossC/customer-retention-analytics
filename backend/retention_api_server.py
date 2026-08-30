import hashlib
import json
import re
import sys
import time
import urllib.error
import urllib.request
from contextlib import asynccontextmanager
from datetime import datetime
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


ROOT = Path(__file__).resolve().parents[1]
MODEL1_SCRIPT_ROOT = ROOT / "model_1" / "training_scripts"
if str(MODEL1_SCRIPT_ROOT) not in sys.path:
    sys.path.insert(0, str(MODEL1_SCRIPT_ROOT))
MODEL1_V2_SCRIPT_ROOT = ROOT / "model_1_v2" / "training_scripts" / "xgboost_model1_v2"
if str(MODEL1_V2_SCRIPT_ROOT) not in sys.path:
    sys.path.insert(0, str(MODEL1_V2_SCRIPT_ROOT))

from build_features import BEHAVIOR_FEATURES, PROFILE_FEATURES, build_feature_row
from model_v2_runtime import (
    apply_probability_mode,
    load_calibrators,
    load_v2,
    mean_shap_contributions,
    predict_raw_proba,
    prepare_x,
)


USE_MODEL1 = True
USE_MODEL2 = True

MODEL1_ARTIFACT_DIR = ROOT / "model_1_v2" / "training_scripts" / "xgboost_model1_v2" / "artifacts"
MODEL1_PATH = MODEL1_ARTIFACT_DIR / "xgboost_model_v2.json"
CALIBRATOR_PATH = MODEL1_ARTIFACT_DIR / "calibrator_v2.joblib"
METADATA_PATH = MODEL1_ARTIFACT_DIR / "model_metadata_v2.json"
MODEL2_PATH = ROOT / "model_2" / "model 2 demo" / "model2_retention_0.5bv2.gguf"

HOST = "127.0.0.1"
PORT = 8000

MODEL2_N_CTX = 2048
MODEL2_N_THREADS = 4
MODEL2_TEMPERATURE = 0.3
MODEL2_TOP_P = 0.9
MODEL2_REPEAT_PENALTY = 1.08

# Windows Smart App Control blocks the unsigned llama.dll / ggml-*.dll shipped in
# the llama-cpp-python wheel (WinError 4551). The "ollama" backend runs the same
# GGUF inside Ollama's signed binaries and talks to it over localhost HTTP, so no
# unsigned code is loaded into this process. Use "llama_cpp" only on machines
# where Smart App Control is off.
MODEL2_BACKEND = "ollama"
OLLAMA_HOST = "http://127.0.0.1:11434"
OLLAMA_MODEL = "retention-0.5bv2"
MODEL2_TIMEOUT = 180
# Hash MODEL2_PATH at startup and refuse to serve unless Ollama holds that exact
# GGUF. Costs ~1s for the 380 MB file.
MODEL2_VERIFY_DIGEST = True

FORBIDDEN_INPUT_FIELDS = {
    "customer_id",
    "customer_name",
    "snapshot_date",
    "loyalty",
    "customer_yearly_value",
    "complaint_text",
    "churn_flag",
}

ACTIONABLE_FEATURES = {
    "latest_days_since_last_transaction",
    "latest_balance_change_30d",
    "latest_transaction_change_30d",
    "latest_card_spend_change_30d",
    "latest_app_login_change_30d",
    "latest_salary_missing_days",
    "latest_external_transfer_change_30d",
    "latest_upi_share_of_spend",
    "latest_fd_maturing_in_30d",
    "latest_products_dropped_90d",
    "latest_complaints_30d",
    "latest_unresolved_complaints",
    "latest_failed_transactions_30d",
    "latest_avg_resolution_time_hrs",
    "latest_emi_bounce_30d",
}

BLOCKED_EXPLANATION_FEATURES = {
    "months_observed",
    "tenure_months",
    "customer_segment",
    "income_regularity",
    "products_count",
    "has_credit_card",
    "has_loan",
}

ACTIONABLE_MARKERS = [
    "balance",
    "transaction",
    "card_spend",
    "app_login",
    "external_transfer",
    "complaints",
    "failed_transactions",
    "days_since_last_transaction",
    "fd_maturing",
    "emi_bounce",
    "salary_missing",
    "resolution_time",
    "products_dropped",
    "upi_share",
]

model1 = None
calibrator = None
metadata = None
model2 = None


class Model1Request(BaseModel):
    profile: dict[str, Any] | None = None
    monthly_history: list[dict[str, Any]] | None = None
    customer: dict[str, Any] | None = None
    threshold: float | None = None
    customer_id: str | None = None
    customer_name: str | None = None
    snapshot_date: str | None = None
    prediction_date: str | None = None
    target_month: str | None = None


class Model2Request(BaseModel):
    payload: dict[str, Any]
    customer_id: str | None = None
    customer_name: str | None = None
    snapshot_date: str | None = None


class BothRequest(BaseModel):
    profile: dict[str, Any] | None = None
    monthly_history: list[dict[str, Any]] | None = None
    customer: dict[str, Any] | None = None
    extra_context: dict[str, Any] | None = None
    threshold: float | None = None
    customer_id: str | None = None
    customer_name: str | None = None
    snapshot_date: str | None = None
    prediction_date: str | None = None
    target_month: str | None = None


class LoadModel2Request(BaseModel):
    model_path: str


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


def validate_model1_input(customer_data: dict[str, Any], features: list[str]) -> None:
    input_fields = set(customer_data)
    missing = sorted(set(features) - input_fields)
    unknown = sorted(input_fields - set(features))
    forbidden = sorted(input_fields & FORBIDDEN_INPUT_FIELDS)

    if missing:
        raise ValueError(f"Missing required fields: {missing}")
    if forbidden:
        raise ValueError(f"Forbidden fields: {forbidden}")
    if unknown:
        raise ValueError(f"Unknown fields: {unknown}")


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


def top_risk_factors(customer_data: dict[str, Any], row: pd.DataFrame, top_n: int = 5) -> list[dict[str, Any]]:
    shap_values = mean_shap_contributions(model1, row)[0]
    factors = []

    for feature, contribution in zip(row.columns.tolist(), shap_values):
        if feature in BLOCKED_EXPLANATION_FEATURES or contribution <= 0:
            continue
        if feature not in ACTIONABLE_FEATURES and not any(marker in feature for marker in ACTIONABLE_MARKERS):
            continue
        value = row.iloc[0][feature]
        if pd.isna(value):
            continue
        factors.append(
            {
                "factor": feature,
                "value": json_safe(value),
                "message": factor_message(feature, value),
                "contribution": float(contribution),
            }
        )

    factors.sort(key=lambda item: item["contribution"], reverse=True)
    return factors[:top_n]


def load_model1() -> None:
    global model1, calibrator, metadata
    for path in [CALIBRATOR_PATH, METADATA_PATH]:
        require_file(path)

    metadata = json.loads(METADATA_PATH.read_text(encoding="utf-8"))
    calibrator = load_calibrators(MODEL1_ARTIFACT_DIR)
    model1 = load_v2(MODEL1_ARTIFACT_DIR, metadata)
    print("Model 1 v2 loaded")


def bytes_to_mb(value: int | None) -> float | None:
    if value is None:
        return None
    return round(value / (1024 * 1024), 2)


def model1_runtime_info() -> dict[str, Any]:
    return {
        "enabled": USE_MODEL1,
        "loaded": model1 is not None,
        "model_name": metadata.get("model_name") if metadata else "model_1_v2",
        "model_type": "xgboost_ensemble",
        "model_path": str(MODEL1_PATH),
        "calibrator_path": str(CALIBRATOR_PATH),
        "metadata_path": str(METADATA_PATH),
        "feature_count": len(metadata["features"]) if metadata else None,
        "threshold": metadata.get("selected_threshold", metadata.get("threshold")) if metadata else None,
        "question_answered": metadata.get("question_answered") if metadata else None,
    }


def model2_runtime_info() -> dict[str, Any]:
    info = {
        "enabled": USE_MODEL2,
        "loaded": model2 is not None,
        "backend": MODEL2_BACKEND,
        "gguf_path": str(MODEL2_PATH),
        "gguf_exists": MODEL2_PATH.exists(),
        "temperature": MODEL2_TEMPERATURE,
        "top_p": MODEL2_TOP_P,
        "repeat_penalty": MODEL2_REPEAT_PENALTY,
        "n_ctx": MODEL2_N_CTX,
        "n_threads": MODEL2_N_THREADS if MODEL2_BACKEND != "ollama" else None,
    }
    if MODEL2_BACKEND == "ollama":
        info.update(
            {
                "ollama_host": OLLAMA_HOST,
                "ollama_model": OLLAMA_MODEL,
                "verify_digest": MODEL2_VERIFY_DIGEST,
                "ollama_runtime": ollama_runtime_info(),
            }
        )
    return info


def ollama_runtime_info() -> dict[str, Any]:
    try:
        running = ollama_get("/api/ps", timeout=5).get("models", [])
    except Exception as exc:
        return {"running": False, "error": str(exc)}

    expected_names = {OLLAMA_MODEL, f"{OLLAMA_MODEL}:latest"}
    active = next(
        (
            item
            for item in running
            if item.get("name") in expected_names or item.get("model") in expected_names
        ),
        None,
    )
    if active is None:
        return {
            "running": False,
            "loaded_models": [item.get("name") or item.get("model") for item in running],
        }

    size = active.get("size")
    size_vram = active.get("size_vram")
    gpu_percent = round((size_vram / size) * 100, 2) if size and size_vram is not None else None
    processor = "CPU"
    if gpu_percent is not None and gpu_percent > 0:
        processor = f"{gpu_percent:g}% GPU"

    return {
        "running": True,
        "name": active.get("name") or active.get("model"),
        "processor": processor,
        "gpu_percent": gpu_percent,
        "size_mb": bytes_to_mb(size),
        "vram_mb": bytes_to_mb(size_vram),
        "context_length": active.get("context_length"),
        "expires_at": active.get("expires_at"),
        "details": active.get("details", {}),
    }


def customer_request_info(request: Model1Request | Model2Request | BothRequest) -> dict[str, Any]:
    info = {
        "customer_id": request.customer_id,
        "customer_name": request.customer_name,
        "snapshot_date": request.snapshot_date,
    }
    if isinstance(request, BothRequest):
        profile = (request.extra_context or {}).get("customer_profile", {})
        info.update(
            {
                "segment": profile.get("segment"),
                "value_tier": profile.get("value_tier"),
                "risk_group": (request.extra_context or {}).get("risk_group"),
                "input_feature_count": len(request.customer or {}),
                "history_months": len(request.monthly_history or []),
            }
        )
    elif isinstance(request, Model1Request):
        info["input_feature_count"] = len(request.customer or {})
        info["history_months"] = len(request.monthly_history or [])
    elif isinstance(request, Model2Request):
        info["payload_type"] = request.payload.get("type")
    return info


def response_meta(
    endpoint: str,
    started_at: float,
    request: Model1Request | Model2Request | BothRequest,
    timings_ms: dict[str, float] | None = None,
) -> dict[str, Any]:
    return {
        "endpoint": endpoint,
        "served_at": datetime.now().isoformat(timespec="seconds"),
        "elapsed_ms": round((time.perf_counter() - started_at) * 1000, 2),
        "timings_ms": timings_ms or {},
        "customer": customer_request_info(request),
        "model1": model1_runtime_info(),
        "model2": model2_runtime_info(),
    }


def ollama_get(route: str, timeout: int = 5) -> dict[str, Any]:
    with urllib.request.urlopen(f"{OLLAMA_HOST}{route}", timeout=timeout) as response:
        return json.loads(response.read())


def ollama_post(route: str, payload: dict[str, Any], timeout: int = 60) -> dict[str, Any]:
    request = urllib.request.Request(
        f"{OLLAMA_HOST}{route}",
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
    )
    with urllib.request.urlopen(request, timeout=timeout) as response:
        return json.loads(response.read())


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def verify_ollama_is_finetune() -> None:
    """Refuse to start unless Ollama serves exactly the GGUF at MODEL2_PATH.

    `ollama create` stores a GGUF verbatim as a blob, so the model layer digest
    equals the file's sha256. Comparing the two catches a stale registration
    (GGUF retrained but `ollama create` never re-run) and any name collision
    with a base model pulled from the registry.
    """
    require_file(MODEL2_PATH)
    info = ollama_post("/api/show", {"model": OLLAMA_MODEL}, timeout=30)

    parent = (info.get("details") or {}).get("parent_model") or ""
    if parent:
        raise RuntimeError(
            f"Ollama model '{OLLAMA_MODEL}' is derived from '{parent}', not the fine-tuned GGUF"
        )

    digests = set(re.findall(r"sha256[-:]([0-9a-f]{64})", info.get("modelfile", "")))
    expected = file_sha256(MODEL2_PATH)
    if expected not in digests:
        raise RuntimeError(
            f"Ollama model '{OLLAMA_MODEL}' does not serve {MODEL2_PATH.name} "
            f"(expected sha256 {expected}, found {sorted(digests)}). "
            f"Re-run: ollama create {OLLAMA_MODEL} -f Modelfile"
        )
    print(f"Model 2 fine-tune verified: sha256 {expected[:16]}... == {MODEL2_PATH.name}")


def ollama_chat(messages: list[dict[str, str]]) -> str:
    body = json.dumps(
        {
            "model": OLLAMA_MODEL,
            "messages": messages,
            "temperature": MODEL2_TEMPERATURE,
            "top_p": MODEL2_TOP_P,
            "repeat_penalty": MODEL2_REPEAT_PENALTY,
            "stream": False,
        }
    ).encode("utf-8")
    request = urllib.request.Request(
        f"{OLLAMA_HOST}/v1/chat/completions",
        data=body,
        headers={"Content-Type": "application/json"},
    )
    with urllib.request.urlopen(request, timeout=MODEL2_TIMEOUT) as response:
        output = json.loads(response.read())
    return output["choices"][0]["message"]["content"]


def load_model2_ollama() -> None:
    global model2
    try:
        tags = ollama_get("/api/tags")
    except (urllib.error.URLError, OSError) as exc:
        raise RuntimeError(f"Ollama is not reachable at {OLLAMA_HOST}: {exc}") from exc

    names = {model["name"] for model in tags.get("models", [])}
    if OLLAMA_MODEL not in names and f"{OLLAMA_MODEL}:latest" not in names:
        raise RuntimeError(
            f"Ollama model '{OLLAMA_MODEL}' not found. Available: {sorted(names)}. "
            f"Create it with: ollama create {OLLAMA_MODEL} -f Modelfile"
        )
    if MODEL2_VERIFY_DIGEST:
        verify_ollama_is_finetune()

    model2 = OLLAMA_MODEL
    print(f"Model 2 ready via Ollama ({OLLAMA_MODEL})")


def load_model2(path: Path | None = None) -> None:
    global model2, MODEL2_PATH
    if MODEL2_BACKEND == "ollama":
        load_model2_ollama()
        return

    if path is not None:
        MODEL2_PATH = path
    require_file(MODEL2_PATH)
    from llama_cpp import Llama

    model2 = Llama(
        model_path=str(MODEL2_PATH),
        n_ctx=MODEL2_N_CTX,
        n_threads=MODEL2_N_THREADS,
        verbose=False,
    )
    print("Model 2 loaded")


def factor_message(feature: str, value: Any) -> str:
    if value is None or pd.isna(value):
        return "This signal increased churn risk."
    if "salary_missing" in feature and float(value) > 0:
        return "Salary or pension was delayed recently."
    if "resolution_time" in feature and float(value) > 0:
        return "Recent complaints took longer to resolve."
    if "products_dropped" in feature and float(value) > 0:
        return "Customer has dropped products recently."
    if "upi_share" in feature and float(value) > 0:
        return "A larger share of spending is happening through UPI."
    if "balance" in feature and float(value) < 0:
        return "Balance has been falling across recent months."
    if "transaction" in feature and float(value) < 0:
        return "Transaction activity has been falling across recent months."
    if "card_spend" in feature and float(value) < 0:
        return "Card spending has been falling across recent months."
    if "app_login" in feature and float(value) < 0:
        return "App usage has been falling across recent months."
    if "external_transfer" in feature and float(value) > 0:
        return "External transfers have increased."
    if "complaints" in feature and float(value) > 0:
        return "Customer has recent complaint activity."
    if "failed_transactions" in feature and float(value) > 0:
        return "Customer has recent failed transactions."
    if "days_since_last_transaction" in feature and float(value) > 0:
        return "Customer has gone longer without transacting."
    if "fd_maturing" in feature and float(value) > 0:
        return "Customer has a fixed deposit maturing soon."
    if "emi_bounce" in feature and float(value) > 0:
        return "Customer has a recent EMI bounce."
    return "This signal increased churn risk."


def latest_customer_from_request(request: Model1Request | BothRequest) -> dict[str, Any]:
    if request.customer:
        return request.customer
    if not request.monthly_history:
        return {}
    latest = dict(request.monthly_history[-1])
    latest.update(request.profile or {})
    return latest


def request_to_v2_row(request: Model1Request | BothRequest) -> tuple[pd.DataFrame, dict[str, Any]]:
    profile = dict(request.profile or {})
    monthly_history = request.monthly_history

    if not monthly_history and request.customer:
        profile = {feature: request.customer.get(feature) for feature in PROFILE_FEATURES}
        monthly_history = [
            {
                "snapshot_date": request.prediction_date or request.snapshot_date,
                **{feature: request.customer.get(feature) for feature in BEHAVIOR_FEATURES},
            }
        ]
    if not monthly_history:
        raise ValueError("Model 1 v2 requires monthly_history with at least one monthly record.")

    missing_profile = sorted(set(PROFILE_FEATURES) - set(profile))
    if missing_profile:
        raise ValueError(f"Missing required profile fields for Model 1 v2: {missing_profile}")

    history = pd.DataFrame(monthly_history).copy()
    missing_history = sorted(set(BEHAVIOR_FEATURES) - set(history.columns))
    if missing_history:
        raise ValueError(f"Missing required monthly_history fields for Model 1 v2: {missing_history}")

    prediction_date = request.prediction_date or request.snapshot_date
    if prediction_date is None:
        prediction_date = history.iloc[-1].get("snapshot_date")
    if prediction_date is None:
        raise ValueError("Model 1 v2 requires prediction_date, snapshot_date, or snapshot_date in monthly_history.")

    history["snapshot_date"] = pd.to_datetime(history.get("snapshot_date", prediction_date))
    history = history.sort_values("snapshot_date").tail(6).reset_index(drop=True)

    for feature in PROFILE_FEATURES:
        history[feature] = profile[feature]
    history["customer_id"] = request.customer_id
    history["customer_name"] = request.customer_name

    target_month = request.target_month
    if target_month is None:
        target_month = (pd.to_datetime(prediction_date) + pd.DateOffset(months=1)).date().isoformat()
    next_row = pd.Series({"snapshot_date": pd.to_datetime(target_month), "churn_flag": 0})

    row = pd.DataFrame([build_feature_row(history, next_row)])
    latest_customer = latest_customer_from_request(request)
    return row, latest_customer


def predict_model1(request: Model1Request | BothRequest) -> dict[str, Any]:
    if model1 is None or calibrator is None or metadata is None:
        raise RuntimeError("Model 1 v2 is not loaded")

    threshold = float(metadata.get("selected_threshold", metadata["threshold"]) if request.threshold is None else request.threshold)
    row, customer_data = request_to_v2_row(request)
    x_row = prepare_x(row, metadata)

    raw_probability = float(predict_raw_proba(model1, x_row)[0])
    probability = float(apply_probability_mode([raw_probability], calibrator, metadata["probability_mode"])[0])
    return {
        "churn_probability": round(probability * 100, 2),
        "raw_churn_probability": round(raw_probability * 100, 2),
        "probability_mode": metadata["probability_mode"],
        "risk_score": risk_score(probability),
        "churn_prediction": "Yes" if probability >= threshold else "No",
        "risk_level": risk_level(probability, metadata["risk_bands"]),
        "top_risk_factors": top_risk_factors(customer_data, x_row),
    }


def pct_message(label: str, value: Any) -> str:
    value = float(value)
    direction = "fell" if value < 0 else "rose"
    return f"{label} {direction} by {abs(value):.2f}% in the last 30 days."


def count_message(single: str, plural: str, value: Any) -> str:
    count = int(float(value))
    label = single if count == 1 else plural
    return f"Customer had {count} {label}."


def risk_signal_message(field: str, value: Any) -> str | None:
    if value is None:
        return None

    if field == "balance_change_30d":
        return pct_message("Balance", value)
    if field == "transaction_change_30d":
        return pct_message("Transactions", value)
    if field == "card_spend_change_30d":
        return pct_message("Card spend", value)
    if field == "app_login_change_30d":
        return pct_message("App logins", value)
    if field == "external_transfer_change_30d":
        return pct_message("External transfers", value)
    if field == "days_since_last_transaction":
        count = int(float(value))
        unit = "day" if count == 1 else "days"
        return f"Customer has not transacted for {count} {unit}."
    if field == "failed_transactions_30d":
        return count_message("failed transaction in the last 30 days", "failed transactions in the last 30 days", value)
    if field == "complaints_30d":
        return count_message("complaint in the last 30 days", "complaints in the last 30 days", value)
    if field == "unresolved_complaints":
        return count_message("unresolved complaint", "unresolved complaints", value)
    if field == "salary_missing_days":
        return f"Salary was missing for {int(float(value))} days."
    if field == "fd_maturing_in_30d" and int(float(value)) > 0:
        return "Fixed deposit is maturing within 30 days."
    if field == "products_dropped_90d":
        return count_message("product dropped in the last 90 days", "products dropped in the last 90 days", value)
    if field == "emi_bounce_30d":
        return count_message("EMI bounce in the last 30 days", "EMI bounces in the last 30 days", value)
    if field == "products_count":
        return f"Customer currently has {int(float(value))} bank product(s)."
    if field == "income_regularity":
        return f"Income regularity is {value}."
    if field == "has_loan" and int(float(value)) > 0:
        return "Customer has an active loan relationship."
    if field == "has_credit_card" and int(float(value)) > 0:
        return "Customer has a credit card relationship."
    return None


def is_risky_signal(field: str, value: Any) -> bool:
    if value is None:
        return False

    if field == "income_regularity":
        return str(value).lower() in {"irregular", "seasonal"}

    try:
        number = float(value)
    except (TypeError, ValueError):
        return False

    if field in {"balance_change_30d", "transaction_change_30d", "card_spend_change_30d"}:
        return number < -5
    if field == "app_login_change_30d":
        return number < -10
    if field == "external_transfer_change_30d":
        return number > 20
    if field == "days_since_last_transaction":
        return number >= 10
    if field in {
        "failed_transactions_30d",
        "complaints_30d",
        "unresolved_complaints",
        "salary_missing_days",
        "fd_maturing_in_30d",
        "products_dropped_90d",
        "emi_bounce_30d",
    }:
        return number > 0
    if field == "products_count":
        return number <= 1
    return False


def build_main_signals(model1_output: dict[str, Any], customer: dict[str, Any]) -> list[dict[str, Any]]:
    signals = []
    used = set()
    ignored_fields = {"age", "branch_code", "card_colour", "customer_segment"}

    for item in model1_output.get("top_risk_factors", []):
        field = item.get("factor")
        value = item.get("value")
        if field in ignored_fields:
            continue
        if item.get("message") and (
            field in ACTIONABLE_FEATURES or any(marker in str(field) for marker in ACTIONABLE_MARKERS)
        ):
            signals.append(
                {
                    "field": field,
                    "value": json_safe(value),
                    "message": item["message"],
                }
            )
            used.add(field)
            continue
        if not is_risky_signal(field, value):
            continue
        message = risk_signal_message(field, value)
        if message:
            signals.append({"field": field, "value": value, "message": message})
            used.add(field)

    backup_fields = [
        "balance_change_30d",
        "transaction_change_30d",
        "card_spend_change_30d",
        "days_since_last_transaction",
        "failed_transactions_30d",
        "complaints_30d",
        "unresolved_complaints",
        "salary_missing_days",
        "fd_maturing_in_30d",
        "products_dropped_90d",
        "emi_bounce_30d",
    ]
    for field in backup_fields:
        if len(signals) >= 5:
            break
        if field in used or field not in customer:
            continue
        value = customer.get(field)
        if not is_risky_signal(field, value):
            continue
        message = risk_signal_message(field, value)
        if message:
            signals.append({"field": field, "value": json_safe(value), "message": message})
            used.add(field)

    if not signals:
        probability = model1_output.get("churn_probability")
        if probability is not None:
            signals.append(
                {
                    "field": "model1_v2_risk_level",
                    "value": probability,
                    "message": f"Model 1 v2 shows low churn risk at {float(probability):.2f}%.",
                }
            )

    return signals[:5]


def trend_summary(trend: dict[str, Any]) -> dict[str, Any]:
    messages = []
    overall_direction = trend.get("overall_direction", "unknown")
    if overall_direction != "unknown":
        messages.append(f"Overall recent direction is {overall_direction}.")

    for field in ["balance_change_30d", "days_since_last_transaction", "complaints_30d", "external_transfer_change_30d"]:
        values = trend.get(field)
        if not isinstance(values, list) or not values:
            continue
        latest = values[-1]
        if not is_risky_signal(field, latest):
            continue
        message = risk_signal_message(field, latest)
        if message:
            messages.append(message)

    return {
        "overall_direction": overall_direction,
        "messages": messages[:5],
    }


def suggested_actions_for(customer: dict[str, Any], risk_level_value: str, complaint_text: str | None) -> list[str]:
    actions = []
    if risk_level_value == "Low":
        actions.append("Monitor only with light-touch service check-in")
    else:
        actions.append("Relationship manager call")

    if complaint_text or int(customer.get("complaints_30d") or 0) > 0 or int(customer.get("unresolved_complaints") or 0) > 0:
        actions.append("Complaint follow-up")
    if int(customer.get("failed_transactions_30d") or 0) > 0:
        actions.append("Resolve failed transactions")
    if int(customer.get("fd_maturing_in_30d") or 0) > 0:
        actions.append("FD renewal or savings discussion")
    if float(customer.get("app_login_change_30d") or 0) < -10:
        actions.append("Digital support")
    if float(customer.get("balance_change_30d") or 0) < -15 or float(customer.get("transaction_change_30d") or 0) < -15:
        actions.append("Usage and relationship check-in")
    if int(customer.get("emi_bounce_30d") or 0) > 0:
        actions.append("Loan repayment support")

    return list(dict.fromkeys(actions))[:6]


def model2_response_format() -> dict[str, Any]:
    return {
        "type": "json_object",
        "schema": {
            "type": "object",
            "properties": {
                "why": {
                    "type": "array",
                    "items": {"type": "string"},
                    "minItems": 2,
                    "maxItems": 4,
                },
                "next_actions": {
                    "type": "array",
                    "items": {"type": "string"},
                    "minItems": 2,
                    "maxItems": 4,
                },
            },
            "required": ["why", "next_actions"],
            "additionalProperties": False,
        },
    }


def parse_model2_response(text: str) -> dict[str, Any]:
    parsed_markdown = parse_model2_markdown_response(text)
    if parsed_markdown["valid"]:
        return {
            "why": parsed_markdown["why"],
            "next_actions": parsed_markdown["next_actions"],
        }

    try:
        result = json.loads(text)
    except json.JSONDecodeError:
        return {
            "valid": False,
            "why": [],
            "next_actions": [],
            "raw_text": text,
            "error": "Model 2 did not return valid JSON.",
        }

    why = result.get("why")
    next_actions = result.get("next_actions")
    if not isinstance(why, list) or not isinstance(next_actions, list):
        return {
            "valid": False,
            "why": [],
            "next_actions": [],
            "raw_text": text,
            "error": "Model 2 JSON must contain why and next_actions as arrays.",
        }
    if not all(isinstance(item, str) and item.strip() for item in why):
        return {
            "valid": False,
            "why": [],
            "next_actions": [],
            "raw_text": text,
            "error": "Every why item must be a non-empty string.",
        }
    if not all(isinstance(item, str) and item.strip() for item in next_actions):
        return {
            "valid": False,
            "why": [],
            "next_actions": [],
            "raw_text": text,
            "error": "Every next_actions item must be a non-empty string.",
        }

    bad_markers = ["###", "{'why'", '"next_actions"', "'next_actions'", "```"]
    joined = "\n".join(why + next_actions)
    if any(marker in joined for marker in bad_markers):
        return {
            "valid": False,
            "why": why,
            "next_actions": next_actions,
            "raw_text": text,
            "error": "Model 2 returned markdown or nested JSON-like text.",
        }
    forbidden_terms = ["competitor", "operator", "campaign", "rate hunting", "rate shopping"]
    if any(term in joined.lower() for term in forbidden_terms):
        return {
            "valid": False,
            "why": why,
            "next_actions": next_actions,
            "raw_text": text,
            "error": "Model 2 invented unsupported business context.",
        }

    return {
        "why": [item.strip() for item in why],
        "next_actions": [item.strip() for item in next_actions],
    }


def clean_model2_line(line: str) -> str:
    line = line.strip()
    line = re.sub(r"^[-*]\s+", "", line)
    line = re.sub(r"^\d+[\.)]\s+", "", line)
    line = line.strip().strip('"').strip("'").strip()
    return line


def split_inline_items(value: str) -> list[str]:
    value = value.strip()
    if not value:
        return []
    if ";" in value:
        return [clean_model2_line(item) for item in value.split(";") if clean_model2_line(item)]
    return [clean_model2_line(value)]


def parse_model2_markdown_response(text: str) -> dict[str, Any]:
    why = []
    next_actions = []
    current_section = None
    normalized_text = re.sub(
        r"\s+((?:\*\*)?\s*next[_\s-]*actions?\s*(?:\*\*)?\s*:)",
        r"\n\1",
        text.replace("\r\n", "\n"),
        flags=re.IGNORECASE,
    )

    for raw_line in normalized_text.split("\n"):
        line = raw_line.strip()
        if not line:
            continue

        normalized = re.sub(r"^[#*\s]+|[*\s:]+$", "", line).lower().replace("_", " ")
        if normalized in {"why", "analysis", "reason", "reasons"}:
            current_section = "why"
            continue
        if normalized in {"next actions", "next action", "actions", "recommendations"}:
            current_section = "next_actions"
            continue

        why_match = re.match(r"^(?:\*\*)?\s*why\s*(?:\*\*)?\s*:\s*(.+)$", line, flags=re.IGNORECASE)
        if why_match:
            why.extend(split_inline_items(why_match.group(1)))
            current_section = "why"
            continue

        actions_match = re.match(
            r"^(?:\*\*)?\s*next[_\s-]*actions?\s*(?:\*\*)?\s*:\s*(.+)$",
            line,
            flags=re.IGNORECASE,
        )
        if actions_match:
            next_actions.extend(split_inline_items(actions_match.group(1)))
            current_section = "next_actions"
            continue

        item = clean_model2_line(line)
        if current_section == "why" and item:
            why.append(item)
        elif current_section == "next_actions" and item:
            next_actions.append(item)

    why = [item for item in why if item and not re.match(r"^next[_\s-]*actions?\s*:", item, flags=re.IGNORECASE)]
    next_actions = [item for item in next_actions if item and not re.match(r"^why\s*:", item, flags=re.IGNORECASE)]
    why = why[:4]
    next_actions = next_actions[:4]

    if why and next_actions:
        joined = "\n".join(why + next_actions).lower()
        forbidden_terms = ["competitor", "operator", "campaign", "rate hunting", "rate shopping"]
        if any(term in joined for term in forbidden_terms):
            return {
                "valid": False,
                "why": why,
                "next_actions": next_actions,
            }
        return {
            "valid": True,
            "why": why,
            "next_actions": next_actions,
        }

    return {
        "valid": False,
        "why": why,
        "next_actions": next_actions,
    }


def short_text(value: str | None, limit: int = 120) -> str | None:
    if not value:
        return None
    value = " ".join(str(value).split())
    if len(value) <= limit:
        return value
    return value[: limit - 3].rstrip() + "..."


def action_sentence(action: str, payload: dict[str, Any]) -> str:
    complaint = short_text(payload.get("complaint"))
    mapping = {
        "Monitor only with light-touch service check-in": "Monitor the account and make only a light-touch service check-in.",
        "Relationship manager call": "Ask a relationship manager to contact the customer and understand the concern.",
        "Complaint follow-up": f"Follow up on the recent complaint: {complaint}" if complaint else "Follow up on recent complaints and confirm resolution.",
        "Resolve failed transactions": "Review failed transactions and help the customer complete payments.",
        "FD renewal or savings discussion": "Discuss FD renewal or a suitable savings option before maturity.",
        "Digital support": "Offer digital support for app, UPI, or payment issues.",
        "Usage and relationship check-in": "Check why account usage has declined and offer relevant support.",
        "Loan repayment support": "Offer support for the recent EMI bounce.",
    }
    return mapping.get(action, action)


def fallback_model2_response(payload: dict[str, Any]) -> dict[str, Any]:
    risk = payload.get("risk", {})
    risk_level_value = risk.get("risk_level", "Unknown")
    probability = risk.get("churn_probability_percent")
    main_signals = payload.get("main_signals") or []

    why = []
    if risk_level_value == "Low":
        if probability is not None:
            why.append(f"Model 1 v2 shows low churn risk at {float(probability):.2f}%.")
        for signal in main_signals:
            message = signal.get("message")
            if message and message not in why:
                why.append(message)
            if len(why) >= 2:
                break
    else:
        if probability is not None:
            why.append(f"Model 1 v2 places this customer in {risk_level_value} churn risk at {float(probability):.2f}%.")
        for signal in main_signals:
            message = signal.get("message")
            if message and message not in why:
                why.append(message)
            if len(why) >= 4:
                break

    if not why:
        why.append("Model 1 v2 did not find a strong recent churn signal.")

    action_limit = 2 if risk_level_value == "Low" else 4
    next_actions = []
    for action in payload.get("suggested_actions") or []:
        sentence = action_sentence(action, payload)
        if sentence and sentence not in next_actions:
            next_actions.append(sentence)
        if len(next_actions) >= action_limit:
            break

    if not next_actions:
        next_actions.append("Monitor the account and review again after the next activity update.")

    return {
        "why": why[:4],
        "next_actions": next_actions[:4],
    }


def response_needs_fallback(result: dict[str, Any]) -> bool:
    if sorted(result.keys()) != ["next_actions", "why"]:
        return True
    if not isinstance(result.get("why"), list) or not isinstance(result.get("next_actions"), list):
        return True
    if not result["why"] or not result["next_actions"]:
        return True
    if len(result["why"]) < 2 or len(result["next_actions"]) < 2:
        return True
    joined = "\n".join(result["why"] + result["next_actions"]).lower()
    bad_markers = [
        "[",
        "]",
        "copy ",
        "source",
        "main_signals",
        "suggested_actions",
        "example",
        "competitor",
        "operator",
        "campaign",
        "rate retention",
        "rate hunting",
        "rate shopping",
        "service outage",
        "funds movement",
    ]
    return any(marker in joined for marker in bad_markers)


def predict_model2(payload: dict[str, Any]) -> dict[str, Any]:
    if model2 is None:
        raise RuntimeError("Model 2 is not loaded")

    system_prompt = (
        "You are a banking retention AI. Your job is to identify why this customer may churn "
        "and suggest practical retention actions. Use only the facts in the user JSON. For Why, use "
        "the messages inside main_signals and the risk object. For Next Actions, use suggested_actions "
        "and make them short practical sentences. Do not invent competitors, rates, operators, campaigns, "
        "products, fees, branch quality, repayment issues, or reasons for money movement. Do not mention "
        "customer age, branch code, card colour, or field names. Do not use square brackets. For Low risk, "
        "keep actions light: monitor, check service quality, and avoid urgent retention offers. For Medium "
        "or High risk, include proactive contact and fixes linked to the strongest signals. Return only two "
        "sections with bullet lines. The only section labels allowed are Why: and Next Actions:. Write 2 to "
        "4 short bullets in each section."
    )
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": json.dumps(payload)},
    ]

    if MODEL2_BACKEND == "ollama":
        text = ollama_chat(messages)
    else:
        output = model2.create_chat_completion(
            messages=messages,
            temperature=MODEL2_TEMPERATURE,
        )
        text = output["choices"][0]["message"]["content"]
    parsed = parse_model2_response(text)
    if response_needs_fallback(parsed):
        return fallback_model2_response(payload)
    return parsed


def build_model2_payload(
    customer: dict[str, Any],
    model1_output: dict[str, Any],
    extra_context: dict[str, Any] | None = None,
    customer_id: str | None = None,
    customer_name: str | None = None,
    snapshot_date: str | None = None,
) -> dict[str, Any]:
    extra_context = extra_context or {}
    profile = extra_context.get("customer_profile", {})
    complaint_text = extra_context.get("recent_complaint_text")
    risk_level_value = model1_output.get("risk_level", "Unknown")
    return {
        "task": "identify_retention_risk_and_actions",
        "customer_identity": {
            "customer_id": customer_id,
            "customer_name": customer_name,
            "snapshot_date": snapshot_date,
        },
        "risk": {
            "churn_probability_percent": model1_output.get("churn_probability"),
            "risk_score": model1_output.get("risk_score"),
            "churn_prediction": model1_output.get("churn_prediction"),
            "risk_level": risk_level_value,
        },
        "customer": {
            "segment": profile.get("segment") or customer.get("customer_segment"),
            "income_regularity": profile.get("income_regularity") or customer.get("income_regularity"),
            "value_tier": profile.get("value_tier"),
            "tenure_months": profile.get("tenure_months") or customer.get("tenure_months"),
            "products_count": profile.get("products_count") or customer.get("products_count"),
            "has_credit_card": bool(profile.get("has_credit_card") or customer.get("has_credit_card")),
            "has_loan": bool(profile.get("has_loan") or customer.get("has_loan")),
        },
        "main_signals": build_main_signals(model1_output, customer),
        "trend_summary": trend_summary(extra_context.get("trend_last_3_months", {})),
        "complaint": complaint_text,
        "risk_group": extra_context.get("risk_group", "unknown"),
        "suggested_actions": suggested_actions_for(customer, risk_level_value, complaint_text),
    }


@asynccontextmanager
async def lifespan(app: FastAPI):
    if USE_MODEL1:
        load_model1()
    if USE_MODEL2:
        load_model2()
    yield


app = FastAPI(title="Customer Retention Local API", lifespan=lifespan)


@app.get("/health")
def health():
    return {
        "ok": True,
        "model1_enabled": USE_MODEL1,
        "model2_enabled": USE_MODEL2,
        "model2_backend": MODEL2_BACKEND,
        "model1_loaded": model1 is not None,
        "model2_loaded": model2 is not None,
        "served_at": datetime.now().isoformat(timespec="seconds"),
        "model1": model1_runtime_info(),
        "model2": model2_runtime_info(),
    }


@app.post("/predict/model1")
def api_model1(request: Model1Request):
    started_at = time.perf_counter()
    try:
        model_started = time.perf_counter()
        model1_output = predict_model1(request)
        timings = {"model1": round((time.perf_counter() - model_started) * 1000, 2)}
        return {
            "meta": response_meta("/predict/model1", started_at, request, timings),
            "model1": model1_output,
        }
    except Exception as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc


@app.post("/predict/model2")
def api_model2(request: Model2Request):
    started_at = time.perf_counter()
    try:
        model_started = time.perf_counter()
        model2_output = predict_model2(request.payload)
        timings = {"model2": round((time.perf_counter() - model_started) * 1000, 2)}
        return {
            "meta": response_meta("/predict/model2", started_at, request, timings),
            "model2": model2_output,
        }
    except Exception as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc


@app.post("/predict/both")
def api_both(request: BothRequest):
    started_at = time.perf_counter()
    try:
        model1_started = time.perf_counter()
        model1_output = predict_model1(request)
        model1_ms = round((time.perf_counter() - model1_started) * 1000, 2)
        customer = latest_customer_from_request(request)
        snapshot_date = request.snapshot_date or request.prediction_date
        model2_payload = build_model2_payload(
            customer,
            model1_output,
            request.extra_context,
            request.customer_id,
            request.customer_name,
            snapshot_date,
        )
        model2_started = time.perf_counter()
        model2_output = predict_model2(model2_payload)
        model2_ms = round((time.perf_counter() - model2_started) * 1000, 2)
        return {
            "meta": response_meta(
                "/predict/both",
                started_at,
                request,
                {"model1": model1_ms, "model2": model2_ms},
            ),
            "model1": model1_output,
            "model2_input": model2_payload,
            "model2": model2_output,
        }
    except Exception as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc


@app.post("/admin/load-model2")
def api_load_model2(request: LoadModel2Request):
    try:
        load_model2(Path(request.model_path))
        return {"ok": True, "model2_path": str(MODEL2_PATH)}
    except Exception as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host=HOST, port=PORT)
