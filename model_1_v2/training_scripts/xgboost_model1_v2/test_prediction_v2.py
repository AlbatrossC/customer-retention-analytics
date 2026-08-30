import argparse
import json
from pathlib import Path

import numpy as np
import pandas as pd

from model_v2_runtime import (
    apply_probability_mode,
    load_calibrators,
    load_v2,
    mean_shap_contributions,
    predict_raw_proba,
    prepare_x,
)


SCRIPT_DIR = Path(__file__).resolve().parent
ARTIFACT_DIR = SCRIPT_DIR / "artifacts"
DATA_PATH = SCRIPT_DIR.parents[1] / "data" / "customers_model_1_v2.csv"

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
    "avg_balance_change_3m",
    "avg_transaction_change_3m",
    "avg_card_spend_change_3m",
    "avg_app_login_change_3m",
    "avg_external_transfer_change_3m",
    "max_days_since_last_transaction_3m",
    "sum_complaints_3m",
    "sum_unresolved_complaints_3m",
    "sum_failed_transactions_3m",
    "sum_products_dropped_3m",
    "avg_balance_change_6m",
    "avg_transaction_change_6m",
    "avg_card_spend_change_6m",
    "avg_app_login_change_6m",
    "avg_external_transfer_change_6m",
    "max_days_since_last_transaction_6m",
    "sum_complaints_6m",
    "sum_unresolved_complaints_6m",
    "sum_failed_transactions_6m",
    "sum_products_dropped_6m",
    "balance_change_30d_trend_6m",
    "transaction_change_30d_trend_6m",
    "card_spend_change_30d_trend_6m",
    "app_login_change_30d_trend_6m",
    "days_since_last_transaction_trend_6m",
    "external_transfer_change_30d_trend_6m",
    "complaints_30d_trend_6m",
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


def risk_score(probability):
    probability = min(max(float(probability), 0.0), 1.0)
    if probability < 0.10:
        score = (probability / 0.10) * 30
    elif probability < 0.20:
        score = 30 + ((probability - 0.10) / 0.10) * 40
    else:
        score = 70 + ((probability - 0.20) / 0.80) * 30
    return round(min(max(score, 0.0), 100.0), 2)


def risk_level(probability, risk_bands):
    if probability >= float(risk_bands["medium"]):
        return "High"
    if probability >= float(risk_bands["low"]):
        return "Medium"
    return "Low"


def factor_message(feature, value):
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


def top_risk_factors(models, row, metadata, top_n=5):
    x_row = prepare_x(row, metadata)
    shap_values = mean_shap_contributions(models, x_row)[0]
    factors = []

    for feature, contribution in zip(metadata["features"], shap_values):
        if feature in BLOCKED_EXPLANATION_FEATURES or contribution <= 0:
            continue
        if feature not in ACTIONABLE_FEATURES and not any(
            marker in feature
            for marker in [
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
        ):
            continue
        value = row.iloc[0][feature]
        if pd.isna(value):
            continue
        factors.append(
            {
                "factor": feature,
                "value": value.item() if hasattr(value, "item") else value,
                "message": factor_message(feature, value),
                "contribution": float(contribution),
            }
        )

    factors.sort(key=lambda item: item["contribution"], reverse=True)
    return factors[:top_n]


def predict(row, models, calibrators, metadata):
    raw_probability = float(predict_raw_proba(models, prepare_x(row, metadata))[0])
    probability = float(apply_probability_mode(raw_probability, calibrators, metadata["probability_mode"])[0])
    return {
        "churn_probability": round(probability * 100, 2),
        "raw_churn_probability": round(raw_probability * 100, 2),
        "probability_mode": metadata["probability_mode"],
        "risk_score": risk_score(probability),
        "churn_prediction": "Yes" if probability >= metadata.get("selected_threshold", metadata["threshold"]) else "No",
        "risk_level": risk_level(probability, metadata["risk_bands"]),
        "top_risk_factors": top_risk_factors(models, row, metadata),
    }


def main():
    parser = argparse.ArgumentParser(description="Run one Model 1 v2 sample prediction.")
    parser.add_argument("--data", default=str(DATA_PATH), help="V2 training CSV.")
    parser.add_argument("--customer-id", default=None, help="Optional customer id.")
    args = parser.parse_args()

    metadata = json.loads((ARTIFACT_DIR / "model_metadata_v2.json").read_text(encoding="utf-8"))
    calibrators = load_calibrators(ARTIFACT_DIR)
    models = load_v2(ARTIFACT_DIR, metadata)

    df = pd.read_csv(args.data)
    if args.customer_id:
        df = df[df["customer_id"] == args.customer_id]
        if df.empty:
            raise ValueError(f"No rows found for customer id {args.customer_id}")

    row = df.sort_values(["customer_id", "prediction_date"]).tail(1)
    result = {
        "customer_id": row.iloc[0]["customer_id"],
        "customer_name": row.iloc[0]["customer_name"],
        "prediction_date": row.iloc[0]["prediction_date"],
        "target_month": row.iloc[0]["target_month"],
        "actual_next_month_churn": int(row.iloc[0]["next_month_churn"]),
        "prediction": predict(row, models, calibrators, metadata),
    }
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
