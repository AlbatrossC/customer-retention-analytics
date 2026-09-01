"""
Generate a sample SQLite database with 10,000 synthetic customers.

Creates:
  - customers table (profile data)
  - customer_snapshots table (6 monthly behavioral snapshots per customer)
  - model1_predictions table (XGBoost churn predictions)
  - model1_risk_factors table (top 5 SHAP-like risk factors per customer)
  - model2_predictions table (LLM retention reason analysis)
  - model2_evidence table (evidence items per customer)
  - customer_clusters table (K-Means cluster assignment)
  - cluster_profiles table (cluster-level feature averages)

Usage:
    python database/generate_sample_db.py
"""

import json
import math
import os
import random
import sqlite3
import sys
from pathlib import Path

import numpy as np
import pandas as pd
from faker import Faker

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
ROOT = Path(__file__).resolve().parents[1]
DB_DIR = ROOT / "database"
DB_PATH = DB_DIR / "sample_customer_retention.db"
SCHEMA_PATH = DB_DIR / "schema.sql"

# ---------------------------------------------------------------------------
# Constants — Approved Model 1 v2 features (from model_metadata_v2.json)
# ---------------------------------------------------------------------------
SEGMENTS = ["salary", "pension", "farmer", "vendor", "business"]
SEGMENT_WEIGHTS = [0.35, 0.15, 0.20, 0.15, 0.15]
INCOME_REGULARITY = ["regular", "irregular", "seasonal"]
CARD_COLOURS = ["blue", "silver", "gold", "platinum"]
CARD_WEIGHTS = [0.40, 0.30, 0.20, 0.10]

# Model 2 approved values
APPROVED_REASONS = [
    "SERVICE_DISSATISFACTION", "COMPETITOR_MIGRATION", "FEE_DISSATISFACTION",
    "LOW_ENGAGEMENT", "PRODUCT_MISMATCH", "DIGITAL_FRICTION",
    "FINANCIAL_STRESS", "LIFE_STAGE_CHANGE", "TEMPORARY_SEASONAL_CHANGE", "UNKNOWN",
]
APPROVED_ACTIONS = [
    "MONITOR", "SERVICE_RECOVERY", "COMPLAINT_ESCALATION", "FEE_WAIVER_REVIEW",
    "RM_CALLBACK", "PRODUCT_REVIEW", "CARD_REVIEW", "LOAN_REVIEW",
    "RE_ENGAGEMENT", "FINANCIAL_GUIDANCE",
]
APPROVED_URGENCY = ["LOW", "MEDIUM", "HIGH"]

# Actionable features for risk factor generation (blocked columns excluded)
ACTIONABLE_FEATURE_POOL = [
    "latest_days_since_last_transaction",
    "latest_balance_change_30d",
    "latest_transaction_change_30d",
    "latest_card_spend_change_30d",
    "latest_app_login_change_30d",
    "latest_salary_missing_days",
    "latest_external_transfer_change_30d",
    "latest_upi_share_of_spend",
    "latest_fd_maturing_in_30d",
    "latest_products_dropped_90d",
    "latest_complaints_30d",
    "latest_unresolved_complaints",
    "latest_failed_transactions_30d",
    "latest_avg_resolution_time_hrs",
    "latest_emi_bounce_30d",
    "avg_balance_change_30d_3m",
    "avg_transaction_change_30d_3m",
    "sum_complaints_30d_3m",
    "sum_failed_transactions_30d_3m",
    "avg_balance_change_30d_6m",
    "avg_transaction_change_30d_6m",
    "sum_complaints_30d_6m",
    "sum_failed_transactions_30d_6m",
    "balance_change_30d_trend_6m",
    "transaction_change_30d_trend_6m",
    "days_since_last_transaction_trend_6m",
    "external_transfer_change_30d_trend_6m",
    "complaints_30d_trend_6m",
    "latest_vs_avg_balance_change_30d_available_history",
    "latest_vs_avg_upi_share_of_spend_available_history",
]

# Human-friendly labels for risk factors
FACTOR_MESSAGES = {
    "latest_days_since_last_transaction": "Customer has been inactive for an extended period.",
    "latest_balance_change_30d": "Significant balance decrease in the last 30 days.",
    "latest_transaction_change_30d": "Transaction frequency has declined sharply.",
    "latest_card_spend_change_30d": "Card spending has dropped significantly.",
    "latest_app_login_change_30d": "Mobile/internet banking engagement has decreased.",
    "latest_salary_missing_days": "Salary credit has been delayed or missing.",
    "latest_external_transfer_change_30d": "Increased fund transfers to external banks.",
    "latest_upi_share_of_spend": "High proportion of spending through third-party UPI apps.",
    "latest_fd_maturing_in_30d": "Fixed deposit maturing soon — retention risk window.",
    "latest_products_dropped_90d": "Customer has dropped banking products recently.",
    "latest_complaints_30d": "Recent service complaints filed.",
    "latest_unresolved_complaints": "Unresolved complaints are pending resolution.",
    "latest_failed_transactions_30d": "Multiple failed transactions in the past month.",
    "latest_avg_resolution_time_hrs": "Slow complaint resolution time experienced.",
    "latest_emi_bounce_30d": "EMI payments have bounced recently.",
    "avg_balance_change_30d_3m": "Average balance has been declining over 3 months.",
    "avg_transaction_change_30d_3m": "Transaction activity declining over 3 months.",
    "sum_complaints_30d_3m": "Accumulated complaints over the past 3 months.",
    "sum_failed_transactions_30d_3m": "Persistent transaction failures over 3 months.",
    "avg_balance_change_30d_6m": "Long-term balance erosion over 6 months.",
    "avg_transaction_change_30d_6m": "Sustained transaction decline over 6 months.",
    "sum_complaints_30d_6m": "Frequent complaints over the past 6 months.",
    "sum_failed_transactions_30d_6m": "Recurring transaction failures over 6 months.",
    "balance_change_30d_trend_6m": "Balance trajectory trending downward over 6 months.",
    "transaction_change_30d_trend_6m": "Transaction volume trending downward over 6 months.",
    "days_since_last_transaction_trend_6m": "Increasing gaps between transactions over 6 months.",
    "external_transfer_change_30d_trend_6m": "External transfer outflow trending upward.",
    "complaints_30d_trend_6m": "Complaint frequency trending upward over 6 months.",
    "latest_vs_avg_balance_change_30d_available_history": "Recent balance change worse than historical average.",
    "latest_vs_avg_upi_share_of_spend_available_history": "UPI spend share has shifted above historical average.",
}

# Clustering features (top behavioral signals from Model 1 v2)
CLUSTERING_FEATURES = [
    "balance_change_30d",
    "transaction_change_30d",
    "days_since_last_transaction",
    "external_transfer_change_30d",
    "complaints_30d",
    "app_login_change_30d",
    "card_spend_change_30d",
    "failed_transactions_30d",
    "unresolved_complaints",
    "emi_bounce_30d",
]

# Reasoning summary templates
REASONING_TEMPLATES = {
    "SERVICE_DISSATISFACTION": [
        "Customer has filed multiple complaints recently with slow resolution times. Service quality issues are the primary driver of churn risk. Immediate service recovery is recommended.",
        "Unresolved complaints and failed transactions indicate systemic service issues affecting this customer's experience. Prioritize complaint escalation.",
    ],
    "COMPETITOR_MIGRATION": [
        "Rising external transfers and declining balance suggest the customer is gradually shifting banking activity to a competitor. Proactive engagement needed.",
        "Increased UPI usage through third-party apps combined with outward fund transfers indicate competitive migration pattern.",
    ],
    "FEE_DISSATISFACTION": [
        "Customer segment and transaction patterns suggest sensitivity to banking fees. Recent product drops may be fee-driven.",
        "Declining engagement combined with product cancellations indicates fee-related dissatisfaction. Fee waiver review recommended.",
    ],
    "LOW_ENGAGEMENT": [
        "Customer shows declining app logins, reduced transaction frequency, and increasing days since last activity. Re-engagement campaign recommended.",
        "Prolonged inactivity and minimal digital engagement signal disengagement from banking services.",
    ],
    "PRODUCT_MISMATCH": [
        "Current product portfolio does not align with customer's usage patterns. Product review may reveal better-fit alternatives.",
        "Customer is under-utilizing held products while showing interest in services not currently subscribed to.",
    ],
    "DIGITAL_FRICTION": [
        "Failed transactions and declining app usage suggest digital channel friction. Technical support or UX improvements needed.",
        "Repeated transaction failures coupled with shift to third-party platforms indicate frustration with digital banking experience.",
    ],
    "FINANCIAL_STRESS": [
        "EMI bounces, balance decline, and salary delays indicate financial stress. Financial guidance and possible loan restructuring recommended.",
        "Multiple stress indicators present: declining balance, missed EMI payments, and reduced transaction activity.",
    ],
    "LIFE_STAGE_CHANGE": [
        "Customer profile changes suggest a life stage transition. Products and services may need realignment to new needs.",
        "Behavioral shifts are consistent with a major life change rather than dissatisfaction. Proactive RM callback recommended.",
    ],
    "TEMPORARY_SEASONAL_CHANGE": [
        "Seasonal income pattern detected. Current dip in activity is likely temporary based on income regularity classification.",
        "Customer segment exhibits seasonal variation. Monitor but no immediate intervention required.",
    ],
    "UNKNOWN": [
        "Insufficient signal strength to determine a clear primary reason. Standard monitoring recommended with periodic check-ins.",
        "Customer shows mixed signals. Continue observation and flag for review if patterns persist.",
    ],
}

# Reason-to-action mapping (weighted probabilities)
REASON_ACTION_MAP = {
    "SERVICE_DISSATISFACTION": ["SERVICE_RECOVERY", "COMPLAINT_ESCALATION", "RM_CALLBACK"],
    "COMPETITOR_MIGRATION": ["RM_CALLBACK", "PRODUCT_REVIEW", "RE_ENGAGEMENT"],
    "FEE_DISSATISFACTION": ["FEE_WAIVER_REVIEW", "PRODUCT_REVIEW", "RM_CALLBACK"],
    "LOW_ENGAGEMENT": ["RE_ENGAGEMENT", "RM_CALLBACK", "MONITOR"],
    "PRODUCT_MISMATCH": ["PRODUCT_REVIEW", "CARD_REVIEW", "LOAN_REVIEW"],
    "DIGITAL_FRICTION": ["SERVICE_RECOVERY", "RE_ENGAGEMENT", "MONITOR"],
    "FINANCIAL_STRESS": ["FINANCIAL_GUIDANCE", "LOAN_REVIEW", "RM_CALLBACK"],
    "LIFE_STAGE_CHANGE": ["RM_CALLBACK", "PRODUCT_REVIEW", "MONITOR"],
    "TEMPORARY_SEASONAL_CHANGE": ["MONITOR", "RE_ENGAGEMENT", "RM_CALLBACK"],
    "UNKNOWN": ["MONITOR", "RM_CALLBACK", "RE_ENGAGEMENT"],
}


fake = Faker("en_IN")
Faker.seed(42)
np.random.seed(42)
random.seed(42)


# ---------------------------------------------------------------------------
# Generators
# ---------------------------------------------------------------------------

def generate_customer_id(index: int) -> str:
    return f"C{10000 + index}"


def generate_customers(n: int = 10000) -> pd.DataFrame:
    """Generate n customer profiles."""
    print(f"Generating {n:,} customer profiles...", flush=True)
    rows = []
    for i in range(n):
        segment = random.choices(SEGMENTS, weights=SEGMENT_WEIGHTS, k=1)[0]
        tenure = random.randint(3, 240)

        # Income regularity correlates with segment
        if segment == "farmer":
            income_reg = random.choices(INCOME_REGULARITY, weights=[0.2, 0.3, 0.5], k=1)[0]
        elif segment == "salary":
            income_reg = random.choices(INCOME_REGULARITY, weights=[0.85, 0.10, 0.05], k=1)[0]
        elif segment == "pension":
            income_reg = random.choices(INCOME_REGULARITY, weights=[0.90, 0.08, 0.02], k=1)[0]
        else:
            income_reg = random.choices(INCOME_REGULARITY, weights=[0.50, 0.35, 0.15], k=1)[0]

        products = random.choices([1, 2, 3, 4, 5], weights=[0.15, 0.30, 0.30, 0.15, 0.10], k=1)[0]

        rows.append({
            "customer_id": generate_customer_id(i),
            "customer_name": fake.name(),
            "age": random.randint(21, 72),
            "tenure_months": tenure,
            "customer_segment": segment,
            "income_regularity": income_reg,
            "customer_yearly_value": round(random.gauss(55000, 30000), 2),
            "loyalty": round(random.uniform(0.1, 1.0), 4),
            "products_count": products,
            "has_credit_card": random.choices([0, 1], weights=[0.35, 0.65], k=1)[0],
            "has_loan": random.choices([0, 1], weights=[0.55, 0.45], k=1)[0],
            "branch_code": f"BR-{random.randint(100, 200)}",
            "card_colour": random.choices(CARD_COLOURS, weights=CARD_WEIGHTS, k=1)[0],
        })

    df = pd.DataFrame(rows)
    # Clamp yearly value
    df["customer_yearly_value"] = df["customer_yearly_value"].clip(lower=5000, upper=200000).round(2)
    return df


def generate_snapshots(customers_df: pd.DataFrame) -> pd.DataFrame:
    """Generate 6 monthly snapshots for each customer."""
    print("Generating 6-month behavioral snapshots...", flush=True)
    months = pd.date_range("2026-01-01", periods=6, freq="MS")
    all_rows = []

    for _, cust in customers_df.iterrows():
        # Customer-level behavioral baseline (determines risk trajectory)
        base_risk = random.random()  # 0=healthy, 1=high-risk
        churned_month = None

        # ~6% overall churn rate
        if base_risk > 0.94:
            churned_month = random.choice([3, 4, 5])  # churn in month 4, 5, or 6

        for month_idx, month_date in enumerate(months):
            # Behavioral degradation for at-risk customers
            risk_factor = base_risk * (1 + month_idx * 0.1)

            # Days since last transaction
            if risk_factor > 0.8:
                days_since = random.randint(8, 30)
            elif risk_factor > 0.5:
                days_since = random.randint(3, 15)
            else:
                days_since = random.randint(0, 8)

            # Balance change
            if risk_factor > 0.7:
                balance_change = round(random.gauss(-15, 12), 1)
            elif risk_factor > 0.4:
                balance_change = round(random.gauss(-2, 8), 1)
            else:
                balance_change = round(random.gauss(5, 8), 1)

            # Transaction change
            txn_change = round(random.gauss(-risk_factor * 10, 12), 1)

            # Card spend change
            card_spend = round(random.gauss(-risk_factor * 8, 10), 1)

            # App login change
            app_login = round(random.gauss(-risk_factor * 6, 15), 1)

            # Salary missing days
            if cust["income_regularity"] == "seasonal":
                salary_missing = random.choices([0, 3, 7, 14], weights=[0.4, 0.2, 0.2, 0.2], k=1)[0]
            elif risk_factor > 0.6:
                salary_missing = random.choices([0, 2, 5, 10], weights=[0.5, 0.2, 0.2, 0.1], k=1)[0]
            else:
                salary_missing = random.choices([0, 1, 2], weights=[0.8, 0.15, 0.05], k=1)[0]

            # External transfers
            ext_transfer = round(random.gauss(risk_factor * 12, 10), 1)

            # UPI share
            upi_share = round(min(1.0, max(0, random.gauss(0.3 + risk_factor * 0.2, 0.15))), 2)

            # FD maturing
            fd_maturing = 1 if random.random() < 0.05 else 0

            # Products dropped
            products_dropped = 0
            if risk_factor > 0.7 and random.random() < 0.15:
                products_dropped = random.randint(1, 2)

            # Complaints
            if risk_factor > 0.6:
                complaints = random.choices([0, 1, 2, 3], weights=[0.4, 0.3, 0.2, 0.1], k=1)[0]
            else:
                complaints = random.choices([0, 1], weights=[0.85, 0.15], k=1)[0]

            # Unresolved complaints
            unresolved = min(complaints, random.choices([0, 1, 2], weights=[0.6, 0.3, 0.1], k=1)[0])

            # Failed transactions
            if risk_factor > 0.5:
                failed_txns = random.choices([0, 1, 2, 3], weights=[0.5, 0.25, 0.15, 0.1], k=1)[0]
            else:
                failed_txns = random.choices([0, 1], weights=[0.9, 0.1], k=1)[0]

            # Resolution time
            avg_resolution = round(random.gauss(24 + risk_factor * 20, 10), 1) if complaints > 0 else 0

            # EMI bounce
            emi_bounce = 0
            if cust["has_loan"] and risk_factor > 0.6:
                emi_bounce = random.choices([0, 1, 2], weights=[0.6, 0.3, 0.1], k=1)[0]

            # Complaint text
            complaint_text = None
            if complaints > 0 and random.random() < 0.6:
                complaint_texts = [
                    "ATM did not dispense cash but amount was debited",
                    "Mobile banking app keeps crashing",
                    "Debit card blocked without notification",
                    "Wrong charges on credit card statement",
                    "Loan EMI debited twice this month",
                    "Internet banking password reset not working",
                    "Branch staff was unhelpful and rude",
                    "FD maturity amount not credited on time",
                    "UPI transaction failed but money deducted",
                    "Account statement has incorrect entries",
                    "Credit card reward points not reflected",
                    "Cheque book request pending for weeks",
                    "NEFT transfer delayed by 3 days",
                    "Insurance premium auto-debit failed",
                    "Home loan prepayment not processed",
                ]
                complaint_text = random.choice(complaint_texts)

            # Churn flag
            churn_flag = 0
            if churned_month is not None and month_idx >= churned_month:
                churn_flag = 1

            all_rows.append({
                "customer_id": cust["customer_id"],
                "snapshot_date": month_date.strftime("%Y-%m-%d"),
                "days_since_last_transaction": days_since,
                "balance_change_30d": balance_change,
                "transaction_change_30d": txn_change,
                "card_spend_change_30d": card_spend,
                "app_login_change_30d": app_login,
                "salary_missing_days": salary_missing,
                "external_transfer_change_30d": ext_transfer,
                "upi_share_of_spend": upi_share,
                "fd_maturing_in_30d": fd_maturing,
                "products_dropped_90d": products_dropped,
                "complaints_30d": complaints,
                "unresolved_complaints": unresolved,
                "failed_transactions_30d": failed_txns,
                "avg_resolution_time_hrs": avg_resolution,
                "emi_bounce_30d": emi_bounce,
                "complaint_text": complaint_text,
                "churn_flag": churn_flag,
            })

    return pd.DataFrame(all_rows)


def generate_model1_predictions(customers_df: pd.DataFrame, snapshots_df: pd.DataFrame) -> tuple:
    """Generate synthetic Model 1 v2 predictions with realistic distributions.

    Uses a two-pass approach:
      Pass 1 — compute raw risk signals for every customer.
      Pass 2 — use quantile thresholds to assign risk tiers and map
               churn probabilities within each tier so the final
               distribution is ~21 % High, ~10 % Medium, ~69 % Low.
    """
    print("Generating Model 1 v2 predictions...", flush=True)

    # ------- Pass 1: collect raw risk signals ------- #
    customer_signals = []
    latest_snapshots = {}

    for _, cust in customers_df.iterrows():
        cid = cust["customer_id"]
        cust_snaps = snapshots_df[snapshots_df["customer_id"] == cid].sort_values("snapshot_date")
        latest = cust_snaps.iloc[-1]
        latest_snapshots[cid] = latest

        sig = 0.0
        sig += max(0, latest["days_since_last_transaction"] - 5) * 0.35
        sig += max(0, -latest["balance_change_30d"]) * 0.25
        sig += max(0, -latest["transaction_change_30d"]) * 0.15
        sig += max(0, latest["external_transfer_change_30d"]) * 0.20
        sig += latest["complaints_30d"] * 3.0
        sig += latest["unresolved_complaints"] * 5.0
        sig += latest["failed_transactions_30d"] * 2.0
        sig += latest["emi_bounce_30d"] * 4.0
        sig += max(0, -latest["app_login_change_30d"]) * 0.10
        sig += max(0, latest["salary_missing_days"]) * 0.30
        sig += random.gauss(0, 2)
        sig = max(0, sig)
        customer_signals.append((cid, sig))

    # ------- Quantile thresholds ------- #
    all_signals = np.array([s for _, s in customer_signals])
    # Top 21% → High, next 10% → Medium, bottom 69% → Low
    p_high = np.percentile(all_signals, 79)   # top 21 %
    p_med = np.percentile(all_signals, 69)    # next 10 %

    # ------- Pass 2: assign probabilities & risk factors ------- #
    predictions = []
    risk_factors_all = []

    for cid, sig in customer_signals:
        latest = latest_snapshots[cid]

        if sig >= p_high:
            risk_level = "High"
            raw_prob = round(random.uniform(25, 85) + random.gauss(0, 3), 2)
        elif sig >= p_med:
            risk_level = "Medium"
            raw_prob = round(random.uniform(12, 25) + random.gauss(0, 2), 2)
        else:
            risk_level = "Low"
            raw_prob = round(random.uniform(0.5, 12) + random.gauss(0, 1), 2)

        raw_prob = round(max(0.5, min(98.5, raw_prob)), 2)

        risk_score = round(max(0, min(100, raw_prob * 1.15 + random.gauss(0, 4))), 1)
        churn_prediction = "Yes" if raw_prob >= 18 else "No"

        predictions.append({
            "customer_id": cid,
            "churn_probability": raw_prob,
            "raw_churn_probability": round(raw_prob + random.gauss(0, 2), 2),
            "probability_mode": "sigmoid",
            "risk_score": risk_score,
            "churn_prediction": churn_prediction,
            "risk_level": risk_level,
        })

        # ---- Top-5 risk factors ---- #
        feature_contributions = []
        for feat in ACTIONABLE_FEATURE_POOL:
            contrib = abs(random.gauss(0, 0.05)) * (raw_prob / 50)
            if "balance" in feat and latest.get("balance_change_30d", 0) < -5:
                contrib += abs(latest["balance_change_30d"]) * 0.002
            if "transaction" in feat and latest.get("days_since_last_transaction", 0) > 5:
                contrib += latest["days_since_last_transaction"] * 0.003
            if "complaint" in feat and latest.get("complaints_30d", 0) > 0:
                contrib += latest["complaints_30d"] * 0.02
            if "external_transfer" in feat and latest.get("external_transfer_change_30d", 0) > 10:
                contrib += latest["external_transfer_change_30d"] * 0.001
            if "emi_bounce" in feat and latest.get("emi_bounce_30d", 0) > 0:
                contrib += latest["emi_bounce_30d"] * 0.03
            feature_contributions.append((feat, contrib))

        feature_contributions.sort(key=lambda x: x[1], reverse=True)
        top_5 = feature_contributions[:5]

        for rank, (feat_name, contrib) in enumerate(top_5, start=1):
            base = feat_name.replace("latest_", "")
            val = latest.get(base, round(random.gauss(0, 5), 1))
            if isinstance(val, (np.floating, float)):
                val = round(float(val), 2)
            elif isinstance(val, (np.integer, int)):
                val = int(val)

            risk_factors_all.append({
                "customer_id": cid,
                "factor_rank": rank,
                "factor_name": feat_name,
                "factor_value": val,
                "factor_message": FACTOR_MESSAGES.get(feat_name, feat_name.replace("_", " ").title()),
                "contribution": round(contrib, 4),
            })

    return pd.DataFrame(predictions), pd.DataFrame(risk_factors_all)


def generate_model2_predictions(customers_df: pd.DataFrame, model1_df: pd.DataFrame) -> tuple:
    """Generate synthetic Model 2 Devang predictions."""
    print("Generating Model 2 (Devang) predictions...", flush=True)
    predictions = []
    evidence_all = []

    for _, cust in customers_df.iterrows():
        cid = cust["customer_id"]
        m1 = model1_df[model1_df["customer_id"] == cid].iloc[0]

        risk_level = m1["risk_level"]
        churn_prob = m1["churn_probability"]

        # Primary reason distribution depends on risk level
        if risk_level == "High":
            reason_weights = [0.25, 0.15, 0.10, 0.10, 0.08, 0.10, 0.12, 0.05, 0.02, 0.03]
            urgency = random.choices(APPROVED_URGENCY, weights=[0.05, 0.30, 0.65], k=1)[0]
        elif risk_level == "Medium":
            reason_weights = [0.15, 0.10, 0.12, 0.20, 0.10, 0.08, 0.08, 0.07, 0.05, 0.05]
            urgency = random.choices(APPROVED_URGENCY, weights=[0.15, 0.55, 0.30], k=1)[0]
        else:
            reason_weights = [0.05, 0.05, 0.05, 0.30, 0.05, 0.05, 0.03, 0.05, 0.15, 0.22]
            urgency = random.choices(APPROVED_URGENCY, weights=[0.60, 0.30, 0.10], k=1)[0]

        primary_reason = random.choices(APPROVED_REASONS, weights=reason_weights, k=1)[0]

        # Secondary reasons (0-2 additional)
        remaining_reasons = [r for r in APPROVED_REASONS if r != primary_reason]
        n_secondary = random.choices([0, 1, 2], weights=[0.3, 0.4, 0.3], k=1)[0]
        secondary_reasons = random.sample(remaining_reasons, min(n_secondary, len(remaining_reasons)))

        # Recommended action based on primary reason
        possible_actions = REASON_ACTION_MAP.get(primary_reason, ["MONITOR"])
        recommended_action = random.choice(possible_actions)

        # Reasoning summary
        templates = REASONING_TEMPLATES.get(primary_reason, REASONING_TEMPLATES["UNKNOWN"])
        reasoning_summary = random.choice(templates)

        secondary_str = ",".join(secondary_reasons) if secondary_reasons else None

        predictions.append({
            "customer_id": cid,
            "primary_reason": primary_reason,
            "reasoning_summary": reasoning_summary,
            "recommended_action": recommended_action,
            "urgency": urgency,
            "secondary_reasons": secondary_str,
            "raw_text": None,
        })

        # Generate evidence items (2-4 per customer)
        n_evidence = random.randint(2, 4)
        evidence_pool = [
            f"balance_change_30d={round(random.gauss(-10, 15), 1)}%",
            f"days_since_last_transaction={random.randint(1, 25)}",
            f"complaints_30d={random.randint(0, 3)}",
            f"external_transfer_change_30d={round(random.gauss(5, 15), 1)}%",
            f"failed_transactions_30d={random.randint(0, 3)}",
            f"app_login_change_30d={round(random.gauss(-5, 12), 1)}%",
            f"emi_bounce_30d={random.randint(0, 2)}",
            f"upi_share_of_spend={round(random.uniform(0.1, 0.7), 2)}",
            f"salary_missing_days={random.randint(0, 10)}",
            f"unresolved_complaints={random.randint(0, 2)}",
            f"products_dropped_90d={random.randint(0, 2)}",
            f"churn_probability={round(churn_prob, 1)}%",
            f"risk_level={risk_level}",
        ]
        selected_evidence = random.sample(evidence_pool, min(n_evidence, len(evidence_pool)))
        for rank, ev_text in enumerate(selected_evidence, start=1):
            evidence_all.append({
                "customer_id": cid,
                "evidence_rank": rank,
                "evidence_text": ev_text,
            })

    return pd.DataFrame(predictions), pd.DataFrame(evidence_all)


def perform_clustering(
    customers_df: pd.DataFrame,
    snapshots_df: pd.DataFrame,
    model1_df: pd.DataFrame,
    model2_df: pd.DataFrame,
    n_clusters: int = 5,
) -> tuple:
    """Perform K-Means clustering on top behavioral features."""
    print(f"Performing K-Means clustering (K={n_clusters})...", flush=True)

    from sklearn.cluster import KMeans
    from sklearn.preprocessing import StandardScaler

    # Aggregate latest snapshot features per customer
    latest_snapshots = (
        snapshots_df
        .sort_values(["customer_id", "snapshot_date"])
        .groupby("customer_id")
        .last()
        .reset_index()
    )

    # Build clustering feature matrix
    cluster_data = latest_snapshots[["customer_id"] + CLUSTERING_FEATURES].copy()
    cluster_data = cluster_data.fillna(0)

    # Standardize features
    scaler = StandardScaler()
    feature_matrix = scaler.fit_transform(cluster_data[CLUSTERING_FEATURES])

    # K-Means
    kmeans = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
    cluster_labels = kmeans.fit_predict(feature_matrix)

    cluster_data["cluster_id"] = cluster_labels

    # Generate meaningful cluster labels
    cluster_label_names = [
        "Stable & Engaged",
        "Service-Sensitive",
        "Declining Balance",
        "Digital Migrators",
        "Financial Stress",
    ]

    # Assign labels based on cluster center characteristics
    centers = kmeans.cluster_centers_
    # Sort clusters by average balance_change (first feature) for consistent labeling
    center_balance_order = np.argsort(centers[:, 0])

    label_mapping = {}
    for rank, cluster_idx in enumerate(center_balance_order):
        label_mapping[int(cluster_idx)] = cluster_label_names[min(rank, len(cluster_label_names) - 1)]

    cluster_data["cluster_label"] = cluster_data["cluster_id"].map(label_mapping)

    # Build cluster assignment table
    cluster_assignments = cluster_data[["customer_id", "cluster_id", "cluster_label"]].copy()

    # Build cluster profiles with average features
    cluster_profiles = []
    for cid_val in range(n_clusters):
        members = cluster_data[cluster_data["cluster_id"] == cid_val]
        member_ids = members["customer_id"].tolist()
        m1_members = model1_df[model1_df["customer_id"].isin(member_ids)]
        m2_members = model2_df[model2_df["customer_id"].isin(member_ids)]

        profile = {
            "cluster_id": int(cid_val),
            "cluster_label": label_mapping.get(cid_val, f"Cluster {cid_val}"),
            "customer_count": len(members),
            "avg_churn_probability": round(m1_members["churn_probability"].mean(), 2),
            "avg_risk_score": round(m1_members["risk_score"].mean(), 2) if "risk_score" in m1_members.columns else 0,
        }

        # Average of clustering features
        for feat in CLUSTERING_FEATURES:
            col_name = f"avg_{feat}"
            profile[col_name] = round(members[feat].mean(), 2) if feat in members.columns else 0

        # Risk distribution
        profile["high_risk_count"] = int((m1_members["risk_level"] == "High").sum())
        profile["medium_risk_count"] = int((m1_members["risk_level"] == "Medium").sum())
        profile["low_risk_count"] = int((m1_members["risk_level"] == "Low").sum())

        # Dominant Model 2 outputs
        if len(m2_members) > 0:
            profile["dominant_primary_reason"] = m2_members["primary_reason"].mode().iloc[0] if len(m2_members["primary_reason"].mode()) > 0 else "UNKNOWN"
            profile["dominant_recommended_action"] = m2_members["recommended_action"].mode().iloc[0] if len(m2_members["recommended_action"].mode()) > 0 else "MONITOR"
        else:
            profile["dominant_primary_reason"] = "UNKNOWN"
            profile["dominant_recommended_action"] = "MONITOR"

        cluster_profiles.append(profile)

    return cluster_assignments, pd.DataFrame(cluster_profiles)


# ---------------------------------------------------------------------------
# Database creation
# ---------------------------------------------------------------------------

def create_database(
    customers_df, snapshots_df, model1_df, risk_factors_df,
    model2_df, evidence_df, cluster_assignments_df, cluster_profiles_df,
):
    """Create and populate the SQLite database."""
    print(f"\nCreating database: {DB_PATH}", flush=True)

    if DB_PATH.exists():
        DB_PATH.unlink()
        print(f"  Deleted existing {DB_PATH.name}")

    conn = sqlite3.connect(DB_PATH)
    conn.execute("PRAGMA foreign_keys = ON")
    conn.execute("PRAGMA journal_mode = WAL")

    # Apply base schema
    schema_sql = SCHEMA_PATH.read_text(encoding="utf-8")
    conn.executescript(schema_sql)

    # Create additional cluster tables
    conn.executescript("""
        CREATE TABLE IF NOT EXISTS customer_clusters (
            customer_id TEXT PRIMARY KEY REFERENCES customers(customer_id),
            cluster_id INTEGER NOT NULL,
            cluster_label TEXT
        );

        CREATE TABLE IF NOT EXISTS cluster_profiles (
            cluster_id INTEGER PRIMARY KEY,
            cluster_label TEXT,
            customer_count INTEGER,
            avg_churn_probability REAL,
            avg_risk_score REAL,
            avg_balance_change_30d REAL,
            avg_transaction_change_30d REAL,
            avg_days_since_last_transaction REAL,
            avg_external_transfer_change_30d REAL,
            avg_complaints_30d REAL,
            avg_app_login_change_30d REAL,
            avg_card_spend_change_30d REAL,
            avg_failed_transactions_30d REAL,
            avg_unresolved_complaints REAL,
            avg_emi_bounce_30d REAL,
            high_risk_count INTEGER,
            medium_risk_count INTEGER,
            low_risk_count INTEGER,
            dominant_primary_reason TEXT,
            dominant_recommended_action TEXT
        );

        CREATE INDEX IF NOT EXISTS idx_clusters_cluster_id
            ON customer_clusters(cluster_id);
    """)
    print("  Schema applied with cluster tables")

    # Insert customers
    print("Inserting data...", flush=True)
    customers_df.to_sql("customers", conn, if_exists="append", index=False)
    print(f"  customers: {len(customers_df):,} rows")

    # Insert snapshots
    snap_cols = [c for c in snapshots_df.columns if c != "id"]
    snapshots_df[snap_cols].to_sql("customer_snapshots", conn, if_exists="append", index=False)
    print(f"  customer_snapshots: {len(snapshots_df):,} rows")

    # Insert model1 predictions
    model1_df.to_sql("model1_predictions", conn, if_exists="append", index=False)
    print(f"  model1_predictions: {len(model1_df):,} rows")

    # Insert risk factors
    rf_cols = [c for c in risk_factors_df.columns if c != "id"]
    risk_factors_df[rf_cols].to_sql("model1_risk_factors", conn, if_exists="append", index=False)
    print(f"  model1_risk_factors: {len(risk_factors_df):,} rows")

    # Insert model2 predictions
    model2_df.to_sql("model2_predictions", conn, if_exists="append", index=False)
    print(f"  model2_predictions: {len(model2_df):,} rows")

    # Insert evidence
    ev_cols = [c for c in evidence_df.columns if c != "id"]
    evidence_df[ev_cols].to_sql("model2_evidence", conn, if_exists="append", index=False)
    print(f"  model2_evidence: {len(evidence_df):,} rows")

    # Insert cluster assignments
    cluster_assignments_df.to_sql("customer_clusters", conn, if_exists="append", index=False)
    print(f"  customer_clusters: {len(cluster_assignments_df):,} rows")

    # Insert cluster profiles
    cluster_profiles_df.to_sql("cluster_profiles", conn, if_exists="append", index=False)
    print(f"  cluster_profiles: {len(cluster_profiles_df):,} rows")

    conn.commit()

    # Print counts
    print("\n--- Row Counts ---")
    tables = [
        "customers", "customer_snapshots", "model1_predictions",
        "model1_risk_factors", "model2_predictions", "model2_evidence",
        "customer_clusters", "cluster_profiles",
    ]
    for table in tables:
        count = conn.execute(f"SELECT COUNT(*) FROM {table}").fetchone()[0]
        print(f"  {table}: {count:,}")

    conn.close()
    size_mb = DB_PATH.stat().st_size / (1024 * 1024)
    print(f"\nDone. Database: {DB_PATH} ({size_mb:.1f} MB)")


def main():
    print("=" * 60)
    print("Sample Customer Retention Database Generator")
    print("=" * 60)
    print()

    # 1. Generate customers
    customers_df = generate_customers(10000)
    print(f"  Generated {len(customers_df):,} customers")

    # 2. Generate snapshots
    snapshots_df = generate_snapshots(customers_df)
    print(f"  Generated {len(snapshots_df):,} snapshots")

    # 3. Generate Model 1 predictions
    model1_df, risk_factors_df = generate_model1_predictions(customers_df, snapshots_df)
    print(f"  Generated {len(model1_df):,} Model 1 predictions")
    print(f"  Generated {len(risk_factors_df):,} risk factors")

    # 4. Generate Model 2 predictions
    model2_df, evidence_df = generate_model2_predictions(customers_df, model1_df)
    print(f"  Generated {len(model2_df):,} Model 2 predictions")
    print(f"  Generated {len(evidence_df):,} evidence items")

    # 5. Perform clustering
    cluster_assignments_df, cluster_profiles_df = perform_clustering(
        customers_df, snapshots_df, model1_df, model2_df
    )
    print(f"  Generated {len(cluster_assignments_df):,} cluster assignments")
    print(f"  Generated {len(cluster_profiles_df):,} cluster profiles")

    # Print risk distribution
    print("\n--- Risk Distribution ---")
    risk_counts = model1_df["risk_level"].value_counts()
    for level in ["High", "Medium", "Low"]:
        count = risk_counts.get(level, 0)
        pct = (count / len(model1_df)) * 100
        print(f"  {level}: {count:,} ({pct:.1f}%)")

    # Print cluster summary
    print("\n--- Cluster Summary ---")
    for _, cp in cluster_profiles_df.iterrows():
        print(f"  Cluster {cp['cluster_id']} ({cp['cluster_label']}): "
              f"{cp['customer_count']:,} customers, "
              f"avg churn={cp['avg_churn_probability']:.1f}%, "
              f"reason={cp['dominant_primary_reason']}")

    # 6. Create database
    create_database(
        customers_df, snapshots_df, model1_df, risk_factors_df,
        model2_df, evidence_df, cluster_assignments_df, cluster_profiles_df,
    )


if __name__ == "__main__":
    main()
