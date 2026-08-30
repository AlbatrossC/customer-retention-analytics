import hashlib
import json
import re
import sys
import urllib.error
import urllib.request
from contextlib import asynccontextmanager
from pathlib import Path
from typing import Any

import joblib
import numpy as np
import pandas as pd
import xgboost as xgb
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from xgboost import XGBClassifier


ROOT = Path(__file__).resolve().parents[1]
MODEL1_SCRIPT_ROOT = ROOT / "model_1" / "training_scripts"
if str(MODEL1_SCRIPT_ROOT) not in sys.path:
    sys.path.insert(0, str(MODEL1_SCRIPT_ROOT))

from prediction_input import normalize_prediction_input, prepare_feature_row


USE_MODEL1 = True
USE_MODEL2 = True

MODEL1_ARTIFACT_DIR = ROOT / "model_1" / "training_scripts" / "xgboost_model1" / "artifacts"
MODEL1_PATH = MODEL1_ARTIFACT_DIR / "xgboost_model.json"
CALIBRATOR_PATH = MODEL1_ARTIFACT_DIR / "isotonic_calibrator.joblib"
METADATA_PATH = MODEL1_ARTIFACT_DIR / "model_metadata.json"
MODEL2_PATH = ROOT / "model_2_kulkarni" / "model 2 demo" / "model2_retention_0.5b.gguf"

HOST = "127.0.0.1"
PORT = 8000

MODEL2_N_CTX = 2048
MODEL2_N_THREADS = 4
MODEL2_TEMPERATURE = 0.3

# Windows Smart App Control blocks the unsigned llama.dll / ggml-*.dll shipped in
# the llama-cpp-python wheel (WinError 4551). The "ollama" backend runs the same
# GGUF inside Ollama's signed binaries and talks to it over localhost HTTP, so no
# unsigned code is loaded into this process. Use "llama_cpp" only on machines
# where Smart App Control is off.
MODEL2_BACKEND = "ollama"
OLLAMA_HOST = "http://127.0.0.1:11434"
OLLAMA_MODEL = "retention-0.5b"
MODEL2_TIMEOUT = 180
# Hash MODEL2_PATH at startup and refuse to serve unless Ollama holds that exact
# GGUF. Costs ~1s for the 380 MB file; set False to skip.
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

model1 = None
calibrator = None
metadata = None
model2 = None


class Model1Request(BaseModel):
    customer: dict[str, Any]
    threshold: float | None = None


class Model2Request(BaseModel):
    payload: dict[str, Any]


class BothRequest(BaseModel):
    customer: dict[str, Any]
    extra_context: dict[str, Any] | None = None
    threshold: float | None = None


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
    dmatrix = xgb.DMatrix(row, enable_categorical=True)
    contributions = model1.get_booster().predict(dmatrix, pred_contribs=True)
    shap_values = np.asarray(contributions)[0, :-1]
    positive = [(feature, float(value)) for feature, value in zip(row.columns.tolist(), shap_values) if value > 0]
    positive.sort(key=lambda item: item[1], reverse=True)
    return [{"factor": feature, "value": json_safe(customer_data[feature])} for feature, _ in positive[:top_n]]


def load_model1() -> None:
    global model1, calibrator, metadata
    for path in [MODEL1_PATH, CALIBRATOR_PATH, METADATA_PATH]:
        require_file(path)

    metadata = json.loads(METADATA_PATH.read_text(encoding="utf-8"))
    calibrator = joblib.load(CALIBRATOR_PATH)
    model1 = XGBClassifier()
    model1.load_model(MODEL1_PATH)
    print("Model 1 loaded")


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
            "response_format": {"type": "json_object"},
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


def predict_model1(customer_data: dict[str, Any], threshold: float | None = None) -> dict[str, Any]:
    if model1 is None or calibrator is None or metadata is None:
        raise RuntimeError("Model 1 is not loaded")

    features = metadata["features"]
    threshold = float(metadata["threshold"] if threshold is None else threshold)
    customer_data = normalize_prediction_input(customer_data, features)
    validate_model1_input(customer_data, features)
    row = prepare_feature_row(customer_data, metadata)

    raw_probability = float(model1.predict_proba(row)[0, 1])
    probability = float(calibrator.predict([raw_probability])[0])
    return {
        "churn_probability": round(probability * 100, 2),
        "risk_score": risk_score(probability),
        "churn_prediction": "Yes" if probability >= threshold else "No",
        "risk_level": risk_level(probability, metadata["risk_bands"]),
        "top_risk_factors": top_risk_factors(customer_data, row),
    }


def predict_model2(payload: dict[str, Any]) -> dict[str, Any]:
    if model2 is None:
        raise RuntimeError("Model 2 is not loaded")

    system_prompt = (
        "You are a retention intelligence assistant for a retail bank. "
        "Return ONLY a JSON object with exactly these two keys: why and next_actions. "
        "Both values must be arrays of short strings. "
        "Put the explanation only in why. "
        "Put every recommendation only in next_actions. "
        "Never combine the keys or put recommendations in why. "
        'Example: {"why": ["Risk increased after repeated transaction declines."], '
        '"next_actions": ["Contact the customer within 24 hours.", "Offer transaction support."]}'
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
            response_format={"type": "json_object"},
            temperature=MODEL2_TEMPERATURE,
        )
        text = output["choices"][0]["message"]["content"]
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        return {"why": [text], "next_actions": []}


def build_model2_payload(
    customer: dict[str, Any],
    model1_output: dict[str, Any],
    extra_context: dict[str, Any] | None = None,
) -> dict[str, Any]:
    extra_context = extra_context or {}
    return {
        "type": "individual",
        "model1_output": model1_output,
        "customer_profile": extra_context.get("customer_profile", {}),
        "current_snapshot": customer,
        "trend_last_3_months": extra_context.get("trend_last_3_months", {}),
        "recent_complaint_text": extra_context.get("recent_complaint_text"),
        "risk_group": extra_context.get("risk_group", "unknown"),
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
    }


@app.post("/predict/model1")
def api_model1(request: Model1Request):
    try:
        return {"model1": predict_model1(request.customer, request.threshold)}
    except Exception as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc


@app.post("/predict/model2")
def api_model2(request: Model2Request):
    try:
        return {"model2": predict_model2(request.payload)}
    except Exception as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc


@app.post("/predict/both")
def api_both(request: BothRequest):
    try:
        model1_output = predict_model1(request.customer, request.threshold)
        model2_payload = build_model2_payload(request.customer, model1_output, request.extra_context)
        return {
            "model1": model1_output,
            "model2_input": model2_payload,
            "model2": predict_model2(model2_payload),
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
