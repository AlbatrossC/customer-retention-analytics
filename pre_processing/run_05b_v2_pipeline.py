import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
import json
import math
import sys
import threading
import time
import urllib.error
import urllib.request
from datetime import date, datetime
from pathlib import Path
from typing import Any

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from backend import retention_api_server as server


CUSTOMERS_CSV = ROOT / "model_1_v2" / "data" / "customers.csv"
DEFAULT_OUTPUT = ROOT / "pre_processing" / "outputs" / "model_05b_v2_pipeline_outputs.json"
CHECKPOINT_EVERY = 25
OLLAMA_TAGS_URL = f"{server.OLLAMA_HOST}/api/tags"
EXPECTED_OLLAMA_MODEL = server.OLLAMA_MODEL

PROFILE_FEATURES = [
    "tenure_months",
    "customer_segment",
    "income_regularity",
    "products_count",
    "has_credit_card",
    "has_loan",
]

BEHAVIOR_FEATURES = [
    "days_since_last_transaction",
    "balance_change_30d",
    "transaction_change_30d",
    "card_spend_change_30d",
    "app_login_change_30d",
    "salary_missing_days",
    "external_transfer_change_30d",
    "upi_share_of_spend",
    "fd_maturing_in_30d",
    "products_dropped_90d",
    "complaints_30d",
    "unresolved_complaints",
    "failed_transactions_30d",
    "avg_resolution_time_hrs",
    "emi_bounce_30d",
]


def clean_value(value: Any) -> Any:
    if value is None:
        return None
    if isinstance(value, (pd.Timestamp, datetime, date)):
        return value.isoformat()
    if isinstance(value, float) and math.isnan(value):
        return None
    try:
        if pd.isna(value):
            return None
    except Exception:
        pass
    if hasattr(value, "item"):
        item = value.item()
        if isinstance(item, (datetime, date)):
            return item.isoformat()
        return item
    return value


def clean_record(record: dict[str, Any]) -> dict[str, Any]:
    return {key: clean_value(value) for key, value in record.items()}


def json_ready(value: Any) -> Any:
    if isinstance(value, dict):
        return {str(key): json_ready(item) for key, item in value.items()}
    if isinstance(value, list):
        return [json_ready(item) for item in value]
    if isinstance(value, tuple):
        return [json_ready(item) for item in value]
    return clean_value(value)


def value_tier(customer_yearly_value: Any) -> str:
    value = float(customer_yearly_value or 0)
    if value >= 80000:
        return "high"
    if value >= 35000:
        return "medium"
    return "low"


def infer_risk_group(row: dict[str, Any]) -> str:
    behaviour_problem = (
        clean_value(row.get("balance_change_30d")) is not None
        and float(row["balance_change_30d"]) < -15
    ) or (
        clean_value(row.get("external_transfer_change_30d")) is not None
        and float(row["external_transfer_change_30d"]) > 25
    ) or int(row.get("days_since_last_transaction") or 0) >= 15
    service_problem = int(row.get("complaints_30d") or 0) > 0 or int(row.get("unresolved_complaints") or 0) > 0

    if behaviour_problem and service_problem:
        return "both"
    if behaviour_problem:
        return "behaviour_problem"
    if service_problem:
        return "service_problem"
    return "neither"


def customer_ids(
    df: pd.DataFrame,
    limit: int | None,
    seed: int | None,
    start_after_customer_id: str | None,
) -> list[Any]:
    ids = pd.Series(sorted(df["customer_id"].dropna().unique()))
    if start_after_customer_id:
        ids = ids[ids.astype(str) > str(start_after_customer_id)]
    if limit is not None:
        ids = ids.sample(n=min(limit, len(ids)), random_state=seed) if seed is not None else ids.head(limit)
    return ids.sort_values().tolist()


def history_for_customer(df: pd.DataFrame, customer_id: Any) -> pd.DataFrame:
    history = df[df["customer_id"] == customer_id].copy()
    history["snapshot_date"] = pd.to_datetime(history["snapshot_date"])
    return history.sort_values("snapshot_date").tail(6)


def customer_histories(df: pd.DataFrame, selected_ids: list[Any]) -> dict[Any, pd.DataFrame]:
    df = df.copy()
    df["snapshot_date"] = pd.to_datetime(df["snapshot_date"])
    selected = df[df["customer_id"].isin(selected_ids)].sort_values(["customer_id", "snapshot_date"])
    return {
        customer_id: history.tail(6).copy()
        for customer_id, history in selected.groupby("customer_id", sort=False)
    }


def build_customer_case(history: pd.DataFrame) -> dict[str, Any]:
    latest = clean_record(history.iloc[-1].to_dict())
    latest_date = pd.to_datetime(latest["snapshot_date"])
    full_history = [
        clean_record(record)
        for record in history.assign(snapshot_date=history["snapshot_date"].dt.date.astype(str)).to_dict(orient="records")
    ]

    profile = {feature: latest[feature] for feature in PROFILE_FEATURES}
    customer = {feature: latest[feature] for feature in PROFILE_FEATURES + BEHAVIOR_FEATURES}
    monthly_history = [
        clean_record(record)
        for record in history[["snapshot_date", *BEHAVIOR_FEATURES]]
        .assign(snapshot_date=history["snapshot_date"].dt.date.astype(str))
        .to_dict(orient="records")
    ]
    extra_context = {
        "customer_profile": {
            "segment": latest["customer_segment"],
            "income_regularity": latest["income_regularity"],
            "tenure_months": latest["tenure_months"],
            "age": latest["age"],
            "customer_yearly_value": latest["customer_yearly_value"],
            "products_count": latest["products_count"],
            "has_credit_card": latest["has_credit_card"],
            "has_loan": latest["has_loan"],
            "value_tier": value_tier(latest["customer_yearly_value"]),
        },
        "trend_last_3_months": {
            "days_since_last_transaction": history["days_since_last_transaction"].map(clean_value).tolist(),
            "balance_change_30d": history["balance_change_30d"].map(clean_value).tolist(),
            "external_transfer_change_30d": history["external_transfer_change_30d"].map(clean_value).tolist(),
            "complaints_30d": history["complaints_30d"].map(clean_value).tolist(),
            "overall_direction": "declining" if float(latest.get("balance_change_30d") or 0) < -10 else "stable",
        },
        "recent_complaint_text": latest.get("complaint_text"),
        "risk_group": infer_risk_group(latest),
    }

    request = {
        "customer_id": latest["customer_id"],
        "customer_name": latest["customer_name"],
        "prediction_date": str(latest_date.date()),
        "snapshot_date": str(latest_date.date()),
        "target_month": str((latest_date + pd.DateOffset(months=1)).date()),
        "profile": profile,
        "monthly_history": monthly_history,
        "customer": customer,
        "extra_context": extra_context,
    }
    return {
        "customer_profile": extra_context["customer_profile"],
        "snapshots_1_to_6_months": full_history,
        "latest_customer_snapshot": latest,
        "request": request,
        "model1_input": {
            "profile": profile,
            "monthly_history": monthly_history,
            "customer": customer,
            "customer_id": latest["customer_id"],
            "customer_name": latest["customer_name"],
            "prediction_date": request["prediction_date"],
            "snapshot_date": request["snapshot_date"],
            "target_month": request["target_month"],
        },
    }


def ensure_models_loaded() -> None:
    print(f"Checking Ollama at {server.OLLAMA_HOST}...", flush=True)
    try:
        with urllib.request.urlopen(OLLAMA_TAGS_URL, timeout=30) as response:
            tags = json.loads(response.read().decode("utf-8"))
    except (TimeoutError, urllib.error.URLError, OSError) as exc:
        raise RuntimeError(
            "Ollama is not responding. Start it in another terminal with `ollama serve`, "
            "wait until it prints `Listening on 127.0.0.1:11434`, then rerun this script."
        ) from exc

    model_names = {item.get("name") for item in tags.get("models", [])}
    if EXPECTED_OLLAMA_MODEL not in model_names and f"{EXPECTED_OLLAMA_MODEL}:latest" not in model_names:
        raise RuntimeError(
            f"Ollama is running, but model `{EXPECTED_OLLAMA_MODEL}` was not found. "
            f"Available models: {sorted(model_names)}"
        )

    print("Loading Model 2 recovery schema...", flush=True)
    server.load_model2_recovery_config()
    if server.model1 is None:
        print("Loading Model 1 v2...", flush=True)
        server.load_model1()
    else:
        print("Model 1 v2 already loaded.", flush=True)
    if server.model2 is None:
        print("Loading 0.5b v2 Model 2...", flush=True)
        server.load_model2()
    else:
        print("0.5b v2 Model 2 already loaded.", flush=True)
    print("Models ready.", flush=True)


def save_results(output_json: Path, results: list[dict[str, Any]]) -> None:
    output_json.parent.mkdir(parents=True, exist_ok=True)
    output_json.write_text(json.dumps(json_ready(results), indent=2, ensure_ascii=False), encoding="utf-8")


def format_seconds(seconds: float) -> str:
    seconds = max(0, int(round(seconds)))
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    if hours:
        return f"{hours}h {minutes}m {seconds}s"
    if minutes:
        return f"{minutes}m {seconds}s"
    return f"{seconds}s"


def result_customer_id(result: dict[str, Any]) -> str | None:
    request = result.get("request") or {}
    customer_id = request.get("customer_id")
    if customer_id is None:
        identity = (result.get("model2_input") or {}).get("customer_identity") or {}
        customer_id = identity.get("customer_id")
    return str(customer_id) if customer_id is not None else None


def load_existing_results(output_json: Path) -> dict[str, dict[str, Any]]:
    if not output_json.exists():
        return {}
    data = json.loads(output_json.read_text(encoding="utf-8"))
    if not isinstance(data, list):
        raise ValueError(f"Existing output must be a JSON list: {output_json}")

    results = {}
    for item in data:
        if not isinstance(item, dict):
            continue
        customer_id = result_customer_id(item)
        if customer_id is not None:
            results[customer_id] = item
    return results


def completed_results(results: list[dict[str, Any] | None]) -> list[dict[str, Any]]:
    return [item for item in results if item is not None]


def ordered_results(
    ordered_customer_ids: list[Any],
    existing_results: dict[str, dict[str, Any]],
    new_results: list[dict[str, Any] | None],
) -> list[dict[str, Any]]:
    by_customer_id = dict(existing_results)
    for item in completed_results(new_results):
        customer_id = result_customer_id(item)
        if customer_id is not None:
            by_customer_id[customer_id] = item
    ordered = []
    seen = set()
    for customer_id in ordered_customer_ids:
        key = str(customer_id)
        if key in by_customer_id:
            ordered.append(by_customer_id[key])
            seen.add(key)
    for customer_id, result in existing_results.items():
        if customer_id not in seen:
            ordered.append(result)
    return ordered


def process_customer(index: int, total: int, history: pd.DataFrame) -> tuple[int, dict[str, Any]]:
    started_at = time.perf_counter()
    worker_name = threading.current_thread().name
    item = build_customer_case(history)
    request = server.BothRequest(**item["request"])
    print(
        f"[{index}/{total}] [{worker_name}] Processing "
        f"{item['request']['customer_id']} - {item['request']['customer_name']}",
        flush=True,
    )

    try:
        print(f"  [{index}/{total}] [{worker_name}] Running Model 1 v2...", flush=True)
        model1_output = server.predict_model1(request)
        latest_customer = server.latest_customer_from_request(request)
        print(f"  [{index}/{total}] [{worker_name}] Building 0.5b v2 Model 2 input...", flush=True)
        model2_input = server.build_model2_payload(
            latest_customer,
            model1_output,
            request.extra_context,
            request.customer_id,
            request.customer_name,
            request.snapshot_date or request.prediction_date,
        )
        print(f"  [{index}/{total}] [{worker_name}] Running 0.5b v2 Model 2...", flush=True)
        model2_output = server.predict_model2(model2_input)
        item.update(
            {
                "ok": True,
                "model1_output": model1_output,
                "model2_input": model2_input,
                "model2_output": model2_output,
                "error": None,
            }
        )
        print(
            f"  [{index}/{total}] [{worker_name}] Customer done in "
            f"{round(time.perf_counter() - started_at, 2)}s.",
            flush=True,
        )
    except Exception as exc:
        item.update({"ok": False, "error": str(exc)})
        print(f"  [{index}/{total}] [{worker_name}] Customer failed: {exc}", flush=True)

    item["seconds"] = round(time.perf_counter() - started_at, 2)
    item["worker"] = worker_name
    return index, item


def print_progress(completed: int, total: int, workers: int, started_at: float) -> None:
    elapsed = time.perf_counter() - started_at
    avg_seconds = elapsed / completed if completed else 0
    customers_per_minute = (completed / elapsed) * 60 if elapsed else 0
    remaining = max(0, total - completed)
    eta_seconds = remaining * avg_seconds
    print(
        f"  Progress: {completed:,}/{total:,} done | workers={workers} | "
        f"total={format_seconds(elapsed)} | avg={avg_seconds:.2f}s/customer | "
        f"rate={customers_per_minute:.2f}/min | eta={format_seconds(eta_seconds)}",
        flush=True,
    )


def run_pipeline(
    input_csv: Path,
    output_json: Path,
    limit: int | None,
    seed: int | None,
    start_after_customer_id: str | None,
    workers: int,
    resume: bool,
) -> list[dict[str, Any]]:
    print(f"Reading customers from {input_csv}", flush=True)
    df = pd.read_csv(input_csv)
    ordered_ids = customer_ids(df, limit, seed, start_after_customer_id)
    existing_results = load_existing_results(output_json) if resume else {}
    selected_ids = [customer_id for customer_id in ordered_ids if str(customer_id) not in existing_results]
    if resume:
        print(f"Existing output results: {len(existing_results):,}", flush=True)
    print(f"Customers to process: {len(selected_ids):,}", flush=True)
    if start_after_customer_id:
        print(f"Starting after customer_id {start_after_customer_id}", flush=True)
    ensure_models_loaded()

    workers = max(1, workers)
    print(f"Preparing customer histories...", flush=True)
    histories = customer_histories(df, selected_ids)
    print(f"Running with {workers} worker(s).", flush=True)

    total = len(selected_ids)
    results: list[dict[str, Any] | None] = [None] * total
    completed = 0
    processing_started_at = time.perf_counter()

    if workers == 1:
        for index, customer_id in enumerate(selected_ids, start=1):
            position, item = process_customer(index, total, histories[customer_id])
            results[position - 1] = item
            completed += 1
            print_progress(completed, total, workers, processing_started_at)
            if completed % CHECKPOINT_EVERY == 0:
                save_results(output_json, ordered_results(ordered_ids, existing_results, results))
                print(
                    f"  Checkpoint saved: {completed:,} customers -> {output_json} | "
                    f"total={format_seconds(time.perf_counter() - processing_started_at)}",
                    flush=True,
                )
    else:
        with ThreadPoolExecutor(max_workers=workers, thread_name_prefix="worker") as executor:
            futures = [
                executor.submit(process_customer, index, total, histories[customer_id])
                for index, customer_id in enumerate(selected_ids, start=1)
            ]
            for future in as_completed(futures):
                position, item = future.result()
                results[position - 1] = item
                completed += 1
                print_progress(completed, total, workers, processing_started_at)
                if completed % CHECKPOINT_EVERY == 0:
                    save_results(output_json, ordered_results(ordered_ids, existing_results, results))
                    print(
                        f"  Checkpoint saved: {completed:,} customers -> {output_json} | "
                        f"total={format_seconds(time.perf_counter() - processing_started_at)}",
                        flush=True,
                    )

    final_results = ordered_results(ordered_ids, existing_results, results)
    save_results(output_json, final_results)
    print(
        f"Saved JSON to {output_json} | processing time="
        f"{format_seconds(time.perf_counter() - processing_started_at)}",
        flush=True,
    )
    return final_results


def main() -> None:
    parser = argparse.ArgumentParser(description="Run Model 1 v2 + 0.5b v2 Model 2 for customers.csv.")
    parser.add_argument("--input", default=str(CUSTOMERS_CSV), help="Input customers CSV.")
    parser.add_argument("--output", default=str(DEFAULT_OUTPUT), help="Output JSON path.")
    parser.add_argument("--limit", type=int, default=None, help="Optional customer limit for smoke tests.")
    parser.add_argument("--seed", type=int, default=None, help="Optional random seed when --limit is set.")
    parser.add_argument(
        "--start-after-customer-id",
        default=None,
        help="Skip customer IDs up to and including this value. Useful after an interrupted run.",
    )
    parser.add_argument(
        "--workers",
        type=int,
        default=8,
        help="Number of customers to process concurrently. Use 1 for serial execution.",
    )
    parser.add_argument(
        "--resume",
        action="store_true",
        help="Keep existing output rows and process only customer IDs missing from the output file.",
    )
    args = parser.parse_args()

    started_at = time.perf_counter()
    results = run_pipeline(
        Path(args.input),
        Path(args.output),
        args.limit,
        args.seed,
        args.start_after_customer_id,
        args.workers,
        args.resume,
    )
    ok_count = sum(1 for item in results if item.get("ok"))
    print("")
    print(f"Finished at {datetime.now().isoformat(timespec='seconds')}")
    print(f"Successful customers: {ok_count:,}/{len(results):,}")
    print(f"Elapsed seconds: {round(time.perf_counter() - started_at, 2)}")


if __name__ == "__main__":
    main()
