import json
from pathlib import Path

import joblib
import lightgbm as lgb
import numpy as np
import pandas as pd
from sklearn.inspection import permutation_importance
from sklearn.isotonic import IsotonicRegression
from sklearn.metrics import average_precision_score, confusion_matrix, precision_score, recall_score, roc_auc_score
from sklearn.model_selection import train_test_split


RANDOM_SEED = 42
ROOT_DIR = Path(__file__).resolve().parents[2]
DATA_PATH = ROOT_DIR / "data" / "model_1_training_data" / "customers.csv"
ARTIFACT_DIR = Path(__file__).resolve().parent / "artifacts"

TARGET = "churn_flag"
CUSTOMER_ID = "customer_id"

DROP_COLUMNS = [
    "customer_id",
    "customer_name",
    "snapshot_date",
    "loyalty",
    "customer_yearly_value",
    "complaint_text",
    "churn_flag",
]

CATEGORICAL_FEATURES = [
    "customer_segment",
    "income_regularity",
    "branch_code",
    "card_colour",
]

FEATURES = [
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

NUMERICAL_FEATURES = [feature for feature in FEATURES if feature not in CATEGORICAL_FEATURES]
THRESHOLD_GRID = [0.03, 0.05, 0.06, 0.08, 0.10, 0.12, 0.15, 0.20, 0.25, 0.30]
DEFAULT_THRESHOLD = 0.10
RISK_BANDS = {"low": 0.10, "medium": 0.20}


def validate_columns(df: pd.DataFrame) -> None:
    missing = sorted(set(DROP_COLUMNS + FEATURES) - set(df.columns))
    if missing:
        raise ValueError(f"customers.csv is missing required columns: {missing}")


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
    assert customer_sets["train"].isdisjoint(customer_sets["validation"])
    assert customer_sets["train"].isdisjoint(customer_sets["test"])
    assert customer_sets["validation"].isdisjoint(customer_sets["test"])

    return {
        name: df[df[CUSTOMER_ID].isin(customer_ids)].copy()
        for name, customer_ids in customer_sets.items()
    }


def prepare_x(df: pd.DataFrame) -> pd.DataFrame:
    x_data = df[FEATURES].copy()
    leaked = sorted(set(DROP_COLUMNS) & set(x_data.columns))
    if leaked:
        raise AssertionError(f"Leakage columns reached X: {leaked}")

    for feature in CATEGORICAL_FEATURES:
        x_data[feature] = x_data[feature].astype("category")
    return x_data


def summarize_split(df: pd.DataFrame) -> dict:
    return {
        "customers": int(df[CUSTOMER_ID].nunique()),
        "rows": int(len(df)),
        "churn_rate": float(df[TARGET].mean()),
    }


def calibrated_probabilities(model: lgb.LGBMClassifier, calibrator: IsotonicRegression, x_data: pd.DataFrame) -> np.ndarray:
    raw_probability = model.predict_proba(x_data)[:, 1]
    return calibrator.predict(raw_probability)


def evaluate(y_true: pd.Series, probabilities: np.ndarray, threshold: float) -> dict:
    predictions = (probabilities >= threshold).astype(int)
    return {
        "roc_auc": float(roc_auc_score(y_true, probabilities)),
        "pr_auc": float(average_precision_score(y_true, probabilities)),
        "precision": float(precision_score(y_true, predictions, zero_division=0)),
        "recall": float(recall_score(y_true, predictions, zero_division=0)),
        "confusion_matrix": confusion_matrix(y_true, predictions).tolist(),
        "flagged_rows": int(predictions.sum()),
    }


def threshold_sweep(y_true: pd.Series, probabilities: np.ndarray) -> list[dict]:
    rows = []
    for threshold in THRESHOLD_GRID:
        predictions = (probabilities >= threshold).astype(int)
        rows.append(
            {
                "threshold": threshold,
                "flagged_rows": int(predictions.sum()),
                "precision": float(precision_score(y_true, predictions, zero_division=0)),
                "recall": float(recall_score(y_true, predictions, zero_division=0)),
            }
        )
    return rows


def permutation_feature_importance(model: lgb.LGBMClassifier, x_test: pd.DataFrame, y_test: pd.Series) -> list[dict]:
    result = permutation_importance(
        model,
        x_test,
        y_test,
        scoring="average_precision",
        n_repeats=3,
        random_state=RANDOM_SEED,
        n_jobs=-1,
    )
    rows = [
        {"feature": feature, "importance_mean": float(mean), "importance_std": float(std)}
        for feature, mean, std in zip(FEATURES, result.importances_mean, result.importances_std)
    ]
    return sorted(rows, key=lambda row: row["importance_mean"], reverse=True)


def branch_and_colour_sweep(model: lgb.LGBMClassifier, calibrator: IsotonicRegression, fixed_row: pd.Series) -> dict:
    base = fixed_row[FEATURES].copy()

    branch_rows = []
    for branch in [f"BR-{code}" for code in range(101, 141)]:
        row = base.copy()
        row["branch_code"] = branch
        branch_rows.append(row)
    branch_probs = calibrated_probabilities(model, calibrator, prepare_x(pd.DataFrame(branch_rows)))

    colour_rows = []
    for colour in ["blue", "green", "silver", "gold", "black"]:
        row = base.copy()
        row["card_colour"] = colour
        colour_rows.append(row)
    colour_probs = calibrated_probabilities(model, calibrator, prepare_x(pd.DataFrame(colour_rows)))

    return {
        "branch_code": {
            "min_probability": float(np.min(branch_probs)),
            "max_probability": float(np.max(branch_probs)),
            "range": float(np.max(branch_probs) - np.min(branch_probs)),
        },
        "card_colour": {
            "min_probability": float(np.min(colour_probs)),
            "max_probability": float(np.max(colour_probs)),
            "range": float(np.max(colour_probs) - np.min(colour_probs)),
        },
    }


def main() -> None:
    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    df = pd.read_csv(DATA_PATH)
    validate_columns(df)

    splits = split_by_customer(df)
    split_summary = {name: summarize_split(split_df) for name, split_df in splits.items()}

    x_train = prepare_x(splits["train"])
    x_validation = prepare_x(splits["validation"])
    x_test = prepare_x(splits["test"])
    y_train = splits["train"][TARGET]
    y_validation = splits["validation"][TARGET]
    y_test = splits["test"][TARGET]

    model = lgb.LGBMClassifier(
        objective="binary",
        metric="average_precision",
        n_estimators=500,
        learning_rate=0.03,
        num_leaves=18,
        max_depth=4,
        min_child_samples=80,
        subsample=0.85,
        subsample_freq=1,
        colsample_bytree=0.85,
        reg_alpha=0.2,
        reg_lambda=4.0,
        random_state=RANDOM_SEED,
        n_jobs=-1,
        verbose=-1,
    )
    model.fit(
        x_train,
        y_train,
        categorical_feature=CATEGORICAL_FEATURES,
        eval_set=[(x_validation, y_validation)],
        eval_metric="average_precision",
        callbacks=[lgb.early_stopping(50, verbose=False)],
    )

    validation_raw = model.predict_proba(x_validation)[:, 1]
    calibrator = IsotonicRegression(out_of_bounds="clip")
    calibrator.fit(validation_raw, y_validation)

    validation_probabilities = calibrated_probabilities(model, calibrator, x_validation)
    test_probabilities = calibrated_probabilities(model, calibrator, x_test)
    validation_metrics = evaluate(y_validation, validation_probabilities, DEFAULT_THRESHOLD)
    test_metrics = evaluate(y_test, test_probabilities, DEFAULT_THRESHOLD)
    validation_threshold_sweep = threshold_sweep(y_validation, validation_probabilities)
    test_calibration = {
        "mean_predicted_probability": float(np.mean(test_probabilities)),
        "sum_predicted_probabilities": float(np.sum(test_probabilities)),
        "true_churner_count": int(y_test.sum()),
        "test_rows": int(len(y_test)),
        "test_churn_rate": float(y_test.mean()),
    }

    if test_metrics["roc_auc"] > 0.95 or test_metrics["pr_auc"] > 0.95:
        raise RuntimeError("Leakage check failed: test metric is suspiciously above 0.95.")

    feature_importance = permutation_feature_importance(model, x_test, y_test)
    decoy_ranks = {
        feature: next(index + 1 for index, row in enumerate(feature_importance) if row["feature"] == feature)
        for feature in ["branch_code", "card_colour"]
    }
    decoy_sweeps = branch_and_colour_sweep(model, calibrator, splits["test"].iloc[0])

    metadata = {
        "model_name": "LightGBM Customer Churn Classifier",
        "features": FEATURES,
        "categorical_features": CATEGORICAL_FEATURES,
        "numerical_features": NUMERICAL_FEATURES,
        "dropped_columns": DROP_COLUMNS,
        "target": TARGET,
        "random_seed": RANDOM_SEED,
        "threshold": DEFAULT_THRESHOLD,
        "risk_bands": RISK_BANDS,
        "calibration": "isotonic_on_validation_raw_probabilities",
        "data_path": str(DATA_PATH.relative_to(ROOT_DIR)),
    }
    metrics = {
        "split_summary": split_summary,
        "validation": validation_metrics,
        "test": test_metrics,
        "validation_threshold_sweep": validation_threshold_sweep,
        "test_calibration": test_calibration,
        "permutation_importance_test": feature_importance,
        "decoy_ranks": decoy_ranks,
        "decoy_probability_sweeps": decoy_sweeps,
    }

    joblib.dump(model, ARTIFACT_DIR / "lightgbm_model.joblib")
    joblib.dump(calibrator, ARTIFACT_DIR / "isotonic_calibrator.joblib")
    (ARTIFACT_DIR / "model_metadata.json").write_text(json.dumps(metadata, indent=2), encoding="utf-8")
    (ARTIFACT_DIR / "metrics.json").write_text(json.dumps(metrics, indent=2), encoding="utf-8")

    print("Split summary")
    for name, summary in split_summary.items():
        print(
            f"{name}: customers={summary['customers']}, rows={summary['rows']}, "
            f"churn_rate={summary['churn_rate']:.4%}"
        )
    print("\nValidation threshold sweep using calibrated probabilities")
    for row in validation_threshold_sweep:
        print(
            f"threshold={row['threshold']:.2f}, flagged={row['flagged_rows']}, "
            f"precision={row['precision']:.4f}, recall={row['recall']:.4f}"
        )
    print(f"\nDefault saved threshold: {DEFAULT_THRESHOLD:.2f}")
    print("\nTest metrics at default threshold")
    print(f"ROC-AUC: {test_metrics['roc_auc']:.4f}")
    print(f"PR-AUC: {test_metrics['pr_auc']:.4f}")
    print(f"Precision: {test_metrics['precision']:.4f}")
    print(f"Recall: {test_metrics['recall']:.4f}")
    print(f"Confusion Matrix: {test_metrics['confusion_matrix']}")
    print(f"Flagged rows: {test_metrics['flagged_rows']}")
    print("\nTest calibration check")
    print(f"Mean predicted probability: {test_calibration['mean_predicted_probability']:.4f}")
    print(f"Sum predicted probabilities: {test_calibration['sum_predicted_probabilities']:.1f}")
    print(f"True churner count: {test_calibration['true_churner_count']}")
    print("\nTop permutation importance features on test")
    for row in feature_importance[:15]:
        print(f"{row['feature']}: {row['importance_mean']:.6f} +/- {row['importance_std']:.6f}")
    print("\nDecoy ranks by permutation importance")
    print(decoy_ranks)
    print("\nDecoy probability sweeps")
    print(decoy_sweeps)


if __name__ == "__main__":
    main()
