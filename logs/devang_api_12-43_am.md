# Devang Model 1 -> Model 2 API Test Results

- API URL: `http://127.0.0.1:8001`
- Created at: `2026-08-31T00:43:35`
- Customers tested: `10`
- Source CSV: `model_1_v2\data\customers.csv`
- Health OK: `True`
- Ollama model: `devang-model2-q4`
- Model 1 loaded: `True`

## Summary

| # | Customer | Model 1 risk | Prediction | Reason | Urgency | Action | OK | Seconds |
|---:|---|---:|---|---|---|---|---|---:|
| 1 | Lajita Sood (`C10165`) | 10.69 | No | SERVICE_DISSATISFACTION | HIGH | COMPLAINT_ESCALATION | yes | 9.83 |
| 2 | Manthan Modi (`C10229`) | 4.9 | No | COMPETITOR_MIGRATION | HIGH | SERVICE_RECOVERY | yes | 2.57 |
| 3 | Kashvi Bhasin (`C10725`) | 2.16 | No | UNKNOWN | MEDIUM | MONITOR | yes | 1.56 |
| 4 | Kashvi Atwal (`C11144`) | 9.58 | No | DIGITAL_FRICTION | HIGH | SERVICE_RECOVERY | yes | 2.43 |
| 5 | Saksham Edwin (`C13440`) | 3.26 | No | LOW_ENGAGEMENT | MEDIUM | RE_ENGAGEMENT | yes | 2.37 |
| 6 | Dakshesh Patla (`C16013`) | 4.71 | No | COMPETITOR_MIGRATION | HIGH | RE_ENGAGEMENT | yes | 2.19 |
| 7 | Warinder Sarna (`C18449`) | 2.55 | No | SERVICE_DISSATISFACTION | HIGH | COMPLAINT_ESCALATION | yes | 2.42 |
| 8 | Rishi Amble (`C18959`) | 2.56 | No | SERVICE_DISSATISFACTION | HIGH | COMPLAINT_ESCALATION | yes | 2.3 |
| 9 | Christopher Chacko (`C19484`) | 4.1 | No | SERVICE_DISSATISFACTION | HIGH | COMPLAINT_ESCALATION | yes | 2.14 |
| 10 | Akshay Basak (`C19549`) | 2.68 | No | UNKNOWN | MEDIUM | MONITOR | yes | 1.8 |

## Details

### Lajita Sood (`C10165`)

- OK: `True`
- Shape errors: `[]`
- Simple output: Reason: SERVICE_DISSATISFACTION | Urgency: HIGH | Action: COMPLAINT_ESCALATION | Why: Service friction is the clearest risk signal here. Complaint escalation fits because complaints_30d=1 and failed_transactions_30d=4 indicate the issue is unresolved or operationally serious.

Request:

```json
{
  "customer_id": "C10165",
  "customer_name": "Lajita Sood",
  "prediction_date": "2026-06-01",
  "snapshot_date": "2026-06-01",
  "target_month": "2026-07-01",
  "profile": {
    "tenure_months": 81,
    "customer_segment": "pension",
    "income_regularity": "regular",
    "products_count": 2,
    "has_credit_card": 0,
    "has_loan": 0
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 8,
      "balance_change_30d": -6.4462,
      "transaction_change_30d": -3.2769,
      "card_spend_change_30d": 24.0204,
      "app_login_change_30d": -0.9027,
      "salary_missing_days": 1.0,
      "external_transfer_change_30d": 21.2447,
      "upi_share_of_spend": 0.1632,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 1,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 31.1338,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-02-01",
      "days_since_last_transaction": 4,
      "balance_change_30d": -14.9671,
      "transaction_change_30d": -3.3442,
      "card_spend_change_30d": -9.9095,
      "app_login_change_30d": -15.5443,
      "salary_missing_days": 1.0,
      "external_transfer_change_30d": -6.4207,
      "upi_share_of_spend": 0.0686,
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
      "days_since_last_transaction": 4,
      "balance_change_30d": 0.9107,
      "transaction_change_30d": -11.3904,
      "card_spend_change_30d": 18.4452,
      "app_login_change_30d": -8.0705,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": 11.52,
      "upi_share_of_spend": 0.2062,
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
      "days_since_last_transaction": 10,
      "balance_change_30d": 3.8965,
      "transaction_change_30d": 9.436,
      "card_spend_change_30d": -2.9731,
      "app_login_change_30d": 5.4656,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -19.4332,
      "upi_share_of_spend": 0.1357,
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
      "days_since_last_transaction": 3,
      "balance_change_30d": -22.4692,
      "transaction_change_30d": -2.3253,
      "card_spend_change_30d": 1.6644,
      "app_login_change_30d": -28.8671,
      "salary_missing_days": 2.0,
      "external_transfer_change_30d": 13.0785,
      "upi_share_of_spend": 0.1465,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 31.5222,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-06-01",
      "days_since_last_transaction": 8,
      "balance_change_30d": -14.8476,
      "transaction_change_30d": -9.6186,
      "card_spend_change_30d": 1.1046,
      "app_login_change_30d": -44.3824,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": 67.1266,
      "upi_share_of_spend": 0.2112,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 4,
      "avg_resolution_time_hrs": 1.0,
      "emi_bounce_30d": 0
    }
  ],
  "customer": {
    "tenure_months": 81,
    "customer_segment": "pension",
    "income_regularity": "regular",
    "products_count": 2,
    "has_credit_card": 0,
    "has_loan": 0,
    "days_since_last_transaction": 8,
    "balance_change_30d": -14.8476,
    "transaction_change_30d": -9.6186,
    "card_spend_change_30d": 1.1046,
    "app_login_change_30d": -44.3824,
    "salary_missing_days": 0.0,
    "external_transfer_change_30d": 67.1266,
    "upi_share_of_spend": 0.2112,
    "fd_maturing_in_30d": 0,
    "products_dropped_90d": 0,
    "complaints_30d": 1,
    "unresolved_complaints": 0,
    "failed_transactions_30d": 4,
    "avg_resolution_time_hrs": 1.0,
    "emi_bounce_30d": 0
  },
  "extra_context": {
    "customer_profile": {
      "segment": "pension",
      "income_regularity": "regular",
      "tenure_months": 81,
      "age": 73,
      "customer_yearly_value": 18585.4853,
      "products_count": 2,
      "has_credit_card": 0,
      "has_loan": 0,
      "value_tier": "low"
    },
    "recent_complaint_text": "Kindly train your staff, the new clerk did not know the FD process."
  }
}
```

Response:

```json
{
  "meta": {
    "endpoint": "/predict/both",
    "served_at": "2026-08-31T00:43:15",
    "elapsed_ms": 9813.93,
    "timings_ms": {
      "model1": 125.42,
      "model2": 9688.39
    },
    "customer_id": "C10165",
    "customer_name": "Lajita Sood",
    "snapshot_date": "2026-06-01"
  },
  "model1": {
    "churn_probability": 10.69,
    "raw_churn_probability": 56.44,
    "probability_mode": "sigmoid",
    "risk_score": 32.77,
    "churn_prediction": "No",
    "risk_level": "Low",
    "top_risk_factors": [
      {
        "factor": "sum_failed_transactions_30d_3m",
        "value": 7.0,
        "message": "Customer has recent failed transactions.",
        "contribution": 0.30768606066703796
      },
      {
        "factor": "latest_vs_avg_upi_share_of_spend_available_history",
        "value": 0.055966666666666665,
        "message": "A larger share of spending is happening through UPI.",
        "contribution": 0.1912844032049179
      },
      {
        "factor": "latest_failed_transactions_30d",
        "value": 4,
        "message": "Customer has recent failed transactions.",
        "contribution": 0.17164821922779083
      },
      {
        "factor": "sum_failed_transactions_30d_6m",
        "value": 8.0,
        "message": "Customer has recent failed transactions.",
        "contribution": 0.13941049575805664
      },
      {
        "factor": "latest_external_transfer_change_30d",
        "value": 67.1266,
        "message": "External transfers have increased.",
        "contribution": 0.12588445842266083
      }
    ]
  },
  "model2_input": {
    "customer_context": {
      "age": 73,
      "tenure_months": 81,
      "customer_segment": "pension",
      "income_regularity": "regular",
      "customer_yearly_value": 18585.4853,
      "products_count": 2,
      "has_credit_card": 0,
      "has_loan": 0
    },
    "behavior": {
      "days_since_last_transaction": 8,
      "balance_change_30d": -14.8476,
      "transaction_change_30d": -9.6186,
      "card_spend_change_30d": 1.1046,
      "app_login_change_30d": -44.3824,
      "salary_missing_days": 0,
      "external_transfer_change_30d": 67.1266,
      "upi_share_of_spend": 0.2112,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "emi_bounce_30d": 0
    },
    "service_evidence": {
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 4,
      "avg_resolution_time_hrs": 1.0,
      "complaint_text": "Kindly train your staff, the new clerk did not know the FD process."
    },
    "model1": {
      "churn_probability": 0.1069,
      "churn_prediction": "No",
      "risk_level": "Low",
      "top_risk_factors": [
        {
          "factor": "sum_failed_transactions_30d_3m",
          "value": 7.0
        },
        {
          "factor": "vs_avg_upi_share_of_spend_available_history",
          "value": 0.055966666666666665
        },
        {
          "factor": "failed_transactions_30d",
          "value": 4
        },
        {
          "factor": "sum_failed_transactions_30d_6m",
          "value": 8.0
        },
        {
          "factor": "external_transfer_change_30d",
          "value": 67.1266
        }
      ]
    },
    "eligible_actions": [
      "MONITOR",
      "SERVICE_RECOVERY",
      "COMPLAINT_ESCALATION",
      "FEE_WAIVER_REVIEW",
      "RM_CALLBACK",
      "PRODUCT_REVIEW",
      "CARD_REVIEW",
      "LOAN_REVIEW",
      "RE_ENGAGEMENT",
      "FINANCIAL_GUIDANCE"
    ],
    "case_id": "C10165"
  },
  "model2": {
    "case_id": "C10165",
    "ok": true,
    "prediction": {
      "evidence": [
        "complaints_30d=1",
        "failed_transactions_30d=4",
        "avg_resolution_time_hrs=1.0",
        "complaint_text describes a recent service issue"
      ],
      "primary_reason": "SERVICE_DISSATISFACTION",
      "reasoning_summary": "Service friction is the clearest risk signal here. Complaint escalation fits because complaints_30d=1 and failed_transactions_30d=4 indicate the issue is unresolved or operationally serious.",
      "recommended_action": "COMPLAINT_ESCALATION",
      "secondary_reasons": [],
      "urgency": "HIGH"
    },
    "raw_text": "{\"evidence\":[\"complaints_30d=1\",\"failed_transactions_30d=4\",\"avg_resolution_time_hrs=1.0\",\"complaint_text describes a recent service issue\"],\"primary_reason\":\"SERVICE_DISSATISFACTION\",\"reasoning_summary\":\"Service friction is the clearest risk signal here. Complaint escalation fits because complaints_30d=1 and failed_transactions_30d=4 indicate the issue is unresolved or operationally serious.\",\"recommended_action\":\"COMPLAINT_ESCALATION\",\"secondary_reasons\":[],\"urgency\":\"HIGH\"}",
    "error": null,
    "latency_s": 9.6883,
    "simple_output": "Reason: SERVICE_DISSATISFACTION | Urgency: HIGH | Action: COMPLAINT_ESCALATION | Why: Service friction is the clearest risk signal here. Complaint escalation fits because complaints_30d=1 and failed_transactions_30d=4 indicate the issue is unresolved or operationally serious."
  }
}
```

### Manthan Modi (`C10229`)

- OK: `True`
- Shape errors: `[]`
- Simple output: Reason: COMPETITOR_MIGRATION | Urgency: HIGH | Action: SERVICE_RECOVERY | Why: The relationship looks at risk from outward movement signals and service friction. Service recovery fits because complaints_30d=0; unresolved_complaints=0; failed_transactions_30d=2 suggest a fixable service issue rather than a product problem.

Request:

```json
{
  "customer_id": "C10229",
  "customer_name": "Manthan Modi",
  "prediction_date": "2026-06-01",
  "snapshot_date": "2026-06-01",
  "target_month": "2026-07-01",
  "profile": {
    "tenure_months": 15,
    "customer_segment": "farmer",
    "income_regularity": "seasonal",
    "products_count": 1,
    "has_credit_card": 0,
    "has_loan": 0
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 10,
      "balance_change_30d": -30.214,
      "transaction_change_30d": 14.6441,
      "card_spend_change_30d": -24.4201,
      "app_login_change_30d": -17.5389,
      "salary_missing_days": null,
      "external_transfer_change_30d": 24.2042,
      "upi_share_of_spend": 0.4808,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 5,
      "unresolved_complaints": 1,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 22.6916,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-02-01",
      "days_since_last_transaction": 15,
      "balance_change_30d": -39.1413,
      "transaction_change_30d": -40.0434,
      "card_spend_change_30d": -25.8251,
      "app_login_change_30d": -23.1744,
      "salary_missing_days": null,
      "external_transfer_change_30d": 57.0331,
      "upi_share_of_spend": 0.5928,
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
      "balance_change_30d": 6.8198,
      "transaction_change_30d": -4.1126,
      "card_spend_change_30d": 9.7768,
      "app_login_change_30d": 18.1536,
      "salary_missing_days": null,
      "external_transfer_change_30d": 16.7455,
      "upi_share_of_spend": 0.3603,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 1.0,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-04-01",
      "days_since_last_transaction": 9,
      "balance_change_30d": 18.0543,
      "transaction_change_30d": -15.8929,
      "card_spend_change_30d": -30.472,
      "app_login_change_30d": -46.1068,
      "salary_missing_days": null,
      "external_transfer_change_30d": 32.0548,
      "upi_share_of_spend": 0.4149,
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
      "balance_change_30d": -30.96,
      "transaction_change_30d": -15.8673,
      "card_spend_change_30d": -23.0965,
      "app_login_change_30d": -4.3501,
      "salary_missing_days": null,
      "external_transfer_change_30d": 1.4152,
      "upi_share_of_spend": 0.4324,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 4,
      "avg_resolution_time_hrs": 25.3278,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-06-01",
      "days_since_last_transaction": 10,
      "balance_change_30d": -9.2222,
      "transaction_change_30d": 14.5212,
      "card_spend_change_30d": -23.9177,
      "app_login_change_30d": 16.3979,
      "salary_missing_days": null,
      "external_transfer_change_30d": 40.1081,
      "upi_share_of_spend": 0.3989,
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
    "tenure_months": 15,
    "customer_segment": "farmer",
    "income_regularity": "seasonal",
    "products_count": 1,
    "has_credit_card": 0,
    "has_loan": 0,
    "days_since_last_transaction": 10,
    "balance_change_30d": -9.2222,
    "transaction_change_30d": 14.5212,
    "card_spend_change_30d": -23.9177,
    "app_login_change_30d": 16.3979,
    "salary_missing_days": null,
    "external_transfer_change_30d": 40.1081,
    "upi_share_of_spend": 0.3989,
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
      "tenure_months": 15,
      "age": 39,
      "customer_yearly_value": 33958.8531,
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
    "served_at": "2026-08-31T00:43:17",
    "elapsed_ms": 2539.79,
    "timings_ms": {
      "model1": 78.58,
      "model2": 2461.08
    },
    "customer_id": "C10229",
    "customer_name": "Manthan Modi",
    "snapshot_date": "2026-06-01"
  },
  "model1": {
    "churn_probability": 4.9,
    "raw_churn_probability": 38.33,
    "probability_mode": "sigmoid",
    "risk_score": 14.7,
    "churn_prediction": "No",
    "risk_level": "Low",
    "top_risk_factors": [
      {
        "factor": "sum_failed_transactions_30d_3m",
        "value": 7.0,
        "message": "Customer has recent failed transactions.",
        "contribution": 0.2545908987522125
      },
      {
        "factor": "sum_failed_transactions_30d_6m",
        "value": 9.0,
        "message": "Customer has recent failed transactions.",
        "contribution": 0.18822962045669556
      },
      {
        "factor": "sum_complaints_30d_6m",
        "value": 7.0,
        "message": "Customer has recent complaint activity.",
        "contribution": 0.0765567198395729
      },
      {
        "factor": "avg_external_transfer_change_30d_3m",
        "value": 24.526033333333334,
        "message": "External transfers have increased.",
        "contribution": 0.04485644772648811
      },
      {
        "factor": "avg_card_spend_change_30d_3m",
        "value": -25.828733333333332,
        "message": "Card spending has been falling across recent months.",
        "contribution": 0.03543368726968765
      }
    ]
  },
  "model2_input": {
    "customer_context": {
      "age": 39,
      "tenure_months": 15,
      "customer_segment": "farmer",
      "income_regularity": "seasonal",
      "customer_yearly_value": 33958.8531,
      "products_count": 1,
      "has_credit_card": 0,
      "has_loan": 0
    },
    "behavior": {
      "days_since_last_transaction": 10,
      "balance_change_30d": -9.2222,
      "transaction_change_30d": 14.5212,
      "card_spend_change_30d": -23.9177,
      "app_login_change_30d": 16.3979,
      "salary_missing_days": null,
      "external_transfer_change_30d": 40.1081,
      "upi_share_of_spend": 0.3989,
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
      "churn_probability": 0.049,
      "churn_prediction": "No",
      "risk_level": "Low",
      "top_risk_factors": [
        {
          "factor": "sum_failed_transactions_30d_3m",
          "value": 7.0
        },
        {
          "factor": "sum_failed_transactions_30d_6m",
          "value": 9.0
        },
        {
          "factor": "sum_complaints_30d_6m",
          "value": 7.0
        },
        {
          "factor": "avg_external_transfer_change_30d_3m",
          "value": 24.526033333333334
        },
        {
          "factor": "avg_card_spend_change_30d_3m",
          "value": -25.828733333333332
        }
      ]
    },
    "eligible_actions": [
      "MONITOR",
      "SERVICE_RECOVERY",
      "COMPLAINT_ESCALATION",
      "FEE_WAIVER_REVIEW",
      "RM_CALLBACK",
      "PRODUCT_REVIEW",
      "CARD_REVIEW",
      "LOAN_REVIEW",
      "RE_ENGAGEMENT",
      "FINANCIAL_GUIDANCE"
    ],
    "case_id": "C10229"
  },
  "model2": {
    "case_id": "C10229",
    "ok": true,
    "prediction": {
      "evidence": [
        "complaints_30d=0",
        "unresolved_complaints=0",
        "failed_transactions_30d=2"
      ],
      "primary_reason": "COMPETITOR_MIGRATION",
      "reasoning_summary": "The relationship looks at risk from outward movement signals and service friction. Service recovery fits because complaints_30d=0; unresolved_complaints=0; failed_transactions_30d=2 suggest a fixable service issue rather than a product problem.",
      "recommended_action": "SERVICE_RECOVERY",
      "secondary_reasons": [],
      "urgency": "HIGH"
    },
    "raw_text": "{\"evidence\":[\"complaints_30d=0\",\"unresolved_complaints=0\",\"failed_transactions_30d=2\"],\"primary_reason\":\"COMPETITOR_MIGRATION\",\"reasoning_summary\":\"The relationship looks at risk from outward movement signals and service friction. Service recovery fits because complaints_30d=0; unresolved_complaints=0; failed_transactions_30d=2 suggest a fixable service issue rather than a product problem.\",\"recommended_action\":\"SERVICE_RECOVERY\",\"secondary_reasons\":[],\"urgency\":\"HIGH\"}",
    "error": null,
    "latency_s": 2.4603,
    "simple_output": "Reason: COMPETITOR_MIGRATION | Urgency: HIGH | Action: SERVICE_RECOVERY | Why: The relationship looks at risk from outward movement signals and service friction. Service recovery fits because complaints_30d=0; unresolved_complaints=0; failed_transactions_30d=2 suggest a fixable service issue rather than a product problem."
  }
}
```

### Kashvi Bhasin (`C10725`)

- OK: `True`
- Shape errors: `[]`
- Simple output: Reason: UNKNOWN | Urgency: MEDIUM | Action: MONITOR | Why: Evidence is mixed or limited, so the cause remains uncertain.

Request:

```json
{
  "customer_id": "C10725",
  "customer_name": "Kashvi Bhasin",
  "prediction_date": "2026-05-01",
  "snapshot_date": "2026-05-01",
  "target_month": "2026-06-01",
  "profile": {
    "tenure_months": 107,
    "customer_segment": "pension",
    "income_regularity": "regular",
    "products_count": 3,
    "has_credit_card": 1,
    "has_loan": 1
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 0,
      "balance_change_30d": 23.2332,
      "transaction_change_30d": 28.1664,
      "card_spend_change_30d": 31.255,
      "app_login_change_30d": 13.0844,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -30.8611,
      "upi_share_of_spend": 0.457,
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
      "days_since_last_transaction": 4,
      "balance_change_30d": 19.2134,
      "transaction_change_30d": 9.0802,
      "card_spend_change_30d": -7.4983,
      "app_login_change_30d": 38.5632,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -13.3057,
      "upi_share_of_spend": 0.486,
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
      "balance_change_30d": 27.0814,
      "transaction_change_30d": 27.5178,
      "card_spend_change_30d": -15.1567,
      "app_login_change_30d": 2.45,
      "salary_missing_days": 1.0,
      "external_transfer_change_30d": 23.4559,
      "upi_share_of_spend": 0.5142,
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
      "balance_change_30d": 11.4077,
      "transaction_change_30d": 27.6543,
      "card_spend_change_30d": 34.5231,
      "app_login_change_30d": 5.3177,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -31.9098,
      "upi_share_of_spend": 0.502,
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
      "days_since_last_transaction": 3,
      "balance_change_30d": 35.7425,
      "transaction_change_30d": 11.1998,
      "card_spend_change_30d": 9.1233,
      "app_login_change_30d": 35.1233,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -19.5988,
      "upi_share_of_spend": 0.4281,
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
    "tenure_months": 107,
    "customer_segment": "pension",
    "income_regularity": "regular",
    "products_count": 3,
    "has_credit_card": 1,
    "has_loan": 1,
    "days_since_last_transaction": 3,
    "balance_change_30d": 35.7425,
    "transaction_change_30d": 11.1998,
    "card_spend_change_30d": 9.1233,
    "app_login_change_30d": 35.1233,
    "salary_missing_days": 0.0,
    "external_transfer_change_30d": -19.5988,
    "upi_share_of_spend": 0.4281,
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
      "tenure_months": 107,
      "age": 72,
      "customer_yearly_value": 23881.4234,
      "products_count": 3,
      "has_credit_card": 1,
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
    "served_at": "2026-08-31T00:43:19",
    "elapsed_ms": 1551.02,
    "timings_ms": {
      "model1": 108.9,
      "model2": 1441.99
    },
    "customer_id": "C10725",
    "customer_name": "Kashvi Bhasin",
    "snapshot_date": "2026-05-01"
  },
  "model1": {
    "churn_probability": 2.16,
    "raw_churn_probability": 20.17,
    "probability_mode": "sigmoid",
    "risk_score": 6.49,
    "churn_prediction": "No",
    "risk_level": "Low",
    "top_risk_factors": [
      {
        "factor": "avg_transaction_change_30d_6m",
        "value": 20.7237,
        "message": "This signal increased churn risk.",
        "contribution": 0.051518380641937256
      },
      {
        "factor": "transaction_change_30d_trend_6m",
        "value": -1.5359100000000054,
        "message": "Transaction activity has been falling across recent months.",
        "contribution": 0.04119129478931427
      },
      {
        "factor": "external_transfer_change_30d_trend_6m",
        "value": 0.39205000000000245,
        "message": "External transfers have increased.",
        "contribution": 0.03477371856570244
      },
      {
        "factor": "app_login_change_30d_trend_6m",
        "value": 1.0832299999999957,
        "message": "This signal increased churn risk.",
        "contribution": 0.010747949592769146
      },
      {
        "factor": "max_salary_missing_days_6m",
        "value": 1.0,
        "message": "Salary or pension was delayed recently.",
        "contribution": 0.007368013262748718
      }
    ]
  },
  "model2_input": {
    "customer_context": {
      "age": 72,
      "tenure_months": 107,
      "customer_segment": "pension",
      "income_regularity": "regular",
      "customer_yearly_value": 23881.4234,
      "products_count": 3,
      "has_credit_card": 1,
      "has_loan": 1
    },
    "behavior": {
      "days_since_last_transaction": 3,
      "balance_change_30d": 35.7425,
      "transaction_change_30d": 11.1998,
      "card_spend_change_30d": 9.1233,
      "app_login_change_30d": 35.1233,
      "salary_missing_days": 0,
      "external_transfer_change_30d": -19.5988,
      "upi_share_of_spend": 0.4281,
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
      "churn_probability": 0.0216,
      "churn_prediction": "No",
      "risk_level": "Low",
      "top_risk_factors": [
        {
          "factor": "avg_transaction_change_30d_6m",
          "value": 20.7237
        },
        {
          "factor": "transaction_change_30d_trend_6m",
          "value": -1.5359100000000054
        },
        {
          "factor": "external_transfer_change_30d_trend_6m",
          "value": 0.39205000000000245
        },
        {
          "factor": "app_login_change_30d_trend_6m",
          "value": 1.0832299999999957
        },
        {
          "factor": "max_salary_missing_days_6m",
          "value": 1.0
        }
      ]
    },
    "eligible_actions": [
      "MONITOR",
      "SERVICE_RECOVERY",
      "COMPLAINT_ESCALATION",
      "FEE_WAIVER_REVIEW",
      "RM_CALLBACK",
      "PRODUCT_REVIEW",
      "CARD_REVIEW",
      "LOAN_REVIEW",
      "RE_ENGAGEMENT",
      "FINANCIAL_GUIDANCE"
    ],
    "case_id": "C10725"
  },
  "model2": {
    "case_id": "C10725",
    "ok": true,
    "prediction": {
      "evidence": [
        "transaction_change_30d=11.2",
        "balance_change_30d=35.7"
      ],
      "primary_reason": "UNKNOWN",
      "reasoning_summary": "Evidence is mixed or limited, so the cause remains uncertain.",
      "recommended_action": "MONITOR",
      "secondary_reasons": [],
      "urgency": "MEDIUM"
    },
    "raw_text": "{\"evidence\":[\"transaction_change_30d=11.2\",\"balance_change_30d=35.7\"],\"primary_reason\":\"UNKNOWN\",\"reasoning_summary\":\"Evidence is mixed or limited, so the cause remains uncertain.\",\"recommended_action\":\"MONITOR\",\"secondary_reasons\":[],\"urgency\":\"MEDIUM\"}",
    "error": null,
    "latency_s": 1.4418,
    "simple_output": "Reason: UNKNOWN | Urgency: MEDIUM | Action: MONITOR | Why: Evidence is mixed or limited, so the cause remains uncertain."
  }
}
```

### Kashvi Atwal (`C11144`)

- OK: `True`
- Shape errors: `[]`
- Simple output: Reason: DIGITAL_FRICTION | Urgency: HIGH | Action: SERVICE_RECOVERY | Why: Digital-service friction is the most supported explanation for the risk signal. Service recovery fits because transaction_change_30d=-30.3 and complaint_text mentions a digital or transaction problem suggest a process fix is needed before escalation.

Request:

```json
{
  "customer_id": "C11144",
  "customer_name": "Kashvi Atwal",
  "prediction_date": "2026-06-01",
  "snapshot_date": "2026-06-01",
  "target_month": "2026-07-01",
  "profile": {
    "tenure_months": 74,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 2,
    "has_credit_card": 0,
    "has_loan": 1
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 3,
      "balance_change_30d": 23.504,
      "transaction_change_30d": 19.6797,
      "card_spend_change_30d": 26.8553,
      "app_login_change_30d": 31.3013,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -3.6415,
      "upi_share_of_spend": 0.4275,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 27.4061,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-02-01",
      "days_since_last_transaction": 10,
      "balance_change_30d": -4.8305,
      "transaction_change_30d": 6.5889,
      "card_spend_change_30d": 20.3014,
      "app_login_change_30d": 14.8986,
      "salary_missing_days": 1.0,
      "external_transfer_change_30d": 38.6935,
      "upi_share_of_spend": 0.4356,
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
      "days_since_last_transaction": 5,
      "balance_change_30d": 20.3823,
      "transaction_change_30d": 15.3723,
      "card_spend_change_30d": 14.4146,
      "app_login_change_30d": 3.5685,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": 12.3098,
      "upi_share_of_spend": 0.4082,
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
      "balance_change_30d": -3.14,
      "transaction_change_30d": 9.6913,
      "card_spend_change_30d": 38.7393,
      "app_login_change_30d": 12.0147,
      "salary_missing_days": 1.0,
      "external_transfer_change_30d": 11.9117,
      "upi_share_of_spend": 0.3631,
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
      "days_since_last_transaction": 9,
      "balance_change_30d": -2.087,
      "transaction_change_30d": -4.9676,
      "card_spend_change_30d": -0.1724,
      "app_login_change_30d": -5.325,
      "salary_missing_days": 3.0,
      "external_transfer_change_30d": -11.997,
      "upi_share_of_spend": 0.4804,
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
      "days_since_last_transaction": 10,
      "balance_change_30d": -1.6249,
      "transaction_change_30d": -30.2779,
      "card_spend_change_30d": -13.1216,
      "app_login_change_30d": -13.6397,
      "salary_missing_days": 4.0,
      "external_transfer_change_30d": 45.1567,
      "upi_share_of_spend": 0.5239,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 2.6837,
      "emi_bounce_30d": 0
    }
  ],
  "customer": {
    "tenure_months": 74,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 2,
    "has_credit_card": 0,
    "has_loan": 1,
    "days_since_last_transaction": 10,
    "balance_change_30d": -1.6249,
    "transaction_change_30d": -30.2779,
    "card_spend_change_30d": -13.1216,
    "app_login_change_30d": -13.6397,
    "salary_missing_days": 4.0,
    "external_transfer_change_30d": 45.1567,
    "upi_share_of_spend": 0.5239,
    "fd_maturing_in_30d": 0,
    "products_dropped_90d": 0,
    "complaints_30d": 1,
    "unresolved_complaints": 0,
    "failed_transactions_30d": 0,
    "avg_resolution_time_hrs": 2.6837,
    "emi_bounce_30d": 0
  },
  "extra_context": {
    "customer_profile": {
      "segment": "salary",
      "income_regularity": "regular",
      "tenure_months": 74,
      "age": 38,
      "customer_yearly_value": 23364.0886,
      "products_count": 2,
      "has_credit_card": 0,
      "has_loan": 1,
      "value_tier": "low"
    },
    "recent_complaint_text": "UPI payment failed twice but amount was debited. No response yet."
  }
}
```

Response:

```json
{
  "meta": {
    "endpoint": "/predict/both",
    "served_at": "2026-08-31T00:43:21",
    "elapsed_ms": 2404.54,
    "timings_ms": {
      "model1": 58.8,
      "model2": 2345.64
    },
    "customer_id": "C11144",
    "customer_name": "Kashvi Atwal",
    "snapshot_date": "2026-06-01"
  },
  "model1": {
    "churn_probability": 9.58,
    "raw_churn_probability": 53.81,
    "probability_mode": "sigmoid",
    "risk_score": 28.75,
    "churn_prediction": "No",
    "risk_level": "Low",
    "top_risk_factors": [
      {
        "factor": "latest_salary_missing_days",
        "value": 4.0,
        "message": "Salary or pension was delayed recently.",
        "contribution": 0.3036269247531891
      },
      {
        "factor": "latest_transaction_change_30d",
        "value": -30.2779,
        "message": "Transaction activity has been falling across recent months.",
        "contribution": 0.2396300882101059
      },
      {
        "factor": "latest_vs_avg_upi_share_of_spend_available_history",
        "value": 0.08411666666666667,
        "message": "A larger share of spending is happening through UPI.",
        "contribution": 0.20566146075725555
      },
      {
        "factor": "transaction_change_30d_trend_6m",
        "value": -8.289671428571426,
        "message": "Transaction activity has been falling across recent months.",
        "contribution": 0.09533492475748062
      },
      {
        "factor": "latest_card_spend_change_30d",
        "value": -13.1216,
        "message": "Card spending has been falling across recent months.",
        "contribution": 0.02200389839708805
      }
    ]
  },
  "model2_input": {
    "customer_context": {
      "age": 38,
      "tenure_months": 74,
      "customer_segment": "salary",
      "income_regularity": "regular",
      "customer_yearly_value": 23364.0886,
      "products_count": 2,
      "has_credit_card": 0,
      "has_loan": 1
    },
    "behavior": {
      "days_since_last_transaction": 10,
      "balance_change_30d": -1.6249,
      "transaction_change_30d": -30.2779,
      "card_spend_change_30d": -13.1216,
      "app_login_change_30d": -13.6397,
      "salary_missing_days": 4,
      "external_transfer_change_30d": 45.1567,
      "upi_share_of_spend": 0.5239,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "emi_bounce_30d": 0
    },
    "service_evidence": {
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 2.6837,
      "complaint_text": "UPI payment failed twice but amount was debited. No response yet."
    },
    "model1": {
      "churn_probability": 0.0958,
      "churn_prediction": "No",
      "risk_level": "Low",
      "top_risk_factors": [
        {
          "factor": "salary_missing_days",
          "value": 4.0
        },
        {
          "factor": "transaction_change_30d",
          "value": -30.2779
        },
        {
          "factor": "vs_avg_upi_share_of_spend_available_history",
          "value": 0.08411666666666667
        },
        {
          "factor": "transaction_change_30d_trend_6m",
          "value": -8.289671428571426
        },
        {
          "factor": "card_spend_change_30d",
          "value": -13.1216
        }
      ]
    },
    "eligible_actions": [
      "MONITOR",
      "SERVICE_RECOVERY",
      "COMPLAINT_ESCALATION",
      "FEE_WAIVER_REVIEW",
      "RM_CALLBACK",
      "PRODUCT_REVIEW",
      "CARD_REVIEW",
      "LOAN_REVIEW",
      "RE_ENGAGEMENT",
      "FINANCIAL_GUIDANCE"
    ],
    "case_id": "C11144"
  },
  "model2": {
    "case_id": "C11144",
    "ok": true,
    "prediction": {
      "evidence": [
        "transaction_change_30d=-30.3",
        "complaint_text mentions a digital or transaction problem",
        "secondary_reasons=SERVICE_DISSATISFACTION"
      ],
      "primary_reason": "DIGITAL_FRICTION",
      "reasoning_summary": "Digital-service friction is the most supported explanation for the risk signal. Service recovery fits because transaction_change_30d=-30.3 and complaint_text mentions a digital or transaction problem suggest a process fix is needed before escalation.",
      "recommended_action": "SERVICE_RECOVERY",
      "secondary_reasons": [
        "SERVICE_DISSATISFACTION"
      ],
      "urgency": "HIGH"
    },
    "raw_text": "{\"evidence\":[\"transaction_change_30d=-30.3\",\"complaint_text mentions a digital or transaction problem\",\"secondary_reasons=SERVICE_DISSATISFACTION\"],\"primary_reason\":\"DIGITAL_FRICTION\",\"reasoning_summary\":\"Digital-service friction is the most supported explanation for the risk signal. Service recovery fits because transaction_change_30d=-30.3 and complaint_text mentions a digital or transaction problem suggest a process fix is needed before escalation.\",\"recommended_action\":\"SERVICE_RECOVERY\",\"secondary_reasons\":[\"SERVICE_DISSATISFACTION\"],\"urgency\":\"HIGH\"}",
    "error": null,
    "latency_s": 2.3455,
    "simple_output": "Reason: DIGITAL_FRICTION | Urgency: HIGH | Action: SERVICE_RECOVERY | Why: Digital-service friction is the most supported explanation for the risk signal. Service recovery fits because transaction_change_30d=-30.3 and complaint_text mentions a digital or transaction problem suggest a process fix is needed before escalation."
  }
}
```

### Saksham Edwin (`C13440`)

- OK: `True`
- Shape errors: `[]`
- Simple output: Reason: LOW_ENGAGEMENT | Urgency: MEDIUM | Action: RE_ENGAGEMENT | Why: The main signal is broad engagement decline without a stronger alternative explanation. Evidence suggests this because transaction_change_30d=-2.5; app_login_change_30d=16.0.

Request:

```json
{
  "customer_id": "C13440",
  "customer_name": "Saksham Edwin",
  "prediction_date": "2026-06-01",
  "snapshot_date": "2026-06-01",
  "target_month": "2026-07-01",
  "profile": {
    "tenure_months": 35,
    "customer_segment": "farmer",
    "income_regularity": "seasonal",
    "products_count": 1,
    "has_credit_card": 0,
    "has_loan": 0
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 21,
      "balance_change_30d": -23.8239,
      "transaction_change_30d": -17.5472,
      "card_spend_change_30d": -13.474,
      "app_login_change_30d": -13.5772,
      "salary_missing_days": null,
      "external_transfer_change_30d": 24.2321,
      "upi_share_of_spend": 0.2358,
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
      "days_since_last_transaction": 19,
      "balance_change_30d": -31.096,
      "transaction_change_30d": -21.1296,
      "card_spend_change_30d": -8.7175,
      "app_login_change_30d": -46.6856,
      "salary_missing_days": null,
      "external_transfer_change_30d": 36.7203,
      "upi_share_of_spend": 0.379,
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
      "days_since_last_transaction": 12,
      "balance_change_30d": 12.041,
      "transaction_change_30d": -17.8063,
      "card_spend_change_30d": -4.5054,
      "app_login_change_30d": 15.0853,
      "salary_missing_days": null,
      "external_transfer_change_30d": -10.7188,
      "upi_share_of_spend": 0.246,
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
      "days_since_last_transaction": 10,
      "balance_change_30d": 24.5557,
      "transaction_change_30d": 26.844,
      "card_spend_change_30d": 10.4631,
      "app_login_change_30d": 19.2582,
      "salary_missing_days": null,
      "external_transfer_change_30d": -23.325,
      "upi_share_of_spend": 0.2296,
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
      "balance_change_30d": 17.4765,
      "transaction_change_30d": 7.7812,
      "card_spend_change_30d": -6.2292,
      "app_login_change_30d": 15.4196,
      "salary_missing_days": null,
      "external_transfer_change_30d": 11.2683,
      "upi_share_of_spend": 0.3505,
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
      "days_since_last_transaction": 11,
      "balance_change_30d": 34.0331,
      "transaction_change_30d": -2.5034,
      "card_spend_change_30d": 11.5176,
      "app_login_change_30d": 16.0211,
      "salary_missing_days": null,
      "external_transfer_change_30d": -11.421,
      "upi_share_of_spend": 0.2735,
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
    "tenure_months": 35,
    "customer_segment": "farmer",
    "income_regularity": "seasonal",
    "products_count": 1,
    "has_credit_card": 0,
    "has_loan": 0,
    "days_since_last_transaction": 11,
    "balance_change_30d": 34.0331,
    "transaction_change_30d": -2.5034,
    "card_spend_change_30d": 11.5176,
    "app_login_change_30d": 16.0211,
    "salary_missing_days": null,
    "external_transfer_change_30d": -11.421,
    "upi_share_of_spend": 0.2735,
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
      "tenure_months": 35,
      "age": 56,
      "customer_yearly_value": 23070.6156,
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
    "served_at": "2026-08-31T00:43:24",
    "elapsed_ms": 2359.27,
    "timings_ms": {
      "model1": 67.69,
      "model2": 2291.46
    },
    "customer_id": "C13440",
    "customer_name": "Saksham Edwin",
    "snapshot_date": "2026-06-01"
  },
  "model1": {
    "churn_probability": 3.26,
    "raw_churn_probability": 29.18,
    "probability_mode": "sigmoid",
    "risk_score": 9.77,
    "churn_prediction": "No",
    "risk_level": "Low",
    "top_risk_factors": [
      {
        "factor": "latest_vs_avg_balance_change_30d_available_history",
        "value": 28.50203333333333,
        "message": "This signal increased churn risk.",
        "contribution": 0.05413104221224785
      },
      {
        "factor": "max_days_since_last_transaction_3m",
        "value": 11.0,
        "message": "Customer has gone longer without transacting.",
        "contribution": 0.01605292223393917
      },
      {
        "factor": "avg_upi_share_of_spend_6m",
        "value": 0.28573333333333334,
        "message": "A larger share of spending is happening through UPI.",
        "contribution": 0.014113095588982105
      },
      {
        "factor": "avg_card_spend_change_30d_3m",
        "value": 5.2505,
        "message": "This signal increased churn risk.",
        "contribution": 0.009409954771399498
      },
      {
        "factor": "card_spend_change_30d_trend_6m",
        "value": 4.211182857142855,
        "message": "This signal increased churn risk.",
        "contribution": 0.00920142512768507
      }
    ]
  },
  "model2_input": {
    "customer_context": {
      "age": 56,
      "tenure_months": 35,
      "customer_segment": "farmer",
      "income_regularity": "seasonal",
      "customer_yearly_value": 23070.6156,
      "products_count": 1,
      "has_credit_card": 0,
      "has_loan": 0
    },
    "behavior": {
      "days_since_last_transaction": 11,
      "balance_change_30d": 34.0331,
      "transaction_change_30d": -2.5034,
      "card_spend_change_30d": 11.5176,
      "app_login_change_30d": 16.0211,
      "salary_missing_days": null,
      "external_transfer_change_30d": -11.421,
      "upi_share_of_spend": 0.2735,
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
      "churn_probability": 0.0326,
      "churn_prediction": "No",
      "risk_level": "Low",
      "top_risk_factors": [
        {
          "factor": "vs_avg_balance_change_30d_available_history",
          "value": 28.50203333333333
        },
        {
          "factor": "max_days_since_last_transaction_3m",
          "value": 11.0
        },
        {
          "factor": "avg_upi_share_of_spend_6m",
          "value": 0.28573333333333334
        },
        {
          "factor": "avg_card_spend_change_30d_3m",
          "value": 5.2505
        },
        {
          "factor": "card_spend_change_30d_trend_6m",
          "value": 4.211182857142855
        }
      ]
    },
    "eligible_actions": [
      "MONITOR",
      "SERVICE_RECOVERY",
      "COMPLAINT_ESCALATION",
      "FEE_WAIVER_REVIEW",
      "RM_CALLBACK",
      "PRODUCT_REVIEW",
      "CARD_REVIEW",
      "LOAN_REVIEW",
      "RE_ENGAGEMENT",
      "FINANCIAL_GUIDANCE"
    ],
    "case_id": "C13440"
  },
  "model2": {
    "case_id": "C13440",
    "ok": true,
    "prediction": {
      "evidence": [
        "transaction_change_30d=-2.5",
        "app_login_change_30d=16.0",
        "card_spend_change_30d=11.5"
      ],
      "primary_reason": "LOW_ENGAGEMENT",
      "reasoning_summary": "The main signal is broad engagement decline without a stronger alternative explanation. Evidence suggests this because transaction_change_30d=-2.5; app_login_change_30d=16.0.",
      "recommended_action": "RE_ENGAGEMENT",
      "secondary_reasons": [],
      "urgency": "MEDIUM"
    },
    "raw_text": "{\"evidence\":[\"transaction_change_30d=-2.5\",\"app_login_change_30d=16.0\",\"card_spend_change_30d=11.5\"],\"primary_reason\":\"LOW_ENGAGEMENT\",\"reasoning_summary\":\"The main signal is broad engagement decline without a stronger alternative explanation. Evidence suggests this because transaction_change_30d=-2.5; app_login_change_30d=16.0.\",\"recommended_action\":\"RE_ENGAGEMENT\",\"secondary_reasons\":[],\"urgency\":\"MEDIUM\"}",
    "error": null,
    "latency_s": 2.2913,
    "simple_output": "Reason: LOW_ENGAGEMENT | Urgency: MEDIUM | Action: RE_ENGAGEMENT | Why: The main signal is broad engagement decline without a stronger alternative explanation. Evidence suggests this because transaction_change_30d=-2.5; app_login_change_30d=16.0."
  }
}
```

### Dakshesh Patla (`C16013`)

- OK: `True`
- Shape errors: `[]`
- Simple output: Reason: COMPETITOR_MIGRATION | Urgency: HIGH | Action: RE_ENGAGEMENT | Why: Complaint evidence suggests the relationship may be at risk from a competitor move. Evidence suggests this because complaints_30d=1; balance_change_30d=-33.2.

Request:

```json
{
  "customer_id": "C16013",
  "customer_name": "Dakshesh Patla",
  "prediction_date": "2026-06-01",
  "snapshot_date": "2026-06-01",
  "target_month": "2026-07-01",
  "profile": {
    "tenure_months": 144,
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
      "balance_change_30d": 16.9602,
      "transaction_change_30d": -1.3613,
      "card_spend_change_30d": -31.6821,
      "app_login_change_30d": -9.9493,
      "salary_missing_days": null,
      "external_transfer_change_30d": 45.4454,
      "upi_share_of_spend": 0.2634,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 26.9852,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-02-01",
      "days_since_last_transaction": 6,
      "balance_change_30d": 15.896,
      "transaction_change_30d": -6.8167,
      "card_spend_change_30d": 4.8341,
      "app_login_change_30d": -31.2984,
      "salary_missing_days": null,
      "external_transfer_change_30d": -1.9719,
      "upi_share_of_spend": 0.1996,
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
      "balance_change_30d": -0.4239,
      "transaction_change_30d": -3.8021,
      "card_spend_change_30d": 22.7226,
      "app_login_change_30d": -10.8127,
      "salary_missing_days": null,
      "external_transfer_change_30d": 8.443,
      "upi_share_of_spend": 0.1578,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 3,
      "avg_resolution_time_hrs": 18.8971,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-04-01",
      "days_since_last_transaction": 5,
      "balance_change_30d": 12.3271,
      "transaction_change_30d": 0.9318,
      "card_spend_change_30d": 8.3089,
      "app_login_change_30d": -4.6292,
      "salary_missing_days": null,
      "external_transfer_change_30d": 10.1205,
      "upi_share_of_spend": 0.2081,
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
      "balance_change_30d": -5.2185,
      "transaction_change_30d": 4.5473,
      "card_spend_change_30d": -10.3081,
      "app_login_change_30d": -10.8895,
      "salary_missing_days": null,
      "external_transfer_change_30d": 13.8516,
      "upi_share_of_spend": 0.1933,
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
      "days_since_last_transaction": 11,
      "balance_change_30d": -33.239,
      "transaction_change_30d": 18.5519,
      "card_spend_change_30d": -21.8798,
      "app_login_change_30d": -6.6172,
      "salary_missing_days": null,
      "external_transfer_change_30d": 54.4564,
      "upi_share_of_spend": 0.1176,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 24.4976,
      "emi_bounce_30d": 0
    }
  ],
  "customer": {
    "tenure_months": 144,
    "customer_segment": "farmer",
    "income_regularity": "seasonal",
    "products_count": 2,
    "has_credit_card": 0,
    "has_loan": 1,
    "days_since_last_transaction": 11,
    "balance_change_30d": -33.239,
    "transaction_change_30d": 18.5519,
    "card_spend_change_30d": -21.8798,
    "app_login_change_30d": -6.6172,
    "salary_missing_days": null,
    "external_transfer_change_30d": 54.4564,
    "upi_share_of_spend": 0.1176,
    "fd_maturing_in_30d": 0,
    "products_dropped_90d": 0,
    "complaints_30d": 1,
    "unresolved_complaints": 0,
    "failed_transactions_30d": 0,
    "avg_resolution_time_hrs": 24.4976,
    "emi_bounce_30d": 0
  },
  "extra_context": {
    "customer_profile": {
      "segment": "farmer",
      "income_regularity": "seasonal",
      "tenure_months": 144,
      "age": 48,
      "customer_yearly_value": 13343.8929,
      "products_count": 2,
      "has_credit_card": 0,
      "has_loan": 1,
      "value_tier": "low"
    },
    "recent_complaint_text": "Please help me link Aadhaar, the branch keeps redirecting me to CSC."
  }
}
```

Response:

```json
{
  "meta": {
    "endpoint": "/predict/both",
    "served_at": "2026-08-31T00:43:26",
    "elapsed_ms": 2170.49,
    "timings_ms": {
      "model1": 75.02,
      "model2": 2095.36
    },
    "customer_id": "C16013",
    "customer_name": "Dakshesh Patla",
    "snapshot_date": "2026-06-01"
  },
  "model1": {
    "churn_probability": 4.71,
    "raw_churn_probability": 37.45,
    "probability_mode": "sigmoid",
    "risk_score": 14.14,
    "churn_prediction": "No",
    "risk_level": "Low",
    "top_risk_factors": [
      {
        "factor": "latest_balance_change_30d",
        "value": -33.239,
        "message": "Balance has been falling across recent months.",
        "contribution": 0.14811648428440094
      },
      {
        "factor": "latest_external_transfer_change_30d",
        "value": 54.4564,
        "message": "External transfers have increased.",
        "contribution": 0.10168500989675522
      },
      {
        "factor": "days_since_last_transaction_trend_6m",
        "value": 0.9999999999999997,
        "message": "Customer has gone longer without transacting.",
        "contribution": 0.040570005774497986
      },
      {
        "factor": "balance_change_30d_trend_6m",
        "value": -8.616814285714286,
        "message": "Balance has been falling across recent months.",
        "contribution": 0.035890091210603714
      },
      {
        "factor": "latest_card_spend_change_30d",
        "value": -21.8798,
        "message": "Card spending has been falling across recent months.",
        "contribution": 0.03196810558438301
      }
    ]
  },
  "model2_input": {
    "customer_context": {
      "age": 48,
      "tenure_months": 144,
      "customer_segment": "farmer",
      "income_regularity": "seasonal",
      "customer_yearly_value": 13343.8929,
      "products_count": 2,
      "has_credit_card": 0,
      "has_loan": 1
    },
    "behavior": {
      "days_since_last_transaction": 11,
      "balance_change_30d": -33.239,
      "transaction_change_30d": 18.5519,
      "card_spend_change_30d": -21.8798,
      "app_login_change_30d": -6.6172,
      "salary_missing_days": null,
      "external_transfer_change_30d": 54.4564,
      "upi_share_of_spend": 0.1176,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "emi_bounce_30d": 0
    },
    "service_evidence": {
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 24.4976,
      "complaint_text": "Please help me link Aadhaar, the branch keeps redirecting me to CSC."
    },
    "model1": {
      "churn_probability": 0.0471,
      "churn_prediction": "No",
      "risk_level": "Low",
      "top_risk_factors": [
        {
          "factor": "balance_change_30d",
          "value": -33.239
        },
        {
          "factor": "external_transfer_change_30d",
          "value": 54.4564
        },
        {
          "factor": "days_since_last_transaction_trend_6m",
          "value": 0.9999999999999997
        },
        {
          "factor": "balance_change_30d_trend_6m",
          "value": -8.616814285714286
        },
        {
          "factor": "card_spend_change_30d",
          "value": -21.8798
        }
      ]
    },
    "eligible_actions": [
      "MONITOR",
      "SERVICE_RECOVERY",
      "COMPLAINT_ESCALATION",
      "FEE_WAIVER_REVIEW",
      "RM_CALLBACK",
      "PRODUCT_REVIEW",
      "CARD_REVIEW",
      "LOAN_REVIEW",
      "RE_ENGAGEMENT",
      "FINANCIAL_GUIDANCE"
    ],
    "case_id": "C16013"
  },
  "model2": {
    "case_id": "C16013",
    "ok": true,
    "prediction": {
      "evidence": [
        "complaints_30d=1",
        "balance_change_30d=-33.2"
      ],
      "primary_reason": "COMPETITOR_MIGRATION",
      "reasoning_summary": "Complaint evidence suggests the relationship may be at risk from a competitor move. Evidence suggests this because complaints_30d=1; balance_change_30d=-33.2.",
      "recommended_action": "RE_ENGAGEMENT",
      "secondary_reasons": [],
      "urgency": "HIGH"
    },
    "raw_text": "{\"evidence\":[\"complaints_30d=1\",\"balance_change_30d=-33.2\"],\"primary_reason\":\"COMPETITOR_MIGRATION\",\"reasoning_summary\":\"Complaint evidence suggests the relationship may be at risk from a competitor move. Evidence suggests this because complaints_30d=1; balance_change_30d=-33.2.\",\"recommended_action\":\"RE_ENGAGEMENT\",\"secondary_reasons\":[],\"urgency\":\"HIGH\"}",
    "error": null,
    "latency_s": 2.0952,
    "simple_output": "Reason: COMPETITOR_MIGRATION | Urgency: HIGH | Action: RE_ENGAGEMENT | Why: Complaint evidence suggests the relationship may be at risk from a competitor move. Evidence suggests this because complaints_30d=1; balance_change_30d=-33.2."
  }
}
```

### Warinder Sarna (`C18449`)

- OK: `True`
- Shape errors: `[]`
- Simple output: Reason: SERVICE_DISSATISFACTION | Urgency: HIGH | Action: COMPLAINT_ESCALATION | Why: Service friction is the clearest risk signal here. Complaint evidence suggests this because complaints_30d=1 and failed_transactions_30d=3.

Request:

```json
{
  "customer_id": "C18449",
  "customer_name": "Warinder Sarna",
  "prediction_date": "2026-06-01",
  "snapshot_date": "2026-06-01",
  "target_month": "2026-07-01",
  "profile": {
    "tenure_months": 123,
    "customer_segment": "pension",
    "income_regularity": "regular",
    "products_count": 2,
    "has_credit_card": 0,
    "has_loan": 0
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 7,
      "balance_change_30d": -23.727,
      "transaction_change_30d": 15.496,
      "card_spend_change_30d": -12.1543,
      "app_login_change_30d": -6.1136,
      "salary_missing_days": 3.0,
      "external_transfer_change_30d": 22.0323,
      "upi_share_of_spend": 0.339,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 2,
      "unresolved_complaints": 1,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 18.9163,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-02-01",
      "days_since_last_transaction": 8,
      "balance_change_30d": -22.1683,
      "transaction_change_30d": 4.1212,
      "card_spend_change_30d": 0.3399,
      "app_login_change_30d": -5.033,
      "salary_missing_days": 1.0,
      "external_transfer_change_30d": 10.0591,
      "upi_share_of_spend": 0.4106,
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
      "balance_change_30d": 28.3187,
      "transaction_change_30d": 9.4057,
      "card_spend_change_30d": -3.0978,
      "app_login_change_30d": 17.1981,
      "salary_missing_days": 1.0,
      "external_transfer_change_30d": 6.7721,
      "upi_share_of_spend": 0.3392,
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
      "balance_change_30d": 10.8899,
      "transaction_change_30d": 7.4736,
      "card_spend_change_30d": 2.4427,
      "app_login_change_30d": 4.6054,
      "salary_missing_days": 1.0,
      "external_transfer_change_30d": -12.2374,
      "upi_share_of_spend": 0.2428,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 1,
      "complaints_30d": 0,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 0.0,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-05-01",
      "days_since_last_transaction": 0,
      "balance_change_30d": 21.8137,
      "transaction_change_30d": 8.667,
      "card_spend_change_30d": 31.145,
      "app_login_change_30d": 27.4122,
      "salary_missing_days": 1.0,
      "external_transfer_change_30d": -47.9723,
      "upi_share_of_spend": 0.2672,
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
      "days_since_last_transaction": 5,
      "balance_change_30d": -0.5462,
      "transaction_change_30d": -0.6836,
      "card_spend_change_30d": 17.2686,
      "app_login_change_30d": 23.1396,
      "salary_missing_days": 1.0,
      "external_transfer_change_30d": -4.4809,
      "upi_share_of_spend": 0.3954,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 3,
      "avg_resolution_time_hrs": 4.2507,
      "emi_bounce_30d": 0
    }
  ],
  "customer": {
    "tenure_months": 123,
    "customer_segment": "pension",
    "income_regularity": "regular",
    "products_count": 2,
    "has_credit_card": 0,
    "has_loan": 0,
    "days_since_last_transaction": 5,
    "balance_change_30d": -0.5462,
    "transaction_change_30d": -0.6836,
    "card_spend_change_30d": 17.2686,
    "app_login_change_30d": 23.1396,
    "salary_missing_days": 1.0,
    "external_transfer_change_30d": -4.4809,
    "upi_share_of_spend": 0.3954,
    "fd_maturing_in_30d": 0,
    "products_dropped_90d": 0,
    "complaints_30d": 1,
    "unresolved_complaints": 0,
    "failed_transactions_30d": 3,
    "avg_resolution_time_hrs": 4.2507,
    "emi_bounce_30d": 0
  },
  "extra_context": {
    "customer_profile": {
      "segment": "pension",
      "income_regularity": "regular",
      "tenure_months": 123,
      "age": 73,
      "customer_yearly_value": 22680.3346,
      "products_count": 2,
      "has_credit_card": 0,
      "has_loan": 0,
      "value_tier": "low"
    },
    "recent_complaint_text": "Kindly refund the failed UPI of 12th. I have attached the screenshot."
  }
}
```

Response:

```json
{
  "meta": {
    "endpoint": "/predict/both",
    "served_at": "2026-08-31T00:43:28",
    "elapsed_ms": 2412.33,
    "timings_ms": {
      "model1": 111.39,
      "model2": 2300.83
    },
    "customer_id": "C18449",
    "customer_name": "Warinder Sarna",
    "snapshot_date": "2026-06-01"
  },
  "model1": {
    "churn_probability": 2.55,
    "raw_churn_probability": 23.73,
    "probability_mode": "sigmoid",
    "risk_score": 7.64,
    "churn_prediction": "No",
    "risk_level": "Low",
    "top_risk_factors": [
      {
        "factor": "latest_vs_avg_upi_share_of_spend_available_history",
        "value": 0.06303333333333333,
        "message": "A larger share of spending is happening through UPI.",
        "contribution": 0.11893592029809952
      },
      {
        "factor": "latest_failed_transactions_30d",
        "value": 3,
        "message": "Customer has recent failed transactions.",
        "contribution": 0.10484085232019424
      },
      {
        "factor": "card_spend_change_30d_trend_6m",
        "value": 7.00200857142857,
        "message": "This signal increased churn risk.",
        "contribution": 0.047285545617341995
      },
      {
        "factor": "transaction_change_30d_trend_6m",
        "value": -1.9769342857142842,
        "message": "Transaction activity has been falling across recent months.",
        "contribution": 0.026231536641716957
      },
      {
        "factor": "sum_failed_transactions_30d_3m",
        "value": 4.0,
        "message": "Customer has recent failed transactions.",
        "contribution": 0.023117244243621826
      }
    ]
  },
  "model2_input": {
    "customer_context": {
      "age": 73,
      "tenure_months": 123,
      "customer_segment": "pension",
      "income_regularity": "regular",
      "customer_yearly_value": 22680.3346,
      "products_count": 2,
      "has_credit_card": 0,
      "has_loan": 0
    },
    "behavior": {
      "days_since_last_transaction": 5,
      "balance_change_30d": -0.5462,
      "transaction_change_30d": -0.6836,
      "card_spend_change_30d": 17.2686,
      "app_login_change_30d": 23.1396,
      "salary_missing_days": 1,
      "external_transfer_change_30d": -4.4809,
      "upi_share_of_spend": 0.3954,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "emi_bounce_30d": 0
    },
    "service_evidence": {
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 3,
      "avg_resolution_time_hrs": 4.2507,
      "complaint_text": "Kindly refund the failed UPI of 12th. I have attached the screenshot."
    },
    "model1": {
      "churn_probability": 0.0255,
      "churn_prediction": "No",
      "risk_level": "Low",
      "top_risk_factors": [
        {
          "factor": "vs_avg_upi_share_of_spend_available_history",
          "value": 0.06303333333333333
        },
        {
          "factor": "failed_transactions_30d",
          "value": 3
        },
        {
          "factor": "card_spend_change_30d_trend_6m",
          "value": 7.00200857142857
        },
        {
          "factor": "transaction_change_30d_trend_6m",
          "value": -1.9769342857142842
        },
        {
          "factor": "sum_failed_transactions_30d_3m",
          "value": 4.0
        }
      ]
    },
    "eligible_actions": [
      "MONITOR",
      "SERVICE_RECOVERY",
      "COMPLAINT_ESCALATION",
      "FEE_WAIVER_REVIEW",
      "RM_CALLBACK",
      "PRODUCT_REVIEW",
      "CARD_REVIEW",
      "LOAN_REVIEW",
      "RE_ENGAGEMENT",
      "FINANCIAL_GUIDANCE"
    ],
    "case_id": "C18449"
  },
  "model2": {
    "case_id": "C18449",
    "ok": true,
    "prediction": {
      "evidence": [
        "complaints_30d=1",
        "failed_transactions_30d=3",
        "avg_resolution_time_hrs=4.3",
        "complaint_text describes a recent service issue"
      ],
      "primary_reason": "SERVICE_DISSATISFACTION",
      "reasoning_summary": "Service friction is the clearest risk signal here. Complaint evidence suggests this because complaints_30d=1 and failed_transactions_30d=3.",
      "recommended_action": "COMPLAINT_ESCALATION",
      "secondary_reasons": [],
      "urgency": "HIGH"
    },
    "raw_text": "{\"evidence\":[\"complaints_30d=1\",\"failed_transactions_30d=3\",\"avg_resolution_time_hrs=4.3\",\"complaint_text describes a recent service issue\"],\"primary_reason\":\"SERVICE_DISSATISFACTION\",\"reasoning_summary\":\"Service friction is the clearest risk signal here. Complaint evidence suggests this because complaints_30d=1 and failed_transactions_30d=3.\",\"recommended_action\":\"COMPLAINT_ESCALATION\",\"secondary_reasons\":[],\"urgency\":\"HIGH\"}",
    "error": null,
    "latency_s": 2.3007,
    "simple_output": "Reason: SERVICE_DISSATISFACTION | Urgency: HIGH | Action: COMPLAINT_ESCALATION | Why: Service friction is the clearest risk signal here. Complaint evidence suggests this because complaints_30d=1 and failed_transactions_30d=3."
  }
}
```

### Rishi Amble (`C18959`)

- OK: `True`
- Shape errors: `[]`
- Simple output: Reason: SERVICE_DISSATISFACTION | Urgency: HIGH | Action: COMPLAINT_ESCALATION | Why: Service friction is the clearest risk signal here. Complaint escalation fits because complaints_30d=1 and avg_resolution_time_hrs=25.7 indicate the issue is unresolved or operationally serious.

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
    "served_at": "2026-08-31T00:43:31",
    "elapsed_ms": 2294.4,
    "timings_ms": {
      "model1": 81.11,
      "model2": 2213.17
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
          "factor": "sum_fd_maturing_in_30d_3m",
          "value": 1.0
        },
        {
          "factor": "upi_share_of_spend",
          "value": 0.0
        },
        {
          "factor": "max_salary_missing_days_6m",
          "value": 0.0
        },
        {
          "factor": "transaction_change_30d_trend_6m",
          "value": -1.717511428571428
        },
        {
          "factor": "count_external_transfer_rise_6m",
          "value": 0
        }
      ]
    },
    "eligible_actions": [
      "MONITOR",
      "SERVICE_RECOVERY",
      "COMPLAINT_ESCALATION",
      "FEE_WAIVER_REVIEW",
      "RM_CALLBACK",
      "PRODUCT_REVIEW",
      "CARD_REVIEW",
      "LOAN_REVIEW",
      "RE_ENGAGEMENT",
      "FINANCIAL_GUIDANCE"
    ],
    "case_id": "C18959"
  },
  "model2": {
    "case_id": "C18959",
    "ok": true,
    "prediction": {
      "evidence": [
        "complaints_30d=1",
        "avg_resolution_time_hrs=25.7",
        "complaint_text describes a recent service issue"
      ],
      "primary_reason": "SERVICE_DISSATISFACTION",
      "reasoning_summary": "Service friction is the clearest risk signal here. Complaint escalation fits because complaints_30d=1 and avg_resolution_time_hrs=25.7 indicate the issue is unresolved or operationally serious.",
      "recommended_action": "COMPLAINT_ESCALATION",
      "secondary_reasons": [],
      "urgency": "HIGH"
    },
    "raw_text": "{\"evidence\":[\"complaints_30d=1\",\"avg_resolution_time_hrs=25.7\",\"complaint_text describes a recent service issue\"],\"primary_reason\":\"SERVICE_DISSATISFACTION\",\"reasoning_summary\":\"Service friction is the clearest risk signal here. Complaint escalation fits because complaints_30d=1 and avg_resolution_time_hrs=25.7 indicate the issue is unresolved or operationally serious.\",\"recommended_action\":\"COMPLAINT_ESCALATION\",\"secondary_reasons\":[],\"urgency\":\"HIGH\"}",
    "error": null,
    "latency_s": 2.213,
    "simple_output": "Reason: SERVICE_DISSATISFACTION | Urgency: HIGH | Action: COMPLAINT_ESCALATION | Why: Service friction is the clearest risk signal here. Complaint escalation fits because complaints_30d=1 and avg_resolution_time_hrs=25.7 indicate the issue is unresolved or operationally serious."
  }
}
```

### Christopher Chacko (`C19484`)

- OK: `True`
- Shape errors: `[]`
- Simple output: Reason: SERVICE_DISSATISFACTION | Urgency: HIGH | Action: COMPLAINT_ESCALATION | Why: Complaint evidence suggests a service friction is the strongest supported explanation for risk. Evidence suggests this because complaints_30d=1; comaint_text describes a recent transaction issue.

Request:

```json
{
  "customer_id": "C19484",
  "customer_name": "Christopher Chacko",
  "prediction_date": "2026-06-01",
  "snapshot_date": "2026-06-01",
  "target_month": "2026-07-01",
  "profile": {
    "tenure_months": 43,
    "customer_segment": "vendor",
    "income_regularity": "irregular",
    "products_count": 3,
    "has_credit_card": 0,
    "has_loan": 0
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 0,
      "balance_change_30d": 13.5499,
      "transaction_change_30d": 7.6246,
      "card_spend_change_30d": 19.2201,
      "app_login_change_30d": 13.7224,
      "salary_missing_days": null,
      "external_transfer_change_30d": -37.0465,
      "upi_share_of_spend": 0.4428,
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
      "balance_change_30d": 7.7752,
      "transaction_change_30d": -4.3642,
      "card_spend_change_30d": 5.1036,
      "app_login_change_30d": -20.2518,
      "salary_missing_days": null,
      "external_transfer_change_30d": 12.7875,
      "upi_share_of_spend": 0.515,
      "fd_maturing_in_30d": 1,
      "products_dropped_90d": 0,
      "complaints_30d": 2,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 2,
      "avg_resolution_time_hrs": 22.6638,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-03-01",
      "days_since_last_transaction": 11,
      "balance_change_30d": -19.1882,
      "transaction_change_30d": -43.3981,
      "card_spend_change_30d": -50.2106,
      "app_login_change_30d": -13.3979,
      "salary_missing_days": null,
      "external_transfer_change_30d": 61.9744,
      "upi_share_of_spend": 0.6311,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 20.13,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-04-01",
      "days_since_last_transaction": 14,
      "balance_change_30d": -22.4732,
      "transaction_change_30d": -8.3582,
      "card_spend_change_30d": -20.4329,
      "app_login_change_30d": -15.341,
      "salary_missing_days": null,
      "external_transfer_change_30d": 31.8088,
      "upi_share_of_spend": 0.6431,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 2,
      "unresolved_complaints": 1,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 36.1489,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-05-01",
      "days_since_last_transaction": 9,
      "balance_change_30d": -11.5909,
      "transaction_change_30d": 0.5566,
      "card_spend_change_30d": 13.5119,
      "app_login_change_30d": 28.5441,
      "salary_missing_days": null,
      "external_transfer_change_30d": 32.9363,
      "upi_share_of_spend": 0.4785,
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
      "days_since_last_transaction": 8,
      "balance_change_30d": 12.1375,
      "transaction_change_30d": 18.2546,
      "card_spend_change_30d": 13.9658,
      "app_login_change_30d": -13.4882,
      "salary_missing_days": null,
      "external_transfer_change_30d": -10.5364,
      "upi_share_of_spend": 0.4632,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 30.5809,
      "emi_bounce_30d": 0
    }
  ],
  "customer": {
    "tenure_months": 43,
    "customer_segment": "vendor",
    "income_regularity": "irregular",
    "products_count": 3,
    "has_credit_card": 0,
    "has_loan": 0,
    "days_since_last_transaction": 8,
    "balance_change_30d": 12.1375,
    "transaction_change_30d": 18.2546,
    "card_spend_change_30d": 13.9658,
    "app_login_change_30d": -13.4882,
    "salary_missing_days": null,
    "external_transfer_change_30d": -10.5364,
    "upi_share_of_spend": 0.4632,
    "fd_maturing_in_30d": 0,
    "products_dropped_90d": 0,
    "complaints_30d": 1,
    "unresolved_complaints": 0,
    "failed_transactions_30d": 0,
    "avg_resolution_time_hrs": 30.5809,
    "emi_bounce_30d": 0
  },
  "extra_context": {
    "customer_profile": {
      "segment": "vendor",
      "income_regularity": "irregular",
      "tenure_months": 43,
      "age": 49,
      "customer_yearly_value": 11093.6721,
      "products_count": 3,
      "has_credit_card": 0,
      "has_loan": 0,
      "value_tier": "low"
    },
    "recent_complaint_text": "UPI payment failed twice but amount was debited. No response yet."
  }
}
```

Response:

```json
{
  "meta": {
    "endpoint": "/predict/both",
    "served_at": "2026-08-31T00:43:33",
    "elapsed_ms": 2124.28,
    "timings_ms": {
      "model1": 63.82,
      "model2": 2060.35
    },
    "customer_id": "C19484",
    "customer_name": "Christopher Chacko",
    "snapshot_date": "2026-06-01"
  },
  "model1": {
    "churn_probability": 4.1,
    "raw_churn_probability": 34.31,
    "probability_mode": "sigmoid",
    "risk_score": 12.3,
    "churn_prediction": "No",
    "risk_level": "Low",
    "top_risk_factors": [
      {
        "factor": "latest_avg_resolution_time_hrs",
        "value": 30.5809,
        "message": "Recent complaints took longer to resolve.",
        "contribution": 0.12112035602331161
      },
      {
        "factor": "days_since_last_transaction_trend_6m",
        "value": 1.2285714285714282,
        "message": "Customer has gone longer without transacting.",
        "contribution": 0.11210320144891739
      },
      {
        "factor": "sum_complaints_30d_6m",
        "value": 6.0,
        "message": "Customer has recent complaint activity.",
        "contribution": 0.07606286555528641
      },
      {
        "factor": "external_transfer_change_30d_trend_6m",
        "value": 4.652322857142856,
        "message": "External transfers have increased.",
        "contribution": 0.03390498459339142
      },
      {
        "factor": "latest_vs_avg_external_transfer_change_30d_available_history",
        "value": -25.857083333333335,
        "message": "This signal increased churn risk.",
        "contribution": 0.019056595861911774
      }
    ]
  },
  "model2_input": {
    "customer_context": {
      "age": 49,
      "tenure_months": 43,
      "customer_segment": "vendor",
      "income_regularity": "irregular",
      "customer_yearly_value": 11093.6721,
      "products_count": 3,
      "has_credit_card": 0,
      "has_loan": 0
    },
    "behavior": {
      "days_since_last_transaction": 8,
      "balance_change_30d": 12.1375,
      "transaction_change_30d": 18.2546,
      "card_spend_change_30d": 13.9658,
      "app_login_change_30d": -13.4882,
      "salary_missing_days": null,
      "external_transfer_change_30d": -10.5364,
      "upi_share_of_spend": 0.4632,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "emi_bounce_30d": 0
    },
    "service_evidence": {
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 30.5809,
      "complaint_text": "UPI payment failed twice but amount was debited. No response yet."
    },
    "model1": {
      "churn_probability": 0.041,
      "churn_prediction": "No",
      "risk_level": "Low",
      "top_risk_factors": [
        {
          "factor": "avg_resolution_time_hrs",
          "value": 30.5809
        },
        {
          "factor": "days_since_last_transaction_trend_6m",
          "value": 1.2285714285714282
        },
        {
          "factor": "sum_complaints_30d_6m",
          "value": 6.0
        },
        {
          "factor": "external_transfer_change_30d_trend_6m",
          "value": 4.652322857142856
        },
        {
          "factor": "vs_avg_external_transfer_change_30d_available_history",
          "value": -25.857083333333335
        }
      ]
    },
    "eligible_actions": [
      "MONITOR",
      "SERVICE_RECOVERY",
      "COMPLAINT_ESCALATION",
      "FEE_WAIVER_REVIEW",
      "RM_CALLBACK",
      "PRODUCT_REVIEW",
      "CARD_REVIEW",
      "LOAN_REVIEW",
      "RE_ENGAGEMENT",
      "FINANCIAL_GUIDANCE"
    ],
    "case_id": "C19484"
  },
  "model2": {
    "case_id": "C19484",
    "ok": true,
    "prediction": {
      "evidence": [
        "complaints_30d=1",
        "external_transfer_change_30d=-10.5"
      ],
      "primary_reason": "SERVICE_DISSATISFACTION",
      "reasoning_summary": "Complaint evidence suggests a service friction is the strongest supported explanation for risk. Evidence suggests this because complaints_30d=1; comaint_text describes a recent transaction issue.",
      "recommended_action": "COMPLAINT_ESCALATION",
      "secondary_reasons": [],
      "urgency": "HIGH"
    },
    "raw_text": "{\"evidence\":[\"complaints_30d=1\",\"external_transfer_change_30d=-10.5\"],\"primary_reason\":\"SERVICE_DISSATISFACTION\",\"reasoning_summary\":\"Complaint evidence suggests a service friction is the strongest supported explanation for risk. Evidence suggests this because complaints_30d=1; comaint_text describes a recent transaction issue.\",\"recommended_action\":\"COMPLAINT_ESCALATION\",\"secondary_reasons\":[],\"urgency\":\"HIGH\"}",
    "error": null,
    "latency_s": 2.0601,
    "simple_output": "Reason: SERVICE_DISSATISFACTION | Urgency: HIGH | Action: COMPLAINT_ESCALATION | Why: Complaint evidence suggests a service friction is the strongest supported explanation for risk. Evidence suggests this because complaints_30d=1; comaint_text describes a recent transaction issue."
  }
}
```

### Akshay Basak (`C19549`)

- OK: `True`
- Shape errors: `[]`
- Simple output: Reason: UNKNOWN | Urgency: MEDIUM | Action: MONITOR | Why: Evidence is mixed or limited, so the cause remains uncertain.

Request:

```json
{
  "customer_id": "C19549",
  "customer_name": "Akshay Basak",
  "prediction_date": "2026-06-01",
  "snapshot_date": "2026-06-01",
  "target_month": "2026-07-01",
  "profile": {
    "tenure_months": 99,
    "customer_segment": "pension",
    "income_regularity": "regular",
    "products_count": 3,
    "has_credit_card": 1,
    "has_loan": 0
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 0,
      "balance_change_30d": 9.4762,
      "transaction_change_30d": 19.0173,
      "card_spend_change_30d": 4.1711,
      "app_login_change_30d": 26.5667,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -51.4072,
      "upi_share_of_spend": 0.3714,
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
      "days_since_last_transaction": 4,
      "balance_change_30d": 29.3477,
      "transaction_change_30d": -0.5338,
      "card_spend_change_30d": 1.0815,
      "app_login_change_30d": -3.3804,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -19.9784,
      "upi_share_of_spend": 0.4665,
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
      "days_since_last_transaction": 5,
      "balance_change_30d": 1.8878,
      "transaction_change_30d": -1.4398,
      "card_spend_change_30d": -14.8114,
      "app_login_change_30d": 9.7497,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": 31.7409,
      "upi_share_of_spend": 0.3303,
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
      "days_since_last_transaction": 4,
      "balance_change_30d": 6.0579,
      "transaction_change_30d": -17.1338,
      "card_spend_change_30d": 19.1177,
      "app_login_change_30d": -24.6862,
      "salary_missing_days": 2.0,
      "external_transfer_change_30d": -0.3718,
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
      "snapshot_date": "2026-05-01",
      "days_since_last_transaction": 2,
      "balance_change_30d": -2.7139,
      "transaction_change_30d": 9.0885,
      "card_spend_change_30d": -22.4706,
      "app_login_change_30d": -6.819,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": 8.4241,
      "upi_share_of_spend": 0.4437,
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
      "balance_change_30d": 5.4889,
      "transaction_change_30d": -14.1438,
      "card_spend_change_30d": 6.1239,
      "app_login_change_30d": 22.4674,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -2.5193,
      "upi_share_of_spend": 0.4276,
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
    "tenure_months": 99,
    "customer_segment": "pension",
    "income_regularity": "regular",
    "products_count": 3,
    "has_credit_card": 1,
    "has_loan": 0,
    "days_since_last_transaction": 1,
    "balance_change_30d": 5.4889,
    "transaction_change_30d": -14.1438,
    "card_spend_change_30d": 6.1239,
    "app_login_change_30d": 22.4674,
    "salary_missing_days": 0.0,
    "external_transfer_change_30d": -2.5193,
    "upi_share_of_spend": 0.4276,
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
      "tenure_months": 99,
      "age": 67,
      "customer_yearly_value": 23075.3957,
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
    "served_at": "2026-08-31T00:43:35",
    "elapsed_ms": 1793.93,
    "timings_ms": {
      "model1": 147.85,
      "model2": 1645.96
    },
    "customer_id": "C19549",
    "customer_name": "Akshay Basak",
    "snapshot_date": "2026-06-01"
  },
  "model1": {
    "churn_probability": 2.68,
    "raw_churn_probability": 24.85,
    "probability_mode": "sigmoid",
    "risk_score": 8.03,
    "churn_prediction": "No",
    "risk_level": "Low",
    "top_risk_factors": [
      {
        "factor": "external_transfer_change_30d_trend_6m",
        "value": 8.500979999999998,
        "message": "External transfers have increased.",
        "contribution": 0.035935793071985245
      },
      {
        "factor": "transaction_change_30d_trend_6m",
        "value": -4.360931428571427,
        "message": "Transaction activity has been falling across recent months.",
        "contribution": 0.02845783531665802
      },
      {
        "factor": "max_salary_missing_days_3m",
        "value": 2.0,
        "message": "Salary or pension was delayed recently.",
        "contribution": 0.01755123771727085
      },
      {
        "factor": "avg_app_login_change_30d_3m",
        "value": -3.012599999999999,
        "message": "App usage has been falling across recent months.",
        "contribution": 0.010454372502863407
      },
      {
        "factor": "latest_vs_avg_upi_share_of_spend_available_history",
        "value": 0.010749999999999982,
        "message": "A larger share of spending is happening through UPI.",
        "contribution": 0.010383608750998974
      }
    ]
  },
  "model2_input": {
    "customer_context": {
      "age": 67,
      "tenure_months": 99,
      "customer_segment": "pension",
      "income_regularity": "regular",
      "customer_yearly_value": 23075.3957,
      "products_count": 3,
      "has_credit_card": 1,
      "has_loan": 0
    },
    "behavior": {
      "days_since_last_transaction": 1,
      "balance_change_30d": 5.4889,
      "transaction_change_30d": -14.1438,
      "card_spend_change_30d": 6.1239,
      "app_login_change_30d": 22.4674,
      "salary_missing_days": 0,
      "external_transfer_change_30d": -2.5193,
      "upi_share_of_spend": 0.4276,
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
      "churn_probability": 0.0268,
      "churn_prediction": "No",
      "risk_level": "Low",
      "top_risk_factors": [
        {
          "factor": "external_transfer_change_30d_trend_6m",
          "value": 8.500979999999998
        },
        {
          "factor": "transaction_change_30d_trend_6m",
          "value": -4.360931428571427
        },
        {
          "factor": "max_salary_missing_days_3m",
          "value": 2.0
        },
        {
          "factor": "avg_app_login_change_30d_3m",
          "value": -3.012599999999999
        },
        {
          "factor": "vs_avg_upi_share_of_spend_available_history",
          "value": 0.010749999999999982
        }
      ]
    },
    "eligible_actions": [
      "MONITOR",
      "SERVICE_RECOVERY",
      "COMPLAINT_ESCALATION",
      "FEE_WAIVER_REVIEW",
      "RM_CALLBACK",
      "PRODUCT_REVIEW",
      "CARD_REVIEW",
      "LOAN_REVIEW",
      "RE_ENGAGEMENT",
      "FINANCIAL_GUIDANCE"
    ],
    "case_id": "C19549"
  },
  "model2": {
    "case_id": "C19549",
    "ok": true,
    "prediction": {
      "evidence": [
        "transaction_change_30d=-14.1",
        "external_transfer_change_30d=2.5"
      ],
      "primary_reason": "UNKNOWN",
      "reasoning_summary": "Evidence is mixed or limited, so the cause remains uncertain.",
      "recommended_action": "MONITOR",
      "secondary_reasons": [],
      "urgency": "MEDIUM"
    },
    "raw_text": "{\"evidence\":[\"transaction_change_30d=-14.1\",\"external_transfer_change_30d=2.5\"],\"primary_reason\":\"UNKNOWN\",\"reasoning_summary\":\"Evidence is mixed or limited, so the cause remains uncertain.\",\"recommended_action\":\"MONITOR\",\"secondary_reasons\":[],\"urgency\":\"MEDIUM\"}",
    "error": null,
    "latency_s": 1.6458,
    "simple_output": "Reason: UNKNOWN | Urgency: MEDIUM | Action: MONITOR | Why: Evidence is mixed or limited, so the cause remains uncertain."
  }
}
```
