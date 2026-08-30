import argparse
import json
from collections import Counter
from pathlib import Path

import joblib
import numpy as np
import pandas as pd
from sklearn.isotonic import IsotonicRegression
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, average_precision_score, confusion_matrix, precision_score, recall_score, roc_auc_score
from sklearn.model_selection import StratifiedGroupKFold, train_test_split
from xgboost import XGBClassifier

from build_features import OUTPUT_DATA, TARGET, build_features
from model_v2_runtime import PRIMARY_MODEL_FILE


SCRIPT_DIR = Path(__file__).resolve().parent
MODEL_V2_ROOT = SCRIPT_DIR.parents[1]
ARTIFACT_DIR = SCRIPT_DIR / "artifacts"
DATA_PATH = OUTPUT_DATA
RANDOM_SEED = 42
# The winning configuration is refitted under each seed and the probabilities are
# averaged. One fit's ROC-AUC swings by a few thousandths on the seed alone, so a
# single fit cannot tell a real gain from seed luck; the average is both slightly
# better and stable enough to quote.
ENSEMBLE_SEEDS = (42, 7, 13)
CV_FOLDS = 5
CUSTOMER_ID = "customer_id"
DEFAULT_THRESHOLD = 0.10
TARGET_MIN_PRECISION = 0.30
TARGET_MIN_RECALL = 0.40
FALLBACK_MIN_PRECISION = 0.25
FALLBACK_MIN_RECALL = 0.35
RISK_BANDS = {"low": 0.12, "medium": 0.25}
MIN_UNIQUE_ROUNDED_PERCENT_VALUES = 200
THRESHOLD_GRID = [
    0.03,
    0.04,
    0.05,
    0.06,
    0.07,
    0.08,
    0.09,
    0.10,
    0.12,
    0.15,
    0.18,
    0.20,
    0.22,
    0.25,
    0.28,
    0.30,
    0.35,
    0.40,
    0.45,
    0.50,
]

CATEGORICAL_FEATURES = [
    "customer_segment",
    "income_regularity",
]

BLOCKED_COLUMNS = {
    "customer_id",
    "customer_name",
    "prediction_date",
    "target_month",
    "snapshot_date",
    "age",
    "customer_yearly_value",
    "loyalty",
    "complaint_text",
    "branch_code",
    "card_colour",
    "churn_flag",
    TARGET,
}


def load_training_data(path):
    if not path.exists():
        print(f"{path} does not exist. Building it first.")
        build_features(output_path=path)
    print(f"Reading v2 training data: {path}", flush=True)
    return pd.read_csv(path)


def feature_columns(df):
    blocked_found = sorted(BLOCKED_COLUMNS & set(df.columns))
    return [column for column in df.columns if column not in blocked_found]


def prepare_x(df, features):
    x_data = df[features].copy()
    leaked = sorted(set(x_data.columns) & BLOCKED_COLUMNS)
    if leaked:
        raise AssertionError(f"Leakage columns reached X: {leaked}")
    for feature in CATEGORICAL_FEATURES:
        x_data[feature] = x_data[feature].astype("category")
    return x_data


def split_by_customer(df):
    """Split by customer into train / fit_validation / calibration / test.

    The validation block is halved on purpose. Early stopping and candidate
    selection consume ``fit_validation``, so the model is already tuned to those
    rows; fitting the calibrator and picking the decision threshold on the same
    rows would read back optimistic precision and recall and ship a threshold
    set slightly too low. ``calibration`` is untouched by model fitting, so the
    threshold chosen on it is the one that transfers to production.
    """
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
    fit_customers, calibration_customers = train_test_split(
        validation_customers,
        train_size=0.50,
        random_state=RANDOM_SEED,
        stratify=validation_customers[TARGET],
    )
    select = lambda customers: df[df[CUSTOMER_ID].isin(set(customers[CUSTOMER_ID]))].copy()
    return {
        "train": select(train_customers),
        "fit_validation": select(fit_customers),
        "calibration": select(calibration_customers),
        "test": select(test_customers),
    }


def evaluate(y_true, probabilities, threshold=DEFAULT_THRESHOLD):
    predictions = (probabilities >= threshold).astype(int)
    return {
        "accuracy": float(accuracy_score(y_true, predictions)),
        "roc_auc": float(roc_auc_score(y_true, probabilities)),
        "pr_auc": float(average_precision_score(y_true, probabilities)),
        "precision": float(precision_score(y_true, predictions, zero_division=0)),
        "recall": float(recall_score(y_true, predictions, zero_division=0)),
        "confusion_matrix": confusion_matrix(y_true, predictions).tolist(),
        "flagged_rows": int(predictions.sum()),
    }


def threshold_sweep(y_true, probabilities):
    rows = []
    for threshold in THRESHOLD_GRID:
        predictions = (probabilities >= threshold).astype(int)
        precision = precision_score(y_true, predictions, zero_division=0)
        recall = recall_score(y_true, predictions, zero_division=0)
        f1 = 0.0 if precision == 0 and recall == 0 else (2 * precision * recall) / (precision + recall)
        beta = 2.0
        f2 = 0.0 if precision == 0 and recall == 0 else ((1 + beta**2) * precision * recall) / ((beta**2 * precision) + recall)
        rows.append(
            {
                "threshold": threshold,
                "flagged_rows": int(predictions.sum()),
                "accuracy": float(accuracy_score(y_true, predictions)),
                "precision": float(precision),
                "recall": float(recall),
                "f1": float(f1),
                "f2": float(f2),
            }
        )
    return rows


def choose_threshold(validation_sweep):
    balanced_rows = [
        row
        for row in validation_sweep
        if row["precision"] >= TARGET_MIN_PRECISION and row["recall"] >= TARGET_MIN_RECALL
    ]
    if balanced_rows:
        return max(balanced_rows, key=lambda row: (row["f1"], row["precision"], row["recall"]))["threshold"]

    fallback_rows = [
        row
        for row in validation_sweep
        if row["precision"] >= FALLBACK_MIN_PRECISION and row["recall"] >= FALLBACK_MIN_RECALL
    ]
    if fallback_rows:
        return max(fallback_rows, key=lambda row: (row["f1"], row["precision"], row["recall"]))["threshold"]

    return max(validation_sweep, key=lambda row: (row["f1"], row["precision"], row["recall"]))["threshold"]


def probability_diagnostics(probabilities):
    rounded = np.round(probabilities * 100, 2)
    counts = Counter(rounded)
    percentiles = np.percentile(rounded, [0, 10, 25, 50, 75, 90, 95, 99, 100])
    return {
        "unique_rounded_percent_values": int(len(counts)),
        "most_common_rounded_percent_values": [
            {"probability_percent": float(value), "count": int(count)}
            for value, count in counts.most_common(10)
        ],
        "percentiles_percent": [float(round(value, 4)) for value in percentiles],
    }


def fit_sigmoid_calibrator(raw_probabilities, y_true):
    calibrator = LogisticRegression(random_state=RANDOM_SEED, max_iter=1000)
    calibrator.fit(raw_probabilities.reshape(-1, 1), y_true)
    return calibrator


def apply_sigmoid(calibrator, raw_probabilities):
    return calibrator.predict_proba(raw_probabilities.reshape(-1, 1))[:, 1]


def choose_probability_mode(results):
    best_mode = "raw"
    best_pr_auc = results["raw"]["validation"]["pr_auc"]
    for mode in ["sigmoid", "isotonic"]:
        mode_pr_auc = results[mode]["validation"]["pr_auc"]
        unique_values = results[mode]["validation_probability_diagnostics"]["unique_rounded_percent_values"]
        if mode_pr_auc >= best_pr_auc - 0.01 and unique_values >= MIN_UNIQUE_ROUNDED_PERCENT_VALUES:
            best_mode = mode
            best_pr_auc = mode_pr_auc
    return best_mode


def xgboost_configs(scale_pos_weight):
    base = {
        "objective": "binary:logistic",
        "eval_metric": "aucpr",
        "enable_categorical": True,
        "tree_method": "hist",
        "random_state": RANDOM_SEED,
        "n_jobs": -1,
        "early_stopping_rounds": 75,
        "scale_pos_weight": scale_pos_weight,
    }
    candidates = [
        {
            "name": "balanced_depth3_regularized",
            "params": {
                **base,
                "n_estimators": 1400,
                "learning_rate": 0.025,
                "max_depth": 3,
                "min_child_weight": 4,
                "subsample": 0.90,
                "colsample_bytree": 0.90,
                "reg_alpha": 0.05,
                "reg_lambda": 2.0,
                "gamma": 0.1,
            },
        },
        {
            "name": "balanced_depth4",
            "params": {
                **base,
                "n_estimators": 1200,
                "learning_rate": 0.03,
                "max_depth": 4,
                "min_child_weight": 4,
                "subsample": 0.90,
                "colsample_bytree": 0.85,
                "reg_alpha": 0.1,
                "reg_lambda": 2.5,
                "gamma": 0.2,
            },
        },
        {
            "name": "half_balanced_depth4",
            "params": {
                **base,
                "n_estimators": 1200,
                "learning_rate": 0.03,
                "max_depth": 4,
                "min_child_weight": 5,
                "subsample": 0.85,
                "colsample_bytree": 0.90,
                "reg_alpha": 0.1,
                "reg_lambda": 3.0,
                "gamma": 0.2,
                "scale_pos_weight": max(1.0, scale_pos_weight * 0.5),
            },
        },
        {
            "name": "precision_depth3",
            "params": {
                **base,
                "n_estimators": 1400,
                "learning_rate": 0.025,
                "max_depth": 3,
                "min_child_weight": 8,
                "subsample": 0.85,
                "colsample_bytree": 0.85,
                "reg_alpha": 0.2,
                "reg_lambda": 4.0,
                "gamma": 0.4,
                "scale_pos_weight": max(1.0, scale_pos_weight * 0.35),
            },
        },
        {
            "name": "precision_depth4",
            "params": {
                **base,
                "n_estimators": 1200,
                "learning_rate": 0.025,
                "max_depth": 4,
                "min_child_weight": 7,
                "subsample": 0.85,
                "colsample_bytree": 0.80,
                "reg_alpha": 0.25,
                "reg_lambda": 4.5,
                "gamma": 0.5,
                "scale_pos_weight": max(1.0, scale_pos_weight * 0.45),
            },
        },
    ]
    return candidates


def train_best_model(x_train, y_train, x_validation, y_validation):
    negative_count = int((y_train == 0).sum())
    positive_count = int((y_train == 1).sum())
    scale_pos_weight = negative_count / max(positive_count, 1)
    print(f"Class balance scale_pos_weight: {scale_pos_weight:.3f}", flush=True)

    best = None
    for candidate in xgboost_configs(scale_pos_weight):
        print(f"Training candidate: {candidate['name']}", flush=True)
        model = XGBClassifier(**candidate["params"])
        model.fit(x_train, y_train, eval_set=[(x_validation, y_validation)], verbose=25)
        validation_probabilities = model.predict_proba(x_validation)[:, 1]
        pr_auc = average_precision_score(y_validation, validation_probabilities)
        roc_auc = roc_auc_score(y_validation, validation_probabilities)
        print(f"Candidate {candidate['name']}: validation PR-AUC={pr_auc:.4f}, ROC-AUC={roc_auc:.4f}", flush=True)
        if best is None or pr_auc > best["validation_pr_auc"]:
            best = {
                "name": candidate["name"],
                "params": candidate["params"],
                "model": model,
                "validation_pr_auc": float(pr_auc),
                "validation_roc_auc": float(roc_auc),
            }

    print(f"Best candidate: {best['name']}", flush=True)
    return best


def train_ensemble(params, x_train, y_train, x_validation, y_validation):
    """Refit the winning configuration once per seed."""
    models = []
    for seed in ENSEMBLE_SEEDS:
        print(f"Fitting ensemble member seed={seed}", flush=True)
        member_params = {**params, "random_state": seed}
        model = XGBClassifier(**member_params)
        model.fit(x_train, y_train, eval_set=[(x_validation, y_validation)], verbose=False)
        member_probabilities = model.predict_proba(x_validation)[:, 1]
        print(
            f"  seed={seed}: validation PR-AUC={average_precision_score(y_validation, member_probabilities):.4f}, "
            f"ROC-AUC={roc_auc_score(y_validation, member_probabilities):.4f}",
            flush=True,
        )
        models.append(model)
    return models


def ensemble_raw_proba(models, x_data):
    return np.column_stack([model.predict_proba(x_data)[:, 1] for model in models]).mean(axis=1)


def cross_validated_score(df, features, params, n_estimators):
    """Grouped 5-fold CV over the whole table, the number worth quoting.

    A single 15% test split of this data moves by roughly +/-0.01 ROC-AUC on the
    split seed alone, which is larger than any gain worth chasing here. Folding
    over every customer uses all 43k rows for evaluation instead of 6k, so the
    result is stable enough to compare two versions of the model against.

    Folds have no validation set to early stop against, so ``n_estimators`` is
    pinned to the round the real fit stopped at. Leaving the configured ceiling
    of 1200+ rounds in place would train past that point and report a
    pessimistic, overfitted number that says nothing about the shipped model.
    """
    y = df[TARGET].to_numpy()
    groups = df[CUSTOMER_ID].to_numpy()
    x_data = prepare_x(df, features)
    out_of_fold = np.zeros(len(df), dtype="float64")
    splitter = StratifiedGroupKFold(n_splits=CV_FOLDS, shuffle=True, random_state=RANDOM_SEED)
    fold_params = {key: value for key, value in params.items() if key != "early_stopping_rounds"}
    fold_params["n_estimators"] = n_estimators

    for fold, (train_index, test_index) in enumerate(splitter.split(x_data, y, groups), start=1):
        print(f"CV fold {fold}/{CV_FOLDS}...", flush=True)
        negative_count = int((y[train_index] == 0).sum())
        positive_count = int((y[train_index] == 1).sum())
        model = XGBClassifier(
            **{**fold_params, "scale_pos_weight": negative_count / max(positive_count, 1)}
        )
        model.fit(x_data.iloc[train_index], y[train_index], verbose=False)
        out_of_fold[test_index] = model.predict_proba(x_data.iloc[test_index])[:, 1]

    return {
        "folds": CV_FOLDS,
        "rows": int(len(df)),
        "n_estimators": int(n_estimators),
        "roc_auc": float(roc_auc_score(y, out_of_fold)),
        "pr_auc": float(average_precision_score(y, out_of_fold)),
    }


def main():
    parser = argparse.ArgumentParser(description="Train Model 1 v2 XGBoost next-month churn model.")
    parser.add_argument("--data", default=str(DATA_PATH), help="V2 training CSV.")
    parser.add_argument("--skip-cv", action="store_true", help="Skip the grouped cross-validation pass.")
    args = parser.parse_args()

    ARTIFACT_DIR.mkdir(parents=True, exist_ok=True)
    df = load_training_data(Path(args.data))
    features = feature_columns(df)
    numerical_features = [feature for feature in features if feature not in CATEGORICAL_FEATURES]
    print(f"Rows loaded: {len(df):,}", flush=True)
    print(f"Customers loaded: {df[CUSTOMER_ID].nunique():,}", flush=True)
    print(f"Positive next-month churn rows: {int(df[TARGET].sum()):,}", flush=True)
    print(f"Training features: {len(features):,}", flush=True)

    print("Splitting by customer into train, validation, and test...", flush=True)
    splits = split_by_customer(df)
    for name, split_df in splits.items():
        print(
            f"{name}: rows={len(split_df):,}, customers={split_df[CUSTOMER_ID].nunique():,}, "
            f"next_month_churn_rate={split_df[TARGET].mean():.4%}",
            flush=True,
        )

    print("Preparing XGBoost matrices...", flush=True)
    x_train = prepare_x(splits["train"], features)
    x_fit_validation = prepare_x(splits["fit_validation"], features)
    x_calibration = prepare_x(splits["calibration"], features)
    x_test = prepare_x(splits["test"], features)
    y_train = splits["train"][TARGET]
    y_fit_validation = splits["fit_validation"][TARGET]
    y_calibration = splits["calibration"][TARGET]
    y_test = splits["test"][TARGET]

    print("Training XGBoost candidates. This is the longest step...", flush=True)
    best_model = train_best_model(x_train, y_train, x_fit_validation, y_fit_validation)

    print(f"Seed-bagging the winning config over {len(ENSEMBLE_SEEDS)} seeds...", flush=True)
    models = train_ensemble(best_model["params"], x_train, y_train, x_fit_validation, y_fit_validation)
    # Rounds the early-stopped members actually used, reused to size the CV fits.
    fitted_rounds = int(np.mean([model.best_iteration + 1 for model in models]))
    print(f"Early stopping settled at ~{fitted_rounds} boosting rounds", flush=True)

    print("Calculating raw probabilities...", flush=True)
    # Calibrator and threshold are fitted on the calibration split, which no
    # model has early-stopped against.
    validation_raw = ensemble_raw_proba(models, x_calibration)
    test_raw = ensemble_raw_proba(models, x_test)
    y_validation = y_calibration

    print("Fitting sigmoid calibrator...", flush=True)
    sigmoid = fit_sigmoid_calibrator(validation_raw, y_validation)
    validation_sigmoid = apply_sigmoid(sigmoid, validation_raw)
    test_sigmoid = apply_sigmoid(sigmoid, test_raw)

    print("Fitting isotonic calibrator...", flush=True)
    isotonic = IsotonicRegression(out_of_bounds="clip")
    isotonic.fit(validation_raw, y_validation)
    validation_isotonic = isotonic.predict(validation_raw)
    test_isotonic = isotonic.predict(test_raw)

    print("Evaluating raw, sigmoid, and isotonic probabilities...", flush=True)
    probability_results = {
        "raw": {
            "validation": evaluate(y_validation, validation_raw),
            "test": evaluate(y_test, test_raw),
            "validation_threshold_sweep": threshold_sweep(y_validation, validation_raw),
            "validation_probability_diagnostics": probability_diagnostics(validation_raw),
            "test_probability_diagnostics": probability_diagnostics(test_raw),
        },
        "sigmoid": {
            "validation": evaluate(y_validation, validation_sigmoid),
            "test": evaluate(y_test, test_sigmoid),
            "validation_threshold_sweep": threshold_sweep(y_validation, validation_sigmoid),
            "validation_probability_diagnostics": probability_diagnostics(validation_sigmoid),
            "test_probability_diagnostics": probability_diagnostics(test_sigmoid),
        },
        "isotonic": {
            "validation": evaluate(y_validation, validation_isotonic),
            "test": evaluate(y_test, test_isotonic),
            "validation_threshold_sweep": threshold_sweep(y_validation, validation_isotonic),
            "validation_probability_diagnostics": probability_diagnostics(validation_isotonic),
            "test_probability_diagnostics": probability_diagnostics(test_isotonic),
        },
    }
    selected_probability_mode = choose_probability_mode(probability_results)
    selected_threshold = choose_threshold(probability_results[selected_probability_mode]["validation_threshold_sweep"])

    for mode in probability_results:
        probability_results[mode]["selected_threshold_test"] = evaluate(
            y_test,
            {"raw": test_raw, "sigmoid": test_sigmoid, "isotonic": test_isotonic}[mode],
            selected_threshold if mode == selected_probability_mode else DEFAULT_THRESHOLD,
        )

    cross_validation = None
    if not args.skip_cv:
        print(f"Running grouped {CV_FOLDS}-fold cross-validation on all rows...", flush=True)
        cross_validation = cross_validated_score(df, features, best_model["params"], fitted_rounds)
        print(
            f"Cross-validated ROC-AUC={cross_validation['roc_auc']:.4f}, "
            f"PR-AUC={cross_validation['pr_auc']:.4f}",
            flush=True,
        )

    print("Writing model artifacts and metrics...", flush=True)
    member_files = [PRIMARY_MODEL_FILE] + [
        f"xgboost_model_v2_seed{seed}.json" for seed in ENSEMBLE_SEEDS[1:]
    ]
    metadata = {
        "model_name": "model_1_v2",
        "question_answered": "Is this customer likely to churn next month?",
        "features": features,
        "categorical_features": CATEGORICAL_FEATURES,
        "numerical_features": numerical_features,
        "blocked_columns": sorted(BLOCKED_COLUMNS),
        "target": TARGET,
        "random_seed": RANDOM_SEED,
        "threshold": DEFAULT_THRESHOLD,
        "selected_threshold": selected_threshold,
        "risk_bands": RISK_BANDS,
        "probability_mode": selected_probability_mode,
        "xgboost_candidate": best_model["name"],
        "ensemble_seeds": list(ENSEMBLE_SEEDS),
        "ensemble_members": member_files,
        "xgboost_params": {key: value for key, value in best_model["params"].items() if key != "early_stopping_rounds"},
        "data_path": str(Path(args.data)),
    }
    metrics = {
        "split_summary": {
            name: {
                "customers": int(split_df[CUSTOMER_ID].nunique()),
                "rows": int(len(split_df)),
                "next_month_churn_rate": float(split_df[TARGET].mean()),
            }
            for name, split_df in splits.items()
        },
        "best_model": {
            "name": best_model["name"],
            "validation_pr_auc": best_model["validation_pr_auc"],
            "validation_roc_auc": best_model["validation_roc_auc"],
        },
        "probability_results": probability_results,
        "selected_probability_mode": selected_probability_mode,
        "selected_threshold": selected_threshold,
        "cross_validation": cross_validation,
    }

    for filename, member in zip(member_files, models):
        member.save_model(ARTIFACT_DIR / filename)
    joblib.dump(
        {
            "sigmoid": sigmoid,
            "isotonic": isotonic,
            "selected_probability_mode": selected_probability_mode,
        },
        ARTIFACT_DIR / "calibrator_v2.joblib",
    )
    (ARTIFACT_DIR / "model_metadata_v2.json").write_text(json.dumps(metadata, indent=2), encoding="utf-8")
    (ARTIFACT_DIR / "metrics_v2.json").write_text(json.dumps(metrics, indent=2), encoding="utf-8")

    print(f"Ensemble members saved: {len(models)}")
    print(f"Selected probability mode: {selected_probability_mode}")
    print(f"Selected threshold: {selected_threshold:.2f}")
    if cross_validation:
        print(
            f"Cross-validated (all {cross_validation['rows']:,} rows): "
            f"ROC-AUC={cross_validation['roc_auc']:.4f}, PR-AUC={cross_validation['pr_auc']:.4f}"
        )
    for mode, result in probability_results.items():
        test = result["selected_threshold_test"] if mode == selected_probability_mode else result["test"]
        diag = result["test_probability_diagnostics"]
        print(
            f"{mode}: PR-AUC={test['pr_auc']:.4f}, ROC-AUC={test['roc_auc']:.4f}, "
            f"precision={test['precision']:.4f}, recall={test['recall']:.4f}, "
            f"unique rounded %={diag['unique_rounded_percent_values']}"
        )


if __name__ == "__main__":
    main()
