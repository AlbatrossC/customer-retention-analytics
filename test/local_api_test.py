import argparse
import json
import math
import time
from datetime import datetime
from pathlib import Path
from urllib import error, request

import pandas as pd


API_URL = "http://127.0.0.1:8000"
CUSTOMERS_CSV = Path("model_1_v2/data/customers.csv")
LOG_DIR = Path("logs")
CUSTOMER_LIMIT = 10
REQUEST_TIMEOUT_SECONDS = 240
MAX_ERROR_CHARS = 800

MODEL1_V2_PROFILE_FEATURES = [
    "tenure_months",
    "customer_segment",
    "income_regularity",
    "products_count",
    "has_credit_card",
    "has_loan",
]

MODEL1_V2_BEHAVIOR_FEATURES = [
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
    text = " ".join(text.split())
    return text[:MAX_ERROR_CHARS]


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


def build_customer_request(df, row):
    row = clean_record(row.to_dict())
    latest_date = pd.to_datetime(row["snapshot_date"])
    history = history_for_customer(df, row["customer_id"], latest_date)

    profile = {feature: row[feature] for feature in MODEL1_V2_PROFILE_FEATURES}
    customer = {feature: row[feature] for feature in MODEL1_V2_PROFILE_FEATURES + MODEL1_V2_BEHAVIOR_FEATURES}
    monthly_history = [
        clean_record(record)
        for record in history[["snapshot_date", *MODEL1_V2_BEHAVIOR_FEATURES]]
        .assign(snapshot_date=history["snapshot_date"].dt.date.astype(str))
        .to_dict(orient="records")
    ]
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
        "prediction_date": str(latest_date.date()),
        "snapshot_date": str(latest_date.date()),
        "target_month": str((latest_date + pd.DateOffset(months=1)).date()),
        "profile": profile,
        "monthly_history": monthly_history,
        "customer": customer,
        "extra_context": extra_context,
    }


def signal_message(field, value):
    if value is None:
        return None
    if field == "balance_change_30d":
        return percent_message("Balance", value)
    if field == "transaction_change_30d":
        return percent_message("Transactions", value)
    if field == "card_spend_change_30d":
        return percent_message("Card spend", value)
    if field == "app_login_change_30d":
        return percent_message("App logins", value)
    if field == "external_transfer_change_30d":
        return percent_message("External transfers", value)
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


def percent_message(label, value):
    value = float(value)
    direction = "fell" if value < 0 else "rose"
    return f"{label} {direction} by {abs(value):.2f}% in the last 30 days."


def count_message(single, plural, value):
    count = int(float(value))
    label = single if count == 1 else plural
    return f"Customer had {count} {label}."


def is_risky_signal(field, value):
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


def build_main_signals(model1_output, customer):
    signals = []
    used = set()
    ignored_fields = {"age", "branch_code", "card_colour", "customer_segment"}
    for item in model1_output.get("top_risk_factors", []):
        field = item.get("factor")
        value = item.get("value")
        if field in ignored_fields or not is_risky_signal(field, value):
            if not item.get("message"):
                continue
            message = item["message"]
        else:
            message = signal_message(field, value)
        if not message and item.get("message"):
            message = item["message"]
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
        if field in used or field not in customer or not is_risky_signal(field, customer.get(field)):
            continue
        message = signal_message(field, customer.get(field))
        if message:
            signals.append({"field": field, "value": customer.get(field), "message": message})
            used.add(field)

    if not signals and model1_output.get("churn_probability") is not None:
        signals.append(
            {
                "field": "model1_risk_level",
                "value": model1_output["churn_probability"],
                "message": f"Model 1 shows low churn risk at {float(model1_output['churn_probability']):.2f}%.",
            }
        )
    return signals[:5]


def trend_summary(trend):
    messages = []
    overall_direction = trend.get("overall_direction", "unknown")
    if overall_direction != "unknown":
        messages.append(f"Overall recent direction is {overall_direction}.")
    for field in ["balance_change_30d", "days_since_last_transaction", "complaints_30d", "external_transfer_change_30d"]:
        values = trend.get(field)
        if not isinstance(values, list) or not values:
            continue
        latest = values[-1]
        if is_risky_signal(field, latest):
            message = signal_message(field, latest)
            if message:
                messages.append(message)
    return {"overall_direction": overall_direction, "messages": messages[:5]}


def suggested_actions_for(customer, risk_level, complaint_text):
    actions = []
    if risk_level == "Low":
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


def build_model2_payload(customer_request, model1_output):
    customer = customer_request["customer"]
    extra_context = customer_request["extra_context"]
    profile = extra_context.get("customer_profile", {})
    complaint_text = extra_context.get("recent_complaint_text")
    risk_level = model1_output.get("risk_level", "Unknown")
    return {
        "task": "identify_retention_risk_and_actions",
        "customer_identity": {
            "customer_id": customer_request["customer_id"],
            "customer_name": customer_request["customer_name"],
            "snapshot_date": customer_request["snapshot_date"],
        },
        "risk": {
            "churn_probability_percent": model1_output.get("churn_probability"),
            "risk_score": model1_output.get("risk_score"),
            "churn_prediction": model1_output.get("churn_prediction"),
            "risk_level": risk_level,
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
        "suggested_actions": suggested_actions_for(customer, risk_level, complaint_text),
    }


def default_output_path():
    # Windows filenames cannot contain ":", so use HH-MM AM/PM.
    return LOG_DIR / f"{datetime.now().strftime('%I-%M %p').lower()}.md"


def fenced_json(value):
    return "```json\n" + json.dumps(value, indent=2, ensure_ascii=False) + "\n```"


def format_list(items):
    if not items:
        return "- None"
    return "\n".join(f"- {item}" for item in items)


def write_markdown(output_path, api_url, health, results):
    lines = [
        "# Local API Test Results",
        "",
        f"- API URL: `{api_url}`",
        f"- Created at: `{datetime.now().isoformat(timespec='seconds')}`",
        f"- Customers tested: `{len(results)}`",
        f"- Source CSV: `{CUSTOMERS_CSV}`",
        f"- Health: `{json.dumps(health, ensure_ascii=False)}`",
        "",
        "## Summary",
        "",
        "| # | Customer | Model 1 v2 Risk | Prediction | Model 2 | Seconds |",
        "|---:|---|---:|---|---|---:|",
    ]

    for index, result in enumerate(results, start=1):
        model1_output = result.get("model1_output") or {}
        lines.append(
            "| {index} | {name} (`{customer_id}`) | {risk} | {prediction} | {model2_status} | {seconds} |".format(
                index=index,
                name=result["customer_name"],
                customer_id=result["customer_id"],
                risk=model1_output.get("churn_probability", "NA"),
                prediction=model1_output.get("churn_prediction", "NA"),
                model2_status="OK" if result.get("model2_ok") else "FAILED",
                seconds=result.get("seconds", "NA"),
            )
        )

    lines.extend(["", "## Customer Details", ""])
    for index, result in enumerate(results, start=1):
        lines.extend(
            [
                f"### {index}. {result['customer_name']} (`{result['customer_id']}`)",
                "",
                f"- Snapshot date: `{result['snapshot_date']}`",
                f"- Model 1 v2 status: `{'OK' if result.get('model1_ok') else 'FAILED'}`",
                f"- Model 2 status: `{'OK' if result.get('model2_ok') else 'FAILED'}`",
                "",
                "#### Model 1 v2 Input",
                "",
                fenced_json(result["model1_input"]),
                "",
                "#### Model 1 v2 Output",
                "",
                fenced_json(result.get("model1_output") or {"error": result.get("model1_error")}),
            ]
        )

        if result.get("model2_input") is not None:
            lines.extend(["", "#### Model 2 Input", "", fenced_json(result["model2_input"])])
        if result.get("model2_output") is not None:
            model2_output = result["model2_output"]
            lines.extend(
                [
                    "",
                    "#### Model 2 Output",
                    "",
                    "Why:",
                    "",
                    format_list(model2_output.get("why")),
                    "",
                    "Next actions:",
                    "",
                    format_list(model2_output.get("next_actions")),
                    "",
                    fenced_json(model2_output),
                ]
            )
        elif result.get("model2_error"):
            lines.extend(["", "#### Model 2 Output", "", f"`{result['model2_error']}`"])
        lines.append("")

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("\n".join(lines), encoding="utf-8")


def run_test(api_url, limit, output_path, random_seed=None):
    api_url = normalize_api_url(api_url)
    print(f"Using API URL: {api_url}")
    print(f"Customer limit: {limit}")

    df = pd.read_csv(CUSTOMERS_CSV)
    latest_rows = latest_rows_for_customers(df, limit, random_seed=random_seed)
    health = get_json(api_url, "/health")
    results = []

    for index, (_, row) in enumerate(latest_rows.iterrows(), start=1):
        customer_request = build_customer_request(df, row)
        print(f"[{index}/{len(latest_rows)}] {customer_request['customer_id']} - {customer_request['customer_name']}")
        started = time.time()
        result = {
            **customer_request,
            "model1_input": {
                "profile": customer_request["profile"],
                "monthly_history": customer_request["monthly_history"],
                "customer_id": customer_request["customer_id"],
                "customer_name": customer_request["customer_name"],
                "prediction_date": customer_request["prediction_date"],
                "snapshot_date": customer_request["snapshot_date"],
                "target_month": customer_request["target_month"],
            },
        }

        try:
            model1_response = post_json(api_url, "/predict/model1", result["model1_input"])
            model1_output = model1_response["model1"]
            result.update({"model1_ok": True, "model1_output": model1_output})
        except Exception as exc:
            result.update(
                {
                    "model1_ok": False,
                    "model1_error": str(exc),
                    "model2_ok": False,
                    "model2_error": "Skipped because Model 1 failed.",
                    "seconds": round(time.time() - started, 2),
                }
            )
            results.append(result)
            continue

        model2_input = build_model2_payload(customer_request, result["model1_output"])
        result["model2_input"] = model2_input
        try:
            model2_response = post_json(
                api_url,
                "/predict/model2",
                {
                    "payload": model2_input,
                    "customer_id": customer_request["customer_id"],
                    "customer_name": customer_request["customer_name"],
                    "snapshot_date": customer_request["snapshot_date"],
                },
            )
            result.update({"model2_ok": True, "model2_output": model2_response["model2"]})
        except Exception as exc:
            result.update({"model2_ok": False, "model2_error": str(exc)})

        result["seconds"] = round(time.time() - started, 2)
        results.append(result)

    write_markdown(output_path, api_url, health, results)
    print(f"Saved results to {output_path}")


def main():
    parser = argparse.ArgumentParser(description="Test local retention API with customers from customers.csv.")
    parser.add_argument("--url", default=API_URL, help="Local API base URL.")
    parser.add_argument("--limit", type=int, default=CUSTOMER_LIMIT, help="Number of customers to test. Default: 10.")
    parser.add_argument("--output", default=None, help="Markdown output path. Default: logs/HH-MM am.md.")
    parser.add_argument("--seed", type=int, default=None, help="Optional random seed for repeatable customer selection.")
    args = parser.parse_args()

    output_path = Path(args.output) if args.output else default_output_path()
    run_test(args.url, args.limit, output_path, random_seed=args.seed)


if __name__ == "__main__":
    main()
