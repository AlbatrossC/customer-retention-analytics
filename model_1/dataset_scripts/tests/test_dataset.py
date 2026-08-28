"""Tests for the Sandbox Bank dataset generator.

    python -m pytest model_1/dataset_scripts/tests -q

The heavier structural assertions live in scripts/check_dataset.py, which runs
against the written CSV. These tests cover the generator's invariants directly,
including the ones that would silently degrade the data rather than break it:
determinism, absorbing churn, and the fact that the label is not a threshold rule.
"""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import pandas as pd
import pytest

PACKAGE_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PACKAGE_ROOT))

from generate import COLUMN_ORDER, build_dataset, to_output_frame  # noqa: E402
from src.behaviour import NO_SALARY_SEGMENTS  # noqa: E402
from src.interventions import ACTIONS, simulate_intervention  # noqa: E402
from src.profiles import PROJECT_ROOT, load_config, make_streams  # noqa: E402
from src.service import load_complaint_texts  # noqa: E402

CHANGE_COLUMNS = [
    "balance_change_30d",
    "transaction_change_30d",
    "card_spend_change_30d",
    "app_login_change_30d",
    "external_transfer_change_30d",
]


@pytest.fixture(scope="module")
def config() -> dict:
    return load_config()


@pytest.fixture(scope="module")
def built(config: dict) -> dict:
    return build_dataset(config, make_streams(config))


@pytest.fixture(scope="module")
def panel(built: dict) -> pd.DataFrame:
    return built["panel"]


# --- identity and shape -------------------------------------------------


def test_customer_ids_are_sequential(panel: pd.DataFrame, config: dict) -> None:
    ids = sorted(panel["customer_id"].unique())
    start = config["dataset"]["customer_id_start"]
    n = config["dataset"]["n_customers"]
    assert len(ids) == n
    assert ids[0] == f"C{start}"
    assert ids[-1] == f"C{start + n - 1}"


def test_snapshot_dates_are_six_monthly(panel: pd.DataFrame, config: dict) -> None:
    dates = sorted(panel["snapshot_date"].unique())
    assert len(dates) == config["dataset"]["n_snapshots"]
    assert dates[0] == "2026-01-01"
    assert dates[-1] == "2026-06-01"


def test_churn_is_absorbing(panel: pd.DataFrame, config: dict) -> None:
    """At most one churn row per customer, and it is always their last."""
    per_customer = panel.groupby("customer_id")["churn_flag"]
    assert per_customer.sum().max() <= config["checks"]["max_churn_rows_per_customer"]
    # The last row is the only one allowed to carry the flag.
    assert (per_customer.apply(lambda values: values.iloc[:-1].sum()) == 0).all()


def test_row_counts_within_bounds(panel: pd.DataFrame, config: dict) -> None:
    sizes = panel.groupby("customer_id").size()
    assert sizes.min() >= config["checks"]["min_snapshots_per_customer"]
    assert sizes.max() <= config["checks"]["max_snapshots_per_customer"]
    # A customer who never churns keeps the full panel.
    never_churned = panel.groupby("customer_id")["churn_flag"].sum() == 0
    assert (sizes[never_churned] == config["dataset"]["n_snapshots"]).all()


def test_output_columns_match_the_spec(panel: pd.DataFrame, config: dict) -> None:
    frame = to_output_frame(panel, config)
    assert list(frame.columns) == COLUMN_ORDER
    # Nothing internal leaks into the file.
    assert not [column for column in frame.columns if column.startswith("_")]


# --- field rules --------------------------------------------------------


def test_tenure_never_precedes_adulthood(panel: pd.DataFrame, config: dict) -> None:
    minimum_age = config["profiles"]["min_banking_age"]
    assert ((panel["tenure_months"] / 12) <= (panel["age"] - minimum_age)).all()


def test_salary_missing_days_is_nan_for_the_right_segments(panel: pd.DataFrame) -> None:
    no_salary = panel["customer_segment"].isin(NO_SALARY_SEGMENTS)
    assert panel.loc[no_salary, "salary_missing_days"].isna().all()
    assert panel.loc[~no_salary, "salary_missing_days"].notna().all()


def test_change_fields_are_clipped(panel: pd.DataFrame, config: dict) -> None:
    lo = config["behaviour"]["change_clip_min"]
    hi = config["behaviour"]["change_clip_max"]
    for column in CHANGE_COLUMNS:
        assert panel[column].between(lo, hi).all(), column


def test_products_count_never_contradicts_the_flags(panel: pd.DataFrame) -> None:
    minimum = 1 + panel["has_credit_card"] + panel["has_loan"]
    assert (panel["products_count"] >= minimum).all()


def test_emi_bounce_only_fires_with_a_loan(panel: pd.DataFrame) -> None:
    assert panel.loc[panel["has_loan"] == 0, "emi_bounce_30d"].eq(0).all()


def test_unresolved_never_exceeds_complaints(panel: pd.DataFrame) -> None:
    assert (panel["unresolved_complaints"] <= panel["complaints_30d"]).all()


def test_complaint_text_is_empty_exactly_when_there_is_no_complaint(
    panel: pd.DataFrame, config: dict
) -> None:
    empty = config["service"]["complaint_text"]["empty_value"]
    has_complaint = panel["complaints_30d"] > 0
    assert (panel.loc[~has_complaint, "complaint_text"] == empty).all()
    assert (panel.loc[has_complaint, "complaint_text"] != empty).all()


def test_upi_share_is_a_proportion(panel: pd.DataFrame) -> None:
    assert panel["upi_share_of_spend"].between(0.0, 1.0).all()


# --- the label ----------------------------------------------------------


def test_churn_rate_is_rare_and_in_band(panel: pd.DataFrame, config: dict) -> None:
    rate = panel["churn_flag"].mean()
    assert config["checks"]["churn_rate_min"] <= rate <= config["checks"]["churn_rate_max"]


def test_label_is_not_a_threshold_rule(panel: pd.DataFrame) -> None:
    """Section 5.1. No feature value may perfectly separate the label.

    If churn were decided by `salary_missing_days > 7` then every row above the
    cut would churn and none below would. A weighted coin flip cannot do that.
    """
    for column in ["salary_missing_days", "days_since_last_transaction", "unresolved_complaints"]:
        values = panel[column].dropna()
        churned = panel.loc[values.index, "churn_flag"]
        for cut in np.percentile(values, [50, 75, 90, 95, 99]):
            above = churned[values > cut]
            if len(above) > 50:
                assert 0.0 < above.mean() < 1.0, f"{column} > {cut} separates the label"


def test_high_risk_customers_sometimes_stay(panel: pd.DataFrame) -> None:
    """The coin flip must cut both ways, or the data is deterministic."""
    worst = panel[panel["unresolved_complaints"] >= 3]
    assert len(worst) > 50
    assert worst["churn_flag"].mean() < 0.9


def test_decoys_carry_no_signal(panel: pd.DataFrame) -> None:
    from scipy.stats import chi2_contingency

    for column in ("branch_code", "card_colour"):
        table = pd.crosstab(panel[column], panel["churn_flag"])
        table = table[table.sum(axis=1) >= 200]
        _stat, p_value, _dof, _expected = chi2_contingency(table)
        assert p_value >= 0.01, f"{column} is not independent of churn"


# --- reproducibility ----------------------------------------------------


def test_reruns_are_byte_identical(config: dict, built: dict) -> None:
    again = build_dataset(config, make_streams(config))
    first = to_output_frame(built["panel"], config).to_csv(index=False, lineterminator="\n")
    second = to_output_frame(again["panel"], config).to_csv(index=False, lineterminator="\n")
    assert first == second


def test_adding_a_stream_does_not_shift_existing_draws(config: dict, panel: pd.DataFrame) -> None:
    """The reason for one named stream per attribute (section 14).

    Appending a name to seed.streams must leave every existing stream's draws
    untouched, so a new column added later does not regenerate the dataset.
    """
    extended = load_config()
    extended["seed"]["streams"] = list(extended["seed"]["streams"]) + ["a_future_column"]
    rebuilt = build_dataset(extended, make_streams(extended))["panel"]
    pd.testing.assert_frame_equal(panel, rebuilt)


# --- complaint texts ----------------------------------------------------


def test_complaint_pool_is_complete(config: dict) -> None:
    texts = load_complaint_texts(config)
    text_cfg = config["service"]["complaint_text"]
    assert sorted(texts) == sorted(text_cfg["categories"])
    for category in text_cfg["categories"]:
        assert len(texts[category]) == text_cfg["texts_per_category"]
    everything = [entry["text"] for entries in texts.values() for entry in entries]
    assert len(everything) == 360
    assert len(set(everything)) == 360


def test_loan_complaints_only_reach_loan_holders(panel: pd.DataFrame, config: dict) -> None:
    texts = load_complaint_texts(config)
    loan_texts = {entry["text"] for entry in texts["loan_emi"]}
    no_loan = panel[panel["has_loan"] == 0]
    assert not set(no_loan["complaint_text"]) & loan_texts


# --- interventions ------------------------------------------------------


def test_responsiveness_covers_every_action(built: dict, config: dict) -> None:
    from src.interventions import build_responsiveness

    frame = build_responsiveness(
        built["profiles"], built["panel"], built["hidden"], config, make_streams(config)
    )
    assert len(frame) == config["dataset"]["n_customers"]
    for action in ACTIONS:
        values = frame[action]
        assert values.between(config["interventions"]["clip_min"], config["interventions"]["clip_max"]).all()


def test_responsiveness_follows_the_section_5_5_rules(built: dict, config: dict) -> None:
    from src.interventions import build_responsiveness

    frame = build_responsiveness(
        built["profiles"], built["panel"], built["hidden"], config, make_streams(config)
    ).merge(built["profiles"][["customer_id", "tenure_months", "customer_segment"]], on="customer_id")

    high_tenure = frame["tenure_months"] > config["interventions"]["high_tenure_months"]
    assert frame.loc[high_tenure, "rm_call"].mean() > frame.loc[~high_tenure, "rm_call"].mean()

    is_pension = frame["customer_segment"] == "pension"
    assert frame.loc[is_pension, "rate_offer"].mean() > frame.loc[~is_pension, "rate_offer"].mean()


def test_simulate_intervention_returns_a_bool(config: dict) -> None:
    path = PROJECT_ROOT / config["dataset"]["responsiveness_csv"]
    if not path.exists():
        pytest.skip("run generate.py first")
    rng = np.random.default_rng(0)
    result = simulate_intervention("C10000", "rm_call", config=config, rng=rng)
    assert isinstance(result, bool)


def test_simulate_intervention_rejects_unknown_input(config: dict) -> None:
    with pytest.raises(ValueError):
        simulate_intervention("C10000", "free_toaster", config=config)


def test_responsiveness_is_not_a_model_feature(panel: pd.DataFrame) -> None:
    assert not set(ACTIONS) & set(panel.columns)


# --- the DROP list ------------------------------------------------------


def test_drop_list_removes_every_identifier(panel: pd.DataFrame, config: dict) -> None:
    from scripts.gate_check10 import make_feature_matrix

    features = make_feature_matrix(panel, config)
    for column in config["gate"]["drop_columns"]:
        assert column not in features.columns
    assert not [column for column in features.columns if column.startswith("_")]
