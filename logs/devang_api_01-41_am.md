# Devang Model 1 -> Model 2 API Test Results

- API URL: `http://127.0.0.1:8001`
- Created at: `2026-08-31T01:43:08`
- Customers tested: `20`
- Source CSV: `model_1_v2\data\customers.csv`
- Health OK: `True`
- Ollama model: `devang-model2-q4`
- Model 1 loaded: `True`

## Summary

| # | Customer | Model 1 risk | Prediction | Reason | Urgency | Action | OK | Seconds |
|---:|---|---:|---|---|---|---|---|---:|
| 1 | Banjeet Balasubramanian (`C10181`) | 24.13 | Yes | SERVICE_DISSATISFACTION | MEDIUM | SERVICE_RECOVERY | yes | 7.94 |
| 2 | Wazir Naik (`C10354`) | 31.27 | Yes | SERVICE_DISSATISFACTION | MEDIUM | SERVICE_RECOVERY | yes | 8.74 |
| 3 | Frado Lad (`C10975`) | 8.28 | No | UNKNOWN | LOW | MONITOR | yes | 5.18 |
| 4 | Dalbir Krish (`C11091`) | 40.44 | Yes | FEE_DISSATISFACTION | HIGH | COMPLAINT_ESCALATION | yes | 2.71 |
| 5 | Abhiram Arora (`C11434`) | 1.43 | No | TEMPORARY_SEASONAL_CHANGE | MEDIUM | RE_ENGAGEMENT | yes | 5.87 |
| 6 | Chatura Bal (`C11472`) | 1.96 | No | TEMPORARY_SEASONAL_CHANGE | LOW | MONITOR | yes | 5.62 |
| 7 | Farhan Bhalla (`C11586`) | 40.95 | Yes | SERVICE_DISSATISFACTION | MEDIUM | SERVICE_RECOVERY | yes | 7.19 |
| 8 | Neel Bir (`C13120`) | 2.06 | No | FINANCIAL_STRESS | MEDIUM | FINANCIAL_GUIDANCE | yes | 3.2 |
| 9 | Bhavani Deep (`C13262`) | 1.97 | No | UNKNOWN | LOW | MONITOR | yes | 5.12 |
| 10 | Sudiksha Khatri (`C16707`) | NA | NA | NA | NA | NA | no | 0.95 |
| 11 | Onveer Setty (`C16974`) | NA | NA | NA | NA | NA | no | 2.04 |
| 12 | Daksha Parekh (`C16975`) | NA | NA | NA | NA | NA | no | 2.02 |
| 13 | Peter Gulati (`C17247`) | NA | NA | NA | NA | NA | no | 2.03 |
| 14 | Bina Ahuja (`C17283`) | 1.83 | No | FEE_DISSATISFACTION | MEDIUM | FEE_WAIVER_REVIEW | yes | 2.91 |
| 15 | Abhiram Mann (`C17720`) | 39.07 | Yes | FINANCIAL_STRESS | MEDIUM | FINANCIAL_GUIDANCE | yes | 13.28 |
| 16 | Peter Sinha (`C18019`) | 4.24 | No | SERVICE_DISSATISFACTION | MEDIUM | COMPLAINT_ESCALATION | yes | 3.89 |
| 17 | Dakshesh Hora (`C18217`) | 2.0 | No | UNKNOWN | LOW | MONITOR | yes | 10.57 |
| 18 | Advika Gera (`C18290`) | 6.28 | No | SERVICE_DISSATISFACTION | HIGH | COMPLAINT_ESCALATION | yes | 4.18 |
| 19 | Yachana Rastogi (`C18690`) | 1.72 | No | UNKNOWN | LOW | MONITOR | yes | 11.81 |
| 20 | Rachita Nanda (`C19885`) | 30.48 | Yes | FINANCIAL_STRESS | HIGH | FINANCIAL_GUIDANCE | yes | 12.07 |

## Details

### Banjeet Balasubramanian (`C10181`)

- OK: `True`
- Shape errors: `[]`
- Simple output: Reason: SERVICE_DISSATISFACTION | Urgency: MEDIUM | Action: SERVICE_RECOVERY | Why: Complaint escalation because complaints_30d=1 and avg_resolution_time_hrs=10.8 suggest a service issue.

Request:

```json
{
  "customer_id": "C10181",
  "customer_name": "Banjeet Balasubramanian",
  "prediction_date": "2026-03-01",
  "snapshot_date": "2026-03-01",
  "target_month": "2026-04-01",
  "profile": {
    "tenure_months": 23,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 1,
    "has_credit_card": 0,
    "has_loan": 0
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 11,
      "balance_change_30d": 5.1734,
      "transaction_change_30d": -1.0903,
      "card_spend_change_30d": -21.5031,
      "app_login_change_30d": 9.6208,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": 2.4449,
      "upi_share_of_spend": 0.8388,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 2,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 4.9441,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-02-01",
      "days_since_last_transaction": 13,
      "balance_change_30d": -5.6099,
      "transaction_change_30d": -25.5776,
      "card_spend_change_30d": 0.839,
      "app_login_change_30d": -18.769,
      "salary_missing_days": 3.0,
      "external_transfer_change_30d": 6.3913,
      "upi_share_of_spend": 1.0,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 0,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 2,
      "avg_resolution_time_hrs": 0.0,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-03-01",
      "days_since_last_transaction": 13,
      "balance_change_30d": -24.8281,
      "transaction_change_30d": -25.18,
      "card_spend_change_30d": -11.614,
      "app_login_change_30d": -3.4032,
      "salary_missing_days": 2.0,
      "external_transfer_change_30d": 45.7368,
      "upi_share_of_spend": 0.9142,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 1,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 10.8355,
      "emi_bounce_30d": 0
    }
  ],
  "customer": {
    "tenure_months": 23,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 1,
    "has_credit_card": 0,
    "has_loan": 0,
    "days_since_last_transaction": 13,
    "balance_change_30d": -24.8281,
    "transaction_change_30d": -25.18,
    "card_spend_change_30d": -11.614,
    "app_login_change_30d": -3.4032,
    "salary_missing_days": 2.0,
    "external_transfer_change_30d": 45.7368,
    "upi_share_of_spend": 0.9142,
    "fd_maturing_in_30d": 0,
    "products_dropped_90d": 1,
    "complaints_30d": 1,
    "unresolved_complaints": 0,
    "failed_transactions_30d": 1,
    "avg_resolution_time_hrs": 10.8355,
    "emi_bounce_30d": 0
  },
  "extra_context": {
    "customer_profile": {
      "segment": "salary",
      "income_regularity": "regular",
      "tenure_months": 23,
      "age": 47,
      "customer_yearly_value": 66805.0492,
      "products_count": 1,
      "has_credit_card": 0,
      "has_loan": 0,
      "value_tier": "medium"
    },
    "recent_complaint_text": "Kindly explain why my UPI was blocked. I received no message."
  }
}
```

Response:

```json
{
  "meta": {
    "endpoint": "/predict/both",
    "served_at": "2026-08-31T01:41:18",
    "elapsed_ms": 7934.12,
    "timings_ms": {
      "model1": 109.36,
      "model2": 7824.59
    },
    "customer_id": "C10181",
    "customer_name": "Banjeet Balasubramanian",
    "snapshot_date": "2026-03-01"
  },
  "model1": {
    "churn_probability": 24.13,
    "raw_churn_probability": 77.42,
    "probability_mode": "sigmoid",
    "risk_score": 71.55,
    "churn_prediction": "Yes",
    "risk_level": "Medium",
    "top_risk_factors": [
      {
        "factor": "latest_days_since_last_transaction",
        "value": 13,
        "message": "Customer has gone longer without transacting.",
        "contribution": 0.3391778767108917
      },
      {
        "factor": "latest_transaction_change_30d",
        "value": -25.18,
        "message": "Transaction activity has been falling across recent months.",
        "contribution": 0.2158239483833313
      },
      {
        "factor": "latest_balance_change_30d",
        "value": -24.8281,
        "message": "Balance has been falling across recent months.",
        "contribution": 0.1520826369524002
      },
      {
        "factor": "transaction_change_30d_trend_6m",
        "value": -12.044850000000002,
        "message": "Transaction activity has been falling across recent months.",
        "contribution": 0.09447312355041504
      },
      {
        "factor": "days_since_last_transaction_trend_6m",
        "value": 0.9999999999999998,
        "message": "Customer has gone longer without transacting.",
        "contribution": 0.07549343258142471
      }
    ]
  },
  "model2_input": {
    "customer_context": {
      "age": 47,
      "tenure_months": 23,
      "customer_segment": "salary",
      "income_regularity": "regular",
      "customer_yearly_value": 66805.0492,
      "products_count": 1,
      "has_credit_card": 0,
      "has_loan": 0
    },
    "behavior": {
      "days_since_last_transaction": 13,
      "balance_change_30d": -24.8281,
      "transaction_change_30d": -25.18,
      "card_spend_change_30d": -11.614,
      "app_login_change_30d": -3.4032,
      "salary_missing_days": 2,
      "external_transfer_change_30d": 45.7368,
      "upi_share_of_spend": 0.9142,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 1,
      "emi_bounce_30d": 0
    },
    "service_evidence": {
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 10.8355,
      "complaint_text": "Kindly explain why my UPI was blocked. I received no message."
    },
    "model1": {
      "churn_probability": 0.2413,
      "churn_prediction": "Yes",
      "risk_level": "Medium",
      "top_risk_factors": [
        {
          "factor": "days_since_last_transaction",
          "value": 13
        },
        {
          "factor": "transaction_change_30d",
          "value": -25.18
        },
        {
          "factor": "balance_change_30d",
          "value": -24.8281
        }
      ]
    },
    "eligible_actions": [
      "FINANCIAL_GUIDANCE",
      "SERVICE_RECOVERY",
      "PRODUCT_REVIEW",
      "RM_CALLBACK",
      "MONITOR"
    ],
    "case_id": "C10181"
  },
  "model2": {
    "case_id": "C10181",
    "ok": true,
    "prediction": {
      "evidence": [
        "complaints_30d=1",
        "unresolved_complaints=0",
        "avg_resolution_time_hrs=10.8",
        "transaction_change_30d=-25.2",
        "balance_change_30d=-24.8"
      ],
      "primary_reason": "SERVICE_DISSATISFACTION",
      "reasoning_summary": "Complaint escalation because complaints_30d=1 and avg_resolution_time_hrs=10.8 suggest a service issue.",
      "recommended_action": "SERVICE_RECOVERY",
      "secondary_reasons": [],
      "urgency": "MEDIUM"
    },
    "warnings": [
      "evidence: 'unresolved_complaints=0' cites a zero/null value, which is not evidence; remove it",
      "reasoning_summary: describes COMPLAINT_ESCALATION but recommended_action is SERVICE_RECOVERY; rewrite the summary around the action you chose"
    ],
    "raw_text": "{\"evidence\":[\"complaints_30d=1\",\"unresolved_complaints=0\",\"avg_resolution_time_hrs=10.8\",\"complaint_text describes a recent service issue without clear escalation-level severity\"],\"primary_reason\":\"SERVICE_DISSATISFACTION\",\"reasoning_summary\":\"Complaint details suggest a service friction without clear escalation-level severity. SERVICE_RECOVERY fits because complaint_text describes a recent service issue without clear escalation-level severity.\",\"recommended_action\":\"SERVICE_RECOVERY\",\"secondary_reasons\":[],\"urgency\":\"MEDIUM\"}",
    "error": null,
    "latency_s": 7.8246,
    "simple_output": "Reason: SERVICE_DISSATISFACTION | Urgency: MEDIUM | Action: SERVICE_RECOVERY | Why: Complaint escalation because complaints_30d=1 and avg_resolution_time_hrs=10.8 suggest a service issue."
  }
}
```

### Wazir Naik (`C10354`)

- OK: `True`
- Shape errors: `[]`
- Simple output: Reason: SERVICE_DISSATISFACTION | Urgency: MEDIUM | Action: SERVICE_RECOVERY | Why: Complaint and service friction signals are mixed or weak. Service recovery fits because complaints_30d=0, unresolved_complaints=0, avg_resolution_time_hrs=0.0, failed_transactions_30d=1 suggest a service issue without a clear escalation level.

Request:

```json
{
  "customer_id": "C10354",
  "customer_name": "Wazir Naik",
  "prediction_date": "2026-06-01",
  "snapshot_date": "2026-06-01",
  "target_month": "2026-07-01",
  "profile": {
    "tenure_months": 6,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 3,
    "has_credit_card": 1,
    "has_loan": 1
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 5,
      "balance_change_30d": -11.0585,
      "transaction_change_30d": -7.5467,
      "card_spend_change_30d": 9.877,
      "app_login_change_30d": 25.5474,
      "salary_missing_days": 4.0,
      "external_transfer_change_30d": 31.9644,
      "upi_share_of_spend": 0.4198,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 1,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 30.2463,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-02-01",
      "days_since_last_transaction": 6,
      "balance_change_30d": -5.8068,
      "transaction_change_30d": 8.4952,
      "card_spend_change_30d": -2.4112,
      "app_login_change_30d": -5.9867,
      "salary_missing_days": 4.0,
      "external_transfer_change_30d": 21.2139,
      "upi_share_of_spend": 0.5238,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 0,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 0.0,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-03-01",
      "days_since_last_transaction": 0,
      "balance_change_30d": 20.5485,
      "transaction_change_30d": 43.7616,
      "card_spend_change_30d": 8.6637,
      "app_login_change_30d": 0.9517,
      "salary_missing_days": 1.0,
      "external_transfer_change_30d": -18.9066,
      "upi_share_of_spend": 0.4616,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 0,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 0.0,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-04-01",
      "days_since_last_transaction": 8,
      "balance_change_30d": 0.4698,
      "transaction_change_30d": -16.9873,
      "card_spend_change_30d": 19.1658,
      "app_login_change_30d": -24.9712,
      "salary_missing_days": 4.0,
      "external_transfer_change_30d": 71.7293,
      "upi_share_of_spend": 0.5968,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 0,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 0.0,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-05-01",
      "days_since_last_transaction": 22,
      "balance_change_30d": -16.5856,
      "transaction_change_30d": 1.7887,
      "card_spend_change_30d": 5.527,
      "app_login_change_30d": -17.5781,
      "salary_missing_days": 4.0,
      "external_transfer_change_30d": 40.9201,
      "upi_share_of_spend": 0.5164,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 2,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 4,
      "avg_resolution_time_hrs": 12.3398,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-06-01",
      "days_since_last_transaction": 14,
      "balance_change_30d": -12.0363,
      "transaction_change_30d": -15.043,
      "card_spend_change_30d": -27.5453,
      "app_login_change_30d": -26.6669,
      "salary_missing_days": 6.0,
      "external_transfer_change_30d": 61.9383,
      "upi_share_of_spend": 0.589,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 0,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 0.0,
      "emi_bounce_30d": 0
    }
  ],
  "customer": {
    "tenure_months": 6,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 3,
    "has_credit_card": 1,
    "has_loan": 1,
    "days_since_last_transaction": 14,
    "balance_change_30d": -12.0363,
    "transaction_change_30d": -15.043,
    "card_spend_change_30d": -27.5453,
    "app_login_change_30d": -26.6669,
    "salary_missing_days": 6.0,
    "external_transfer_change_30d": 61.9383,
    "upi_share_of_spend": 0.589,
    "fd_maturing_in_30d": 0,
    "products_dropped_90d": 0,
    "complaints_30d": 0,
    "unresolved_complaints": 0,
    "failed_transactions_30d": 1,
    "avg_resolution_time_hrs": 0.0,
    "emi_bounce_30d": 0
  },
  "extra_context": {
    "customer_profile": {
      "segment": "salary",
      "income_regularity": "regular",
      "tenure_months": 6,
      "age": 26,
      "customer_yearly_value": 88961.8473,
      "products_count": 3,
      "has_credit_card": 1,
      "has_loan": 1,
      "value_tier": "high"
    },
    "recent_complaint_text": null
  }
}
```

Response:

```json
{
  "meta": {
    "endpoint": "/predict/both",
    "served_at": "2026-08-31T01:41:27",
    "elapsed_ms": 8741.62,
    "timings_ms": {
      "model1": 63.53,
      "model2": 8677.95
    },
    "customer_id": "C10354",
    "customer_name": "Wazir Naik",
    "snapshot_date": "2026-06-01"
  },
  "model1": {
    "churn_probability": 31.27,
    "raw_churn_probability": 85.11,
    "probability_mode": "sigmoid",
    "risk_score": 74.23,
    "churn_prediction": "Yes",
    "risk_level": "High",
    "top_risk_factors": [
      {
        "factor": "latest_days_since_last_transaction",
        "value": 14,
        "message": "Customer has gone longer without transacting.",
        "contribution": 0.5789387822151184
      },
      {
        "factor": "latest_salary_missing_days",
        "value": 6.0,
        "message": "Salary or pension was delayed recently.",
        "contribution": 0.2811279594898224
      },
      {
        "factor": "latest_vs_avg_upi_share_of_spend_available_history",
        "value": 0.07110000000000005,
        "message": "A larger share of spending is happening through UPI.",
        "contribution": 0.21313293278217316
      },
      {
        "factor": "days_since_last_transaction_trend_6m",
        "value": 2.8857142857142857,
        "message": "Customer has gone longer without transacting.",
        "contribution": 0.18605159223079681
      },
      {
        "factor": "latest_external_transfer_change_30d",
        "value": 61.9383,
        "message": "External transfers have increased.",
        "contribution": 0.1098957434296608
      }
    ]
  },
  "model2_input": {
    "customer_context": {
      "age": 26,
      "tenure_months": 6,
      "customer_segment": "salary",
      "income_regularity": "regular",
      "customer_yearly_value": 88961.8473,
      "products_count": 3,
      "has_credit_card": 1,
      "has_loan": 1
    },
    "behavior": {
      "days_since_last_transaction": 14,
      "balance_change_30d": -12.0363,
      "transaction_change_30d": -15.043,
      "card_spend_change_30d": -27.5453,
      "app_login_change_30d": -26.6669,
      "salary_missing_days": 6,
      "external_transfer_change_30d": 61.9383,
      "upi_share_of_spend": 0.589,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "emi_bounce_30d": 0
    },
    "service_evidence": {
      "complaints_30d": 0,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 0.0,
      "complaint_text": null
    },
    "model1": {
      "churn_probability": 0.3127,
      "churn_prediction": "Yes",
      "risk_level": "High",
      "top_risk_factors": [
        {
          "factor": "days_since_last_transaction",
          "value": 14
        },
        {
          "factor": "salary_missing_days",
          "value": 6
        },
        {
          "factor": "upi_share_of_spend",
          "value": 0.589
        }
      ]
    },
    "eligible_actions": [
      "FINANCIAL_GUIDANCE",
      "SERVICE_RECOVERY",
      "PRODUCT_REVIEW",
      "RE_ENGAGEMENT",
      "MONITOR"
    ],
    "case_id": "C10354"
  },
  "model2": {
    "case_id": "C10354",
    "ok": true,
    "prediction": {
      "evidence": [
        "complaints_30d=0",
        "unresolved_complaints=0",
        "avg_resolution_time_hrs=0.0",
        "failed_transactions_30d=1"
      ],
      "primary_reason": "SERVICE_DISSATISFACTION",
      "reasoning_summary": "Complaint and service friction signals are mixed or weak. Service recovery fits because complaints_30d=0, unresolved_complaints=0, avg_resolution_time_hrs=0.0, failed_transactions_30d=1 suggest a service issue without a clear escalation level.",
      "recommended_action": "SERVICE_RECOVERY",
      "secondary_reasons": [],
      "urgency": "MEDIUM"
    },
    "warnings": [
      "evidence: 'complaints_30d=0' cites a zero/null value, which is not evidence; remove it",
      "evidence: 'unresolved_complaints=0' cites a zero/null value, which is not evidence; remove it",
      "evidence: 'avg_resolution_time_hrs=0.0' cites a zero/null value, which is not evidence; remove it",
      "primary_reason: SERVICE_DISSATISFACTION requires a non-zero complaint signal, but complaints_30d, unresolved_complaints and avg_resolution_time_hrs are all 0 and complaint_text is null; choose the reason matching the behavior signals"
    ],
    "raw_text": "{\"evidence\":[\"complaints_30d=0\",\"unresolved_complaints=0\",\"avg_resolution_time_hrs=0.0\"],\"primary_reason\":\"SERVICE_DISSATISFACTION\",\"reasoning_summary\":\"Complaint and resolution signal strength is low or mixed; service recovery fits because complaints_30d=0, unresolved_complaints=0, avg_resolution_time_hrs=0.0 cite a weak signal.\",\"recommended_action\":\"SERVICE_RECOVERY\",\"secondary_reasons\":[],\"urgency\":\"MEDIUM\"}",
    "error": null,
    "latency_s": 8.6779,
    "simple_output": "Reason: SERVICE_DISSATISFACTION | Urgency: MEDIUM | Action: SERVICE_RECOVERY | Why: Complaint and service friction signals are mixed or weak. Service recovery fits because complaints_30d=0, unresolved_complaints=0, avg_resolution_time_hrs=0.0, failed_transactions_30d=1 suggest a service issue without a clear escalation level."
  }
}
```

### Frado Lad (`C10975`)

- OK: `True`
- Shape errors: `[]`
- Simple output: Reason: UNKNOWN | Urgency: LOW | Action: MONITOR | Why: Complaint and resolution signals are mixed or weak; evidence is genuinely unclear.

Request:

```json
{
  "customer_id": "C10975",
  "customer_name": "Frado Lad",
  "prediction_date": "2026-06-01",
  "snapshot_date": "2026-06-01",
  "target_month": "2026-07-01",
  "profile": {
    "tenure_months": 31,
    "customer_segment": "vendor",
    "income_regularity": "irregular",
    "products_count": 3,
    "has_credit_card": 0,
    "has_loan": 1
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 5,
      "balance_change_30d": 17.8527,
      "transaction_change_30d": -4.0291,
      "card_spend_change_30d": 14.9044,
      "app_login_change_30d": -4.1813,
      "salary_missing_days": null,
      "external_transfer_change_30d": 27.0756,
      "upi_share_of_spend": 0.6125,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 0,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 0.0,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-02-01",
      "days_since_last_transaction": 6,
      "balance_change_30d": 5.5751,
      "transaction_change_30d": 8.3607,
      "card_spend_change_30d": 22.5903,
      "app_login_change_30d": -18.982,
      "salary_missing_days": null,
      "external_transfer_change_30d": 36.5257,
      "upi_share_of_spend": 0.6681,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 0,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 0.0,
      "emi_bounce_30d": 1
    },
    {
      "snapshot_date": "2026-03-01",
      "days_since_last_transaction": 15,
      "balance_change_30d": -12.5295,
      "transaction_change_30d": -7.8644,
      "card_spend_change_30d": -28.0643,
      "app_login_change_30d": -21.0718,
      "salary_missing_days": null,
      "external_transfer_change_30d": 14.8563,
      "upi_share_of_spend": 0.7306,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 0,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 2,
      "avg_resolution_time_hrs": 0.0,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-04-01",
      "days_since_last_transaction": 14,
      "balance_change_30d": -25.2357,
      "transaction_change_30d": -27.7011,
      "card_spend_change_30d": -10.3842,
      "app_login_change_30d": -2.8293,
      "salary_missing_days": null,
      "external_transfer_change_30d": 11.3559,
      "upi_share_of_spend": 0.6469,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 0,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 0.0,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-05-01",
      "days_since_last_transaction": 7,
      "balance_change_30d": 19.1982,
      "transaction_change_30d": -10.2616,
      "card_spend_change_30d": -3.9291,
      "app_login_change_30d": 19.2329,
      "salary_missing_days": null,
      "external_transfer_change_30d": 78.5378,
      "upi_share_of_spend": 0.6752,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 1,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 48.5316,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-06-01",
      "days_since_last_transaction": 11,
      "balance_change_30d": -16.6448,
      "transaction_change_30d": -11.3713,
      "card_spend_change_30d": -27.3349,
      "app_login_change_30d": -34.2901,
      "salary_missing_days": null,
      "external_transfer_change_30d": 46.6245,
      "upi_share_of_spend": 0.708,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 0,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 0.0,
      "emi_bounce_30d": 0
    }
  ],
  "customer": {
    "tenure_months": 31,
    "customer_segment": "vendor",
    "income_regularity": "irregular",
    "products_count": 3,
    "has_credit_card": 0,
    "has_loan": 1,
    "days_since_last_transaction": 11,
    "balance_change_30d": -16.6448,
    "transaction_change_30d": -11.3713,
    "card_spend_change_30d": -27.3349,
    "app_login_change_30d": -34.2901,
    "salary_missing_days": null,
    "external_transfer_change_30d": 46.6245,
    "upi_share_of_spend": 0.708,
    "fd_maturing_in_30d": 0,
    "products_dropped_90d": 0,
    "complaints_30d": 0,
    "unresolved_complaints": 0,
    "failed_transactions_30d": 0,
    "avg_resolution_time_hrs": 0.0,
    "emi_bounce_30d": 0
  },
  "extra_context": {
    "customer_profile": {
      "segment": "vendor",
      "income_regularity": "irregular",
      "tenure_months": 31,
      "age": 48,
      "customer_yearly_value": 27161.4748,
      "products_count": 3,
      "has_credit_card": 0,
      "has_loan": 1,
      "value_tier": "low"
    },
    "recent_complaint_text": null
  }
}
```

Response:

```json
{
  "meta": {
    "endpoint": "/predict/both",
    "served_at": "2026-08-31T01:41:32",
    "elapsed_ms": 5158.18,
    "timings_ms": {
      "model1": 83.48,
      "model2": 5074.55
    },
    "customer_id": "C10975",
    "customer_name": "Frado Lad",
    "snapshot_date": "2026-06-01"
  },
  "model1": {
    "churn_probability": 8.28,
    "raw_churn_probability": 50.36,
    "probability_mode": "sigmoid",
    "risk_score": 24.83,
    "churn_prediction": "No",
    "risk_level": "Low",
    "top_risk_factors": [
      {
        "factor": "latest_vs_avg_upi_share_of_spend_available_history",
        "value": 0.03444999999999987,
        "message": "A larger share of spending is happening through UPI.",
        "contribution": 0.08561644703149796
      },
      {
        "factor": "latest_app_login_change_30d",
        "value": -34.2901,
        "message": "App usage has been falling across recent months.",
        "contribution": 0.07046792656183243
      },
      {
        "factor": "max_avg_resolution_time_hrs_3m",
        "value": 48.5316,
        "message": "Recent complaints took longer to resolve.",
        "contribution": 0.0661461278796196
      },
      {
        "factor": "latest_upi_share_of_spend",
        "value": 0.708,
        "message": "A larger share of spending is happening through UPI.",
        "contribution": 0.0418095625936985
      },
      {
        "factor": "external_transfer_change_30d_trend_6m",
        "value": 6.293725714285712,
        "message": "External transfers have increased.",
        "contribution": 0.03636994957923889
      }
    ]
  },
  "model2_input": {
    "customer_context": {
      "age": 48,
      "tenure_months": 31,
      "customer_segment": "vendor",
      "income_regularity": "irregular",
      "customer_yearly_value": 27161.4748,
      "products_count": 3,
      "has_credit_card": 0,
      "has_loan": 1
    },
    "behavior": {
      "days_since_last_transaction": 11,
      "balance_change_30d": -16.6448,
      "transaction_change_30d": -11.3713,
      "card_spend_change_30d": -27.3349,
      "app_login_change_30d": -34.2901,
      "salary_missing_days": null,
      "external_transfer_change_30d": 46.6245,
      "upi_share_of_spend": 0.708,
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
      "churn_probability": 0.0828,
      "churn_prediction": "No",
      "risk_level": "Low",
      "top_risk_factors": [
        {
          "factor": "upi_share_of_spend",
          "value": 0.708
        },
        {
          "factor": "app_login_change_30d",
          "value": -34.2901
        },
        {
          "factor": "external_transfer_change_30d",
          "value": 46.6245
        }
      ]
    },
    "eligible_actions": [
      "PRODUCT_REVIEW",
      "RE_ENGAGEMENT",
      "MONITOR"
    ],
    "case_id": "C10975"
  },
  "model2": {
    "case_id": "C10975",
    "ok": true,
    "prediction": {
      "evidence": [
        "complaints_30d=0",
        "unresolved_complaints=0",
        "avg_resolution_time_hrs=0.0"
      ],
      "primary_reason": "UNKNOWN",
      "reasoning_summary": "Complaint and resolution signals are mixed or weak; evidence is genuinely unclear.",
      "recommended_action": "MONITOR",
      "secondary_reasons": [],
      "urgency": "LOW"
    },
    "warnings": [
      "evidence: 'complaints_30d=0' cites a zero/null value, which is not evidence; remove it",
      "evidence: 'unresolved_complaints=0' cites a zero/null value, which is not evidence; remove it",
      "evidence: 'avg_resolution_time_hrs=0.0' cites a zero/null value, which is not evidence; remove it"
    ],
    "raw_text": "{\"evidence\":[\"products_count=3\",\"complaints_30d=0\",\"external_transfer_change_30d=46.6\"],\"primary_reason\":\"PRODUCT_MISMATCH\",\"reasoning_summary\":\"The relationship looks mismatched because products_count=3 and complaints_30d=0 suggest PRODUCT_MISMATCH.\",\"recommended_action\":\"PRODUCT_REVIEW\",\"secondary_reasons\":[],\"urgency\":\"MEDIUM\"}",
    "error": null,
    "latency_s": 5.0745,
    "simple_output": "Reason: UNKNOWN | Urgency: LOW | Action: MONITOR | Why: Complaint and resolution signals are mixed or weak; evidence is genuinely unclear."
  }
}
```

### Dalbir Krish (`C11091`)

- OK: `True`
- Shape errors: `[]`
- Simple output: Reason: FEE_DISSATISFACTION | Urgency: HIGH | Action: COMPLAINT_ESCALATION | Why: Complaint escalation because complaints_30d=3 and unresolved_complaints=2 with complaint_text mentioning fees or charges are troubling.

Request:

```json
{
  "customer_id": "C11091",
  "customer_name": "Dalbir Krish",
  "prediction_date": "2026-06-01",
  "snapshot_date": "2026-06-01",
  "target_month": "2026-07-01",
  "profile": {
    "tenure_months": 226,
    "customer_segment": "farmer",
    "income_regularity": "seasonal",
    "products_count": 1,
    "has_credit_card": 0,
    "has_loan": 0
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 8,
      "balance_change_30d": -17.3509,
      "transaction_change_30d": -24.3498,
      "card_spend_change_30d": 0.8655,
      "app_login_change_30d": -20.0268,
      "salary_missing_days": null,
      "external_transfer_change_30d": 21.4322,
      "upi_share_of_spend": 0.201,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 0,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 0.0,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-02-01",
      "days_since_last_transaction": 17,
      "balance_change_30d": -30.1203,
      "transaction_change_30d": -11.5747,
      "card_spend_change_30d": -17.6465,
      "app_login_change_30d": -7.6702,
      "salary_missing_days": null,
      "external_transfer_change_30d": 46.8033,
      "upi_share_of_spend": 0.1343,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 4,
      "avg_resolution_time_hrs": 12.1889,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-03-01",
      "days_since_last_transaction": 14,
      "balance_change_30d": -3.7858,
      "transaction_change_30d": -7.8927,
      "card_spend_change_30d": -29.4274,
      "app_login_change_30d": 0.1296,
      "salary_missing_days": null,
      "external_transfer_change_30d": 39.4443,
      "upi_share_of_spend": 0.1817,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 0,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 2,
      "avg_resolution_time_hrs": 0.0,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-04-01",
      "days_since_last_transaction": 12,
      "balance_change_30d": -3.2008,
      "transaction_change_30d": -12.9756,
      "card_spend_change_30d": -17.4209,
      "app_login_change_30d": -25.1918,
      "salary_missing_days": null,
      "external_transfer_change_30d": 6.5301,
      "upi_share_of_spend": 0.089,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 0,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 0.0,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-05-01",
      "days_since_last_transaction": 23,
      "balance_change_30d": -20.9399,
      "transaction_change_30d": -56.5687,
      "card_spend_change_30d": -68.8842,
      "app_login_change_30d": -38.817,
      "salary_missing_days": null,
      "external_transfer_change_30d": 81.2348,
      "upi_share_of_spend": 0.2873,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 2,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 31.3267,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-06-01",
      "days_since_last_transaction": 22,
      "balance_change_30d": -48.9275,
      "transaction_change_30d": -41.315,
      "card_spend_change_30d": -58.5351,
      "app_login_change_30d": -49.9021,
      "salary_missing_days": null,
      "external_transfer_change_30d": 106.0705,
      "upi_share_of_spend": 0.3583,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 1,
      "complaints_30d": 3,
      "unresolved_complaints": 2,
      "failed_transactions_30d": 8,
      "avg_resolution_time_hrs": 58.6674,
      "emi_bounce_30d": 0
    }
  ],
  "customer": {
    "tenure_months": 226,
    "customer_segment": "farmer",
    "income_regularity": "seasonal",
    "products_count": 1,
    "has_credit_card": 0,
    "has_loan": 0,
    "days_since_last_transaction": 22,
    "balance_change_30d": -48.9275,
    "transaction_change_30d": -41.315,
    "card_spend_change_30d": -58.5351,
    "app_login_change_30d": -49.9021,
    "salary_missing_days": null,
    "external_transfer_change_30d": 106.0705,
    "upi_share_of_spend": 0.3583,
    "fd_maturing_in_30d": 0,
    "products_dropped_90d": 1,
    "complaints_30d": 3,
    "unresolved_complaints": 2,
    "failed_transactions_30d": 8,
    "avg_resolution_time_hrs": 58.6674,
    "emi_bounce_30d": 0
  },
  "extra_context": {
    "customer_profile": {
      "segment": "farmer",
      "income_regularity": "seasonal",
      "tenure_months": 226,
      "age": 49,
      "customer_yearly_value": 66925.5926,
      "products_count": 1,
      "has_credit_card": 0,
      "has_loan": 0,
      "value_tier": "medium"
    },
    "recent_complaint_text": "Please confirm if charges apply on inward remittance from my son."
  }
}
```

Response:

```json
{
  "meta": {
    "endpoint": "/predict/both",
    "served_at": "2026-08-31T01:41:35",
    "elapsed_ms": 2705.83,
    "timings_ms": {
      "model1": 93.09,
      "model2": 2612.57
    },
    "customer_id": "C11091",
    "customer_name": "Dalbir Krish",
    "snapshot_date": "2026-06-01"
  },
  "model1": {
    "churn_probability": 40.44,
    "raw_churn_probability": 93.71,
    "probability_mode": "sigmoid",
    "risk_score": 77.67,
    "churn_prediction": "Yes",
    "risk_level": "High",
    "top_risk_factors": [
      {
        "factor": "latest_days_since_last_transaction",
        "value": 22,
        "message": "Customer has gone longer without transacting.",
        "contribution": 0.5143784880638123
      },
      {
        "factor": "latest_transaction_change_30d",
        "value": -41.315,
        "message": "Transaction activity has been falling across recent months.",
        "contribution": 0.4217112362384796
      },
      {
        "factor": "latest_vs_avg_upi_share_of_spend_available_history",
        "value": 0.1497,
        "message": "A larger share of spending is happening through UPI.",
        "contribution": 0.24843627214431763
      },
      {
        "factor": "max_avg_resolution_time_hrs_3m",
        "value": 58.6674,
        "message": "Recent complaints took longer to resolve.",
        "contribution": 0.1840265989303589
      },
      {
        "factor": "latest_balance_change_30d",
        "value": -48.9275,
        "message": "Balance has been falling across recent months.",
        "contribution": 0.17752601206302643
      }
    ]
  },
  "model2_input": {
    "customer_context": {
      "age": 49,
      "tenure_months": 226,
      "customer_segment": "farmer",
      "income_regularity": "seasonal",
      "customer_yearly_value": 66925.5926,
      "products_count": 1,
      "has_credit_card": 0,
      "has_loan": 0
    },
    "behavior": {
      "days_since_last_transaction": 22,
      "balance_change_30d": -48.9275,
      "transaction_change_30d": -41.315,
      "card_spend_change_30d": -58.5351,
      "app_login_change_30d": -49.9021,
      "salary_missing_days": null,
      "external_transfer_change_30d": 106.0705,
      "upi_share_of_spend": 0.3583,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 1,
      "emi_bounce_30d": 0
    },
    "service_evidence": {
      "complaints_30d": 3,
      "unresolved_complaints": 2,
      "failed_transactions_30d": 8,
      "avg_resolution_time_hrs": 58.6674,
      "complaint_text": "Please confirm if charges apply on inward remittance from my son."
    },
    "model1": {
      "churn_probability": 0.4044,
      "churn_prediction": "Yes",
      "risk_level": "High",
      "top_risk_factors": [
        {
          "factor": "days_since_last_transaction",
          "value": 22
        },
        {
          "factor": "transaction_change_30d",
          "value": -41.315
        },
        {
          "factor": "upi_share_of_spend",
          "value": 0.3583
        }
      ]
    },
    "eligible_actions": [
      "COMPLAINT_ESCALATION",
      "FEE_WAIVER_REVIEW",
      "SERVICE_RECOVERY",
      "PRODUCT_REVIEW",
      "MONITOR"
    ],
    "case_id": "C11091"
  },
  "model2": {
    "case_id": "C11091",
    "ok": true,
    "prediction": {
      "evidence": [
        "complaints_30d=3",
        "unresolved_complaints=2",
        "avg_resolution_time_hrs=58.7",
        "complaint_text contains confusing charges or fees"
      ],
      "primary_reason": "FEE_DISSATISFACTION",
      "reasoning_summary": "Complaint escalation because complaints_30d=3 and unresolved_complaints=2 with complaint_text mentioning fees or charges are troubling.",
      "recommended_action": "COMPLAINT_ESCALATION",
      "secondary_reasons": [],
      "urgency": "HIGH"
    },
    "warnings": [],
    "raw_text": "{\n    \"evidence\": [\n        \"complaints_30d=3\",\n        \"unresolved_complaints=2\",\n        \"avg_resolution_time_hrs=58.7\",\n        \"complaint_text contains confusing charges or fees\"\n    ],\n    \"primary_reason\": \"FEE_DISSATISFACTION\",\n    \"reasoning_summary\": \"Complaint escalation because complaints_30d=3 and unresolved_complaints=2 with complaint_text mentioning fees or charges are troubling.\",\n    \"recommended_action\": \"COMPLAINT_ESCALATION\",\n    \"secondary_reasons\": [],\n    \"urgency\": \"HIGH\"\n}",
    "error": null,
    "latency_s": 2.6125,
    "simple_output": "Reason: FEE_DISSATISFACTION | Urgency: HIGH | Action: COMPLAINT_ESCALATION | Why: Complaint escalation because complaints_30d=3 and unresolved_complaints=2 with complaint_text mentioning fees or charges are troubling."
  }
}
```

### Abhiram Arora (`C11434`)

- OK: `True`
- Shape errors: `[]`
- Simple output: Reason: TEMPORARY_SEASONAL_CHANGE | Urgency: MEDIUM | Action: RE_ENGAGEMENT | Why: Temporary seasonal change is the supported explanation for the relationship between evidence values. Evidence suggests this because complaints_30d=0, unresolved_complaints=0, avg_resolution_time_hrs=0.0.

Request:

```json
{
  "customer_id": "C11434",
  "customer_name": "Abhiram Arora",
  "prediction_date": "2026-06-01",
  "snapshot_date": "2026-06-01",
  "target_month": "2026-07-01",
  "profile": {
    "tenure_months": 144,
    "customer_segment": "farmer",
    "income_regularity": "seasonal",
    "products_count": 2,
    "has_credit_card": 0,
    "has_loan": 0
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 18,
      "balance_change_30d": -47.7553,
      "transaction_change_30d": -12.6936,
      "card_spend_change_30d": -23.4746,
      "app_login_change_30d": -31.9102,
      "salary_missing_days": null,
      "external_transfer_change_30d": 34.3827,
      "upi_share_of_spend": 0.5537,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 1,
      "complaints_30d": 0,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 0.0,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-02-01",
      "days_since_last_transaction": 12,
      "balance_change_30d": -23.1063,
      "transaction_change_30d": -13.5755,
      "card_spend_change_30d": -38.646,
      "app_login_change_30d": -14.2921,
      "salary_missing_days": null,
      "external_transfer_change_30d": 30.8813,
      "upi_share_of_spend": 0.5396,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 0,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 0.0,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-03-01",
      "days_since_last_transaction": 8,
      "balance_change_30d": 1.8486,
      "transaction_change_30d": 15.6011,
      "card_spend_change_30d": 15.6308,
      "app_login_change_30d": 44.4766,
      "salary_missing_days": null,
      "external_transfer_change_30d": -25.4406,
      "upi_share_of_spend": 0.4141,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 0,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 0.0,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-04-01",
      "days_since_last_transaction": 3,
      "balance_change_30d": 43.1637,
      "transaction_change_30d": 13.5673,
      "card_spend_change_30d": 27.6291,
      "app_login_change_30d": 21.7997,
      "salary_missing_days": null,
      "external_transfer_change_30d": -30.0879,
      "upi_share_of_spend": 0.4621,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 0,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 0.0,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-05-01",
      "days_since_last_transaction": 3,
      "balance_change_30d": 31.4257,
      "transaction_change_30d": 34.3361,
      "card_spend_change_30d": 49.0244,
      "app_login_change_30d": -3.2229,
      "salary_missing_days": null,
      "external_transfer_change_30d": -33.5274,
      "upi_share_of_spend": 0.3517,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 1,
      "complaints_30d": 0,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 3,
      "avg_resolution_time_hrs": 0.0,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-06-01",
      "days_since_last_transaction": 0,
      "balance_change_30d": 33.5856,
      "transaction_change_30d": 21.3141,
      "card_spend_change_30d": 62.6345,
      "app_login_change_30d": 54.6137,
      "salary_missing_days": null,
      "external_transfer_change_30d": -23.231,
      "upi_share_of_spend": 0.2892,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 0,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 0.0,
      "emi_bounce_30d": 0
    }
  ],
  "customer": {
    "tenure_months": 144,
    "customer_segment": "farmer",
    "income_regularity": "seasonal",
    "products_count": 2,
    "has_credit_card": 0,
    "has_loan": 0,
    "days_since_last_transaction": 0,
    "balance_change_30d": 33.5856,
    "transaction_change_30d": 21.3141,
    "card_spend_change_30d": 62.6345,
    "app_login_change_30d": 54.6137,
    "salary_missing_days": null,
    "external_transfer_change_30d": -23.231,
    "upi_share_of_spend": 0.2892,
    "fd_maturing_in_30d": 0,
    "products_dropped_90d": 0,
    "complaints_30d": 0,
    "unresolved_complaints": 0,
    "failed_transactions_30d": 1,
    "avg_resolution_time_hrs": 0.0,
    "emi_bounce_30d": 0
  },
  "extra_context": {
    "customer_profile": {
      "segment": "farmer",
      "income_regularity": "seasonal",
      "tenure_months": 144,
      "age": 47,
      "customer_yearly_value": 10383.941,
      "products_count": 2,
      "has_credit_card": 0,
      "has_loan": 0,
      "value_tier": "low"
    },
    "recent_complaint_text": null
  }
}
```

Response:

```json
{
  "meta": {
    "endpoint": "/predict/both",
    "served_at": "2026-08-31T01:41:41",
    "elapsed_ms": 5864.75,
    "timings_ms": {
      "model1": 67.21,
      "model2": 5797.38
    },
    "customer_id": "C11434",
    "customer_name": "Abhiram Arora",
    "snapshot_date": "2026-06-01"
  },
  "model1": {
    "churn_probability": 1.43,
    "raw_churn_probability": 11.08,
    "probability_mode": "sigmoid",
    "risk_score": 4.28,
    "churn_prediction": "No",
    "risk_level": "Low",
    "top_risk_factors": [
      {
        "factor": "latest_vs_avg_card_spend_change_30d_available_history",
        "value": 47.16813333333334,
        "message": "This signal increased churn risk.",
        "contribution": 0.1664414256811142
      },
      {
        "factor": "latest_vs_avg_balance_change_30d_available_history",
        "value": 27.0586,
        "message": "This signal increased churn risk.",
        "contribution": 0.07401101291179657
      },
      {
        "factor": "avg_balance_change_30d_3m",
        "value": 36.05833333333333,
        "message": "This signal increased churn risk.",
        "contribution": 0.035236094146966934
      },
      {
        "factor": "sum_failed_transactions_30d_6m",
        "value": 7.0,
        "message": "Customer has recent failed transactions.",
        "contribution": 0.028613174334168434
      },
      {
        "factor": "count_failed_transaction_month_6m",
        "value": 5,
        "message": "This signal increased churn risk.",
        "contribution": 0.025922099128365517
      }
    ]
  },
  "model2_input": {
    "customer_context": {
      "age": 47,
      "tenure_months": 144,
      "customer_segment": "farmer",
      "income_regularity": "seasonal",
      "customer_yearly_value": 10383.941,
      "products_count": 2,
      "has_credit_card": 0,
      "has_loan": 0
    },
    "behavior": {
      "days_since_last_transaction": 0,
      "balance_change_30d": 33.5856,
      "transaction_change_30d": 21.3141,
      "card_spend_change_30d": 62.6345,
      "app_login_change_30d": 54.6137,
      "salary_missing_days": null,
      "external_transfer_change_30d": -23.231,
      "upi_share_of_spend": 0.2892,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "emi_bounce_30d": 0
    },
    "service_evidence": {
      "complaints_30d": 0,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 0.0,
      "complaint_text": null
    },
    "model1": {
      "churn_probability": 0.0143,
      "churn_prediction": "No",
      "risk_level": "Low",
      "top_risk_factors": [
        {
          "factor": "card_spend_change_30d",
          "value": 62.6345
        },
        {
          "factor": "balance_change_30d",
          "value": 33.5856
        },
        {
          "factor": "failed_transactions_30d",
          "value": 1
        }
      ]
    },
    "eligible_actions": [
      "SERVICE_RECOVERY",
      "RE_ENGAGEMENT",
      "MONITOR"
    ],
    "case_id": "C11434"
  },
  "model2": {
    "case_id": "C11434",
    "ok": true,
    "prediction": {
      "evidence": [
        "complaints_30d=0",
        "unresolved_complaints=0",
        "avg_resolution_time_hrs=0.0"
      ],
      "primary_reason": "TEMPORARY_SEASONAL_CHANGE",
      "reasoning_summary": "Temporary seasonal change is the supported explanation for the relationship between evidence values. Evidence suggests this because complaints_30d=0, unresolved_complaints=0, avg_resolution_time_hrs=0.0.",
      "recommended_action": "RE_ENGAGEMENT",
      "secondary_reasons": [],
      "urgency": "MEDIUM"
    },
    "warnings": [
      "evidence: 'complaints_30d=0' cites a zero/null value, which is not evidence; remove it",
      "evidence: 'unresolved_complaints=0' cites a zero/null value, which is not evidence; remove it",
      "evidence: 'avg_resolution_time_hrs=0.0' cites a zero/null value, which is not evidence; remove it"
    ],
    "raw_text": "{\"evidence\":[\"balance_change_30d=33.6\",\"card_spend_change_30d=62.6\"],\"primary_reason\":\"DIGITAL_FRICTION\",\"reasoning_summary\":\"Digital friction is the strongest supported signal here because complaints_30d=0 and balance_change_30d=33.6 suggest a digital experience problem without clear escalation-level evidence.\",\"recommended_action\":\"RE_ENGAGEMENT\",\"secondary_reasons\":[],\"urgency\":\"MEDIUM\"}",
    "error": null,
    "latency_s": 5.7974,
    "simple_output": "Reason: TEMPORARY_SEASONAL_CHANGE | Urgency: MEDIUM | Action: RE_ENGAGEMENT | Why: Temporary seasonal change is the supported explanation for the relationship between evidence values. Evidence suggests this because complaints_30d=0, unresolved_complaints=0, avg_resolution_time_hrs=0.0."
  }
}
```

### Chatura Bal (`C11472`)

- OK: `True`
- Shape errors: `[]`
- Simple output: Reason: TEMPORARY_SEASONAL_CHANGE | Urgency: LOW | Action: MONITOR | Why: Temporary seasonal change is the most supported explanation for the risk signal. Evidence suggests this because complaints_30d=0, unresolved_complaints=0, avg_resolution_time_hrs=0.

Request:

```json
{
  "customer_id": "C11472",
  "customer_name": "Chatura Bal",
  "prediction_date": "2026-06-01",
  "snapshot_date": "2026-06-01",
  "target_month": "2026-07-01",
  "profile": {
    "tenure_months": 216,
    "customer_segment": "farmer",
    "income_regularity": "seasonal",
    "products_count": 3,
    "has_credit_card": 0,
    "has_loan": 0
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 14,
      "balance_change_30d": -10.5543,
      "transaction_change_30d": -21.3134,
      "card_spend_change_30d": -25.4056,
      "app_login_change_30d": -14.7491,
      "salary_missing_days": null,
      "external_transfer_change_30d": 19.5286,
      "upi_share_of_spend": 0.7158,
      "fd_maturing_in_30d": 1,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 2,
      "avg_resolution_time_hrs": 34.0602,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-02-01",
      "days_since_last_transaction": 10,
      "balance_change_30d": -32.1148,
      "transaction_change_30d": -5.6289,
      "card_spend_change_30d": -3.5672,
      "app_login_change_30d": 7.6265,
      "salary_missing_days": null,
      "external_transfer_change_30d": 41.8711,
      "upi_share_of_spend": 0.8644,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 0,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 0.0,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-03-01",
      "days_since_last_transaction": 12,
      "balance_change_30d": -17.255,
      "transaction_change_30d": -14.8176,
      "card_spend_change_30d": -18.8183,
      "app_login_change_30d": -7.6632,
      "salary_missing_days": null,
      "external_transfer_change_30d": 36.2155,
      "upi_share_of_spend": 0.7272,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 0,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 0.0,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-04-01",
      "days_since_last_transaction": 12,
      "balance_change_30d": -9.1599,
      "transaction_change_30d": -26.4674,
      "card_spend_change_30d": -0.3904,
      "app_login_change_30d": -13.6647,
      "salary_missing_days": null,
      "external_transfer_change_30d": 37.3157,
      "upi_share_of_spend": 0.7011,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 1.0,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-05-01",
      "days_since_last_transaction": 6,
      "balance_change_30d": 14.0429,
      "transaction_change_30d": 6.2995,
      "card_spend_change_30d": 18.2312,
      "app_login_change_30d": 16.2717,
      "salary_missing_days": null,
      "external_transfer_change_30d": 22.7831,
      "upi_share_of_spend": 0.7235,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 0,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 0.0,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-06-01",
      "days_since_last_transaction": 3,
      "balance_change_30d": 7.0317,
      "transaction_change_30d": 17.5141,
      "card_spend_change_30d": 8.0962,
      "app_login_change_30d": 11.1619,
      "salary_missing_days": null,
      "external_transfer_change_30d": 15.0808,
      "upi_share_of_spend": 0.6203,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 0,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 0.0,
      "emi_bounce_30d": 0
    }
  ],
  "customer": {
    "tenure_months": 216,
    "customer_segment": "farmer",
    "income_regularity": "seasonal",
    "products_count": 3,
    "has_credit_card": 0,
    "has_loan": 0,
    "days_since_last_transaction": 3,
    "balance_change_30d": 7.0317,
    "transaction_change_30d": 17.5141,
    "card_spend_change_30d": 8.0962,
    "app_login_change_30d": 11.1619,
    "salary_missing_days": null,
    "external_transfer_change_30d": 15.0808,
    "upi_share_of_spend": 0.6203,
    "fd_maturing_in_30d": 0,
    "products_dropped_90d": 0,
    "complaints_30d": 0,
    "unresolved_complaints": 0,
    "failed_transactions_30d": 1,
    "avg_resolution_time_hrs": 0.0,
    "emi_bounce_30d": 0
  },
  "extra_context": {
    "customer_profile": {
      "segment": "farmer",
      "income_regularity": "seasonal",
      "tenure_months": 216,
      "age": 54,
      "customer_yearly_value": 8627.3513,
      "products_count": 3,
      "has_credit_card": 0,
      "has_loan": 0,
      "value_tier": "low"
    },
    "recent_complaint_text": null
  }
}
```

Response:

```json
{
  "meta": {
    "endpoint": "/predict/both",
    "served_at": "2026-08-31T01:41:46",
    "elapsed_ms": 5615.12,
    "timings_ms": {
      "model1": 64.2,
      "model2": 5550.77
    },
    "customer_id": "C11472",
    "customer_name": "Chatura Bal",
    "snapshot_date": "2026-06-01"
  },
  "model1": {
    "churn_probability": 1.96,
    "raw_churn_probability": 17.94,
    "probability_mode": "sigmoid",
    "risk_score": 5.87,
    "churn_prediction": "No",
    "risk_level": "Low",
    "top_risk_factors": [
      {
        "factor": "count_balance_drop_6m",
        "value": 4,
        "message": "This signal increased churn risk.",
        "contribution": 0.046647462993860245
      },
      {
        "factor": "card_spend_change_30d_trend_6m",
        "value": 7.180917142857142,
        "message": "This signal increased churn risk.",
        "contribution": 0.0350114144384861
      },
      {
        "factor": "avg_upi_share_of_spend_6m",
        "value": 0.7253833333333333,
        "message": "A larger share of spending is happening through UPI.",
        "contribution": 0.03071168065071106
      },
      {
        "factor": "latest_upi_share_of_spend",
        "value": 0.6203,
        "message": "A larger share of spending is happening through UPI.",
        "contribution": 0.029130419716238976
      },
      {
        "factor": "max_days_since_last_transaction_3m",
        "value": 12.0,
        "message": "Customer has gone longer without transacting.",
        "contribution": 0.022791976109147072
      }
    ]
  },
  "model2_input": {
    "customer_context": {
      "age": 54,
      "tenure_months": 216,
      "customer_segment": "farmer",
      "income_regularity": "seasonal",
      "customer_yearly_value": 8627.3513,
      "products_count": 3,
      "has_credit_card": 0,
      "has_loan": 0
    },
    "behavior": {
      "days_since_last_transaction": 3,
      "balance_change_30d": 7.0317,
      "transaction_change_30d": 17.5141,
      "card_spend_change_30d": 8.0962,
      "app_login_change_30d": 11.1619,
      "salary_missing_days": null,
      "external_transfer_change_30d": 15.0808,
      "upi_share_of_spend": 0.6203,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "emi_bounce_30d": 0
    },
    "service_evidence": {
      "complaints_30d": 0,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 0.0,
      "complaint_text": null
    },
    "model1": {
      "churn_probability": 0.0196,
      "churn_prediction": "No",
      "risk_level": "Low",
      "top_risk_factors": [
        {
          "factor": "card_spend_change_30d",
          "value": 8.0962
        },
        {
          "factor": "upi_share_of_spend",
          "value": 0.6203
        },
        {
          "factor": "days_since_last_transaction",
          "value": 3
        }
      ]
    },
    "eligible_actions": [
      "SERVICE_RECOVERY",
      "RE_ENGAGEMENT",
      "MONITOR"
    ],
    "case_id": "C11472"
  },
  "model2": {
    "case_id": "C11472",
    "ok": true,
    "prediction": {
      "evidence": [
        "complaints_30d=0",
        "unresolved_complaints=0",
        "avg_resolution_time_hrs=0"
      ],
      "primary_reason": "TEMPORARY_SEASONAL_CHANGE",
      "reasoning_summary": "Temporary seasonal change is the most supported explanation for the risk signal. Evidence suggests this because complaints_30d=0, unresolved_complaints=0, avg_resolution_time_hrs=0.",
      "recommended_action": "MONITOR",
      "secondary_reasons": [],
      "urgency": "LOW"
    },
    "warnings": [
      "evidence: 'complaints_30d=0' cites a zero/null value, which is not evidence; remove it",
      "evidence: 'unresolved_complaints=0' cites a zero/null value, which is not evidence; remove it",
      "evidence: 'avg_resolution_time_hrs=0' cites a zero/null value, which is not evidence; remove it"
    ],
    "raw_text": "{\"evidence\":[\"complaints_30d=0\",\"unresolved_complaints=0\",\"avg_resolution_time_hrs=0.0\"],\"primary_reason\":\"DIGITAL_FRICTION\",\"reasoning_summary\":\"Digital friction is the strongest supported signal here because complaints_30d=0 and unresolved_complaints=0 cite a mix of mixed or weak signals.\",\"recommended_action\":\"RE_ENGAGEMENT\",\"secondary_reasons\":[],\"urgency\":\"MEDIUM\"}",
    "error": null,
    "latency_s": 5.5507,
    "simple_output": "Reason: TEMPORARY_SEASONAL_CHANGE | Urgency: LOW | Action: MONITOR | Why: Temporary seasonal change is the most supported explanation for the risk signal. Evidence suggests this because complaints_30d=0, unresolved_complaints=0, avg_resolution_time_hrs=0."
  }
}
```

### Farhan Bhalla (`C11586`)

- OK: `True`
- Shape errors: `[]`
- Simple output: Reason: SERVICE_DISSATISFACTION | Urgency: MEDIUM | Action: SERVICE_RECOVERY | Why: Complaint escalation because complaints_30d=1 and avg_resolution_time_hrs=47.7 suggest a service issue without clear escalation-level evidence.

Request:

```json
{
  "customer_id": "C11586",
  "customer_name": "Farhan Bhalla",
  "prediction_date": "2026-05-01",
  "snapshot_date": "2026-05-01",
  "target_month": "2026-06-01",
  "profile": {
    "tenure_months": 124,
    "customer_segment": "pension",
    "income_regularity": "regular",
    "products_count": 2,
    "has_credit_card": 0,
    "has_loan": 0
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 2,
      "balance_change_30d": -7.934,
      "transaction_change_30d": -18.2618,
      "card_spend_change_30d": -13.0673,
      "app_login_change_30d": -14.7619,
      "salary_missing_days": 3.0,
      "external_transfer_change_30d": 55.3284,
      "upi_share_of_spend": 0.6987,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 0,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 0.0,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-02-01",
      "days_since_last_transaction": 1,
      "balance_change_30d": -4.1097,
      "transaction_change_30d": -12.8991,
      "card_spend_change_30d": 2.8682,
      "app_login_change_30d": 8.2026,
      "salary_missing_days": 2.0,
      "external_transfer_change_30d": 8.9765,
      "upi_share_of_spend": 0.661,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 0,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 0.0,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-03-01",
      "days_since_last_transaction": 9,
      "balance_change_30d": -12.5577,
      "transaction_change_30d": 7.0673,
      "card_spend_change_30d": -10.367,
      "app_login_change_30d": 0.6747,
      "salary_missing_days": 2.0,
      "external_transfer_change_30d": 45.7492,
      "upi_share_of_spend": 0.7978,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 2,
      "avg_resolution_time_hrs": 27.7751,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-04-01",
      "days_since_last_transaction": 14,
      "balance_change_30d": -39.4118,
      "transaction_change_30d": -26.8493,
      "card_spend_change_30d": -30.4073,
      "app_login_change_30d": -18.4395,
      "salary_missing_days": 4.0,
      "external_transfer_change_30d": 28.1115,
      "upi_share_of_spend": 0.7684,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 27.0497,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-05-01",
      "days_since_last_transaction": 19,
      "balance_change_30d": -51.1523,
      "transaction_change_30d": -53.0375,
      "card_spend_change_30d": -28.0792,
      "app_login_change_30d": -51.8445,
      "salary_missing_days": 7.0,
      "external_transfer_change_30d": 77.0187,
      "upi_share_of_spend": 0.9531,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 3,
      "avg_resolution_time_hrs": 47.7295,
      "emi_bounce_30d": 0
    }
  ],
  "customer": {
    "tenure_months": 124,
    "customer_segment": "pension",
    "income_regularity": "regular",
    "products_count": 2,
    "has_credit_card": 0,
    "has_loan": 0,
    "days_since_last_transaction": 19,
    "balance_change_30d": -51.1523,
    "transaction_change_30d": -53.0375,
    "card_spend_change_30d": -28.0792,
    "app_login_change_30d": -51.8445,
    "salary_missing_days": 7.0,
    "external_transfer_change_30d": 77.0187,
    "upi_share_of_spend": 0.9531,
    "fd_maturing_in_30d": 0,
    "products_dropped_90d": 0,
    "complaints_30d": 1,
    "unresolved_complaints": 0,
    "failed_transactions_30d": 3,
    "avg_resolution_time_hrs": 47.7295,
    "emi_bounce_30d": 0
  },
  "extra_context": {
    "customer_profile": {
      "segment": "pension",
      "income_regularity": "regular",
      "tenure_months": 124,
      "age": 78,
      "customer_yearly_value": 8575.7788,
      "products_count": 2,
      "has_credit_card": 0,
      "has_loan": 0,
      "value_tier": "low"
    },
    "recent_complaint_text": "Follow up done. Customer still waiting on ATM dispute from last quarter."
  }
}
```

Response:

```json
{
  "meta": {
    "endpoint": "/predict/both",
    "served_at": "2026-08-31T01:41:53",
    "elapsed_ms": 7189.93,
    "timings_ms": {
      "model1": 82.43,
      "model2": 7107.37
    },
    "customer_id": "C11586",
    "customer_name": "Farhan Bhalla",
    "snapshot_date": "2026-05-01"
  },
  "model1": {
    "churn_probability": 40.95,
    "raw_churn_probability": 94.15,
    "probability_mode": "sigmoid",
    "risk_score": 77.86,
    "churn_prediction": "Yes",
    "risk_level": "High",
    "top_risk_factors": [
      {
        "factor": "latest_days_since_last_transaction",
        "value": 19,
        "message": "Customer has gone longer without transacting.",
        "contribution": 0.5498703122138977
      },
      {
        "factor": "latest_transaction_change_30d",
        "value": -53.0375,
        "message": "Transaction activity has been falling across recent months.",
        "contribution": 0.4067476987838745
      },
      {
        "factor": "latest_vs_avg_upi_share_of_spend_available_history",
        "value": 0.1772999999999999,
        "message": "A larger share of spending is happening through UPI.",
        "contribution": 0.2186962515115738
      },
      {
        "factor": "latest_salary_missing_days",
        "value": 7.0,
        "message": "Salary or pension was delayed recently.",
        "contribution": 0.21655915677547455
      },
      {
        "factor": "latest_balance_change_30d",
        "value": -51.1523,
        "message": "Balance has been falling across recent months.",
        "contribution": 0.18680596351623535
      }
    ]
  },
  "model2_input": {
    "customer_context": {
      "age": 78,
      "tenure_months": 124,
      "customer_segment": "pension",
      "income_regularity": "regular",
      "customer_yearly_value": 8575.7788,
      "products_count": 2,
      "has_credit_card": 0,
      "has_loan": 0
    },
    "behavior": {
      "days_since_last_transaction": 19,
      "balance_change_30d": -51.1523,
      "transaction_change_30d": -53.0375,
      "card_spend_change_30d": -28.0792,
      "app_login_change_30d": -51.8445,
      "salary_missing_days": 7,
      "external_transfer_change_30d": 77.0187,
      "upi_share_of_spend": 0.9531,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "emi_bounce_30d": 0
    },
    "service_evidence": {
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 3,
      "avg_resolution_time_hrs": 47.7295,
      "complaint_text": "Follow up done. Customer still waiting on ATM dispute from last quarter."
    },
    "model1": {
      "churn_probability": 0.4095,
      "churn_prediction": "Yes",
      "risk_level": "High",
      "top_risk_factors": [
        {
          "factor": "days_since_last_transaction",
          "value": 19
        },
        {
          "factor": "transaction_change_30d",
          "value": -53.0375
        },
        {
          "factor": "upi_share_of_spend",
          "value": 0.9531
        }
      ]
    },
    "eligible_actions": [
      "FINANCIAL_GUIDANCE",
      "SERVICE_RECOVERY",
      "PRODUCT_REVIEW",
      "RE_ENGAGEMENT",
      "MONITOR"
    ],
    "case_id": "C11586"
  },
  "model2": {
    "case_id": "C11586",
    "ok": true,
    "prediction": {
      "evidence": [
        "complaints_30d=1",
        "unresolved_complaints=0",
        "avg_resolution_time_hrs=47.7",
        "transaction_change_30d=-53.0",
        "card_spend_change_30d=-28.1",
        "complaint_text describes a recent service issue"
      ],
      "primary_reason": "SERVICE_DISSATISFACTION",
      "reasoning_summary": "Complaint escalation because complaints_30d=1 and avg_resolution_time_hrs=47.7 suggest a service issue without clear escalation-level evidence.",
      "recommended_action": "SERVICE_RECOVERY",
      "secondary_reasons": [],
      "urgency": "MEDIUM"
    },
    "warnings": [
      "evidence: 'unresolved_complaints=0' cites a zero/null value, which is not evidence; remove it",
      "reasoning_summary: describes COMPLAINT_ESCALATION but recommended_action is SERVICE_RECOVERY; rewrite the summary around the action you chose"
    ],
    "raw_text": "{\"evidence\":[\"complaints_30d=1\",\"unresolved_complaints=0\",\"avg_resolution_time_hrs=47.7\",\"complaint_text describes a real issue without clear escalation-level severity\"],\"primary_reason\":\"SERVICE_DISSATISFACTION\",\"reasoning_summary\":\"Complaint escalation because complaints_30d=1 and avg_resolution_time_hrs=47.7 suggest the service is dissatisfied or a complaint may need to be escalated.\",\"recommended_action\":\"SERVICE_RECOVERY\",\"secondary_reasons\":[],\"urgency\":\"HIGH\"}",
    "error": null,
    "latency_s": 7.1073,
    "simple_output": "Reason: SERVICE_DISSATISFACTION | Urgency: MEDIUM | Action: SERVICE_RECOVERY | Why: Complaint escalation because complaints_30d=1 and avg_resolution_time_hrs=47.7 suggest a service issue without clear escalation-level evidence."
  }
}
```

### Neel Bir (`C13120`)

- OK: `True`
- Shape errors: `[]`
- Simple output: Reason: FINANCIAL_STRESS | Urgency: MEDIUM | Action: FINANCIAL_GUIDANCE | Why: Evidence suggests this because complaint_text is null, unresolved_complaints=0, avg_resolution_time_hrs=0.0 and transaction_change_30d=27.0. Evidence weighs against secondary_reasons=[SERVICE_DISSATISFACTION, DIGITAL_FRICTION]. Recommendation: FINANCIAL_GUIDANCE

Request:

```json
{
  "customer_id": "C13120",
  "customer_name": "Neel Bir",
  "prediction_date": "2026-01-01",
  "snapshot_date": "2026-01-01",
  "target_month": "2026-02-01",
  "profile": {
    "tenure_months": 6,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 3,
    "has_credit_card": 0,
    "has_loan": 1
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 5,
      "balance_change_30d": 18.6211,
      "transaction_change_30d": 26.9888,
      "card_spend_change_30d": 14.7369,
      "app_login_change_30d": 9.5853,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -19.2093,
      "upi_share_of_spend": 0.2392,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 0,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 2,
      "avg_resolution_time_hrs": 0.0,
      "emi_bounce_30d": 1
    }
  ],
  "customer": {
    "tenure_months": 6,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 3,
    "has_credit_card": 0,
    "has_loan": 1,
    "days_since_last_transaction": 5,
    "balance_change_30d": 18.6211,
    "transaction_change_30d": 26.9888,
    "card_spend_change_30d": 14.7369,
    "app_login_change_30d": 9.5853,
    "salary_missing_days": 0.0,
    "external_transfer_change_30d": -19.2093,
    "upi_share_of_spend": 0.2392,
    "fd_maturing_in_30d": 0,
    "products_dropped_90d": 0,
    "complaints_30d": 0,
    "unresolved_complaints": 0,
    "failed_transactions_30d": 2,
    "avg_resolution_time_hrs": 0.0,
    "emi_bounce_30d": 1
  },
  "extra_context": {
    "customer_profile": {
      "segment": "salary",
      "income_regularity": "regular",
      "tenure_months": 6,
      "age": 24,
      "customer_yearly_value": 45559.2903,
      "products_count": 3,
      "has_credit_card": 0,
      "has_loan": 1,
      "value_tier": "medium"
    },
    "recent_complaint_text": null
  }
}
```

Response:

```json
{
  "meta": {
    "endpoint": "/predict/both",
    "served_at": "2026-08-31T01:41:57",
    "elapsed_ms": 3192.58,
    "timings_ms": {
      "model1": 74.86,
      "model2": 3117.57
    },
    "customer_id": "C13120",
    "customer_name": "Neel Bir",
    "snapshot_date": "2026-01-01"
  },
  "model1": {
    "churn_probability": 2.06,
    "raw_churn_probability": 19.1,
    "probability_mode": "sigmoid",
    "risk_score": 6.18,
    "churn_prediction": "No",
    "risk_level": "Low",
    "top_risk_factors": [
      {
        "factor": "avg_upi_share_of_spend_6m",
        "value": 0.2392,
        "message": "A larger share of spending is happening through UPI.",
        "contribution": 0.018367400392889977
      },
      {
        "factor": "transaction_change_30d_trend_6m",
        "value": 0.0,
        "message": "This signal increased churn risk.",
        "contribution": 0.01746944524347782
      },
      {
        "factor": "sum_emi_bounce_30d_3m",
        "value": 1.0,
        "message": "Customer has a recent EMI bounce.",
        "contribution": 0.014771189540624619
      },
      {
        "factor": "count_external_transfer_rise_6m",
        "value": 0,
        "message": "This signal increased churn risk.",
        "contribution": 0.012359191663563251
      },
      {
        "factor": "latest_vs_avg_card_spend_change_30d_available_history",
        "value": 0.0,
        "message": "This signal increased churn risk.",
        "contribution": 0.006343191023916006
      }
    ]
  },
  "model2_input": {
    "customer_context": {
      "age": 24,
      "tenure_months": 6,
      "customer_segment": "salary",
      "income_regularity": "regular",
      "customer_yearly_value": 45559.2903,
      "products_count": 3,
      "has_credit_card": 0,
      "has_loan": 1
    },
    "behavior": {
      "days_since_last_transaction": 5,
      "balance_change_30d": 18.6211,
      "transaction_change_30d": 26.9888,
      "card_spend_change_30d": 14.7369,
      "app_login_change_30d": 9.5853,
      "salary_missing_days": 0,
      "external_transfer_change_30d": -19.2093,
      "upi_share_of_spend": 0.2392,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "emi_bounce_30d": 1
    },
    "service_evidence": {
      "complaints_30d": 0,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 2,
      "avg_resolution_time_hrs": 0.0,
      "complaint_text": null
    },
    "model1": {
      "churn_probability": 0.0206,
      "churn_prediction": "No",
      "risk_level": "Low",
      "top_risk_factors": [
        {
          "factor": "upi_share_of_spend",
          "value": 0.2392
        },
        {
          "factor": "transaction_change_30d",
          "value": 26.9888
        },
        {
          "factor": "emi_bounce_30d",
          "value": 1
        }
      ]
    },
    "eligible_actions": [
      "LOAN_REVIEW",
      "FINANCIAL_GUIDANCE",
      "SERVICE_RECOVERY",
      "MONITOR"
    ],
    "case_id": "C13120"
  },
  "model2": {
    "case_id": "C13120",
    "ok": true,
    "prediction": {
      "evidence": [
        "emi_bounce_30d=1",
        "transaction_change_30d=27.0",
        "app_login_change_30d=9.6"
      ],
      "primary_reason": "FINANCIAL_STRESS",
      "reasoning_summary": "Evidence suggests this because complaint_text is null, unresolved_complaints=0, avg_resolution_time_hrs=0.0 and transaction_change_30d=27.0. Evidence weighs against secondary_reasons=[SERVICE_DISSATISFACTION, DIGITAL_FRICTION]. Recommendation: FINANCIAL_GUIDANCE",
      "recommended_action": "FINANCIAL_GUIDANCE",
      "secondary_reasons": [],
      "urgency": "MEDIUM"
    },
    "warnings": [],
    "raw_text": "{\n    \"evidence\": [\n        \"emi_bounce_30d=1\",\n        \"transaction_change_30d=27.0\",\n        \"app_login_change_30d=9.6\"\n    ],\n    \"primary_reason\": \"FINANCIAL_STRESS\",\n    \"reasoning_summary\": \"Evidence suggests this because complaint_text is null, unresolved_complaints=0, avg_resolution_time_hrs=0.0 and transaction_change_30d=27.0. Evidence weighs against secondary_reasons=[SERVICE_DISSATISFACTION, DIGITAL_FRICTION]. Recommendation: FINANCIAL_GUIDANCE\",\n    \"recommended_action\": \"FINANCIAL_GUIDANCE\",\n    \"secondary_reasons\": [],\n    \"urgency\": \"MEDIUM\"\n}",
    "error": null,
    "latency_s": 3.1175,
    "simple_output": "Reason: FINANCIAL_STRESS | Urgency: MEDIUM | Action: FINANCIAL_GUIDANCE | Why: Evidence suggests this because complaint_text is null, unresolved_complaints=0, avg_resolution_time_hrs=0.0 and transaction_change_30d=27.0. Evidence weighs against secondary_reasons=[SERVICE_DISSATISFACTION, DIGITAL_FRICTION]. Recommendation: FINANCIAL_GUIDANCE"
  }
}
```

### Bhavani Deep (`C13262`)

- OK: `True`
- Shape errors: `[]`
- Simple output: Reason: UNKNOWN | Urgency: LOW | Action: MONITOR | Why: Complaint and resolution signals are mixed or weak; evidence is genuinely unclear.

Request:

```json
{
  "customer_id": "C13262",
  "customer_name": "Bhavani Deep",
  "prediction_date": "2026-06-01",
  "snapshot_date": "2026-06-01",
  "target_month": "2026-07-01",
  "profile": {
    "tenure_months": 79,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 2,
    "has_credit_card": 1,
    "has_loan": 0
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 6,
      "balance_change_30d": -7.5439,
      "transaction_change_30d": -0.8912,
      "card_spend_change_30d": -10.5402,
      "app_login_change_30d": 10.0531,
      "salary_missing_days": 2.0,
      "external_transfer_change_30d": 12.8859,
      "upi_share_of_spend": 0.2458,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 6.5142,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-02-01",
      "days_since_last_transaction": 8,
      "balance_change_30d": 35.1944,
      "transaction_change_30d": 4.0124,
      "card_spend_change_30d": 0.2083,
      "app_login_change_30d": -6.2015,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -10.4291,
      "upi_share_of_spend": 0.0953,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 1,
      "complaints_30d": 0,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 0.0,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-03-01",
      "days_since_last_transaction": 0,
      "balance_change_30d": 1.2428,
      "transaction_change_30d": 10.1332,
      "card_spend_change_30d": 23.8427,
      "app_login_change_30d": 6.8349,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -1.1543,
      "upi_share_of_spend": 0.0265,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 0,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 0.0,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-04-01",
      "days_since_last_transaction": 1,
      "balance_change_30d": 5.4595,
      "transaction_change_30d": 33.5672,
      "card_spend_change_30d": 13.0714,
      "app_login_change_30d": 7.1917,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -15.2583,
      "upi_share_of_spend": 0.068,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 0,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 0.0,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-05-01",
      "days_since_last_transaction": 1,
      "balance_change_30d": 21.4278,
      "transaction_change_30d": -3.7673,
      "card_spend_change_30d": 31.0633,
      "app_login_change_30d": 10.3658,
      "salary_missing_days": 1.0,
      "external_transfer_change_30d": 5.261,
      "upi_share_of_spend": 0.0432,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 0,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 0.0,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-06-01",
      "days_since_last_transaction": 1,
      "balance_change_30d": 23.51,
      "transaction_change_30d": 29.1971,
      "card_spend_change_30d": 39.8212,
      "app_login_change_30d": 38.7213,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -27.6671,
      "upi_share_of_spend": 0.049,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 0,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 2,
      "avg_resolution_time_hrs": 0.0,
      "emi_bounce_30d": 0
    }
  ],
  "customer": {
    "tenure_months": 79,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 2,
    "has_credit_card": 1,
    "has_loan": 0,
    "days_since_last_transaction": 1,
    "balance_change_30d": 23.51,
    "transaction_change_30d": 29.1971,
    "card_spend_change_30d": 39.8212,
    "app_login_change_30d": 38.7213,
    "salary_missing_days": 0.0,
    "external_transfer_change_30d": -27.6671,
    "upi_share_of_spend": 0.049,
    "fd_maturing_in_30d": 0,
    "products_dropped_90d": 0,
    "complaints_30d": 0,
    "unresolved_complaints": 0,
    "failed_transactions_30d": 2,
    "avg_resolution_time_hrs": 0.0,
    "emi_bounce_30d": 0
  },
  "extra_context": {
    "customer_profile": {
      "segment": "salary",
      "income_regularity": "regular",
      "tenure_months": 79,
      "age": 35,
      "customer_yearly_value": 33227.437,
      "products_count": 2,
      "has_credit_card": 1,
      "has_loan": 0,
      "value_tier": "low"
    },
    "recent_complaint_text": null
  }
}
```

Response:

```json
{
  "meta": {
    "endpoint": "/predict/both",
    "served_at": "2026-08-31T01:42:02",
    "elapsed_ms": 5113.6,
    "timings_ms": {
      "model1": 148.35,
      "model2": 4965.11
    },
    "customer_id": "C13262",
    "customer_name": "Bhavani Deep",
    "snapshot_date": "2026-06-01"
  },
  "model1": {
    "churn_probability": 1.97,
    "raw_churn_probability": 18.12,
    "probability_mode": "sigmoid",
    "risk_score": 5.91,
    "churn_prediction": "No",
    "risk_level": "Low",
    "top_risk_factors": [
      {
        "factor": "card_spend_change_30d_trend_6m",
        "value": 9.531448571428568,
        "message": "This signal increased churn risk.",
        "contribution": 0.04914986714720726
      },
      {
        "factor": "latest_upi_share_of_spend",
        "value": 0.049,
        "message": "A larger share of spending is happening through UPI.",
        "contribution": 0.03397022932767868
      },
      {
        "factor": "avg_transaction_change_30d_6m",
        "value": 12.0419,
        "message": "This signal increased churn risk.",
        "contribution": 0.018631968647241592
      },
      {
        "factor": "count_external_transfer_rise_6m",
        "value": 0,
        "message": "This signal increased churn risk.",
        "contribution": 0.017085939645767212
      },
      {
        "factor": "avg_upi_share_of_spend_6m",
        "value": 0.08796666666666668,
        "message": "A larger share of spending is happening through UPI.",
        "contribution": 0.015266149304807186
      }
    ]
  },
  "model2_input": {
    "customer_context": {
      "age": 35,
      "tenure_months": 79,
      "customer_segment": "salary",
      "income_regularity": "regular",
      "customer_yearly_value": 33227.437,
      "products_count": 2,
      "has_credit_card": 1,
      "has_loan": 0
    },
    "behavior": {
      "days_since_last_transaction": 1,
      "balance_change_30d": 23.51,
      "transaction_change_30d": 29.1971,
      "card_spend_change_30d": 39.8212,
      "app_login_change_30d": 38.7213,
      "salary_missing_days": 0,
      "external_transfer_change_30d": -27.6671,
      "upi_share_of_spend": 0.049,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "emi_bounce_30d": 0
    },
    "service_evidence": {
      "complaints_30d": 0,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 2,
      "avg_resolution_time_hrs": 0.0,
      "complaint_text": null
    },
    "model1": {
      "churn_probability": 0.0197,
      "churn_prediction": "No",
      "risk_level": "Low",
      "top_risk_factors": [
        {
          "factor": "card_spend_change_30d",
          "value": 39.8212
        },
        {
          "factor": "upi_share_of_spend",
          "value": 0.049
        },
        {
          "factor": "transaction_change_30d",
          "value": 29.1971
        }
      ]
    },
    "eligible_actions": [
      "SERVICE_RECOVERY",
      "RE_ENGAGEMENT",
      "MONITOR"
    ],
    "case_id": "C13262"
  },
  "model2": {
    "case_id": "C13262",
    "ok": true,
    "prediction": {
      "evidence": [
        "complaints_30d=0",
        "unresolved_complaints=0",
        "avg_resolution_time_hrs=0.0"
      ],
      "primary_reason": "UNKNOWN",
      "reasoning_summary": "Complaint and resolution signals are mixed or weak; evidence is genuinely unclear.",
      "recommended_action": "MONITOR",
      "secondary_reasons": [],
      "urgency": "LOW"
    },
    "warnings": [
      "evidence: 'complaints_30d=0' cites a zero/null value, which is not evidence; remove it",
      "evidence: 'unresolved_complaints=0' cites a zero/null value, which is not evidence; remove it",
      "evidence: 'avg_resolution_time_hrs=0.0' cites a zero/null value, which is not evidence; remove it"
    ],
    "raw_text": "{\"evidence\":[\"complaints_30d=0\",\"unresolved_complaints=0\",\"avg_resolution_time_hrs=0.0\"],\"primary_reason\":\"LOW_ENGAGEMENT\",\"reasoning_summary\":\"Days_since_last_transaction=1 and transaction_change_30d=29.2 suggest this because complaint_text is null.\",\"recommended_action\":\"RE_ENGAGEMENT\",\"secondary_reasons\":[],\"urgency\":\"MEDIUM\"}",
    "error": null,
    "latency_s": 4.9651,
    "simple_output": "Reason: UNKNOWN | Urgency: LOW | Action: MONITOR | Why: Complaint and resolution signals are mixed or weak; evidence is genuinely unclear."
  }
}
```

### Sudiksha Khatri (`C16707`)

- OK: `False`
- Shape errors: `[]`
- Simple output: None

Request:

```json
{
  "customer_id": "C16707",
  "customer_name": "Sudiksha Khatri",
  "prediction_date": "2026-06-01",
  "snapshot_date": "2026-06-01",
  "target_month": "2026-07-01",
  "profile": {
    "tenure_months": 217,
    "customer_segment": "farmer",
    "income_regularity": "seasonal",
    "products_count": 1,
    "has_credit_card": 0,
    "has_loan": 0
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 1,
      "balance_change_30d": -3.811,
      "transaction_change_30d": 3.331,
      "card_spend_change_30d": 9.4088,
      "app_login_change_30d": -5.8592,
      "salary_missing_days": null,
      "external_transfer_change_30d": 20.8142,
      "upi_share_of_spend": 0.1561,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 0,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 3,
      "avg_resolution_time_hrs": 0.0,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-02-01",
      "days_since_last_transaction": 1,
      "balance_change_30d": -8.1656,
      "transaction_change_30d": 10.8743,
      "card_spend_change_30d": 32.0417,
      "app_login_change_30d": -9.5039,
      "salary_missing_days": null,
      "external_transfer_change_30d": 23.9718,
      "upi_share_of_spend": 0.3428,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 0,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 0.0,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-03-01",
      "days_since_last_transaction": 0,
      "balance_change_30d": 19.6384,
      "transaction_change_30d": 8.6137,
      "card_spend_change_30d": 31.9976,
      "app_login_change_30d": 26.3109,
      "salary_missing_days": null,
      "external_transfer_change_30d": 17.7085,
      "upi_share_of_spend": 0.1203,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 0,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 0.0,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-04-01",
      "days_since_last_transaction": 0,
      "balance_change_30d": 2.8485,
      "transaction_change_30d": 27.3592,
      "card_spend_change_30d": 17.3398,
      "app_login_change_30d": 27.6655,
      "salary_missing_days": null,
      "external_transfer_change_30d": -33.5788,
      "upi_share_of_spend": 0.0729,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 0,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 0.0,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-05-01",
      "days_since_last_transaction": 0,
      "balance_change_30d": 20.7369,
      "transaction_change_30d": 10.6187,
      "card_spend_change_30d": 43.4432,
      "app_login_change_30d": 11.2069,
      "salary_missing_days": null,
      "external_transfer_change_30d": -31.8945,
      "upi_share_of_spend": 0.0781,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 0,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 0.0,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-06-01",
      "days_since_last_transaction": 0,
      "balance_change_30d": 27.0311,
      "transaction_change_30d": 17.1254,
      "card_spend_change_30d": 10.3722,
      "app_login_change_30d": 26.6521,
      "salary_missing_days": null,
      "external_transfer_change_30d": 9.5041,
      "upi_share_of_spend": 0.1558,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 0,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 0.0,
      "emi_bounce_30d": 0
    }
  ],
  "customer": {
    "tenure_months": 217,
    "customer_segment": "farmer",
    "income_regularity": "seasonal",
    "products_count": 1,
    "has_credit_card": 0,
    "has_loan": 0,
    "days_since_last_transaction": 0,
    "balance_change_30d": 27.0311,
    "transaction_change_30d": 17.1254,
    "card_spend_change_30d": 10.3722,
    "app_login_change_30d": 26.6521,
    "salary_missing_days": null,
    "external_transfer_change_30d": 9.5041,
    "upi_share_of_spend": 0.1558,
    "fd_maturing_in_30d": 0,
    "products_dropped_90d": 0,
    "complaints_30d": 0,
    "unresolved_complaints": 0,
    "failed_transactions_30d": 0,
    "avg_resolution_time_hrs": 0.0,
    "emi_bounce_30d": 0
  },
  "extra_context": {
    "customer_profile": {
      "segment": "farmer",
      "income_regularity": "seasonal",
      "tenure_months": 217,
      "age": 61,
      "customer_yearly_value": 43642.3229,
      "products_count": 1,
      "has_credit_card": 0,
      "has_loan": 0,
      "value_tier": "medium"
    },
    "recent_complaint_text": null
  }
}
```

Response:

```json
{
  "error": "[WinError 10054] An existing connection was forcibly closed by the remote host"
}
```

### Onveer Setty (`C16974`)

- OK: `False`
- Shape errors: `[]`
- Simple output: None

Request:

```json
{
  "customer_id": "C16974",
  "customer_name": "Onveer Setty",
  "prediction_date": "2026-03-01",
  "snapshot_date": "2026-03-01",
  "target_month": "2026-04-01",
  "profile": {
    "tenure_months": 50,
    "customer_segment": "vendor",
    "income_regularity": "irregular",
    "products_count": 3,
    "has_credit_card": 0,
    "has_loan": 0
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 1,
      "balance_change_30d": -1.6318,
      "transaction_change_30d": 5.1814,
      "card_spend_change_30d": 28.3122,
      "app_login_change_30d": 14.5354,
      "salary_missing_days": null,
      "external_transfer_change_30d": -3.794,
      "upi_share_of_spend": 0.5396,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 2,
      "unresolved_complaints": 2,
      "failed_transactions_30d": 2,
      "avg_resolution_time_hrs": 47.9191,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-02-01",
      "days_since_last_transaction": 4,
      "balance_change_30d": -0.1672,
      "transaction_change_30d": -10.4025,
      "card_spend_change_30d": 3.9691,
      "app_login_change_30d": -9.6095,
      "salary_missing_days": null,
      "external_transfer_change_30d": -6.3192,
      "upi_share_of_spend": 0.5845,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 5,
      "unresolved_complaints": 3,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 55.7761,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-03-01",
      "days_since_last_transaction": 5,
      "balance_change_30d": 15.1795,
      "transaction_change_30d": -4.8482,
      "card_spend_change_30d": -36.6984,
      "app_login_change_30d": 24.2244,
      "salary_missing_days": null,
      "external_transfer_change_30d": 22.1922,
      "upi_share_of_spend": 0.6662,
      "fd_maturing_in_30d": 1,
      "products_dropped_90d": 0,
      "complaints_30d": 6,
      "unresolved_complaints": 6,
      "failed_transactions_30d": 4,
      "avg_resolution_time_hrs": 129.1931,
      "emi_bounce_30d": 0
    }
  ],
  "customer": {
    "tenure_months": 50,
    "customer_segment": "vendor",
    "income_regularity": "irregular",
    "products_count": 3,
    "has_credit_card": 0,
    "has_loan": 0,
    "days_since_last_transaction": 5,
    "balance_change_30d": 15.1795,
    "transaction_change_30d": -4.8482,
    "card_spend_change_30d": -36.6984,
    "app_login_change_30d": 24.2244,
    "salary_missing_days": null,
    "external_transfer_change_30d": 22.1922,
    "upi_share_of_spend": 0.6662,
    "fd_maturing_in_30d": 1,
    "products_dropped_90d": 0,
    "complaints_30d": 6,
    "unresolved_complaints": 6,
    "failed_transactions_30d": 4,
    "avg_resolution_time_hrs": 129.1931,
    "emi_bounce_30d": 0
  },
  "extra_context": {
    "customer_profile": {
      "segment": "vendor",
      "income_regularity": "irregular",
      "tenure_months": 50,
      "age": 48,
      "customer_yearly_value": 9158.2073,
      "products_count": 3,
      "has_credit_card": 0,
      "has_loan": 0,
      "value_tier": "low"
    },
    "recent_complaint_text": "Card ka number galat print hua hai. Branch ne bola online complaint karo."
  }
}
```

Response:

```json
{
  "error": "Could not call http://127.0.0.1:8001/predict/both: <urlopen error [WinError 10061] No connection could be made because the target machine actively refused it>"
}
```

### Daksha Parekh (`C16975`)

- OK: `False`
- Shape errors: `[]`
- Simple output: None

Request:

```json
{
  "customer_id": "C16975",
  "customer_name": "Daksha Parekh",
  "prediction_date": "2026-06-01",
  "snapshot_date": "2026-06-01",
  "target_month": "2026-07-01",
  "profile": {
    "tenure_months": 55,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 3,
    "has_credit_card": 1,
    "has_loan": 0
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 0,
      "balance_change_30d": 42.8921,
      "transaction_change_30d": 19.6282,
      "card_spend_change_30d": 11.655,
      "app_login_change_30d": 6.0247,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": 15.1825,
      "upi_share_of_spend": 0.6782,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 0,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 0.0,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-02-01",
      "days_since_last_transaction": 0,
      "balance_change_30d": -13.5944,
      "transaction_change_30d": -16.7331,
      "card_spend_change_30d": 11.3219,
      "app_login_change_30d": -0.7962,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": 31.067,
      "upi_share_of_spend": 0.7644,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 30.8654,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-03-01",
      "days_since_last_transaction": 0,
      "balance_change_30d": 4.7424,
      "transaction_change_30d": -14.81,
      "card_spend_change_30d": 26.1211,
      "app_login_change_30d": -3.1147,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": 12.985,
      "upi_share_of_spend": 0.822,
      "fd_maturing_in_30d": 1,
      "products_dropped_90d": 0,
      "complaints_30d": 0,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 0.0,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-04-01",
      "days_since_last_transaction": 0,
      "balance_change_30d": 20.6111,
      "transaction_change_30d": 32.225,
      "card_spend_change_30d": 23.1315,
      "app_login_change_30d": 20.6147,
      "salary_missing_days": 2.0,
      "external_transfer_change_30d": 10.1661,
      "upi_share_of_spend": 0.6526,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 0,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 0.0,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-05-01",
      "days_since_last_transaction": 0,
      "balance_change_30d": -18.9587,
      "transaction_change_30d": 1.3978,
      "card_spend_change_30d": -11.6282,
      "app_login_change_30d": 4.1923,
      "salary_missing_days": 2.0,
      "external_transfer_change_30d": -31.7076,
      "upi_share_of_spend": 0.7397,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 0,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 3,
      "avg_resolution_time_hrs": 0.0,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-06-01",
      "days_since_last_transaction": 0,
      "balance_change_30d": 7.239,
      "transaction_change_30d": 26.478,
      "card_spend_change_30d": 4.0425,
      "app_login_change_30d": 9.5869,
      "salary_missing_days": 1.0,
      "external_transfer_change_30d": -18.2657,
      "upi_share_of_spend": 0.7371,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 0,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 0.0,
      "emi_bounce_30d": 0
    }
  ],
  "customer": {
    "tenure_months": 55,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 3,
    "has_credit_card": 1,
    "has_loan": 0,
    "days_since_last_transaction": 0,
    "balance_change_30d": 7.239,
    "transaction_change_30d": 26.478,
    "card_spend_change_30d": 4.0425,
    "app_login_change_30d": 9.5869,
    "salary_missing_days": 1.0,
    "external_transfer_change_30d": -18.2657,
    "upi_share_of_spend": 0.7371,
    "fd_maturing_in_30d": 0,
    "products_dropped_90d": 0,
    "complaints_30d": 0,
    "unresolved_complaints": 0,
    "failed_transactions_30d": 0,
    "avg_resolution_time_hrs": 0.0,
    "emi_bounce_30d": 0
  },
  "extra_context": {
    "customer_profile": {
      "segment": "salary",
      "income_regularity": "regular",
      "tenure_months": 55,
      "age": 37,
      "customer_yearly_value": 52146.5375,
      "products_count": 3,
      "has_credit_card": 1,
      "has_loan": 0,
      "value_tier": "medium"
    },
    "recent_complaint_text": null
  }
}
```

Response:

```json
{
  "error": "Could not call http://127.0.0.1:8001/predict/both: <urlopen error [WinError 10061] No connection could be made because the target machine actively refused it>"
}
```

### Peter Gulati (`C17247`)

- OK: `False`
- Shape errors: `[]`
- Simple output: None

Request:

```json
{
  "customer_id": "C17247",
  "customer_name": "Peter Gulati",
  "prediction_date": "2026-05-01",
  "snapshot_date": "2026-05-01",
  "target_month": "2026-06-01",
  "profile": {
    "tenure_months": 14,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 3,
    "has_credit_card": 1,
    "has_loan": 1
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 4,
      "balance_change_30d": 18.5415,
      "transaction_change_30d": 7.7459,
      "card_spend_change_30d": 56.7985,
      "app_login_change_30d": 15.5318,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -51.2226,
      "upi_share_of_spend": 0.4609,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 0,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 0.0,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-02-01",
      "days_since_last_transaction": 12,
      "balance_change_30d": 17.8382,
      "transaction_change_30d": -5.9846,
      "card_spend_change_30d": 22.5242,
      "app_login_change_30d": 19.6772,
      "salary_missing_days": 2.0,
      "external_transfer_change_30d": 50.4917,
      "upi_share_of_spend": 0.5079,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 0,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 0.0,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-03-01",
      "days_since_last_transaction": 11,
      "balance_change_30d": 4.2909,
      "transaction_change_30d": 1.3254,
      "card_spend_change_30d": -0.3486,
      "app_login_change_30d": 15.9549,
      "salary_missing_days": 2.0,
      "external_transfer_change_30d": 17.5516,
      "upi_share_of_spend": 0.5808,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 0,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 0.0,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-04-01",
      "days_since_last_transaction": 17,
      "balance_change_30d": -18.8697,
      "transaction_change_30d": -7.8286,
      "card_spend_change_30d": -6.7069,
      "app_login_change_30d": -22.6943,
      "salary_missing_days": 3.0,
      "external_transfer_change_30d": 26.6245,
      "upi_share_of_spend": 0.5843,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 1,
      "complaints_30d": 0,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 0.0,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-05-01",
      "days_since_last_transaction": 23,
      "balance_change_30d": -21.8479,
      "transaction_change_30d": -36.9531,
      "card_spend_change_30d": -19.8936,
      "app_login_change_30d": -19.5964,
      "salary_missing_days": 7.0,
      "external_transfer_change_30d": 69.6979,
      "upi_share_of_spend": 0.6706,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 0,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 3,
      "avg_resolution_time_hrs": 0.0,
      "emi_bounce_30d": 0
    }
  ],
  "customer": {
    "tenure_months": 14,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 3,
    "has_credit_card": 1,
    "has_loan": 1,
    "days_since_last_transaction": 23,
    "balance_change_30d": -21.8479,
    "transaction_change_30d": -36.9531,
    "card_spend_change_30d": -19.8936,
    "app_login_change_30d": -19.5964,
    "salary_missing_days": 7.0,
    "external_transfer_change_30d": 69.6979,
    "upi_share_of_spend": 0.6706,
    "fd_maturing_in_30d": 0,
    "products_dropped_90d": 0,
    "complaints_30d": 0,
    "unresolved_complaints": 0,
    "failed_transactions_30d": 3,
    "avg_resolution_time_hrs": 0.0,
    "emi_bounce_30d": 0
  },
  "extra_context": {
    "customer_profile": {
      "segment": "salary",
      "income_regularity": "regular",
      "tenure_months": 14,
      "age": 33,
      "customer_yearly_value": 73741.6081,
      "products_count": 3,
      "has_credit_card": 1,
      "has_loan": 1,
      "value_tier": "medium"
    },
    "recent_complaint_text": null
  }
}
```

Response:

```json
{
  "error": "Could not call http://127.0.0.1:8001/predict/both: <urlopen error [WinError 10061] No connection could be made because the target machine actively refused it>"
}
```

### Bina Ahuja (`C17283`)

- OK: `True`
- Shape errors: `[]`
- Simple output: Reason: FEE_DISSATISFACTION | Urgency: MEDIUM | Action: FEE_WAIVER_REVIEW | Why: Complaint evidence suggests this may be a fee dissatisfaction issue.

Request:

```json
{
  "customer_id": "C17283",
  "customer_name": "Bina Ahuja",
  "prediction_date": "2026-06-01",
  "snapshot_date": "2026-06-01",
  "target_month": "2026-07-01",
  "profile": {
    "tenure_months": 128,
    "customer_segment": "farmer",
    "income_regularity": "seasonal",
    "products_count": 2,
    "has_credit_card": 0,
    "has_loan": 1
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 2,
      "balance_change_30d": 24.9343,
      "transaction_change_30d": 0.0074,
      "card_spend_change_30d": 50.2283,
      "app_login_change_30d": 5.1577,
      "salary_missing_days": null,
      "external_transfer_change_30d": 8.622,
      "upi_share_of_spend": 0.5335,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 0,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 0.0,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-02-01",
      "days_since_last_transaction": 11,
      "balance_change_30d": -8.8514,
      "transaction_change_30d": -5.7807,
      "card_spend_change_30d": 11.0108,
      "app_login_change_30d": -27.0264,
      "salary_missing_days": null,
      "external_transfer_change_30d": 24.7346,
      "upi_share_of_spend": 0.5457,
      "fd_maturing_in_30d": 1,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 14.6138,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-03-01",
      "days_since_last_transaction": 2,
      "balance_change_30d": 2.4601,
      "transaction_change_30d": -12.6446,
      "card_spend_change_30d": 4.8761,
      "app_login_change_30d": 5.9776,
      "salary_missing_days": null,
      "external_transfer_change_30d": 3.875,
      "upi_share_of_spend": 0.5183,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 0,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 0.0,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-04-01",
      "days_since_last_transaction": 0,
      "balance_change_30d": 10.9824,
      "transaction_change_30d": 4.1103,
      "card_spend_change_30d": 17.7612,
      "app_login_change_30d": 45.6803,
      "salary_missing_days": null,
      "external_transfer_change_30d": -18.5788,
      "upi_share_of_spend": 0.4421,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 0,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 0.0,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-05-01",
      "days_since_last_transaction": 0,
      "balance_change_30d": 41.1527,
      "transaction_change_30d": 17.4296,
      "card_spend_change_30d": 29.7525,
      "app_login_change_30d": 14.0575,
      "salary_missing_days": null,
      "external_transfer_change_30d": 2.0751,
      "upi_share_of_spend": 0.3284,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 2,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 37.5624,
      "emi_bounce_30d": 1
    },
    {
      "snapshot_date": "2026-06-01",
      "days_since_last_transaction": 0,
      "balance_change_30d": 44.5757,
      "transaction_change_30d": 17.2812,
      "card_spend_change_30d": 49.924,
      "app_login_change_30d": 5.5472,
      "salary_missing_days": null,
      "external_transfer_change_30d": -51.18,
      "upi_share_of_spend": 0.4221,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 1.0,
      "emi_bounce_30d": 0
    }
  ],
  "customer": {
    "tenure_months": 128,
    "customer_segment": "farmer",
    "income_regularity": "seasonal",
    "products_count": 2,
    "has_credit_card": 0,
    "has_loan": 1,
    "days_since_last_transaction": 0,
    "balance_change_30d": 44.5757,
    "transaction_change_30d": 17.2812,
    "card_spend_change_30d": 49.924,
    "app_login_change_30d": 5.5472,
    "salary_missing_days": null,
    "external_transfer_change_30d": -51.18,
    "upi_share_of_spend": 0.4221,
    "fd_maturing_in_30d": 0,
    "products_dropped_90d": 0,
    "complaints_30d": 1,
    "unresolved_complaints": 0,
    "failed_transactions_30d": 0,
    "avg_resolution_time_hrs": 1.0,
    "emi_bounce_30d": 0
  },
  "extra_context": {
    "customer_profile": {
      "segment": "farmer",
      "income_regularity": "seasonal",
      "tenure_months": 128,
      "age": 59,
      "customer_yearly_value": 26620.1538,
      "products_count": 2,
      "has_credit_card": 0,
      "has_loan": 1,
      "value_tier": "low"
    },
    "recent_complaint_text": "Kindly refund the ATM usage charges, I used your own bank ATM."
  }
}
```

Response:

```json
{
  "meta": {
    "endpoint": "/predict/both",
    "served_at": "2026-08-31T01:42:12",
    "elapsed_ms": 1875.82,
    "timings_ms": {
      "model1": 82.97,
      "model2": 1792.69
    },
    "customer_id": "C17283",
    "customer_name": "Bina Ahuja",
    "snapshot_date": "2026-06-01"
  },
  "model1": {
    "churn_probability": 1.83,
    "raw_churn_probability": 16.43,
    "probability_mode": "sigmoid",
    "risk_score": 5.48,
    "churn_prediction": "No",
    "risk_level": "Low",
    "top_risk_factors": [
      {
        "factor": "latest_vs_avg_external_transfer_change_30d_available_history",
        "value": -46.10465,
        "message": "This signal increased churn risk.",
        "contribution": 0.07049665600061417
      },
      {
        "factor": "latest_external_transfer_change_30d",
        "value": -51.18,
        "message": "This signal increased churn risk.",
        "contribution": 0.06947476416826248
      },
      {
        "factor": "latest_vs_avg_balance_change_30d_available_history",
        "value": 25.366733333333332,
        "message": "This signal increased churn risk.",
        "contribution": 0.05909287929534912
      },
      {
        "factor": "avg_app_login_change_30d_6m",
        "value": 8.232316666666668,
        "message": "This signal increased churn risk.",
        "contribution": 0.010799000971019268
      },
      {
        "factor": "sum_fd_maturing_in_30d_6m",
        "value": 1.0,
        "message": "Customer has a fixed deposit maturing soon.",
        "contribution": 0.007160181179642677
      }
    ]
  },
  "model2_input": {
    "customer_context": {
      "age": 59,
      "tenure_months": 128,
      "customer_segment": "farmer",
      "income_regularity": "seasonal",
      "customer_yearly_value": 26620.1538,
      "products_count": 2,
      "has_credit_card": 0,
      "has_loan": 1
    },
    "behavior": {
      "days_since_last_transaction": 0,
      "balance_change_30d": 44.5757,
      "transaction_change_30d": 17.2812,
      "card_spend_change_30d": 49.924,
      "app_login_change_30d": 5.5472,
      "salary_missing_days": null,
      "external_transfer_change_30d": -51.18,
      "upi_share_of_spend": 0.4221,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "emi_bounce_30d": 0
    },
    "service_evidence": {
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 1.0,
      "complaint_text": "Kindly refund the ATM usage charges, I used your own bank ATM."
    },
    "model1": {
      "churn_probability": 0.0183,
      "churn_prediction": "No",
      "risk_level": "Low",
      "top_risk_factors": [
        {
          "factor": "external_transfer_change_30d",
          "value": -51.18
        },
        {
          "factor": "balance_change_30d",
          "value": 44.5757
        },
        {
          "factor": "app_login_change_30d",
          "value": 5.5472
        }
      ]
    },
    "eligible_actions": [
      "FEE_WAIVER_REVIEW",
      "SERVICE_RECOVERY",
      "MONITOR"
    ],
    "case_id": "C17283"
  },
  "model2": {
    "case_id": "C17283",
    "ok": true,
    "prediction": {
      "evidence": [
        "complaints_30d=1",
        "avg_resolution_time_hrs=1.0",
        "complaint_text describes a recent fee or charge issue"
      ],
      "primary_reason": "FEE_DISSATISFACTION",
      "reasoning_summary": "Complaint evidence suggests this may be a fee dissatisfaction issue.",
      "recommended_action": "FEE_WAIVER_REVIEW",
      "secondary_reasons": [],
      "urgency": "MEDIUM"
    },
    "warnings": [],
    "raw_text": "{\"evidence\":[\"complaints_30d=1\",\"avg_resolution_time_hrs=1.0\",\"complaint_text describes a recent fee or charge issue\"],\"primary_reason\":\"FEE_DISSATISFACTION\",\"reasoning_summary\":\"Complaint evidence suggests this may be a fee dissatisfaction issue.\",\"recommended_action\":\"FEE_WAIVER_REVIEW\",\"secondary_reasons\":[],\"urgency\":\"MEDIUM\"}",
    "error": null,
    "latency_s": 1.7927,
    "simple_output": "Reason: FEE_DISSATISFACTION | Urgency: MEDIUM | Action: FEE_WAIVER_REVIEW | Why: Complaint evidence suggests this may be a fee dissatisfaction issue."
  }
}
```

### Abhiram Mann (`C17720`)

- OK: `True`
- Shape errors: `[]`
- Simple output: Reason: FINANCIAL_STRESS | Urgency: MEDIUM | Action: FINANCIAL_GUIDANCE | Why: Evidence suggests this because transaction_change_30d=-43.2 and balance_change_30d=-49.0 point to a financial issue. Financial Guidance fits because fees, charges or penalties levied wrongly (FEE_DISSATISFACTION) and complaint_text is null are absent.

Request:

```json
{
  "customer_id": "C17720",
  "customer_name": "Abhiram Mann",
  "prediction_date": "2026-04-01",
  "snapshot_date": "2026-04-01",
  "target_month": "2026-05-01",
  "profile": {
    "tenure_months": 156,
    "customer_segment": "pension",
    "income_regularity": "regular",
    "products_count": 1,
    "has_credit_card": 0,
    "has_loan": 0
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 14,
      "balance_change_30d": 10.0079,
      "transaction_change_30d": 15.7033,
      "card_spend_change_30d": -12.5881,
      "app_login_change_30d": 6.2308,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -3.343,
      "upi_share_of_spend": 0.6111,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 0,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 0.0,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-02-01",
      "days_since_last_transaction": 22,
      "balance_change_30d": -8.8916,
      "transaction_change_30d": -18.6635,
      "card_spend_change_30d": -23.3008,
      "app_login_change_30d": -13.2822,
      "salary_missing_days": 3.0,
      "external_transfer_change_30d": 8.1095,
      "upi_share_of_spend": 0.7688,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 0,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 3,
      "avg_resolution_time_hrs": 0.0,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-03-01",
      "days_since_last_transaction": 20,
      "balance_change_30d": -7.5255,
      "transaction_change_30d": -15.0636,
      "card_spend_change_30d": 15.1859,
      "app_login_change_30d": -3.0135,
      "salary_missing_days": 3.0,
      "external_transfer_change_30d": 29.4241,
      "upi_share_of_spend": 0.7902,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 0,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 0.0,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-04-01",
      "days_since_last_transaction": 23,
      "balance_change_30d": -49.0065,
      "transaction_change_30d": -43.1814,
      "card_spend_change_30d": -47.9353,
      "app_login_change_30d": -11.7074,
      "salary_missing_days": 3.0,
      "external_transfer_change_30d": 56.4448,
      "upi_share_of_spend": 0.8316,
      "fd_maturing_in_30d": 1,
      "products_dropped_90d": 0,
      "complaints_30d": 0,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 0.0,
      "emi_bounce_30d": 0
    }
  ],
  "customer": {
    "tenure_months": 156,
    "customer_segment": "pension",
    "income_regularity": "regular",
    "products_count": 1,
    "has_credit_card": 0,
    "has_loan": 0,
    "days_since_last_transaction": 23,
    "balance_change_30d": -49.0065,
    "transaction_change_30d": -43.1814,
    "card_spend_change_30d": -47.9353,
    "app_login_change_30d": -11.7074,
    "salary_missing_days": 3.0,
    "external_transfer_change_30d": 56.4448,
    "upi_share_of_spend": 0.8316,
    "fd_maturing_in_30d": 1,
    "products_dropped_90d": 0,
    "complaints_30d": 0,
    "unresolved_complaints": 0,
    "failed_transactions_30d": 1,
    "avg_resolution_time_hrs": 0.0,
    "emi_bounce_30d": 0
  },
  "extra_context": {
    "customer_profile": {
      "segment": "pension",
      "income_regularity": "regular",
      "tenure_months": 156,
      "age": 79,
      "customer_yearly_value": 14902.8682,
      "products_count": 1,
      "has_credit_card": 0,
      "has_loan": 0,
      "value_tier": "low"
    },
    "recent_complaint_text": null
  }
}
```

Response:

```json
{
  "meta": {
    "endpoint": "/predict/both",
    "served_at": "2026-08-31T01:42:25",
    "elapsed_ms": 13275.55,
    "timings_ms": {
      "model1": 97.67,
      "model2": 13177.67
    },
    "customer_id": "C17720",
    "customer_name": "Abhiram Mann",
    "snapshot_date": "2026-04-01"
  },
  "model1": {
    "churn_probability": 39.07,
    "raw_churn_probability": 92.47,
    "probability_mode": "sigmoid",
    "risk_score": 77.15,
    "churn_prediction": "Yes",
    "risk_level": "High",
    "top_risk_factors": [
      {
        "factor": "latest_days_since_last_transaction",
        "value": 23,
        "message": "Customer has gone longer without transacting.",
        "contribution": 0.5783494114875793
      },
      {
        "factor": "latest_transaction_change_30d",
        "value": -43.1814,
        "message": "Transaction activity has been falling across recent months.",
        "contribution": 0.44484201073646545
      },
      {
        "factor": "latest_vs_avg_upi_share_of_spend_available_history",
        "value": 0.081175,
        "message": "A larger share of spending is happening through UPI.",
        "contribution": 0.25843557715415955
      },
      {
        "factor": "latest_balance_change_30d",
        "value": -49.0065,
        "message": "Balance has been falling across recent months.",
        "contribution": 0.19936351478099823
      },
      {
        "factor": "latest_card_spend_change_30d",
        "value": -47.9353,
        "message": "Card spending has been falling across recent months.",
        "contribution": 0.18698640167713165
      }
    ]
  },
  "model2_input": {
    "customer_context": {
      "age": 79,
      "tenure_months": 156,
      "customer_segment": "pension",
      "income_regularity": "regular",
      "customer_yearly_value": 14902.8682,
      "products_count": 1,
      "has_credit_card": 0,
      "has_loan": 0
    },
    "behavior": {
      "days_since_last_transaction": 23,
      "balance_change_30d": -49.0065,
      "transaction_change_30d": -43.1814,
      "card_spend_change_30d": -47.9353,
      "app_login_change_30d": -11.7074,
      "salary_missing_days": 3,
      "external_transfer_change_30d": 56.4448,
      "upi_share_of_spend": 0.8316,
      "fd_maturing_in_30d": 1,
      "products_dropped_90d": 0,
      "emi_bounce_30d": 0
    },
    "service_evidence": {
      "complaints_30d": 0,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 0.0,
      "complaint_text": null
    },
    "model1": {
      "churn_probability": 0.3907,
      "churn_prediction": "Yes",
      "risk_level": "High",
      "top_risk_factors": [
        {
          "factor": "days_since_last_transaction",
          "value": 23
        },
        {
          "factor": "transaction_change_30d",
          "value": -43.1814
        },
        {
          "factor": "upi_share_of_spend",
          "value": 0.8316
        }
      ]
    },
    "eligible_actions": [
      "FINANCIAL_GUIDANCE",
      "SERVICE_RECOVERY",
      "PRODUCT_REVIEW",
      "RE_ENGAGEMENT",
      "MONITOR"
    ],
    "case_id": "C17720"
  },
  "model2": {
    "case_id": "C17720",
    "ok": true,
    "prediction": {
      "evidence": [
        "transaction_change_30d=-43.2",
        "app_login_change_30d=-11.7",
        "days_since_last_transaction=23",
        "emi_bounce_30d=0",
        "card_spend_change_30d=-48.0",
        "balance_change_30d=-49.0"
      ],
      "primary_reason": "FINANCIAL_STRESS",
      "reasoning_summary": "Evidence suggests this because transaction_change_30d=-43.2 and balance_change_30d=-49.0 point to a financial issue. Financial Guidance fits because fees, charges or penalties levied wrongly (FEE_DISSATISFACTION) and complaint_text is null are absent.",
      "recommended_action": "FINANCIAL_GUIDANCE",
      "secondary_reasons": [],
      "urgency": "MEDIUM"
    },
    "warnings": [
      "evidence: 'emi_bounce_30d=0' cites a zero/null value, which is not evidence; remove it",
      "urgency: model1.risk_level is High, so urgency must be HIGH, not MEDIUM"
    ],
    "raw_text": "{\"evidence\":[\"complaints_30d=0\",\"unresolved_complaints=0\",\"avg_resolution_time_hrs=0.0\"],\"primary_reason\":\"FINANCIAL_STRESS\",\"reasoning_summary\":\"Complaint and resolution signals suggest this may be a product-fit issue rather than a service friction.\",\"recommended_action\":\"FINANCIAL_GUIDANCE\",\"secondary_reasons\":[],\"urgency\":\"HIGH\"}",
    "error": null,
    "latency_s": 13.1776,
    "simple_output": "Reason: FINANCIAL_STRESS | Urgency: MEDIUM | Action: FINANCIAL_GUIDANCE | Why: Evidence suggests this because transaction_change_30d=-43.2 and balance_change_30d=-49.0 point to a financial issue. Financial Guidance fits because fees, charges or penalties levied wrongly (FEE_DISSATISFACTION) and complaint_text is null are absent."
  }
}
```

### Peter Sinha (`C18019`)

- OK: `True`
- Shape errors: `[]`
- Simple output: Reason: SERVICE_DISSATISFACTION | Urgency: MEDIUM | Action: COMPLAINT_ESCALATION | Why: Complaint escalation because complaints_30d=2 and unresolved_complaints=1 suggest SERVICE_DISSATISFACTION (service friction) without a stronger cause.

Request:

```json
{
  "customer_id": "C18019",
  "customer_name": "Peter Sinha",
  "prediction_date": "2026-06-01",
  "snapshot_date": "2026-06-01",
  "target_month": "2026-07-01",
  "profile": {
    "tenure_months": 102,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 4,
    "has_credit_card": 1,
    "has_loan": 1
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 10,
      "balance_change_30d": 16.8773,
      "transaction_change_30d": -9.5731,
      "card_spend_change_30d": -18.7358,
      "app_login_change_30d": 3.6951,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": 44.4758,
      "upi_share_of_spend": 0.6379,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 1,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 26.7013,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-02-01",
      "days_since_last_transaction": 5,
      "balance_change_30d": 10.0374,
      "transaction_change_30d": 9.5963,
      "card_spend_change_30d": 28.1236,
      "app_login_change_30d": 27.2244,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -7.4921,
      "upi_share_of_spend": 0.5644,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 0,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 0.0,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-03-01",
      "days_since_last_transaction": 10,
      "balance_change_30d": -3.7309,
      "transaction_change_30d": -14.169,
      "card_spend_change_30d": -11.0514,
      "app_login_change_30d": -6.7791,
      "salary_missing_days": 2.0,
      "external_transfer_change_30d": 20.5642,
      "upi_share_of_spend": 0.7018,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 1,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 20.8306,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-04-01",
      "days_since_last_transaction": 8,
      "balance_change_30d": -0.3249,
      "transaction_change_30d": 0.5337,
      "card_spend_change_30d": 26.5613,
      "app_login_change_30d": 25.0211,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -3.5931,
      "upi_share_of_spend": 0.5997,
      "fd_maturing_in_30d": 1,
      "products_dropped_90d": 0,
      "complaints_30d": 0,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 0.0,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-05-01",
      "days_since_last_transaction": 6,
      "balance_change_30d": -17.6413,
      "transaction_change_30d": 0.5667,
      "card_spend_change_30d": 2.4901,
      "app_login_change_30d": -2.9156,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -5.4993,
      "upi_share_of_spend": 0.7551,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 1,
      "failed_transactions_30d": 2,
      "avg_resolution_time_hrs": 46.1363,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-06-01",
      "days_since_last_transaction": 9,
      "balance_change_30d": -4.096,
      "transaction_change_30d": 0.9327,
      "card_spend_change_30d": -10.1968,
      "app_login_change_30d": 7.1978,
      "salary_missing_days": 1.0,
      "external_transfer_change_30d": 12.3643,
      "upi_share_of_spend": 0.6191,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 2,
      "unresolved_complaints": 1,
      "failed_transactions_30d": 2,
      "avg_resolution_time_hrs": 24.4545,
      "emi_bounce_30d": 0
    }
  ],
  "customer": {
    "tenure_months": 102,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 4,
    "has_credit_card": 1,
    "has_loan": 1,
    "days_since_last_transaction": 9,
    "balance_change_30d": -4.096,
    "transaction_change_30d": 0.9327,
    "card_spend_change_30d": -10.1968,
    "app_login_change_30d": 7.1978,
    "salary_missing_days": 1.0,
    "external_transfer_change_30d": 12.3643,
    "upi_share_of_spend": 0.6191,
    "fd_maturing_in_30d": 0,
    "products_dropped_90d": 0,
    "complaints_30d": 2,
    "unresolved_complaints": 1,
    "failed_transactions_30d": 2,
    "avg_resolution_time_hrs": 24.4545,
    "emi_bounce_30d": 0
  },
  "extra_context": {
    "customer_profile": {
      "segment": "salary",
      "income_regularity": "regular",
      "tenure_months": 102,
      "age": 36,
      "customer_yearly_value": 27600.0788,
      "products_count": 4,
      "has_credit_card": 1,
      "has_loan": 1,
      "value_tier": "low"
    },
    "recent_complaint_text": "Please confirm status of my ATM dispute raised on 18th last month."
  }
}
```

Response:

```json
{
  "meta": {
    "endpoint": "/predict/both",
    "served_at": "2026-08-31T01:42:29",
    "elapsed_ms": 3884.25,
    "timings_ms": {
      "model1": 79.0,
      "model2": 3805.1
    },
    "customer_id": "C18019",
    "customer_name": "Peter Sinha",
    "snapshot_date": "2026-06-01"
  },
  "model1": {
    "churn_probability": 4.24,
    "raw_churn_probability": 35.09,
    "probability_mode": "sigmoid",
    "risk_score": 12.73,
    "churn_prediction": "No",
    "risk_level": "Low",
    "top_risk_factors": [
      {
        "factor": "sum_fd_maturing_in_30d_3m",
        "value": 1.0,
        "message": "Customer has a fixed deposit maturing soon.",
        "contribution": 0.12024595588445663
      },
      {
        "factor": "max_avg_resolution_time_hrs_3m",
        "value": 46.1363,
        "message": "Recent complaints took longer to resolve.",
        "contribution": 0.06042410060763359
      },
      {
        "factor": "sum_unresolved_complaints_6m",
        "value": 3.0,
        "message": "Customer has recent complaint activity.",
        "contribution": 0.03718646243214607
      },
      {
        "factor": "balance_change_30d_trend_6m",
        "value": -5.271331428571427,
        "message": "Balance has been falling across recent months.",
        "contribution": 0.034917205572128296
      },
      {
        "factor": "latest_upi_share_of_spend",
        "value": 0.6191,
        "message": "A larger share of spending is happening through UPI.",
        "contribution": 0.024536794051527977
      }
    ]
  },
  "model2_input": {
    "customer_context": {
      "age": 36,
      "tenure_months": 102,
      "customer_segment": "salary",
      "income_regularity": "regular",
      "customer_yearly_value": 27600.0788,
      "products_count": 4,
      "has_credit_card": 1,
      "has_loan": 1
    },
    "behavior": {
      "days_since_last_transaction": 9,
      "balance_change_30d": -4.096,
      "transaction_change_30d": 0.9327,
      "card_spend_change_30d": -10.1968,
      "app_login_change_30d": 7.1978,
      "salary_missing_days": 1,
      "external_transfer_change_30d": 12.3643,
      "upi_share_of_spend": 0.6191,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "emi_bounce_30d": 0
    },
    "service_evidence": {
      "complaints_30d": 2,
      "unresolved_complaints": 1,
      "failed_transactions_30d": 2,
      "avg_resolution_time_hrs": 24.4545,
      "complaint_text": "Please confirm status of my ATM dispute raised on 18th last month."
    },
    "model1": {
      "churn_probability": 0.0424,
      "churn_prediction": "No",
      "risk_level": "Low",
      "top_risk_factors": [
        {
          "factor": "fd_maturing_in_30d",
          "value": 0
        },
        {
          "factor": "unresolved_complaints",
          "value": 1
        },
        {
          "factor": "balance_change_30d",
          "value": -4.096
        }
      ]
    },
    "eligible_actions": [
      "COMPLAINT_ESCALATION",
      "CARD_REVIEW",
      "FINANCIAL_GUIDANCE",
      "SERVICE_RECOVERY",
      "MONITOR"
    ],
    "case_id": "C18019"
  },
  "model2": {
    "case_id": "C18019",
    "ok": true,
    "prediction": {
      "evidence": [
        "complaints_30d=2",
        "unresolved_complaints=1",
        "avg_resolution_time_hrs=24.5"
      ],
      "primary_reason": "SERVICE_DISSATISFACTION",
      "reasoning_summary": "Complaint escalation because complaints_30d=2 and unresolved_complaints=1 suggest SERVICE_DISSATISFACTION (service friction) without a stronger cause.",
      "recommended_action": "COMPLAINT_ESCALATION",
      "secondary_reasons": [],
      "urgency": "MEDIUM"
    },
    "warnings": [],
    "raw_text": "{\n    \"evidence\": [\n        \"complaints_30d=2\",\n        \"unresolved_complaints=1\",\n        \"avg_resolution_time_hrs=24.5\"\n    ],\n    \"primary_reason\": \"SERVICE_DISSATISFACTION\",\n    \"reasoning_summary\": \"Complaint escalation because complaints_30d=2 and unresolved_complaints=1 suggest SERVICE_DISSATISFACTION (service friction) without a stronger cause.\",\n    \"recommended_action\": \"COMPLAINT_ESCALATION\",\n    \"secondary_reasons\": [],\n    \"urgency\": \"MEDIUM\"\n}",
    "error": null,
    "latency_s": 3.805,
    "simple_output": "Reason: SERVICE_DISSATISFACTION | Urgency: MEDIUM | Action: COMPLAINT_ESCALATION | Why: Complaint escalation because complaints_30d=2 and unresolved_complaints=1 suggest SERVICE_DISSATISFACTION (service friction) without a stronger cause."
  }
}
```

### Dakshesh Hora (`C18217`)

- OK: `True`
- Shape errors: `[]`
- Simple output: Reason: UNKNOWN | Urgency: LOW | Action: MONITOR | Why: Complaint and service friction signals are mixed or weak; the cause remains uncertain.

Request:

```json
{
  "customer_id": "C18217",
  "customer_name": "Dakshesh Hora",
  "prediction_date": "2026-06-01",
  "snapshot_date": "2026-06-01",
  "target_month": "2026-07-01",
  "profile": {
    "tenure_months": 133,
    "customer_segment": "pension",
    "income_regularity": "regular",
    "products_count": 1,
    "has_credit_card": 0,
    "has_loan": 0
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 6,
      "balance_change_30d": 7.5218,
      "transaction_change_30d": 2.1613,
      "card_spend_change_30d": -1.0434,
      "app_login_change_30d": 0.1094,
      "salary_missing_days": 1.0,
      "external_transfer_change_30d": 25.1128,
      "upi_share_of_spend": 0.2216,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 0,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 0.0,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-02-01",
      "days_since_last_transaction": 1,
      "balance_change_30d": 14.1813,
      "transaction_change_30d": 4.8768,
      "card_spend_change_30d": 52.4872,
      "app_login_change_30d": 22.6154,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -27.6007,
      "upi_share_of_spend": 0.2374,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 0,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 0.0,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-03-01",
      "days_since_last_transaction": 2,
      "balance_change_30d": 0.0831,
      "transaction_change_30d": 41.8483,
      "card_spend_change_30d": 24.3278,
      "app_login_change_30d": 37.4364,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -40.4107,
      "upi_share_of_spend": 0.2563,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 3,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 28.9454,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-04-01",
      "days_since_last_transaction": 8,
      "balance_change_30d": 17.3055,
      "transaction_change_30d": 12.2578,
      "card_spend_change_30d": 43.1331,
      "app_login_change_30d": 26.1515,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": 2.0445,
      "upi_share_of_spend": 0.2665,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 0,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 0.0,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-05-01",
      "days_since_last_transaction": 6,
      "balance_change_30d": 27.4192,
      "transaction_change_30d": 16.0226,
      "card_spend_change_30d": 2.2724,
      "app_login_change_30d": 30.6712,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -43.4736,
      "upi_share_of_spend": 0.1951,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 0,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 0.0,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-06-01",
      "days_since_last_transaction": 0,
      "balance_change_30d": 8.1783,
      "transaction_change_30d": 6.9647,
      "card_spend_change_30d": 24.647,
      "app_login_change_30d": 24.0246,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -3.8029,
      "upi_share_of_spend": 0.1986,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 0,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 0.0,
      "emi_bounce_30d": 0
    }
  ],
  "customer": {
    "tenure_months": 133,
    "customer_segment": "pension",
    "income_regularity": "regular",
    "products_count": 1,
    "has_credit_card": 0,
    "has_loan": 0,
    "days_since_last_transaction": 0,
    "balance_change_30d": 8.1783,
    "transaction_change_30d": 6.9647,
    "card_spend_change_30d": 24.647,
    "app_login_change_30d": 24.0246,
    "salary_missing_days": 0.0,
    "external_transfer_change_30d": -3.8029,
    "upi_share_of_spend": 0.1986,
    "fd_maturing_in_30d": 0,
    "products_dropped_90d": 0,
    "complaints_30d": 0,
    "unresolved_complaints": 0,
    "failed_transactions_30d": 0,
    "avg_resolution_time_hrs": 0.0,
    "emi_bounce_30d": 0
  },
  "extra_context": {
    "customer_profile": {
      "segment": "pension",
      "income_regularity": "regular",
      "tenure_months": 133,
      "age": 77,
      "customer_yearly_value": 6729.9333,
      "products_count": 1,
      "has_credit_card": 0,
      "has_loan": 0,
      "value_tier": "low"
    },
    "recent_complaint_text": null
  }
}
```

Response:

```json
{
  "meta": {
    "endpoint": "/predict/both",
    "served_at": "2026-08-31T01:42:40",
    "elapsed_ms": 10544.19,
    "timings_ms": {
      "model1": 71.39,
      "model2": 10472.63
    },
    "customer_id": "C18217",
    "customer_name": "Dakshesh Hora",
    "snapshot_date": "2026-06-01"
  },
  "model1": {
    "churn_probability": 2.0,
    "raw_churn_probability": 18.43,
    "probability_mode": "sigmoid",
    "risk_score": 6.0,
    "churn_prediction": "No",
    "risk_level": "Low",
    "top_risk_factors": [
      {
        "factor": "avg_upi_share_of_spend_6m",
        "value": 0.22925000000000004,
        "message": "A larger share of spending is happening through UPI.",
        "contribution": 0.02293499745428562
      },
      {
        "factor": "avg_transaction_change_30d_6m",
        "value": 14.021916666666664,
        "message": "This signal increased churn risk.",
        "contribution": 0.019847076386213303
      },
      {
        "factor": "latest_vs_avg_card_spend_change_30d_available_history",
        "value": 0.3429833333333292,
        "message": "This signal increased churn risk.",
        "contribution": 0.015545654110610485
      },
      {
        "factor": "max_days_since_last_transaction_3m",
        "value": 8.0,
        "message": "Customer has gone longer without transacting.",
        "contribution": 0.013036725111305714
      },
      {
        "factor": "max_salary_missing_days_6m",
        "value": 1.0,
        "message": "Salary or pension was delayed recently.",
        "contribution": 0.007885432802140713
      }
    ]
  },
  "model2_input": {
    "customer_context": {
      "age": 77,
      "tenure_months": 133,
      "customer_segment": "pension",
      "income_regularity": "regular",
      "customer_yearly_value": 6729.9333,
      "products_count": 1,
      "has_credit_card": 0,
      "has_loan": 0
    },
    "behavior": {
      "days_since_last_transaction": 0,
      "balance_change_30d": 8.1783,
      "transaction_change_30d": 6.9647,
      "card_spend_change_30d": 24.647,
      "app_login_change_30d": 24.0246,
      "salary_missing_days": 0,
      "external_transfer_change_30d": -3.8029,
      "upi_share_of_spend": 0.1986,
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
      "churn_probability": 0.02,
      "churn_prediction": "No",
      "risk_level": "Low",
      "top_risk_factors": [
        {
          "factor": "upi_share_of_spend",
          "value": 0.1986
        },
        {
          "factor": "transaction_change_30d",
          "value": 6.9647
        },
        {
          "factor": "card_spend_change_30d",
          "value": 24.647
        }
      ]
    },
    "eligible_actions": [
      "RE_ENGAGEMENT",
      "PRODUCT_REVIEW",
      "MONITOR"
    ],
    "case_id": "C18217"
  },
  "model2": {
    "case_id": "C18217",
    "ok": true,
    "prediction": {
      "evidence": [
        "complaints_30d=0",
        "unresolved_complaints=0",
        "avg_resolution_time_hrs=0.0"
      ],
      "primary_reason": "UNKNOWN",
      "reasoning_summary": "Complaint and service friction signals are mixed or weak; the cause remains uncertain.",
      "recommended_action": "MONITOR",
      "secondary_reasons": [],
      "urgency": "LOW"
    },
    "warnings": [
      "evidence: 'complaints_30d=0' cites a zero/null value, which is not evidence; remove it",
      "evidence: 'unresolved_complaints=0' cites a zero/null value, which is not evidence; remove it",
      "evidence: 'avg_resolution_time_hrs=0.0' cites a zero/null value, which is not evidence; remove it"
    ],
    "raw_text": "{\"evidence\":[\"complaints_30d=0\",\"unresolved_complaints=0\",\"avg_resolution_time_hrs=0.0\"],\"primary_reason\":\"UNKNOWN\",\"reasoning_summary\":\"Complaint and service friction signals are mixed or weak; the cause remains uncertain.\",\"recommended_action\":\"MONITOR\",\"secondary_reasons\":[],\"urgency\":\"LOW\"}",
    "error": null,
    "latency_s": 10.4725,
    "simple_output": "Reason: UNKNOWN | Urgency: LOW | Action: MONITOR | Why: Complaint and service friction signals are mixed or weak; the cause remains uncertain."
  }
}
```

### Advika Gera (`C18290`)

- OK: `True`
- Shape errors: `[]`
- Simple output: Reason: SERVICE_DISSATISFACTION | Urgency: HIGH | Action: COMPLAINT_ESCALATION | Why: Complaint escalation because complaints_30d=1 and unresolved_complaints=1 indicate the issue is unresolved or operationally serious.

Request:

```json
{
  "customer_id": "C18290",
  "customer_name": "Advika Gera",
  "prediction_date": "2026-06-01",
  "snapshot_date": "2026-06-01",
  "target_month": "2026-07-01",
  "profile": {
    "tenure_months": 70,
    "customer_segment": "business",
    "income_regularity": "irregular",
    "products_count": 4,
    "has_credit_card": 1,
    "has_loan": 1
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 3,
      "balance_change_30d": 6.9622,
      "transaction_change_30d": 0.5754,
      "card_spend_change_30d": -4.3685,
      "app_login_change_30d": 9.5089,
      "salary_missing_days": null,
      "external_transfer_change_30d": -24.5373,
      "upi_share_of_spend": 0.3144,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 0,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 0.0,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-02-01",
      "days_since_last_transaction": 9,
      "balance_change_30d": -24.5413,
      "transaction_change_30d": 33.5757,
      "card_spend_change_30d": -16.2991,
      "app_login_change_30d": -26.0229,
      "salary_missing_days": null,
      "external_transfer_change_30d": -0.0349,
      "upi_share_of_spend": 0.4644,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 3,
      "unresolved_complaints": 2,
      "failed_transactions_30d": 4,
      "avg_resolution_time_hrs": 59.3011,
      "emi_bounce_30d": 1
    },
    {
      "snapshot_date": "2026-03-01",
      "days_since_last_transaction": 9,
      "balance_change_30d": 18.7084,
      "transaction_change_30d": 1.1208,
      "card_spend_change_30d": -2.1819,
      "app_login_change_30d": 21.6702,
      "salary_missing_days": null,
      "external_transfer_change_30d": 6.4447,
      "upi_share_of_spend": 0.3915,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 2,
      "complaints_30d": 0,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 0.0,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-04-01",
      "days_since_last_transaction": 11,
      "balance_change_30d": -3.8655,
      "transaction_change_30d": -24.519,
      "card_spend_change_30d": 9.8611,
      "app_login_change_30d": 20.7937,
      "salary_missing_days": null,
      "external_transfer_change_30d": 4.179,
      "upi_share_of_spend": 0.4053,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 0,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 2,
      "avg_resolution_time_hrs": 0.0,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-05-01",
      "days_since_last_transaction": 6,
      "balance_change_30d": 3.8944,
      "transaction_change_30d": -7.8998,
      "card_spend_change_30d": -4.9265,
      "app_login_change_30d": -8.9541,
      "salary_missing_days": null,
      "external_transfer_change_30d": 31.0296,
      "upi_share_of_spend": 0.3574,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 0,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 0.0,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-06-01",
      "days_since_last_transaction": 9,
      "balance_change_30d": 14.2274,
      "transaction_change_30d": -4.3285,
      "card_spend_change_30d": -9.3543,
      "app_login_change_30d": 7.2862,
      "salary_missing_days": null,
      "external_transfer_change_30d": -2.3356,
      "upi_share_of_spend": 0.4015,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 1,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 41.327,
      "emi_bounce_30d": 0
    }
  ],
  "customer": {
    "tenure_months": 70,
    "customer_segment": "business",
    "income_regularity": "irregular",
    "products_count": 4,
    "has_credit_card": 1,
    "has_loan": 1,
    "days_since_last_transaction": 9,
    "balance_change_30d": 14.2274,
    "transaction_change_30d": -4.3285,
    "card_spend_change_30d": -9.3543,
    "app_login_change_30d": 7.2862,
    "salary_missing_days": null,
    "external_transfer_change_30d": -2.3356,
    "upi_share_of_spend": 0.4015,
    "fd_maturing_in_30d": 0,
    "products_dropped_90d": 0,
    "complaints_30d": 1,
    "unresolved_complaints": 1,
    "failed_transactions_30d": 1,
    "avg_resolution_time_hrs": 41.327,
    "emi_bounce_30d": 0
  },
  "extra_context": {
    "customer_profile": {
      "segment": "business",
      "income_regularity": "irregular",
      "tenure_months": 70,
      "age": 31,
      "customer_yearly_value": 15639.1022,
      "products_count": 4,
      "has_credit_card": 1,
      "has_loan": 1,
      "value_tier": "low"
    },
    "recent_complaint_text": "Please confirm whether Saturday banking is available at this branch."
  }
}
```

Response:

```json
{
  "meta": {
    "endpoint": "/predict/both",
    "served_at": "2026-08-31T01:42:44",
    "elapsed_ms": 4163.35,
    "timings_ms": {
      "model1": 166.06,
      "model2": 3997.07
    },
    "customer_id": "C18290",
    "customer_name": "Advika Gera",
    "snapshot_date": "2026-06-01"
  },
  "model1": {
    "churn_probability": 6.28,
    "raw_churn_probability": 43.95,
    "probability_mode": "sigmoid",
    "risk_score": 18.83,
    "churn_prediction": "No",
    "risk_level": "Low",
    "top_risk_factors": [
      {
        "factor": "latest_avg_resolution_time_hrs",
        "value": 41.327,
        "message": "Recent complaints took longer to resolve.",
        "contribution": 0.4231213629245758
      },
      {
        "factor": "sum_failed_transactions_30d_6m",
        "value": 8.0,
        "message": "Customer has recent failed transactions.",
        "contribution": 0.14307960867881775
      },
      {
        "factor": "external_transfer_change_30d_trend_6m",
        "value": 5.769608571428571,
        "message": "External transfers have increased.",
        "contribution": 0.030088385567069054
      },
      {
        "factor": "sum_unresolved_complaints_6m",
        "value": 3.0,
        "message": "Customer has recent complaint activity.",
        "contribution": 0.02321949601173401
      },
      {
        "factor": "max_avg_resolution_time_hrs_6m",
        "value": 59.3011,
        "message": "Recent complaints took longer to resolve.",
        "contribution": 0.022067828103899956
      }
    ]
  },
  "model2_input": {
    "customer_context": {
      "age": 31,
      "tenure_months": 70,
      "customer_segment": "business",
      "income_regularity": "irregular",
      "customer_yearly_value": 15639.1022,
      "products_count": 4,
      "has_credit_card": 1,
      "has_loan": 1
    },
    "behavior": {
      "days_since_last_transaction": 9,
      "balance_change_30d": 14.2274,
      "transaction_change_30d": -4.3285,
      "card_spend_change_30d": -9.3543,
      "app_login_change_30d": 7.2862,
      "salary_missing_days": null,
      "external_transfer_change_30d": -2.3356,
      "upi_share_of_spend": 0.4015,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "emi_bounce_30d": 0
    },
    "service_evidence": {
      "complaints_30d": 1,
      "unresolved_complaints": 1,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 41.327,
      "complaint_text": "Please confirm whether Saturday banking is available at this branch."
    },
    "model1": {
      "churn_probability": 0.0628,
      "churn_prediction": "No",
      "risk_level": "Low",
      "top_risk_factors": [
        {
          "factor": "failed_transactions_30d",
          "value": 1
        },
        {
          "factor": "external_transfer_change_30d",
          "value": -2.3356
        },
        {
          "factor": "unresolved_complaints",
          "value": 1
        }
      ]
    },
    "eligible_actions": [
      "COMPLAINT_ESCALATION",
      "SERVICE_RECOVERY",
      "MONITOR"
    ],
    "case_id": "C18290"
  },
  "model2": {
    "case_id": "C18290",
    "ok": true,
    "prediction": {
      "evidence": [
        "complaints_30d=1",
        "unresolved_complaints=1",
        "failed_transactions_30d=1",
        "avg_resolution_time_hrs=41.3",
        "complaint_text describes a recent service issue"
      ],
      "primary_reason": "SERVICE_DISSATISFACTION",
      "reasoning_summary": "Complaint escalation because complaints_30d=1 and unresolved_complaints=1 indicate the issue is unresolved or operationally serious.",
      "recommended_action": "COMPLAINT_ESCALATION",
      "secondary_reasons": [],
      "urgency": "HIGH"
    },
    "warnings": [],
    "raw_text": "{\"evidence\":[\"complaints_30d=1\",\"unresolved_complaints=1\",\"failed_transactions_30d=1\",\"avg_resolution_time_hrs=41.3\",\"complaint_text describes a recent service issue\"],\"primary_reason\":\"SERVICE_DISSATISFACTION\",\"reasoning_summary\":\"Complaint escalation because complaints_30d=1 and unresolved_complaints=1 indicate the issue is unresolved or operationally serious.\",\"recommended_action\":\"COMPLAINT_ESCALATION\",\"secondary_reasons\":[],\"urgency\":\"HIGH\"}",
    "error": null,
    "latency_s": 3.997,
    "simple_output": "Reason: SERVICE_DISSATISFACTION | Urgency: HIGH | Action: COMPLAINT_ESCALATION | Why: Complaint escalation because complaints_30d=1 and unresolved_complaints=1 indicate the issue is unresolved or operationally serious."
  }
}
```

### Yachana Rastogi (`C18690`)

- OK: `True`
- Shape errors: `[]`
- Simple output: Reason: UNKNOWN | Urgency: LOW | Action: MONITOR | Why: Complaint and resolution signals are mixed or weak; evidence is genuinely unclear.

Request:

```json
{
  "customer_id": "C18690",
  "customer_name": "Yachana Rastogi",
  "prediction_date": "2026-06-01",
  "snapshot_date": "2026-06-01",
  "target_month": "2026-07-01",
  "profile": {
    "tenure_months": 160,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 2,
    "has_credit_card": 1,
    "has_loan": 0
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 10,
      "balance_change_30d": 7.8797,
      "transaction_change_30d": -1.023,
      "card_spend_change_30d": 8.3204,
      "app_login_change_30d": 18.5217,
      "salary_missing_days": 3.0,
      "external_transfer_change_30d": 78.305,
      "upi_share_of_spend": 0.51,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 2,
      "unresolved_complaints": 1,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 19.2834,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-02-01",
      "days_since_last_transaction": 13,
      "balance_change_30d": 9.7634,
      "transaction_change_30d": 2.9084,
      "card_spend_change_30d": -5.045,
      "app_login_change_30d": -23.9356,
      "salary_missing_days": 2.0,
      "external_transfer_change_30d": -23.6894,
      "upi_share_of_spend": 0.4885,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 0,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 0.0,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-03-01",
      "days_since_last_transaction": 6,
      "balance_change_30d": -1.1428,
      "transaction_change_30d": -2.9345,
      "card_spend_change_30d": 15.9918,
      "app_login_change_30d": 24.5508,
      "salary_missing_days": 1.0,
      "external_transfer_change_30d": -2.5341,
      "upi_share_of_spend": 0.3506,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 0,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 0.0,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-04-01",
      "days_since_last_transaction": 3,
      "balance_change_30d": 51.597,
      "transaction_change_30d": 7.7671,
      "card_spend_change_30d": 9.9575,
      "app_login_change_30d": 20.9012,
      "salary_missing_days": 1.0,
      "external_transfer_change_30d": -60.7566,
      "upi_share_of_spend": 0.4268,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 36.9983,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-05-01",
      "days_since_last_transaction": 1,
      "balance_change_30d": 14.1501,
      "transaction_change_30d": 21.9792,
      "card_spend_change_30d": 26.7744,
      "app_login_change_30d": 8.2682,
      "salary_missing_days": 2.0,
      "external_transfer_change_30d": -55.3492,
      "upi_share_of_spend": 0.2643,
      "fd_maturing_in_30d": 1,
      "products_dropped_90d": 0,
      "complaints_30d": 0,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 0.0,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-06-01",
      "days_since_last_transaction": 2,
      "balance_change_30d": 29.0024,
      "transaction_change_30d": 6.7684,
      "card_spend_change_30d": 12.3731,
      "app_login_change_30d": 0.8358,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -3.3845,
      "upi_share_of_spend": 0.2612,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 0,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 0.0,
      "emi_bounce_30d": 0
    }
  ],
  "customer": {
    "tenure_months": 160,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 2,
    "has_credit_card": 1,
    "has_loan": 0,
    "days_since_last_transaction": 2,
    "balance_change_30d": 29.0024,
    "transaction_change_30d": 6.7684,
    "card_spend_change_30d": 12.3731,
    "app_login_change_30d": 0.8358,
    "salary_missing_days": 0.0,
    "external_transfer_change_30d": -3.3845,
    "upi_share_of_spend": 0.2612,
    "fd_maturing_in_30d": 0,
    "products_dropped_90d": 0,
    "complaints_30d": 0,
    "unresolved_complaints": 0,
    "failed_transactions_30d": 0,
    "avg_resolution_time_hrs": 0.0,
    "emi_bounce_30d": 0
  },
  "extra_context": {
    "customer_profile": {
      "segment": "salary",
      "income_regularity": "regular",
      "tenure_months": 160,
      "age": 50,
      "customer_yearly_value": 38161.4195,
      "products_count": 2,
      "has_credit_card": 1,
      "has_loan": 0,
      "value_tier": "medium"
    },
    "recent_complaint_text": null
  }
}
```

Response:

```json
{
  "meta": {
    "endpoint": "/predict/both",
    "served_at": "2026-08-31T01:42:56",
    "elapsed_ms": 11791.16,
    "timings_ms": {
      "model1": 151.17,
      "model2": 11639.8
    },
    "customer_id": "C18690",
    "customer_name": "Yachana Rastogi",
    "snapshot_date": "2026-06-01"
  },
  "model1": {
    "churn_probability": 1.72,
    "raw_churn_probability": 15.13,
    "probability_mode": "sigmoid",
    "risk_score": 5.16,
    "churn_prediction": "No",
    "risk_level": "Low",
    "top_risk_factors": [
      {
        "factor": "sum_fd_maturing_in_30d_3m",
        "value": 1.0,
        "message": "Customer has a fixed deposit maturing soon.",
        "contribution": 0.0946701243519783
      },
      {
        "factor": "latest_vs_avg_card_spend_change_30d_available_history",
        "value": 0.9777333333333349,
        "message": "This signal increased churn risk.",
        "contribution": 0.01819510944187641
      },
      {
        "factor": "sum_failed_transactions_30d_6m",
        "value": 5.0,
        "message": "Customer has recent failed transactions.",
        "contribution": 0.00979698821902275
      },
      {
        "factor": "max_salary_missing_days_3m",
        "value": 2.0,
        "message": "Salary or pension was delayed recently.",
        "contribution": 0.009700494818389416
      },
      {
        "factor": "app_login_change_30d_trend_6m",
        "value": 0.1294942857142856,
        "message": "This signal increased churn risk.",
        "contribution": 0.0067772469483315945
      }
    ]
  },
  "model2_input": {
    "customer_context": {
      "age": 50,
      "tenure_months": 160,
      "customer_segment": "salary",
      "income_regularity": "regular",
      "customer_yearly_value": 38161.4195,
      "products_count": 2,
      "has_credit_card": 1,
      "has_loan": 0
    },
    "behavior": {
      "days_since_last_transaction": 2,
      "balance_change_30d": 29.0024,
      "transaction_change_30d": 6.7684,
      "card_spend_change_30d": 12.3731,
      "app_login_change_30d": 0.8358,
      "salary_missing_days": 0,
      "external_transfer_change_30d": -3.3845,
      "upi_share_of_spend": 0.2612,
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
      "churn_probability": 0.0172,
      "churn_prediction": "No",
      "risk_level": "Low",
      "top_risk_factors": [
        {
          "factor": "fd_maturing_in_30d",
          "value": 0
        },
        {
          "factor": "card_spend_change_30d",
          "value": 12.3731
        },
        {
          "factor": "failed_transactions_30d",
          "value": 0
        }
      ]
    },
    "eligible_actions": [
      "RE_ENGAGEMENT",
      "PRODUCT_REVIEW",
      "MONITOR"
    ],
    "case_id": "C18690"
  },
  "model2": {
    "case_id": "C18690",
    "ok": true,
    "prediction": {
      "evidence": [
        "complaints_30d=0",
        "unresolved_complaints=0",
        "avg_resolution_time_hrs=0.0"
      ],
      "primary_reason": "UNKNOWN",
      "reasoning_summary": "Complaint and resolution signals are mixed or weak; evidence is genuinely unclear.",
      "recommended_action": "MONITOR",
      "secondary_reasons": [],
      "urgency": "LOW"
    },
    "warnings": [
      "evidence: 'complaints_30d=0' cites a zero/null value, which is not evidence; remove it",
      "evidence: 'unresolved_complaints=0' cites a zero/null value, which is not evidence; remove it",
      "evidence: 'avg_resolution_time_hrs=0.0' cites a zero/null value, which is not evidence; remove it"
    ],
    "raw_text": "{\"evidence\":[\"complaints_30d=0\",\"unresolved_complaints=0\",\"avg_resolution_time_hrs=0.0\"],\"primary_reason\":\"UNKNOWN\",\"reasoning_summary\":\"Complaint and resolution signals are mixed or weak; relationship-strengthening action is supported by evidence.\",\"recommended_action\":\"RE_ENGAGEMENT\",\"secondary_reasons\":[],\"urgency\":\"MEDIUM\"}",
    "error": null,
    "latency_s": 11.6398,
    "simple_output": "Reason: UNKNOWN | Urgency: LOW | Action: MONITOR | Why: Complaint and resolution signals are mixed or weak; evidence is genuinely unclear."
  }
}
```

### Rachita Nanda (`C19885`)

- OK: `True`
- Shape errors: `[]`
- Simple output: Reason: FINANCIAL_STRESS | Urgency: HIGH | Action: FINANCIAL_GUIDANCE | Why: The relationship looks stuck in a financial rut. Digital friction fits because app_login_change_30d=-8.6 and external_transfer_change_30d=47.7 suggest the current setup is creating friction.

Request:

```json
{
  "customer_id": "C19885",
  "customer_name": "Rachita Nanda",
  "prediction_date": "2026-06-01",
  "snapshot_date": "2026-06-01",
  "target_month": "2026-07-01",
  "profile": {
    "tenure_months": 287,
    "customer_segment": "pension",
    "income_regularity": "regular",
    "products_count": 3,
    "has_credit_card": 1,
    "has_loan": 0
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 6,
      "balance_change_30d": 17.2725,
      "transaction_change_30d": -4.3031,
      "card_spend_change_30d": 8.4554,
      "app_login_change_30d": -11.353,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -0.7283,
      "upi_share_of_spend": 0.0812,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 0,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 0.0,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-02-01",
      "days_since_last_transaction": 0,
      "balance_change_30d": 7.5432,
      "transaction_change_30d": 5.818,
      "card_spend_change_30d": 26.7931,
      "app_login_change_30d": 28.4341,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": 10.2437,
      "upi_share_of_spend": 0.1079,
      "fd_maturing_in_30d": 1,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 24.7313,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-03-01",
      "days_since_last_transaction": 3,
      "balance_change_30d": -9.2294,
      "transaction_change_30d": -4.3879,
      "card_spend_change_30d": 14.6719,
      "app_login_change_30d": -2.3876,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": 4.3487,
      "upi_share_of_spend": 0.0605,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 13.046,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-04-01",
      "days_since_last_transaction": 11,
      "balance_change_30d": -17.8762,
      "transaction_change_30d": -20.2833,
      "card_spend_change_30d": -22.6167,
      "app_login_change_30d": -28.0067,
      "salary_missing_days": 3.0,
      "external_transfer_change_30d": 31.2827,
      "upi_share_of_spend": 0.1889,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 0,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 0.0,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-05-01",
      "days_since_last_transaction": 10,
      "balance_change_30d": -7.5096,
      "transaction_change_30d": -3.5154,
      "card_spend_change_30d": -6.5334,
      "app_login_change_30d": -22.9502,
      "salary_missing_days": 2.0,
      "external_transfer_change_30d": 13.9925,
      "upi_share_of_spend": 0.1645,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 1,
      "complaints_30d": 0,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 0.0,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-06-01",
      "days_since_last_transaction": 17,
      "balance_change_30d": -48.0782,
      "transaction_change_30d": -27.5313,
      "card_spend_change_30d": -28.375,
      "app_login_change_30d": -8.5088,
      "salary_missing_days": 3.0,
      "external_transfer_change_30d": 47.7371,
      "upi_share_of_spend": 0.2497,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 0,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 0.0,
      "emi_bounce_30d": 0
    }
  ],
  "customer": {
    "tenure_months": 287,
    "customer_segment": "pension",
    "income_regularity": "regular",
    "products_count": 3,
    "has_credit_card": 1,
    "has_loan": 0,
    "days_since_last_transaction": 17,
    "balance_change_30d": -48.0782,
    "transaction_change_30d": -27.5313,
    "card_spend_change_30d": -28.375,
    "app_login_change_30d": -8.5088,
    "salary_missing_days": 3.0,
    "external_transfer_change_30d": 47.7371,
    "upi_share_of_spend": 0.2497,
    "fd_maturing_in_30d": 0,
    "products_dropped_90d": 0,
    "complaints_30d": 0,
    "unresolved_complaints": 0,
    "failed_transactions_30d": 1,
    "avg_resolution_time_hrs": 0.0,
    "emi_bounce_30d": 0
  },
  "extra_context": {
    "customer_profile": {
      "segment": "pension",
      "income_regularity": "regular",
      "tenure_months": 287,
      "age": 63,
      "customer_yearly_value": 27052.2193,
      "products_count": 3,
      "has_credit_card": 1,
      "has_loan": 0,
      "value_tier": "low"
    },
    "recent_complaint_text": null
  }
}
```

Response:

```json
{
  "meta": {
    "endpoint": "/predict/both",
    "served_at": "2026-08-31T01:43:08",
    "elapsed_ms": 12053.59,
    "timings_ms": {
      "model1": 185.9,
      "model2": 11867.47
    },
    "customer_id": "C19885",
    "customer_name": "Rachita Nanda",
    "snapshot_date": "2026-06-01"
  },
  "model1": {
    "churn_probability": 30.48,
    "raw_churn_probability": 84.3,
    "probability_mode": "sigmoid",
    "risk_score": 73.93,
    "churn_prediction": "Yes",
    "risk_level": "High",
    "top_risk_factors": [
      {
        "factor": "latest_days_since_last_transaction",
        "value": 17,
        "message": "Customer has gone longer without transacting.",
        "contribution": 0.6340673565864563
      },
      {
        "factor": "latest_transaction_change_30d",
        "value": -27.5313,
        "message": "Transaction activity has been falling across recent months.",
        "contribution": 0.25470831990242004
      },
      {
        "factor": "latest_balance_change_30d",
        "value": -48.0782,
        "message": "Balance has been falling across recent months.",
        "contribution": 0.2190340757369995
      },
      {
        "factor": "latest_vs_avg_upi_share_of_spend_available_history",
        "value": 0.10758333333333334,
        "message": "A larger share of spending is happening through UPI.",
        "contribution": 0.2138000726699829
      },
      {
        "factor": "days_since_last_transaction_trend_6m",
        "value": 2.6571428571428566,
        "message": "Customer has gone longer without transacting.",
        "contribution": 0.19309569895267487
      }
    ]
  },
  "model2_input": {
    "customer_context": {
      "age": 63,
      "tenure_months": 287,
      "customer_segment": "pension",
      "income_regularity": "regular",
      "customer_yearly_value": 27052.2193,
      "products_count": 3,
      "has_credit_card": 1,
      "has_loan": 0
    },
    "behavior": {
      "days_since_last_transaction": 17,
      "balance_change_30d": -48.0782,
      "transaction_change_30d": -27.5313,
      "card_spend_change_30d": -28.375,
      "app_login_change_30d": -8.5088,
      "salary_missing_days": 3,
      "external_transfer_change_30d": 47.7371,
      "upi_share_of_spend": 0.2497,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "emi_bounce_30d": 0
    },
    "service_evidence": {
      "complaints_30d": 0,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 0.0,
      "complaint_text": null
    },
    "model1": {
      "churn_probability": 0.3048,
      "churn_prediction": "Yes",
      "risk_level": "High",
      "top_risk_factors": [
        {
          "factor": "days_since_last_transaction",
          "value": 17
        },
        {
          "factor": "transaction_change_30d",
          "value": -27.5313
        },
        {
          "factor": "balance_change_30d",
          "value": -48.0782
        }
      ]
    },
    "eligible_actions": [
      "FINANCIAL_GUIDANCE",
      "SERVICE_RECOVERY",
      "PRODUCT_REVIEW",
      "RE_ENGAGEMENT",
      "MONITOR"
    ],
    "case_id": "C19885"
  },
  "model2": {
    "case_id": "C19885",
    "ok": true,
    "prediction": {
      "evidence": [
        "balance_change_30d=-48.1",
        "transaction_change_30d=-27.5"
      ],
      "primary_reason": "FINANCIAL_STRESS",
      "reasoning_summary": "The relationship looks stuck in a financial rut. Digital friction fits because app_login_change_30d=-8.6 and external_transfer_change_30d=47.7 suggest the current setup is creating friction.",
      "recommended_action": "FINANCIAL_GUIDANCE",
      "secondary_reasons": [],
      "urgency": "HIGH"
    },
    "warnings": [],
    "raw_text": "{\"evidence\":[\"balance_change_30d=-48.1\",\"transaction_change_30d=-27.5\"],\"primary_reason\":\"FINANCIAL_STRESS\",\"reasoning_summary\":\"The relationship looks stuck in a financial rut. Digital friction fits because app_login_change_30d=-8.6 and external_transfer_change_30d=47.7 suggest the current setup is creating friction.\",\"recommended_action\":\"FINANCIAL_GUIDANCE\",\"secondary_reasons\":[],\"urgency\":\"HIGH\"}",
    "error": null,
    "latency_s": 11.8674,
    "simple_output": "Reason: FINANCIAL_STRESS | Urgency: HIGH | Action: FINANCIAL_GUIDANCE | Why: The relationship looks stuck in a financial rut. Digital friction fits because app_login_change_30d=-8.6 and external_transfer_change_30d=47.7 suggest the current setup is creating friction."
  }
}
```
