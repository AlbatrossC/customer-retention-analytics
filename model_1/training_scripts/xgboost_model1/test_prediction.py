import json

from predict_churn import predict_churn


SAMPLE_INPUT = {
    "age": 26,
    "tenure_months": 61,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 3,
    "has_credit_card": 0,
    "has_loan": 1,
    "days_since_last_transaction": 21,
    "balance_change_30d": -32,
    "transaction_change_30d": -28,
    "card_spend_change_30d": -35,
    "app_login_change_30d": -40,
    "salary_missing_days": 5,
    "external_transfer_change_30d": 52,
    "upi_share_of_spend": 0.78,
    "fd_maturing_in_30d": 0,
    "products_dropped_90d": 1,
    "complaints_30d": 2,
    "unresolved_complaints": 1,
    "failed_transactions_30d": 3,
    "avg_resolution_time_hrs": 36.5,
    "emi_bounce_30d": 0,
    "branch_code": "BR-135",
    "card_colour": "green",
}


if __name__ == "__main__":
    print(json.dumps(predict_churn(SAMPLE_INPUT), indent=2))
