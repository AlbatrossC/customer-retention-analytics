import argparse
import hashlib
from pathlib import Path

import numpy as np
import pandas as pd


SCRIPT_DIR = Path(__file__).resolve().parent
MODEL_V2_ROOT = SCRIPT_DIR.parents[1]
REPO_ROOT = SCRIPT_DIR.parents[2]

SOURCE_DATA = MODEL_V2_ROOT / "data" / "customers.csv"
OUTPUT_DATA = MODEL_V2_ROOT / "data" / "customers_model_1_v2.csv"

IDENTITY_COLUMNS = [
    "customer_id",
    "customer_name",
    "prediction_date",
    "target_month",
]
TARGET = "next_month_churn"

PROFILE_FEATURES = [
    "tenure_months",
    "customer_segment",
    "income_regularity",
    "products_count",
    "has_credit_card",
    "has_loan",
]

BEHAVIOR_FEATURES = [
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
]

AVERAGE_FEATURES = [
    "balance_change_30d",
    "transaction_change_30d",
    "card_spend_change_30d",
    "app_login_change_30d",
    "external_transfer_change_30d",
    "upi_share_of_spend",
]

MAX_FEATURES = [
    "days_since_last_transaction",
    "salary_missing_days",
    "avg_resolution_time_hrs",
]

SUM_FEATURES = [
    "fd_maturing_in_30d",
    "products_dropped_90d",
    "complaints_30d",
    "unresolved_complaints",
    "failed_transactions_30d",
    "emi_bounce_30d",
]

TREND_FEATURES = [
    "balance_change_30d",
    "transaction_change_30d",
    "card_spend_change_30d",
    "app_login_change_30d",
    "days_since_last_transaction",
    "external_transfer_change_30d",
    "complaints_30d",
]

RISK_COUNT_RULES = {
    "balance_drop": ("balance_change_30d", lambda value: value < -5),
    "transaction_drop": ("transaction_change_30d", lambda value: value < -5),
    "card_spend_drop": ("card_spend_change_30d", lambda value: value < -5),
    "app_login_drop": ("app_login_change_30d", lambda value: value < -10),
    "external_transfer_rise": ("external_transfer_change_30d", lambda value: value > 20),
    "quiet_customer": ("days_since_last_transaction", lambda value: value >= 10),
    "complaint_month": ("complaints_30d", lambda value: value > 0),
    "unresolved_complaint_month": ("unresolved_complaints", lambda value: value > 0),
    "failed_transaction_month": ("failed_transactions_30d", lambda value: value > 0),
    "product_drop_month": ("products_dropped_90d", lambda value: value > 0),
    "emi_bounce_month": ("emi_bounce_30d", lambda value: value > 0),
}

EXCLUDED_FROM_TRAINING = [
    "customer_id",
    "customer_name",
    "snapshot_date",
    "age",
    "customer_yearly_value",
    "loyalty",
    "complaint_text",
    "branch_code",
    "card_colour",
    "churn_flag",
]


def clean_number(value):
    if pd.isna(value):
        return np.nan
    return float(value)


def slope(values):
    series = pd.Series(values, dtype="float64").dropna()
    if len(series) < 2:
        return 0.0
    x_values = np.arange(len(series), dtype="float64")
    return float(np.polyfit(x_values, series.to_numpy(), 1)[0])


def summarize_window(output, history, suffix):
    for feature in AVERAGE_FEATURES:
        output[f"avg_{feature}_{suffix}"] = clean_number(history[feature].mean())
    for feature in MAX_FEATURES:
        output[f"max_{feature}_{suffix}"] = clean_number(history[feature].max())
    for feature in SUM_FEATURES:
        output[f"sum_{feature}_{suffix}"] = clean_number(history[feature].sum())
    for name, (feature, rule) in RISK_COUNT_RULES.items():
        values = pd.to_numeric(history[feature], errors="coerce")
        output[f"count_{name}_{suffix}"] = int(values.map(lambda value: False if pd.isna(value) else rule(value)).sum())


def latest_vs_history(output, history):
    latest = history.iloc[-1]
    for feature in AVERAGE_FEATURES:
        average_value = history[feature].mean()
        latest_value = latest[feature]
        if pd.isna(average_value) or pd.isna(latest_value):
            output[f"latest_vs_avg_{feature}_available_history"] = 0.0
        else:
            output[f"latest_vs_avg_{feature}_available_history"] = float(latest_value - average_value)


def build_feature_row(history, next_row):
    latest = history.iloc[-1]
    output = {
        "customer_id": latest["customer_id"],
        "customer_name": latest["customer_name"],
        "prediction_date": latest["snapshot_date"].date().isoformat(),
        "target_month": next_row["snapshot_date"].date().isoformat(),
        TARGET: int(next_row["churn_flag"]),
        "months_observed": int(len(history)),
    }

    for feature in PROFILE_FEATURES:
        output[feature] = latest[feature]
    for feature in BEHAVIOR_FEATURES:
        output[f"latest_{feature}"] = latest[feature]

    summarize_window(output, history.tail(3), "3m")
    summarize_window(output, history.tail(6), "6m")
    summarize_window(output, history, "available_history")
    latest_vs_history(output, history)

    for feature in TREND_FEATURES:
        output[f"{feature}_trend_6m"] = slope(history.tail(6)[feature])

    return output


def column_signature(series):
    """Stable fingerprint of a column's values, NaN handled consistently."""
    hashed = pd.util.hash_pandas_object(series, index=False).to_numpy()
    return hashlib.sha1(hashed.tobytes()).hexdigest()


def drop_duplicate_columns(df, protected):
    """Remove feature columns that are exact copies of an earlier column.

    The source panel only spans a handful of months and history is capped at 6
    rows, so every ``*_available_history`` summary comes out byte-identical to
    its ``*_6m`` twin. Feeding both to XGBoost splits each signal's importance
    across duplicate columns, which dilutes column subsampling and smears the
    SHAP attributions that Model 2 turns into retention reasons. Dropping them
    costs no information. This is done by comparing values rather than by
    hardcoding the suffix, so a longer panel keeps the columns automatically.
    """
    first_seen = {}
    duplicates = {}
    for column in df.columns:
        if column in protected:
            continue
        signature = column_signature(df[column])
        original = first_seen.get(signature)
        if original is not None and df[column].equals(df[original]):
            duplicates[column] = original
        else:
            first_seen.setdefault(signature, column)
    if duplicates:
        print(f"Dropping {len(duplicates)} duplicate feature columns:", flush=True)
        for column, original in duplicates.items():
            print(f"  {column} == {original}", flush=True)
    return df.drop(columns=list(duplicates)), duplicates


def build_features(source_path=SOURCE_DATA, output_path=OUTPUT_DATA):
    print(f"Reading source data: {source_path}", flush=True)
    df = pd.read_csv(source_path)
    df["snapshot_date"] = pd.to_datetime(df["snapshot_date"])
    rows = []
    customer_count = df["customer_id"].nunique()

    print(f"Building next-month feature rows for {customer_count:,} customers...", flush=True)
    for customer_index, (_, customer_df) in enumerate(
        df.sort_values(["customer_id", "snapshot_date"]).groupby("customer_id"),
        start=1,
    ):
        customer_df = customer_df.reset_index(drop=True)
        for row_index in range(len(customer_df) - 1):
            history = customer_df.iloc[max(0, row_index - 5) : row_index + 1]
            next_row = customer_df.iloc[row_index + 1]
            rows.append(build_feature_row(history, next_row))
        if customer_index % 1000 == 0:
            print(f"Processed {customer_index:,}/{customer_count:,} customers...", flush=True)

    output_df = pd.DataFrame(rows)
    output_df, _ = drop_duplicate_columns(output_df, protected=set(IDENTITY_COLUMNS) | {TARGET})
    output_path.parent.mkdir(parents=True, exist_ok=True)
    print(f"Writing v2 feature table: {output_path}", flush=True)
    output_df.to_csv(output_path, index=False)
    return output_df


def main():
    parser = argparse.ArgumentParser(description="Build Model 1 v2 next-month training features.")
    parser.add_argument("--source", default=str(SOURCE_DATA), help="Source customers.csv path.")
    parser.add_argument("--output", default=str(OUTPUT_DATA), help="Output v2 CSV path.")
    args = parser.parse_args()

    output_df = build_features(Path(args.source), Path(args.output))
    feature_count = len([c for c in output_df.columns if c not in set(IDENTITY_COLUMNS) | {TARGET}])
    print(f"Wrote {len(output_df):,} rows to {args.output}")
    print(f"Feature columns kept: {feature_count:,}")
    print(f"Positive next_month_churn rows: {int(output_df[TARGET].sum()):,}")


if __name__ == "__main__":
    main()
