"""Stage 2 - six monthly snapshots per customer.

The point of this module is section 5.3: behaviour is autocorrelated. Each
customer gets a hidden drift state assigned once, and a declining customer's six
snapshots get progressively worse month over month rather than showing one
random bad month.

Every observed behaviour column is a readout of a single hidden latent state:

    state[t] = drift_step * t + ar1_carryover[t] + farmer_season_bump[t]
    column   = centre + slope * state[t] + column noise

so the columns move together the way a real customer's behaviour does.
"""

from __future__ import annotations

import numpy as np
import pandas as pd

# Segments with no salary or pension credit to be late. 4.4: salary_missing_days
# is NaN for these, never 0.
NO_SALARY_SEGMENTS = ("farmer", "vendor", "business")

LATENT_STATE_COLUMN = "_latent_state"


def snapshot_dates(config: dict) -> pd.DatetimeIndex:
    """Six monthly dates, 2026-01-01 to 2026-06-01."""
    ds = config["dataset"]
    return pd.date_range(
        start=ds["snapshot_start"],
        periods=ds["n_snapshots"],
        freq=f"{ds['snapshot_freq_months']}MS",
    )


def assign_drift_states(
    profiles: pd.DataFrame, config: dict, streams: dict[str, np.random.Generator]
) -> pd.DataFrame:
    """The hidden drift state, one draw per customer (5.3).

    Assigned outside build_panel so the later stages can condition on it - the
    service-driven second pathway is defined as a subset of the customers who
    are stable or improving on behaviour.
    """
    shares = config["behaviour"]["drift_states"]
    names = list(shares)
    probs = np.array([shares[name] for name in names], dtype=float)
    drift_state = streams["drift_state"].choice(
        names, size=len(profiles), p=probs / probs.sum()
    )
    return pd.DataFrame(
        {"customer_id": profiles["customer_id"].to_numpy(), "drift_state": drift_state}
    )


def _drift_steps(
    config: dict, rng: np.random.Generator, drift_state: np.ndarray
) -> np.ndarray:
    """One step size per customer. Positive means getting worse."""
    drift = config["behaviour"]["drift"]
    mean = np.array([drift[state]["step_mean"] for state in drift_state])
    sd = np.array([drift[state]["step_sd"] for state in drift_state])
    return rng.normal(mean, sd)


def _latent_state(
    config: dict,
    streams: dict[str, np.random.Generator],
    drift_state: np.ndarray,
    segment: np.ndarray,
    dates: pd.DatetimeIndex,
) -> np.ndarray:
    """Hidden per-customer-per-snapshot state, shape (n_customers, n_snapshots)."""
    behaviour = config["behaviour"]
    n, periods = len(drift_state), len(dates)

    step = _drift_steps(config, streams["behaviour_trend"], drift_state)
    # Cumulative, not per-snapshot independent: this is what makes a declining
    # customer trend instead of wobble.
    trend = step[:, None] * np.arange(periods)[None, :]

    rho = behaviour["ar1_rho"]
    shocks = streams["behaviour_noise"].normal(0.0, behaviour["noise_sd"], size=(n, periods))
    carry = np.empty_like(shocks)
    carry[:, 0] = shocks[:, 0]
    for t in range(1, periods):
        carry[:, t] = rho * carry[:, t - 1] + shocks[:, t]

    state = trend + carry

    # Farmers dip in the configured lean season regardless of drift state.
    season = behaviour["farmer_season"]
    in_season = np.isin(dates.month, season["months"])
    bump = streams["farmer_season"].normal(
        season["state_bump"], season["bump_sd"], size=(n, periods)
    )
    is_farmer = (segment == "farmer")[:, None]
    state = state + np.where(is_farmer & in_season[None, :], bump, 0.0)
    return state


def _readout(
    config: dict,
    rng: np.random.Generator,
    state: np.ndarray,
    field: str,
) -> np.ndarray:
    """A percent-change column read off the latent state, then clipped."""
    behaviour = config["behaviour"]
    params = behaviour["fields"][field]
    values = (
        params["centre"]
        + params["slope"] * state
        + rng.normal(0.0, params["noise_sd"], size=state.shape)
    )
    # 4.4: without clipping, trivially small accounts dominate the model.
    return np.clip(values, behaviour["change_clip_min"], behaviour["change_clip_max"])


def build_panel(
    profiles: pd.DataFrame,
    drift: pd.DataFrame,
    shock: pd.DataFrame,
    config: dict,
    streams: dict[str, np.random.Generator],
) -> pd.DataFrame:
    """Expand static profiles into the 60,000 row customer-snapshot panel.

    ``drift`` carries the hidden drift state per customer, ``shock`` the hidden
    service-shock flag. Both are assigned before this call so behaviour can
    condition on them.
    """
    behaviour = config["behaviour"]
    base_cfg = behaviour["baseline"]
    dates = snapshot_dates(config)
    n, periods = len(profiles), len(dates)

    segment = profiles["customer_segment"].to_numpy()
    drift_state = drift["drift_state"].to_numpy()
    service_shock = shock["service_shock"].to_numpy().astype(bool)
    state = _latent_state(config, streams, drift_state, segment, dates)

    baseline_rng = streams["baseline"]
    base_days = baseline_rng.normal(
        base_cfg["days_since_last_transaction_mean"],
        base_cfg["days_since_last_transaction_sd"],
        size=n,
    )
    base_upi = baseline_rng.normal(
        base_cfg["upi_share_mean"], base_cfg["upi_share_sd"], size=n
    )
    base_salary_missing = baseline_rng.normal(
        base_cfg["salary_missing_days_mean"],
        base_cfg["salary_missing_days_sd"],
        size=n,
    )

    days = (
        base_days[:, None]
        + behaviour["days_since_last_transaction_slope"] * state
        + streams["days_since_last_transaction"].normal(
            0.0, behaviour["days_since_last_transaction_noise_sd"], size=(n, periods)
        )
    )
    days = np.clip(
        np.rint(days),
        base_cfg["days_since_last_transaction_min"],
        base_cfg["days_since_last_transaction_max"],
    ).astype(int)

    salary_missing = (
        base_salary_missing[:, None]
        + behaviour["salary_missing_days_slope"] * state
        + streams["salary_missing_days"].normal(
            0.0, behaviour["salary_missing_days_noise_sd"], size=(n, periods)
        )
    )
    salary_missing = np.clip(
        np.rint(salary_missing), 0.0, base_cfg["salary_missing_days_max"]
    )
    # NaN for farmer, vendor and business. Not 0 - they have no expected credit,
    # which is a different statement from "the credit arrived on time".
    has_salary = ~np.isin(segment, NO_SALARY_SEGMENTS)
    salary_missing = np.where(has_salary[:, None], salary_missing, np.nan)

    upi = (
        base_upi[:, None]
        + behaviour["upi_share_slope"] * state
        + streams["upi_share_of_spend"].normal(
            0.0, behaviour["upi_share_noise_sd"], size=(n, periods)
        )
    )
    upi = np.clip(upi, behaviour["upi_share_min"], behaviour["upi_share_max"])

    # The service-driven group is far likelier to be holding a maturing deposit -
    # the classic exit moment for a customer whose behaviour still looks fine.
    fd_p = np.where(
        service_shock,
        config["service"]["second_pathway"]["fd_maturing_p"],
        behaviour["fd_maturing_p"],
    )
    fd = (streams["fd_maturing"].random((n, periods)) < fd_p[:, None]).astype(int)

    dropped_cfg = behaviour["products_dropped"]
    dropped_lambda = dropped_cfg["lambda_base"] + dropped_cfg["lambda_per_state"] * np.clip(
        state, 0.0, None
    )
    dropped = np.minimum(
        streams["products_dropped"].poisson(dropped_lambda), dropped_cfg["max"]
    ).astype(int)

    # Decoys. Drawn once per customer and repeated across their snapshots - a
    # customer does not move branch every month - but with no link to anything
    # else in the dataset. If SHAP ranks either highly, something is broken.
    branch_cfg = config["decoys"]["branch_codes"]
    branch_pool = [
        f"{branch_cfg['prefix']}{branch_cfg['first'] + i}" for i in range(branch_cfg["count"])
    ]
    branch_code = streams["decoy_branch"].choice(branch_pool, size=n)
    card_colour = streams["decoy_card"].choice(config["decoys"]["card_colours"], size=n)

    def repeat(values: np.ndarray) -> np.ndarray:
        return np.repeat(values, periods)

    panel = pd.DataFrame(
        {
            "customer_id": repeat(profiles["customer_id"].to_numpy()),
            "customer_name": repeat(profiles["customer_name"].to_numpy()),
            "snapshot_date": np.tile(dates.strftime("%Y-%m-%d"), n),
            "age": repeat(profiles["age"].to_numpy()),
            "tenure_months": repeat(profiles["tenure_months"].to_numpy()),
            "customer_segment": repeat(segment),
            "income_regularity": repeat(profiles["income_regularity"].to_numpy()),
            "customer_yearly_value": repeat(profiles["customer_yearly_value"].to_numpy()),
            "loyalty": repeat(profiles["loyalty"].to_numpy()),
            "products_count": repeat(profiles["products_count"].to_numpy()),
            "has_credit_card": repeat(profiles["has_credit_card"].to_numpy()),
            "has_loan": repeat(profiles["has_loan"].to_numpy()),
            "days_since_last_transaction": days.ravel(),
            "salary_missing_days": salary_missing.ravel(),
            "upi_share_of_spend": upi.ravel(),
            "fd_maturing_in_30d": fd.ravel(),
            "products_dropped_90d": dropped.ravel(),
            "branch_code": repeat(branch_code),
            "card_colour": repeat(card_colour),
            LATENT_STATE_COLUMN: state.ravel(),
        }
    )

    for field in behaviour["fields"]:
        panel[field] = _readout(config, streams[field], state, field).ravel()

    return panel
