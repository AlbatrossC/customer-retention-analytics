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
MODEL2_RECOVERY_CONFIG_PATH = ROOT / "backend" / "model2_recovery_schemas.json"

HOST = "127.0.0.1"
PORT = 8000

MODEL2_N_CTX = 2048
MODEL2_N_THREADS = 4
MODEL2_TEMPERATURE = 0.3
MODEL2_TOP_P = 0.9
MODEL2_REPEAT_PENALTY = 1.08
MODEL2_MAX_RETRIES = 3

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
model2_recovery_config_cache: dict[str, Any] | None = None
model2_recovery_config_mtime: float | None = None
model2_recovery_config_error: str | None = None


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
        "max_retries": MODEL2_MAX_RETRIES,
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
    info["recovery_config"] = model2_recovery_config_info()
    return info


def model2_recovery_config_info() -> dict[str, Any]:
    try:
        config = load_model2_recovery_config()
        return {
            "path": str(MODEL2_RECOVERY_CONFIG_PATH),
            "loaded": True,
            "schema_count": len(config["recovery_schemas"]),
            "modified_at": datetime.fromtimestamp(float(model2_recovery_config_mtime)).isoformat(timespec="seconds")
            if model2_recovery_config_mtime is not None
            else None,
            "error": None,
        }
    except Exception as exc:
        return {
            "path": str(MODEL2_RECOVERY_CONFIG_PATH),
            "loaded": False,
            "schema_count": 0,
            "modified_at": None,
            "error": str(exc),
        }


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
    try:
        with urllib.request.urlopen(request, timeout=MODEL2_TIMEOUT) as response:
            output = json.loads(response.read())
    except urllib.error.HTTPError as exc:
        details = exc.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"Ollama chat HTTP {exc.code}: {short_text(details, 500) or exc.reason}") from exc
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


def short_text(value: str | None, limit: int = 120) -> str | None:
    if not value:
        return None
    value = " ".join(str(value).split())
    if len(value) <= limit:
        return value
    return value[: limit - 3].rstrip() + "..."


def validate_model2_recovery_config(config: dict[str, Any]) -> None:
    if not isinstance(config.get("system_prompt"), str) or not config["system_prompt"].strip():
        raise ValueError("Model 2 recovery config requires a non-empty system_prompt.")
    contract = config.get("output_contract")
    if not isinstance(contract, dict):
        raise ValueError("Model 2 recovery config requires output_contract.")
    schemas = config.get("recovery_schemas")
    if not isinstance(schemas, list) or not schemas:
        raise ValueError("Model 2 recovery config requires at least one recovery schema.")

    schema_ids = set()
    action_ids = set()
    for schema in schemas:
        schema_id = schema.get("id")
        if not isinstance(schema_id, str) or not schema_id.strip():
            raise ValueError("Every recovery schema requires a non-empty id.")
        if schema_id in schema_ids:
            raise ValueError(f"Duplicate recovery schema id: {schema_id}")
        schema_ids.add(schema_id)
        if not isinstance(schema.get("use_when"), str) or not schema["use_when"].strip():
            raise ValueError(f"Recovery schema {schema_id} requires use_when text.")
        if not isinstance(schema.get("summary_reason"), str) or not schema["summary_reason"].strip():
            raise ValueError(f"Recovery schema {schema_id} requires summary_reason.")
        actions = schema.get("actions")
        if not isinstance(actions, list) or not actions:
            raise ValueError(f"Recovery schema {schema_id} requires at least one action.")
        for action in actions:
            action_id = action.get("id")
            if not isinstance(action_id, str) or not action_id.strip():
                raise ValueError(f"Every action in {schema_id} requires a non-empty id.")
            if action_id in action_ids:
                raise ValueError(f"Duplicate recovery action id: {action_id}")
            action_ids.add(action_id)
            for key in ["label", "priority", "reason"]:
                if not isinstance(action.get(key), str) or not action[key].strip():
                    raise ValueError(f"Action {action_id} requires {key}.")
            if action["priority"] not in set(contract.get("priority_values", [])):
                raise ValueError(f"Action {action_id} has unsupported priority {action['priority']}.")
            if not isinstance(action.get("evidence_fields"), list) or not action["evidence_fields"]:
                raise ValueError(f"Action {action_id} requires evidence_fields.")


def load_model2_recovery_config(force: bool = False) -> dict[str, Any]:
    global model2_recovery_config_cache, model2_recovery_config_mtime, model2_recovery_config_error
    try:
        stat = MODEL2_RECOVERY_CONFIG_PATH.stat()
        if (
            not force
            and model2_recovery_config_cache is not None
            and model2_recovery_config_mtime == stat.st_mtime
        ):
            return model2_recovery_config_cache
        config = json.loads(MODEL2_RECOVERY_CONFIG_PATH.read_text(encoding="utf-8"))
        validate_model2_recovery_config(config)
        model2_recovery_config_cache = config
        model2_recovery_config_mtime = stat.st_mtime
        model2_recovery_config_error = None
        return config
    except Exception as exc:
        model2_recovery_config_error = str(exc)
        raise


def recovery_schema_map(config: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {schema["id"]: schema for schema in config["recovery_schemas"]}


def recovery_action_map(config: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {
        action["id"]: action
        for schema in config["recovery_schemas"]
        for action in schema["actions"]
    }


def compact_recovery_catalog(config: dict[str, Any]) -> list[dict[str, Any]]:
    return [
        {
            "schema_id": schema["id"],
            "use_when": schema["use_when"],
            "actions": [
                {
                    "action_id": action["id"],
                    "action_label": action["label"],
                    "priority": action["priority"],
                    "evidence_fields": action["evidence_fields"],
                }
                for action in schema["actions"]
            ],
        }
        for schema in config["recovery_schemas"]
    ]


def build_model2_system_prompt(config: dict[str, Any]) -> str:
    contract = config["output_contract"]
    return (
        f"{config['system_prompt'].strip()}\n\n"
        "Output contract:\n"
        "- Return only JSON with keys: primary_schema, selected_schemas, actions, summary_reason.\n"
        "- primary_schema must be one selected schema_id.\n"
        f"- selected_schemas must contain 1 to {contract['max_selected_schemas']} schema ids.\n"
        "- Each action must contain action_id, action_label, reason, priority, evidence_fields.\n"
        "- Every action_id must come from the selected schemas.\n"
        f"- priority must be one of: {', '.join(contract['priority_values'])}.\n"
        "- For Low risk with an active issue, selected action priority must be low.\n"
        "- For Low risk without a meaningful active issue, select LOW_RISK_MONITOR only.\n"
        "- No markdown, comments, explanations outside JSON, or copied catalog dumps.\n"
        "The allowed recovery schemas and actions are provided in the user JSON."
    )


def model2_prompt_payload(payload: dict[str, Any], config: dict[str, Any]) -> dict[str, Any]:
    prompt_payload = dict(payload)
    prompt_payload["allowed_recovery_schemas"] = compact_recovery_catalog(config)
    return prompt_payload


def parse_model2_response(text: str, payload: dict[str, Any], config: dict[str, Any]) -> dict[str, Any]:
    try:
        result = json.loads(text)
    except json.JSONDecodeError:
        return {
            "valid": False,
            "raw_text": text,
            "error": "Model 2 did not return strict JSON.",
        }
    return validate_model2_response(result, payload, config, raw_text=text)


def response_action_limits(payload: dict[str, Any], config: dict[str, Any]) -> tuple[int, int]:
    contract = config["output_contract"]
    risk_level_value = (payload.get("risk") or {}).get("risk_level")
    if risk_level_value == "Low":
        return int(contract["min_actions_low_risk"]), int(contract["max_actions_low_risk"])
    return int(contract["min_actions_medium_high_risk"]), int(contract["max_actions_medium_high_risk"])


def validate_model2_response(
    result: Any,
    payload: dict[str, Any],
    config: dict[str, Any],
    raw_text: str | None = None,
) -> dict[str, Any]:
    if not isinstance(result, dict):
        return invalid_model2_response(raw_text, "Model 2 JSON must be an object.")

    required = set(config["output_contract"]["required_keys"])
    if set(result) != required:
        return invalid_model2_response(raw_text, "Model 2 JSON has unsupported or missing top-level keys.")

    schemas_by_id = recovery_schema_map(config)
    selected_schemas = result.get("selected_schemas")
    primary_schema = result.get("primary_schema")
    if not isinstance(primary_schema, str) or primary_schema not in schemas_by_id:
        return invalid_model2_response(raw_text, "primary_schema must be a known recovery schema id.")
    if not isinstance(selected_schemas, list) or not selected_schemas:
        return invalid_model2_response(raw_text, "selected_schemas must be a non-empty array.")
    max_schemas = int(config["output_contract"]["max_selected_schemas"])
    if len(selected_schemas) > max_schemas:
        return invalid_model2_response(raw_text, f"selected_schemas cannot exceed {max_schemas}.")
    if primary_schema not in selected_schemas:
        return invalid_model2_response(raw_text, "primary_schema must also appear in selected_schemas.")
    if len(set(selected_schemas)) != len(selected_schemas):
        return invalid_model2_response(raw_text, "selected_schemas cannot contain duplicates.")
    if not all(isinstance(schema_id, str) and schema_id in schemas_by_id for schema_id in selected_schemas):
        return invalid_model2_response(raw_text, "selected_schemas contains an unknown schema id.")

    risk_level_value = (payload.get("risk") or {}).get("risk_level")
    if risk_level_value == "Low":
        active_issue_schemas = strong_active_issue_schema_ids(payload, config)
        if active_issue_schemas and selected_schemas == ["LOW_RISK_MONITOR"]:
            return invalid_model2_response(raw_text, "Low-risk customers with active issues should use the relevant recovery schema.")
        if not active_issue_schemas and selected_schemas != ["LOW_RISK_MONITOR"]:
            return invalid_model2_response(raw_text, "Low-risk customers without active issues must use LOW_RISK_MONITOR.")
        if active_issue_schemas and not all(schema_id in active_issue_schemas for schema_id in selected_schemas):
            return invalid_model2_response(raw_text, "Low-risk recovery schemas must match strong active issues.")

    actions = result.get("actions")
    min_actions, max_actions = response_action_limits(payload, config)
    if not isinstance(actions, list) or not (min_actions <= len(actions) <= max_actions):
        return invalid_model2_response(raw_text, f"actions must contain {min_actions} to {max_actions} items.")

    allowed_actions = {
        action["id"]: action
        for schema_id in selected_schemas
        for action in schemas_by_id[schema_id]["actions"]
    }
    priority_values = set(config["output_contract"]["priority_values"])
    required_action_keys = set(config["output_contract"]["action_required_keys"])
    seen_actions = set()
    normalized_actions = []
    for action in actions:
        if not isinstance(action, dict) or set(action) != required_action_keys:
            return invalid_model2_response(raw_text, "Every action must match the required action object shape.")
        action_id = action.get("action_id")
        if action_id not in allowed_actions:
            return invalid_model2_response(raw_text, "Every action_id must come from the selected schemas.")
        if action_id in seen_actions:
            return invalid_model2_response(raw_text, "actions cannot contain duplicate action_id values.")
        seen_actions.add(action_id)
        reason = action.get("reason")
        if not isinstance(reason, str) or not reason.strip():
            return invalid_model2_response(raw_text, "Every action requires one non-empty reason.")
        if contains_forbidden_model2_text(reason):
            return invalid_model2_response(raw_text, "Model 2 invented unsupported business context.")
        priority = action.get("priority")
        if priority not in priority_values:
            return invalid_model2_response(raw_text, "Every action priority must be supported.")
        if risk_level_value == "Low" and priority != "low":
            return invalid_model2_response(raw_text, "Low-risk customer actions must use low priority.")
        evidence_fields = action.get("evidence_fields")
        if not isinstance(evidence_fields, list) or not all(isinstance(item, str) and item for item in evidence_fields):
            return invalid_model2_response(raw_text, "Every action requires evidence_fields as strings.")
        catalog_action = allowed_actions[action_id]
        normalized_actions.append(
            {
                "action_id": action_id,
                "action_label": catalog_action["label"],
                "reason": reason.strip(),
                "priority": priority,
                "evidence_fields": evidence_fields,
            }
        )

    summary_reason = result.get("summary_reason")
    if not isinstance(summary_reason, str) or not summary_reason.strip():
        return invalid_model2_response(raw_text, "summary_reason must be a non-empty string.")
    if contains_forbidden_model2_text(summary_reason):
        return invalid_model2_response(raw_text, "Model 2 invented unsupported business context.")

    return {
        "primary_schema": primary_schema,
        "selected_schemas": selected_schemas,
        "actions": normalized_actions,
        "summary_reason": summary_reason.strip(),
    }


def invalid_model2_response(raw_text: str | None, error: str) -> dict[str, Any]:
    return {
        "valid": False,
        "raw_text": raw_text,
        "error": error,
    }


def contains_forbidden_model2_text(value: str) -> bool:
    forbidden_terms = [
        "```",
        "###",
        "competitor",
        "operator",
        "campaign",
        "rate hunting",
        "rate shopping",
        "branch quality",
        "hidden fee",
        "funds movement",
        "service outage",
    ]
    lowered = value.lower()
    return any(term in lowered for term in forbidden_terms)


def response_needs_fallback(result: dict[str, Any]) -> bool:
    return result.get("valid") is False


def as_number(value: Any) -> float | None:
    if value is None:
        return None
    try:
        if pd.isna(value):
            return None
    except Exception:
        pass
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def customer_signal_value(payload: dict[str, Any], field: str) -> Any:
    if field in {"risk_level", "churn_probability_percent"}:
        return (payload.get("risk") or {}).get(field)
    if field in {"complaint", "complaint_text"}:
        return payload.get("complaint")
    signals = payload.get("customer_signals") or {}
    if field in signals:
        return signals.get(field)
    customer = payload.get("customer") or {}
    if field in customer:
        return customer.get(field)
    for signal in payload.get("main_signals") or []:
        if signal.get("field") == field:
            return signal.get("value")
    return None


def complaint_mentions_transaction_failure(text: str | None) -> bool:
    if not text:
        return False
    lowered = text.lower()
    keywords = ["failed", "declined", "atm", "cash", "payment", "transaction", "not showing", "stuck"]
    return any(keyword in lowered for keyword in keywords)


def score_recovery_schema(schema_id: str, payload: dict[str, Any]) -> tuple[int, list[str]]:
    evidence = []
    risk = payload.get("risk") or {}
    customer = payload.get("customer") or {}
    complaint = payload.get("complaint")

    def add_if(condition: bool, field: str, score: int = 1) -> int:
        if condition:
            if field not in evidence:
                evidence.append(field)
            return score
        return 0

    score = 0
    if schema_id == "SERVICE_COMPLAINT":
        score += add_if((as_number(customer_signal_value(payload, "complaints_30d")) or 0) > 0, "complaints_30d", 2)
        score += add_if((as_number(customer_signal_value(payload, "unresolved_complaints")) or 0) > 0, "unresolved_complaints", 3)
        score += add_if(bool(complaint), "complaint", 2)
        score += add_if((as_number(customer_signal_value(payload, "avg_resolution_time_hrs")) or 0) >= 48, "avg_resolution_time_hrs", 2)
    elif schema_id == "TRANSACTION_FAILURE":
        score += add_if((as_number(customer_signal_value(payload, "failed_transactions_30d")) or 0) > 0, "failed_transactions_30d", 3)
        score += add_if(complaint_mentions_transaction_failure(complaint), "complaint", 2)
    elif schema_id == "ACTIVITY_DECLINE":
        score += add_if((as_number(customer_signal_value(payload, "transaction_change_30d")) or 0) < -5, "transaction_change_30d", 2)
        score += add_if((as_number(customer_signal_value(payload, "card_spend_change_30d")) or 0) < -5, "card_spend_change_30d", 2)
        score += add_if((as_number(customer_signal_value(payload, "app_login_change_30d")) or 0) < -10, "app_login_change_30d", 1)
        score += add_if((as_number(customer_signal_value(payload, "days_since_last_transaction")) or 0) >= 10, "days_since_last_transaction", 2)
    elif schema_id == "BALANCE_OUTFLOW":
        score += add_if((as_number(customer_signal_value(payload, "balance_change_30d")) or 0) < -15, "balance_change_30d", 3)
        score += add_if((as_number(customer_signal_value(payload, "external_transfer_change_30d")) or 0) > 20, "external_transfer_change_30d", 2)
    elif schema_id == "DIGITAL_DISENGAGEMENT":
        score += add_if((as_number(customer_signal_value(payload, "app_login_change_30d")) or 0) < -10, "app_login_change_30d", 3)
        if (as_number(customer_signal_value(payload, "failed_transactions_30d")) or 0) > 0:
            score += add_if((as_number(customer_signal_value(payload, "upi_share_of_spend")) or 0) >= 0.65, "upi_share_of_spend", 1)
    elif schema_id == "SALARY_OR_INCOME_BREAK":
        score += add_if((as_number(customer_signal_value(payload, "salary_missing_days")) or 0) > 0, "salary_missing_days", 3)
    elif schema_id == "FD_MATURITY":
        score += add_if((as_number(customer_signal_value(payload, "fd_maturing_in_30d")) or 0) > 0, "fd_maturing_in_30d", 3)
    elif schema_id == "PRODUCT_DROPOFF":
        score += add_if((as_number(customer_signal_value(payload, "products_dropped_90d")) or 0) > 0, "products_dropped_90d", 3)
    elif schema_id == "LOAN_REPAYMENT_STRESS":
        score += add_if((as_number(customer_signal_value(payload, "emi_bounce_30d")) or 0) > 0, "emi_bounce_30d", 3)
        score += add_if(bool(customer.get("has_loan")) and (as_number(customer_signal_value(payload, "emi_bounce_30d")) or 0) > 0, "has_loan", 1)
    elif schema_id == "LOW_RISK_MONITOR":
        score += add_if(risk.get("risk_level") == "Low", "risk_level", 2)

    return score, evidence


def strong_active_issue_schema_ids(payload: dict[str, Any], config: dict[str, Any]) -> list[str]:
    checks = {
        "SERVICE_COMPLAINT": (
            (as_number(customer_signal_value(payload, "unresolved_complaints")) or 0) > 0
            or (as_number(customer_signal_value(payload, "complaints_30d")) or 0) >= 2
            or bool(payload.get("complaint"))
            or (as_number(customer_signal_value(payload, "avg_resolution_time_hrs")) or 0) >= 24
        ),
        "TRANSACTION_FAILURE": (
            (as_number(customer_signal_value(payload, "failed_transactions_30d")) or 0) >= 2
            or complaint_mentions_transaction_failure(payload.get("complaint"))
        ),
        "ACTIVITY_DECLINE": (
            (as_number(customer_signal_value(payload, "days_since_last_transaction")) or 0) >= 14
            or (as_number(customer_signal_value(payload, "transaction_change_30d")) or 0) <= -20
            or (as_number(customer_signal_value(payload, "card_spend_change_30d")) or 0) <= -20
            or (as_number(customer_signal_value(payload, "app_login_change_30d")) or 0) <= -25
        ),
        "BALANCE_OUTFLOW": (
            (as_number(customer_signal_value(payload, "balance_change_30d")) or 0) <= -20
            or (as_number(customer_signal_value(payload, "external_transfer_change_30d")) or 0) >= 40
        ),
        "DIGITAL_DISENGAGEMENT": (
            (as_number(customer_signal_value(payload, "app_login_change_30d")) or 0) <= -25
            or (
                (as_number(customer_signal_value(payload, "failed_transactions_30d")) or 0) >= 2
                and (as_number(customer_signal_value(payload, "upi_share_of_spend")) or 0) >= 0.65
            )
        ),
        "SALARY_OR_INCOME_BREAK": (as_number(customer_signal_value(payload, "salary_missing_days")) or 0) > 0,
        "FD_MATURITY": (as_number(customer_signal_value(payload, "fd_maturing_in_30d")) or 0) > 0,
        "PRODUCT_DROPOFF": (as_number(customer_signal_value(payload, "products_dropped_90d")) or 0) > 0,
        "LOAN_REPAYMENT_STRESS": (as_number(customer_signal_value(payload, "emi_bounce_30d")) or 0) > 0,
    }
    schema_ids = {schema["id"] for schema in config["recovery_schemas"]}
    return [schema["id"] for schema in config["recovery_schemas"] if schema["id"] in schema_ids and checks.get(schema["id"])]


def deterministic_schema_selection(payload: dict[str, Any], config: dict[str, Any]) -> list[str]:
    risk_level_value = (payload.get("risk") or {}).get("risk_level")
    if risk_level_value == "Low":
        active_issue_schemas = strong_active_issue_schema_ids(payload, config)
        max_schemas = int(config["output_contract"]["max_selected_schemas"])
        return active_issue_schemas[:max_schemas] if active_issue_schemas else ["LOW_RISK_MONITOR"]

    scored = []
    for index, schema in enumerate(config["recovery_schemas"]):
        score, evidence = score_recovery_schema(schema["id"], payload)
        if schema["id"] == "LOW_RISK_MONITOR":
            continue
        if score >= 2:
            scored.append((schema["id"], score, len(evidence), index))

    scored.sort(key=lambda item: (-item[1], -item[2], item[3]))
    if not scored:
        return ["ACTIVITY_DECLINE"] if risk_level_value in {"Medium", "High"} else ["LOW_RISK_MONITOR"]
    return [schema_id for schema_id, _, _, _ in scored[:3]]


def action_reason(action: dict[str, Any], payload: dict[str, Any]) -> str:
    evidence_messages = []
    evidence_fields = action.get("evidence_fields") or []
    for signal in payload.get("main_signals") or []:
        if signal.get("field") in evidence_fields and signal.get("message"):
            evidence_messages.append(signal["message"])
    if evidence_messages:
        return evidence_messages[0]

    action_id = action["id"]
    complaint = short_text(payload.get("complaint"))
    risk = payload.get("risk") or {}
    probability = risk.get("churn_probability_percent")
    if action_id in {"complaint_follow_up", "complaint_escalation", "service_recovery_call"} and complaint:
        return f"Recent complaint needs follow-up: {complaint}"
    if action_id == "charge_reversal_review" and complaint:
        return f"Complaint text may involve a charge review: {complaint}"
    if probability is not None and "risk_level" in evidence_fields:
        return f"Model 1 v2 places this customer at {risk.get('risk_level', 'elevated')} risk with {float(probability):.2f}% churn probability."
    return action["reason"]


def fallback_model2_response(payload: dict[str, Any], config: dict[str, Any] | None = None) -> dict[str, Any]:
    config = config or load_model2_recovery_config()
    schemas_by_id = recovery_schema_map(config)
    selected_schemas = deterministic_schema_selection(payload, config)
    primary_schema = selected_schemas[0]
    _, max_actions = response_action_limits(payload, config)
    risk_level_value = (payload.get("risk") or {}).get("risk_level")
    target_actions = 2 if risk_level_value == "Low" else min(max_actions, max(2, len(selected_schemas) + 1))

    actions = []
    used = set()
    for schema_id in selected_schemas:
        for action in schemas_by_id[schema_id]["actions"]:
            if action["id"] in used:
                continue
            actions.append(
                {
                    "action_id": action["id"],
                    "action_label": action["label"],
                    "reason": action_reason(action, payload),
                    "priority": "low" if risk_level_value == "Low" else action["priority"],
                    "evidence_fields": action["evidence_fields"],
                }
            )
            used.add(action["id"])
            if len(actions) >= target_actions:
                break
        if len(actions) >= target_actions:
            break

    return {
        "primary_schema": primary_schema,
        "selected_schemas": selected_schemas,
        "actions": actions,
        "summary_reason": schemas_by_id[primary_schema]["summary_reason"],
    }


def predict_model2(payload: dict[str, Any]) -> dict[str, Any]:
    if model2 is None:
        raise RuntimeError("Model 2 is not loaded")

    recovery_config = load_model2_recovery_config()
    system_prompt = build_model2_system_prompt(recovery_config)
    prompt_payload = model2_prompt_payload(payload, recovery_config)
    last_invalid = None

    for attempt in range(1, MODEL2_MAX_RETRIES + 1):
        attempt_payload = dict(prompt_payload)
        if last_invalid is not None:
            attempt_payload["previous_invalid_output"] = {
                "attempt": attempt - 1,
                "error": last_invalid.get("error"),
                "instruction": "Return strict JSON only, with known schema ids and catalog action ids.",
            }
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": json.dumps(attempt_payload, ensure_ascii=False)},
        ]

        try:
            if MODEL2_BACKEND == "ollama":
                text = ollama_chat(messages)
            else:
                output = model2.create_chat_completion(
                    messages=messages,
                    temperature=MODEL2_TEMPERATURE,
                )
                text = output["choices"][0]["message"]["content"]
        except Exception as exc:
            last_invalid = invalid_model2_response(None, str(exc))
            continue
        parsed = parse_model2_response(text, payload, recovery_config)
        if not response_needs_fallback(parsed):
            return parsed
        last_invalid = parsed

    return fallback_model2_response(payload, recovery_config)


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
    customer_signals = {
        feature: json_safe(customer.get(feature))
        for feature in BEHAVIOR_FEATURES
        if feature in customer
    }
    recovery_config = load_model2_recovery_config()
    return {
        "task": "select_recovery_schemas_and_actions",
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
        "customer_signals": customer_signals,
        "main_signals": build_main_signals(model1_output, customer),
        "trend_summary": trend_summary(extra_context.get("trend_last_3_months", {})),
        "complaint": complaint_text,
        "risk_group": extra_context.get("risk_group", "unknown"),
        "allowed_recovery_schemas": compact_recovery_catalog(recovery_config),
    }


@asynccontextmanager
async def lifespan(app: FastAPI):
    load_model2_recovery_config()
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
