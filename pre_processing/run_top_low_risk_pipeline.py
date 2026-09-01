import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
import json
import math
import sys
import time
import urllib.error
import urllib.request
from datetime import date, datetime
from pathlib import Path
from typing import Any

import numpy as np
import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from backend import devang_api_server as server


CUSTOMERS_CSV = ROOT / "model_1_v2" / "data" / "customers.csv"
MODEL1_OUTPUT_JSON = ROOT / "pre_processing" / "outputs" / "model_1_v2_customer_outputs.json"
DEFAULT_OUTPUT = ROOT / "pre_processing" / "outputs" / "top_low_risk_customers.json"

DEFAULT_WORKERS = 6
CHECKPOINT_EVERY = 10
PROGRESS_WIDTH = 30
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


def format_seconds(seconds: float) -> str:
    seconds = max(0, int(round(seconds)))
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    if hours:
        return f"{hours}h {minutes}m {seconds}s"
    if minutes:
        return f"{minutes}m {seconds}s"
    return f"{seconds}s"


def load_model1_outputs(path: Path) -> dict[str, dict[str, Any]]:
    if not path.exists():
        raise FileNotFoundError(f"Missing Model 1 output JSON: {path}")

    data = json.loads(path.read_text(encoding="utf-8"))
    rows = data.get("customers") if isinstance(data, dict) else data
    if not isinstance(rows, list):
        raise ValueError(f"Model 1 output JSON must contain a customers list: {path}")

    outputs: dict[str, dict[str, Any]] = {}
    for row in rows:
        if not isinstance(row, dict):
            continue
        customer_id = row.get("customer_id")
        model1_output = row.get("model_1_output") or row.get("model1_output")
        if customer_id is None or not isinstance(model1_output, dict):
            continue
        outputs[str(customer_id)] = {
            "customer_id": row.get("customer_id"),
            "customer_name": row.get("customer_name"),
            "model1_input": row.get("model_1_input") or row.get("model1_input"),
            "model1_output": model1_output,
        }
    return outputs


def select_top_low_risk_records(
    model1_outputs: dict[str, dict[str, Any]],
    percentile_threshold: float = 90.0,
    top_n: int | None = 688,
) -> list[dict[str, Any]]:
    """
    Select Tier 5 Low Risk customers (top 10% highest churn probability among Low Risk).
    """
    low_records = [
        rec for rec in model1_outputs.values()
        if rec["model1_output"].get("risk_level") == "Low"
    ]
    
    if not low_records:
        raise ValueError("No Low Risk customers found in Model 1 output JSON.")

    probs = [rec["model1_output"].get("churn_probability", 0.0) for rec in low_records]
    p_val = float(np.percentile(probs, percentile_threshold))

    # Sort descending by churn_probability and risk_score
    sorted_low = sorted(
        low_records,
        key=lambda rec: (
            rec["model1_output"].get("churn_probability", 0.0),
            rec["model1_output"].get("risk_score", 0.0),
            str(rec.get("customer_id", ""))
        ),
        reverse=True,
    )

    if top_n is not None and top_n > 0:
        selected = sorted_low[:top_n]
    else:
        selected = [rec for rec in sorted_low if rec["model1_output"].get("churn_probability", 0.0) > p_val]

    return selected


def customer_histories(df: pd.DataFrame, selected_ids: list[str]) -> dict[str, pd.DataFrame]:
    df = df.copy()
    df["customer_id"] = df["customer_id"].astype(str)
    df["snapshot_date"] = pd.to_datetime(df["snapshot_date"])
    selected = df[df["customer_id"].isin(selected_ids)].sort_values(["customer_id", "snapshot_date"])
    return {
        str(customer_id): history.tail(6).copy()
        for customer_id, history in selected.groupby("customer_id", sort=False)
    }


def build_customer_case(history: pd.DataFrame, model1_record: dict[str, Any]) -> dict[str, Any]:
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
        "customer_id": latest["customer_id"],
        "customer_name": latest["customer_name"],
        "risk_level": model1_record["model1_output"].get("risk_level"),
        "customer_profile": extra_context["customer_profile"],
        "snapshots_1_to_6_months": full_history,
        "latest_customer_snapshot": latest,
        "request": request,
        "model1_input": model1_record.get("model1_input"),
        "model1_output": model1_record["model1_output"],
    }


def ensure_devang_model_loaded() -> None:
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

    server.PRINT_PREDICTIONS = False
    server.require_ollama_model()
    print(f"Devang Model 2 ready: {EXPECTED_OLLAMA_MODEL}", flush=True)


def result_customer_id(result: dict[str, Any]) -> str | None:
    customer_id = result.get("customer_id")
    if customer_id is None:
        request = result.get("request") or {}
        customer_id = request.get("customer_id")
    if customer_id is None:
        model2_input = result.get("model2_input") or {}
        customer_id = model2_input.get("case_id")
    return str(customer_id) if customer_id is not None else None


def load_existing_results(output_json: Path) -> dict[str, dict[str, Any]]:
    if not output_json.exists():
        return {}
    try:
        data = json.loads(output_json.read_text(encoding="utf-8"))
    except Exception:
        return {}
    rows = data.get("customers") if isinstance(data, dict) else data
    if not isinstance(rows, list):
        return {}

    results = {}
    for item in rows:
        if not isinstance(item, dict):
            continue
        customer_id = result_customer_id(item)
        if customer_id is not None:
            results[customer_id] = item
    return results


def risk_summary(results: list[dict[str, Any]]) -> dict[str, int]:
    counts = {"High": 0, "Medium": 0, "Low": 0, "Unknown": 0}
    for item in results:
        risk = item.get("risk_level") or (item.get("model1_output") or {}).get("risk_level") or "Unknown"
        counts[risk if risk in counts else "Unknown"] += 1
    return {
        "total_high_risk": counts["High"],
        "total_medium_risk": counts["Medium"],
        "total_low_risk": counts["Low"],
        "total_unknown_risk": counts["Unknown"],
    }


def output_document(
    results: list[dict[str, Any]],
    total_selected: int,
    skipped_existing: int,
    started_at: float,
    status: str,
    workers: int,
) -> dict[str, Any]:
    ok_count = sum(1 for item in results if item.get("ok"))
    return {
        "total_customer_selected": total_selected,
        "total_customer_processed": len(results),
        "successful_customers": ok_count,
        "failed_customers": len(results) - ok_count,
        "skipped_existing_customers": skipped_existing,
        "risk_summary": risk_summary(results),
        "meta": {
            "tier_description": "Tier 5 Low Risk (Top 10% highest churn probability in Low Risk)",
            "status": status,
            "model": "devang-model2",
            "model1_source": "precomputed_json",
            "created_at": datetime.now().isoformat(timespec="seconds"),
            "elapsed_seconds": round(time.perf_counter() - started_at, 2),
            "workers": workers,
        },
        "customers": results,
    }


def save_results(
    output_json: Path,
    results: list[dict[str, Any]],
    total_selected: int,
    skipped_existing: int,
    started_at: float,
    status: str,
    workers: int,
) -> None:
    output_json.parent.mkdir(parents=True, exist_ok=True)
    document = output_document(results, total_selected, skipped_existing, started_at, status, workers)
    output_json.write_text(json.dumps(json_ready(document), indent=2, ensure_ascii=False), encoding="utf-8")


def ordered_results(
    ordered_ids: list[str],
    existing: dict[str, dict[str, Any]],
    new: list[dict[str, Any]],
) -> list[dict[str, Any]]:
    by_id = dict(existing)
    for item in new:
        customer_id = result_customer_id(item)
        if customer_id is not None:
            by_id[customer_id] = item
    return [by_id[customer_id] for customer_id in ordered_ids if customer_id in by_id]


def progress_line(completed: int, total: int, workers: int, started_at: float, ok: int, failed: int) -> str:
    elapsed = time.perf_counter() - started_at
    ratio = completed / total if total else 1.0
    filled = int(PROGRESS_WIDTH * ratio)
    bar = "#" * filled + "-" * (PROGRESS_WIDTH - filled)
    avg_seconds = elapsed / completed if completed else 0
    rate = (completed / elapsed) * 60 if elapsed else 0
    eta = (total - completed) * avg_seconds
    return (
        f"\r[{bar}] {completed:,}/{total:,} ({ratio * 100:5.1f}%) | "
        f"ok={ok:,} fail={failed:,} | workers={workers} | "
        f"elapsed={format_seconds(elapsed)} | avg={avg_seconds:.1f}s | "
        f"rate={rate:.2f}/min | eta={format_seconds(eta)}"
    )


def print_progress(completed: int, total: int, workers: int, started_at: float, ok: int, failed: int) -> None:
    print(progress_line(completed, total, workers, started_at, ok, failed), end="", flush=True)


def process_customer(index: int, total: int, history: pd.DataFrame, model1_record: dict[str, Any]) -> tuple[int, dict[str, Any]]:
    started_at = time.perf_counter()
    item = build_customer_case(history, model1_record)
    request = server.BothRequest(**item["request"])

    try:
        latest_customer = server.model1_server.latest_customer_from_request(request)
        model2_input = server.build_devang_model2_input(
            customer=latest_customer,
            model1_output=item["model1_output"],
            extra_context=request.extra_context,
            case_id=request.customer_id,
        )
        model2_output = server.predict_one(model2_input)
        item.update(
            {
                "ok": True,
                "model2_input": model2_input,
                "model2_output": model2_output,
                "error": None,
            }
        )
    except Exception as exc:
        item.update({"ok": False, "error": str(exc)})

    item["seconds"] = round(time.perf_counter() - started_at, 2)
    item["position"] = index
    item["total"] = total
    return index, item


def run_pipeline(
    input_csv: Path,
    model1_json: Path,
    output_json: Path,
    top_n: int,
    workers: int,
    resume: bool,
    checkpoint_every: int,
) -> list[dict[str, Any]]:
    started_at = time.perf_counter()
    print(f"Loading Model 1 outputs from {model1_json}", flush=True)
    model1_outputs = load_model1_outputs(model1_json)
    
    # Select Tier 5 Low Risk (top 688 by churn probability descending)
    selected_records = select_top_low_risk_records(model1_outputs, percentile_threshold=90.0, top_n=top_n)
    selected_ids = [str(record["customer_id"]) for record in selected_records]
    selected_by_id = {str(record["customer_id"]): record for record in selected_records}

    existing_results = load_existing_results(output_json) if resume else {}
    ids_to_process = [customer_id for customer_id in selected_ids if customer_id not in existing_results]
    skipped_existing = len(selected_ids) - len(ids_to_process)

    min_prob = min(r["model1_output"].get("churn_probability", 0) for r in selected_records)
    max_prob = max(r["model1_output"].get("churn_probability", 0) for r in selected_records)

    print(f"Target Pool: Tier 5 Low-Risk Customers (P90 to P100)", flush=True)
    print(f"Total Selected: {len(selected_ids):,} customers (Churn Prob Range: {min_prob:.2f}% to {max_prob:.2f}%)", flush=True)
    
    if resume and skipped_existing > 0:
        print(
            f"Resume enabled: loaded {len(existing_results):,} existing results from {output_json}. "
            f"Skipping {skipped_existing:,} already completed customers. {len(ids_to_process):,} remaining.",
            flush=True,
        )
    elif len(ids_to_process) == 0:
        print(f"All {len(selected_ids):,} customers are already completed in {output_json}!", flush=True)
        return [existing_results[cid] for cid in selected_ids if cid in existing_results]

    print(f"Reading CSV context from {input_csv}", flush=True)
    df = pd.read_csv(input_csv)
    histories = customer_histories(df, ids_to_process)
    missing_csv_ids = sorted(set(ids_to_process) - set(histories))
    if missing_csv_ids:
        raise ValueError(f"{len(missing_csv_ids):,} selected customers are missing from CSV, first={missing_csv_ids[0]}")

    ensure_devang_model_loaded()

    workers = max(1, workers)
    total = len(ids_to_process)
    completed = 0
    ok_count = 0
    failed_count = 0
    new_results: list[dict[str, Any]] = []
    processing_started_at = time.perf_counter()

    print(f"Running Devang Model 2 with {workers} workers for {total:,} customers.", flush=True)
    print_progress(completed, total, workers, processing_started_at, ok_count, failed_count)

    if total:
        with ThreadPoolExecutor(max_workers=workers, thread_name_prefix="top_low_risk") as executor:
            futures = [
                executor.submit(process_customer, index, total, histories[customer_id], selected_by_id[customer_id])
                for index, customer_id in enumerate(ids_to_process, start=1)
            ]
            for future in as_completed(futures):
                _, item = future.result()
                new_results.append(item)
                completed += 1
                if item.get("ok"):
                    ok_count += 1
                else:
                    failed_count += 1
                print_progress(completed, total, workers, processing_started_at, ok_count, failed_count)

                if checkpoint_every > 0 and completed % checkpoint_every == 0:
                    final_so_far = ordered_results(selected_ids, existing_results, new_results)
                    save_results(
                        output_json,
                        final_so_far,
                        len(selected_ids),
                        skipped_existing,
                        started_at,
                        "partial",
                        workers,
                    )

    print("", flush=True)
    final_results = ordered_results(selected_ids, existing_results, new_results)
    save_results(
        output_json,
        final_results,
        len(selected_ids),
        skipped_existing,
        started_at,
        "complete",
        workers,
    )
    print(f"Saved JSON checkpoint/output to {output_json}", flush=True)
    return final_results


def main() -> None:
    parser = argparse.ArgumentParser(description="Run Devang Model 2 on Tier 5 (Top 10% Highest Probability) Low-Risk Customers.")
    parser.add_argument("--input", default=str(CUSTOMERS_CSV), help="Input customers CSV for raw customer context.")
    parser.add_argument("--model1-json", default=str(MODEL1_OUTPUT_JSON), help="Precomputed Model 1 v2 output JSON.")
    parser.add_argument("--output", default=str(DEFAULT_OUTPUT), help="Output JSON path.")
    parser.add_argument("--top-n", type=int, default=688, help="Number of top low-risk customers to process (default: 688).")
    parser.add_argument("--workers", type=int, default=DEFAULT_WORKERS, help="Number of concurrent Devang workers (default: 6).")
    parser.add_argument(
        "--resume",
        action=argparse.BooleanOptionalAction,
        default=True,
        help="Skip customer IDs already present in the output JSON. Enabled by default.",
    )
    parser.add_argument(
        "--checkpoint-every",
        type=int,
        default=CHECKPOINT_EVERY,
        help="Save partial JSON every N completed customers (default: 10). Use 0 to disable checkpoints.",
    )
    args = parser.parse_args()

    started_at = time.perf_counter()
    results = run_pipeline(
        input_csv=Path(args.input),
        model1_json=Path(args.model1_json),
        output_json=Path(args.output),
        top_n=args.top_n,
        workers=args.workers,
        resume=args.resume,
        checkpoint_every=args.checkpoint_every,
    )
    ok_count = sum(1 for item in results if item.get("ok"))
    print("")
    print(f"Finished at {datetime.now().isoformat(timespec='seconds')}")
    print(f"Successful Devang Model 2 customers: {ok_count:,}/{len(results):,}")
    print(f"Elapsed seconds: {round(time.perf_counter() - started_at, 2)}")


if __name__ == "__main__":
    main()
