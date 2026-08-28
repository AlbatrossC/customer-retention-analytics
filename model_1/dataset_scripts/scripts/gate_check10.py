"""Section 13 check 10 - the gate.

A throwaway LightGBM fit on the stages built so far. Split by customer, drop
every column in the section 8 DROP list, report test ROC-AUC, PR-AUC and the
overall churn rate.

Above 0.95 the data is too obvious, below 0.70 there is no signal. Either way
nothing built on top of it would be worth keeping.
"""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from src.profiles import load_config, make_streams, build_profiles  # noqa: E402


def split_by_customer(
    customer_ids: np.ndarray, config: dict, rng: np.random.Generator
) -> pd.Series:
    """Assign whole customers to train / validation / test, never rows.

    A random row split puts C10291's January row in train and their June row in
    test, and the model memorises the customer instead of learning the pattern.
    """
    cfg = config["split"]
    unique = np.array(sorted(set(customer_ids)))
    shuffled = rng.permutation(unique)
    n = len(shuffled)
    n_train = int(round(n * cfg["train"]))
    n_val = int(round(n * cfg["validation"]))
    assignment = {}
    for cid in shuffled[:n_train]:
        assignment[cid] = "train"
    for cid in shuffled[n_train : n_train + n_val]:
        assignment[cid] = "validation"
    for cid in shuffled[n_train + n_val :]:
        assignment[cid] = "test"
    return pd.Series(customer_ids).map(assignment)


def make_feature_matrix(frame: pd.DataFrame, config: dict) -> pd.DataFrame:
    """Drop the section 8 DROP list and anything internal, cast categoricals."""
    gate = config["gate"]
    drop = [column for column in gate["drop_columns"] if column in frame.columns]
    internal = [column for column in frame.columns if column.startswith("_")]
    features = frame.drop(columns=drop + internal)
    for column in gate["categorical_columns"]:
        if column in features.columns:
            features[column] = features[column].astype("category")
    return features


def run_gate(panel: pd.DataFrame, config: dict, rng: np.random.Generator) -> dict:
    from lightgbm import LGBMClassifier
    from sklearn.metrics import average_precision_score, roc_auc_score

    split = split_by_customer(panel["customer_id"].to_numpy(), config, rng)
    target = config["gate"]["target"]

    features = make_feature_matrix(panel, config)
    labels = panel[target].to_numpy()

    is_train = (split == "train").to_numpy()
    is_test = (split == "test").to_numpy()

    model = LGBMClassifier(**config["gate"]["lightgbm"])
    model.fit(features[is_train], labels[is_train])
    scores = model.predict_proba(features[is_test])[:, 1]

    return {
        "roc_auc": roc_auc_score(labels[is_test], scores),
        "pr_auc": average_precision_score(labels[is_test], scores),
        "churn_rate": float(labels.mean()),
        "feature_columns": list(features.columns),
        "model": model,
        "split": split,
    }


def build_panel_for_gate(config: dict, streams: dict) -> pd.DataFrame:
    from generate import build_dataset

    return build_dataset(config, streams)["panel"]


def main() -> int:
    config = load_config()
    streams = make_streams(config)
    panel = build_panel_for_gate(config, streams)
    result = run_gate(panel, config, streams["split"])

    print("Section 13 check 10 - gate")
    print(f"  rows                 : {len(panel):,}")
    print(f"  feature columns      : {len(result['feature_columns'])}")
    print(f"  overall churn rate   : {result['churn_rate']:.4f}")
    print(f"  test ROC-AUC         : {result['roc_auc']:.4f}")
    print(f"  test PR-AUC          : {result['pr_auc']:.4f}")

    lo = config["gate"]["roc_auc_min"]
    hi = config["gate"]["roc_auc_max"]
    verdict = "PASS" if lo <= result["roc_auc"] <= hi else "FAIL"
    print(f"  gate ({lo} - {hi})    : {verdict}")

    importances = pd.Series(
        result["model"].feature_importances_, index=result["feature_columns"]
    ).sort_values(ascending=False)
    print("\n  top feature importances (gain-free split count):")
    for name, value in importances.head(12).items():
        print(f"    {name:<32} {value}")
    return 0 if verdict == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
