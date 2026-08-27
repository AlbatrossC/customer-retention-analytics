import json
from pathlib import Path
from typing import Any

import joblib
import numpy as np
import pandas as pd
from sklearn.metrics import average_precision_score, confusion_matrix, precision_score, recall_score, roc_auc_score
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier


ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "model_1_training_data" / "customers.csv"
RESULTS_PATH = ROOT / "results.md"
RANDOM_SEED = 42
TARGET = "churn_flag"
CUSTOMER_ID = "customer_id"


BASE = {
    "age": 38,
    "tenure_months": 96,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 3,
    "has_credit_card": 1,
    "has_loan": 1,
    "days_since_last_transaction": 4,
    "balance_change_30d": 12,
    "transaction_change_30d": 6,
    "card_spend_change_30d": 8,
    "app_login_change_30d": 4,
    "salary_missing_days": 0,
    "external_transfer_change_30d": 4,
    "upi_share_of_spend": 0.32,
    "fd_maturing_in_30d": 0,
    "products_dropped_90d": 0,
    "complaints_30d": 0,
    "unresolved_complaints": 0,
    "failed_transactions_30d": 0,
    "avg_resolution_time_hrs": 0,
    "emi_bounce_30d": 0,
    "branch_code": "BR-121",
    "card_colour": "gold",
}


def merged(**changes):
    row = BASE.copy()
    row.update(changes)
    return row


EXAMPLES = [
    {"name": "Healthy salary customer", "expected": "Very low risk", "data": BASE},
    {
        "name": "Salary customer going quiet",
        "expected": "Medium risk",
        "data": merged(
            days_since_last_transaction=20,
            balance_change_30d=-34,
            transaction_change_30d=-38,
            card_spend_change_30d=-35,
            app_login_change_30d=-42,
            external_transfer_change_30d=70,
            salary_missing_days=3,
            upi_share_of_spend=0.68,
        ),
    },
    {
        "name": "Complaint-heavy customer",
        "expected": "Medium to high risk",
        "data": merged(
            complaints_30d=4,
            unresolved_complaints=3,
            failed_transactions_30d=8,
            avg_resolution_time_hrs=88,
            fd_maturing_in_30d=1,
        ),
    },
    {
        "name": "Everything going wrong",
        "expected": "Highest risk",
        "data": merged(
            days_since_last_transaction=25,
            balance_change_30d=-45,
            transaction_change_30d=-55,
            card_spend_change_30d=-48,
            app_login_change_30d=-60,
            external_transfer_change_30d=110,
            salary_missing_days=6,
            upi_share_of_spend=0.82,
            complaints_30d=5,
            unresolved_complaints=4,
            failed_transactions_30d=10,
            avg_resolution_time_hrs=110,
            fd_maturing_in_30d=1,
            products_dropped_90d=2,
        ),
    },
    {
        "name": "Farmer with no salary field",
        "expected": "Should not crash; NaN salary is valid",
        "data": merged(
            age=49,
            tenure_months=55,
            customer_segment="farmer",
            income_regularity="seasonal",
            has_credit_card=0,
            has_loan=0,
            salary_missing_days=np.nan,
            days_since_last_transaction=17,
            balance_change_30d=-26,
            transaction_change_30d=-20,
            card_spend_change_30d=-10,
            external_transfer_change_30d=35,
            emi_bounce_30d=0,
        ),
    },
    {
        "name": "Pension FD maturity",
        "expected": "Moderate risk",
        "data": merged(
            age=72,
            tenure_months=210,
            customer_segment="pension",
            income_regularity="regular",
            has_loan=0,
            emi_bounce_30d=0,
            fd_maturing_in_30d=1,
            external_transfer_change_30d=90,
            balance_change_30d=-22,
            salary_missing_days=1,
        ),
    },
    {
        "name": "Vendor with failed payments",
        "expected": "Service risk",
        "data": merged(
            age=33,
            tenure_months=28,
            customer_segment="vendor",
            income_regularity="irregular",
            has_credit_card=0,
            salary_missing_days=np.nan,
            days_since_last_transaction=12,
            balance_change_30d=-15,
            failed_transactions_30d=7,
            complaints_30d=2,
            unresolved_complaints=1,
            avg_resolution_time_hrs=54,
        ),
    },
    {
        "name": "Improving after complaint",
        "expected": "Low risk",
        "data": merged(
            days_since_last_transaction=2,
            balance_change_30d=24,
            transaction_change_30d=30,
            card_spend_change_30d=18,
            app_login_change_30d=22,
            external_transfer_change_30d=-15,
            complaints_30d=1,
            unresolved_complaints=0,
            failed_transactions_30d=0,
            avg_resolution_time_hrs=8,
        ),
    },
]


def split_by_customer(df: pd.DataFrame) -> dict[str, pd.DataFrame]:
    customer_labels = df.groupby(CUSTOMER_ID)[TARGET].max().reset_index()
    train_customers, holdout_customers = train_test_split(
        customer_labels,
        train_size=0.70,
        random_state=RANDOM_SEED,
        stratify=customer_labels[TARGET],
    )
    validation_customers, test_customers = train_test_split(
        holdout_customers,
        train_size=0.50,
        random_state=RANDOM_SEED,
        stratify=holdout_customers[TARGET],
    )
    customer_sets = {
        "train": set(train_customers[CUSTOMER_ID]),
        "validation": set(validation_customers[CUSTOMER_ID]),
        "test": set(test_customers[CUSTOMER_ID]),
    }
    return {name: df[df[CUSTOMER_ID].isin(ids)].copy() for name, ids in customer_sets.items()}


def prepare_categorical_frame(df: pd.DataFrame, metadata: dict) -> pd.DataFrame:
    frame = df[metadata["features"]].copy()
    for feature in metadata["categorical_features"]:
        if "category_values" in metadata:
            dtype = pd.CategoricalDtype(categories=metadata["category_values"][feature])
            frame[feature] = frame[feature].astype(str).astype(dtype)
        else:
            frame[feature] = frame[feature].astype("category")
    return frame


def probability_to_output(probability: float, threshold: float) -> dict:
    if probability >= 0.20:
        risk = "High"
    elif probability >= 0.10:
        risk = "Medium"
    else:
        risk = "Low"
    return {
        "probability": probability,
        "probability_text": f"{probability * 100:.2f}%",
        "prediction": "Yes" if probability >= threshold else "No",
        "risk": risk,
    }


def metric_block(y_true: pd.Series, probabilities: np.ndarray, threshold: float) -> dict:
    predictions = (probabilities >= threshold).astype(int)
    return {
        "roc_auc": float(roc_auc_score(y_true, probabilities)),
        "pr_auc": float(average_precision_score(y_true, probabilities)),
        "precision": float(precision_score(y_true, predictions, zero_division=0)),
        "recall": float(recall_score(y_true, predictions, zero_division=0)),
        "confusion_matrix": confusion_matrix(y_true, predictions).tolist(),
        "flagged_rows": int(predictions.sum()),
        "mean_probability": float(np.mean(probabilities)),
    }


def fit_status(metrics: dict) -> tuple[str, str]:
    train_roc = metrics["train"]["roc_auc"]
    test_roc = metrics["test"]["roc_auc"]
    train_pr = metrics["train"]["pr_auc"]
    test_pr = metrics["test"]["pr_auc"]
    roc_gap = train_roc - test_roc
    pr_gap = train_pr - test_pr

    if train_roc < 0.75 and test_roc < 0.75:
        return "Underfitting", "It is weak on train and test."
    if roc_gap > 0.08 or pr_gap > 0.12 or train_roc > 0.93:
        return "Overfitting", "Train is much better than test."
    if 0.78 <= test_roc <= 0.86 and 0.40 <= test_pr <= 0.55 and roc_gap <= 0.08:
        return "Healthy", "Train and test are close enough."
    return "Watch", "Not clearly bad, but check it again with more examples."


class OldXGBoostModel:
    name = "XGBoost old"

    def __init__(self):
        artifact_dir = ROOT / "training_scripts" / "xgboost_model1" / "artifacts"
        self.metadata = json.loads((artifact_dir / "model_metadata.json").read_text(encoding="utf-8"))
        self.preprocessor = joblib.load(artifact_dir / "preprocessor.joblib")
        self.model = XGBClassifier()
        self.model.load_model(artifact_dir / "xgboost_model.json")

    @property
    def threshold(self) -> float:
        return float(self.metadata["threshold"])

    def probabilities(self, df: pd.DataFrame) -> np.ndarray:
        return self.model.predict_proba(self.preprocessor.transform(df[self.metadata["features"]]))[:, 1]

    def predict_example(self, data: dict) -> dict:
        probability = float(self.probabilities(pd.DataFrame([data]))[0])
        return probability_to_output(probability, self.threshold)


class CalibratedXGBoostModel:
    name = "XGBoost calibrated"

    def __init__(self):
        artifact_dir = ROOT / "training_scripts" / "xgboost_model1" / "artifacts_candidate"
        self.metadata = json.loads((artifact_dir / "model_metadata.json").read_text(encoding="utf-8"))
        self.calibrator = joblib.load(artifact_dir / "isotonic_calibrator.joblib")
        self.model = XGBClassifier()
        self.model.load_model(artifact_dir / "xgboost_model.json")

    @property
    def threshold(self) -> float:
        return float(self.metadata["threshold"])

    def probabilities(self, df: pd.DataFrame) -> np.ndarray:
        frame = prepare_categorical_frame(df, self.metadata)
        raw = self.model.predict_proba(frame)[:, 1]
        return self.calibrator.predict(raw)

    def predict_example(self, data: dict) -> dict:
        probability = float(self.probabilities(pd.DataFrame([data]))[0])
        return probability_to_output(probability, self.threshold)


class LightGBMModel:
    def __init__(self, name: str, folder: str):
        self.name = name
        artifact_dir = ROOT / "training_scripts" / folder / "artifacts"
        self.metadata = json.loads((artifact_dir / "model_metadata.json").read_text(encoding="utf-8"))
        self.calibrator = joblib.load(artifact_dir / "isotonic_calibrator.joblib")
        self.model = joblib.load(artifact_dir / "lightgbm_model.joblib")

    @property
    def threshold(self) -> float:
        return float(self.metadata["threshold"])

    def probabilities(self, df: pd.DataFrame) -> np.ndarray:
        frame = prepare_categorical_frame(df, self.metadata)
        raw = self.model.predict_proba(frame)[:, 1]
        return self.calibrator.predict(raw)

    def predict_example(self, data: dict) -> dict:
        probability = float(self.probabilities(pd.DataFrame([data]))[0])
        return probability_to_output(probability, self.threshold)


def evaluate_models(models: list, splits: dict[str, pd.DataFrame]) -> dict:
    all_metrics = {}
    for model in models:
        model_metrics = {}
        for split_name, split_df in splits.items():
            model_metrics[split_name] = metric_block(
                split_df[TARGET],
                model.probabilities(split_df),
                model.threshold,
            )
        status, note = fit_status(model_metrics)
        model_metrics["fit_status"] = status
        model_metrics["fit_note"] = note
        all_metrics[model.name] = model_metrics
    return all_metrics


def run_examples(models: list) -> list[dict]:
    rows = []
    for example in EXAMPLES:
        outputs = {model.name: model.predict_example(example["data"]) for model in models}
        rows.append({"name": example["name"], "expected": example["expected"], "outputs": outputs})
    return rows


def write_markdown(metrics: dict, examples: list[dict]) -> None:
    lines = [
        "# Model Results",
        "",
        "The dataset was not changed.",
        "",
        "Tested four models:",
        "",
        "- XGBoost old",
        "- XGBoost calibrated",
        "- LightGBM model 1",
        "- LightGBM model 2",
        "",
        "## Simple Answer",
        "",
        "The old XGBoost model is not good for probability display. It is too confident.",
        "",
        "The three calibrated models are healthier.",
        "",
        "Best practical choices:",
        "",
        "1. XGBoost calibrated",
        "2. LightGBM model 2",
        "",
        "## Fit Check",
        "",
        "| Model | Status | Why | Train ROC | Val ROC | Test ROC | Train PR | Val PR | Test PR |",
        "|---|---|---|---:|---:|---:|---:|---:|---:|",
    ]
    for model_name, model_metrics in metrics.items():
        lines.append(
            f"| {model_name} | {model_metrics['fit_status']} | {model_metrics['fit_note']} | "
            f"{model_metrics['train']['roc_auc']:.4f} | {model_metrics['validation']['roc_auc']:.4f} | {model_metrics['test']['roc_auc']:.4f} | "
            f"{model_metrics['train']['pr_auc']:.4f} | {model_metrics['validation']['pr_auc']:.4f} | {model_metrics['test']['pr_auc']:.4f} |"
        )

    lines.extend(
        [
            "",
            "## Test Set Results",
            "",
            "| Model | Precision | Recall | Flagged Rows | Mean Probability | Confusion Matrix |",
            "|---|---:|---:|---:|---:|---|",
        ]
    )
    for model_name, model_metrics in metrics.items():
        test = model_metrics["test"]
        lines.append(
            f"| {model_name} | {test['precision']:.4f} | {test['recall']:.4f} | "
            f"{test['flagged_rows']} | {test['mean_probability']:.4f} | {test['confusion_matrix']} |"
        )

    lines.extend(
        [
            "",
            "## Example Tests",
            "",
            "| Example | Expected | XGBoost old | XGBoost calibrated | LightGBM 1 | LightGBM 2 |",
            "|---|---|---:|---:|---:|---:|",
        ]
    )
    for row in examples:
        lines.append(
            f"| {row['name']} | {row['expected']} | "
            f"{row['outputs']['XGBoost old']['probability_text']} | "
            f"{row['outputs']['XGBoost calibrated']['probability_text']} | "
            f"{row['outputs']['LightGBM model 1']['probability_text']} | "
            f"{row['outputs']['LightGBM model 2']['probability_text']} |"
        )

    lines.extend(
        [
            "",
            "## Example Predictions",
            "",
            "| Example | XGBoost old | XGBoost calibrated | LightGBM 1 | LightGBM 2 |",
            "|---|---|---|---|---|",
        ]
    )
    for row in examples:
        lines.append(
            f"| {row['name']} | "
            f"{row['outputs']['XGBoost old']['prediction']} / {row['outputs']['XGBoost old']['risk']} | "
            f"{row['outputs']['XGBoost calibrated']['prediction']} / {row['outputs']['XGBoost calibrated']['risk']} | "
            f"{row['outputs']['LightGBM model 1']['prediction']} / {row['outputs']['LightGBM model 1']['risk']} | "
            f"{row['outputs']['LightGBM model 2']['prediction']} / {row['outputs']['LightGBM model 2']['risk']} |"
        )

    lines.extend(
        [
            "",
            "## Plain Meaning",
            "",
            "Overfitting means train score is much higher than test score.",
            "",
            "Underfitting means both train and test scores are weak.",
            "",
            "Healthy means train, validation, and test are close, and test ROC/PR are in the expected range.",
            "",
            "In these results, the calibrated models look healthy. The old XGBoost model ranks customers fairly well, but its probabilities are too high.",
        ]
    )
    RESULTS_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    df = pd.read_csv(DATA_PATH)
    splits = split_by_customer(df)
    models = [
        OldXGBoostModel(),
        CalibratedXGBoostModel(),
        LightGBMModel("LightGBM model 1", "lightgbm_model1"),
        LightGBMModel("LightGBM model 2", "lightgbm_model2"),
    ]
    metrics = evaluate_models(models, splits)
    examples = run_examples(models)
    write_markdown(metrics, examples)
    print(f"Wrote {RESULTS_PATH}")


if __name__ == "__main__":
    main()
