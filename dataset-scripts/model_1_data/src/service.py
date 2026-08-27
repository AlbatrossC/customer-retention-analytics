"""Stage 4 - service events, and the second churn pathway.

Ordering and causation. Section 5.4 requires the service columns to be
generated after ``churn_flag`` exists. That is an ordering constraint, not a
causal one: in reality complaints cause churn, not the reverse. So this module
splits into two halves that run either side of the label.

Before the label
    ``assign_service_shock`` picks the second-pathway group and
    ``build_latent_pressure`` draws the hidden complaint pressure that enters
    the churn score in label.py.

After the label
    ``build_service_columns`` draws the observed service columns, primarily
    from that same latent pressure. Conditioning on ``churn_flag`` is kept
    deliberately weak - a feature drawn from the label is leakage and would
    inflate ROC-AUC dishonestly.

Every observed column is a noisy read of the latent pressure, never a
deterministic function of it. Counts pass through Poisson and Binomial draws,
so ``unresolved_complaints`` cannot be inverted back to the latent term. If it
could, that column would recite a score component exactly and we would be back
to the threshold rules section 5.1 forbids.
"""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pandas as pd

from .behaviour import LATENT_STATE_COLUMN
from .profiles import PROJECT_ROOT

LATENT_PRESSURE_COLUMN = "_latent_pressure"
SERVICE_SHOCK_COLUMN = "service_shock"

# Categories whose texts count as a fee complaint, used by the fee_waiver
# responsiveness rule in interventions.py.
FEE_CATEGORY = "fees_charges"


def assign_service_shock(
    profiles: pd.DataFrame,
    drift: pd.DataFrame,
    config: dict,
    streams: dict[str, np.random.Generator],
) -> pd.DataFrame:
    """Pick the second-pathway group.

    A shocked customer takes a service failure and is far more likely to be
    holding a maturing deposit. Where their behaviour is stable or improving,
    that becomes a churn route entirely separate from behavioural decay, with a
    different SHAP profile.

    With ``allow_on_declining`` the shock also fires on declining customers at
    the same base rate, producing an overlap group whose risk comes from both
    routes at once. Gating it to non-declining customers instead makes the two
    pathways perfectly disjoint, which is not how real customers behave.
    """
    cfg = config["service"]["second_pathway"]
    draw = streams["service_shock"].random(len(profiles))
    shock = draw < cfg["share"]
    if not cfg["allow_on_declining"]:
        shock = shock & (drift["drift_state"] != "declining").to_numpy()
    return pd.DataFrame(
        {
            "customer_id": profiles["customer_id"].to_numpy(),
            SERVICE_SHOCK_COLUMN: shock.astype(int),
        }
    )


def _shock_ramp(config: dict, periods: int) -> np.ndarray:
    """Service failure builds over the six snapshots rather than arriving whole."""
    cfg = config["service"]["second_pathway"]
    floor = cfg["ramp_floor"]
    if periods == 1:
        return np.array([1.0])
    return floor + (1.0 - floor) * np.arange(periods) / (periods - 1)


def build_latent_pressure(
    panel: pd.DataFrame,
    shock: pd.DataFrame,
    config: dict,
    streams: dict[str, np.random.Generator],
) -> np.ndarray:
    """Hidden complaint pressure per row. Runs BEFORE the label.

    Two sources, and they are what make the two churn pathways distinct:
    a decaying behaviour state, and the second-pathway service failure.
    """
    cfg = config["service"]["latent_pressure"]
    periods = config["dataset"]["n_snapshots"]

    state = panel[LATENT_STATE_COLUMN].to_numpy()
    lam = cfg["lambda_base"] + cfg["lambda_per_state"] * np.clip(state, 0.0, None)

    shock_flag = (
        panel["customer_id"].map(shock.set_index("customer_id")[SERVICE_SHOCK_COLUMN]).to_numpy()
    )
    ramp = np.tile(_shock_ramp(config, periods), len(panel) // periods)
    lam = lam + shock_flag * config["service"]["second_pathway"]["pressure_lambda"] * ramp

    return np.minimum(streams["label_latent_service"].poisson(lam), cfg["max"])


def load_complaint_texts(config: dict, root: Path | None = None) -> dict:
    """Read the 360 complaint texts, 60 per category."""
    root = root or PROJECT_ROOT
    path = root / config["dataset"]["complaint_texts_json"]
    with open(path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def _pick_complaint_texts(
    panel: pd.DataFrame,
    complaints: np.ndarray,
    config: dict,
    rng: np.random.Generator,
    texts: dict,
) -> tuple[np.ndarray, np.ndarray]:
    """One text per complaining row, preferring texts tagged for the segment."""
    text_cfg = config["service"]["complaint_text"]
    categories = list(text_cfg["categories"])
    weights = np.array([text_cfg["category_weights"][name] for name in categories])
    weights = weights / weights.sum()

    segment = panel["customer_segment"].to_numpy()
    has_loan = panel["has_loan"].to_numpy()

    # Pre-index the pool by (category, segment) so the per-row work is a lookup.
    by_segment: dict[tuple[str, str], list[str]] = {}
    for category in categories:
        entries = texts[category]
        for seg in set(segment):
            fitting = [e["text"] for e in entries if seg in e["segments"]]
            by_segment[(category, seg)] = fitting or [e["text"] for e in entries]

    chosen_category = rng.choice(categories, size=len(panel), p=weights)
    # A customer with no loan does not complain about an EMI.
    loan_only = np.array([category == "loan_emi" for category in chosen_category])
    redraw = loan_only & (has_loan == 0)
    if redraw.any():
        alternatives = [name for name in categories if name != "loan_emi"]
        alt_weights = np.array([text_cfg["category_weights"][name] for name in alternatives])
        alt_weights = alt_weights / alt_weights.sum()
        chosen_category = chosen_category.copy()
        chosen_category[redraw] = rng.choice(
            alternatives, size=int(redraw.sum()), p=alt_weights
        )

    picks = rng.random(len(panel))
    out_text = np.full(len(panel), text_cfg["empty_value"], dtype=object)
    out_category = np.full(len(panel), text_cfg["empty_value"], dtype=object)
    complaining = complaints > 0
    for index in np.flatnonzero(complaining):
        pool = by_segment[(chosen_category[index], segment[index])]
        out_text[index] = pool[int(picks[index] * len(pool))]
        out_category[index] = chosen_category[index]
    return out_text, out_category


def build_service_columns(
    panel: pd.DataFrame,
    latent_pressure: np.ndarray,
    config: dict,
    streams: dict[str, np.random.Generator],
    texts: dict | None = None,
) -> pd.DataFrame:
    """Add the section 4.5 service columns. Runs AFTER the label exists."""
    panel = panel.copy()
    observed = config["service"]["observed"]
    churn = panel["churn_flag"].to_numpy()
    state = np.clip(panel[LATENT_STATE_COLUMN].to_numpy(), 0.0, None)
    latent = latent_pressure.astype(float)

    # complaints_30d - Poisson around the latent pressure. The Poisson noise is
    # what stops the observed count from inverting back to the latent term.
    cfg = observed["complaints"]
    complaint_lambda = (
        cfg["lambda_base"] + cfg["lambda_per_latent"] * latent + cfg["churn_bump"] * churn
    )
    complaints = np.minimum(
        streams["service_complaints"].poisson(complaint_lambda), cfg["max"]
    ).astype(int)

    # unresolved_complaints - a binomial thinning of the complaints actually made,
    # so it can never exceed complaints_30d.
    cfg = observed["unresolved"]
    p_unresolved = np.clip(
        cfg["p_base"] + cfg["p_per_latent"] * latent + cfg["churn_bump"] * churn,
        0.0,
        cfg["p_max"],
    )
    unresolved = streams["service_complaints"].binomial(complaints, p_unresolved).astype(int)

    cfg = observed["failed_transactions"]
    failed_lambda = (
        cfg["lambda_base"]
        + cfg["lambda_per_latent"] * latent
        + cfg["lambda_per_state"] * state
        + cfg["churn_bump"] * churn
    )
    failed = np.minimum(
        streams["service_failed"].poisson(failed_lambda), cfg["max"]
    ).astype(int)

    cfg = observed["resolution_hours"]
    resolution = streams["service_resolution"].normal(
        cfg["base_mean"] + cfg["per_unresolved"] * unresolved + cfg["per_latent"] * latent,
        cfg["sd"],
    )
    resolution = np.clip(resolution, cfg["min"], cfg["max"])
    # Nothing to resolve when nothing was raised.
    resolution = np.where(complaints > 0, resolution, cfg["no_complaint_value"])

    cfg = observed["emi_bounce"]
    p_bounce = np.clip(
        cfg["p_base"]
        + cfg["p_per_latent"] * latent
        + cfg["p_per_state"] * state
        + cfg["churn_bump"] * churn,
        0.0,
        cfg["p_max"],
    )
    emi_bounce = (streams["service_emi"].random(len(panel)) < p_bounce).astype(int)
    # 4.5: only ever fires where has_loan == 1.
    emi_bounce = emi_bounce * panel["has_loan"].to_numpy()

    texts = texts if texts is not None else load_complaint_texts(config)
    complaint_text, complaint_category = _pick_complaint_texts(
        panel, complaints, config, streams["service_text"], texts
    )

    panel["complaints_30d"] = complaints
    panel["unresolved_complaints"] = unresolved
    panel["failed_transactions_30d"] = failed
    panel["avg_resolution_time_hrs"] = resolution
    panel["emi_bounce_30d"] = emi_bounce
    panel["complaint_text"] = complaint_text
    panel["_complaint_category"] = complaint_category
    return panel
