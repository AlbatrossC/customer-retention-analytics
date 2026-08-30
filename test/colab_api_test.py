import argparse
import json
import math
import time
from datetime import datetime
from pathlib import Path
from urllib import error, request

import pandas as pd


API_URL = "https://encryption-shall-foster-overall.trycloudflare.com"
CUSTOMERS_CSV = Path("model_1/data/customers.csv")
OUTPUT_MD = Path("test/colab_api_test_results.md")
CUSTOMER_LIMIT = 10
RANDOM_SEED = None
REQUEST_TIMEOUT_SECONDS = 240
MAX_ERROR_CHARS = 500
MAX_RETRIES = 2
RETRY_SLEEP_SECONDS = 5

MODEL1_FEATURES = [
    "age",
    "tenure_months",
    "customer_segment",
    "income_regularity",
    "products_count",
    "has_credit_card",
    "has_loan",
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
    "branch_code",
    "card_colour",
]


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
    api_url = api_url.strip()
    if api_url.startswith("[") and "](" in api_url and api_url.endswith(")"):
        api_url = api_url.split("](", 1)[1][:-1]
    api_url = api_url.strip().rstrip("/")
    if not api_url.startswith(("http://", "https://")):
        api_url = f"https://{api_url}"
    return api_url


def short_error_text(text):
    text = " ".join(text.split())
    if "<title>" in text.lower():
        lower = text.lower()
        start = lower.find("<title>") + len("<title>")
        end = lower.find("</title>", start)
        if end > start:
            text = text[start:end]
    return text[:MAX_ERROR_CHARS]


def post_json_once(api_url, endpoint, payload):
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


def post_json(api_url, endpoint, payload):
    last_error = None
    for attempt in range(1, MAX_RETRIES + 2):
        try:
            return post_json_once(api_url, endpoint, payload)
        except Exception as exc:
            last_error = exc
            if attempt <= MAX_RETRIES:
                print(f"Request failed. Retry {attempt}/{MAX_RETRIES} in {RETRY_SLEEP_SECONDS}s: {exc}")
                time.sleep(RETRY_SLEEP_SECONDS)
    raise last_error


def get_json_once(api_url, endpoint):
    url = f"{api_url.rstrip('/')}{endpoint}"
    try:
        with request.urlopen(url, timeout=60) as response:
            return json.loads(response.read().decode("utf-8"))
    except error.HTTPError as exc:
        message = short_error_text(exc.read().decode("utf-8", errors="replace"))
        raise RuntimeError(f"HTTP {exc.code} from {url}: {message}") from exc
    except error.URLError as exc:
        raise RuntimeError(f"Could not call {url}: {exc}") from exc


def get_json(api_url, endpoint):
    last_error = None
    for attempt in range(1, MAX_RETRIES + 2):
        try:
            return get_json_once(api_url, endpoint)
        except Exception as exc:
            last_error = exc
            if attempt <= MAX_RETRIES:
                print(f"Health check failed. Retry {attempt}/{MAX_RETRIES} in {RETRY_SLEEP_SECONDS}s: {exc}")
                time.sleep(RETRY_SLEEP_SECONDS)
    raise last_error


def latest_rows_for_customers(df, limit, random_seed=None):
    df = df.copy()
    df["snapshot_date"] = pd.to_datetime(df["snapshot_date"])
    customer_ids = pd.Series(df["customer_id"].unique()).sample(
        n=min(limit, df["customer_id"].nunique()),
        random_state=random_seed,
    )
    latest = (
        df[df["customer_id"].isin(customer_ids)]
        .sort_values(["customer_id", "snapshot_date"])
        .groupby("customer_id", as_index=False)
        .tail(1)
        .sort_values("customer_id")
    )
    return latest


def history_for_customer(df, customer_id, latest_date):
    customer_df = df[df["customer_id"] == customer_id].copy()
    customer_df["snapshot_date"] = pd.to_datetime(customer_df["snapshot_date"])
    history = customer_df[customer_df["snapshot_date"] <= latest_date].sort_values("snapshot_date").tail(3)
    return history


def infer_risk_group(row):
    behaviour_problem = (
        clean_value(row["balance_change_30d"]) is not None
        and float(row["balance_change_30d"]) < -15
    ) or (
        clean_value(row["external_transfer_change_30d"]) is not None
        and float(row["external_transfer_change_30d"]) > 25
    ) or int(row["days_since_last_transaction"]) >= 15

    service_problem = int(row["complaints_30d"]) > 0 or int(row["unresolved_complaints"]) > 0

    if behaviour_problem and service_problem:
        return "both"
    if behaviour_problem:
        return "behaviour_problem"
    if service_problem:
        return "service_problem"
    return "neither"


def value_tier(customer_yearly_value):
    value = float(customer_yearly_value)
    if value >= 80000:
        return "high"
    if value >= 35000:
        return "medium"
    return "low"


def build_request_payload(df, row):
    row = clean_record(row.to_dict())
    customer = {feature: row[feature] for feature in MODEL1_FEATURES}
    history = history_for_customer(df, row["customer_id"], pd.to_datetime(row["snapshot_date"]))

    extra_context = {
        "customer_profile": {
            "segment": row["customer_segment"],
            "income_regularity": row["income_regularity"],
            "tenure_months": row["tenure_months"],
            "age": row["age"],
            "products_count": row["products_count"],
            "has_credit_card": row["has_credit_card"],
            "has_loan": row["has_loan"],
            "value_tier": value_tier(row["customer_yearly_value"]),
        },
        "trend_last_3_months": {
            "days_since_last_transaction": history["days_since_last_transaction"].map(clean_value).tolist(),
            "balance_change_30d": history["balance_change_30d"].map(clean_value).tolist(),
            "external_transfer_change_30d": history["external_transfer_change_30d"].map(clean_value).tolist(),
            "complaints_30d": history["complaints_30d"].map(clean_value).tolist(),
            "overall_direction": "declining" if float(row["balance_change_30d"] or 0) < -10 else "stable",
        },
        "recent_complaint_text": row.get("complaint_text"),
        "risk_group": infer_risk_group(row),
    }

    return {
        "customer_id": row["customer_id"],
        "customer_name": row["customer_name"],
        "snapshot_date": str(pd.to_datetime(row["snapshot_date"]).date()),
        "customer": customer,
        "extra_context": extra_context,
    }


def format_list(items):
    if not items:
        return "None"
    if isinstance(items, str):
        return items
    return "<br>".join(f"- {item}" for item in items)


def top_factors_text(factors):
    if not factors:
        return "None"
    return "<br>".join(f"- {item.get('factor')}: {item.get('value')}" for item in factors)


def model2_quality(model2):
    if not isinstance(model2, dict):
        return "Invalid"
    if sorted(model2.keys()) != ["next_actions", "why"]:
        return "Invalid"
    if not isinstance(model2.get("why"), list):
        return "Invalid"
    if not isinstance(model2.get("next_actions"), list):
        return "Invalid"
    if not all(isinstance(item, str) and item.strip() for item in model2["why"]):
        return "Invalid"
    if not all(isinstance(item, str) and item.strip() for item in model2["next_actions"]):
        return "Invalid"
    return "Valid"


def write_markdown(output_path, api_url, health, results):
    lines = [
        "# Colab API Test Results",
        "",
        f"- API URL: `{api_url.rstrip('/')}`",
        f"- Created at: `{datetime.now().isoformat(timespec='seconds')}`",
        f"- Customers tested: `{len(results)}`",
        f"- Health: `{json.dumps(health)}`",
        "",
        "## Summary",
        "",
        "| # | Customer | Risk | Prediction | Model 2 Status | JSON |",
        "|---:|---|---:|---|---|---|",
    ]

    for index, result in enumerate(results, start=1):
        model1 = result.get("response", {}).get("model1", {})
        model2 = result.get("response", {}).get("model2")
        model2_status = "OK" if result.get("ok") and model2 else "Failed"
        quality = model2_quality(model2) if model2_status == "OK" else "NA"
        lines.append(
            "| {index} | {customer_name} (`{customer_id}`) | {risk}% | {prediction} | {status} | {quality} |".format(
                index=index,
                customer_name=result["customer_name"],
                customer_id=result["customer_id"],
                risk=model1.get("churn_probability", "NA"),
                prediction=model1.get("churn_prediction", "NA"),
                status=model2_status,
                quality=quality,
            )
        )

    lines.extend(["", "## Customer Details", ""])

    for index, result in enumerate(results, start=1):
        lines.extend(
            [
                f"### {index}. {result['customer_name']} (`{result['customer_id']}`)",
                "",
                f"- Snapshot date: `{result['snapshot_date']}`",
                f"- Status: `{'OK' if result['ok'] else 'FAILED'}`",
            ]
        )

        if not result["ok"]:
            lines.extend(["", f"Error: `{result['error']}`", ""])
            continue

        response = result["response"]
        model1 = response.get("model1", {})
        model2 = response.get("model2", {})
        lines.extend(
            [
                "",
                "**Model 1 Output**",
                "",
                f"- Churn probability: `{model1.get('churn_probability')}`",
                f"- Risk score: `{model1.get('risk_score')}`",
                f"- Churn prediction: `{model1.get('churn_prediction')}`",
                f"- Risk level: `{model1.get('risk_level')}`",
                "",
                "Top risk factors:",
                "",
                top_factors_text(model1.get("top_risk_factors")),
                "",
                "**Model 2 Output**",
                "",
                "Why:",
                "",
                format_list(model2.get("why")),
                "",
                "Next actions:",
                "",
                format_list(model2.get("next_actions")),
                "",
            ]
        )

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("\n".join(lines), encoding="utf-8")


def run_test(api_url, limit, output_path, random_seed=None):
    api_url = normalize_api_url(api_url)
    print(f"Using API URL: {api_url}")

    df = pd.read_csv(CUSTOMERS_CSV)
    latest_rows = latest_rows_for_customers(df, limit, random_seed=random_seed)
    try:
        health = get_json(api_url, "/health")
    except Exception as exc:
        health = {"ok": False, "error": str(exc)}
        write_markdown(output_path, api_url, health, [])
        print(f"API health check failed: {exc}")
        print(f"Saved results to {output_path}")
        return
    results = []

    for index, (_, row) in enumerate(latest_rows.iterrows(), start=1):
        payload = build_request_payload(df, row)
        print(f"[{index}/{len(latest_rows)}] Testing {payload['customer_id']} - {payload['customer_name']}")
        started = time.time()
        try:
            response = post_json(
                api_url,
                "/predict/both",
                {
                    "customer": payload["customer"],
                    "extra_context": payload["extra_context"],
                },
            )
            results.append({**payload, "ok": True, "response": response, "seconds": round(time.time() - started, 2)})
        except Exception as exc:
            results.append({**payload, "ok": False, "error": str(exc), "seconds": round(time.time() - started, 2)})

    write_markdown(output_path, api_url, health, results)
    print(f"Saved results to {output_path}")


def main():
    parser = argparse.ArgumentParser(description="Test Colab API with random customers from customers.csv.")
    parser.add_argument("--url", default=API_URL, help="Colab API base URL.")
    parser.add_argument("--limit", type=int, default=CUSTOMER_LIMIT, help="Number of customers to test.")
    parser.add_argument("--output", default=str(OUTPUT_MD), help="Markdown output path.")
    parser.add_argument("--seed", type=int, default=RANDOM_SEED, help="Optional random seed for repeatable tests.")
    args = parser.parse_args()

    run_test(args.url, args.limit, Path(args.output), random_seed=args.seed)


if __name__ == "__main__":
    main()
