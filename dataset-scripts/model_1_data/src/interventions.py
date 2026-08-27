"""Stage 5 - hidden intervention responsiveness (section 5.5).

Every customer gets a hidden probability of responding to each of the five
retention actions. This feeds the Sandbox Bank agent later, which is why it is
built now rather than retrofitted.

Responsiveness never becomes a model feature. It is written to
data/responsiveness.csv, which is the simulator's private file, not training
data. If it leaked into the feature matrix the model would be predicting churn
from the answer to "would a retention call have worked".
"""

from __future__ import annotations

from functools import lru_cache
from pathlib import Path

import numpy as np
import pandas as pd

from .profiles import PROJECT_ROOT
from .service import FEE_CATEGORY

ACTIONS = ("fee_waiver", "rm_call", "complaint_escalation", "rate_offer", "do_nothing")

COMPLAINT_CATEGORY_COLUMN = "_complaint_category"


def _per_customer_flags(panel: pd.DataFrame, profiles: pd.DataFrame) -> pd.DataFrame:
    """Collapse the panel to the one-row-per-customer facts the rules need."""
    grouped = panel.groupby("customer_id", sort=False)
    flags = pd.DataFrame(
        {
            "had_fee_complaint": grouped[COMPLAINT_CATEGORY_COLUMN]
            .apply(lambda values: bool((values == FEE_CATEGORY).any()))
            .astype(int),
            "had_unresolved": (grouped["unresolved_complaints"].max() > 0).astype(int),
            "deposit_heavy": (grouped["fd_maturing_in_30d"].max() > 0).astype(int),
        }
    )
    return profiles.set_index("customer_id").join(flags).reset_index()


def build_responsiveness(
    profiles: pd.DataFrame,
    panel: pd.DataFrame,
    hidden: pd.DataFrame,
    config: dict,
    streams: dict[str, np.random.Generator],
) -> pd.DataFrame:
    """One hidden response probability per customer per action."""
    cfg = config["interventions"]
    rng = streams["responsiveness"]
    facts = _per_customer_flags(panel, profiles)
    n = len(facts)

    low_value_cut = facts["customer_yearly_value"].quantile(cfg["low_value_quantile"])
    low_value = (facts["customer_yearly_value"] < low_value_cut).to_numpy().astype(int)
    high_tenure = (facts["tenure_months"] > cfg["high_tenure_months"]).to_numpy().astype(int)
    is_pension = (facts["customer_segment"] == "pension").to_numpy().astype(int)
    fee_complaint = facts["had_fee_complaint"].to_numpy()
    unresolved = facts["had_unresolved"].to_numpy()
    deposit_heavy = facts["deposit_heavy"].to_numpy()

    actions = cfg["actions"]
    values = {
        # Works best on low value customers and on fee complaints.
        "fee_waiver": actions["fee_waiver"]["base"]
        + actions["fee_waiver"]["low_value_bonus"] * low_value
        + actions["fee_waiver"]["fee_complaint_bonus"] * fee_complaint,
        # Works best on long tenure customers, who still value the relationship.
        "rm_call": actions["rm_call"]["base"]
        + actions["rm_call"]["high_tenure_bonus"] * high_tenure,
        # Only meaningful where something is actually stuck.
        "complaint_escalation": actions["complaint_escalation"]["base"]
        + actions["complaint_escalation"]["unresolved_bonus"] * unresolved,
        # Works best on pension and deposit heavy customers.
        "rate_offer": actions["rate_offer"]["base"]
        + actions["rate_offer"]["pension_bonus"] * is_pension
        + actions["rate_offer"]["deposit_heavy_bonus"] * deposit_heavy,
        # Baseline. Some customers stay whatever the bank does or does not do.
        "do_nothing": np.full(n, float(actions["do_nothing"]["base"])),
    }

    frame = pd.DataFrame({"customer_id": facts["customer_id"].to_numpy()})
    for action in ACTIONS:
        jittered = values[action] + rng.normal(0.0, cfg["noise_sd"], size=n)
        frame[action] = np.clip(jittered, cfg["clip_min"], cfg["clip_max"])

    # drift_state and service_shock ride along in this hidden file so the
    # acceptance checks and the agent can identify the two churn pathways
    # without either ever appearing in customers.csv.
    return frame.merge(hidden, on="customer_id", how="left")


@lru_cache(maxsize=1)
def _load_responsiveness(path: str) -> pd.DataFrame:
    return pd.read_csv(path).set_index("customer_id")


def simulate_intervention(
    customer_id: str,
    action: str,
    config: dict | None = None,
    rng: np.random.Generator | None = None,
    root: Path | None = None,
) -> bool:
    """Did the customer respond to this retention action?

    A weighted coin flip against the customer's hidden responsiveness, the same
    way the churn label is drawn. Two identical calls can disagree - that is the
    point of a simulator.
    """
    if action not in ACTIONS:
        raise ValueError(f"unknown action {action!r}, expected one of {ACTIONS}")

    if config is None:
        from .profiles import load_config

        config = load_config()
    root = root or PROJECT_ROOT
    table = _load_responsiveness(str(root / config["dataset"]["responsiveness_csv"]))

    if customer_id not in table.index:
        raise KeyError(f"unknown customer_id {customer_id!r}")

    rng = rng or np.random.default_rng()
    return bool(rng.random() < table.loc[customer_id, action])
