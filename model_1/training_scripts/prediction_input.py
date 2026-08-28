from __future__ import annotations

from datetime import datetime
from typing import Any

import numpy as np
import pandas as pd


RAW_INPUT_FIELDS = {"profile", "monthly_history"}


def is_raw_prediction_input(customer_data: dict) -> bool:
    return bool(RAW_INPUT_FIELDS & set(customer_data))


def normalize_prediction_input(customer_data: dict, features: list[str]) -> dict:
    if not is_raw_prediction_input(customer_data):
        return customer_data

    profile = customer_data.get("profile", {})
    history = customer_data.get("monthly_history", [])
    if not isinstance(profile, dict):
        raise ValueError("Raw prediction input field 'profile' must be an object.")
    if not isinstance(history, list) or not history:
        raise ValueError("Raw prediction input field 'monthly_history' must be a non-empty array.")
    if len(history) > 6:
        raise ValueError("Raw prediction input accepts at most 6 monthly records.")

    sorted_history = sorted(history, key=_month_sort_key)
    latest = sorted_history[-1]
    previous = sorted_history[-2] if len(sorted_history) > 1 else None

    feature_row = {
        "age": _pick("age", latest, profile),
        "tenure_months": _pick("tenure_months", latest, profile),
        "customer_segment": _pick("customer_segment", latest, profile),
        "income_regularity": _pick("income_regularity", latest, profile),
        "products_count": _pick("products_count", latest, profile),
        "has_credit_card": _pick("has_credit_card", latest, profile),
        "has_loan": _pick("has_loan", latest, profile),
        "days_since_last_transaction": _pick("days_since_last_transaction", latest, profile),
        "balance_change_30d": _change_or_existing("balance_change_30d", "balance", latest, previous),
        "transaction_change_30d": _change_or_existing("transaction_change_30d", "transaction_count", latest, previous),
        "card_spend_change_30d": _change_or_existing("card_spend_change_30d", "card_spend", latest, previous),
        "app_login_change_30d": _change_or_existing("app_login_change_30d", "app_logins", latest, previous),
        "salary_missing_days": _pick_optional("salary_missing_days", latest, profile),
        "external_transfer_change_30d": _change_or_existing(
            "external_transfer_change_30d",
            "external_transfer_amount",
            latest,
            previous,
        ),
        "upi_share_of_spend": _upi_share(latest),
        "fd_maturing_in_30d": _pick_default("fd_maturing_in_30d", latest, profile, 0),
        "products_dropped_90d": _pick_default("products_dropped_90d", latest, profile, 0),
        "complaints_30d": _pick_alias("complaints_30d", "complaints", latest, profile, 0),
        "unresolved_complaints": _pick_default("unresolved_complaints", latest, profile, 0),
        "failed_transactions_30d": _pick_alias("failed_transactions_30d", "failed_transactions", latest, profile, 0),
        "avg_resolution_time_hrs": _pick_default("avg_resolution_time_hrs", latest, profile, 0),
        "emi_bounce_30d": _pick_default("emi_bounce_30d", latest, profile, 0),
        "branch_code": _pick("branch_code", latest, profile),
        "card_colour": _pick("card_colour", latest, profile),
    }

    return {feature: feature_row[feature] for feature in features}


def prepare_feature_row(customer_data: dict, metadata: dict, use_category_values: bool = False) -> pd.DataFrame:
    features = metadata["features"]
    categorical_features = metadata["categorical_features"]
    numerical_features = metadata["numerical_features"]
    values = {
        feature: np.nan if customer_data[feature] is None else customer_data[feature]
        for feature in features
    }
    row = pd.DataFrame([values])
    for feature in numerical_features:
        row[feature] = pd.to_numeric(row[feature], errors="raise")
    for feature in categorical_features:
        if use_category_values and "category_values" in metadata:
            dtype = pd.CategoricalDtype(categories=metadata["category_values"][feature])
            row[feature] = row[feature].astype(str).astype(dtype)
        else:
            row[feature] = row[feature].astype("category")
    return row


def _month_sort_key(row: dict) -> datetime:
    value = row.get("snapshot_date") or row.get("month") or row.get("date")
    if value is None:
        return datetime.min
    return datetime.fromisoformat(str(value))


def _pick(field: str, latest: dict, profile: dict) -> Any:
    value = _pick_optional(field, latest, profile)
    if value is None:
        raise ValueError(f"Raw prediction input cannot build required field '{field}'.")
    return value


def _pick_optional(field: str, latest: dict, profile: dict) -> Any:
    if field in latest:
        return latest[field]
    if field in profile:
        return profile[field]
    return None


def _pick_default(field: str, latest: dict, profile: dict, default: Any) -> Any:
    value = _pick_optional(field, latest, profile)
    return default if value is None else value


def _pick_alias(field: str, alias: str, latest: dict, profile: dict, default: Any) -> Any:
    value = _pick_optional(field, latest, profile)
    if value is not None:
        return value
    value = _pick_optional(alias, latest, profile)
    return default if value is None else value


def _change_or_existing(field: str, raw_field: str, latest: dict, previous: dict | None) -> float:
    if field in latest:
        return latest[field]
    if previous is None:
        return 0.0
    current = latest.get(raw_field)
    baseline = previous.get(raw_field)
    if current is None or baseline in (None, 0):
        return 0.0
    return ((float(current) - float(baseline)) / abs(float(baseline))) * 100


def _upi_share(latest: dict) -> float:
    if "upi_share_of_spend" in latest:
        return latest["upi_share_of_spend"]
    upi_spend = latest.get("upi_spend")
    total_spend = latest.get("total_spend")
    if upi_spend is None or total_spend in (None, 0):
        return 0.0
    return float(upi_spend) / float(total_spend)
