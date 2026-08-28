"""Stage 3 - the churn label.

Section 5.1 is the rule this module exists to obey: never write threshold rules
to decide churn. There is no ``if salary_missing_days > 7`` anywhere here.

Section 5.2 is the method: build a score, push it through a sigmoid, flip a
weighted coin, then flip an extra unexplained share of the non-churners. Because
it is a coin flip, some high-risk customers stay and some low-risk customers
leave. That is the point.
"""

from __future__ import annotations

import numpy as np
import pandas as pd


def _drop_percent(change: np.ndarray) -> np.ndarray:
    """A percent change of -31 is a 31% drop. A rise is not a drop, so it is 0."""
    return np.clip(-change, 0.0, None)


def churn_score(panel: pd.DataFrame, config: dict, latent_pressure: np.ndarray) -> np.ndarray:
    """The additive score of section 5.2."""
    weights = config["label"]["weights"]

    # NaN contributes 0: farmer, vendor and business have no expected credit, so
    # the term is absent rather than favourable.
    salary_missing = np.nan_to_num(
        panel["salary_missing_days"].to_numpy(dtype=float), nan=0.0
    )

    return (
        config["label"]["base_logit"]
        + weights["salary_missing_days"] * salary_missing
        + weights["balance_drop_percent"]
        * _drop_percent(panel["balance_change_30d"].to_numpy())
        + weights["card_spend_drop_percent"]
        * _drop_percent(panel["card_spend_change_30d"].to_numpy())
        + weights["days_since_last_transaction"]
        * panel["days_since_last_transaction"].to_numpy()
        + weights["unresolved_complaints"] * latent_pressure
        + weights["fd_maturing_in_30d"] * panel["fd_maturing_in_30d"].to_numpy()
        + weights["tenure_months_sqrt"] * np.sqrt(panel["tenure_months"].to_numpy())
        + panel["loyalty"].to_numpy()  # hidden, one draw per customer
    )


def assign_labels(
    panel: pd.DataFrame,
    latent_pressure: np.ndarray,
    config: dict,
    streams: dict[str, np.random.Generator],
) -> pd.DataFrame:
    """Add churn_flag to the panel. Returns a new frame.

    ``latent_pressure`` is the hidden complaint pressure from service.py, drawn
    before this call. It carries the unresolved_complaints term of section 5.2
    into the score; the observed complaint columns are drawn from it afterwards.
    """
    panel = panel.copy()
    score = churn_score(panel, config, latent_pressure)
    chance = 1.0 / (1.0 + np.exp(-score))
    churn_flag = streams["label_coin"].binomial(1, chance)

    # Real customers also leave for reasons the bank cannot observe.
    unexplained = streams["label_unexplained"].random(len(panel)) < (
        config["label"]["unexplained_churn_rate"]
    )
    churn_flag = np.where((churn_flag == 0) & unexplained, 1, churn_flag)

    panel["churn_flag"] = churn_flag.astype(int)
    return panel


def truncate_at_churn(panel: pd.DataFrame, config: dict) -> pd.DataFrame:
    """Churn is absorbing: a customer's panel stops at their first churn row.

    Churn is dormancy sustained over 30 days (section 3). A customer labelled
    dormant in April cannot then be described as actively transacting in May -
    the two rows would describe the same 30 day window and contradict each
    other - and no customer can churn twice. So once churn_flag fires, no
    further snapshots are generated for that customer.

    Every customer keeps between 1 and 6 rows, at most one row has
    churn_flag = 1, and that row is always their last.
    """
    if not config["label"]["absorbing"]:
        return panel

    order = panel.groupby("customer_id", sort=False).cumcount()
    churned = panel["churn_flag"].to_numpy() == 1
    # Position of each customer's first churn row, or a sentinel past the end.
    sentinel = config["dataset"]["n_snapshots"]
    first_churn = (
        pd.Series(np.where(churned, order, sentinel), index=panel.index)
        .groupby(panel["customer_id"].to_numpy(), sort=False)
        .transform("min")
        .to_numpy()
    )
    return panel[order.to_numpy() <= first_churn].reset_index(drop=True)
