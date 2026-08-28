import json
from pathlib import Path

from llama_cpp import Llama

SCRIPT_DIR = Path(__file__).resolve().parent
MODEL_PATH = SCRIPT_DIR / "model2_retention_0.5b.gguf"

llm = Llama(
    model_path=str(MODEL_PATH),
    n_ctx=2048,
    n_threads=4,
    verbose=False,
)

test_input_1 = {
    "type": "individual",
    "model1_output": {
        "churn_probability": 0.85,
        "risk_tier": "critical",
        "top_risk_drivers": [
            {"feature": "external_transfer_change_30d", "badness_score": 0.78, "direction": "increases_risk"},
            {"feature": "days_since_last_transaction", "badness_score": 0.61, "direction": "increases_risk"},
            {"feature": "balance_change_30d", "badness_score": 0.58, "direction": "increases_risk"}
        ]
    },
    "customer_profile": {
        "segment": "salary",
        "income_regularity": "regular",
        "tenure_months": 61,
        "age": 26,
        "products_count": 3,
        "has_credit_card": 0,
        "has_loan": 1,
        "value_tier": "medium"
    },
    "current_snapshot": {
        "days_since_last_transaction": 19,
        "balance_change_30d": -35.24,
        "transaction_change_30d": -8.0,
        "card_spend_change_30d": -34.0,
        "app_login_change_30d": -12.0,
        "salary_missing_days": 4,
        "external_transfer_change_30d": 44.5,
        "upi_share_of_spend": 0.41,
        "fd_maturing_in_30d": 0,
        "products_dropped_90d": 0,
        "complaints_30d": 0,
        "unresolved_complaints": 0,
        "failed_transactions_30d": 1,
        "avg_resolution_time_hrs": 0.0,
        "emi_bounce_30d": 0
    },
    "trend_last_3_months": {
        "days_since_last_transaction": [16, 18, 19],
        "balance_change_30d": [-9.7, -12.7, -35.2],
        "external_transfer_change_30d": [25.5, 67.1, 44.5],
        "complaints_30d": [2, 0, 0],
        "overall_direction": "declining"
    },
    "recent_complaint_text": "Please confirm my final EMI, the app and passbook show different amounts.",
    "risk_group": "behaviour_problem"
}

output = llm.create_chat_completion(
    messages=[
        {"role": "system", "content": "You are a retention intelligence assistant for a retail bank. Return ONLY a JSON object with exactly these two keys: why and next_actions. Both values must be arrays of short strings. Put the explanation only in why. Put every recommendation only in next_actions. Never combine the keys or put recommendations in why. Example: {\"why\": [\"Risk increased after repeated transaction declines.\"], \"next_actions\": [\"Contact the customer within 24 hours.\", \"Offer transaction support.\"]}"},
        {"role": "user", "content": json.dumps(test_input_1)}
    ],
    response_format={
        "type": "json_object",
        "schema": {
            "type": "object",
            "properties": {
                "why": {"type": "array", "items": {"type": "string"}},
                "next_actions": {"type": "array", "items": {"type": "string"}},
            },
            "required": ["why", "next_actions"],
        },
    },
    temperature=0.3
)
response = output["choices"][0]["message"]["content"]

try:
    result = json.loads(response)
    print("Why:", result.get("why", "Not provided"))
    print("Next actions:")
    for action in result.get("next_actions", []):
        print(f"- {action}")
except json.JSONDecodeError:
    print(response)
