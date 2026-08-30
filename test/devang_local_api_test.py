import argparse
import json
import math
import time
from datetime import datetime
from pathlib import Path
from urllib import error, request

import pandas as pd


API_URL = "http://127.0.0.1:8001"
CUSTOMERS_CSV = Path("model_1_v2/data/customers.csv")
LOG_DIR = Path("logs")
CUSTOMER_LIMIT = 10
REQUEST_TIMEOUT_SECONDS = 240
MAX_ERROR_CHARS = 1000

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

EXPECTED_OUTPUT_KEYS = {
    "primary_reason",
    "secondary_reasons",
    "evidence",
    "urgency",
    "recommended_action",
    "reasoning_summary",
}


def clean_value(value):
    if value is None:
        return None
    if isinstance(value, float) and math.isnan(value):
        return None
    if pd.isna(value):
        return None
    if hasattr(value, "item"):
        return value.item()
    return value


def clean_record(record):
    return {key: clean_value(value) for key, value in record.items()}


def normalize_api_url(api_url):
    api_url = api_url.strip().rstrip("/")
    if not api_url.startswith(("http://", "https://")):
        api_url = f"http://{api_url}"
    return api_url


def short_error_text(text):
    return " ".join(text.split())[:MAX_ERROR_CHARS]


def get_json(api_url, endpoint):
    url = f"{api_url.rstrip('/')}{endpoint}"
    try:
        with request.urlopen(url, timeout=60) as response:
            return json.loads(response.read().decode("utf-8"))
    except error.HTTPError as exc:
        message = short_error_text(exc.read().decode("utf-8", errors="replace"))
        raise RuntimeError(f"HTTP {exc.code} from {url}: {message}") from exc
    except error.URLError as exc:
        raise RuntimeError(f"Could not call {url}: {exc}") from exc


def post_json(api_url, endpoint, payload):
    url = f"{api_url.rstrip('/')}{endpoint}"
    body = json.dumps(payload).encode("utf-8")
    req = request.Request(
        url,
        data=body,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    try:
        with request.urlopen(req, timeout=REQUEST_TIMEOUT_SECONDS) as response:
            return json.loads(response.read().decode("utf-8"))
    except error.HTTPError as exc:
        message = short_error_text(exc.read().decode("utf-8", errors="replace"))
        raise RuntimeError(f"HTTP {exc.code} from {url}: {message}") from exc
    except error.URLError as exc:
        raise RuntimeError(f"Could not call {url}: {exc}") from exc


def latest_rows_for_customers(df, limit, random_seed=None):
    df = df.copy()
    df["snapshot_date"] = pd.to_datetime(df["snapshot_date"])
    customer_ids = pd.Series(df["customer_id"].unique()).sample(
        n=min(limit, df["customer_id"].nunique()),
        random_state=random_seed,
    )
    return (
        df[df["customer_id"].isin(customer_ids)]
        .sort_values(["customer_id", "snapshot_date"])
        .groupby("customer_id", as_index=False)
        .tail(1)
        .sort_values("customer_id")
    )


def history_for_customer(df, customer_id, latest_date):
    customer_df = df[df["customer_id"] == customer_id].copy()
    customer_df["snapshot_date"] = pd.to_datetime(customer_df["snapshot_date"])
    return customer_df[customer_df["snapshot_date"] <= latest_date].sort_values("snapshot_date").tail(6)


def value_tier(customer_yearly_value):
    value = float(customer_yearly_value)
    if value >= 80000:
        return "high"
    if value >= 35000:
        return "medium"
    return "low"


def build_customer_request(df, row):
    row = clean_record(row.to_dict())
    latest_date = pd.to_datetime(row["snapshot_date"])
    history = history_for_customer(df, row["customer_id"], latest_date)

    profile = {feature: row[feature] for feature in PROFILE_FEATURES}
    customer = {feature: row[feature] for feature in PROFILE_FEATURES + BEHAVIOR_FEATURES}
    monthly_history = [
        clean_record(record)
        for record in history[["snapshot_date", *BEHAVIOR_FEATURES]]
        .assign(snapshot_date=history["snapshot_date"].dt.date.astype(str))
        .to_dict(orient="records")
    ]

    return {
        "customer_id": row["customer_id"],
        "customer_name": row["customer_name"],
        "prediction_date": str(latest_date.date()),
        "snapshot_date": str(latest_date.date()),
        "target_month": str((latest_date + pd.DateOffset(months=1)).date()),
        "profile": profile,
        "monthly_history": monthly_history,
        "customer": customer,
        "extra_context": {
            "customer_profile": {
                "segment": row["customer_segment"],
                "income_regularity": row["income_regularity"],
                "tenure_months": row["tenure_months"],
                "age": row["age"],
                "customer_yearly_value": row["customer_yearly_value"],
                "products_count": row["products_count"],
                "has_credit_card": row["has_credit_card"],
                "has_loan": row["has_loan"],
                "value_tier": value_tier(row["customer_yearly_value"]),
            },
            "recent_complaint_text": row.get("complaint_text"),
        },
    }


def validate_response_shape(response):
    errors = []
    if "model1" not in response:
        errors.append("response.model1 is missing")
    if "model2_input" not in response:
        errors.append("response.model2_input is missing")

    model2 = response.get("model2")
    if not isinstance(model2, dict):
        return errors + ["response.model2 is missing or not an object"]
    if not model2.get("ok"):
        errors.append(f"model2 returned ok=false: {model2.get('error')}")

    prediction = model2.get("prediction")
    if not isinstance(prediction, dict):
        return errors + ["model2.prediction is missing or not an object"]

    missing = EXPECTED_OUTPUT_KEYS - set(prediction)
    extra = set(prediction) - EXPECTED_OUTPUT_KEYS
    if missing:
        errors.append(f"missing output keys: {sorted(missing)}")
    if extra:
        errors.append(f"unexpected output keys: {sorted(extra)}")

    eligible_actions = (response.get("model2_input") or {}).get("eligible_actions") or []
    if prediction.get("recommended_action") not in eligible_actions:
        errors.append(
            f"recommended_action={prediction.get('recommended_action')} is not in eligible_actions={eligible_actions}"
        )
    return errors


def default_output_path():
    return LOG_DIR / f"devang_api_{datetime.now().strftime('%I-%M_%p').lower()}.md"


def fenced_json(value):
    return "```json\n" + json.dumps(value, indent=2, ensure_ascii=False) + "\n```"


def write_report(output_path, api_url, health, results):
    lines = [
        "# Devang Model 1 -> Model 2 API Test Results",
        "",
        f"- API URL: `{api_url}`",
        f"- Created at: `{datetime.now().isoformat(timespec='seconds')}`",
        f"- Customers tested: `{len(results)}`",
        f"- Source CSV: `{CUSTOMERS_CSV}`",
        f"- Health OK: `{health.get('ok')}`",
        f"- Ollama model: `{health.get('ollama_model')}`",
        f"- Model 1 loaded: `{health.get('model1_loaded')}`",
        "",
        "## Summary",
        "",
        "| # | Customer | Model 1 risk | Prediction | Reason | Urgency | Action | OK | Seconds |",
        "|---:|---|---:|---|---|---|---|---|---:|",
    ]

    for index, result in enumerate(results, start=1):
        response = result.get("response") or {}
        model1 = response.get("model1") or {}
        prediction = ((response.get("model2") or {}).get("prediction")) or {}
        lines.append(
            "| {index} | {name} (`{customer_id}`) | {risk} | {churn} | {reason} | {urgency} | {action} | {ok} | {seconds} |".format(
                index=index,
                name=result["customer_name"],
                customer_id=result["customer_id"],
                risk=model1.get("churn_probability", "NA"),
                churn=model1.get("churn_prediction", "NA"),
                reason=prediction.get("primary_reason", "NA"),
                urgency=prediction.get("urgency", "NA"),
                action=prediction.get("recommended_action", "NA"),
                ok="yes" if result["ok"] else "no",
                seconds=result["seconds"],
            )
        )

    lines.extend(["", "## Details", ""])
    for result in results:
        response = result.get("response")
        model2 = (response or {}).get("model2") or {}
        lines.extend(
            [
                f"### {result['customer_name']} (`{result['customer_id']}`)",
                "",
                f"- OK: `{result['ok']}`",
                f"- Shape errors: `{result['shape_errors']}`",
                f"- Simple output: {model2.get('simple_output')}",
                "",
                "Request:",
                "",
                fenced_json(result["request"]),
                "",
                "Response:",
                "",
                fenced_json(response or {"error": result.get("error")}),
                "",
            ]
        )

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("\n".join(lines), encoding="utf-8")


def run_test(api_url, limit, output_path, random_seed=None):
    api_url = normalize_api_url(api_url)
    print("Using API URL:", api_url)
    print("Checking health...")
    health = get_json(api_url, "/health")
    print("Health:", json.dumps(health, indent=2, ensure_ascii=False))

    df = pd.read_csv(CUSTOMERS_CSV)
    latest_rows = latest_rows_for_customers(df, limit, random_seed=random_seed)
    results = []

    for index, (_, row) in enumerate(latest_rows.iterrows(), start=1):
        customer_request = build_customer_request(df, row)
        print(f"[{index}/{len(latest_rows)}] {customer_request['customer_id']} - {customer_request['customer_name']}")
        started_at = time.perf_counter()
        result = {
            "customer_id": customer_request["customer_id"],
            "customer_name": customer_request["customer_name"],
            "request": customer_request,
            "ok": False,
            "shape_errors": [],
            "seconds": None,
        }
        try:
            response = post_json(api_url, "/predict/both", customer_request)
            shape_errors = validate_response_shape(response)
            result.update({"response": response, "shape_errors": shape_errors, "ok": not shape_errors})
            simple = (response.get("model2") or {}).get("simple_output")
            if simple:
                print("  ", simple)
            if shape_errors:
                print("  Shape errors:", shape_errors)
        except Exception as exc:
            result["error"] = str(exc)
            print("  Failed:", exc)
        result["seconds"] = round(time.perf_counter() - started_at, 2)
        results.append(result)

    write_report(output_path, api_url, health, results)
    print("Saved report to:", output_path)


def main():
    parser = argparse.ArgumentParser(description="Test Devang API with customer.csv via Model 1 -> Model 2.")
    parser.add_argument("--url", default=API_URL, help="API base URL.")
    parser.add_argument("--limit", type=int, default=CUSTOMER_LIMIT, help="Number of customers to test.")
    parser.add_argument("--output", default=None, help="Markdown output path.")
    parser.add_argument("--seed", type=int, default=None, help="Optional random seed.")
    args = parser.parse_args()

    output_path = Path(args.output) if args.output else default_output_path()
    run_test(args.url, args.limit, output_path, random_seed=args.seed)


if __name__ == "__main__":
    main()
