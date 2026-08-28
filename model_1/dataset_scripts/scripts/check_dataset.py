"""Verify model_1/data/customers.csv against the ten acceptance checks.

    python model_1/dataset_scripts/scripts/check_dataset.py

Prints one PASS or FAIL line per check and exits non-zero if any fail.
"""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from scripts.gate_check10 import run_gate, split_by_customer  # noqa: E402
from src.behaviour import NO_SALARY_SEGMENTS  # noqa: E402
from src.profiles import PROJECT_ROOT, load_config, make_streams  # noqa: E402

ROOT = PROJECT_ROOT

CHANGE_COLUMNS = [
    "balance_change_30d",
    "transaction_change_30d",
    "card_spend_change_30d",
    "app_login_change_30d",
    "external_transfer_change_30d",
]

# Behaviour columns that should get worse for a declining customer. The sign is
# the direction of deterioration.
TREND_COLUMNS = {
    "balance_change_30d": -1,
    "transaction_change_30d": -1,
    "card_spend_change_30d": -1,
    "app_login_change_30d": -1,
    "days_since_last_transaction": +1,
}


class Results:
    def __init__(self) -> None:
        self.failures = 0

    def report(self, number: int, title: str, passed: bool, detail: str = "") -> None:
        status = "PASS" if passed else "FAIL"
        if not passed:
            self.failures += 1
        line = f"[{status}] {number:>2}. {title}"
        print(f"{line}\n         {detail}" if detail else line)


def check_1_shape(frame: pd.DataFrame, config: dict, results: Results) -> None:
    """Churn is absorbing, so the panel is ragged rather than a flat 6 per customer."""
    cfg = config["checks"]
    sizes = frame.groupby("customer_id").size()
    churn_per_customer = frame.groupby("customer_id")["churn_flag"].sum()

    size_ok = bool(
        (sizes >= cfg["min_snapshots_per_customer"]).all()
        and (sizes <= cfg["max_snapshots_per_customer"]).all()
    )
    once_ok = bool((churn_per_customer <= cfg["max_churn_rows_per_customer"]).all())
    # Every churn row must be the last row its customer has.
    last_rows = frame.groupby("customer_id").tail(1)
    churn_rows = frame[frame["churn_flag"] == 1]
    last_ok = bool(set(churn_rows.index) <= set(last_rows.index))

    results.report(
        1,
        "Row shape: 1-6 rows per customer, at most one churn row, always last",
        size_ok and once_ok and last_ok,
        f"{len(frame):,} rows, {frame['customer_id'].nunique():,} customers, "
        f"rows per customer {sizes.min()}-{sizes.max()}, "
        f"customers with >1 churn row {int((churn_per_customer > 1).sum())}, "
        f"churn rows not last {len(churn_rows) - len(set(churn_rows.index) & set(last_rows.index))}",
    )


def check_2_churn_rate(frame: pd.DataFrame, config: dict, results: Results) -> None:
    cfg = config["checks"]
    lo, hi = cfg["churn_rate_min"], cfg["churn_rate_max"]
    overall = frame["churn_flag"].mean()
    by_split = frame.groupby("_split")["churn_flag"].mean()
    passed = bool(lo <= overall <= hi and ((by_split >= lo) & (by_split <= hi)).all())
    detail = f"overall {overall:.4f}; " + ", ".join(
        f"{name} {value:.4f}" for name, value in by_split.items()
    )
    results.report(2, f"Churn rate within [{lo}, {hi}] overall and in every split", passed, detail)


def check_3_tenure(frame: pd.DataFrame, config: dict, results: Results) -> None:
    minimum_age = config["profiles"]["min_banking_age"]
    violations = int(((frame["tenure_months"] / 12) > (frame["age"] - minimum_age)).sum())
    results.report(
        3,
        f"tenure_months / 12 <= age - {minimum_age} for every row",
        violations == 0,
        f"{violations} violations",
    )


def check_4_salary_missing(frame: pd.DataFrame, config: dict, results: Results) -> None:
    no_salary = frame["customer_segment"].isin(NO_SALARY_SEGMENTS)
    missing = frame["salary_missing_days"].isna()
    should_be_nan = int((no_salary & ~missing).sum())
    should_not_be_nan = int((~no_salary & missing).sum())
    results.report(
        4,
        "salary_missing_days is NaN exactly for farmer, vendor and business",
        should_be_nan == 0 and should_not_be_nan == 0,
        f"{should_be_nan} non-NaN in {'/'.join(NO_SALARY_SEGMENTS)}, "
        f"{should_not_be_nan} NaN in salary/pension",
    )


def check_5_clipping(frame: pd.DataFrame, config: dict, results: Results) -> None:
    lo = config["behaviour"]["change_clip_min"]
    hi = config["behaviour"]["change_clip_max"]
    outside = {
        column: int(((frame[column] < lo) | (frame[column] > hi)).sum())
        for column in CHANGE_COLUMNS
    }
    total = sum(outside.values())
    observed = frame[CHANGE_COLUMNS]
    results.report(
        5,
        f"Every _change_30d field inside [{lo}, {hi}]",
        total == 0,
        f"{total} values outside; observed range "
        f"[{observed.min().min():.1f}, {observed.max().max():.1f}]",
    )


def check_6_decoys(frame: pd.DataFrame, config: dict, results: Results) -> None:
    """Flatness as a chi-square test of independence, not a raw spread.

    With 40 branches at a 6% base rate, sampling noise alone moves the observed
    rate by a couple of points, so a spread threshold would either be too tight
    or meaningless. The question is whether churn is independent of the decoy.
    """
    from scipy.stats import chi2_contingency

    cfg = config["checks"]
    details, passed = [], True
    for column in ("branch_code", "card_colour"):
        table = pd.crosstab(frame[column], frame["churn_flag"])
        keep = table.sum(axis=1) >= cfg["decoy_min_rows_per_level"]
        table = table[keep]
        _stat, p_value, _dof, _expected = chi2_contingency(table)
        rates = frame.groupby(column)["churn_flag"].mean()[keep.index[keep]]
        spread = rates.max() - rates.min()
        ok = p_value >= cfg["decoy_chi2_min_p"]
        passed = passed and ok
        details.append(
            f"{column}: {len(table)} levels, chi2 p={p_value:.3f}, spread={spread:.4f}"
        )
    results.report(
        6,
        f"Churn rate flat across branch_code and card_colour (chi2 p >= {cfg['decoy_chi2_min_p']})",
        passed,
        "; ".join(details),
    )


def check_7_no_extremes(frame: pd.DataFrame, config: dict, results: Results) -> None:
    """No single feature value may produce a 0% or 100% churn rate."""
    cfg = config["checks"]
    minimum = cfg["extreme_rate_min_rows"]
    candidates = [
        "customer_segment",
        "income_regularity",
        "branch_code",
        "card_colour",
        "products_count",
        "has_credit_card",
        "has_loan",
        "fd_maturing_in_30d",
        "products_dropped_90d",
        "complaints_30d",
        "unresolved_complaints",
        "emi_bounce_30d",
    ]
    offenders = []
    for column in candidates:
        grouped = frame.groupby(column)["churn_flag"].agg(["mean", "size"])
        grouped = grouped[grouped["size"] >= minimum]
        extreme = grouped[(grouped["mean"] <= 0.0) | (grouped["mean"] >= 1.0)]
        for value, row in extreme.iterrows():
            offenders.append(f"{column}={value} rate={row['mean']:.2f} n={int(row['size'])}")
    results.report(
        7,
        f"No single feature value gives a 0% or 100% churn rate (n >= {minimum})",
        not offenders,
        "; ".join(offenders) if offenders else f"{len(candidates)} columns checked, none extreme",
    )


def check_8_declining_trend(
    frame: pd.DataFrame, hidden: pd.DataFrame, config: dict, results: Results
) -> None:
    """A declining customer's snapshots must visibly trend downward."""
    cfg = config["checks"]
    declining = set(hidden.loc[hidden["drift_state"] == "declining", "customer_id"])
    subset = frame[frame["customer_id"].isin(declining)]
    sizes = subset.groupby("customer_id").size()
    eligible = set(sizes[sizes >= cfg["trend_min_rows"]].index)
    subset = subset[subset["customer_id"].isin(eligible)]

    # Second half worse than first half, averaged over the trending columns.
    trending = 0
    for _cid, rows in subset.groupby("customer_id", sort=False):
        half = len(rows) // 2
        votes = 0
        for column, sign in TREND_COLUMNS.items():
            first = rows[column].iloc[:half].mean()
            second = rows[column].iloc[half:].mean()
            votes += sign * (second - first) > 0
        trending += votes >= len(TREND_COLUMNS) / 2
    fraction = trending / len(eligible) if eligible else 0.0
    results.report(
        8,
        f"Declining customers trend downward (>= {cfg['declining_trend_min_fraction']:.0%})",
        fraction >= cfg["declining_trend_min_fraction"],
        f"{trending:,} of {len(eligible):,} eligible declining customers "
        f"({fraction:.1%}) worsen on most behaviour columns",
    )


def check_9_split_purity(frame: pd.DataFrame, config: dict, results: Results) -> None:
    per_customer = frame.groupby("customer_id")["_split"].nunique()
    leaked = int((per_customer > 1).sum())
    counts = frame.groupby("_split")["customer_id"].nunique().to_dict()
    results.report(
        9,
        "No customer_id appears in more than one split",
        leaked == 0,
        f"{leaked} customers span splits; customers per split {counts}",
    )


def check_10_gate(frame: pd.DataFrame, config: dict, streams: dict, results: Results) -> None:
    gate = config["gate"]
    result = run_gate(frame, config, streams["split"])
    lo, hi = gate["roc_auc_min"], gate["roc_auc_max"]
    passed = bool(lo <= result["roc_auc"] <= hi)
    results.report(
        10,
        f"Quick LightGBM fit gives test ROC-AUC in [{lo}, {hi}]",
        passed,
        f"ROC-AUC {result['roc_auc']:.4f}, PR-AUC {result['pr_auc']:.4f}, "
        f"{len(result['feature_columns'])} features",
    )


def main() -> int:
    config = load_config()
    streams = make_streams(config)

    frame = pd.read_csv(ROOT / config["dataset"]["output_csv"])
    hidden = pd.read_csv(ROOT / config["dataset"]["responsiveness_csv"])
    frame["_split"] = split_by_customer(
        frame["customer_id"].to_numpy(), config, streams["split"]
    ).to_numpy()

    print(f"Checking {config['dataset']['output_csv']} against section 13\n")
    results = Results()
    check_1_shape(frame, config, results)
    check_2_churn_rate(frame, config, results)
    check_3_tenure(frame, config, results)
    check_4_salary_missing(frame, config, results)
    check_5_clipping(frame, config, results)
    check_6_decoys(frame, config, results)
    check_7_no_extremes(frame, config, results)
    check_8_declining_trend(frame, hidden, config, results)
    check_9_split_purity(frame, config, results)
    check_10_gate(frame, config, streams, results)

    print(
        f"\n{10 - results.failures} of 10 checks passed."
        if results.failures
        else "\nAll 10 checks passed."
    )
    return 1 if results.failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
