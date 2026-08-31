import argparse
import json
import math
import sys
import time
from datetime import date, datetime
from pathlib import Path
from typing import Any

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from backend import retention_api_server as server


CUSTOMERS_CSV = ROOT / "model_1_v2" / "data" / "customers.csv"
DEFAULT_OUTPUT = ROOT / "pre_processing" / "outputs" / "model_1_v2_customer_outputs.json"
DEFAULT_CHECKPOINT_EVERY = 100

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


def json_ready(value: Any) -> Any:
    if isinstance(value, dict):
        return {str(key): json_ready(item) for key, item in value.items()}
    if isinstance(value, list):
        return [json_ready(item) for item in value]
    if isinstance(value, tuple):
        return [json_ready(item) for item in value]
    return clean_value(value)


def clean_record(record: dict[str, Any]) -> dict[str, Any]:
    return {key: clean_value(value) for key, value in record.items()}


def customer_ids(df: pd.DataFrame, limit: int | None, seed: int | None) -> list[Any]:
    ids = pd.Series(sorted(df["customer_id"].dropna().unique()))
    if limit is not None:
        ids = ids.sample(n=min(limit, len(ids)), random_state=seed) if seed is not None else ids.head(limit)
    return ids.sort_values().tolist()


def customer_histories(df: pd.DataFrame, selected_ids: list[Any]) -> dict[Any, pd.DataFrame]:
    df = df.copy()
    df["snapshot_date"] = pd.to_datetime(df["snapshot_date"])
    selected = df[df["customer_id"].isin(selected_ids)].sort_values(["customer_id", "snapshot_date"])
    return {
        customer_id: history.copy()
        for customer_id, history in selected.groupby("customer_id", sort=False)
    }


def build_customer_record(history: pd.DataFrame) -> tuple[dict[str, Any], server.Model1Request]:
    latest = clean_record(history.iloc[-1].to_dict())
    latest_date = pd.to_datetime(latest["snapshot_date"])
    model_history = history.tail(6).copy()
    monthly_history = [
        clean_record(record)
        for record in model_history[["snapshot_date", *BEHAVIOR_FEATURES]]
        .assign(snapshot_date=model_history["snapshot_date"].dt.date.astype(str))
        .to_dict(orient="records")
    ]

    profile = {feature: latest[feature] for feature in PROFILE_FEATURES}
    customer = {feature: latest[feature] for feature in PROFILE_FEATURES + BEHAVIOR_FEATURES}
    request_payload = {
        "customer_id": latest["customer_id"],
        "customer_name": latest["customer_name"],
        "prediction_date": str(latest_date.date()),
        "snapshot_date": str(latest_date.date()),
        "target_month": str((latest_date + pd.DateOffset(months=1)).date()),
        "profile": profile,
        "monthly_history": monthly_history,
        "customer": customer,
    }
    request = server.Model1Request(**request_payload)
    engineered_row, _ = server.request_to_v2_row(request)

    record = {
        "customer_id": latest.get("customer_id"),
        "customer_name": latest.get("customer_name"),
        "model_1_input": clean_record(
            {feature: engineered_row.iloc[0][feature] for feature in server.metadata["features"]}
        ),
    }
    return record, request


def format_seconds(seconds: float) -> str:
    seconds = max(0, int(round(seconds)))
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    if hours:
        return f"{hours}h {minutes}m {seconds}s"
    if minutes:
        return f"{minutes}m {seconds}s"
    return f"{seconds}s"


def empty_risk_counts() -> dict[str, int]:
    return {"High": 0, "Medium": 0, "Low": 0, "Unknown": 0}


def output_document(
    customers: list[dict[str, Any]],
    total_customers: int,
    started_at: float,
    status: str,
) -> dict[str, Any]:
    risk_counts = empty_risk_counts()
    ok_count = 0
    failed_count = 0
    for customer in customers:
        if customer.get("ok"):
            ok_count += 1
        else:
            failed_count += 1
        risk_level = ((customer.get("model_1_output") or {}).get("risk_level") or "Unknown")
        risk_counts[risk_level if risk_level in risk_counts else "Unknown"] += 1

    return {
        "total_customer_processed": len(customers),
        "total_customers_in_scope": total_customers,
        "successful_customers": ok_count,
        "failed_customers": failed_count,
        "risk_summary": {
            "total_high_risk": risk_counts["High"],
            "total_medium_risk": risk_counts["Medium"],
            "total_low_risk": risk_counts["Low"],
            "total_unknown_risk": risk_counts["Unknown"],
        },
        "meta": {
            "status": status,
            "model": "model_1_v2",
            "created_at": datetime.now().isoformat(timespec="seconds"),
            "elapsed_seconds": round(time.perf_counter() - started_at, 2),
        },
        "customers": customers,
    }


def save_output(
    output_json: Path,
    customers: list[dict[str, Any]],
    total_customers: int,
    started_at: float,
    status: str,
) -> None:
    output_json.parent.mkdir(parents=True, exist_ok=True)
    document = output_document(customers, total_customers, started_at, status)
    output_json.write_text(json.dumps(json_ready(document), indent=2, ensure_ascii=False), encoding="utf-8")


def print_progress(completed: int, total: int, started_at: float) -> None:
    elapsed = time.perf_counter() - started_at
    avg_seconds = elapsed / completed if completed else 0
    rate = (completed / elapsed) * 60 if elapsed else 0
    eta = (total - completed) * avg_seconds
    print(
        f"Progress: {completed:,}/{total:,} customers done | "
        f"elapsed={format_seconds(elapsed)} | avg={avg_seconds:.2f}s/customer | "
        f"rate={rate:.2f}/min | eta={format_seconds(eta)}",
        flush=True,
    )


def run_model_1_v2(
    input_csv: Path,
    output_json: Path,
    limit: int | None,
    seed: int | None,
    checkpoint_every: int,
) -> dict[str, Any]:
    if not input_csv.exists():
        raise FileNotFoundError(f"Missing input CSV: {input_csv}")

    started_at = time.perf_counter()
    print(f"Reading customers from {input_csv}", flush=True)
    df = pd.read_csv(input_csv)
    selected_ids = customer_ids(df, limit, seed)
    total = len(selected_ids)
    print(f"Total customers to process: {total:,}", flush=True)

    print("Loading Model 1 v2...", flush=True)
    server.load_model1()
    print("Model 1 v2 ready.", flush=True)

    print("Preparing customer snapshots...", flush=True)
    histories = customer_histories(df, selected_ids)

    customers: list[dict[str, Any]] = []
    print("Starting predictions...", flush=True)
    for index, customer_id in enumerate(selected_ids, start=1):
        customer_started_at = time.perf_counter()
        history = histories[customer_id]
        latest = history.iloc[-1]
        print(
            f"[{index:,}/{total:,}] Running Model 1 v2 for "
            f"{latest['customer_id']} - {latest['customer_name']}",
            flush=True,
        )

        try:
            record, request = build_customer_record(history)
            record["model_1_output"] = server.predict_model1(request)
            record["ok"] = True
            record["error"] = None
        except Exception as exc:
            record = {
                "customer_id": clean_value(latest.get("customer_id")),
                "customer_name": clean_value(latest.get("customer_name")),
                "ok": False,
                "error": str(exc),
            }
            print(f"  Customer failed: {exc}", flush=True)

        record["seconds"] = round(time.perf_counter() - customer_started_at, 2)
        customers.append(record)
        risk = (record.get("model_1_output") or {}).get("risk_level", "Unknown")
        print(f"  Done in {record['seconds']}s | risk={risk}", flush=True)
        print_progress(index, total, started_at)

        if checkpoint_every > 0 and index % checkpoint_every == 0:
            save_output(output_json, customers, total, started_at, "partial")
            print(f"  Checkpoint saved to {output_json}", flush=True)

    save_output(output_json, customers, total, started_at, "complete")
    return output_document(customers, total, started_at, "complete")


def main() -> None:
    parser = argparse.ArgumentParser(description="Run Model 1 v2 for customers.csv and save full JSON output.")
    parser.add_argument("--input", default=str(CUSTOMERS_CSV), help="Input customers.csv path.")
    parser.add_argument("--output", default=str(DEFAULT_OUTPUT), help="Output JSON path.")
    parser.add_argument("--limit", type=int, default=None, help="Optional customer limit for smoke tests.")
    parser.add_argument("--seed", type=int, default=None, help="Optional random seed when --limit is set.")
    parser.add_argument(
        "--checkpoint-every",
        type=int,
        default=DEFAULT_CHECKPOINT_EVERY,
        help="Save partial JSON after this many customers. Use 0 to disable checkpoints.",
    )
    args = parser.parse_args()

    started_at = time.perf_counter()
    document = run_model_1_v2(
        input_csv=Path(args.input),
        output_json=Path(args.output),
        limit=args.limit,
        seed=args.seed,
        checkpoint_every=args.checkpoint_every,
    )

    print("")
    print("Model 1 v2 JSON export complete.", flush=True)
    print(f"Customers processed: {document['total_customer_processed']:,}", flush=True)
    print(f"Successful customers: {document['successful_customers']:,}", flush=True)
    print(f"Failed customers: {document['failed_customers']:,}", flush=True)
    print(f"Risk summary: {document['risk_summary']}", flush=True)
    print(f"Output JSON: {Path(args.output)}", flush=True)
    print(f"Elapsed seconds: {round(time.perf_counter() - started_at, 2)}", flush=True)


if __name__ == "__main__":
    main()
