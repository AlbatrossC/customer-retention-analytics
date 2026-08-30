# Devang Local API Test Results

- API URL: `http://127.0.0.1:8001`
- Created at: `2026-08-31T00:35:32`
- Examples tested: `4`
- Health OK: `True`
- Ollama model: `devang-model2-q4`

## Summary

| File | OK | Reason | Urgency | Action | Seconds |
|---|---|---|---|---|---:|
| example_1_input.json | yes | SERVICE_DISSATISFACTION | HIGH | COMPLAINT_ESCALATION | 8.42 |
| example_2_input.json | yes | COMPETITOR_MIGRATION | HIGH | PRODUCT_REVIEW | 2.16 |
| example_3_input.json | yes | PRODUCT_MISMATCH | MEDIUM | RE_ENGAGEMENT | 2.1 |
| example_4_input.json | yes | FINANCIAL_STRESS | HIGH | LOAN_REVIEW | 1.6 |

## Details

### example_1_input.json

- OK: `True`
- Shape errors: `[]`
- Simple output: Reason: SERVICE_DISSATISFACTION | Urgency: HIGH | Action: COMPLAINT_ESCALATION | Why: Service friction is the clearest risk signal here. Complaint escalation fits because complaints_30d=2 and unresolved_complaints=1 indicate the issue is unresolved or operationally serious.

Input:

```json
{
  "customer_context": {
    "age": 39,
    "tenure_months": 48,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "customer_yearly_value": 62000.0,
    "products_count": 4,
    "has_credit_card": 1,
    "has_loan": 0
  },
  "behavior": {
    "days_since_last_transaction": 24,
    "balance_change_30d": -38.5,
    "transaction_change_30d": -28.0,
    "card_spend_change_30d": -18.0,
    "app_login_change_30d": -42.0,
    "salary_missing_days": null,
    "external_transfer_change_30d": 55.0,
    "upi_share_of_spend": 0.58,
    "fd_maturing_in_30d": 0,
    "products_dropped_90d": 1,
    "emi_bounce_30d": 0
  },
  "service_evidence": {
    "complaints_30d": 2,
    "unresolved_complaints": 1,
    "failed_transactions_30d": 1,
    "avg_resolution_time_hrs": 64.0,
    "complaint_text": "Customer says complaint has not been resolved and branch follow-up was delayed"
  },
  "model1": {
    "churn_probability": 0.78,
    "churn_prediction": "Yes",
    "risk_level": "High",
    "top_risk_factors": [
      {
        "factor": "complaints_30d",
        "value": 2
      },
      {
        "factor": "balance_change_30d",
        "value": -38.5
      },
      {
        "factor": "days_since_last_transaction",
        "value": 24
      }
    ]
  },
  "eligible_actions": [
    "SERVICE_RECOVERY",
    "COMPLAINT_ESCALATION",
    "RM_CALLBACK",
    "MONITOR"
  ]
}
```

Response:

```json
{
  "model2": {
    "case_id": null,
    "ok": true,
    "prediction": {
      "evidence": [
        "complaints_30d=2",
        "unresolved_complaints=1",
        "failed_transactions_30d=1",
        "avg_resolution_time_hrs=64.0",
        "complaint_text describes a recent service issue"
      ],
      "primary_reason": "SERVICE_DISSATISFACTION",
      "reasoning_summary": "Service friction is the clearest risk signal here. Complaint escalation fits because complaints_30d=2 and unresolved_complaints=1 indicate the issue is unresolved or operationally serious.",
      "recommended_action": "COMPLAINT_ESCALATION",
      "secondary_reasons": [],
      "urgency": "HIGH"
    },
    "raw_text": "{\"evidence\":[\"complaints_30d=2\",\"unresolved_complaints=1\",\"failed_transactions_30d=1\",\"avg_resolution_time_hrs=64.0\",\"complaint_text describes a recent service issue\"],\"primary_reason\":\"SERVICE_DISSATISFACTION\",\"reasoning_summary\":\"Service friction is the clearest risk signal here. Complaint escalation fits because complaints_30d=2 and unresolved_complaints=1 indicate the issue is unresolved or operationally serious.\",\"recommended_action\":\"COMPLAINT_ESCALATION\",\"secondary_reasons\":[],\"urgency\":\"HIGH\"}",
    "error": null,
    "latency_s": 8.4079,
    "simple_output": "Reason: SERVICE_DISSATISFACTION | Urgency: HIGH | Action: COMPLAINT_ESCALATION | Why: Service friction is the clearest risk signal here. Complaint escalation fits because complaints_30d=2 and unresolved_complaints=1 indicate the issue is unresolved or operationally serious."
  }
}
```

### example_2_input.json

- OK: `True`
- Shape errors: `[]`
- Simple output: Reason: COMPETITOR_MIGRATION | Urgency: HIGH | Action: PRODUCT_REVIEW | Why: The pattern suggests funds or activity may be shifting to another provider. Product review fits because external_transfer_change_30d=72 and balance_change_30d=-22.0 warrant checking if the relationship looks at risk of being passed to a competitor.

Input:

```json
{
  "customer_context": {
    "age": 51,
    "tenure_months": 96,
    "customer_segment": "business",
    "income_regularity": "irregular",
    "customer_yearly_value": 114000.0,
    "products_count": 5,
    "has_credit_card": 1,
    "has_loan": 1
  },
  "behavior": {
    "days_since_last_transaction": 8,
    "balance_change_30d": -22.0,
    "transaction_change_30d": -6.5,
    "card_spend_change_30d": -4.0,
    "app_login_change_30d": -8.0,
    "salary_missing_days": null,
    "external_transfer_change_30d": 72.0,
    "upi_share_of_spend": 0.32,
    "fd_maturing_in_30d": 1,
    "products_dropped_90d": 0,
    "emi_bounce_30d": 0
  },
  "service_evidence": {
    "complaints_30d": 0,
    "unresolved_complaints": 0,
    "failed_transactions_30d": 0,
    "avg_resolution_time_hrs": 0.0,
    "complaint_text": null
  },
  "model1": {
    "churn_probability": 0.64,
    "churn_prediction": "Yes",
    "risk_level": "Medium",
    "top_risk_factors": [
      {
        "factor": "external_transfer_change_30d",
        "value": 72.0
      },
      {
        "factor": "fd_maturing_in_30d",
        "value": 1
      },
      {
        "factor": "balance_change_30d",
        "value": -22.0
      }
    ]
  },
  "eligible_actions": [
    "RM_CALLBACK",
    "PRODUCT_REVIEW",
    "FINANCIAL_GUIDANCE",
    "MONITOR"
  ]
}
```

Response:

```json
{
  "model2": {
    "case_id": null,
    "ok": true,
    "prediction": {
      "evidence": [
        "external_transfer_change_30d=72",
        "balance_change_30d=-22.0"
      ],
      "primary_reason": "COMPETITOR_MIGRATION",
      "reasoning_summary": "The pattern suggests funds or activity may be shifting to another provider. Product review fits because external_transfer_change_30d=72 and balance_change_30d=-22.0 warrant checking if the relationship looks at risk of being passed to a competitor.",
      "recommended_action": "PRODUCT_REVIEW",
      "secondary_reasons": [],
      "urgency": "HIGH"
    },
    "raw_text": "{\"evidence\":[\"external_transfer_change_30d=72\",\"balance_change_30d=-22.0\"],\"primary_reason\":\"COMPETITOR_MIGRATION\",\"reasoning_summary\":\"The pattern suggests funds or activity may be shifting to another provider. Product review fits because external_transfer_change_30d=72 and balance_change_30d=-22.0 warrant checking if the relationship looks at risk of being passed to a competitor.\",\"recommended_action\":\"PRODUCT_REVIEW\",\"secondary_reasons\":[],\"urgency\":\"HIGH\"}",
    "error": null,
    "latency_s": 2.148,
    "simple_output": "Reason: COMPETITOR_MIGRATION | Urgency: HIGH | Action: PRODUCT_REVIEW | Why: The pattern suggests funds or activity may be shifting to another provider. Product review fits because external_transfer_change_30d=72 and balance_change_30d=-22.0 warrant checking if the relationship looks at risk of being passed to a competitor."
  }
}
```

### example_3_input.json

- OK: `True`
- Shape errors: `[]`
- Simple output: Reason: PRODUCT_MISMATCH | Urgency: MEDIUM | Action: RE_ENGAGEMENT | Why: The current banking setup likely does not match the customer's product needs because products_count=2 and customer_yearly_value=26,000 suggest relationship narrowing or a product-fit gap.

Input:

```json
{
  "customer_context": {
    "age": 28,
    "tenure_months": 18,
    "customer_segment": "vendor",
    "income_regularity": "seasonal",
    "customer_yearly_value": 26000.0,
    "products_count": 2,
    "has_credit_card": 0,
    "has_loan": 0
  },
  "behavior": {
    "days_since_last_transaction": 4,
    "balance_change_30d": 3.5,
    "transaction_change_30d": 5.0,
    "card_spend_change_30d": 0.0,
    "app_login_change_30d": -2.0,
    "salary_missing_days": null,
    "external_transfer_change_30d": 4.0,
    "upi_share_of_spend": 0.76,
    "fd_maturing_in_30d": 0,
    "products_dropped_90d": 0,
    "emi_bounce_30d": 0
  },
  "service_evidence": {
    "complaints_30d": 0,
    "unresolved_complaints": 0,
    "failed_transactions_30d": 0,
    "avg_resolution_time_hrs": 0.0,
    "complaint_text": null
  },
  "model1": {
    "churn_probability": 0.18,
    "churn_prediction": "No",
    "risk_level": "Low",
    "top_risk_factors": [
      {
        "factor": "products_count",
        "value": 2
      },
      {
        "factor": "customer_yearly_value",
        "value": 26000.0
      },
      {
        "factor": "app_login_change_30d",
        "value": -2.0
      }
    ]
  },
  "eligible_actions": [
    "MONITOR",
    "RE_ENGAGEMENT",
    "PRODUCT_REVIEW"
  ]
}
```

Response:

```json
{
  "model2": {
    "case_id": null,
    "ok": true,
    "prediction": {
      "evidence": [
        "products_count=2",
        "customer_yearly_value=26,000",
        "app_login_change_30d=-2.0"
      ],
      "primary_reason": "PRODUCT_MISMATCH",
      "reasoning_summary": "The current banking setup likely does not match the customer's product needs because products_count=2 and customer_yearly_value=26,000 suggest relationship narrowing or a product-fit gap.",
      "recommended_action": "RE_ENGAGEMENT",
      "secondary_reasons": [],
      "urgency": "MEDIUM"
    },
    "raw_text": "{\"evidence\":[\"products_count=2\",\"customer_yearly_value=26,000\",\"app_login_change_30d=-2.0\"],\"primary_reason\":\"PRODUCT_MISMATCH\",\"reasoning_summary\":\"The current banking setup likely does not match the customer's product needs because products_count=2 and customer_yearly_value=26,000 suggest relationship narrowing or a product-fit gap.\",\"recommended_action\":\"RE_ENGAGEMENT\",\"secondary_reasons\":[],\"urgency\":\"MEDIUM\"}",
    "error": null,
    "latency_s": 2.0824,
    "simple_output": "Reason: PRODUCT_MISMATCH | Urgency: MEDIUM | Action: RE_ENGAGEMENT | Why: The current banking setup likely does not match the customer's product needs because products_count=2 and customer_yearly_value=26,000 suggest relationship narrowing or a product-fit gap."
  }
}
```

### example_4_input.json

- OK: `True`
- Shape errors: `[]`
- Simple output: Reason: FINANCIAL_STRESS | Urgency: HIGH | Action: LOAN_REVIEW | Why: The observed payment and cash-flow signals are the strongest evidence here. Evidence suggests this because salary_missing_days=12; emi_bounce_30d=1.

Input:

```json
{
  "customer_context": {
    "age": 44,
    "tenure_months": 72,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "customer_yearly_value": 54000.0,
    "products_count": 3,
    "has_credit_card": 1,
    "has_loan": 1
  },
  "behavior": {
    "days_since_last_transaction": 16,
    "balance_change_30d": -12.0,
    "transaction_change_30d": -10.0,
    "card_spend_change_30d": -14.0,
    "app_login_change_30d": -25.0,
    "salary_missing_days": 12,
    "external_transfer_change_30d": 18.0,
    "upi_share_of_spend": 0.45,
    "fd_maturing_in_30d": 0,
    "products_dropped_90d": 0,
    "emi_bounce_30d": 1
  },
  "service_evidence": {
    "complaints_30d": 0,
    "unresolved_complaints": 0,
    "failed_transactions_30d": 0,
    "avg_resolution_time_hrs": 0.0,
    "complaint_text": null
  },
  "model1": {
    "churn_probability": 0.69,
    "churn_prediction": "Yes",
    "risk_level": "High",
    "top_risk_factors": [
      {
        "factor": "salary_missing_days",
        "value": 12
      },
      {
        "factor": "emi_bounce_30d",
        "value": 1
      },
      {
        "factor": "app_login_change_30d",
        "value": -25.0
      }
    ]
  },
  "eligible_actions": [
    "FINANCIAL_GUIDANCE",
    "LOAN_REVIEW",
    "RM_CALLBACK",
    "MONITOR"
  ]
}
```

Response:

```json
{
  "model2": {
    "case_id": null,
    "ok": true,
    "prediction": {
      "evidence": [
        "salary_missing_days=12",
        "emi_bounce_30d=1"
      ],
      "primary_reason": "FINANCIAL_STRESS",
      "reasoning_summary": "The observed payment and cash-flow signals are the strongest evidence here. Evidence suggests this because salary_missing_days=12; emi_bounce_30d=1.",
      "recommended_action": "LOAN_REVIEW",
      "secondary_reasons": [],
      "urgency": "HIGH"
    },
    "raw_text": "{\"evidence\":[\"salary_missing_days=12\",\"emi_bounce_30d=1\"],\"primary_reason\":\"FINANCIAL_STRESS\",\"reasoning_summary\":\"The observed payment and cash-flow signals are the strongest evidence here. Evidence suggests this because salary_missing_days=12; emi_bounce_30d=1.\",\"recommended_action\":\"LOAN_REVIEW\",\"secondary_reasons\":[],\"urgency\":\"HIGH\"}",
    "error": null,
    "latency_s": 1.5991,
    "simple_output": "Reason: FINANCIAL_STRESS | Urgency: HIGH | Action: LOAN_REVIEW | Why: The observed payment and cash-flow signals are the strongest evidence here. Evidence suggests this because salary_missing_days=12; emi_bounce_30d=1."
  }
}
```
