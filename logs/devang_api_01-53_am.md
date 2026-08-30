# Devang Model 1 -> Model 2 API Test Results

- API URL: `http://127.0.0.1:8001`
- Created at: `2026-08-31T01:55:17`
- Customers tested: `20`
- Source CSV: `model_1_v2\data\customers.csv`
- Health OK: `True`
- Ollama model: `devang-model2-q4`
- Model 1 loaded: `True`

## Summary

| # | Customer | Model 1 risk | Prediction | Reason | Urgency | Action | OK | Seconds |
|---:|---|---:|---|---|---|---|---|---:|
| 1 | Maanav Kalita (`C11943`) | 2.95 | No | UNKNOWN | LOW | MONITOR | yes | 12.58 |
| 2 | Rushil Lala (`C12229`) | 41.5 | Yes | SERVICE_DISSATISFACTION | MEDIUM | SERVICE_RECOVERY | yes | 8.66 |
| 3 | Chakradev Varghese (`C12305`) | 7.92 | No | SERVICE_DISSATISFACTION | MEDIUM | SERVICE_RECOVERY | yes | 6.94 |
| 4 | Netra Sehgal (`C12387`) | 1.66 | No | DIGITAL_FRICTION | MEDIUM | RE_ENGAGEMENT | yes | 5.66 |
| 5 | Aarna Prashad (`C12458`) | 3.2 | No | UNKNOWN | LOW | MONITOR | yes | 4.94 |
| 6 | Raksha Dey (`C12665`) | 3.62 | No | UNKNOWN | LOW | MONITOR | yes | 4.64 |
| 7 | Varenya Chander (`C13013`) | 2.57 | No | UNKNOWN | LOW | MONITOR | yes | 4.97 |
| 8 | Ikbal Rama (`C13510`) | 3.22 | No | SERVICE_DISSATISFACTION | MEDIUM | COMPLAINT_ESCALATION | yes | 2.4 |
| 9 | Brijesh Grover (`C15116`) | 20.84 | Yes | SERVICE_DISSATISFACTION | MEDIUM | COMPLAINT_ESCALATION | yes | 2.5 |
| 10 | Kashish Sunder (`C15803`) | 4.41 | No | SERVICE_DISSATISFACTION | MEDIUM | SERVICE_RECOVERY | yes | 5.57 |
| 11 | Chakradev Dube (`C15841`) | 4.1 | No | UNKNOWN | LOW | MONITOR | yes | 4.83 |
| 12 | Oscar Contractor (`C16195`) | 35.84 | Yes | SERVICE_DISSATISFACTION | HIGH | COMPLAINT_ESCALATION | yes | 3.79 |
| 13 | Krishna Dhar (`C16445`) | 1.69 | No | UNKNOWN | LOW | MONITOR | yes | 7.25 |
| 14 | Zaid Dube (`C17792`) | 6.68 | No | UNKNOWN | LOW | MONITOR | yes | 7.07 |
| 15 | Wishi Radhakrishnan (`C17972`) | 2.1 | No | UNKNOWN | LOW | MONITOR | yes | 8.79 |
| 16 | Charita Nair (`C18567`) | 2.52 | No | UNKNOWN | LOW | MONITOR | yes | 8.82 |
| 17 | Aashi Datta (`C18742`) | 2.55 | No | SERVICE_DISSATISFACTION | MEDIUM | SERVICE_RECOVERY | yes | 10.31 |
| 18 | Rishi Amble (`C18959`) | 2.56 | No | FEE_DISSATISFACTION | MEDIUM | FEE_WAIVER_REVIEW | yes | 5.23 |
| 19 | Abhimanyu Chandran (`C19165`) | 2.56 | No | UNKNOWN | LOW | MONITOR | yes | 8.46 |
| 20 | Reyansh Dayal (`C19912`) | 9.12 | No | SERVICE_DISSATISFACTION | MEDIUM | COMPLAINT_ESCALATION | yes | 4.24 |

## Details

### Maanav Kalita (`C11943`)

- OK: `True`
- Shape errors: `[]`
- Simple output: Reason: UNKNOWN | Urgency: LOW | Action: MONITOR | Why: Complaint and resolution signals are mixed or weak; evidence is genuinely unclear.

Request:

```json
{
  "customer_id": "C11943",
  "customer_name": "Maanav Kalita",
  "prediction_date": "2026-06-01",
  "snapshot_date": "2026-06-01",
  "target_month": "2026-07-01",
  "profile": {
    "tenure_months": 57,
    "customer_segment": "vendor",
    "income_regularity": "irregular",
    "products_count": 1,
    "has_credit_card": 0,
    "has_loan": 0
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 8,
      "balance_change_30d": -17.2241,
      "transaction_change_30d": 3.8208,
      "card_spend_change_30d": 22.2802,
      "app_login_change_30d": -23.2769,
      "salary_missing_days": null,
      "external_transfer_change_30d": -32.7824,
      "upi_share_of_spend": 0.6709,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 0,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 2,
      "avg_resolution_time_hrs": 0.0,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-02-01",
      "days_since_last_transaction": 8,
      "balance_change_30d": 3.8401,
      "transaction_change_30d": 11.4586,
      "card_spend_change_30d": -27.6942,
      "app_login_change_30d": -7.1947,
      "salary_missing_days": null,
      "external_transfer_change_30d": 8.5596,
      "upi_share_of_spend": 0.5433,
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
      "days_since_last_transaction": 5,
      "balance_change_30d": 39.2108,
      "transaction_change_30d": 12.2713,
      "card_spend_change_30d": 37.0306,
      "app_login_change_30d": 35.6792,
      "salary_missing_days": null,
      "external_transfer_change_30d": -36.9506,
      "upi_share_of_spend": 0.6437,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 2,
      "unresolved_complaints": 1,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 9.9089,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-04-01",
      "days_since_last_transaction": 2,
      "balance_change_30d": 19.2135,
      "transaction_change_30d": 36.3567,
      "card_spend_change_30d": 36.366,
      "app_login_change_30d": 18.4461,
      "salary_missing_days": null,
      "external_transfer_change_30d": -21.0358,
      "upi_share_of_spend": 0.5381,
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
      "days_since_last_transaction": 5,
      "balance_change_30d": 38.9401,
      "transaction_change_30d": 17.7045,
      "card_spend_change_30d": 42.0343,
      "app_login_change_30d": 20.7815,
      "salary_missing_days": null,
      "external_transfer_change_30d": -37.6973,
      "upi_share_of_spend": 0.4455,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 0,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 2,
      "avg_resolution_time_hrs": 0.0,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-06-01",
      "days_since_last_transaction": 5,
      "balance_change_30d": 47.7232,
      "transaction_change_30d": 31.2274,
      "card_spend_change_30d": 31.7993,
      "app_login_change_30d": 13.7833,
      "salary_missing_days": null,
      "external_transfer_change_30d": -29.7932,
      "upi_share_of_spend": 0.6249,
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
    "tenure_months": 57,
    "customer_segment": "vendor",
    "income_regularity": "irregular",
    "products_count": 1,
    "has_credit_card": 0,
    "has_loan": 0,
    "days_since_last_transaction": 5,
    "balance_change_30d": 47.7232,
    "transaction_change_30d": 31.2274,
    "card_spend_change_30d": 31.7993,
    "app_login_change_30d": 13.7833,
    "salary_missing_days": null,
    "external_transfer_change_30d": -29.7932,
    "upi_share_of_spend": 0.6249,
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
      "tenure_months": 57,
      "age": 41,
      "customer_yearly_value": 13165.4842,
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
    "served_at": "2026-08-31T01:53:22",
    "elapsed_ms": 12559.28,
    "timings_ms": {
      "model1": 219.45,
      "model2": 12339.61
    },
    "customer_id": "C11943",
    "customer_name": "Maanav Kalita",
    "snapshot_date": "2026-06-01"
  },
  "model1": {
    "churn_probability": 2.95,
    "raw_churn_probability": 26.98,
    "probability_mode": "sigmoid",
    "risk_score": 8.84,
    "churn_prediction": "No",
    "risk_level": "Low",
    "top_risk_factors": [
      {
        "factor": "latest_vs_avg_upi_share_of_spend_available_history",
        "value": 0.04716666666666669,
        "message": "A larger share of spending is happening through UPI.",
        "contribution": 0.09300187230110168
      },
      {
        "factor": "card_spend_change_30d_trend_6m",
        "value": 7.317611428571425,
        "message": "This signal increased churn risk.",
        "contribution": 0.06793023645877838
      },
      {
        "factor": "latest_vs_avg_balance_change_30d_available_history",
        "value": 25.7726,
        "message": "This signal increased churn risk.",
        "contribution": 0.06787043064832687
      },
      {
        "factor": "avg_balance_change_30d_3m",
        "value": 35.29226666666667,
        "message": "This signal increased churn risk.",
        "contribution": 0.04148125648498535
      },
      {
        "factor": "latest_upi_share_of_spend",
        "value": 0.6249,
        "message": "A larger share of spending is happening through UPI.",
        "contribution": 0.03592826798558235
      }
    ]
  },
  "model2_input": {
    "customer_context": {
      "age": 41,
      "tenure_months": 57,
      "customer_segment": "vendor",
      "income_regularity": "irregular",
      "customer_yearly_value": 13165.4842,
      "products_count": 1,
      "has_credit_card": 0,
      "has_loan": 0
    },
    "behavior": {
      "days_since_last_transaction": 5,
      "balance_change_30d": 47.7232,
      "transaction_change_30d": 31.2274,
      "card_spend_change_30d": 31.7993,
      "app_login_change_30d": 13.7833,
      "salary_missing_days": null,
      "external_transfer_change_30d": -29.7932,
      "upi_share_of_spend": 0.6249,
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
      "churn_probability": 0.0295,
      "churn_prediction": "No",
      "risk_level": "Low",
      "top_risk_factors": [
        {
          "factor": "upi_share_of_spend",
          "value": 0.6249
        },
        {
          "factor": "card_spend_change_30d",
          "value": 31.7993
        },
        {
          "factor": "balance_change_30d",
          "value": 47.7232
        }
      ]
    },
    "eligible_actions": [
      "RE_ENGAGEMENT",
      "PRODUCT_REVIEW",
      "MONITOR"
    ],
    "case_id": "C11943"
  },
  "model2": {
    "case_id": "C11943",
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
    "raw_text": "{\"evidence\":[\"complaints_30d=0\",\"unresolved_complaints=0\",\"avg_resolution_time_hrs=0.0\"],\"primary_reason\":\"LOW_ENGAGEMENT\",\"reasoning_summary\":\"Days_since_last_transaction=5 and transaction_change_30d=31.2 are the strongest signals pointing to LOW_ENGAGEMENT.\",\"recommended_action\":\"RE_ENGAGEMENT\",\"secondary_reasons\":[],\"urgency\":\"MEDIUM\"}",
    "error": null,
    "latency_s": 12.3394,
    "simple_output": "Reason: UNKNOWN | Urgency: LOW | Action: MONITOR | Why: Complaint and resolution signals are mixed or weak; evidence is genuinely unclear."
  }
}
```

### Rushil Lala (`C12229`)

- OK: `True`
- Shape errors: `[]`
- Simple output: Reason: SERVICE_DISSATISFACTION | Urgency: MEDIUM | Action: SERVICE_RECOVERY | Why: Complaint escalation because complaints_30d=1 and failed_transactions_30d=7 suggest SERVICE_DISSATISFACTION at 20%.

Request:

```json
{
  "customer_id": "C12229",
  "customer_name": "Rushil Lala",
  "prediction_date": "2026-04-01",
  "snapshot_date": "2026-04-01",
  "target_month": "2026-05-01",
  "profile": {
    "tenure_months": 23,
    "customer_segment": "vendor",
    "income_regularity": "irregular",
    "products_count": 2,
    "has_credit_card": 1,
    "has_loan": 0
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 1,
      "balance_change_30d": -9.5333,
      "transaction_change_30d": -0.909,
      "card_spend_change_30d": -19.9492,
      "app_login_change_30d": -3.8573,
      "salary_missing_days": null,
      "external_transfer_change_30d": 3.584,
      "upi_share_of_spend": 0.3546,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 0,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 2,
      "avg_resolution_time_hrs": 0.0,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-02-01",
      "days_since_last_transaction": 7,
      "balance_change_30d": -16.9696,
      "transaction_change_30d": 2.095,
      "card_spend_change_30d": -1.4148,
      "app_login_change_30d": -24.8644,
      "salary_missing_days": null,
      "external_transfer_change_30d": 28.6601,
      "upi_share_of_spend": 0.4516,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 1,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 43.4827,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-03-01",
      "days_since_last_transaction": 11,
      "balance_change_30d": -44.0304,
      "transaction_change_30d": -17.3357,
      "card_spend_change_30d": -20.8457,
      "app_login_change_30d": -31.4923,
      "salary_missing_days": null,
      "external_transfer_change_30d": 72.5496,
      "upi_share_of_spend": 0.3905,
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
      "days_since_last_transaction": 14,
      "balance_change_30d": -80.1619,
      "transaction_change_30d": -38.4202,
      "card_spend_change_30d": -21.2583,
      "app_login_change_30d": -34.1397,
      "salary_missing_days": null,
      "external_transfer_change_30d": 61.6553,
      "upi_share_of_spend": 0.6042,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 7,
      "avg_resolution_time_hrs": 16.9292,
      "emi_bounce_30d": 0
    }
  ],
  "customer": {
    "tenure_months": 23,
    "customer_segment": "vendor",
    "income_regularity": "irregular",
    "products_count": 2,
    "has_credit_card": 1,
    "has_loan": 0,
    "days_since_last_transaction": 14,
    "balance_change_30d": -80.1619,
    "transaction_change_30d": -38.4202,
    "card_spend_change_30d": -21.2583,
    "app_login_change_30d": -34.1397,
    "salary_missing_days": null,
    "external_transfer_change_30d": 61.6553,
    "upi_share_of_spend": 0.6042,
    "fd_maturing_in_30d": 0,
    "products_dropped_90d": 0,
    "complaints_30d": 1,
    "unresolved_complaints": 0,
    "failed_transactions_30d": 7,
    "avg_resolution_time_hrs": 16.9292,
    "emi_bounce_30d": 0
  },
  "extra_context": {
    "customer_profile": {
      "segment": "vendor",
      "income_regularity": "irregular",
      "tenure_months": 23,
      "age": 54,
      "customer_yearly_value": 17822.3821,
      "products_count": 2,
      "has_credit_card": 1,
      "has_loan": 0,
      "value_tier": "low"
    },
    "recent_complaint_text": "Branch opens late almost daily. Customers wait outside in the sun."
  }
}
```

Response:

```json
{
  "meta": {
    "endpoint": "/predict/both",
    "served_at": "2026-08-31T01:53:31",
    "elapsed_ms": 8650.33,
    "timings_ms": {
      "model1": 152.0,
      "model2": 8498.13
    },
    "customer_id": "C12229",
    "customer_name": "Rushil Lala",
    "snapshot_date": "2026-04-01"
  },
  "model1": {
    "churn_probability": 41.5,
    "raw_churn_probability": 94.65,
    "probability_mode": "sigmoid",
    "risk_score": 78.06,
    "churn_prediction": "Yes",
    "risk_level": "High",
    "top_risk_factors": [
      {
        "factor": "latest_days_since_last_transaction",
        "value": 14,
        "message": "Customer has gone longer without transacting.",
        "contribution": 0.4540511667728424
      },
      {
        "factor": "latest_transaction_change_30d",
        "value": -38.4202,
        "message": "Transaction activity has been falling across recent months.",
        "contribution": 0.3989320993423462
      },
      {
        "factor": "sum_failed_transactions_30d_3m",
        "value": 8.0,
        "message": "Customer has recent failed transactions.",
        "contribution": 0.24490542709827423
      },
      {
        "factor": "latest_balance_change_30d",
        "value": -80.1619,
        "message": "Balance has been falling across recent months.",
        "contribution": 0.2413872927427292
      },
      {
        "factor": "latest_vs_avg_upi_share_of_spend_available_history",
        "value": 0.15397499999999997,
        "message": "A larger share of spending is happening through UPI.",
        "contribution": 0.20933358371257782
      }
    ]
  },
  "model2_input": {
    "customer_context": {
      "age": 54,
      "tenure_months": 23,
      "customer_segment": "vendor",
      "income_regularity": "irregular",
      "customer_yearly_value": 17822.3821,
      "products_count": 2,
      "has_credit_card": 1,
      "has_loan": 0
    },
    "behavior": {
      "days_since_last_transaction": 14,
      "balance_change_30d": -80.1619,
      "transaction_change_30d": -38.4202,
      "card_spend_change_30d": -21.2583,
      "app_login_change_30d": -34.1397,
      "salary_missing_days": null,
      "external_transfer_change_30d": 61.6553,
      "upi_share_of_spend": 0.6042,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "emi_bounce_30d": 0
    },
    "service_evidence": {
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 7,
      "avg_resolution_time_hrs": 16.9292,
      "complaint_text": "Branch opens late almost daily. Customers wait outside in the sun."
    },
    "model1": {
      "churn_probability": 0.415,
      "churn_prediction": "Yes",
      "risk_level": "High",
      "top_risk_factors": [
        {
          "factor": "days_since_last_transaction",
          "value": 14
        },
        {
          "factor": "transaction_change_30d",
          "value": -38.4202
        },
        {
          "factor": "failed_transactions_30d",
          "value": 7
        }
      ]
    },
    "eligible_actions": [
      "SERVICE_RECOVERY",
      "PRODUCT_REVIEW",
      "RE_ENGAGEMENT",
      "RM_CALLBACK",
      "MONITOR"
    ],
    "case_id": "C12229"
  },
  "model2": {
    "case_id": "C12229",
    "ok": true,
    "prediction": {
      "evidence": [
        "complaints_30d=1",
        "unresolved_complaints=0",
        "failed_transactions_30d=7",
        "avg_resolution_time_hrs=16.9",
        "transaction_change_30d=-38.4"
      ],
      "primary_reason": "SERVICE_DISSATISFACTION",
      "reasoning_summary": "Complaint escalation because complaints_30d=1 and failed_transactions_30d=7 suggest SERVICE_DISSATISFACTION at 20%.",
      "recommended_action": "SERVICE_RECOVERY",
      "secondary_reasons": [],
      "urgency": "MEDIUM"
    },
    "warnings": [
      "evidence: 'unresolved_complaints=0' cites a zero/null value, which is not evidence; remove it",
      "reasoning_summary: describes COMPLAINT_ESCALATION but recommended_action is SERVICE_RECOVERY; rewrite the summary around the action you chose"
    ],
    "raw_text": "{\"evidence\":[\"complaints_30d=1\",\"failed_transactions_30d=7\",\"transaction_change_30d=-38.4\"],\"primary_reason\":\"SERVICE_DISSATISFACTION\",\"reasoning_summary\":\"Complaint escalation fits because complaints_30d=1 and failed_transactions_30d=7 show SERVICE_DISSATISFACTION.\",\"recommended_action\":\"SERVICE_RECOVERY\",\"secondary_reasons\":[],\"urgency\":\"HIGH\"}",
    "error": null,
    "latency_s": 8.4979,
    "simple_output": "Reason: SERVICE_DISSATISFACTION | Urgency: MEDIUM | Action: SERVICE_RECOVERY | Why: Complaint escalation because complaints_30d=1 and failed_transactions_30d=7 suggest SERVICE_DISSATISFACTION at 20%."
  }
}
```

### Chakradev Varghese (`C12305`)

- OK: `True`
- Shape errors: `[]`
- Simple output: Reason: SERVICE_DISSATISFACTION | Urgency: MEDIUM | Action: SERVICE_RECOVERY | Why: Complaint escalation because complaints_30d=2 and avg_resolution_time_hrs=11.1 suggest a service issue.

Request:

```json
{
  "customer_id": "C12305",
  "customer_name": "Chakradev Varghese",
  "prediction_date": "2026-06-01",
  "snapshot_date": "2026-06-01",
  "target_month": "2026-07-01",
  "profile": {
    "tenure_months": 50,
    "customer_segment": "vendor",
    "income_regularity": "irregular",
    "products_count": 3,
    "has_credit_card": 0,
    "has_loan": 1
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 6,
      "balance_change_30d": -8.0959,
      "transaction_change_30d": -17.8335,
      "card_spend_change_30d": 16.841,
      "app_login_change_30d": -23.8679,
      "salary_missing_days": null,
      "external_transfer_change_30d": 39.3731,
      "upi_share_of_spend": 0.5778,
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
      "balance_change_30d": 4.0536,
      "transaction_change_30d": 31.8941,
      "card_spend_change_30d": 18.364,
      "app_login_change_30d": 31.5914,
      "salary_missing_days": null,
      "external_transfer_change_30d": -33.3598,
      "upi_share_of_spend": 0.6456,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 12.9133,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-03-01",
      "days_since_last_transaction": 9,
      "balance_change_30d": 5.1505,
      "transaction_change_30d": 5.2971,
      "card_spend_change_30d": 8.0146,
      "app_login_change_30d": -12.9752,
      "salary_missing_days": null,
      "external_transfer_change_30d": 19.0226,
      "upi_share_of_spend": 0.66,
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
      "days_since_last_transaction": 1,
      "balance_change_30d": 1.1623,
      "transaction_change_30d": 23.5862,
      "card_spend_change_30d": 10.0726,
      "app_login_change_30d": 17.6851,
      "salary_missing_days": null,
      "external_transfer_change_30d": -41.7065,
      "upi_share_of_spend": 0.6707,
      "fd_maturing_in_30d": 1,
      "products_dropped_90d": 0,
      "complaints_30d": 0,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 0.0,
      "emi_bounce_30d": 1
    },
    {
      "snapshot_date": "2026-05-01",
      "days_since_last_transaction": 6,
      "balance_change_30d": 8.3259,
      "transaction_change_30d": 17.1934,
      "card_spend_change_30d": 5.4322,
      "app_login_change_30d": 25.2706,
      "salary_missing_days": null,
      "external_transfer_change_30d": -44.3096,
      "upi_share_of_spend": 0.5901,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 15.6162,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-06-01",
      "days_since_last_transaction": 10,
      "balance_change_30d": -7.5091,
      "transaction_change_30d": 12.2201,
      "card_spend_change_30d": -25.5389,
      "app_login_change_30d": -45.6591,
      "salary_missing_days": null,
      "external_transfer_change_30d": 53.3148,
      "upi_share_of_spend": 0.691,
      "fd_maturing_in_30d": 1,
      "products_dropped_90d": 0,
      "complaints_30d": 2,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 3,
      "avg_resolution_time_hrs": 11.083,
      "emi_bounce_30d": 0
    }
  ],
  "customer": {
    "tenure_months": 50,
    "customer_segment": "vendor",
    "income_regularity": "irregular",
    "products_count": 3,
    "has_credit_card": 0,
    "has_loan": 1,
    "days_since_last_transaction": 10,
    "balance_change_30d": -7.5091,
    "transaction_change_30d": 12.2201,
    "card_spend_change_30d": -25.5389,
    "app_login_change_30d": -45.6591,
    "salary_missing_days": null,
    "external_transfer_change_30d": 53.3148,
    "upi_share_of_spend": 0.691,
    "fd_maturing_in_30d": 1,
    "products_dropped_90d": 0,
    "complaints_30d": 2,
    "unresolved_complaints": 0,
    "failed_transactions_30d": 3,
    "avg_resolution_time_hrs": 11.083,
    "emi_bounce_30d": 0
  },
  "extra_context": {
    "customer_profile": {
      "segment": "vendor",
      "income_regularity": "irregular",
      "tenure_months": 50,
      "age": 54,
      "customer_yearly_value": 9600.0826,
      "products_count": 3,
      "has_credit_card": 0,
      "has_loan": 1,
      "value_tier": "low"
    },
    "recent_complaint_text": "Requesting duplicate PIN as I have forgotten mine. Guide the process."
  }
}
```

Response:

```json
{
  "meta": {
    "endpoint": "/predict/both",
    "served_at": "2026-08-31T01:53:38",
    "elapsed_ms": 6920.3,
    "timings_ms": {
      "model1": 132.91,
      "model2": 6787.18
    },
    "customer_id": "C12305",
    "customer_name": "Chakradev Varghese",
    "snapshot_date": "2026-06-01"
  },
  "model1": {
    "churn_probability": 7.92,
    "raw_churn_probability": 49.33,
    "probability_mode": "sigmoid",
    "risk_score": 23.76,
    "churn_prediction": "No",
    "risk_level": "Low",
    "top_risk_factors": [
      {
        "factor": "latest_vs_avg_upi_share_of_spend_available_history",
        "value": 0.05179999999999996,
        "message": "A larger share of spending is happening through UPI.",
        "contribution": 0.19634394347667694
      },
      {
        "factor": "latest_fd_maturing_in_30d",
        "value": 1,
        "message": "Customer has a fixed deposit maturing soon.",
        "contribution": 0.1402580738067627
      },
      {
        "factor": "sum_fd_maturing_in_30d_3m",
        "value": 2.0,
        "message": "Customer has a fixed deposit maturing soon.",
        "contribution": 0.12331406027078629
      },
      {
        "factor": "latest_failed_transactions_30d",
        "value": 3,
        "message": "Customer has recent failed transactions.",
        "contribution": 0.09307778626680374
      },
      {
        "factor": "sum_failed_transactions_30d_3m",
        "value": 5.0,
        "message": "Customer has recent failed transactions.",
        "contribution": 0.05392167344689369
      }
    ]
  },
  "model2_input": {
    "customer_context": {
      "age": 54,
      "tenure_months": 50,
      "customer_segment": "vendor",
      "income_regularity": "irregular",
      "customer_yearly_value": 9600.0826,
      "products_count": 3,
      "has_credit_card": 0,
      "has_loan": 1
    },
    "behavior": {
      "days_since_last_transaction": 10,
      "balance_change_30d": -7.5091,
      "transaction_change_30d": 12.2201,
      "card_spend_change_30d": -25.5389,
      "app_login_change_30d": -45.6591,
      "salary_missing_days": null,
      "external_transfer_change_30d": 53.3148,
      "upi_share_of_spend": 0.691,
      "fd_maturing_in_30d": 1,
      "products_dropped_90d": 0,
      "emi_bounce_30d": 0
    },
    "service_evidence": {
      "complaints_30d": 2,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 3,
      "avg_resolution_time_hrs": 11.083,
      "complaint_text": "Requesting duplicate PIN as I have forgotten mine. Guide the process."
    },
    "model1": {
      "churn_probability": 0.0792,
      "churn_prediction": "No",
      "risk_level": "Low",
      "top_risk_factors": [
        {
          "factor": "upi_share_of_spend",
          "value": 0.691
        },
        {
          "factor": "fd_maturing_in_30d",
          "value": 1
        },
        {
          "factor": "failed_transactions_30d",
          "value": 3
        }
      ]
    },
    "eligible_actions": [
      "SERVICE_RECOVERY",
      "PRODUCT_REVIEW",
      "RE_ENGAGEMENT",
      "MONITOR"
    ],
    "case_id": "C12305"
  },
  "model2": {
    "case_id": "C12305",
    "ok": true,
    "prediction": {
      "evidence": [
        "complaints_30d=2",
        "unresolved_complaints=0",
        "avg_resolution_time_hrs=11.1",
        "complaint_text describes a recent service issue"
      ],
      "primary_reason": "SERVICE_DISSATISFACTION",
      "reasoning_summary": "Complaint escalation because complaints_30d=2 and avg_resolution_time_hrs=11.1 suggest a service issue.",
      "recommended_action": "SERVICE_RECOVERY",
      "secondary_reasons": [],
      "urgency": "MEDIUM"
    },
    "warnings": [
      "evidence: 'unresolved_complaints=0' cites a zero/null value, which is not evidence; remove it",
      "reasoning_summary: describes COMPLAINT_ESCALATION but recommended_action is SERVICE_RECOVERY; rewrite the summary around the action you chose"
    ],
    "raw_text": "{\"evidence\":[\"complaints_30d=2\",\"failed_transactions_30d=3\",\"avg_resolution_time_hrs=11.1\",\"complaint_text describes a real service issue without being clearly escalated or resolved\"],\"primary_reason\":\"SERVICE_DISSATISFACTION\",\"reasoning_summary\":\"Complaint escalation fits because complaints_30d=2 and failed_transactions_30d=3 show a real service issue without being clearly escalated or resolved.\",\"recommended_action\":\"SERVICE_RECOVERY\",\"secondary_reasons\":[],\"urgency\":\"HIGH\"}",
    "error": null,
    "latency_s": 6.7856,
    "simple_output": "Reason: SERVICE_DISSATISFACTION | Urgency: MEDIUM | Action: SERVICE_RECOVERY | Why: Complaint escalation because complaints_30d=2 and avg_resolution_time_hrs=11.1 suggest a service issue."
  }
}
```

### Netra Sehgal (`C12387`)

- OK: `True`
- Shape errors: `[]`
- Simple output: Reason: DIGITAL_FRICTION | Urgency: MEDIUM | Action: RE_ENGAGEMENT | Why: Digital friction is supported by card_spend_change_30d=19.7 and external_transfer_change_30d=5.1 pointing to a card or transaction experience issue.

Request:

```json
{
  "customer_id": "C12387",
  "customer_name": "Netra Sehgal",
  "prediction_date": "2026-06-01",
  "snapshot_date": "2026-06-01",
  "target_month": "2026-07-01",
  "profile": {
    "tenure_months": 180,
    "customer_segment": "farmer",
    "income_regularity": "seasonal",
    "products_count": 1,
    "has_credit_card": 0,
    "has_loan": 0
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 13,
      "balance_change_30d": -16.5649,
      "transaction_change_30d": -51.5165,
      "card_spend_change_30d": -51.0974,
      "app_login_change_30d": 4.1427,
      "salary_missing_days": null,
      "external_transfer_change_30d": 21.8034,
      "upi_share_of_spend": 0.5148,
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
      "days_since_last_transaction": 13,
      "balance_change_30d": -20.9463,
      "transaction_change_30d": -44.9417,
      "card_spend_change_30d": -26.6895,
      "app_login_change_30d": -9.5999,
      "salary_missing_days": null,
      "external_transfer_change_30d": 22.8319,
      "upi_share_of_spend": 0.4358,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 1,
      "complaints_30d": 2,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 2.5159,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-03-01",
      "days_since_last_transaction": 12,
      "balance_change_30d": -17.7364,
      "transaction_change_30d": -13.8309,
      "card_spend_change_30d": -4.8068,
      "app_login_change_30d": -14.8597,
      "salary_missing_days": null,
      "external_transfer_change_30d": 8.9688,
      "upi_share_of_spend": 0.3245,
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
      "days_since_last_transaction": 9,
      "balance_change_30d": -11.1413,
      "transaction_change_30d": 3.7024,
      "card_spend_change_30d": 16.0838,
      "app_login_change_30d": 22.774,
      "salary_missing_days": null,
      "external_transfer_change_30d": 46.2693,
      "upi_share_of_spend": 0.2864,
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
      "balance_change_30d": 24.9497,
      "transaction_change_30d": 21.6997,
      "card_spend_change_30d": 18.3102,
      "app_login_change_30d": 16.9062,
      "salary_missing_days": null,
      "external_transfer_change_30d": -5.6184,
      "upi_share_of_spend": 0.2766,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 2,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 18.647,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-06-01",
      "days_since_last_transaction": 5,
      "balance_change_30d": 6.2587,
      "transaction_change_30d": 10.2211,
      "card_spend_change_30d": 19.714,
      "app_login_change_30d": -14.3253,
      "salary_missing_days": null,
      "external_transfer_change_30d": 5.0691,
      "upi_share_of_spend": 0.2772,
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
    "tenure_months": 180,
    "customer_segment": "farmer",
    "income_regularity": "seasonal",
    "products_count": 1,
    "has_credit_card": 0,
    "has_loan": 0,
    "days_since_last_transaction": 5,
    "balance_change_30d": 6.2587,
    "transaction_change_30d": 10.2211,
    "card_spend_change_30d": 19.714,
    "app_login_change_30d": -14.3253,
    "salary_missing_days": null,
    "external_transfer_change_30d": 5.0691,
    "upi_share_of_spend": 0.2772,
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
      "tenure_months": 180,
      "age": 52,
      "customer_yearly_value": 24158.734,
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
    "served_at": "2026-08-31T01:53:43",
    "elapsed_ms": 5646.96,
    "timings_ms": {
      "model1": 246.97,
      "model2": 5399.73
    },
    "customer_id": "C12387",
    "customer_name": "Netra Sehgal",
    "snapshot_date": "2026-06-01"
  },
  "model1": {
    "churn_probability": 1.66,
    "raw_churn_probability": 14.37,
    "probability_mode": "sigmoid",
    "risk_score": 4.98,
    "churn_prediction": "No",
    "risk_level": "Low",
    "top_risk_factors": [
      {
        "factor": "count_balance_drop_6m",
        "value": 4,
        "message": "This signal increased churn risk.",
        "contribution": 0.03476974368095398
      },
      {
        "factor": "card_spend_change_30d_trend_6m",
        "value": 14.569905714285712,
        "message": "This signal increased churn risk.",
        "contribution": 0.03459930047392845
      },
      {
        "factor": "latest_vs_avg_external_transfer_change_30d_available_history",
        "value": -11.48491666666667,
        "message": "This signal increased churn risk.",
        "contribution": 0.027573557570576668
      },
      {
        "factor": "max_days_since_last_transaction_3m",
        "value": 9.0,
        "message": "Customer has gone longer without transacting.",
        "contribution": 0.0244675874710083
      },
      {
        "factor": "count_balance_drop_3m",
        "value": 1,
        "message": "This signal increased churn risk.",
        "contribution": 0.005091591272503138
      }
    ]
  },
  "model2_input": {
    "customer_context": {
      "age": 52,
      "tenure_months": 180,
      "customer_segment": "farmer",
      "income_regularity": "seasonal",
      "customer_yearly_value": 24158.734,
      "products_count": 1,
      "has_credit_card": 0,
      "has_loan": 0
    },
    "behavior": {
      "days_since_last_transaction": 5,
      "balance_change_30d": 6.2587,
      "transaction_change_30d": 10.2211,
      "card_spend_change_30d": 19.714,
      "app_login_change_30d": -14.3253,
      "salary_missing_days": null,
      "external_transfer_change_30d": 5.0691,
      "upi_share_of_spend": 0.2772,
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
      "churn_probability": 0.0166,
      "churn_prediction": "No",
      "risk_level": "Low",
      "top_risk_factors": [
        {
          "factor": "card_spend_change_30d",
          "value": 19.714
        },
        {
          "factor": "external_transfer_change_30d",
          "value": 5.0691
        },
        {
          "factor": "days_since_last_transaction",
          "value": 5
        }
      ]
    },
    "eligible_actions": [
      "RE_ENGAGEMENT",
      "PRODUCT_REVIEW",
      "MONITOR"
    ],
    "case_id": "C12387"
  },
  "model2": {
    "case_id": "C12387",
    "ok": true,
    "prediction": {
      "evidence": [
        "card_spend_change_30d=19.7",
        "external_transfer_change_30d=5.1"
      ],
      "primary_reason": "DIGITAL_FRICTION",
      "reasoning_summary": "Digital friction is supported by card_spend_change_30d=19.7 and external_transfer_change_30d=5.1 pointing to a card or transaction experience issue.",
      "recommended_action": "RE_ENGAGEMENT",
      "secondary_reasons": [],
      "urgency": "MEDIUM"
    },
    "warnings": [],
    "raw_text": "{\"evidence\":[\"card_spend_change_30d=19.7\",\"external_transfer_change_30d=5.1\"],\"primary_reason\":\"DIGITAL_FRICTION\",\"reasoning_summary\":\"Digital friction is supported by card_spend_change_30d=19.7 and external_transfer_change_30d=5.1 pointing to a card or transaction experience issue.\",\"recommended_action\":\"RE_ENGAGEMENT\",\"secondary_reasons\":[],\"urgency\":\"MEDIUM\"}",
    "error": null,
    "latency_s": 5.3981,
    "simple_output": "Reason: DIGITAL_FRICTION | Urgency: MEDIUM | Action: RE_ENGAGEMENT | Why: Digital friction is supported by card_spend_change_30d=19.7 and external_transfer_change_30d=5.1 pointing to a card or transaction experience issue."
  }
}
```

### Aarna Prashad (`C12458`)

- OK: `True`
- Shape errors: `[]`
- Simple output: Reason: UNKNOWN | Urgency: LOW | Action: MONITOR | Why: Complaint and resolution signals are mixed or weak; evidence is genuinely unclear.

Request:

```json
{
  "customer_id": "C12458",
  "customer_name": "Aarna Prashad",
  "prediction_date": "2026-06-01",
  "snapshot_date": "2026-06-01",
  "target_month": "2026-07-01",
  "profile": {
    "tenure_months": 88,
    "customer_segment": "business",
    "income_regularity": "irregular",
    "products_count": 2,
    "has_credit_card": 0,
    "has_loan": 1
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 3,
      "balance_change_30d": -17.6134,
      "transaction_change_30d": 5.0823,
      "card_spend_change_30d": 0.2329,
      "app_login_change_30d": 17.9131,
      "salary_missing_days": null,
      "external_transfer_change_30d": 48.1316,
      "upi_share_of_spend": 0.168,
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
      "days_since_last_transaction": 3,
      "balance_change_30d": -5.9347,
      "transaction_change_30d": 5.1947,
      "card_spend_change_30d": 13.1348,
      "app_login_change_30d": -15.7478,
      "salary_missing_days": null,
      "external_transfer_change_30d": -23.4353,
      "upi_share_of_spend": 0.1477,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 4,
      "unresolved_complaints": 2,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 64.0188,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-03-01",
      "days_since_last_transaction": 5,
      "balance_change_30d": 1.0313,
      "transaction_change_30d": 12.3305,
      "card_spend_change_30d": -11.1874,
      "app_login_change_30d": 2.549,
      "salary_missing_days": null,
      "external_transfer_change_30d": 12.4105,
      "upi_share_of_spend": 0.1122,
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
      "days_since_last_transaction": 5,
      "balance_change_30d": -0.9225,
      "transaction_change_30d": -10.1335,
      "card_spend_change_30d": 21.1914,
      "app_login_change_30d": -3.3775,
      "salary_missing_days": null,
      "external_transfer_change_30d": -22.8726,
      "upi_share_of_spend": 0.1049,
      "fd_maturing_in_30d": 1,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 1,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 52.1243,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-05-01",
      "days_since_last_transaction": 1,
      "balance_change_30d": 14.9231,
      "transaction_change_30d": 6.2841,
      "card_spend_change_30d": 24.928,
      "app_login_change_30d": 27.1126,
      "salary_missing_days": null,
      "external_transfer_change_30d": 4.9318,
      "upi_share_of_spend": 0.109,
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
      "days_since_last_transaction": 0,
      "balance_change_30d": 9.419,
      "transaction_change_30d": 12.984,
      "card_spend_change_30d": 55.7565,
      "app_login_change_30d": -14.7056,
      "salary_missing_days": null,
      "external_transfer_change_30d": 1.0504,
      "upi_share_of_spend": 0.027,
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
    "tenure_months": 88,
    "customer_segment": "business",
    "income_regularity": "irregular",
    "products_count": 2,
    "has_credit_card": 0,
    "has_loan": 1,
    "days_since_last_transaction": 0,
    "balance_change_30d": 9.419,
    "transaction_change_30d": 12.984,
    "card_spend_change_30d": 55.7565,
    "app_login_change_30d": -14.7056,
    "salary_missing_days": null,
    "external_transfer_change_30d": 1.0504,
    "upi_share_of_spend": 0.027,
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
      "segment": "business",
      "income_regularity": "irregular",
      "tenure_months": 88,
      "age": 34,
      "customer_yearly_value": 224032.8128,
      "products_count": 2,
      "has_credit_card": 0,
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
    "served_at": "2026-08-31T01:53:48",
    "elapsed_ms": 4931.14,
    "timings_ms": {
      "model1": 151.84,
      "model2": 4779.1
    },
    "customer_id": "C12458",
    "customer_name": "Aarna Prashad",
    "snapshot_date": "2026-06-01"
  },
  "model1": {
    "churn_probability": 3.2,
    "raw_churn_probability": 28.77,
    "probability_mode": "sigmoid",
    "risk_score": 9.59,
    "churn_prediction": "No",
    "risk_level": "Low",
    "top_risk_factors": [
      {
        "factor": "max_avg_resolution_time_hrs_3m",
        "value": 52.1243,
        "message": "Recent complaints took longer to resolve.",
        "contribution": 0.3122532367706299
      },
      {
        "factor": "latest_upi_share_of_spend",
        "value": 0.027,
        "message": "A larger share of spending is happening through UPI.",
        "contribution": 0.14980967342853546
      },
      {
        "factor": "sum_fd_maturing_in_30d_3m",
        "value": 1.0,
        "message": "Customer has a fixed deposit maturing soon.",
        "contribution": 0.06626195460557938
      },
      {
        "factor": "sum_unresolved_complaints_6m",
        "value": 3.0,
        "message": "Customer has recent complaint activity.",
        "contribution": 0.03934755548834801
      },
      {
        "factor": "avg_upi_share_of_spend_6m",
        "value": 0.11146666666666666,
        "message": "A larger share of spending is happening through UPI.",
        "contribution": 0.02670297585427761
      }
    ]
  },
  "model2_input": {
    "customer_context": {
      "age": 34,
      "tenure_months": 88,
      "customer_segment": "business",
      "income_regularity": "irregular",
      "customer_yearly_value": 224032.8128,
      "products_count": 2,
      "has_credit_card": 0,
      "has_loan": 1
    },
    "behavior": {
      "days_since_last_transaction": 0,
      "balance_change_30d": 9.419,
      "transaction_change_30d": 12.984,
      "card_spend_change_30d": 55.7565,
      "app_login_change_30d": -14.7056,
      "salary_missing_days": null,
      "external_transfer_change_30d": 1.0504,
      "upi_share_of_spend": 0.027,
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
      "churn_probability": 0.032,
      "churn_prediction": "No",
      "risk_level": "Low",
      "top_risk_factors": [
        {
          "factor": "upi_share_of_spend",
          "value": 0.027
        },
        {
          "factor": "fd_maturing_in_30d",
          "value": 0
        },
        {
          "factor": "unresolved_complaints",
          "value": 0
        }
      ]
    },
    "eligible_actions": [
      "SERVICE_RECOVERY",
      "RE_ENGAGEMENT",
      "MONITOR"
    ],
    "case_id": "C12458"
  },
  "model2": {
    "case_id": "C12458",
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
    "raw_text": "{\"evidence\":[\"complaints_30d=0\",\"unresolved_complaints=0\",\"avg_resolution_time_hrs=0.0\"],\"primary_reason\":\"UNKNOWN\",\"reasoning_summary\":\"Complaint and resolution signals are mixed or weak; relationship-strengthening action is uncertain because evidence is limited.\",\"recommended_action\":\"MONITOR\",\"secondary_reasons\":[],\"urgency\":\"LOW\"}",
    "error": null,
    "latency_s": 4.7783,
    "simple_output": "Reason: UNKNOWN | Urgency: LOW | Action: MONITOR | Why: Complaint and resolution signals are mixed or weak; evidence is genuinely unclear."
  }
}
```

### Raksha Dey (`C12665`)

- OK: `True`
- Shape errors: `[]`
- Simple output: Reason: UNKNOWN | Urgency: LOW | Action: MONITOR | Why: Complaint and resolution signals are mixed or weak; evidence is genuinely unclear.

Request:

```json
{
  "customer_id": "C12665",
  "customer_name": "Raksha Dey",
  "prediction_date": "2026-06-01",
  "snapshot_date": "2026-06-01",
  "target_month": "2026-07-01",
  "profile": {
    "tenure_months": 166,
    "customer_segment": "pension",
    "income_regularity": "regular",
    "products_count": 1,
    "has_credit_card": 0,
    "has_loan": 0
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 5,
      "balance_change_30d": -17.7682,
      "transaction_change_30d": 13.0831,
      "card_spend_change_30d": -32.7373,
      "app_login_change_30d": 24.0787,
      "salary_missing_days": 2.0,
      "external_transfer_change_30d": 32.7507,
      "upi_share_of_spend": 0.2879,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 37.7343,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-02-01",
      "days_since_last_transaction": 2,
      "balance_change_30d": 4.2804,
      "transaction_change_30d": -8.6836,
      "card_spend_change_30d": -21.4134,
      "app_login_change_30d": -25.8962,
      "salary_missing_days": 4.0,
      "external_transfer_change_30d": 29.0012,
      "upi_share_of_spend": 0.2615,
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
      "balance_change_30d": -6.1337,
      "transaction_change_30d": -16.4095,
      "card_spend_change_30d": -24.9147,
      "app_login_change_30d": 19.1528,
      "salary_missing_days": 3.0,
      "external_transfer_change_30d": -12.902,
      "upi_share_of_spend": 0.1925,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 1,
      "complaints_30d": 0,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 0.0,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-04-01",
      "days_since_last_transaction": 7,
      "balance_change_30d": 0.16,
      "transaction_change_30d": 1.8041,
      "card_spend_change_30d": -12.8957,
      "app_login_change_30d": 20.56,
      "salary_missing_days": 4.0,
      "external_transfer_change_30d": -34.9591,
      "upi_share_of_spend": 0.2631,
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
      "days_since_last_transaction": 2,
      "balance_change_30d": 0.2867,
      "transaction_change_30d": -9.4602,
      "card_spend_change_30d": -1.9441,
      "app_login_change_30d": 7.6059,
      "salary_missing_days": 3.0,
      "external_transfer_change_30d": -8.0647,
      "upi_share_of_spend": 0.2933,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 15.953,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-06-01",
      "days_since_last_transaction": 8,
      "balance_change_30d": 1.6759,
      "transaction_change_30d": -14.9466,
      "card_spend_change_30d": -10.6028,
      "app_login_change_30d": -19.516,
      "salary_missing_days": 3.0,
      "external_transfer_change_30d": 30.9548,
      "upi_share_of_spend": 0.349,
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
    "tenure_months": 166,
    "customer_segment": "pension",
    "income_regularity": "regular",
    "products_count": 1,
    "has_credit_card": 0,
    "has_loan": 0,
    "days_since_last_transaction": 8,
    "balance_change_30d": 1.6759,
    "transaction_change_30d": -14.9466,
    "card_spend_change_30d": -10.6028,
    "app_login_change_30d": -19.516,
    "salary_missing_days": 3.0,
    "external_transfer_change_30d": 30.9548,
    "upi_share_of_spend": 0.349,
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
      "tenure_months": 166,
      "age": 72,
      "customer_yearly_value": 14897.1195,
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
    "served_at": "2026-08-31T01:53:53",
    "elapsed_ms": 4631.28,
    "timings_ms": {
      "model1": 149.09,
      "model2": 4481.98
    },
    "customer_id": "C12665",
    "customer_name": "Raksha Dey",
    "snapshot_date": "2026-06-01"
  },
  "model1": {
    "churn_probability": 3.62,
    "raw_churn_probability": 31.55,
    "probability_mode": "sigmoid",
    "risk_score": 10.87,
    "churn_prediction": "No",
    "risk_level": "Low",
    "top_risk_factors": [
      {
        "factor": "latest_salary_missing_days",
        "value": 3.0,
        "message": "Salary or pension was delayed recently.",
        "contribution": 0.20721739530563354
      },
      {
        "factor": "latest_vs_avg_upi_share_of_spend_available_history",
        "value": 0.07445000000000002,
        "message": "A larger share of spending is happening through UPI.",
        "contribution": 0.19815953075885773
      },
      {
        "factor": "avg_card_spend_change_30d_6m",
        "value": -17.418000000000003,
        "message": "Card spending has been falling across recent months.",
        "contribution": 0.037229135632514954
      },
      {
        "factor": "card_spend_change_30d_trend_6m",
        "value": 5.174268571428569,
        "message": "This signal increased churn risk.",
        "contribution": 0.036768920719623566
      },
      {
        "factor": "latest_app_login_change_30d",
        "value": -19.516,
        "message": "App usage has been falling across recent months.",
        "contribution": 0.02235383354127407
      }
    ]
  },
  "model2_input": {
    "customer_context": {
      "age": 72,
      "tenure_months": 166,
      "customer_segment": "pension",
      "income_regularity": "regular",
      "customer_yearly_value": 14897.1195,
      "products_count": 1,
      "has_credit_card": 0,
      "has_loan": 0
    },
    "behavior": {
      "days_since_last_transaction": 8,
      "balance_change_30d": 1.6759,
      "transaction_change_30d": -14.9466,
      "card_spend_change_30d": -10.6028,
      "app_login_change_30d": -19.516,
      "salary_missing_days": 3,
      "external_transfer_change_30d": 30.9548,
      "upi_share_of_spend": 0.349,
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
      "churn_probability": 0.0362,
      "churn_prediction": "No",
      "risk_level": "Low",
      "top_risk_factors": [
        {
          "factor": "salary_missing_days",
          "value": 3
        },
        {
          "factor": "upi_share_of_spend",
          "value": 0.349
        },
        {
          "factor": "card_spend_change_30d",
          "value": -10.6028
        }
      ]
    },
    "eligible_actions": [
      "FINANCIAL_GUIDANCE",
      "PRODUCT_REVIEW",
      "MONITOR"
    ],
    "case_id": "C12665"
  },
  "model2": {
    "case_id": "C12665",
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
    "raw_text": "{\"evidence\":[\"complaints_30d=0\",\"unresolved_complaints=0\",\"avg_resolution_time_hrs=0.0\"],\"primary_reason\":\"UNKNOWN\",\"reasoning_summary\":\"Complaint and resolution signals are mixed or weak; evidence is genuinely ambiguous.\",\"recommended_action\":\"MONITOR\",\"secondary_reasons\":[],\"urgency\":\"LOW\"}",
    "error": null,
    "latency_s": 4.4817,
    "simple_output": "Reason: UNKNOWN | Urgency: LOW | Action: MONITOR | Why: Complaint and resolution signals are mixed or weak; evidence is genuinely unclear."
  }
}
```

### Varenya Chander (`C13013`)

- OK: `True`
- Shape errors: `[]`
- Simple output: Reason: UNKNOWN | Urgency: LOW | Action: MONITOR | Why: Complaint and resolution signals are mixed or weak; relationship strength is uncertain.

Request:

```json
{
  "customer_id": "C13013",
  "customer_name": "Varenya Chander",
  "prediction_date": "2026-06-01",
  "snapshot_date": "2026-06-01",
  "target_month": "2026-07-01",
  "profile": {
    "tenure_months": 90,
    "customer_segment": "business",
    "income_regularity": "irregular",
    "products_count": 1,
    "has_credit_card": 0,
    "has_loan": 0
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 9,
      "balance_change_30d": -6.0666,
      "transaction_change_30d": -24.4708,
      "card_spend_change_30d": -10.2432,
      "app_login_change_30d": -35.0922,
      "salary_missing_days": null,
      "external_transfer_change_30d": 18.5707,
      "upi_share_of_spend": 0.6023,
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
      "days_since_last_transaction": 7,
      "balance_change_30d": 10.9348,
      "transaction_change_30d": 6.6455,
      "card_spend_change_30d": 1.0044,
      "app_login_change_30d": 7.1891,
      "salary_missing_days": null,
      "external_transfer_change_30d": -31.0226,
      "upi_share_of_spend": 0.6349,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 10.4821,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-03-01",
      "days_since_last_transaction": 5,
      "balance_change_30d": -11.6246,
      "transaction_change_30d": 23.2285,
      "card_spend_change_30d": 28.5776,
      "app_login_change_30d": 7.1385,
      "salary_missing_days": null,
      "external_transfer_change_30d": -9.7325,
      "upi_share_of_spend": 0.6323,
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
      "balance_change_30d": 3.9842,
      "transaction_change_30d": -8.626,
      "card_spend_change_30d": -10.6113,
      "app_login_change_30d": -10.0874,
      "salary_missing_days": null,
      "external_transfer_change_30d": 2.0216,
      "upi_share_of_spend": 0.6311,
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
      "days_since_last_transaction": 8,
      "balance_change_30d": 11.1454,
      "transaction_change_30d": -13.5106,
      "card_spend_change_30d": -11.0321,
      "app_login_change_30d": -2.856,
      "salary_missing_days": null,
      "external_transfer_change_30d": 13.9739,
      "upi_share_of_spend": 0.6161,
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
      "days_since_last_transaction": 10,
      "balance_change_30d": -9.5142,
      "transaction_change_30d": 4.3272,
      "card_spend_change_30d": 15.3837,
      "app_login_change_30d": 13.9864,
      "salary_missing_days": null,
      "external_transfer_change_30d": 10.2695,
      "upi_share_of_spend": 0.5622,
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
    "tenure_months": 90,
    "customer_segment": "business",
    "income_regularity": "irregular",
    "products_count": 1,
    "has_credit_card": 0,
    "has_loan": 0,
    "days_since_last_transaction": 10,
    "balance_change_30d": -9.5142,
    "transaction_change_30d": 4.3272,
    "card_spend_change_30d": 15.3837,
    "app_login_change_30d": 13.9864,
    "salary_missing_days": null,
    "external_transfer_change_30d": 10.2695,
    "upi_share_of_spend": 0.5622,
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
      "segment": "business",
      "income_regularity": "irregular",
      "tenure_months": 90,
      "age": 53,
      "customer_yearly_value": 60124.1501,
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
  "meta": {
    "endpoint": "/predict/both",
    "served_at": "2026-08-31T01:53:58",
    "elapsed_ms": 4969.12,
    "timings_ms": {
      "model1": 62.87,
      "model2": 4906.11
    },
    "customer_id": "C13013",
    "customer_name": "Varenya Chander",
    "snapshot_date": "2026-06-01"
  },
  "model1": {
    "churn_probability": 2.57,
    "raw_churn_probability": 23.93,
    "probability_mode": "sigmoid",
    "risk_score": 7.7,
    "churn_prediction": "No",
    "risk_level": "Low",
    "top_risk_factors": [
      {
        "factor": "external_transfer_change_30d_trend_6m",
        "value": 3.006788571428572,
        "message": "External transfers have increased.",
        "contribution": 0.035891275852918625
      },
      {
        "factor": "latest_upi_share_of_spend",
        "value": 0.5622,
        "message": "A larger share of spending is happening through UPI.",
        "contribution": 0.03067750297486782
      },
      {
        "factor": "max_days_since_last_transaction_3m",
        "value": 10.0,
        "message": "Customer has gone longer without transacting.",
        "contribution": 0.013279810547828674
      },
      {
        "factor": "count_external_transfer_rise_6m",
        "value": 0,
        "message": "This signal increased churn risk.",
        "contribution": 0.010658547282218933
      },
      {
        "factor": "latest_vs_avg_balance_change_30d_available_history",
        "value": -9.324033333333334,
        "message": "Balance has been falling across recent months.",
        "contribution": 0.010611925274133682
      }
    ]
  },
  "model2_input": {
    "customer_context": {
      "age": 53,
      "tenure_months": 90,
      "customer_segment": "business",
      "income_regularity": "irregular",
      "customer_yearly_value": 60124.1501,
      "products_count": 1,
      "has_credit_card": 0,
      "has_loan": 0
    },
    "behavior": {
      "days_since_last_transaction": 10,
      "balance_change_30d": -9.5142,
      "transaction_change_30d": 4.3272,
      "card_spend_change_30d": 15.3837,
      "app_login_change_30d": 13.9864,
      "salary_missing_days": null,
      "external_transfer_change_30d": 10.2695,
      "upi_share_of_spend": 0.5622,
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
      "churn_probability": 0.0257,
      "churn_prediction": "No",
      "risk_level": "Low",
      "top_risk_factors": [
        {
          "factor": "external_transfer_change_30d",
          "value": 10.2695
        },
        {
          "factor": "upi_share_of_spend",
          "value": 0.5622
        },
        {
          "factor": "days_since_last_transaction",
          "value": 10
        }
      ]
    },
    "eligible_actions": [
      "RE_ENGAGEMENT",
      "PRODUCT_REVIEW",
      "MONITOR"
    ],
    "case_id": "C13013"
  },
  "model2": {
    "case_id": "C13013",
    "ok": true,
    "prediction": {
      "evidence": [
        "complaints_30d=0",
        "unresolved_complaints=0",
        "avg_resolution_time_hrs=0.0"
      ],
      "primary_reason": "UNKNOWN",
      "reasoning_summary": "Complaint and resolution signals are mixed or weak; relationship strength is uncertain.",
      "recommended_action": "MONITOR",
      "secondary_reasons": [],
      "urgency": "LOW"
    },
    "warnings": [
      "evidence: 'complaints_30d=0' cites a zero/null value, which is not evidence; remove it",
      "evidence: 'unresolved_complaints=0' cites a zero/null value, which is not evidence; remove it",
      "evidence: 'avg_resolution_time_hrs=0.0' cites a zero/null value, which is not evidence; remove it"
    ],
    "raw_text": "{\"evidence\":[\"products_dropped_90d=0\",\"complaints_30d=0\",\"external_transfer_change_30d=10.3\"],\"primary_reason\":\"PRODUCT_MISMATCH\",\"reasoning_summary\":\"The relationship looks out of alignment because products_dropped_90d=0 and complaint_text is null.\",\"recommended_action\":\"PRODUCT_REVIEW\",\"secondary_reasons\":[],\"urgency\":\"MEDIUM\"}",
    "error": null,
    "latency_s": 4.906,
    "simple_output": "Reason: UNKNOWN | Urgency: LOW | Action: MONITOR | Why: Complaint and resolution signals are mixed or weak; relationship strength is uncertain."
  }
}
```

### Ikbal Rama (`C13510`)

- OK: `True`
- Shape errors: `[]`
- Simple output: Reason: SERVICE_DISSATISFACTION | Urgency: MEDIUM | Action: COMPLAINT_ESCALATION | Why: Complaint escalation because complaints_30d=2 and unresolved_complaints=1 suggest SERVICE_DISSATISFACTION=SERVICE_ESCALATION.

Request:

```json
{
  "customer_id": "C13510",
  "customer_name": "Ikbal Rama",
  "prediction_date": "2026-06-01",
  "snapshot_date": "2026-06-01",
  "target_month": "2026-07-01",
  "profile": {
    "tenure_months": 68,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 1,
    "has_credit_card": 0,
    "has_loan": 0
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 1,
      "balance_change_30d": 12.544,
      "transaction_change_30d": 6.3971,
      "card_spend_change_30d": -0.1334,
      "app_login_change_30d": 16.8939,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": 19.2787,
      "upi_share_of_spend": 0.403,
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
      "days_since_last_transaction": 4,
      "balance_change_30d": -11.2776,
      "transaction_change_30d": -18.0183,
      "card_spend_change_30d": 12.992,
      "app_login_change_30d": -9.5316,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -3.4836,
      "upi_share_of_spend": 0.4231,
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
      "days_since_last_transaction": 6,
      "balance_change_30d": -13.7188,
      "transaction_change_30d": 10.1638,
      "card_spend_change_30d": -25.1624,
      "app_login_change_30d": -13.0612,
      "salary_missing_days": 1.0,
      "external_transfer_change_30d": -15.4171,
      "upi_share_of_spend": 0.4754,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 0,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 3,
      "avg_resolution_time_hrs": 0.0,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-04-01",
      "days_since_last_transaction": 2,
      "balance_change_30d": -3.8353,
      "transaction_change_30d": -2.7697,
      "card_spend_change_30d": 11.373,
      "app_login_change_30d": 5.3909,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": 6.8562,
      "upi_share_of_spend": 0.3163,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 13.4256,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-05-01",
      "days_since_last_transaction": 2,
      "balance_change_30d": 11.5165,
      "transaction_change_30d": 11.5043,
      "card_spend_change_30d": 7.2089,
      "app_login_change_30d": 32.7434,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -11.912,
      "upi_share_of_spend": 0.3091,
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
      "days_since_last_transaction": 2,
      "balance_change_30d": 22.9811,
      "transaction_change_30d": 34.1051,
      "card_spend_change_30d": 26.5783,
      "app_login_change_30d": 16.7457,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -10.1805,
      "upi_share_of_spend": 0.3232,
      "fd_maturing_in_30d": 1,
      "products_dropped_90d": 0,
      "complaints_30d": 2,
      "unresolved_complaints": 1,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 27.284,
      "emi_bounce_30d": 0
    }
  ],
  "customer": {
    "tenure_months": 68,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 1,
    "has_credit_card": 0,
    "has_loan": 0,
    "days_since_last_transaction": 2,
    "balance_change_30d": 22.9811,
    "transaction_change_30d": 34.1051,
    "card_spend_change_30d": 26.5783,
    "app_login_change_30d": 16.7457,
    "salary_missing_days": 0.0,
    "external_transfer_change_30d": -10.1805,
    "upi_share_of_spend": 0.3232,
    "fd_maturing_in_30d": 1,
    "products_dropped_90d": 0,
    "complaints_30d": 2,
    "unresolved_complaints": 1,
    "failed_transactions_30d": 0,
    "avg_resolution_time_hrs": 27.284,
    "emi_bounce_30d": 0
  },
  "extra_context": {
    "customer_profile": {
      "segment": "salary",
      "income_regularity": "regular",
      "tenure_months": 68,
      "age": 44,
      "customer_yearly_value": 48863.9795,
      "products_count": 1,
      "has_credit_card": 0,
      "has_loan": 0,
      "value_tier": "medium"
    },
    "recent_complaint_text": "Customer angry about EMI bounce charge. Says balance was sufficient."
  }
}
```

Response:

```json
{
  "meta": {
    "endpoint": "/predict/both",
    "served_at": "2026-08-31T01:54:00",
    "elapsed_ms": 2398.21,
    "timings_ms": {
      "model1": 80.17,
      "model2": 2317.84
    },
    "customer_id": "C13510",
    "customer_name": "Ikbal Rama",
    "snapshot_date": "2026-06-01"
  },
  "model1": {
    "churn_probability": 3.22,
    "raw_churn_probability": 28.92,
    "probability_mode": "sigmoid",
    "risk_score": 9.65,
    "churn_prediction": "No",
    "risk_level": "Low",
    "top_risk_factors": [
      {
        "factor": "latest_fd_maturing_in_30d",
        "value": 1,
        "message": "Customer has a fixed deposit maturing soon.",
        "contribution": 0.22217197716236115
      },
      {
        "factor": "latest_avg_resolution_time_hrs",
        "value": 27.284,
        "message": "Recent complaints took longer to resolve.",
        "contribution": 0.16052469611167908
      },
      {
        "factor": "sum_fd_maturing_in_30d_3m",
        "value": 1.0,
        "message": "Customer has a fixed deposit maturing soon.",
        "contribution": 0.10477137565612793
      },
      {
        "factor": "count_external_transfer_rise_6m",
        "value": 0,
        "message": "This signal increased churn risk.",
        "contribution": 0.016850756481289864
      },
      {
        "factor": "latest_vs_avg_app_login_change_30d_available_history",
        "value": 8.54885,
        "message": "This signal increased churn risk.",
        "contribution": 0.01603507436811924
      }
    ]
  },
  "model2_input": {
    "customer_context": {
      "age": 44,
      "tenure_months": 68,
      "customer_segment": "salary",
      "income_regularity": "regular",
      "customer_yearly_value": 48863.9795,
      "products_count": 1,
      "has_credit_card": 0,
      "has_loan": 0
    },
    "behavior": {
      "days_since_last_transaction": 2,
      "balance_change_30d": 22.9811,
      "transaction_change_30d": 34.1051,
      "card_spend_change_30d": 26.5783,
      "app_login_change_30d": 16.7457,
      "salary_missing_days": 0,
      "external_transfer_change_30d": -10.1805,
      "upi_share_of_spend": 0.3232,
      "fd_maturing_in_30d": 1,
      "products_dropped_90d": 0,
      "emi_bounce_30d": 0
    },
    "service_evidence": {
      "complaints_30d": 2,
      "unresolved_complaints": 1,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 27.284,
      "complaint_text": "Customer angry about EMI bounce charge. Says balance was sufficient."
    },
    "model1": {
      "churn_probability": 0.0322,
      "churn_prediction": "No",
      "risk_level": "Low",
      "top_risk_factors": [
        {
          "factor": "fd_maturing_in_30d",
          "value": 1
        },
        {
          "factor": "app_login_change_30d",
          "value": 16.7457
        },
        {
          "factor": "transaction_change_30d",
          "value": 34.1051
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
    "case_id": "C13510"
  },
  "model2": {
    "case_id": "C13510",
    "ok": true,
    "prediction": {
      "evidence": [
        "complaints_30d=2",
        "unresolved_complaints=1",
        "avg_resolution_time_hrs=27.3"
      ],
      "primary_reason": "SERVICE_DISSATISFACTION",
      "reasoning_summary": "Complaint escalation because complaints_30d=2 and unresolved_complaints=1 suggest SERVICE_DISSATISFACTION=SERVICE_ESCALATION.",
      "recommended_action": "COMPLAINT_ESCALATION",
      "secondary_reasons": [],
      "urgency": "MEDIUM"
    },
    "warnings": [],
    "raw_text": "{\n    \"evidence\": [\n        \"complaints_30d=2\",\n        \"unresolved_complaints=1\",\n        \"avg_resolution_time_hrs=27.3\"\n    ],\n    \"primary_reason\": \"SERVICE_DISSATISFACTION\",\n    \"reasoning_summary\": \"Complaint escalation because complaints_30d=2 and unresolved_complaints=1 suggest SERVICE_DISSATISFACTION=SERVICE_ESCALATION.\",\n    \"recommended_action\": \"COMPLAINT_ESCALATION\",\n    \"secondary_reasons\": [],\n    \"urgency\": \"MEDIUM\"\n}",
    "error": null,
    "latency_s": 2.3177,
    "simple_output": "Reason: SERVICE_DISSATISFACTION | Urgency: MEDIUM | Action: COMPLAINT_ESCALATION | Why: Complaint escalation because complaints_30d=2 and unresolved_complaints=1 suggest SERVICE_DISSATISFACTION=SERVICE_ESCALATION."
  }
}
```

### Brijesh Grover (`C15116`)

- OK: `True`
- Shape errors: `[]`
- Simple output: Reason: SERVICE_DISSATISFACTION | Urgency: MEDIUM | Action: COMPLAINT_ESCALATION | Why: Complaint escalation because complaints_30d=6 and unresolved_complaints=5 show the issue is unresolved or operationally serious.

Request:

```json
{
  "customer_id": "C15116",
  "customer_name": "Brijesh Grover",
  "prediction_date": "2026-02-01",
  "snapshot_date": "2026-02-01",
  "target_month": "2026-03-01",
  "profile": {
    "tenure_months": 93,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 2,
    "has_credit_card": 1,
    "has_loan": 0
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 0,
      "balance_change_30d": 31.1463,
      "transaction_change_30d": 23.4068,
      "card_spend_change_30d": 56.2642,
      "app_login_change_30d": 29.9602,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -28.7998,
      "upi_share_of_spend": 0.326,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 27.9026,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-02-01",
      "days_since_last_transaction": 2,
      "balance_change_30d": 34.5163,
      "transaction_change_30d": 19.7712,
      "card_spend_change_30d": 40.0932,
      "app_login_change_30d": 45.2845,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -24.4496,
      "upi_share_of_spend": 0.3708,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 6,
      "unresolved_complaints": 5,
      "failed_transactions_30d": 7,
      "avg_resolution_time_hrs": 110.397,
      "emi_bounce_30d": 0
    }
  ],
  "customer": {
    "tenure_months": 93,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 2,
    "has_credit_card": 1,
    "has_loan": 0,
    "days_since_last_transaction": 2,
    "balance_change_30d": 34.5163,
    "transaction_change_30d": 19.7712,
    "card_spend_change_30d": 40.0932,
    "app_login_change_30d": 45.2845,
    "salary_missing_days": 0.0,
    "external_transfer_change_30d": -24.4496,
    "upi_share_of_spend": 0.3708,
    "fd_maturing_in_30d": 0,
    "products_dropped_90d": 0,
    "complaints_30d": 6,
    "unresolved_complaints": 5,
    "failed_transactions_30d": 7,
    "avg_resolution_time_hrs": 110.397,
    "emi_bounce_30d": 0
  },
  "extra_context": {
    "customer_profile": {
      "segment": "salary",
      "income_regularity": "regular",
      "tenure_months": 93,
      "age": 42,
      "customer_yearly_value": 34383.0487,
      "products_count": 2,
      "has_credit_card": 1,
      "has_loan": 0,
      "value_tier": "low"
    },
    "recent_complaint_text": "Cash trapped in the machine shutter. Guard said complain to bank."
  }
}
```

Response:

```json
{
  "meta": {
    "endpoint": "/predict/both",
    "served_at": "2026-08-31T01:54:03",
    "elapsed_ms": 2474.99,
    "timings_ms": {
      "model1": 72.01,
      "model2": 2402.83
    },
    "customer_id": "C15116",
    "customer_name": "Brijesh Grover",
    "snapshot_date": "2026-02-01"
  },
  "model1": {
    "churn_probability": 20.84,
    "raw_churn_probability": 73.35,
    "probability_mode": "sigmoid",
    "risk_score": 70.31,
    "churn_prediction": "Yes",
    "risk_level": "Medium",
    "top_risk_factors": [
      {
        "factor": "max_avg_resolution_time_hrs_3m",
        "value": 110.397,
        "message": "Recent complaints took longer to resolve.",
        "contribution": 0.5651076436042786
      },
      {
        "factor": "latest_avg_resolution_time_hrs",
        "value": 110.397,
        "message": "Recent complaints took longer to resolve.",
        "contribution": 0.2916426956653595
      },
      {
        "factor": "avg_balance_change_30d_6m",
        "value": 32.8313,
        "message": "This signal increased churn risk.",
        "contribution": 0.24745027720928192
      },
      {
        "factor": "sum_failed_transactions_30d_3m",
        "value": 7.0,
        "message": "Customer has recent failed transactions.",
        "contribution": 0.242184117436409
      },
      {
        "factor": "latest_failed_transactions_30d",
        "value": 7,
        "message": "Customer has recent failed transactions.",
        "contribution": 0.15356291830539703
      }
    ]
  },
  "model2_input": {
    "customer_context": {
      "age": 42,
      "tenure_months": 93,
      "customer_segment": "salary",
      "income_regularity": "regular",
      "customer_yearly_value": 34383.0487,
      "products_count": 2,
      "has_credit_card": 1,
      "has_loan": 0
    },
    "behavior": {
      "days_since_last_transaction": 2,
      "balance_change_30d": 34.5163,
      "transaction_change_30d": 19.7712,
      "card_spend_change_30d": 40.0932,
      "app_login_change_30d": 45.2845,
      "salary_missing_days": 0,
      "external_transfer_change_30d": -24.4496,
      "upi_share_of_spend": 0.3708,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "emi_bounce_30d": 0
    },
    "service_evidence": {
      "complaints_30d": 6,
      "unresolved_complaints": 5,
      "failed_transactions_30d": 7,
      "avg_resolution_time_hrs": 110.397,
      "complaint_text": "Cash trapped in the machine shutter. Guard said complain to bank."
    },
    "model1": {
      "churn_probability": 0.2084,
      "churn_prediction": "Yes",
      "risk_level": "Medium",
      "top_risk_factors": [
        {
          "factor": "balance_change_30d",
          "value": 34.5163
        },
        {
          "factor": "failed_transactions_30d",
          "value": 7
        },
        {
          "factor": "app_login_change_30d",
          "value": 45.2845
        }
      ]
    },
    "eligible_actions": [
      "COMPLAINT_ESCALATION",
      "SERVICE_RECOVERY",
      "RM_CALLBACK",
      "MONITOR"
    ],
    "case_id": "C15116"
  },
  "model2": {
    "case_id": "C15116",
    "ok": true,
    "prediction": {
      "evidence": [
        "complaints_30d=6",
        "unresolved_complaints=5",
        "avg_resolution_time_hrs=110.4",
        "complaint_text describes a recent service issue"
      ],
      "primary_reason": "SERVICE_DISSATISFACTION",
      "reasoning_summary": "Complaint escalation because complaints_30d=6 and unresolved_complaints=5 show the issue is unresolved or operationally serious.",
      "recommended_action": "COMPLAINT_ESCALATION",
      "secondary_reasons": [],
      "urgency": "MEDIUM"
    },
    "warnings": [],
    "raw_text": "{\n    \"evidence\": [\n        \"complaints_30d=6\",\n        \"unresolved_complaints=5\",\n        \"avg_resolution_time_hrs=110.4\",\n        \"complaint_text describes a recent service issue\"\n    ],\n    \"primary_reason\": \"SERVICE_DISSATISFACTION\",\n    \"reasoning_summary\": \"Complaint escalation because complaints_30d=6 and unresolved_complaints=5 show the issue is unresolved or operationally serious.\",\n    \"recommended_action\": \"COMPLAINT_ESCALATION\",\n    \"secondary_reasons\": [],\n    \"urgency\": \"MEDIUM\"\n}",
    "error": null,
    "latency_s": 2.4026,
    "simple_output": "Reason: SERVICE_DISSATISFACTION | Urgency: MEDIUM | Action: COMPLAINT_ESCALATION | Why: Complaint escalation because complaints_30d=6 and unresolved_complaints=5 show the issue is unresolved or operationally serious."
  }
}
```

### Kashish Sunder (`C15803`)

- OK: `True`
- Shape errors: `[]`
- Simple output: Reason: SERVICE_DISSATISFACTION | Urgency: MEDIUM | Action: SERVICE_RECOVERY | Why: Complaint escalation because complaints_30d=1 and avg_resolution_time_hrs=21.2 suggest a service problem.

Request:

```json
{
  "customer_id": "C15803",
  "customer_name": "Kashish Sunder",
  "prediction_date": "2026-06-01",
  "snapshot_date": "2026-06-01",
  "target_month": "2026-07-01",
  "profile": {
    "tenure_months": 114,
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
      "balance_change_30d": 15.9664,
      "transaction_change_30d": 8.25,
      "card_spend_change_30d": 13.8868,
      "app_login_change_30d": 30.2993,
      "salary_missing_days": 1.0,
      "external_transfer_change_30d": -41.5553,
      "upi_share_of_spend": 0.3294,
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
      "days_since_last_transaction": 7,
      "balance_change_30d": 4.8476,
      "transaction_change_30d": -0.9515,
      "card_spend_change_30d": -22.7319,
      "app_login_change_30d": 1.0911,
      "salary_missing_days": 4.0,
      "external_transfer_change_30d": 2.9342,
      "upi_share_of_spend": 0.402,
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
      "days_since_last_transaction": 7,
      "balance_change_30d": -5.7422,
      "transaction_change_30d": 6.3629,
      "card_spend_change_30d": 22.2564,
      "app_login_change_30d": -25.4282,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": 23.2142,
      "upi_share_of_spend": 0.3533,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 28.4239,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-04-01",
      "days_since_last_transaction": 5,
      "balance_change_30d": 4.2623,
      "transaction_change_30d": 27.451,
      "card_spend_change_30d": 15.9073,
      "app_login_change_30d": 9.8395,
      "salary_missing_days": 1.0,
      "external_transfer_change_30d": 17.2158,
      "upi_share_of_spend": 0.3463,
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
      "balance_change_30d": 0.4428,
      "transaction_change_30d": -9.7366,
      "card_spend_change_30d": -16.3618,
      "app_login_change_30d": 9.1938,
      "salary_missing_days": 2.0,
      "external_transfer_change_30d": -18.7535,
      "upi_share_of_spend": 0.2696,
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
      "days_since_last_transaction": 6,
      "balance_change_30d": 11.2302,
      "transaction_change_30d": 11.3952,
      "card_spend_change_30d": 3.856,
      "app_login_change_30d": 11.4416,
      "salary_missing_days": 2.0,
      "external_transfer_change_30d": -15.3645,
      "upi_share_of_spend": 0.3495,
      "fd_maturing_in_30d": 1,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 21.2286,
      "emi_bounce_30d": 0
    }
  ],
  "customer": {
    "tenure_months": 114,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 2,
    "has_credit_card": 1,
    "has_loan": 0,
    "days_since_last_transaction": 6,
    "balance_change_30d": 11.2302,
    "transaction_change_30d": 11.3952,
    "card_spend_change_30d": 3.856,
    "app_login_change_30d": 11.4416,
    "salary_missing_days": 2.0,
    "external_transfer_change_30d": -15.3645,
    "upi_share_of_spend": 0.3495,
    "fd_maturing_in_30d": 1,
    "products_dropped_90d": 0,
    "complaints_30d": 1,
    "unresolved_complaints": 0,
    "failed_transactions_30d": 0,
    "avg_resolution_time_hrs": 21.2286,
    "emi_bounce_30d": 0
  },
  "extra_context": {
    "customer_profile": {
      "segment": "salary",
      "income_regularity": "regular",
      "tenure_months": 114,
      "age": 35,
      "customer_yearly_value": 39818.9495,
      "products_count": 2,
      "has_credit_card": 1,
      "has_loan": 0,
      "value_tier": "medium"
    },
    "recent_complaint_text": "KYC update took four visits. Every time a new document was demanded."
  }
}
```

Response:

```json
{
  "meta": {
    "endpoint": "/predict/both",
    "served_at": "2026-08-31T01:54:09",
    "elapsed_ms": 5553.77,
    "timings_ms": {
      "model1": 79.61,
      "model2": 5474.0
    },
    "customer_id": "C15803",
    "customer_name": "Kashish Sunder",
    "snapshot_date": "2026-06-01"
  },
  "model1": {
    "churn_probability": 4.41,
    "raw_churn_probability": 35.96,
    "probability_mode": "sigmoid",
    "risk_score": 13.24,
    "churn_prediction": "No",
    "risk_level": "Low",
    "top_risk_factors": [
      {
        "factor": "latest_fd_maturing_in_30d",
        "value": 1,
        "message": "Customer has a fixed deposit maturing soon.",
        "contribution": 0.21845704317092896
      },
      {
        "factor": "sum_fd_maturing_in_30d_3m",
        "value": 1.0,
        "message": "Customer has a fixed deposit maturing soon.",
        "contribution": 0.10144590586423874
      },
      {
        "factor": "latest_salary_missing_days",
        "value": 2.0,
        "message": "Salary or pension was delayed recently.",
        "contribution": 0.05818580463528633
      },
      {
        "factor": "external_transfer_change_30d_trend_6m",
        "value": 1.7112142857142842,
        "message": "External transfers have increased.",
        "contribution": 0.023362867534160614
      },
      {
        "factor": "latest_vs_avg_upi_share_of_spend_available_history",
        "value": 0.007816666666666638,
        "message": "A larger share of spending is happening through UPI.",
        "contribution": 0.02125186286866665
      }
    ]
  },
  "model2_input": {
    "customer_context": {
      "age": 35,
      "tenure_months": 114,
      "customer_segment": "salary",
      "income_regularity": "regular",
      "customer_yearly_value": 39818.9495,
      "products_count": 2,
      "has_credit_card": 1,
      "has_loan": 0
    },
    "behavior": {
      "days_since_last_transaction": 6,
      "balance_change_30d": 11.2302,
      "transaction_change_30d": 11.3952,
      "card_spend_change_30d": 3.856,
      "app_login_change_30d": 11.4416,
      "salary_missing_days": 2,
      "external_transfer_change_30d": -15.3645,
      "upi_share_of_spend": 0.3495,
      "fd_maturing_in_30d": 1,
      "products_dropped_90d": 0,
      "emi_bounce_30d": 0
    },
    "service_evidence": {
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 21.2286,
      "complaint_text": "KYC update took four visits. Every time a new document was demanded."
    },
    "model1": {
      "churn_probability": 0.0441,
      "churn_prediction": "No",
      "risk_level": "Low",
      "top_risk_factors": [
        {
          "factor": "fd_maturing_in_30d",
          "value": 1
        },
        {
          "factor": "salary_missing_days",
          "value": 2
        },
        {
          "factor": "external_transfer_change_30d",
          "value": -15.3645
        }
      ]
    },
    "eligible_actions": [
      "FINANCIAL_GUIDANCE",
      "SERVICE_RECOVERY",
      "PRODUCT_REVIEW",
      "MONITOR"
    ],
    "case_id": "C15803"
  },
  "model2": {
    "case_id": "C15803",
    "ok": true,
    "prediction": {
      "evidence": [
        "complaints_30d=1",
        "unresolved_complaints=0",
        "avg_resolution_time_hrs=21.2",
        "complaint_text describes a recent service issue"
      ],
      "primary_reason": "SERVICE_DISSATISFACTION",
      "reasoning_summary": "Complaint escalation because complaints_30d=1 and avg_resolution_time_hrs=21.2 suggest a service problem.",
      "recommended_action": "SERVICE_RECOVERY",
      "secondary_reasons": [],
      "urgency": "MEDIUM"
    },
    "warnings": [
      "evidence: 'unresolved_complaints=0' cites a zero/null value, which is not evidence; remove it",
      "reasoning_summary: describes COMPLAINT_ESCALATION but recommended_action is SERVICE_RECOVERY; rewrite the summary around the action you chose"
    ],
    "raw_text": "{\"evidence\":[\"complaints_30d=1\",\"unresolved_complaints=0\",\"avg_resolution_time_hrs=21.2\",\"complaint_text describes a recent service issue without clear escalation-level details\"],\"primary_reason\":\"SERVICE_DISSATISFACTION\",\"reasoning_summary\":\"Complaint evidence suggests SERVICE_DISSATISFACTION without clear escalation-level concern. Evidence suggests this because complaints_30d=1; avg_resolution_time_hrs=21.2.\",\"recommended_action\":\"SERVICE_RECOVERY\",\"secondary_reasons\":[],\"urgency\":\"MEDIUM\"}",
    "error": null,
    "latency_s": 5.4739,
    "simple_output": "Reason: SERVICE_DISSATISFACTION | Urgency: MEDIUM | Action: SERVICE_RECOVERY | Why: Complaint escalation because complaints_30d=1 and avg_resolution_time_hrs=21.2 suggest a service problem."
  }
}
```

### Chakradev Dube (`C15841`)

- OK: `True`
- Shape errors: `[]`
- Simple output: Reason: UNKNOWN | Urgency: LOW | Action: MONITOR | Why: Complaint and resolution signals are mixed or weak; no clear reason stands out.

Request:

```json
{
  "customer_id": "C15841",
  "customer_name": "Chakradev Dube",
  "prediction_date": "2026-06-01",
  "snapshot_date": "2026-06-01",
  "target_month": "2026-07-01",
  "profile": {
    "tenure_months": 1,
    "customer_segment": "vendor",
    "income_regularity": "irregular",
    "products_count": 2,
    "has_credit_card": 1,
    "has_loan": 0
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 13,
      "balance_change_30d": 6.9781,
      "transaction_change_30d": 3.7612,
      "card_spend_change_30d": -0.5254,
      "app_login_change_30d": 29.2013,
      "salary_missing_days": null,
      "external_transfer_change_30d": 24.3968,
      "upi_share_of_spend": 0.133,
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
      "balance_change_30d": 1.9101,
      "transaction_change_30d": 17.377,
      "card_spend_change_30d": -6.3393,
      "app_login_change_30d": 8.898,
      "salary_missing_days": null,
      "external_transfer_change_30d": -20.8128,
      "upi_share_of_spend": 0.2267,
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
      "balance_change_30d": 13.3193,
      "transaction_change_30d": -7.4376,
      "card_spend_change_30d": -11.1052,
      "app_login_change_30d": 6.8394,
      "salary_missing_days": null,
      "external_transfer_change_30d": 33.9844,
      "upi_share_of_spend": 0.1419,
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
      "days_since_last_transaction": 11,
      "balance_change_30d": 17.5741,
      "transaction_change_30d": -0.5601,
      "card_spend_change_30d": 5.8089,
      "app_login_change_30d": 20.4113,
      "salary_missing_days": null,
      "external_transfer_change_30d": 11.2521,
      "upi_share_of_spend": 0.1268,
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
      "days_since_last_transaction": 17,
      "balance_change_30d": -12.9088,
      "transaction_change_30d": -28.0706,
      "card_spend_change_30d": -6.3804,
      "app_login_change_30d": -26.3251,
      "salary_missing_days": null,
      "external_transfer_change_30d": 59.2015,
      "upi_share_of_spend": 0.1885,
      "fd_maturing_in_30d": 1,
      "products_dropped_90d": 0,
      "complaints_30d": 0,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 2,
      "avg_resolution_time_hrs": 0.0,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-06-01",
      "days_since_last_transaction": 12,
      "balance_change_30d": 14.5935,
      "transaction_change_30d": -2.5736,
      "card_spend_change_30d": 26.5658,
      "app_login_change_30d": -5.9131,
      "salary_missing_days": null,
      "external_transfer_change_30d": 9.3625,
      "upi_share_of_spend": 0.1273,
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
    "tenure_months": 1,
    "customer_segment": "vendor",
    "income_regularity": "irregular",
    "products_count": 2,
    "has_credit_card": 1,
    "has_loan": 0,
    "days_since_last_transaction": 12,
    "balance_change_30d": 14.5935,
    "transaction_change_30d": -2.5736,
    "card_spend_change_30d": 26.5658,
    "app_login_change_30d": -5.9131,
    "salary_missing_days": null,
    "external_transfer_change_30d": 9.3625,
    "upi_share_of_spend": 0.1273,
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
      "segment": "vendor",
      "income_regularity": "irregular",
      "tenure_months": 1,
      "age": 51,
      "customer_yearly_value": 10788.8346,
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
    "served_at": "2026-08-31T01:54:13",
    "elapsed_ms": 4819.54,
    "timings_ms": {
      "model1": 71.39,
      "model2": 4747.99
    },
    "customer_id": "C15841",
    "customer_name": "Chakradev Dube",
    "snapshot_date": "2026-06-01"
  },
  "model1": {
    "churn_probability": 4.1,
    "raw_churn_probability": 34.3,
    "probability_mode": "sigmoid",
    "risk_score": 12.29,
    "churn_prediction": "No",
    "risk_level": "Low",
    "top_risk_factors": [
      {
        "factor": "sum_fd_maturing_in_30d_3m",
        "value": 1.0,
        "message": "Customer has a fixed deposit maturing soon.",
        "contribution": 0.04404938220977783
      },
      {
        "factor": "external_transfer_change_30d_trend_6m",
        "value": 4.0611171428571415,
        "message": "External transfers have increased.",
        "contribution": 0.030151382088661194
      },
      {
        "factor": "avg_upi_share_of_spend_6m",
        "value": 0.15736666666666668,
        "message": "A larger share of spending is happening through UPI.",
        "contribution": 0.024889543652534485
      },
      {
        "factor": "max_days_since_last_transaction_3m",
        "value": 17.0,
        "message": "Customer has gone longer without transacting.",
        "contribution": 0.017115717753767967
      },
      {
        "factor": "latest_upi_share_of_spend",
        "value": 0.1273,
        "message": "A larger share of spending is happening through UPI.",
        "contribution": 0.00974783580750227
      }
    ]
  },
  "model2_input": {
    "customer_context": {
      "age": 51,
      "tenure_months": 1,
      "customer_segment": "vendor",
      "income_regularity": "irregular",
      "customer_yearly_value": 10788.8346,
      "products_count": 2,
      "has_credit_card": 1,
      "has_loan": 0
    },
    "behavior": {
      "days_since_last_transaction": 12,
      "balance_change_30d": 14.5935,
      "transaction_change_30d": -2.5736,
      "card_spend_change_30d": 26.5658,
      "app_login_change_30d": -5.9131,
      "salary_missing_days": null,
      "external_transfer_change_30d": 9.3625,
      "upi_share_of_spend": 0.1273,
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
      "churn_probability": 0.041,
      "churn_prediction": "No",
      "risk_level": "Low",
      "top_risk_factors": [
        {
          "factor": "fd_maturing_in_30d",
          "value": 0
        },
        {
          "factor": "external_transfer_change_30d",
          "value": 9.3625
        },
        {
          "factor": "upi_share_of_spend",
          "value": 0.1273
        }
      ]
    },
    "eligible_actions": [
      "SERVICE_RECOVERY",
      "RE_ENGAGEMENT",
      "MONITOR"
    ],
    "case_id": "C15841"
  },
  "model2": {
    "case_id": "C15841",
    "ok": true,
    "prediction": {
      "evidence": [
        "complaints_30d=0",
        "unresolved_complaints=0",
        "avg_resolution_time_hrs=0.0"
      ],
      "primary_reason": "UNKNOWN",
      "reasoning_summary": "Complaint and resolution signals are mixed or weak; no clear reason stands out.",
      "recommended_action": "MONITOR",
      "secondary_reasons": [],
      "urgency": "LOW"
    },
    "warnings": [
      "evidence: 'complaints_30d=0' cites a zero/null value, which is not evidence; remove it",
      "evidence: 'unresolved_complaints=0' cites a zero/null value, which is not evidence; remove it",
      "evidence: 'avg_resolution_time_hrs=0.0' cites a zero/null value, which is not evidence; remove it"
    ],
    "raw_text": "{\"evidence\":[\"complaints_30d=0\",\"unresolved_complaints=0\",\"avg_resolution_time_hrs=0.0\"],\"primary_reason\":\"DIGITAL_FRICTION\",\"reasoning_summary\":\"Digital friction is the strongest supported signal here because complaints_30d=0 and unresolved_complaints=0 cite a mix of mixed or weak signals.\",\"recommended_action\":\"RE_ENGAGEMENT\",\"secondary_reasons\":[],\"urgency\":\"MEDIUM\"}",
    "error": null,
    "latency_s": 4.7479,
    "simple_output": "Reason: UNKNOWN | Urgency: LOW | Action: MONITOR | Why: Complaint and resolution signals are mixed or weak; no clear reason stands out."
  }
}
```

### Oscar Contractor (`C16195`)

- OK: `True`
- Shape errors: `[]`
- Simple output: Reason: SERVICE_DISSATISFACTION | Urgency: HIGH | Action: COMPLAINT_ESCALATION | Why: Complaint escalation because complaints_30d=5 and unresolved_complaints=2 show service friction.

Request:

```json
{
  "customer_id": "C16195",
  "customer_name": "Oscar Contractor",
  "prediction_date": "2026-04-01",
  "snapshot_date": "2026-04-01",
  "target_month": "2026-05-01",
  "profile": {
    "tenure_months": 81,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 4,
    "has_credit_card": 0,
    "has_loan": 1
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 10,
      "balance_change_30d": 6.491,
      "transaction_change_30d": -14.3384,
      "card_spend_change_30d": 8.8228,
      "app_login_change_30d": 20.8999,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -12.2504,
      "upi_share_of_spend": 0.2323,
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
      "days_since_last_transaction": 2,
      "balance_change_30d": -9.1873,
      "transaction_change_30d": -15.9171,
      "card_spend_change_30d": -24.2366,
      "app_login_change_30d": -18.1521,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -15.0967,
      "upi_share_of_spend": 0.3656,
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
      "balance_change_30d": 14.1207,
      "transaction_change_30d": -10.8871,
      "card_spend_change_30d": -26.2081,
      "app_login_change_30d": -20.2092,
      "salary_missing_days": 3.0,
      "external_transfer_change_30d": 44.5514,
      "upi_share_of_spend": 0.3868,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 15.8262,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-04-01",
      "days_since_last_transaction": 16,
      "balance_change_30d": -44.0438,
      "transaction_change_30d": -33.2669,
      "card_spend_change_30d": -63.0185,
      "app_login_change_30d": -57.3214,
      "salary_missing_days": 3.0,
      "external_transfer_change_30d": 89.1173,
      "upi_share_of_spend": 0.3704,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 5,
      "unresolved_complaints": 2,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 38.9291,
      "emi_bounce_30d": 1
    }
  ],
  "customer": {
    "tenure_months": 81,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 4,
    "has_credit_card": 0,
    "has_loan": 1,
    "days_since_last_transaction": 16,
    "balance_change_30d": -44.0438,
    "transaction_change_30d": -33.2669,
    "card_spend_change_30d": -63.0185,
    "app_login_change_30d": -57.3214,
    "salary_missing_days": 3.0,
    "external_transfer_change_30d": 89.1173,
    "upi_share_of_spend": 0.3704,
    "fd_maturing_in_30d": 0,
    "products_dropped_90d": 0,
    "complaints_30d": 5,
    "unresolved_complaints": 2,
    "failed_transactions_30d": 0,
    "avg_resolution_time_hrs": 38.9291,
    "emi_bounce_30d": 1
  },
  "extra_context": {
    "customer_profile": {
      "segment": "salary",
      "income_regularity": "regular",
      "tenure_months": 81,
      "age": 27,
      "customer_yearly_value": 33964.1782,
      "products_count": 4,
      "has_credit_card": 0,
      "has_loan": 1,
      "value_tier": "low"
    },
    "recent_complaint_text": "Failed transaction reversed only partially. Rs 60 still not credited."
  }
}
```

Response:

```json
{
  "meta": {
    "endpoint": "/predict/both",
    "served_at": "2026-08-31T01:54:17",
    "elapsed_ms": 3782.42,
    "timings_ms": {
      "model1": 70.69,
      "model2": 3711.58
    },
    "customer_id": "C16195",
    "customer_name": "Oscar Contractor",
    "snapshot_date": "2026-04-01"
  },
  "model1": {
    "churn_probability": 35.84,
    "raw_churn_probability": 89.51,
    "probability_mode": "sigmoid",
    "risk_score": 75.94,
    "churn_prediction": "Yes",
    "risk_level": "High",
    "top_risk_factors": [
      {
        "factor": "latest_days_since_last_transaction",
        "value": 16,
        "message": "Customer has gone longer without transacting.",
        "contribution": 0.43857088685035706
      },
      {
        "factor": "latest_transaction_change_30d",
        "value": -33.2669,
        "message": "Transaction activity has been falling across recent months.",
        "contribution": 0.24827666580677032
      },
      {
        "factor": "latest_salary_missing_days",
        "value": 3.0,
        "message": "Salary or pension was delayed recently.",
        "contribution": 0.2102251797914505
      },
      {
        "factor": "latest_card_spend_change_30d",
        "value": -63.0185,
        "message": "Card spending has been falling across recent months.",
        "contribution": 0.19945521652698517
      },
      {
        "factor": "days_since_last_transaction_trend_6m",
        "value": 2.599999999999999,
        "message": "Customer has gone longer without transacting.",
        "contribution": 0.17664854228496552
      }
    ]
  },
  "model2_input": {
    "customer_context": {
      "age": 27,
      "tenure_months": 81,
      "customer_segment": "salary",
      "income_regularity": "regular",
      "customer_yearly_value": 33964.1782,
      "products_count": 4,
      "has_credit_card": 0,
      "has_loan": 1
    },
    "behavior": {
      "days_since_last_transaction": 16,
      "balance_change_30d": -44.0438,
      "transaction_change_30d": -33.2669,
      "card_spend_change_30d": -63.0185,
      "app_login_change_30d": -57.3214,
      "salary_missing_days": 3,
      "external_transfer_change_30d": 89.1173,
      "upi_share_of_spend": 0.3704,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "emi_bounce_30d": 1
    },
    "service_evidence": {
      "complaints_30d": 5,
      "unresolved_complaints": 2,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 38.9291,
      "complaint_text": "Failed transaction reversed only partially. Rs 60 still not credited."
    },
    "model1": {
      "churn_probability": 0.3584,
      "churn_prediction": "Yes",
      "risk_level": "High",
      "top_risk_factors": [
        {
          "factor": "days_since_last_transaction",
          "value": 16
        },
        {
          "factor": "transaction_change_30d",
          "value": -33.2669
        },
        {
          "factor": "salary_missing_days",
          "value": 3
        }
      ]
    },
    "eligible_actions": [
      "COMPLAINT_ESCALATION",
      "LOAN_REVIEW",
      "FINANCIAL_GUIDANCE",
      "SERVICE_RECOVERY",
      "MONITOR"
    ],
    "case_id": "C16195"
  },
  "model2": {
    "case_id": "C16195",
    "ok": true,
    "prediction": {
      "evidence": [
        "complaints_30d=5",
        "unresolved_complaints=2",
        "avg_resolution_time_hrs=38.9",
        "complaint_text describes a recent service issue"
      ],
      "primary_reason": "SERVICE_DISSATISFACTION",
      "reasoning_summary": "Complaint escalation because complaints_30d=5 and unresolved_complaints=2 show service friction.",
      "recommended_action": "COMPLAINT_ESCALATION",
      "secondary_reasons": [],
      "urgency": "HIGH"
    },
    "warnings": [],
    "raw_text": "{\n    \"evidence\": [\n        \"complaints_30d=5\",\n        \"unresolved_complaints=2\",\n        \"avg_resolution_time_hrs=38.9\",\n        \"complaint_text describes a recent service issue\"\n    ],\n    \"primary_reason\": \"SERVICE_DISSATISFACTION\",\n    \"reasoning_summary\": \"Complaint escalation because complaints_30d=5 and unresolved_complaints=2 show service friction.\",\n    \"recommended_action\": \"COMPLAINT_ESCALATION\",\n    \"secondary_reasons\": [],\n    \"urgency\": \"HIGH\"\n}",
    "error": null,
    "latency_s": 3.7114,
    "simple_output": "Reason: SERVICE_DISSATISFACTION | Urgency: HIGH | Action: COMPLAINT_ESCALATION | Why: Complaint escalation because complaints_30d=5 and unresolved_complaints=2 show service friction."
  }
}
```

### Krishna Dhar (`C16445`)

- OK: `True`
- Shape errors: `[]`
- Simple output: Reason: UNKNOWN | Urgency: LOW | Action: MONITOR | Why: Complaint and resolution signals are mixed or weak; evidence is genuinely ambiguous.

Request:

```json
{
  "customer_id": "C16445",
  "customer_name": "Krishna Dhar",
  "prediction_date": "2026-06-01",
  "snapshot_date": "2026-06-01",
  "target_month": "2026-07-01",
  "profile": {
    "tenure_months": 179,
    "customer_segment": "farmer",
    "income_regularity": "seasonal",
    "products_count": 1,
    "has_credit_card": 0,
    "has_loan": 0
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 14,
      "balance_change_30d": -21.2514,
      "transaction_change_30d": -14.5964,
      "card_spend_change_30d": -37.786,
      "app_login_change_30d": -15.3866,
      "salary_missing_days": null,
      "external_transfer_change_30d": -19.7216,
      "upi_share_of_spend": 0.631,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 1,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 41.2604,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-02-01",
      "days_since_last_transaction": 14,
      "balance_change_30d": -10.6216,
      "transaction_change_30d": -8.6472,
      "card_spend_change_30d": -13.0595,
      "app_login_change_30d": 14.5646,
      "salary_missing_days": null,
      "external_transfer_change_30d": 4.4018,
      "upi_share_of_spend": 0.5656,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 1,
      "complaints_30d": 0,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 0.0,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-03-01",
      "days_since_last_transaction": 6,
      "balance_change_30d": 24.3782,
      "transaction_change_30d": 14.5753,
      "card_spend_change_30d": 22.7582,
      "app_login_change_30d": 29.5724,
      "salary_missing_days": null,
      "external_transfer_change_30d": 1.056,
      "upi_share_of_spend": 0.3359,
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
      "days_since_last_transaction": 5,
      "balance_change_30d": 19.2474,
      "transaction_change_30d": 11.6211,
      "card_spend_change_30d": 14.4136,
      "app_login_change_30d": 29.135,
      "salary_missing_days": null,
      "external_transfer_change_30d": -30.1792,
      "upi_share_of_spend": 0.3691,
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
      "days_since_last_transaction": 11,
      "balance_change_30d": 18.9088,
      "transaction_change_30d": 16.2888,
      "card_spend_change_30d": 32.6368,
      "app_login_change_30d": 10.9925,
      "salary_missing_days": null,
      "external_transfer_change_30d": -16.2333,
      "upi_share_of_spend": 0.3796,
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
      "days_since_last_transaction": 0,
      "balance_change_30d": 66.37,
      "transaction_change_30d": 64.928,
      "card_spend_change_30d": 75.3203,
      "app_login_change_30d": 21.2236,
      "salary_missing_days": null,
      "external_transfer_change_30d": -69.577,
      "upi_share_of_spend": 0.2426,
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
    "tenure_months": 179,
    "customer_segment": "farmer",
    "income_regularity": "seasonal",
    "products_count": 1,
    "has_credit_card": 0,
    "has_loan": 0,
    "days_since_last_transaction": 0,
    "balance_change_30d": 66.37,
    "transaction_change_30d": 64.928,
    "card_spend_change_30d": 75.3203,
    "app_login_change_30d": 21.2236,
    "salary_missing_days": null,
    "external_transfer_change_30d": -69.577,
    "upi_share_of_spend": 0.2426,
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
      "segment": "farmer",
      "income_regularity": "seasonal",
      "tenure_months": 179,
      "age": 57,
      "customer_yearly_value": 10606.7546,
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
    "served_at": "2026-08-31T01:54:24",
    "elapsed_ms": 7244.61,
    "timings_ms": {
      "model1": 57.02,
      "model2": 7187.45
    },
    "customer_id": "C16445",
    "customer_name": "Krishna Dhar",
    "snapshot_date": "2026-06-01"
  },
  "model1": {
    "churn_probability": 1.69,
    "raw_churn_probability": 14.76,
    "probability_mode": "sigmoid",
    "risk_score": 5.07,
    "churn_prediction": "No",
    "risk_level": "Low",
    "top_risk_factors": [
      {
        "factor": "latest_vs_avg_card_spend_change_30d_available_history",
        "value": 59.6064,
        "message": "This signal increased churn risk.",
        "contribution": 0.10030313581228256
      },
      {
        "factor": "latest_external_transfer_change_30d",
        "value": -69.577,
        "message": "This signal increased churn risk.",
        "contribution": 0.08609946817159653
      },
      {
        "factor": "latest_vs_avg_external_transfer_change_30d_available_history",
        "value": -47.868116666666666,
        "message": "This signal increased churn risk.",
        "contribution": 0.0442713163793087
      },
      {
        "factor": "max_days_since_last_transaction_3m",
        "value": 11.0,
        "message": "Customer has gone longer without transacting.",
        "contribution": 0.039571020752191544
      },
      {
        "factor": "avg_transaction_change_30d_6m",
        "value": 14.028266666666667,
        "message": "This signal increased churn risk.",
        "contribution": 0.025430208072066307
      }
    ]
  },
  "model2_input": {
    "customer_context": {
      "age": 57,
      "tenure_months": 179,
      "customer_segment": "farmer",
      "income_regularity": "seasonal",
      "customer_yearly_value": 10606.7546,
      "products_count": 1,
      "has_credit_card": 0,
      "has_loan": 0
    },
    "behavior": {
      "days_since_last_transaction": 0,
      "balance_change_30d": 66.37,
      "transaction_change_30d": 64.928,
      "card_spend_change_30d": 75.3203,
      "app_login_change_30d": 21.2236,
      "salary_missing_days": null,
      "external_transfer_change_30d": -69.577,
      "upi_share_of_spend": 0.2426,
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
      "churn_probability": 0.0169,
      "churn_prediction": "No",
      "risk_level": "Low",
      "top_risk_factors": [
        {
          "factor": "card_spend_change_30d",
          "value": 75.3203
        },
        {
          "factor": "external_transfer_change_30d",
          "value": -69.577
        },
        {
          "factor": "days_since_last_transaction",
          "value": 0
        }
      ]
    },
    "eligible_actions": [
      "SERVICE_RECOVERY",
      "RE_ENGAGEMENT",
      "MONITOR"
    ],
    "case_id": "C16445"
  },
  "model2": {
    "case_id": "C16445",
    "ok": true,
    "prediction": {
      "evidence": [
        "complaints_30d=0",
        "unresolved_complaints=0",
        "avg_resolution_time_hrs=0.0"
      ],
      "primary_reason": "UNKNOWN",
      "reasoning_summary": "Complaint and resolution signals are mixed or weak; evidence is genuinely ambiguous.",
      "recommended_action": "MONITOR",
      "secondary_reasons": [],
      "urgency": "LOW"
    },
    "warnings": [
      "evidence: 'complaints_30d=0' cites a zero/null value, which is not evidence; remove it",
      "evidence: 'unresolved_complaints=0' cites a zero/null value, which is not evidence; remove it",
      "evidence: 'avg_resolution_time_hrs=0.0' cites a zero/null value, which is not evidence; remove it"
    ],
    "raw_text": "{\"evidence\":[\"complaints_30d=0\",\"unresolved_complaints=0\",\"avg_resolution_time_hrs=0.0\"],\"primary_reason\":\"UNKNOWN\",\"reasoning_summary\":\"Complaint and resolution signals are mixed or weak; relationship with the product team is a concern.\",\"recommended_action\":\"RE_ENGAGEMENT\",\"secondary_reasons\":[],\"urgency\":\"MEDIUM\"}",
    "error": null,
    "latency_s": 7.1873,
    "simple_output": "Reason: UNKNOWN | Urgency: LOW | Action: MONITOR | Why: Complaint and resolution signals are mixed or weak; evidence is genuinely ambiguous."
  }
}
```

### Zaid Dube (`C17792`)

- OK: `True`
- Shape errors: `[]`
- Simple output: Reason: UNKNOWN | Urgency: LOW | Action: MONITOR | Why: Complaint and resolution signals are mixed or weak; evidence is genuinely ambiguous.

Request:

```json
{
  "customer_id": "C17792",
  "customer_name": "Zaid Dube",
  "prediction_date": "2026-01-01",
  "snapshot_date": "2026-01-01",
  "target_month": "2026-02-01",
  "profile": {
    "tenure_months": 19,
    "customer_segment": "vendor",
    "income_regularity": "irregular",
    "products_count": 1,
    "has_credit_card": 0,
    "has_loan": 0
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 13,
      "balance_change_30d": -1.8042,
      "transaction_change_30d": -1.2266,
      "card_spend_change_30d": -27.5389,
      "app_login_change_30d": 7.9321,
      "salary_missing_days": null,
      "external_transfer_change_30d": 28.7611,
      "upi_share_of_spend": 0.1976,
      "fd_maturing_in_30d": 1,
      "products_dropped_90d": 0,
      "complaints_30d": 0,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 2,
      "avg_resolution_time_hrs": 0.0,
      "emi_bounce_30d": 0
    }
  ],
  "customer": {
    "tenure_months": 19,
    "customer_segment": "vendor",
    "income_regularity": "irregular",
    "products_count": 1,
    "has_credit_card": 0,
    "has_loan": 0,
    "days_since_last_transaction": 13,
    "balance_change_30d": -1.8042,
    "transaction_change_30d": -1.2266,
    "card_spend_change_30d": -27.5389,
    "app_login_change_30d": 7.9321,
    "salary_missing_days": null,
    "external_transfer_change_30d": 28.7611,
    "upi_share_of_spend": 0.1976,
    "fd_maturing_in_30d": 1,
    "products_dropped_90d": 0,
    "complaints_30d": 0,
    "unresolved_complaints": 0,
    "failed_transactions_30d": 2,
    "avg_resolution_time_hrs": 0.0,
    "emi_bounce_30d": 0
  },
  "extra_context": {
    "customer_profile": {
      "segment": "vendor",
      "income_regularity": "irregular",
      "tenure_months": 19,
      "age": 34,
      "customer_yearly_value": 7525.1195,
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
    "served_at": "2026-08-31T01:54:31",
    "elapsed_ms": 7066.79,
    "timings_ms": {
      "model1": 96.6,
      "model2": 6970.02
    },
    "customer_id": "C17792",
    "customer_name": "Zaid Dube",
    "snapshot_date": "2026-01-01"
  },
  "model1": {
    "churn_probability": 6.68,
    "raw_churn_probability": 45.4,
    "probability_mode": "sigmoid",
    "risk_score": 20.05,
    "churn_prediction": "No",
    "risk_level": "Low",
    "top_risk_factors": [
      {
        "factor": "latest_days_since_last_transaction",
        "value": 13,
        "message": "Customer has gone longer without transacting.",
        "contribution": 0.20845437049865723
      },
      {
        "factor": "sum_fd_maturing_in_30d_3m",
        "value": 1.0,
        "message": "Customer has a fixed deposit maturing soon.",
        "contribution": 0.05535263940691948
      },
      {
        "factor": "latest_fd_maturing_in_30d",
        "value": 1,
        "message": "Customer has a fixed deposit maturing soon.",
        "contribution": 0.05458450689911842
      },
      {
        "factor": "avg_card_spend_change_30d_3m",
        "value": -27.5389,
        "message": "Card spending has been falling across recent months.",
        "contribution": 0.03003619611263275
      },
      {
        "factor": "avg_card_spend_change_30d_6m",
        "value": -27.5389,
        "message": "Card spending has been falling across recent months.",
        "contribution": 0.02433313988149166
      }
    ]
  },
  "model2_input": {
    "customer_context": {
      "age": 34,
      "tenure_months": 19,
      "customer_segment": "vendor",
      "income_regularity": "irregular",
      "customer_yearly_value": 7525.1195,
      "products_count": 1,
      "has_credit_card": 0,
      "has_loan": 0
    },
    "behavior": {
      "days_since_last_transaction": 13,
      "balance_change_30d": -1.8042,
      "transaction_change_30d": -1.2266,
      "card_spend_change_30d": -27.5389,
      "app_login_change_30d": 7.9321,
      "salary_missing_days": null,
      "external_transfer_change_30d": 28.7611,
      "upi_share_of_spend": 0.1976,
      "fd_maturing_in_30d": 1,
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
      "churn_probability": 0.0668,
      "churn_prediction": "No",
      "risk_level": "Low",
      "top_risk_factors": [
        {
          "factor": "days_since_last_transaction",
          "value": 13
        },
        {
          "factor": "fd_maturing_in_30d",
          "value": 1
        },
        {
          "factor": "card_spend_change_30d",
          "value": -27.5389
        }
      ]
    },
    "eligible_actions": [
      "SERVICE_RECOVERY",
      "PRODUCT_REVIEW",
      "MONITOR"
    ],
    "case_id": "C17792"
  },
  "model2": {
    "case_id": "C17792",
    "ok": true,
    "prediction": {
      "evidence": [
        "complaints_30d=0",
        "unresolved_complaints=0",
        "avg_resolution_time_hrs=0.0"
      ],
      "primary_reason": "UNKNOWN",
      "reasoning_summary": "Complaint and resolution signals are mixed or weak; evidence is genuinely ambiguous.",
      "recommended_action": "MONITOR",
      "secondary_reasons": [],
      "urgency": "LOW"
    },
    "warnings": [
      "evidence: 'complaints_30d=0' cites a zero/null value, which is not evidence; remove it",
      "evidence: 'unresolved_complaints=0' cites a zero/null value, which is not evidence; remove it",
      "evidence: 'avg_resolution_time_hrs=0.0' cites a zero/null value, which is not evidence; remove it"
    ],
    "raw_text": "{\"evidence\":[\"complaints_30d=0\",\"unresolved_complaints=0\",\"avg_resolution_time_hrs=0.0\"],\"primary_reason\":\"UNKNOWN\",\"reasoning_summary\":\"Complaint and resolution signals are mixed or weak; relationship with product or service is unclear.\",\"recommended_action\":\"MONITOR\",\"secondary_reasons\":[],\"urgency\":\"LOW\"}",
    "error": null,
    "latency_s": 6.9698,
    "simple_output": "Reason: UNKNOWN | Urgency: LOW | Action: MONITOR | Why: Complaint and resolution signals are mixed or weak; evidence is genuinely ambiguous."
  }
}
```

### Wishi Radhakrishnan (`C17972`)

- OK: `True`
- Shape errors: `[]`
- Simple output: Reason: UNKNOWN | Urgency: LOW | Action: MONITOR | Why: Complaint and resolution signals are mixed or weak; evidence is genuinely unclear.

Request:

```json
{
  "customer_id": "C17972",
  "customer_name": "Wishi Radhakrishnan",
  "prediction_date": "2026-06-01",
  "snapshot_date": "2026-06-01",
  "target_month": "2026-07-01",
  "profile": {
    "tenure_months": 31,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 2,
    "has_credit_card": 0,
    "has_loan": 1
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 4,
      "balance_change_30d": -35.2863,
      "transaction_change_30d": 0.84,
      "card_spend_change_30d": -0.2243,
      "app_login_change_30d": -27.8907,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -4.1982,
      "upi_share_of_spend": 0.3445,
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
      "days_since_last_transaction": 5,
      "balance_change_30d": 9.1652,
      "transaction_change_30d": 1.2814,
      "card_spend_change_30d": 2.1265,
      "app_login_change_30d": -2.4004,
      "salary_missing_days": 1.0,
      "external_transfer_change_30d": 9.5247,
      "upi_share_of_spend": 0.5353,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 19.1122,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-03-01",
      "days_since_last_transaction": 6,
      "balance_change_30d": 4.6971,
      "transaction_change_30d": 9.2189,
      "card_spend_change_30d": 24.7342,
      "app_login_change_30d": 10.7397,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": 14.3893,
      "upi_share_of_spend": 0.444,
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
      "days_since_last_transaction": 7,
      "balance_change_30d": 5.1944,
      "transaction_change_30d": 19.9242,
      "card_spend_change_30d": -6.605,
      "app_login_change_30d": 3.761,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -39.794,
      "upi_share_of_spend": 0.4659,
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
      "balance_change_30d": 36.7734,
      "transaction_change_30d": 31.3479,
      "card_spend_change_30d": 16.0694,
      "app_login_change_30d": -6.7818,
      "salary_missing_days": 1.0,
      "external_transfer_change_30d": -0.1546,
      "upi_share_of_spend": 0.2335,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 0,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 0.0,
      "emi_bounce_30d": 1
    },
    {
      "snapshot_date": "2026-06-01",
      "days_since_last_transaction": 2,
      "balance_change_30d": 15.5763,
      "transaction_change_30d": 0.5826,
      "card_spend_change_30d": 24.1652,
      "app_login_change_30d": 33.4917,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -12.8005,
      "upi_share_of_spend": 0.3448,
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
    "tenure_months": 31,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 2,
    "has_credit_card": 0,
    "has_loan": 1,
    "days_since_last_transaction": 2,
    "balance_change_30d": 15.5763,
    "transaction_change_30d": 0.5826,
    "card_spend_change_30d": 24.1652,
    "app_login_change_30d": 33.4917,
    "salary_missing_days": 0.0,
    "external_transfer_change_30d": -12.8005,
    "upi_share_of_spend": 0.3448,
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
      "tenure_months": 31,
      "age": 43,
      "customer_yearly_value": 8695.8316,
      "products_count": 2,
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
    "served_at": "2026-08-31T01:54:40",
    "elapsed_ms": 8776.03,
    "timings_ms": {
      "model1": 78.55,
      "model2": 8697.35
    },
    "customer_id": "C17972",
    "customer_name": "Wishi Radhakrishnan",
    "snapshot_date": "2026-06-01"
  },
  "model1": {
    "churn_probability": 2.1,
    "raw_churn_probability": 19.5,
    "probability_mode": "sigmoid",
    "risk_score": 6.3,
    "churn_prediction": "No",
    "risk_level": "Low",
    "top_risk_factors": [
      {
        "factor": "count_external_transfer_rise_6m",
        "value": 0,
        "message": "This signal increased churn risk.",
        "contribution": 0.017993154004216194
      },
      {
        "factor": "avg_transaction_change_30d_6m",
        "value": 10.532499999999999,
        "message": "This signal increased churn risk.",
        "contribution": 0.01493367925286293
      },
      {
        "factor": "avg_app_login_change_30d_6m",
        "value": 1.8199166666666666,
        "message": "This signal increased churn risk.",
        "contribution": 0.014533191919326782
      },
      {
        "factor": "max_salary_missing_days_6m",
        "value": 1.0,
        "message": "Salary or pension was delayed recently.",
        "contribution": 0.014255044050514698
      },
      {
        "factor": "card_spend_change_30d_trend_6m",
        "value": 3.783914285714285,
        "message": "This signal increased churn risk.",
        "contribution": 0.007431656122207642
      }
    ]
  },
  "model2_input": {
    "customer_context": {
      "age": 43,
      "tenure_months": 31,
      "customer_segment": "salary",
      "income_regularity": "regular",
      "customer_yearly_value": 8695.8316,
      "products_count": 2,
      "has_credit_card": 0,
      "has_loan": 1
    },
    "behavior": {
      "days_since_last_transaction": 2,
      "balance_change_30d": 15.5763,
      "transaction_change_30d": 0.5826,
      "card_spend_change_30d": 24.1652,
      "app_login_change_30d": 33.4917,
      "salary_missing_days": 0,
      "external_transfer_change_30d": -12.8005,
      "upi_share_of_spend": 0.3448,
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
      "churn_probability": 0.021,
      "churn_prediction": "No",
      "risk_level": "Low",
      "top_risk_factors": [
        {
          "factor": "transaction_change_30d",
          "value": 0.5826
        },
        {
          "factor": "app_login_change_30d",
          "value": 33.4917
        },
        {
          "factor": "salary_missing_days",
          "value": 0
        }
      ]
    },
    "eligible_actions": [
      "SERVICE_RECOVERY",
      "RE_ENGAGEMENT",
      "MONITOR"
    ],
    "case_id": "C17972"
  },
  "model2": {
    "case_id": "C17972",
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
    "raw_text": "{\"evidence\":[\"transaction_change_30d=0.58\",\"complaints_30d=0\"],\"primary_reason\":\"DIGITAL_FRICTION\",\"reasoning_summary\":\"Digital friction is the strongest supported signal here because transaction_change_30d=0.6 and app_login_change_30d=33.5 suggest a digital experience problem.\",\"recommended_action\":\"RE_ENGAGEMENT\",\"secondary_reasons\":[],\"urgency\":\"MEDIUM\"}",
    "error": null,
    "latency_s": 8.6971,
    "simple_output": "Reason: UNKNOWN | Urgency: LOW | Action: MONITOR | Why: Complaint and resolution signals are mixed or weak; evidence is genuinely unclear."
  }
}
```

### Charita Nair (`C18567`)

- OK: `True`
- Shape errors: `[]`
- Simple output: Reason: UNKNOWN | Urgency: LOW | Action: MONITOR | Why: Complaint and resolution signals are mixed or weak, so the cause remains uncertain.

Request:

```json
{
  "customer_id": "C18567",
  "customer_name": "Charita Nair",
  "prediction_date": "2026-06-01",
  "snapshot_date": "2026-06-01",
  "target_month": "2026-07-01",
  "profile": {
    "tenure_months": 122,
    "customer_segment": "business",
    "income_regularity": "irregular",
    "products_count": 3,
    "has_credit_card": 1,
    "has_loan": 0
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 7,
      "balance_change_30d": -13.4866,
      "transaction_change_30d": 8.5922,
      "card_spend_change_30d": 7.5828,
      "app_login_change_30d": 9.6229,
      "salary_missing_days": null,
      "external_transfer_change_30d": -2.8855,
      "upi_share_of_spend": 0.4486,
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
      "days_since_last_transaction": 8,
      "balance_change_30d": 0.4359,
      "transaction_change_30d": 10.8255,
      "card_spend_change_30d": 5.8831,
      "app_login_change_30d": -16.289,
      "salary_missing_days": null,
      "external_transfer_change_30d": 4.2576,
      "upi_share_of_spend": 0.5467,
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
      "days_since_last_transaction": 7,
      "balance_change_30d": 13.0577,
      "transaction_change_30d": 3.9337,
      "card_spend_change_30d": -17.8535,
      "app_login_change_30d": 34.1818,
      "salary_missing_days": null,
      "external_transfer_change_30d": 21.637,
      "upi_share_of_spend": 0.5892,
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
      "days_since_last_transaction": 8,
      "balance_change_30d": 20.2945,
      "transaction_change_30d": 13.9986,
      "card_spend_change_30d": -20.074,
      "app_login_change_30d": 17.8683,
      "salary_missing_days": null,
      "external_transfer_change_30d": -8.0068,
      "upi_share_of_spend": 0.4984,
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
      "days_since_last_transaction": 5,
      "balance_change_30d": 21.9949,
      "transaction_change_30d": 1.8689,
      "card_spend_change_30d": 12.0263,
      "app_login_change_30d": 28.3405,
      "salary_missing_days": null,
      "external_transfer_change_30d": -11.2751,
      "upi_share_of_spend": 0.5349,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 1,
      "complaints_30d": 0,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 0.0,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-06-01",
      "days_since_last_transaction": 11,
      "balance_change_30d": 19.6677,
      "transaction_change_30d": 23.9564,
      "card_spend_change_30d": 39.2923,
      "app_login_change_30d": 11.3463,
      "salary_missing_days": null,
      "external_transfer_change_30d": -34.3064,
      "upi_share_of_spend": 0.5148,
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
    "tenure_months": 122,
    "customer_segment": "business",
    "income_regularity": "irregular",
    "products_count": 3,
    "has_credit_card": 1,
    "has_loan": 0,
    "days_since_last_transaction": 11,
    "balance_change_30d": 19.6677,
    "transaction_change_30d": 23.9564,
    "card_spend_change_30d": 39.2923,
    "app_login_change_30d": 11.3463,
    "salary_missing_days": null,
    "external_transfer_change_30d": -34.3064,
    "upi_share_of_spend": 0.5148,
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
      "segment": "business",
      "income_regularity": "irregular",
      "tenure_months": 122,
      "age": 30,
      "customer_yearly_value": 136263.9085,
      "products_count": 3,
      "has_credit_card": 1,
      "has_loan": 0,
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
    "served_at": "2026-08-31T01:54:49",
    "elapsed_ms": 8795.33,
    "timings_ms": {
      "model1": 182.74,
      "model2": 8612.41
    },
    "customer_id": "C18567",
    "customer_name": "Charita Nair",
    "snapshot_date": "2026-06-01"
  },
  "model1": {
    "churn_probability": 2.52,
    "raw_churn_probability": 23.48,
    "probability_mode": "sigmoid",
    "risk_score": 7.55,
    "churn_prediction": "No",
    "risk_level": "Low",
    "top_risk_factors": [
      {
        "factor": "latest_vs_avg_card_spend_change_30d_available_history",
        "value": 34.81613333333333,
        "message": "This signal increased churn risk.",
        "contribution": 0.10104981064796448
      },
      {
        "factor": "card_spend_change_30d_trend_6m",
        "value": 4.993045714285713,
        "message": "This signal increased churn risk.",
        "contribution": 0.044217467308044434
      },
      {
        "factor": "latest_vs_avg_external_transfer_change_30d_available_history",
        "value": -29.209866666666663,
        "message": "This signal increased churn risk.",
        "contribution": 0.022293226793408394
      },
      {
        "factor": "latest_upi_share_of_spend",
        "value": 0.5148,
        "message": "A larger share of spending is happening through UPI.",
        "contribution": 0.014256294816732407
      },
      {
        "factor": "max_days_since_last_transaction_3m",
        "value": 11.0,
        "message": "Customer has gone longer without transacting.",
        "contribution": 0.0087207006290555
      }
    ]
  },
  "model2_input": {
    "customer_context": {
      "age": 30,
      "tenure_months": 122,
      "customer_segment": "business",
      "income_regularity": "irregular",
      "customer_yearly_value": 136263.9085,
      "products_count": 3,
      "has_credit_card": 1,
      "has_loan": 0
    },
    "behavior": {
      "days_since_last_transaction": 11,
      "balance_change_30d": 19.6677,
      "transaction_change_30d": 23.9564,
      "card_spend_change_30d": 39.2923,
      "app_login_change_30d": 11.3463,
      "salary_missing_days": null,
      "external_transfer_change_30d": -34.3064,
      "upi_share_of_spend": 0.5148,
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
      "churn_probability": 0.0252,
      "churn_prediction": "No",
      "risk_level": "Low",
      "top_risk_factors": [
        {
          "factor": "card_spend_change_30d",
          "value": 39.2923
        },
        {
          "factor": "external_transfer_change_30d",
          "value": -34.3064
        },
        {
          "factor": "upi_share_of_spend",
          "value": 0.5148
        }
      ]
    },
    "eligible_actions": [
      "SERVICE_RECOVERY",
      "RE_ENGAGEMENT",
      "MONITOR"
    ],
    "case_id": "C18567"
  },
  "model2": {
    "case_id": "C18567",
    "ok": true,
    "prediction": {
      "evidence": [
        "complaints_30d=0",
        "unresolved_complaints=0",
        "avg_resolution_time_hrs=0.0"
      ],
      "primary_reason": "UNKNOWN",
      "reasoning_summary": "Complaint and resolution signals are mixed or weak, so the cause remains uncertain.",
      "recommended_action": "MONITOR",
      "secondary_reasons": [],
      "urgency": "LOW"
    },
    "warnings": [
      "evidence: 'complaints_30d=0' cites a zero/null value, which is not evidence; remove it",
      "evidence: 'unresolved_complaints=0' cites a zero/null value, which is not evidence; remove it",
      "evidence: 'avg_resolution_time_hrs=0.0' cites a zero/null value, which is not evidence; remove it"
    ],
    "raw_text": "{\"evidence\":[\"complaints_30d=0\",\"unresolved_complaints=0\",\"avg_resolution_time_hrs=0.0\"],\"primary_reason\":\"DIGITAL_FRICTION\",\"reasoning_summary\":\"Digital friction is the strongest supported signal here because complaints_30d=0 and unresolved_complaints=0 cite a mixed or weak signal without avg_resolution_time_hrs=0.0 to amplify it.\",\"recommended_action\":\"RE_ENGAGEMENT\",\"secondary_reasons\":[],\"urgency\":\"MEDIUM\"}",
    "error": null,
    "latency_s": 8.6121,
    "simple_output": "Reason: UNKNOWN | Urgency: LOW | Action: MONITOR | Why: Complaint and resolution signals are mixed or weak, so the cause remains uncertain."
  }
}
```

### Aashi Datta (`C18742`)

- OK: `True`
- Shape errors: `[]`
- Simple output: Reason: SERVICE_DISSATISFACTION | Urgency: MEDIUM | Action: SERVICE_RECOVERY | Why: Complaint escalation because complaints_30d=1 and failed_transactions_30d=1 suggest a service problem.

Request:

```json
{
  "customer_id": "C18742",
  "customer_name": "Aashi Datta",
  "prediction_date": "2026-06-01",
  "snapshot_date": "2026-06-01",
  "target_month": "2026-07-01",
  "profile": {
    "tenure_months": 47,
    "customer_segment": "vendor",
    "income_regularity": "irregular",
    "products_count": 1,
    "has_credit_card": 0,
    "has_loan": 0
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 3,
      "balance_change_30d": -12.1976,
      "transaction_change_30d": -5.5812,
      "card_spend_change_30d": -3.3694,
      "app_login_change_30d": 14.8635,
      "salary_missing_days": null,
      "external_transfer_change_30d": -28.1976,
      "upi_share_of_spend": 0.1766,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 1,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 16.2176,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-02-01",
      "days_since_last_transaction": 6,
      "balance_change_30d": -2.5801,
      "transaction_change_30d": 2.2643,
      "card_spend_change_30d": 9.7424,
      "app_login_change_30d": 7.3048,
      "salary_missing_days": null,
      "external_transfer_change_30d": 36.7233,
      "upi_share_of_spend": 0.1599,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 2,
      "unresolved_complaints": 1,
      "failed_transactions_30d": 4,
      "avg_resolution_time_hrs": 41.3342,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-03-01",
      "days_since_last_transaction": 8,
      "balance_change_30d": 12.3578,
      "transaction_change_30d": 8.7143,
      "card_spend_change_30d": -11.3225,
      "app_login_change_30d": 3.2518,
      "salary_missing_days": null,
      "external_transfer_change_30d": 45.4388,
      "upi_share_of_spend": 0.1331,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 3,
      "avg_resolution_time_hrs": 9.4339,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-04-01",
      "days_since_last_transaction": 7,
      "balance_change_30d": 8.116,
      "transaction_change_30d": 20.7385,
      "card_spend_change_30d": 4.9667,
      "app_login_change_30d": 5.6626,
      "salary_missing_days": null,
      "external_transfer_change_30d": -16.813,
      "upi_share_of_spend": 0.1506,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 32.9626,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-05-01",
      "days_since_last_transaction": 1,
      "balance_change_30d": 14.1306,
      "transaction_change_30d": 13.3322,
      "card_spend_change_30d": 22.2867,
      "app_login_change_30d": 21.7343,
      "salary_missing_days": null,
      "external_transfer_change_30d": 9.5936,
      "upi_share_of_spend": 0.2049,
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
      "days_since_last_transaction": 0,
      "balance_change_30d": 21.5382,
      "transaction_change_30d": 33.5831,
      "card_spend_change_30d": 29.7751,
      "app_login_change_30d": 24.8422,
      "salary_missing_days": null,
      "external_transfer_change_30d": -27.0166,
      "upi_share_of_spend": 0.0147,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 1,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 17.6598,
      "emi_bounce_30d": 0
    }
  ],
  "customer": {
    "tenure_months": 47,
    "customer_segment": "vendor",
    "income_regularity": "irregular",
    "products_count": 1,
    "has_credit_card": 0,
    "has_loan": 0,
    "days_since_last_transaction": 0,
    "balance_change_30d": 21.5382,
    "transaction_change_30d": 33.5831,
    "card_spend_change_30d": 29.7751,
    "app_login_change_30d": 24.8422,
    "salary_missing_days": null,
    "external_transfer_change_30d": -27.0166,
    "upi_share_of_spend": 0.0147,
    "fd_maturing_in_30d": 0,
    "products_dropped_90d": 1,
    "complaints_30d": 1,
    "unresolved_complaints": 0,
    "failed_transactions_30d": 1,
    "avg_resolution_time_hrs": 17.6598,
    "emi_bounce_30d": 0
  },
  "extra_context": {
    "customer_profile": {
      "segment": "vendor",
      "income_regularity": "irregular",
      "tenure_months": 47,
      "age": 34,
      "customer_yearly_value": 6144.619,
      "products_count": 1,
      "has_credit_card": 0,
      "has_loan": 0,
      "value_tier": "low"
    },
    "recent_complaint_text": "Branch opens late almost daily. Customers wait outside in the sun."
  }
}
```

Response:

```json
{
  "meta": {
    "endpoint": "/predict/both",
    "served_at": "2026-08-31T01:54:59",
    "elapsed_ms": 10303.57,
    "timings_ms": {
      "model1": 70.21,
      "model2": 10233.23
    },
    "customer_id": "C18742",
    "customer_name": "Aashi Datta",
    "snapshot_date": "2026-06-01"
  },
  "model1": {
    "churn_probability": 2.55,
    "raw_churn_probability": 23.74,
    "probability_mode": "sigmoid",
    "risk_score": 7.64,
    "churn_prediction": "No",
    "risk_level": "Low",
    "top_risk_factors": [
      {
        "factor": "sum_failed_transactions_30d_6m",
        "value": 9.0,
        "message": "Customer has recent failed transactions.",
        "contribution": 0.10282719880342484
      },
      {
        "factor": "latest_upi_share_of_spend",
        "value": 0.0147,
        "message": "A larger share of spending is happening through UPI.",
        "contribution": 0.0945863127708435
      },
      {
        "factor": "sum_complaints_30d_6m",
        "value": 6.0,
        "message": "Customer has recent complaint activity.",
        "contribution": 0.06111818179488182
      },
      {
        "factor": "latest_vs_avg_external_transfer_change_30d_available_history",
        "value": -30.304683333333333,
        "message": "This signal increased churn risk.",
        "contribution": 0.034346695989370346
      },
      {
        "factor": "card_spend_change_30d_trend_6m",
        "value": 6.275559999999999,
        "message": "This signal increased churn risk.",
        "contribution": 0.028095701709389687
      }
    ]
  },
  "model2_input": {
    "customer_context": {
      "age": 34,
      "tenure_months": 47,
      "customer_segment": "vendor",
      "income_regularity": "irregular",
      "customer_yearly_value": 6144.619,
      "products_count": 1,
      "has_credit_card": 0,
      "has_loan": 0
    },
    "behavior": {
      "days_since_last_transaction": 0,
      "balance_change_30d": 21.5382,
      "transaction_change_30d": 33.5831,
      "card_spend_change_30d": 29.7751,
      "app_login_change_30d": 24.8422,
      "salary_missing_days": null,
      "external_transfer_change_30d": -27.0166,
      "upi_share_of_spend": 0.0147,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 1,
      "emi_bounce_30d": 0
    },
    "service_evidence": {
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 17.6598,
      "complaint_text": "Branch opens late almost daily. Customers wait outside in the sun."
    },
    "model1": {
      "churn_probability": 0.0255,
      "churn_prediction": "No",
      "risk_level": "Low",
      "top_risk_factors": [
        {
          "factor": "failed_transactions_30d",
          "value": 1
        },
        {
          "factor": "upi_share_of_spend",
          "value": 0.0147
        },
        {
          "factor": "complaints_30d",
          "value": 1
        }
      ]
    },
    "eligible_actions": [
      "SERVICE_RECOVERY",
      "PRODUCT_REVIEW",
      "MONITOR"
    ],
    "case_id": "C18742"
  },
  "model2": {
    "case_id": "C18742",
    "ok": true,
    "prediction": {
      "evidence": [
        "complaints_30d=1",
        "failed_transactions_30d=1",
        "avg_resolution_time_hrs=17.7",
        "complaint_text describes a recent service issue"
      ],
      "primary_reason": "SERVICE_DISSATISFACTION",
      "reasoning_summary": "Complaint escalation because complaints_30d=1 and failed_transactions_30d=1 suggest a service problem.",
      "recommended_action": "SERVICE_RECOVERY",
      "secondary_reasons": [],
      "urgency": "MEDIUM"
    },
    "warnings": [
      "reasoning_summary: describes COMPLAINT_ESCALATION but recommended_action is SERVICE_RECOVERY; rewrite the summary around the action you chose"
    ],
    "raw_text": "{\"evidence\":[\"complaints_30d=1\",\"failed_transactions_30d=1\",\"avg_resolution_time_hrs=17.7\",\"complaint_text describes a recent service issue\"],\"primary_reason\":\"SERVICE_DISSATISFACTION\",\"reasoning_summary\":\"Complaint escalation because complaints_30d=1 and failed_transactions_30d=1 point to a real service problem.\",\"recommended_action\":\"SERVICE_RECOVERY\",\"secondary_reasons\":[],\"urgency\":\"HIGH\"}",
    "error": null,
    "latency_s": 10.2331,
    "simple_output": "Reason: SERVICE_DISSATISFACTION | Urgency: MEDIUM | Action: SERVICE_RECOVERY | Why: Complaint escalation because complaints_30d=1 and failed_transactions_30d=1 suggest a service problem."
  }
}
```

### Rishi Amble (`C18959`)

- OK: `True`
- Shape errors: `[]`
- Simple output: Reason: FEE_DISSATISFACTION | Urgency: MEDIUM | Action: FEE_WAIVER_REVIEW | Why: Complaint evidence suggests dissatisfaction with fees or charges. Evidence suggests this because complaint_text=Aapne bina bataye charges badha diye. Yeh sahi baat nahi hai.; avg_resolution_time_hrs=25.7.

Request:

```json
{
  "customer_id": "C18959",
  "customer_name": "Rishi Amble",
  "prediction_date": "2026-06-01",
  "snapshot_date": "2026-06-01",
  "target_month": "2026-07-01",
  "profile": {
    "tenure_months": 77,
    "customer_segment": "pension",
    "income_regularity": "regular",
    "products_count": 1,
    "has_credit_card": 0,
    "has_loan": 0
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 10,
      "balance_change_30d": 23.073,
      "transaction_change_30d": 13.8527,
      "card_spend_change_30d": 8.4513,
      "app_login_change_30d": 12.6436,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": 1.9503,
      "upi_share_of_spend": 0.0,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 3,
      "unresolved_complaints": 1,
      "failed_transactions_30d": 3,
      "avg_resolution_time_hrs": 52.1297,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-02-01",
      "days_since_last_transaction": 11,
      "balance_change_30d": -18.3401,
      "transaction_change_30d": 5.7631,
      "card_spend_change_30d": -8.121,
      "app_login_change_30d": -20.8275,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": 8.9319,
      "upi_share_of_spend": 0.032,
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
      "days_since_last_transaction": 3,
      "balance_change_30d": 30.9336,
      "transaction_change_30d": 3.2037,
      "card_spend_change_30d": 1.2965,
      "app_login_change_30d": 42.1671,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -35.6603,
      "upi_share_of_spend": 0.0,
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
      "days_since_last_transaction": 5,
      "balance_change_30d": 37.9851,
      "transaction_change_30d": -1.854,
      "card_spend_change_30d": 4.6731,
      "app_login_change_30d": -0.9019,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": 4.1863,
      "upi_share_of_spend": 0.0,
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
      "days_since_last_transaction": 4,
      "balance_change_30d": 22.8029,
      "transaction_change_30d": 1.7462,
      "card_spend_change_30d": 20.45,
      "app_login_change_30d": 30.8742,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -56.5068,
      "upi_share_of_spend": 0.0,
      "fd_maturing_in_30d": 1,
      "products_dropped_90d": 0,
      "complaints_30d": 0,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 0.0,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-06-01",
      "days_since_last_transaction": 3,
      "balance_change_30d": 31.5161,
      "transaction_change_30d": 5.2518,
      "card_spend_change_30d": 20.587,
      "app_login_change_30d": 17.2541,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -7.5937,
      "upi_share_of_spend": 0.0,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 25.7242,
      "emi_bounce_30d": 0
    }
  ],
  "customer": {
    "tenure_months": 77,
    "customer_segment": "pension",
    "income_regularity": "regular",
    "products_count": 1,
    "has_credit_card": 0,
    "has_loan": 0,
    "days_since_last_transaction": 3,
    "balance_change_30d": 31.5161,
    "transaction_change_30d": 5.2518,
    "card_spend_change_30d": 20.587,
    "app_login_change_30d": 17.2541,
    "salary_missing_days": 0.0,
    "external_transfer_change_30d": -7.5937,
    "upi_share_of_spend": 0.0,
    "fd_maturing_in_30d": 0,
    "products_dropped_90d": 0,
    "complaints_30d": 1,
    "unresolved_complaints": 0,
    "failed_transactions_30d": 0,
    "avg_resolution_time_hrs": 25.7242,
    "emi_bounce_30d": 0
  },
  "extra_context": {
    "customer_profile": {
      "segment": "pension",
      "income_regularity": "regular",
      "tenure_months": 77,
      "age": 67,
      "customer_yearly_value": 16051.8685,
      "products_count": 1,
      "has_credit_card": 0,
      "has_loan": 0,
      "value_tier": "low"
    },
    "recent_complaint_text": "Aapne bina bataye charges badha diye. Yeh sahi baat nahi hai."
  }
}
```

Response:

```json
{
  "meta": {
    "endpoint": "/predict/both",
    "served_at": "2026-08-31T01:55:05",
    "elapsed_ms": 5222.95,
    "timings_ms": {
      "model1": 66.54,
      "model2": 5156.22
    },
    "customer_id": "C18959",
    "customer_name": "Rishi Amble",
    "snapshot_date": "2026-06-01"
  },
  "model1": {
    "churn_probability": 2.56,
    "raw_churn_probability": 23.82,
    "probability_mode": "sigmoid",
    "risk_score": 7.67,
    "churn_prediction": "No",
    "risk_level": "Low",
    "top_risk_factors": [
      {
        "factor": "sum_fd_maturing_in_30d_3m",
        "value": 1.0,
        "message": "Customer has a fixed deposit maturing soon.",
        "contribution": 0.07857856899499893
      },
      {
        "factor": "latest_upi_share_of_spend",
        "value": 0.0,
        "message": "This signal increased churn risk.",
        "contribution": 0.0611373670399189
      },
      {
        "factor": "max_salary_missing_days_6m",
        "value": 0.0,
        "message": "This signal increased churn risk.",
        "contribution": 0.02170749008655548
      },
      {
        "factor": "transaction_change_30d_trend_6m",
        "value": -1.717511428571428,
        "message": "Transaction activity has been falling across recent months.",
        "contribution": 0.02087041549384594
      },
      {
        "factor": "count_external_transfer_rise_6m",
        "value": 0,
        "message": "This signal increased churn risk.",
        "contribution": 0.018784482032060623
      }
    ]
  },
  "model2_input": {
    "customer_context": {
      "age": 67,
      "tenure_months": 77,
      "customer_segment": "pension",
      "income_regularity": "regular",
      "customer_yearly_value": 16051.8685,
      "products_count": 1,
      "has_credit_card": 0,
      "has_loan": 0
    },
    "behavior": {
      "days_since_last_transaction": 3,
      "balance_change_30d": 31.5161,
      "transaction_change_30d": 5.2518,
      "card_spend_change_30d": 20.587,
      "app_login_change_30d": 17.2541,
      "salary_missing_days": 0,
      "external_transfer_change_30d": -7.5937,
      "upi_share_of_spend": 0.0,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "emi_bounce_30d": 0
    },
    "service_evidence": {
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 25.7242,
      "complaint_text": "Aapne bina bataye charges badha diye. Yeh sahi baat nahi hai."
    },
    "model1": {
      "churn_probability": 0.0256,
      "churn_prediction": "No",
      "risk_level": "Low",
      "top_risk_factors": [
        {
          "factor": "fd_maturing_in_30d",
          "value": 0
        },
        {
          "factor": "upi_share_of_spend",
          "value": 0.0
        },
        {
          "factor": "salary_missing_days",
          "value": 0
        }
      ]
    },
    "eligible_actions": [
      "FEE_WAIVER_REVIEW",
      "SERVICE_RECOVERY",
      "MONITOR"
    ],
    "case_id": "C18959"
  },
  "model2": {
    "case_id": "C18959",
    "ok": true,
    "prediction": {
      "evidence": [
        "complaint_text=Aapne bina bataye charges badha diye. Yeh sahi baat nahi hai.",
        "avg_resolution_time_hrs=25.7",
        "complaints_30d=1"
      ],
      "primary_reason": "FEE_DISSATISFACTION",
      "reasoning_summary": "Complaint evidence suggests dissatisfaction with fees or charges. Evidence suggests this because complaint_text=Aapne bina bataye charges badha diye. Yeh sahi baat nahi hai.; avg_resolution_time_hrs=25.7.",
      "recommended_action": "FEE_WAIVER_REVIEW",
      "secondary_reasons": [],
      "urgency": "MEDIUM"
    },
    "warnings": [],
    "raw_text": "{\n    \"evidence\": [\n        \"complaint_text=Aapne bina bataye charges badha diye. Yeh sahi baat nahi hai.\",\n        \"avg_resolution_time_hrs=25.7\",\n        \"complaints_30d=1\"\n    ],\n    \"primary_reason\": \"FEE_DISSATISFACTION\",\n    \"reasoning_summary\": \"Complaint evidence suggests dissatisfaction with fees or charges. Evidence suggests this because complaint_text=Aapne bina bataye charges badha diye. Yeh sahi baat nahi hai.; avg_resolution_time_hrs=25.7.\",\n    \"recommended_action\": \"FEE_WAIVER_REVIEW\",\n    \"secondary_reasons\": [],\n    \"urgency\": \"MEDIUM\"\n}",
    "error": null,
    "latency_s": 5.1561,
    "simple_output": "Reason: FEE_DISSATISFACTION | Urgency: MEDIUM | Action: FEE_WAIVER_REVIEW | Why: Complaint evidence suggests dissatisfaction with fees or charges. Evidence suggests this because complaint_text=Aapne bina bataye charges badha diye. Yeh sahi baat nahi hai.; avg_resolution_time_hrs=25.7."
  }
}
```

### Abhimanyu Chandran (`C19165`)

- OK: `True`
- Shape errors: `[]`
- Simple output: Reason: UNKNOWN | Urgency: LOW | Action: MONITOR | Why: Complaint and service friction signals are mixed or weak; the cause remains uncertain.

Request:

```json
{
  "customer_id": "C19165",
  "customer_name": "Abhimanyu Chandran",
  "prediction_date": "2026-06-01",
  "snapshot_date": "2026-06-01",
  "target_month": "2026-07-01",
  "profile": {
    "tenure_months": 110,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 1,
    "has_credit_card": 0,
    "has_loan": 0
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 4,
      "balance_change_30d": 21.7161,
      "transaction_change_30d": 4.8409,
      "card_spend_change_30d": 11.0675,
      "app_login_change_30d": -5.9992,
      "salary_missing_days": 3.0,
      "external_transfer_change_30d": -37.0456,
      "upi_share_of_spend": 0.3421,
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
      "balance_change_30d": 37.9662,
      "transaction_change_30d": 36.803,
      "card_spend_change_30d": 40.536,
      "app_login_change_30d": 25.1632,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -32.249,
      "upi_share_of_spend": 0.2141,
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
      "days_since_last_transaction": 7,
      "balance_change_30d": 7.7649,
      "transaction_change_30d": -6.2369,
      "card_spend_change_30d": -8.4722,
      "app_login_change_30d": -14.9767,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": 7.4781,
      "upi_share_of_spend": 0.3713,
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
      "days_since_last_transaction": 3,
      "balance_change_30d": 4.3561,
      "transaction_change_30d": 18.066,
      "card_spend_change_30d": 22.2397,
      "app_login_change_30d": 29.9172,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": 0.6183,
      "upi_share_of_spend": 0.2551,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 25.1625,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-05-01",
      "days_since_last_transaction": 4,
      "balance_change_30d": 13.6736,
      "transaction_change_30d": 30.8135,
      "card_spend_change_30d": 42.1143,
      "app_login_change_30d": 38.1896,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -6.02,
      "upi_share_of_spend": 0.2477,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 0,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 2,
      "avg_resolution_time_hrs": 0.0,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-06-01",
      "days_since_last_transaction": 6,
      "balance_change_30d": 12.5965,
      "transaction_change_30d": 21.7481,
      "card_spend_change_30d": 26.691,
      "app_login_change_30d": 14.4434,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -31.6204,
      "upi_share_of_spend": 0.3092,
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
    "tenure_months": 110,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 1,
    "has_credit_card": 0,
    "has_loan": 0,
    "days_since_last_transaction": 6,
    "balance_change_30d": 12.5965,
    "transaction_change_30d": 21.7481,
    "card_spend_change_30d": 26.691,
    "app_login_change_30d": 14.4434,
    "salary_missing_days": 0.0,
    "external_transfer_change_30d": -31.6204,
    "upi_share_of_spend": 0.3092,
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
      "tenure_months": 110,
      "age": 33,
      "customer_yearly_value": 19660.9081,
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
    "served_at": "2026-08-31T01:55:13",
    "elapsed_ms": 8437.3,
    "timings_ms": {
      "model1": 67.43,
      "model2": 8369.74
    },
    "customer_id": "C19165",
    "customer_name": "Abhimanyu Chandran",
    "snapshot_date": "2026-06-01"
  },
  "model1": {
    "churn_probability": 2.56,
    "raw_churn_probability": 23.89,
    "probability_mode": "sigmoid",
    "risk_score": 7.69,
    "churn_prediction": "No",
    "risk_level": "Low",
    "top_risk_factors": [
      {
        "factor": "external_transfer_change_30d_trend_6m",
        "value": 2.827234285714286,
        "message": "External transfers have increased.",
        "contribution": 0.03924190625548363
      },
      {
        "factor": "latest_vs_avg_upi_share_of_spend_available_history",
        "value": 0.01928333333333332,
        "message": "A larger share of spending is happening through UPI.",
        "contribution": 0.024178413674235344
      },
      {
        "factor": "avg_transaction_change_30d_6m",
        "value": 17.672433333333334,
        "message": "This signal increased churn risk.",
        "contribution": 0.021710669621825218
      },
      {
        "factor": "count_external_transfer_rise_6m",
        "value": 0,
        "message": "This signal increased churn risk.",
        "contribution": 0.017123067751526833
      },
      {
        "factor": "latest_vs_avg_card_spend_change_30d_available_history",
        "value": 4.3282833333333315,
        "message": "This signal increased churn risk.",
        "contribution": 0.015142207033932209
      }
    ]
  },
  "model2_input": {
    "customer_context": {
      "age": 33,
      "tenure_months": 110,
      "customer_segment": "salary",
      "income_regularity": "regular",
      "customer_yearly_value": 19660.9081,
      "products_count": 1,
      "has_credit_card": 0,
      "has_loan": 0
    },
    "behavior": {
      "days_since_last_transaction": 6,
      "balance_change_30d": 12.5965,
      "transaction_change_30d": 21.7481,
      "card_spend_change_30d": 26.691,
      "app_login_change_30d": 14.4434,
      "salary_missing_days": 0,
      "external_transfer_change_30d": -31.6204,
      "upi_share_of_spend": 0.3092,
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
      "churn_probability": 0.0256,
      "churn_prediction": "No",
      "risk_level": "Low",
      "top_risk_factors": [
        {
          "factor": "external_transfer_change_30d",
          "value": -31.6204
        },
        {
          "factor": "upi_share_of_spend",
          "value": 0.3092
        },
        {
          "factor": "transaction_change_30d",
          "value": 21.7481
        }
      ]
    },
    "eligible_actions": [
      "RE_ENGAGEMENT",
      "PRODUCT_REVIEW",
      "MONITOR"
    ],
    "case_id": "C19165"
  },
  "model2": {
    "case_id": "C19165",
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
    "raw_text": "{\"evidence\":[\"complaints_30d=0\",\"unresolved_complaints=0\",\"avg_resolution_time_hrs=0.0\"],\"primary_reason\":\"LOW_ENGAGEMENT\",\"reasoning_summary\":\"Days_since_last_transaction=6 and transaction_change_30d=21.7 together suggest the relationship is on the right path but could use re-engagement.\",\"recommended_action\":\"RE_ENGAGEMENT\",\"secondary_reasons\":[],\"urgency\":\"MEDIUM\"}",
    "error": null,
    "latency_s": 8.3695,
    "simple_output": "Reason: UNKNOWN | Urgency: LOW | Action: MONITOR | Why: Complaint and service friction signals are mixed or weak; the cause remains uncertain."
  }
}
```

### Reyansh Dayal (`C19912`)

- OK: `True`
- Shape errors: `[]`
- Simple output: Reason: SERVICE_DISSATISFACTION | Urgency: MEDIUM | Action: COMPLAINT_ESCALATION | Why: Complaint escalation because complaints_30d=3 and unresolved_complaints=1 indicate a service issue.

Request:

```json
{
  "customer_id": "C19912",
  "customer_name": "Reyansh Dayal",
  "prediction_date": "2026-05-01",
  "snapshot_date": "2026-05-01",
  "target_month": "2026-06-01",
  "profile": {
    "tenure_months": 49,
    "customer_segment": "farmer",
    "income_regularity": "seasonal",
    "products_count": 2,
    "has_credit_card": 0,
    "has_loan": 1
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 5,
      "balance_change_30d": -8.1249,
      "transaction_change_30d": -9.2931,
      "card_spend_change_30d": 11.4126,
      "app_login_change_30d": 17.1809,
      "salary_missing_days": null,
      "external_transfer_change_30d": 1.5619,
      "upi_share_of_spend": 0.2364,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 2,
      "avg_resolution_time_hrs": 29.4719,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-02-01",
      "days_since_last_transaction": 12,
      "balance_change_30d": 7.3538,
      "transaction_change_30d": 4.1643,
      "card_spend_change_30d": -10.2745,
      "app_login_change_30d": -4.6626,
      "salary_missing_days": null,
      "external_transfer_change_30d": 53.8614,
      "upi_share_of_spend": 0.3046,
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
      "days_since_last_transaction": 4,
      "balance_change_30d": 18.8131,
      "transaction_change_30d": 18.6083,
      "card_spend_change_30d": 5.8729,
      "app_login_change_30d": 1.7488,
      "salary_missing_days": null,
      "external_transfer_change_30d": -3.1914,
      "upi_share_of_spend": 0.2625,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 11.8783,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-04-01",
      "days_since_last_transaction": 6,
      "balance_change_30d": 33.4756,
      "transaction_change_30d": -10.7926,
      "card_spend_change_30d": -24.2582,
      "app_login_change_30d": 8.833,
      "salary_missing_days": null,
      "external_transfer_change_30d": -34.4944,
      "upi_share_of_spend": 0.1821,
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
      "days_since_last_transaction": 11,
      "balance_change_30d": 5.1004,
      "transaction_change_30d": 28.2725,
      "card_spend_change_30d": -6.6478,
      "app_login_change_30d": -2.9672,
      "salary_missing_days": null,
      "external_transfer_change_30d": -8.427,
      "upi_share_of_spend": 0.2318,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 3,
      "unresolved_complaints": 1,
      "failed_transactions_30d": 3,
      "avg_resolution_time_hrs": 52.0866,
      "emi_bounce_30d": 0
    }
  ],
  "customer": {
    "tenure_months": 49,
    "customer_segment": "farmer",
    "income_regularity": "seasonal",
    "products_count": 2,
    "has_credit_card": 0,
    "has_loan": 1,
    "days_since_last_transaction": 11,
    "balance_change_30d": 5.1004,
    "transaction_change_30d": 28.2725,
    "card_spend_change_30d": -6.6478,
    "app_login_change_30d": -2.9672,
    "salary_missing_days": null,
    "external_transfer_change_30d": -8.427,
    "upi_share_of_spend": 0.2318,
    "fd_maturing_in_30d": 0,
    "products_dropped_90d": 0,
    "complaints_30d": 3,
    "unresolved_complaints": 1,
    "failed_transactions_30d": 3,
    "avg_resolution_time_hrs": 52.0866,
    "emi_bounce_30d": 0
  },
  "extra_context": {
    "customer_profile": {
      "segment": "farmer",
      "income_regularity": "seasonal",
      "tenure_months": 49,
      "age": 38,
      "customer_yearly_value": 15997.5877,
      "products_count": 2,
      "has_credit_card": 0,
      "has_loan": 1,
      "value_tier": "low"
    },
    "recent_complaint_text": "Farmer says crop payment delayed, will not be able to service loan."
  }
}
```

Response:

```json
{
  "meta": {
    "endpoint": "/predict/both",
    "served_at": "2026-08-31T01:55:17",
    "elapsed_ms": 4217.99,
    "timings_ms": {
      "model1": 70.65,
      "model2": 4147.19
    },
    "customer_id": "C19912",
    "customer_name": "Reyansh Dayal",
    "snapshot_date": "2026-05-01"
  },
  "model1": {
    "churn_probability": 9.12,
    "raw_churn_probability": 52.64,
    "probability_mode": "sigmoid",
    "risk_score": 27.36,
    "churn_prediction": "No",
    "risk_level": "Low",
    "top_risk_factors": [
      {
        "factor": "max_avg_resolution_time_hrs_3m",
        "value": 52.0866,
        "message": "Recent complaints took longer to resolve.",
        "contribution": 0.4233734905719757
      },
      {
        "factor": "latest_avg_resolution_time_hrs",
        "value": 52.0866,
        "message": "Recent complaints took longer to resolve.",
        "contribution": 0.33758941292762756
      },
      {
        "factor": "latest_failed_transactions_30d",
        "value": 3,
        "message": "Customer has recent failed transactions.",
        "contribution": 0.1464718133211136
      },
      {
        "factor": "sum_failed_transactions_30d_3m",
        "value": 5.0,
        "message": "Customer has recent failed transactions.",
        "contribution": 0.0496642105281353
      },
      {
        "factor": "latest_vs_avg_balance_change_30d_available_history",
        "value": -6.223200000000001,
        "message": "Balance has been falling across recent months.",
        "contribution": 0.042647138237953186
      }
    ]
  },
  "model2_input": {
    "customer_context": {
      "age": 38,
      "tenure_months": 49,
      "customer_segment": "farmer",
      "income_regularity": "seasonal",
      "customer_yearly_value": 15997.5877,
      "products_count": 2,
      "has_credit_card": 0,
      "has_loan": 1
    },
    "behavior": {
      "days_since_last_transaction": 11,
      "balance_change_30d": 5.1004,
      "transaction_change_30d": 28.2725,
      "card_spend_change_30d": -6.6478,
      "app_login_change_30d": -2.9672,
      "salary_missing_days": null,
      "external_transfer_change_30d": -8.427,
      "upi_share_of_spend": 0.2318,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "emi_bounce_30d": 0
    },
    "service_evidence": {
      "complaints_30d": 3,
      "unresolved_complaints": 1,
      "failed_transactions_30d": 3,
      "avg_resolution_time_hrs": 52.0866,
      "complaint_text": "Farmer says crop payment delayed, will not be able to service loan."
    },
    "model1": {
      "churn_probability": 0.0912,
      "churn_prediction": "No",
      "risk_level": "Low",
      "top_risk_factors": [
        {
          "factor": "failed_transactions_30d",
          "value": 3
        },
        {
          "factor": "balance_change_30d",
          "value": 5.1004
        },
        {
          "factor": "transaction_change_30d",
          "value": 28.2725
        }
      ]
    },
    "eligible_actions": [
      "COMPLAINT_ESCALATION",
      "LOAN_REVIEW",
      "SERVICE_RECOVERY",
      "MONITOR"
    ],
    "case_id": "C19912"
  },
  "model2": {
    "case_id": "C19912",
    "ok": true,
    "prediction": {
      "evidence": [
        "complaints_30d=3",
        "unresolved_complaints=1",
        "avg_resolution_time_hrs=52.1",
        "complaint_text describes a recent service issue"
      ],
      "primary_reason": "SERVICE_DISSATISFACTION",
      "reasoning_summary": "Complaint escalation because complaints_30d=3 and unresolved_complaints=1 indicate a service issue.",
      "recommended_action": "COMPLAINT_ESCALATION",
      "secondary_reasons": [],
      "urgency": "MEDIUM"
    },
    "warnings": [],
    "raw_text": "{\n    \"evidence\": [\n        \"complaints_30d=3\",\n        \"unresolved_complaints=1\",\n        \"avg_resolution_time_hrs=52.1\",\n        \"complaint_text describes a recent service issue\"\n    ],\n    \"primary_reason\": \"SERVICE_DISSATISFACTION\",\n    \"reasoning_summary\": \"Complaint escalation because complaints_30d=3 and unresolved_complaints=1 indicate a service issue.\",\n    \"recommended_action\": \"COMPLAINT_ESCALATION\",\n    \"secondary_reasons\": [],\n    \"urgency\": \"MEDIUM\"\n}",
    "error": null,
    "latency_s": 4.147,
    "simple_output": "Reason: SERVICE_DISSATISFACTION | Urgency: MEDIUM | Action: COMPLAINT_ESCALATION | Why: Complaint escalation because complaints_30d=3 and unresolved_complaints=1 indicate a service issue."
  }
}
```
