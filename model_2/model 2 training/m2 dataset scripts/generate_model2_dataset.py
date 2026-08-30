"""
Model 2 (Retention Intelligence LLM) — Training Dataset Generator
==================================================================

Reads Model 1's training data (customers.csv) and produces two JSONL
files matching the schemas discussed:

  - individual_dataset.jsonl   (~400 examples, one customer each)
  - cohort_dataset.jsonl       (~100 examples, one segment/cluster each)

IMPORTANT ASSUMPTION
---------------------
Model 1 (the actual XGBoost/LightGBM classifier) is not available in this
environment, so `churn_probability` and `top_risk_drivers` below are computed
with a transparent heuristic (a weighted "badness score" per feature,
squashed to 0-1, nudged by the true churn_flag to mimic calibration).

THIS IS A STAND-IN. Before real fine-tuning, replace `compute_model1_output()`
with an actual call to your trained Model 1 + a SHAP explainer
(`shap.TreeExplainer(model).shap_values(X)`), so `top_risk_drivers` reflects
real feature attributions instead of the heuristic used here.

The "why" / "next_actions" text is generated from template + phrase banks
with randomized wording for lexical diversity. Treat this as strong SEED
data: spot-check a sample, and optionally pass each through a local open
LLM (e.g. Llama-3.1-8B via Ollama) with a "paraphrase, keep facts, keep
JSON shape" prompt to add more natural variation before final fine-tuning.
"""

import json
import os
import random
from pathlib import Path

import numpy as np
import pandas as pd

random.seed(42)
np.random.seed(42)

SCRIPT_DIR = Path(__file__).resolve().parent
OUT_DIR = Path(os.environ.get("MODEL2_OUTPUT_DIR", SCRIPT_DIR))

if "MODEL2_CUSTOMERS_CSV" in os.environ:
    SRC = Path(os.environ["MODEL2_CUSTOMERS_CSV"])
else:
    customer_csv_candidates = [
        SCRIPT_DIR / "customers.csv",
        SCRIPT_DIR.parents[1] / "data" / "model_1_training_data" / "customers.csv",
    ]
    SRC = next((path for path in customer_csv_candidates if path.exists()), customer_csv_candidates[0])

# --------------------------------------------------------------------------
# 1. Load data
# --------------------------------------------------------------------------
df = pd.read_csv(SRC)
df["snapshot_date"] = pd.to_datetime(df["snapshot_date"])
df = df.sort_values(["customer_id", "snapshot_date"])

# Features Model 1 is allowed to see (README section 5)
BEHAVIOUR_FEATURES = [
    "days_since_last_transaction", "balance_change_30d", "transaction_change_30d",
    "card_spend_change_30d", "app_login_change_30d", "salary_missing_days",
    "external_transfer_change_30d", "upi_share_of_spend", "fd_maturing_in_30d",
    "products_dropped_90d",
]
SERVICE_FEATURES = [
    "complaints_30d", "unresolved_complaints", "failed_transactions_30d",
    "avg_resolution_time_hrs", "emi_bounce_30d",
]
TREND_FEATURES = [
    "days_since_last_transaction", "balance_change_30d",
    "external_transfer_change_30d", "complaints_30d",
]

# direction: +1 means "higher value = more risk", -1 means "lower value = more risk"
RISK_DIRECTION = {
    "days_since_last_transaction": +1,
    "balance_change_30d": -1,
    "transaction_change_30d": -1,
    "card_spend_change_30d": -1,
    "app_login_change_30d": -1,
    "salary_missing_days": +1,
    "external_transfer_change_30d": +1,
    "upi_share_of_spend": +1,          # high = drifting to fintech
    "fd_maturing_in_30d": +1,
    "products_dropped_90d": +1,
    "complaints_30d": +1,
    "unresolved_complaints": +1,
    "failed_transactions_30d": +1,
    "avg_resolution_time_hrs": +1,
    "emi_bounce_30d": +1,
}

ALL_RISK_FEATURES = list(RISK_DIRECTION.keys())

# --------------------------------------------------------------------------
# 2. Heuristic "badness score" per feature (0-1, min-max normalised) —
#    stand-in for what a real SHAP explainer would give us.
# --------------------------------------------------------------------------
badness = pd.DataFrame(index=df.index)
for feat in ALL_RISK_FEATURES:
    col = df[feat]
    if col.isna().all():
        badness[feat] = 0.0
        continue
    direction = RISK_DIRECTION[feat]
    signed = col * direction  # now "higher = worse" always
    lo, hi = signed.quantile(0.02), signed.quantile(0.98)
    norm = ((signed - lo) / (hi - lo + 1e-9)).clip(0, 1)
    badness[feat] = norm.fillna(0.0)

df["badness_score"] = badness.mean(axis=1)

# Heuristic churn probability: badness + boost if actually churned + noise
noise = np.random.normal(0, 0.05, size=len(df))
raw_prob = 0.05 + 0.75 * df["badness_score"] + 0.15 * df["churn_flag"] + noise
df["churn_probability"] = raw_prob.clip(0.02, 0.97).round(3)


def risk_tier(p):
    if p >= 0.75: return "critical"
    if p >= 0.5: return "high"
    if p >= 0.25: return "medium"
    return "low"


df["risk_tier"] = df["churn_probability"].apply(risk_tier)


MIN_BADNESS_TO_FLAG = 0.35  # below this, a feature isn't really "driving" risk

# Absolute-magnitude floors so quantile-stretched trivial moves (e.g. "card
# spend down 2%") can't masquerade as a top driver just because they sit in
# a compressed tail of the distribution.
MIN_ABS_MAGNITUDE = {
    "days_since_last_transaction": 14,
    "balance_change_30d": 15,
    "transaction_change_30d": 15,
    "card_spend_change_30d": 15,
    "app_login_change_30d": 15,
    "salary_missing_days": 3,
    "external_transfer_change_30d": 20,
    "upi_share_of_spend": 0.5,
    "fd_maturing_in_30d": 1,
    "products_dropped_90d": 1,
    "complaints_30d": 1,
    "unresolved_complaints": 1,
    "failed_transactions_30d": 3,
    "avg_resolution_time_hrs": 48,
    "emi_bounce_30d": 1,
}


def passes_magnitude_floor(feat, value):
    floor = MIN_ABS_MAGNITUDE.get(feat)
    if floor is None or value is None or pd.isna(value):
        return True
    return abs(value) >= floor


def top_risk_drivers_from_scores(score_map, row, k=3):
    """score_map: {feature: badness_score} already computed at the right level."""
    ranked = sorted(score_map.items(), key=lambda kv: kv[1], reverse=True)
    ranked = [
        (f, s) for f, s in ranked
        if s >= MIN_BADNESS_TO_FLAG
        and not pd.isna(row.get(f))
        and passes_magnitude_floor(f, row.get(f))
    ]
    out = []
    for feat, score in ranked[:k]:
        out.append({
            "feature": feat,
            "badness_score": round(float(score), 3),
            "direction": "increases_risk",
        })
    return out


def value_tier(v):
    if v < 25000: return "low"
    if v < 60000: return "medium"
    return "high"


def tenure_band(m):
    if m < 12: return "0-1 years"
    if m < 36: return "1-3 years"
    if m < 84: return "3-7 years"
    return "7+ years"


def products_band(n):
    if n <= 1: return "1"
    if n <= 3: return "2-3"
    return "4+"


def risk_group(row, score_map):
    """score_map: {feature: badness_score} computed at customer (last-snapshot) level."""
    beh_scores = [score_map[f] for f in BEHAVIOUR_FEATURES if not pd.isna(row[f])]
    svc_scores = [score_map[f] for f in SERVICE_FEATURES if not pd.isna(row[f])]
    behaviour_bad = np.mean(beh_scores) if beh_scores else 0.0
    service_bad = np.mean(svc_scores) if svc_scores else 0.0
    b = behaviour_bad > 0.45
    s = service_bad > 0.45
    if b and s: return "both"
    if b: return "behaviour_problem"
    if s: return "service_problem"
    return "neither"


# --------------------------------------------------------------------------
# 3. Build per-customer trend + pick the "current" (last) snapshot
# --------------------------------------------------------------------------
records = []
for cust_id, g in df.groupby("customer_id"):
    g = g.sort_values("snapshot_date")
    last = g.iloc[-1]

    trend = {}
    last3 = g.tail(3)
    for feat in TREND_FEATURES:
        vals = last3[feat].tolist()
        vals = [None if pd.isna(v) else round(float(v), 2) for v in vals]
        trend[feat] = vals

    # crude direction: compare first vs last of the "bad-direction-adjusted" balance/days trend
    bal_vals = [v for v in trend["balance_change_30d"] if v is not None]
    days_vals = [v for v in trend["days_since_last_transaction"] if v is not None]
    if len(bal_vals) >= 2 and len(days_vals) >= 2:
        getting_worse = (bal_vals[-1] < bal_vals[0]) and (days_vals[-1] >= days_vals[0])
        getting_better = (bal_vals[-1] > bal_vals[0]) and (days_vals[-1] <= days_vals[0])
        direction = "declining" if getting_worse else ("improving" if getting_better else "stable")
    else:
        direction = "stable"

    rec = last.to_dict()
    rec["customer_id"] = cust_id
    rec["trend"] = trend
    rec["trend_direction"] = direction
    rec["n_months_observed"] = len(g)
    records.append(rec)

cust_df = pd.DataFrame(records)

# Recompute badness at the customer (last-snapshot) level so indices line up
# consistently — this compares each customer's last snapshot against the
# distribution of other customers' last snapshots, which is what Model 1
# would actually see at inference time.
cust_badness = pd.DataFrame(index=cust_df.index)
for feat in ALL_RISK_FEATURES:
    col = cust_df[feat]
    if col.isna().all():
        cust_badness[feat] = 0.0
        continue
    direction = RISK_DIRECTION[feat]
    signed = col * direction
    lo, hi = signed.quantile(0.02), signed.quantile(0.98)
    norm = ((signed - lo) / (hi - lo + 1e-9)).clip(0, 1)
    cust_badness[feat] = norm.fillna(0.0)

cust_df["risk_group"] = [
    risk_group(cust_df.loc[i], cust_badness.loc[i].to_dict())
    for i in cust_df.index
]
cust_df["top_drivers"] = [
    top_risk_drivers_from_scores(cust_badness.loc[i].to_dict(), cust_df.loc[i])
    for i in cust_df.index
]


# --------------------------------------------------------------------------
# 4. Phrase banks for "why" / "next_actions" (seed text generation)
# --------------------------------------------------------------------------
WHY_PHRASES = {
    "days_since_last_transaction": [
        "It has been {v:.0f} days since their last transaction, well beyond their usual pattern.",
        "Transaction gaps have widened to {v:.0f} days, a classic sign of disengagement.",
    ],
    "balance_change_30d": [
        "Account balance has fallen {v:.0f}% in the last 30 days.",
        "Balance is down {v:.0f}% this month, suggesting funds are being withdrawn or moved.",
    ],
    "transaction_change_30d": [
        "Transaction volume has dropped {v:.0f}% compared to their normal activity.",
    ],
    "card_spend_change_30d": [
        "Card spending is down {v:.0f}%, indicating reduced day-to-day engagement.",
    ],
    "app_login_change_30d": [
        "App logins have fallen {v:.0f}%, suggesting the customer is disengaging from digital channels.",
    ],
    "salary_missing_days": [
        "Salary/pension credit is running {v:.0f} days late this cycle.",
    ],
    "external_transfer_change_30d": [
        "Transfers to other banks have spiked {v:.0f}%, a strong signal funds are migrating elsewhere.",
        "Outbound transfers to external banks are up {v:.0f}%, often a precursor to switching banks.",
    ],
    "upi_share_of_spend": [
        "{v:.0%} of spend now goes through UPI, suggesting a drift toward fintech apps over core banking products.",
    ],
    "fd_maturing_in_30d": [
        "A fixed deposit is maturing within 30 days — a classic moment where customers move funds elsewhere.",
    ],
    "products_dropped_90d": [
        "The customer has closed {v:.0f} product(s) in the last 90 days.",
    ],
    "complaints_30d": [
        "{v:.0f} complaint(s) were raised in the last 30 days.",
    ],
    "unresolved_complaints": [
        "{v:.0f} complaint(s) remain unresolved, which is actively damaging trust.",
    ],
    "failed_transactions_30d": [
        "The customer experienced {v:.0f} failed transactions this month, a source of friction.",
    ],
    "avg_resolution_time_hrs": [
        "Complaints are taking an average of {v:.0f} hours to resolve, far slower than ideal.",
    ],
    "emi_bounce_30d": [
        "An EMI bounced this month, indicating cash-flow stress or account dissatisfaction.",
    ],
}

TREND_PHRASES = {
    "declining": [
        "This is not a one-off dip — the customer's key metrics have been getting worse for several consecutive months.",
        "The trend across the last few months shows a steady decline rather than a single bad month.",
    ],
    "improving": [
        "Despite the current flag, the recent trend is actually improving month over month.",
    ],
    "stable": [
        "Values are wobbling around a normal range with no clear worsening trend.",
    ],
}

NEXT_ACTIONS = {
    "days_since_last_transaction": ["rm_call: Schedule a personal check-in call within 2-3 days."],
    "balance_change_30d": ["rate_offer: Offer a rate or fee incentive to encourage funds to stay."],
    "external_transfer_change_30d": ["rm_call: Have a relationship manager reach out before more funds move externally."],
    "salary_missing_days": ["Verify and resolve any delay on the salary/pension credit pipeline."],
    "fd_maturing_in_30d": ["rate_offer: Proactively offer an FD renewal incentive ahead of the maturity date."],
    "complaints_30d": ["complaint_escalation: Escalate open complaints to a priority resolution queue."],
    "unresolved_complaints": ["complaint_escalation: Close out unresolved complaints and follow up personally."],
    "avg_resolution_time_hrs": ["complaint_escalation: Fast-track this customer's complaint handling SLA."],
    "products_dropped_90d": ["rm_call: Understand why products were closed and offer a suited alternative."],
    "emi_bounce_30d": ["rm_call: Check in on affordability and offer restructuring options if needed."],
    "upi_share_of_spend": ["fee_waiver: Offer incentives to route more spend back through bank-issued cards."],
}

FALLBACK_WHY = [
    "No single strong driver stands out — this is a moderate, broad-based risk from several mildly negative signals together.",
]
FALLBACK_ACTION = ["do_nothing: Monitor for now; re-assess next cycle before taking action."]


def fmt_val(feat, row):
    v = row.get(feat)
    if v is None or (isinstance(v, float) and pd.isna(v)):
        return None
    return v


def build_why_and_actions(row):
    why, actions = [], []
    for d in row["top_drivers"]:
        feat = d["feature"]
        v = fmt_val(feat, row)
        if v is None:
            continue
        template = random.choice(WHY_PHRASES.get(feat, []))
        try:
            why.append(template.format(v=v))
        except Exception:
            why.append(template)
        if feat in NEXT_ACTIONS:
            actions.append(random.choice(NEXT_ACTIONS[feat]) if isinstance(NEXT_ACTIONS[feat], list) else NEXT_ACTIONS[feat])

    if row["risk_tier"] in ("high", "critical"):
        why.append(random.choice(TREND_PHRASES[row["trend_direction"]]))

    complaint = row.get("complaint_text")
    if isinstance(complaint, str) and complaint.strip():
        why.append(f'The customer explicitly raised a service issue: "{complaint.strip()}"')
        actions.append("complaint_escalation: Directly address the specific issue the customer raised.")

    if not why:
        why = FALLBACK_WHY.copy()
    if not actions:
        actions = FALLBACK_ACTION.copy()

    # de-duplicate while preserving order, cap length
    why = list(dict.fromkeys(why))[:5]
    actions = list(dict.fromkeys(actions))[:4]
    return why, actions


# --------------------------------------------------------------------------
# 5. Build INDIVIDUAL examples (~400), stratified by risk_group
# --------------------------------------------------------------------------
TARGET_INDIVIDUAL = 400
TARGET_SHARE = {"behaviour_problem": 0.40, "service_problem": 0.25, "both": 0.20, "neither": 0.15}

individual_examples = []
for grp, share in TARGET_SHARE.items():
    pool = cust_df[cust_df["risk_group"] == grp]
    n = min(len(pool), round(TARGET_INDIVIDUAL * share))
    sampled = pool.sample(n=n, random_state=42) if n > 0 else pool
    for _, row in sampled.iterrows():
        why, actions = build_why_and_actions(row)

        salary_val = row["salary_missing_days"]
        salary_val = None if pd.isna(salary_val) else round(float(salary_val), 1)

        example = {
            "type": "individual",
            "customer_id": row["customer_id"],
            "snapshot_date": row["snapshot_date"].strftime("%Y-%m-%d"),
            "model1_output": {
                "churn_probability": round(float(row["churn_probability"]), 3),
                "risk_tier": row["risk_tier"],
                "top_risk_drivers": row["top_drivers"],
            },
            "customer_profile": {
                "segment": row["customer_segment"],
                "income_regularity": row["income_regularity"],
                "tenure_months": int(row["tenure_months"]),
                "age": int(row["age"]),
                "products_count": int(row["products_count"]),
                "has_credit_card": int(row["has_credit_card"]),
                "has_loan": int(row["has_loan"]),
                "value_tier": value_tier(row["customer_yearly_value"]),
            },
            "current_snapshot": {
                "days_since_last_transaction": int(row["days_since_last_transaction"]),
                "balance_change_30d": round(float(row["balance_change_30d"]), 2),
                "transaction_change_30d": round(float(row["transaction_change_30d"]), 2),
                "card_spend_change_30d": round(float(row["card_spend_change_30d"]), 2),
                "app_login_change_30d": round(float(row["app_login_change_30d"]), 2),
                "salary_missing_days": salary_val,
                "external_transfer_change_30d": round(float(row["external_transfer_change_30d"]), 2),
                "upi_share_of_spend": round(float(row["upi_share_of_spend"]), 3),
                "fd_maturing_in_30d": int(row["fd_maturing_in_30d"]),
                "products_dropped_90d": int(row["products_dropped_90d"]),
                "complaints_30d": int(row["complaints_30d"]),
                "unresolved_complaints": int(row["unresolved_complaints"]),
                "failed_transactions_30d": int(row["failed_transactions_30d"]),
                "avg_resolution_time_hrs": round(float(row["avg_resolution_time_hrs"]), 1),
                "emi_bounce_30d": int(row["emi_bounce_30d"]),
            },
            "trend_last_3_months": {**row["trend"], "overall_direction": row["trend_direction"]},
            "recent_complaint_text": row["complaint_text"] if isinstance(row["complaint_text"], str) and row["complaint_text"].strip() else None,
            "risk_group": row["risk_group"],
            "output": {"why": why, "next_actions": actions},
        }
        individual_examples.append(example)

random.shuffle(individual_examples)
print(f"Individual examples built: {len(individual_examples)}")

# --------------------------------------------------------------------------
# 6. Build COHORT examples (~100) by clustering on segment / risk_group /
#    tenure band / trend direction / value tier
# --------------------------------------------------------------------------
cust_df["tenure_band"] = cust_df["tenure_months"].apply(tenure_band)
cust_df["value_tier"] = cust_df["customer_yearly_value"].apply(value_tier)
cust_df["products_band"] = cust_df["products_count"].apply(products_band)

cluster_cols = ["customer_segment", "risk_group", "tenure_band", "trend_direction", "value_tier"]
clusters = cust_df.groupby(cluster_cols)

cohort_examples = []
cid = 0
for keys, g in clusters:
    if len(g) < 8:
        continue  # too small to call a "cohort"
    cid += 1
    segment, rgroup, tband, tdir, vtier = keys

    agg = {
        "avg_days_since_last_transaction": round(g["days_since_last_transaction"].mean(), 1),
        "avg_balance_change_30d": round(g["balance_change_30d"].mean(), 1),
        "avg_external_transfer_change_30d": round(g["external_transfer_change_30d"].mean(), 1),
        "pct_with_complaints": round((g["complaints_30d"] > 0).mean(), 2),
        "pct_fd_maturing_30d": round(g["fd_maturing_in_30d"].mean(), 2),
        "pct_unresolved_complaints": round((g["unresolved_complaints"] > 0).mean(), 2),
    }

    # Build a pseudo-row to reuse the phrase banks for cohort-level "why"
    pseudo = {
        "top_drivers": [],
        "risk_tier": risk_tier(g["churn_probability"].mean()),
        "trend_direction": tdir,
        "complaint_text": None,
        "days_since_last_transaction": agg["avg_days_since_last_transaction"],
        "balance_change_30d": agg["avg_balance_change_30d"],
        "external_transfer_change_30d": agg["avg_external_transfer_change_30d"],
    }
    # top 2 shared drivers = whichever aggregate signals look worst
    driver_candidates = []
    if agg["avg_balance_change_30d"] < -10:
        driver_candidates.append("balance_change_30d")
    if agg["avg_days_since_last_transaction"] > 12:
        driver_candidates.append("days_since_last_transaction")
    if agg["avg_external_transfer_change_30d"] > 15:
        driver_candidates.append("external_transfer_change_30d")
    if agg["pct_with_complaints"] > 0.2:
        driver_candidates.append("complaints_30d")
    if agg["pct_fd_maturing_30d"] > 0.2:
        driver_candidates.append("fd_maturing_in_30d")
    pseudo["top_drivers"] = [{"feature": f, "badness_score": 0.0, "direction": "increases_risk"} for f in driver_candidates[:3]]
    pseudo["complaints_30d"] = 1 if agg["pct_with_complaints"] > 0.2 else 0

    why, actions = build_why_and_actions(pseudo)
    why = [w.replace("The customer", "This group of customers").replace("their", "their") for w in why]
    why.insert(0, f"This cohort of {len(g)} {segment} customers shares a {rgroup.replace('_', ' ')} pattern.")

    cohort_examples.append({
        "type": "cohort",
        "cohort_id": f"COHORT_{cid:03d}",
        "cohort_size": int(len(g)),
        "model1_output": {
            "avg_churn_probability": round(float(g["churn_probability"].mean()), 3),
            "shared_risk_drivers": driver_candidates[:3],
        },
        "segment_profile": {
            "customer_segment": segment,
            "tenure_band": tband,
            "value_tier": vtier,
            "products_band": g["products_band"].mode().iloc[0],
        },
        "aggregate_behaviour": agg,
        "dominant_trend": tdir,
        "risk_group": rgroup,
        "output": {"why": why, "next_actions": actions},
    })

random.shuffle(cohort_examples)
cohort_examples = cohort_examples[:100]
print(f"Cohort examples built: {len(cohort_examples)}")

# --------------------------------------------------------------------------
# 7. Write outputs
# --------------------------------------------------------------------------
os.makedirs(OUT_DIR, exist_ok=True)

def write_jsonl(path, records):
    with open(path, "w") as f:
        for r in records:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")

write_jsonl(OUT_DIR / "individual_dataset.jsonl", individual_examples)
write_jsonl(OUT_DIR / "cohort_dataset.jsonl", cohort_examples)
write_jsonl(OUT_DIR / "model2_training_data.jsonl", individual_examples + cohort_examples)

print("Done.")
print(f"Total combined examples: {len(individual_examples) + len(cohort_examples)}")
