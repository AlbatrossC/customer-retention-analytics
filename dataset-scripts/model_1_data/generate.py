"""Sandbox Bank - generate the Model 1 training dataset.

Runs every stage end to end and writes, under data/model_1_training_data/,
customers.csv (53,040 rows) plus the hidden responsiveness.csv.

    python dataset-scripts/model_1_data/generate.py

Stage order matters and is not interchangeable:

    1. profiles          static customers
    2. service shock     the hidden second-pathway group
    3. behaviour         six autocorrelated snapshots each
    4. latent pressure   hidden complaint pressure, BEFORE the label
    5. label             score, sigmoid, weighted coin flip
    6. service columns   observed complaints, AFTER the label
    7. truncate          churn is absorbing, so a panel stops at its churn row
    8. responsiveness    hidden intervention response

Reruns are byte identical: every draw comes from a named stream spawned off
SeedSequence(seed.master) in config.yaml.
"""

from __future__ import annotations

from pathlib import Path

import numpy as np
import pandas as pd

from src.behaviour import LATENT_STATE_COLUMN, assign_drift_states, build_panel
from src.label import assign_labels, truncate_at_churn
from src.profiles import PROJECT_ROOT, build_profiles, load_config, make_streams
from src.service import (
    SERVICE_SHOCK_COLUMN,
    assign_service_shock,
    build_latent_pressure,
    build_service_columns,
    load_complaint_texts,
)

ROOT = PROJECT_ROOT

# Section 7 order. customer_yearly_value and loyalty are carried in the CSV but
# appear in the section 8 DROP list, so they never reach the feature matrix.
COLUMN_ORDER = [
    "customer_id",
    "customer_name",
    "snapshot_date",
    "age",
    "tenure_months",
    "customer_segment",
    "income_regularity",
    "customer_yearly_value",
    "loyalty",
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
    "complaint_text",
    "branch_code",
    "card_colour",
    "churn_flag",
]

FLOAT_COLUMNS = [
    "customer_yearly_value",
    "loyalty",
    "balance_change_30d",
    "transaction_change_30d",
    "card_spend_change_30d",
    "app_login_change_30d",
    "salary_missing_days",
    "external_transfer_change_30d",
    "upi_share_of_spend",
    "avg_resolution_time_hrs",
]


def build_dataset(
    config: dict, streams: dict[str, np.random.Generator], root: Path = ROOT
) -> dict:
    """Run every generation stage. Returns the panel and the hidden frames."""
    profiles = build_profiles(config, streams)
    drift = assign_drift_states(profiles, config, streams)
    shock = assign_service_shock(profiles, drift, config, streams)

    panel = build_panel(profiles, drift, shock, config, streams)

    # Before the label: the hidden complaint pressure that enters the score.
    latent_pressure = build_latent_pressure(panel, shock, config, streams)
    panel = assign_labels(panel, latent_pressure, config, streams)

    # After the label: the observed service columns, drawn from that pressure.
    texts = load_complaint_texts(config, root=root)
    panel = build_service_columns(panel, latent_pressure, config, streams, texts=texts)

    # Drawn on the full panel and truncated afterwards, so that adding or
    # removing truncation never shifts any stream's sequence of draws.
    panel["_latent_pressure"] = latent_pressure
    panel = truncate_at_churn(panel, config)

    hidden = drift.merge(shock, on="customer_id")
    return {
        "panel": panel,
        "profiles": profiles,
        "hidden": hidden,
        "latent_pressure": panel["_latent_pressure"].to_numpy(),
    }


def to_output_frame(panel: pd.DataFrame, config: dict) -> pd.DataFrame:
    """Select and round the columns that go to disk, in section 7 order."""
    frame = panel[COLUMN_ORDER].copy()
    precision = config["dataset"]["float_precision"]
    for column in FLOAT_COLUMNS:
        frame[column] = frame[column].round(precision)
    return frame


def main() -> int:
    config = load_config()
    streams = make_streams(config)

    built = build_dataset(config, streams)
    panel = built["panel"]

    from src.interventions import build_responsiveness

    responsiveness = build_responsiveness(
        built["profiles"], panel, built["hidden"], config, streams
    )

    output_path = ROOT / config["dataset"]["output_csv"]
    output_path.parent.mkdir(parents=True, exist_ok=True)
    frame = to_output_frame(panel, config)
    # lineterminator is pinned so the file is byte identical on Windows too.
    frame.to_csv(output_path, index=False, lineterminator="\n")

    responsiveness_path = ROOT / config["dataset"]["responsiveness_csv"]
    responsiveness.to_csv(responsiveness_path, index=False, lineterminator="\n")

    print(f"wrote {output_path}  {len(frame):,} rows x {len(frame.columns)} columns")
    print(f"wrote {responsiveness_path}  {len(responsiveness):,} rows")
    print(f"churn rate {frame['churn_flag'].mean():.4f}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
