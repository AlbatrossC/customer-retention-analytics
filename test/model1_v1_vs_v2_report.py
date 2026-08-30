import argparse
import json
import sys
from collections import Counter
from datetime import datetime
from pathlib import Path

import joblib
import numpy as np
import pandas as pd
import xgboost as xgb
from sklearn.metrics import accuracy_score, average_precision_score, confusion_matrix, precision_score, recall_score, roc_auc_score
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "model_1_v2" / "training_scripts" / "xgboost_model1_v2"))
from model_v2_runtime import (  # noqa: E402
    apply_probability_mode,
    load_v2,
    mean_shap_contributions,
    predict_raw_proba,
)

V1_DATA = ROOT / "model_1" / "data" / "customers.csv"
V1_ARTIFACTS = ROOT / "model_1" / "training_scripts" / "xgboost_model1" / "artifacts"
V2_DATA = ROOT / "model_1_v2" / "data" / "customers_model_1_v2.csv"
V2_SOURCE_DATA = ROOT / "model_1_v2" / "data" / "customers.csv"
V2_ARTIFACTS = ROOT / "model_1_v2" / "training_scripts" / "xgboost_model1_v2" / "artifacts"
OUTPUT_DIR = ROOT / "logs"
RANDOM_SEED = 42
DEFAULT_LIMIT = 30


def load_model(path):
    model = XGBClassifier()
    model.load_model(path)
    return model


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def prepare_x(df, features, categorical_features, numerical_features=None):
    x_data = df[features].copy()
    for feature in numerical_features or []:
        x_data[feature] = pd.to_numeric(x_data[feature], errors="raise")
    for feature in categorical_features:
        x_data[feature] = x_data[feature].astype("category")
    return x_data


def split_v1_test(df):
    customer_labels = df.groupby("customer_id")["churn_flag"].max().reset_index()
    _, holdout_customers = train_test_split(
        customer_labels,
        train_size=0.70,
        random_state=RANDOM_SEED,
        stratify=customer_labels["churn_flag"],
    )
    _, test_customers = train_test_split(
        holdout_customers,
        train_size=0.50,
        random_state=RANDOM_SEED,
        stratify=holdout_customers["churn_flag"],
    )
    return df[df["customer_id"].isin(set(test_customers["customer_id"]))].copy()


def split_v2_test(df):
    customer_labels = df.groupby("customer_id")["next_month_churn"].max().reset_index()
    _, holdout_customers = train_test_split(
        customer_labels,
        train_size=0.70,
        random_state=RANDOM_SEED,
        stratify=customer_labels["next_month_churn"],
    )
    _, test_customers = train_test_split(
        holdout_customers,
        train_size=0.50,
        random_state=RANDOM_SEED,
        stratify=holdout_customers["next_month_churn"],
    )
    return df[df["customer_id"].isin(set(test_customers["customer_id"]))].copy()


def evaluate(y_true, probabilities, threshold):
    predictions = (probabilities >= threshold).astype(int)
    return {
        "accuracy": float(accuracy_score(y_true, predictions)),
        "precision": float(precision_score(y_true, predictions, zero_division=0)),
        "recall": float(recall_score(y_true, predictions, zero_division=0)),
        "roc_auc": float(roc_auc_score(y_true, probabilities)),
        "pr_auc": float(average_precision_score(y_true, probabilities)),
        "confusion_matrix": confusion_matrix(y_true, predictions).tolist(),
        "flagged_rows": int(predictions.sum()),
        "rows": int(len(y_true)),
        "positive_rows": int(np.sum(y_true)),
    }


def probability_diagnostics(probabilities):
    rounded = np.round(probabilities * 100, 2)
    counts = Counter(rounded)
    return {
        "unique_rounded_percent_values": int(len(counts)),
        "most_common_rounded_percent_values": [
            {"probability_percent": float(value), "count": int(count)}
            for value, count in counts.most_common(5)
        ],
        "percentiles_percent": [
            float(round(value, 4))
            for value in np.percentile(rounded, [0, 10, 25, 50, 75, 90, 95, 99, 100])
        ],
    }


def apply_v2_probability(raw_probability, calibrators, mode):
    return float(apply_probability_mode([raw_probability], calibrators, mode)[0])


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


def clean_value(value):
    if pd.isna(value):
        return None
    if hasattr(value, "item"):
        return value.item()
    return value


def clean_record(record):
    return {key: clean_value(value) for key, value in record.items()}


def v1_top_risk_factors(model, customer_data, row, features, top_n=5):
    dmatrix = xgb.DMatrix(row, enable_categorical=True)
    contributions = model.get_booster().predict(dmatrix, pred_contribs=True)
    shap_values = np.asarray(contributions)[0, :-1]
    positive = [(feature, float(value)) for feature, value in zip(features, shap_values) if value > 0]
    positive.sort(key=lambda item: item[1], reverse=True)
    return [{"factor": feature, "value": clean_value(customer_data[feature])} for feature, _ in positive[:top_n]]


def factor_message(feature, value):
    if value is None:
        return "This signal increased churn risk."
    value_number = None
    try:
        value_number = float(value)
    except (TypeError, ValueError):
        pass
    if "balance" in feature and value_number is not None and value_number < 0:
        return "Balance has been falling across recent months."
    if "transaction" in feature and value_number is not None and value_number < 0:
        return "Transaction activity has been falling across recent months."
    if "card_spend" in feature and value_number is not None and value_number < 0:
        return "Card spending has been falling across recent months."
    if "app_login" in feature and value_number is not None and value_number < 0:
        return "App usage has been falling across recent months."
    if "external_transfer" in feature and value_number is not None and value_number > 0:
        return "External transfers have increased."
    if "complaints" in feature and value_number is not None and value_number > 0:
        return "Customer has recent complaint activity."
    if "failed_transactions" in feature and value_number is not None and value_number > 0:
        return "Customer has recent failed transactions."
    if "days_since_last_transaction" in feature and value_number is not None and value_number > 0:
        return "Customer has gone longer without transacting."
    if "fd_maturing" in feature and value_number is not None and value_number > 0:
        return "Customer has a fixed deposit maturing soon."
    if "emi_bounce" in feature and value_number is not None and value_number > 0:
        return "Customer has a recent EMI bounce."
    return "This signal increased churn risk."


def v2_top_risk_factors(models, row, metadata, top_n=5):
    blocked = set(metadata.get("blocked_columns", []))
    blocked.update(
        {
            "months_observed",
            "tenure_months",
            "customer_segment",
            "income_regularity",
            "products_count",
            "has_credit_card",
            "has_loan",
        }
    )
    actionable = [
        feature
        for feature in metadata["features"]
        if feature not in blocked
    ]
    x_row = prepare_x(row, metadata["features"], metadata["categorical_features"], metadata.get("numerical_features"))
    shap_values = mean_shap_contributions(models, x_row)[0]
    factors = []
    for feature, contribution in zip(metadata["features"], shap_values):
        if feature not in actionable or contribution <= 0:
            continue
        value = clean_value(row.iloc[0][feature])
        factors.append(
            {
                "factor": feature,
                "value": value,
                "message": factor_message(feature, value),
                "contribution": float(contribution),
            }
        )
    factors.sort(key=lambda item: item["contribution"], reverse=True)
    return factors[:top_n]


def predict_v1(model, calibrator, metadata, input_payload):
    row = prepare_x(
        pd.DataFrame([input_payload["customer"]]),
        metadata["features"],
        metadata["categorical_features"],
        metadata.get("numerical_features"),
    )
    raw_probability = float(model.predict_proba(row)[0, 1])
    probability = float(calibrator.predict([raw_probability])[0])
    return {
        "churn_probability": round(probability * 100, 2),
        "raw_churn_probability": round(raw_probability * 100, 2),
        "risk_score": risk_score(probability),
        "churn_prediction": "Yes" if probability >= metadata.get("selected_threshold", metadata["threshold"]) else "No",
        "risk_level": risk_level(probability, metadata["risk_bands"]),
        "top_risk_factors": v1_top_risk_factors(model, input_payload["customer"], row, metadata["features"]),
    }


def predict_v2(models, calibrators, metadata, v2_row):
    row = pd.DataFrame([v2_row])
    raw_probability = float(
        predict_raw_proba(
            models,
            prepare_x(row, metadata["features"], metadata["categorical_features"], metadata.get("numerical_features")),
        )[0]
    )
    probability = apply_v2_probability(raw_probability, calibrators, metadata["probability_mode"])
    return {
        "churn_probability": round(probability * 100, 2),
        "raw_churn_probability": round(raw_probability * 100, 2),
        "probability_mode": metadata["probability_mode"],
        "risk_score": risk_score(probability),
        "churn_prediction": "Yes" if probability >= metadata["threshold"] else "No",
        "risk_level": risk_level(probability, metadata["risk_bands"]),
        "top_risk_factors": v2_top_risk_factors(models, row, metadata),
    }


def latest_v1_input(v1_df, customer_id, features, prediction_date, next_month_churn):
    """Model 1's input for the SAME month v2 predicts from.

    Taking the customer's last snapshot instead would hand Model 1 the churn
    month itself: churn is absorbing in this dataset, so a churned customer's
    final row IS the month they left, and its features already show the
    collapse. Scored that way Model 1 is not predicting anything, and the two
    models cannot be put in one table. Anchoring both to v2's prediction_date
    gives them the same information and the same question.
    """
    customer_rows = (
        v1_df[v1_df["customer_id"] == customer_id]
        .assign(snapshot_date=lambda data: pd.to_datetime(data["snapshot_date"]))
        .sort_values("snapshot_date")
    )
    aligned = customer_rows[customer_rows["snapshot_date"] == pd.to_datetime(prediction_date)]
    row = (aligned if not aligned.empty else customer_rows.tail(1)).iloc[0]
    clean = clean_record(row.to_dict())
    return {
        "customer_id": clean["customer_id"],
        "customer_name": clean["customer_name"],
        "snapshot_date": str(pd.to_datetime(clean["snapshot_date"]).date()),
        "customer": {feature: clean[feature] for feature in features},
        "actual_next_month_churn": int(next_month_churn),
    }


def v2_raw_input(v2_source_df, v2_row):
    history = (
        v2_source_df[
            (v2_source_df["customer_id"] == v2_row["customer_id"])
            & (pd.to_datetime(v2_source_df["snapshot_date"]) <= pd.to_datetime(v2_row["prediction_date"]))
        ]
        .assign(snapshot_date=lambda data: pd.to_datetime(data["snapshot_date"]))
        .sort_values("snapshot_date")
        .tail(6)
    )
    profile_source = history.iloc[-1]
    history_fields = [
        "snapshot_date",
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
    monthly_history = []
    for record in history[history_fields].to_dict(orient="records"):
        clean = clean_record(record)
        clean["snapshot_date"] = str(pd.to_datetime(clean["snapshot_date"]).date())
        monthly_history.append(clean)
    return {
        "customer_id": v2_row["customer_id"],
        "customer_name": v2_row["customer_name"],
        "prediction_date": v2_row["prediction_date"],
        "target_month": v2_row["target_month"],
        "profile": {
            "tenure_months": clean_value(profile_source["tenure_months"]),
            "customer_segment": clean_value(profile_source["customer_segment"]),
            "income_regularity": clean_value(profile_source["income_regularity"]),
            "products_count": clean_value(profile_source["products_count"]),
            "has_credit_card": clean_value(profile_source["has_credit_card"]),
            "has_loan": clean_value(profile_source["has_loan"]),
        },
        "monthly_history": monthly_history,
        "actual_next_month_churn": int(v2_row["next_month_churn"]),
    }


def metrics_for_models(v1_df, v2_df, v1_model, v1_calibrator, v1_metadata, v2_models, v2_calibrators, v2_metadata):
    v1_test = split_v1_test(v1_df)
    v1_x = prepare_x(
        v1_test,
        v1_metadata["features"],
        v1_metadata["categorical_features"],
        v1_metadata.get("numerical_features"),
    )
    v1_raw = v1_model.predict_proba(v1_x)[:, 1]
    v1_probs = v1_calibrator.predict(v1_raw)

    v2_test = split_v2_test(v2_df)
    v2_x = prepare_x(
        v2_test,
        v2_metadata["features"],
        v2_metadata["categorical_features"],
        v2_metadata.get("numerical_features"),
    )
    v2_raw = predict_raw_proba(v2_models, v2_x)
    v2_probs = np.array([apply_v2_probability(prob, v2_calibrators, v2_metadata["probability_mode"]) for prob in v2_raw])

    # Apples-to-apples: score Model 1 on the same rows and the same label as v2,
    # by joining v1's snapshot for each of v2's prediction months. Model 1's own
    # metrics below answer an easier question and are not comparable to these.
    aligned = v2_test[["customer_id", "prediction_date", "next_month_churn"]].merge(
        v1_df.rename(columns={"snapshot_date": "prediction_date"}),
        on=["customer_id", "prediction_date"],
        how="inner",
    )
    aligned_x = prepare_x(
        aligned,
        v1_metadata["features"],
        v1_metadata["categorical_features"],
        v1_metadata.get("numerical_features"),
    )
    aligned_probs = v1_calibrator.predict(v1_model.predict_proba(aligned_x)[:, 1])

    return {
        "model_1_same_task_next_month": {
            "question": "Is this customer likely to churn next month? (Model 1, same rows and label as v2)",
            "metrics": evaluate(aligned["next_month_churn"], aligned_probs, v1_metadata["threshold"]),
            "probability_diagnostics": probability_diagnostics(aligned_probs),
        },
        "model_1_v2_next_month": {
            "question": "Is this customer likely to churn next month?",
            "metrics": evaluate(v2_test["next_month_churn"], v2_probs, v2_metadata.get("selected_threshold", v2_metadata["threshold"])),
            "probability_diagnostics": probability_diagnostics(v2_probs),
        },
        "model_1_own_task_current_month": {
            "question": "Is this customer churning in this snapshot? (Model 1's original task, NOT comparable)",
            "metrics": evaluate(v1_test["churn_flag"], v1_probs, v1_metadata["threshold"]),
            "probability_diagnostics": probability_diagnostics(v1_probs),
        },
    }


def markdown_json(value):
    return "```json\n" + json.dumps(value, indent=2, ensure_ascii=False) + "\n```"


def write_report(output_path, metrics, results):
    lines = [
        "# Model 1 vs Model 1 v2 Report",
        "",
        f"- Created at: `{datetime.now().isoformat(timespec='seconds')}`",
        f"- Customers tested: `{len(results)}`",
        "",
        "## Important Note",
        "",
        "Churn is absorbing in this dataset: a churned customer's panel stops at the month",
        "they leave, so `churn_flag = 1` is always their final row. Model 1's original task -",
        "\"is this customer churning in this snapshot?\" - therefore scores it on a row whose",
        "features already show the collapse. That is detection after the fact, not prediction,",
        "and it leaves no time to run a retention action.",
        "",
        "The first two metric blocks below put both models on the same footing: same rows,",
        "same month of input, same next-month label. The third block is Model 1's original",
        "task, kept for reference only. Its higher numbers come from the easier question,",
        "not from a better model - do not compare them across blocks.",
        "",
        "## Metrics",
        "",
    ]

    for model_name, payload in metrics.items():
        model_metrics = payload["metrics"]
        diagnostics = payload["probability_diagnostics"]
        lines.extend(
            [
                f"### {model_name}",
                "",
                f"- Question: {payload['question']}",
                f"- Accuracy: `{model_metrics['accuracy']:.4f}`",
                f"- Precision: `{model_metrics['precision']:.4f}`",
                f"- Recall: `{model_metrics['recall']:.4f}`",
                f"- ROC-AUC: `{model_metrics['roc_auc']:.4f}`",
                f"- PR-AUC: `{model_metrics['pr_auc']:.4f}`",
                f"- Flagged rows: `{model_metrics['flagged_rows']}`",
                f"- Rows evaluated: `{model_metrics['rows']}`",
                f"- Positive rows: `{model_metrics['positive_rows']}`",
                f"- Confusion matrix: `{model_metrics['confusion_matrix']}`",
                f"- Unique rounded probability values: `{diagnostics['unique_rounded_percent_values']}`",
                f"- Most common probabilities: `{diagnostics['most_common_rounded_percent_values']}`",
                f"- Probability percentiles: `{diagnostics['percentiles_percent']}`",
                "",
            ]
        )

    lines.extend(
        [
            "## 30 Customer Test",
            "",
            "Both models score the same month and are graded on the same label: did this",
            "customer churn in the following month?",
            "",
            "| # | Customer | Prediction Month | Model 1 Risk | Model 1 v2 Risk | Actual Next Month |",
            "|---:|---|---|---:|---:|---:|",
        ]
    )
    for index, result in enumerate(results, start=1):
        lines.append(
            f"| {index} | {result['customer_name']} (`{result['customer_id']}`) | "
            f"{result['model_1_input']['snapshot_date']} | "
            f"{result['model_1_output']['churn_probability']}% | "
            f"{result['model_1_v2_output']['churn_probability']}% | "
            f"{result['model_1_v2_input']['actual_next_month_churn']} |"
        )

    lines.extend(["", "## Customer Details", ""])
    for index, result in enumerate(results, start=1):
        lines.extend(
            [
                f"### {index}. {result['customer_name']} (`{result['customer_id']}`)",
                "",
                "#### Model 1 Input",
                "",
                markdown_json(result["model_1_input"]),
                "",
                "#### Model 1 Output",
                "",
                markdown_json(result["model_1_output"]),
                "",
                "#### Model 1 v2 Input",
                "",
                markdown_json(result["model_1_v2_input"]),
                "",
                "#### Model 1 v2 Output",
                "",
                markdown_json(result["model_1_v2_output"]),
                "",
            ]
        )

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text("\n".join(lines), encoding="utf-8")


def main():
    parser = argparse.ArgumentParser(description="Compare old Model 1 and Model 1 v2.")
    parser.add_argument("--limit", type=int, default=DEFAULT_LIMIT, help="Number of customers to test.")
    parser.add_argument("--seed", type=int, default=RANDOM_SEED, help="Random seed.")
    parser.add_argument("--output", default=None, help="Markdown output path.")
    args = parser.parse_args()

    v1_metadata = read_json(V1_ARTIFACTS / "model_metadata.json")
    v2_metadata = read_json(V2_ARTIFACTS / "model_metadata_v2.json")
    v1_model = load_model(V1_ARTIFACTS / "xgboost_model.json")
    v2_models = load_v2(V2_ARTIFACTS, v2_metadata)
    v1_calibrator = joblib.load(V1_ARTIFACTS / "isotonic_calibrator.joblib")
    v2_calibrators = joblib.load(V2_ARTIFACTS / "calibrator_v2.joblib")

    v1_df = pd.read_csv(V1_DATA)
    v2_df = pd.read_csv(V2_DATA)
    v2_source_df = pd.read_csv(V2_SOURCE_DATA)

    print("Calculating metrics for both models...", flush=True)
    metrics = metrics_for_models(v1_df, v2_df, v1_model, v1_calibrator, v1_metadata, v2_models, v2_calibrators, v2_metadata)

    print(f"Testing {args.limit} customers...", flush=True)
    sample_rows = (
        v2_df.sort_values(["customer_id", "prediction_date"])
        .groupby("customer_id", as_index=False)
        .tail(1)
        .sample(n=min(args.limit, v2_df["customer_id"].nunique()), random_state=args.seed)
        .sort_values("customer_id")
    )

    results = []
    for index, v2_row in enumerate(sample_rows.to_dict(orient="records"), start=1):
        customer_id = v2_row["customer_id"]
        print(f"[{index}/{len(sample_rows)}] {customer_id}", flush=True)
        v1_input = latest_v1_input(
            v1_df,
            customer_id,
            v1_metadata["features"],
            v2_row["prediction_date"],
            v2_row["next_month_churn"],
        )
        v2_input = v2_raw_input(v2_source_df, v2_row)
        results.append(
            {
                "customer_id": customer_id,
                "customer_name": v2_row["customer_name"],
                "model_1_input": v1_input,
                "model_1_output": predict_v1(v1_model, v1_calibrator, v1_metadata, v1_input),
                "model_1_v2_input": v2_input,
                "model_1_v2_output": predict_v2(v2_models, v2_calibrators, v2_metadata, v2_row),
            }
        )

    output_path = Path(args.output) if args.output else OUTPUT_DIR / f"model1_vs_model1_v2_{datetime.now().strftime('%I-%M_%p').lower()}.md"
    write_report(output_path, metrics, results)
    print(f"Saved report to {output_path}")


if __name__ == "__main__":
    main()
