# Devang Model 1 -> Model 2 API Test Results

- API URL: `http://127.0.0.1:8001`
- Created at: `2026-08-31T01:59:01`
- Customers tested: `20`
- Source CSV: `model_1_v2\data\customers.csv`
- Health OK: `True`
- Ollama model: `devang-model2-q4`
- Model 1 loaded: `True`

## Summary

| # | Customer | Model 1 risk | Prediction | Reason | Urgency | Action | OK | Seconds |
|---:|---|---:|---|---|---|---|---|---:|
| 1 | Ijaya Chahal (`C10848`) | 3.03 | No | UNKNOWN | LOW | MONITOR | yes | 10.43 |
| 2 | Amara Rana (`C11465`) | 41.65 | Yes | DIGITAL_FRICTION | MEDIUM | RE_ENGAGEMENT | yes | 12.36 |
| 3 | Ladli Ramakrishnan (`C11842`) | 2.4 | No | UNKNOWN | LOW | MONITOR | yes | 9.05 |
| 4 | Kevin Parmer (`C11964`) | 2.49 | No | UNKNOWN | LOW | MONITOR | yes | 8.71 |
| 5 | Indali Kala (`C12474`) | 2.1 | No | FEE_DISSATISFACTION | MEDIUM | FINANCIAL_GUIDANCE | yes | 7.43 |
| 6 | Ekaraj Raju (`C12629`) | 35.88 | Yes | FINANCIAL_STRESS | MEDIUM | FINANCIAL_GUIDANCE | yes | 9.14 |
| 7 | Udarsh Bath (`C12997`) | 2.39 | No | TEMPORARY_SEASONAL_CHANGE | LOW | RE_ENGAGEMENT | yes | 10.79 |
| 8 | Widisha Chatterjee (`C13116`) | 3.03 | No | UNKNOWN | LOW | MONITOR | yes | 7.52 |
| 9 | Jatin Purohit (`C13656`) | 42.39 | Yes | FINANCIAL_STRESS | MEDIUM | FINANCIAL_GUIDANCE | yes | 14.99 |
| 10 | Lopa Chandran (`C15140`) | 2.63 | No | UNKNOWN | LOW | MONITOR | yes | 9.66 |
| 11 | Kai Peri (`C15390`) | 2.67 | No | SERVICE_DISSATISFACTION | MEDIUM | SERVICE_RECOVERY | yes | 11.56 |
| 12 | Widisha Parmer (`C15968`) | 1.75 | No | FINANCIAL_STRESS | MEDIUM | FINANCIAL_GUIDANCE | yes | 11.64 |
| 13 | Nihal Bakshi (`C16055`) | 4.9 | No | FEE_DISSATISFACTION | MEDIUM | FEE_WAIVER_REVIEW | yes | 11.91 |
| 14 | Veer Mody (`C16114`) | 3.09 | No | UNKNOWN | LOW | MONITOR | yes | 7.82 |
| 15 | Nakul Iyengar (`C17377`) | 41.38 | Yes | SERVICE_DISSATISFACTION | MEDIUM | SERVICE_RECOVERY | yes | 11.33 |
| 16 | Jatin Buch (`C17417`) | 4.82 | No | DIGITAL_FRICTION | MEDIUM | MONITOR | yes | 7.18 |
| 17 | Girindra Brar (`C18347`) | 30.4 | Yes | SERVICE_DISSATISFACTION | HIGH | COMPLAINT_ESCALATION | yes | 4.87 |
| 18 | Ekanta Oommen (`C18523`) | 2.42 | No | FINANCIAL_STRESS | MEDIUM | PRODUCT_REVIEW | yes | 6.74 |
| 19 | Shivani Pathak (`C19078`) | 4.38 | No | UNKNOWN | LOW | MONITOR | yes | 8.51 |
| 20 | Yochana Pau (`C19645`) | 4.0 | No | UNKNOWN | LOW | MONITOR | yes | 8.77 |

## Details

### Ijaya Chahal (`C10848`)

- OK: `True`
- Shape errors: `[]`
- Simple output: Reason: UNKNOWN | Urgency: LOW | Action: MONITOR | Why: Complaint and resolution signals are mixed or weak; relationship strength is unclear.

Request:

```json
{
  "customer_id": "C10848",
  "customer_name": "Ijaya Chahal",
  "prediction_date": "2026-06-01",
  "snapshot_date": "2026-06-01",
  "target_month": "2026-07-01",
  "profile": {
    "tenure_months": 13,
    "customer_segment": "business",
    "income_regularity": "irregular",
    "products_count": 5,
    "has_credit_card": 1,
    "has_loan": 1
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 1,
      "balance_change_30d": 16.0749,
      "transaction_change_30d": 10.2486,
      "card_spend_change_30d": 18.4142,
      "app_login_change_30d": 11.3633,
      "salary_missing_days": null,
      "external_transfer_change_30d": -12.714,
      "upi_share_of_spend": 0.3524,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 23.2772,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-02-01",
      "days_since_last_transaction": 12,
      "balance_change_30d": 23.5974,
      "transaction_change_30d": 13.0573,
      "card_spend_change_30d": 20.0908,
      "app_login_change_30d": 11.87,
      "salary_missing_days": null,
      "external_transfer_change_30d": -11.464,
      "upi_share_of_spend": 0.5159,
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
      "balance_change_30d": 4.7988,
      "transaction_change_30d": -5.8818,
      "card_spend_change_30d": 0.2148,
      "app_login_change_30d": 36.6357,
      "salary_missing_days": null,
      "external_transfer_change_30d": -43.9684,
      "upi_share_of_spend": 0.5017,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 0,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 0.0,
      "emi_bounce_30d": 1
    },
    {
      "snapshot_date": "2026-04-01",
      "days_since_last_transaction": 7,
      "balance_change_30d": -14.2831,
      "transaction_change_30d": 15.8706,
      "card_spend_change_30d": 25.2924,
      "app_login_change_30d": 26.2424,
      "salary_missing_days": null,
      "external_transfer_change_30d": -0.6017,
      "upi_share_of_spend": 0.3892,
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
      "days_since_last_transaction": 1,
      "balance_change_30d": -1.0656,
      "transaction_change_30d": 29.4881,
      "card_spend_change_30d": -13.8062,
      "app_login_change_30d": 11.9878,
      "salary_missing_days": null,
      "external_transfer_change_30d": -22.1657,
      "upi_share_of_spend": 0.411,
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
      "days_since_last_transaction": 7,
      "balance_change_30d": 10.3588,
      "transaction_change_30d": -5.7746,
      "card_spend_change_30d": 1.409,
      "app_login_change_30d": 27.5919,
      "salary_missing_days": null,
      "external_transfer_change_30d": -24.4977,
      "upi_share_of_spend": 0.5285,
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
    "tenure_months": 13,
    "customer_segment": "business",
    "income_regularity": "irregular",
    "products_count": 5,
    "has_credit_card": 1,
    "has_loan": 1,
    "days_since_last_transaction": 7,
    "balance_change_30d": 10.3588,
    "transaction_change_30d": -5.7746,
    "card_spend_change_30d": 1.409,
    "app_login_change_30d": 27.5919,
    "salary_missing_days": null,
    "external_transfer_change_30d": -24.4977,
    "upi_share_of_spend": 0.5285,
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
      "tenure_months": 13,
      "age": 39,
      "customer_yearly_value": 38084.1655,
      "products_count": 5,
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
  "meta": {
    "endpoint": "/predict/both",
    "served_at": "2026-08-31T01:56:00",
    "elapsed_ms": 10401.0,
    "timings_ms": {
      "model1": 71.03,
      "model2": 10329.8
    },
    "customer_id": "C10848",
    "customer_name": "Ijaya Chahal",
    "snapshot_date": "2026-06-01"
  },
  "model1": {
    "churn_probability": 3.03,
    "raw_churn_probability": 27.55,
    "probability_mode": "sigmoid",
    "risk_score": 9.08,
    "churn_prediction": "No",
    "risk_level": "Low",
    "top_risk_factors": [
      {
        "factor": "latest_vs_avg_upi_share_of_spend_available_history",
        "value": 0.07871666666666671,
        "message": "A larger share of spending is happening through UPI.",
        "contribution": 0.15070407092571259
      },
      {
        "factor": "transaction_change_30d_trend_6m",
        "value": -0.25917714285714183,
        "message": "Transaction activity has been falling across recent months.",
        "contribution": 0.027725128456950188
      },
      {
        "factor": "count_external_transfer_rise_6m",
        "value": 0,
        "message": "This signal increased churn risk.",
        "contribution": 0.019578102976083755
      },
      {
        "factor": "latest_upi_share_of_spend",
        "value": 0.5285,
        "message": "A larger share of spending is happening through UPI.",
        "contribution": 0.014847230166196823
      },
      {
        "factor": "app_login_change_30d_trend_6m",
        "value": 2.0315171428571412,
        "message": "This signal increased churn risk.",
        "contribution": 0.008668160997331142
      }
    ]
  },
  "model2_input": {
    "customer_context": {
      "age": 39,
      "tenure_months": 13,
      "customer_segment": "business",
      "income_regularity": "irregular",
      "customer_yearly_value": 38084.1655,
      "products_count": 5,
      "has_credit_card": 1,
      "has_loan": 1
    },
    "behavior": {
      "days_since_last_transaction": 7,
      "balance_change_30d": 10.3588,
      "transaction_change_30d": -5.7746,
      "card_spend_change_30d": 1.409,
      "app_login_change_30d": 27.5919,
      "salary_missing_days": null,
      "external_transfer_change_30d": -24.4977,
      "upi_share_of_spend": 0.5285,
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
      "churn_probability": 0.0303,
      "churn_prediction": "No",
      "risk_level": "Low",
      "top_risk_factors": [
        {
          "factor": "upi_share_of_spend",
          "value": 0.5285
        },
        {
          "factor": "transaction_change_30d",
          "value": -5.7746
        },
        {
          "factor": "app_login_change_30d",
          "value": 27.5919
        }
      ]
    },
    "eligible_actions": [
      "SERVICE_RECOVERY",
      "RE_ENGAGEMENT",
      "MONITOR"
    ],
    "case_id": "C10848"
  },
  "model2": {
    "case_id": "C10848",
    "ok": true,
    "prediction": {
      "evidence": [
        "complaints_30d=0",
        "unresolved_complaints=0",
        "avg_resolution_time_hrs=0.0"
      ],
      "primary_reason": "UNKNOWN",
      "reasoning_summary": "Complaint and resolution signals are mixed or weak; relationship strength is unclear.",
      "recommended_action": "MONITOR",
      "secondary_reasons": [],
      "urgency": "LOW"
    },
    "warnings": [
      "evidence: 'complaints_30d=0' cites a zero/null value, which is not evidence; remove it",
      "evidence: 'unresolved_complaints=0' cites a zero/null value, which is not evidence; remove it",
      "evidence: 'avg_resolution_time_hrs=0.0' cites a zero/null value, which is not evidence; remove it"
    ],
    "raw_text": "{\"evidence\":[\"transaction_change_30d=-5.8\",\"complaints_30d=0\"],\"primary_reason\":\"DIGITAL_FRICTION\",\"reasoning_summary\":\"Digital friction is supported by transaction_change_30d=-5.8 and complaints_30d=0. DIGITAL_FRICTION fits because complaints_30d=0 and transaction_change_30d=-5.8 suggest a digital experience problem without clear escalation-level evidence.\",\"recommended_action\":\"RE_ENGAGEMENT\",\"secondary_reasons\":[],\"urgency\":\"MEDIUM\"}",
    "error": null,
    "latency_s": 10.3295,
    "simple_output": "Reason: UNKNOWN | Urgency: LOW | Action: MONITOR | Why: Complaint and resolution signals are mixed or weak; relationship strength is unclear."
  }
}
```

### Amara Rana (`C11465`)

- OK: `True`
- Shape errors: `[]`
- Simple output: Reason: DIGITAL_FRICTION | Urgency: MEDIUM | Action: RE_ENGAGEMENT | Why: Digital friction is the clearest signal here because complaints_30d=0 and avg_resolution_time_hrs=0.0 suggest a digital experience problem without clear escalation-level evidence.

Request:

```json
{
  "customer_id": "C11465",
  "customer_name": "Amara Rana",
  "prediction_date": "2026-06-01",
  "snapshot_date": "2026-06-01",
  "target_month": "2026-07-01",
  "profile": {
    "tenure_months": 98,
    "customer_segment": "business",
    "income_regularity": "irregular",
    "products_count": 2,
    "has_credit_card": 1,
    "has_loan": 0
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 1,
      "balance_change_30d": 21.0695,
      "transaction_change_30d": -22.4397,
      "card_spend_change_30d": -4.4002,
      "app_login_change_30d": 19.6577,
      "salary_missing_days": null,
      "external_transfer_change_30d": -8.9191,
      "upi_share_of_spend": 0.296,
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
      "balance_change_30d": -8.3063,
      "transaction_change_30d": 3.6052,
      "card_spend_change_30d": 8.2126,
      "app_login_change_30d": -17.4477,
      "salary_missing_days": null,
      "external_transfer_change_30d": 33.9903,
      "upi_share_of_spend": 0.3018,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 8.0797,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-03-01",
      "days_since_last_transaction": 12,
      "balance_change_30d": -15.4904,
      "transaction_change_30d": -4.7693,
      "card_spend_change_30d": -27.5476,
      "app_login_change_30d": -11.7465,
      "salary_missing_days": null,
      "external_transfer_change_30d": -5.8098,
      "upi_share_of_spend": 0.4585,
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
      "days_since_last_transaction": 21,
      "balance_change_30d": -12.2016,
      "transaction_change_30d": -45.1629,
      "card_spend_change_30d": -21.1059,
      "app_login_change_30d": -19.9134,
      "salary_missing_days": null,
      "external_transfer_change_30d": 59.9603,
      "upi_share_of_spend": 0.5632,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 2,
      "unresolved_complaints": 1,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 50.3618,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-05-01",
      "days_since_last_transaction": 13,
      "balance_change_30d": -34.5488,
      "transaction_change_30d": -31.4178,
      "card_spend_change_30d": -16.2272,
      "app_login_change_30d": -16.9717,
      "salary_missing_days": null,
      "external_transfer_change_30d": 48.0805,
      "upi_share_of_spend": 0.5548,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 2,
      "unresolved_complaints": 1,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 32.1827,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-06-01",
      "days_since_last_transaction": 21,
      "balance_change_30d": -65.8238,
      "transaction_change_30d": -58.6328,
      "card_spend_change_30d": -48.8467,
      "app_login_change_30d": -33.4329,
      "salary_missing_days": null,
      "external_transfer_change_30d": 71.0152,
      "upi_share_of_spend": 0.6433,
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
    "tenure_months": 98,
    "customer_segment": "business",
    "income_regularity": "irregular",
    "products_count": 2,
    "has_credit_card": 1,
    "has_loan": 0,
    "days_since_last_transaction": 21,
    "balance_change_30d": -65.8238,
    "transaction_change_30d": -58.6328,
    "card_spend_change_30d": -48.8467,
    "app_login_change_30d": -33.4329,
    "salary_missing_days": null,
    "external_transfer_change_30d": 71.0152,
    "upi_share_of_spend": 0.6433,
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
      "tenure_months": 98,
      "age": 54,
      "customer_yearly_value": 161887.056,
      "products_count": 2,
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
    "served_at": "2026-08-31T01:56:13",
    "elapsed_ms": 12344.12,
    "timings_ms": {
      "model1": 372.33,
      "model2": 11971.57
    },
    "customer_id": "C11465",
    "customer_name": "Amara Rana",
    "snapshot_date": "2026-06-01"
  },
  "model1": {
    "churn_probability": 41.65,
    "raw_churn_probability": 94.77,
    "probability_mode": "sigmoid",
    "risk_score": 78.12,
    "churn_prediction": "Yes",
    "risk_level": "High",
    "top_risk_factors": [
      {
        "factor": "latest_days_since_last_transaction",
        "value": 21,
        "message": "Customer has gone longer without transacting.",
        "contribution": 0.6509332060813904
      },
      {
        "factor": "latest_transaction_change_30d",
        "value": -58.6328,
        "message": "Transaction activity has been falling across recent months.",
        "contribution": 0.4655364453792572
      },
      {
        "factor": "latest_vs_avg_upi_share_of_spend_available_history",
        "value": 0.17370000000000002,
        "message": "A larger share of spending is happening through UPI.",
        "contribution": 0.2642871141433716
      },
      {
        "factor": "latest_balance_change_30d",
        "value": -65.8238,
        "message": "Balance has been falling across recent months.",
        "contribution": 0.22491709887981415
      },
      {
        "factor": "latest_card_spend_change_30d",
        "value": -48.8467,
        "message": "Card spending has been falling across recent months.",
        "contribution": 0.18553967773914337
      }
    ]
  },
  "model2_input": {
    "customer_context": {
      "age": 54,
      "tenure_months": 98,
      "customer_segment": "business",
      "income_regularity": "irregular",
      "customer_yearly_value": 161887.056,
      "products_count": 2,
      "has_credit_card": 1,
      "has_loan": 0
    },
    "behavior": {
      "days_since_last_transaction": 21,
      "balance_change_30d": -65.8238,
      "transaction_change_30d": -58.6328,
      "card_spend_change_30d": -48.8467,
      "app_login_change_30d": -33.4329,
      "salary_missing_days": null,
      "external_transfer_change_30d": 71.0152,
      "upi_share_of_spend": 0.6433,
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
      "churn_probability": 0.4165,
      "churn_prediction": "Yes",
      "risk_level": "High",
      "top_risk_factors": [
        {
          "factor": "days_since_last_transaction",
          "value": 21
        },
        {
          "factor": "transaction_change_30d",
          "value": -58.6328
        },
        {
          "factor": "upi_share_of_spend",
          "value": 0.6433
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
    "case_id": "C11465"
  },
  "model2": {
    "case_id": "C11465",
    "ok": true,
    "prediction": {
      "evidence": [
        "complaints_30d=0",
        "unresolved_complaints=0",
        "avg_resolution_time_hrs=0.0",
        "app_login_change_30d=-33.4",
        "transaction_change_30d=-58.6",
        "card_spend_change_30d=-48.8",
        "emi_bounce_30d=0",
        "external_transfer_change_30d=71.0"
      ],
      "primary_reason": "DIGITAL_FRICTION",
      "reasoning_summary": "Digital friction is the clearest signal here because complaints_30d=0 and avg_resolution_time_hrs=0.0 suggest a digital experience problem without clear escalation-level evidence.",
      "recommended_action": "RE_ENGAGEMENT",
      "secondary_reasons": [],
      "urgency": "MEDIUM"
    },
    "warnings": [
      "evidence: 'complaints_30d=0' cites a zero/null value, which is not evidence; remove it",
      "evidence: 'unresolved_complaints=0' cites a zero/null value, which is not evidence; remove it",
      "evidence: 'avg_resolution_time_hrs=0.0' cites a zero/null value, which is not evidence; remove it",
      "evidence: 'emi_bounce_30d=0' cites a zero/null value, which is not evidence; remove it",
      "reasoning_summary: describes COMPLAINT_ESCALATION but recommended_action is RE_ENGAGEMENT; rewrite the summary around the action you chose"
    ],
    "raw_text": "{\"evidence\":[\"complaints_30d=0\",\"unresolved_complaints=0\",\"avg_resolution_time_hrs=0.0\"],\"primary_reason\":\"SERVICE_DISSATISFACTION\",\"reasoning_summary\":\"Complaint and service friction signals are mixed or weak; SERVICE_RECOVERY fits because complaints_30d=0 and unresolved_complaints=0 suggest a service recovery fit.\",\"recommended_action\":\"SERVICE_RECOVERY\",\"secondary_reasons\":[],\"urgency\":\"MEDIUM\"}",
    "error": null,
    "latency_s": 11.9712,
    "simple_output": "Reason: DIGITAL_FRICTION | Urgency: MEDIUM | Action: RE_ENGAGEMENT | Why: Digital friction is the clearest signal here because complaints_30d=0 and avg_resolution_time_hrs=0.0 suggest a digital experience problem without clear escalation-level evidence."
  }
}
```

### Ladli Ramakrishnan (`C11842`)

- OK: `True`
- Shape errors: `[]`
- Simple output: Reason: UNKNOWN | Urgency: LOW | Action: MONITOR | Why: Complaint and resolution signals are mixed or weak; evidence is genuinely unclear.

Request:

```json
{
  "customer_id": "C11842",
  "customer_name": "Ladli Ramakrishnan",
  "prediction_date": "2026-06-01",
  "snapshot_date": "2026-06-01",
  "target_month": "2026-07-01",
  "profile": {
    "tenure_months": 26,
    "customer_segment": "vendor",
    "income_regularity": "irregular",
    "products_count": 1,
    "has_credit_card": 0,
    "has_loan": 0
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 6,
      "balance_change_30d": 28.2685,
      "transaction_change_30d": 12.3917,
      "card_spend_change_30d": 12.398,
      "app_login_change_30d": 24.5259,
      "salary_missing_days": null,
      "external_transfer_change_30d": 32.3361,
      "upi_share_of_spend": 0.3769,
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
      "days_since_last_transaction": 5,
      "balance_change_30d": 23.6346,
      "transaction_change_30d": 24.6036,
      "card_spend_change_30d": 44.1562,
      "app_login_change_30d": 32.0839,
      "salary_missing_days": null,
      "external_transfer_change_30d": -32.0426,
      "upi_share_of_spend": 0.4534,
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
      "days_since_last_transaction": 0,
      "balance_change_30d": 26.1907,
      "transaction_change_30d": -4.49,
      "card_spend_change_30d": 23.0744,
      "app_login_change_30d": 55.838,
      "salary_missing_days": null,
      "external_transfer_change_30d": -19.3602,
      "upi_share_of_spend": 0.2854,
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
      "days_since_last_transaction": 7,
      "balance_change_30d": -5.4012,
      "transaction_change_30d": 23.2479,
      "card_spend_change_30d": -8.5101,
      "app_login_change_30d": 9.0756,
      "salary_missing_days": null,
      "external_transfer_change_30d": 12.3439,
      "upi_share_of_spend": 0.4971,
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
      "balance_change_30d": 20.5138,
      "transaction_change_30d": 22.7656,
      "card_spend_change_30d": 38.4682,
      "app_login_change_30d": -12.3719,
      "salary_missing_days": null,
      "external_transfer_change_30d": -22.4592,
      "upi_share_of_spend": 0.4529,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 2,
      "unresolved_complaints": 1,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 22.5774,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-06-01",
      "days_since_last_transaction": 3,
      "balance_change_30d": 29.4999,
      "transaction_change_30d": 33.808,
      "card_spend_change_30d": 49.2863,
      "app_login_change_30d": 9.4005,
      "salary_missing_days": null,
      "external_transfer_change_30d": 0.1657,
      "upi_share_of_spend": 0.4731,
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
    "tenure_months": 26,
    "customer_segment": "vendor",
    "income_regularity": "irregular",
    "products_count": 1,
    "has_credit_card": 0,
    "has_loan": 0,
    "days_since_last_transaction": 3,
    "balance_change_30d": 29.4999,
    "transaction_change_30d": 33.808,
    "card_spend_change_30d": 49.2863,
    "app_login_change_30d": 9.4005,
    "salary_missing_days": null,
    "external_transfer_change_30d": 0.1657,
    "upi_share_of_spend": 0.4731,
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
      "segment": "vendor",
      "income_regularity": "irregular",
      "tenure_months": 26,
      "age": 37,
      "customer_yearly_value": 24982.195,
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
    "served_at": "2026-08-31T01:56:22",
    "elapsed_ms": 9043.93,
    "timings_ms": {
      "model1": 291.94,
      "model2": 8751.69
    },
    "customer_id": "C11842",
    "customer_name": "Ladli Ramakrishnan",
    "snapshot_date": "2026-06-01"
  },
  "model1": {
    "churn_probability": 2.4,
    "raw_churn_probability": 22.48,
    "probability_mode": "sigmoid",
    "risk_score": 7.21,
    "churn_prediction": "No",
    "risk_level": "Low",
    "top_risk_factors": [
      {
        "factor": "latest_vs_avg_upi_share_of_spend_available_history",
        "value": 0.04996666666666666,
        "message": "A larger share of spending is happening through UPI.",
        "contribution": 0.18109440803527832
      },
      {
        "factor": "avg_transaction_change_30d_6m",
        "value": 18.72113333333333,
        "message": "This signal increased churn risk.",
        "contribution": 0.0347573347389698
      },
      {
        "factor": "latest_card_spend_change_30d",
        "value": 49.2863,
        "message": "This signal increased churn risk.",
        "contribution": 0.018017582595348358
      },
      {
        "factor": "latest_upi_share_of_spend",
        "value": 0.4731,
        "message": "A larger share of spending is happening through UPI.",
        "contribution": 0.015296641737222672
      },
      {
        "factor": "card_spend_change_30d_trend_6m",
        "value": 3.879799999999998,
        "message": "This signal increased churn risk.",
        "contribution": 0.014081936329603195
      }
    ]
  },
  "model2_input": {
    "customer_context": {
      "age": 37,
      "tenure_months": 26,
      "customer_segment": "vendor",
      "income_regularity": "irregular",
      "customer_yearly_value": 24982.195,
      "products_count": 1,
      "has_credit_card": 0,
      "has_loan": 0
    },
    "behavior": {
      "days_since_last_transaction": 3,
      "balance_change_30d": 29.4999,
      "transaction_change_30d": 33.808,
      "card_spend_change_30d": 49.2863,
      "app_login_change_30d": 9.4005,
      "salary_missing_days": null,
      "external_transfer_change_30d": 0.1657,
      "upi_share_of_spend": 0.4731,
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
      "churn_probability": 0.024,
      "churn_prediction": "No",
      "risk_level": "Low",
      "top_risk_factors": [
        {
          "factor": "upi_share_of_spend",
          "value": 0.4731
        },
        {
          "factor": "transaction_change_30d",
          "value": 33.808
        },
        {
          "factor": "card_spend_change_30d",
          "value": 49.2863
        }
      ]
    },
    "eligible_actions": [
      "SERVICE_RECOVERY",
      "RE_ENGAGEMENT",
      "MONITOR"
    ],
    "case_id": "C11842"
  },
  "model2": {
    "case_id": "C11842",
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
    "raw_text": "{\"evidence\":[\"complaints_30d=0\",\"unresolved_complaints=0\",\"avg_resolution_time_hrs=0.0\"],\"primary_reason\":\"DIGITAL_FRICTION\",\"reasoning_summary\":\"Digital friction is the strongest supported signal here because complaints_30d=0 and unresolved_complaints=0 cite a mix of absence and low-level digital-service friction without a clearer cause.\",\"recommended_action\":\"RE_ENGAGEMENT\",\"secondary_reasons\":[],\"urgency\":\"MEDIUM\"}",
    "error": null,
    "latency_s": 8.7515,
    "simple_output": "Reason: UNKNOWN | Urgency: LOW | Action: MONITOR | Why: Complaint and resolution signals are mixed or weak; evidence is genuinely unclear."
  }
}
```

### Kevin Parmer (`C11964`)

- OK: `True`
- Shape errors: `[]`
- Simple output: Reason: UNKNOWN | Urgency: LOW | Action: MONITOR | Why: Complaint and resolution signals are mixed or weak; relationship strength is uncertain.

Request:

```json
{
  "customer_id": "C11964",
  "customer_name": "Kevin Parmer",
  "prediction_date": "2026-06-01",
  "snapshot_date": "2026-06-01",
  "target_month": "2026-07-01",
  "profile": {
    "tenure_months": 118,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 2,
    "has_credit_card": 1,
    "has_loan": 0
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 8,
      "balance_change_30d": -7.4056,
      "transaction_change_30d": -10.6249,
      "card_spend_change_30d": -6.5614,
      "app_login_change_30d": 17.6754,
      "salary_missing_days": 1.0,
      "external_transfer_change_30d": -4.3703,
      "upi_share_of_spend": 0.3265,
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
      "days_since_last_transaction": 0,
      "balance_change_30d": 1.9217,
      "transaction_change_30d": -6.1666,
      "card_spend_change_30d": -5.9601,
      "app_login_change_30d": 14.6137,
      "salary_missing_days": 1.0,
      "external_transfer_change_30d": -6.4344,
      "upi_share_of_spend": 0.1817,
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
      "days_since_last_transaction": 14,
      "balance_change_30d": -10.8153,
      "transaction_change_30d": -19.8168,
      "card_spend_change_30d": -38.5238,
      "app_login_change_30d": 13.2675,
      "salary_missing_days": 6.0,
      "external_transfer_change_30d": 1.9071,
      "upi_share_of_spend": 0.3744,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 2,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 2,
      "avg_resolution_time_hrs": 16.1415,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-04-01",
      "days_since_last_transaction": 3,
      "balance_change_30d": 24.9425,
      "transaction_change_30d": 2.7154,
      "card_spend_change_30d": -4.9761,
      "app_login_change_30d": -15.2831,
      "salary_missing_days": 4.0,
      "external_transfer_change_30d": 57.4708,
      "upi_share_of_spend": 0.4092,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 4.7165,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-05-01",
      "days_since_last_transaction": 6,
      "balance_change_30d": 19.4285,
      "transaction_change_30d": 3.1107,
      "card_spend_change_30d": -19.8827,
      "app_login_change_30d": 10.5605,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": 16.3096,
      "upi_share_of_spend": 0.3806,
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
      "balance_change_30d": 13.1741,
      "transaction_change_30d": 18.814,
      "card_spend_change_30d": 45.5991,
      "app_login_change_30d": 19.6662,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": 9.3014,
      "upi_share_of_spend": 0.3618,
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
    "tenure_months": 118,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 2,
    "has_credit_card": 1,
    "has_loan": 0,
    "days_since_last_transaction": 6,
    "balance_change_30d": 13.1741,
    "transaction_change_30d": 18.814,
    "card_spend_change_30d": 45.5991,
    "app_login_change_30d": 19.6662,
    "salary_missing_days": 0.0,
    "external_transfer_change_30d": 9.3014,
    "upi_share_of_spend": 0.3618,
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
      "tenure_months": 118,
      "age": 37,
      "customer_yearly_value": 35918.9471,
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
    "served_at": "2026-08-31T01:56:31",
    "elapsed_ms": 8699.82,
    "timings_ms": {
      "model1": 230.33,
      "model2": 8469.14
    },
    "customer_id": "C11964",
    "customer_name": "Kevin Parmer",
    "snapshot_date": "2026-06-01"
  },
  "model1": {
    "churn_probability": 2.49,
    "raw_churn_probability": 23.27,
    "probability_mode": "sigmoid",
    "risk_score": 7.48,
    "churn_prediction": "No",
    "risk_level": "Low",
    "top_risk_factors": [
      {
        "factor": "latest_vs_avg_card_spend_change_30d_available_history",
        "value": 50.64993333333334,
        "message": "This signal increased churn risk.",
        "contribution": 0.07590318471193314
      },
      {
        "factor": "external_transfer_change_30d_trend_6m",
        "value": 5.490119999999999,
        "message": "External transfers have increased.",
        "contribution": 0.03471753001213074
      },
      {
        "factor": "card_spend_change_30d_trend_6m",
        "value": 7.216639999999996,
        "message": "This signal increased churn risk.",
        "contribution": 0.03216816484928131
      },
      {
        "factor": "latest_vs_avg_upi_share_of_spend_available_history",
        "value": 0.022766666666666657,
        "message": "A larger share of spending is happening through UPI.",
        "contribution": 0.023562774062156677
      },
      {
        "factor": "sum_products_dropped_90d_6m",
        "value": 2.0,
        "message": "Customer has dropped products recently.",
        "contribution": 0.006215376779437065
      }
    ]
  },
  "model2_input": {
    "customer_context": {
      "age": 37,
      "tenure_months": 118,
      "customer_segment": "salary",
      "income_regularity": "regular",
      "customer_yearly_value": 35918.9471,
      "products_count": 2,
      "has_credit_card": 1,
      "has_loan": 0
    },
    "behavior": {
      "days_since_last_transaction": 6,
      "balance_change_30d": 13.1741,
      "transaction_change_30d": 18.814,
      "card_spend_change_30d": 45.5991,
      "app_login_change_30d": 19.6662,
      "salary_missing_days": 0,
      "external_transfer_change_30d": 9.3014,
      "upi_share_of_spend": 0.3618,
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
      "churn_probability": 0.0249,
      "churn_prediction": "No",
      "risk_level": "Low",
      "top_risk_factors": [
        {
          "factor": "card_spend_change_30d",
          "value": 45.5991
        },
        {
          "factor": "external_transfer_change_30d",
          "value": 9.3014
        },
        {
          "factor": "upi_share_of_spend",
          "value": 0.3618
        }
      ]
    },
    "eligible_actions": [
      "RE_ENGAGEMENT",
      "PRODUCT_REVIEW",
      "MONITOR"
    ],
    "case_id": "C11964"
  },
  "model2": {
    "case_id": "C11964",
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
    "raw_text": "{\"evidence\":[\"complaints_30d=0\",\"unresolved_complaints=0\",\"avg_resolution_time_hrs=0.0\"],\"primary_reason\":\"LOW_ENGAGEMENT\",\"reasoning_summary\":\"Days_since_last_transaction=6 and transaction_change_30d=18.8 suggest this because complaint_text is null.\",\"recommended_action\":\"RE_ENGAGEMENT\",\"secondary_reasons\":[],\"urgency\":\"MEDIUM\"}",
    "error": null,
    "latency_s": 8.4687,
    "simple_output": "Reason: UNKNOWN | Urgency: LOW | Action: MONITOR | Why: Complaint and resolution signals are mixed or weak; relationship strength is uncertain."
  }
}
```

### Indali Kala (`C12474`)

- OK: `True`
- Shape errors: `[]`
- Simple output: Reason: FEE_DISSATISFACTION | Urgency: MEDIUM | Action: FINANCIAL_GUIDANCE | Why: Complaint_text mentions fees or charges, and evidence suggests dissatisfaction with fees or charges. FEE_DISSATISFACTION fits because complaints_30d=1 and external_transfer_change_30d=13.3 suggest fees or charge-related issue.

Request:

```json
{
  "customer_id": "C12474",
  "customer_name": "Indali Kala",
  "prediction_date": "2026-06-01",
  "snapshot_date": "2026-06-01",
  "target_month": "2026-07-01",
  "profile": {
    "tenure_months": 223,
    "customer_segment": "pension",
    "income_regularity": "regular",
    "products_count": 2,
    "has_credit_card": 1,
    "has_loan": 0
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 4,
      "balance_change_30d": 18.1376,
      "transaction_change_30d": -0.8988,
      "card_spend_change_30d": 4.0339,
      "app_login_change_30d": -39.0297,
      "salary_missing_days": 2.0,
      "external_transfer_change_30d": 0.5427,
      "upi_share_of_spend": 0.3453,
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
      "days_since_last_transaction": 0,
      "balance_change_30d": 25.9032,
      "transaction_change_30d": 11.1745,
      "card_spend_change_30d": -11.5086,
      "app_login_change_30d": 9.6981,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": 7.1834,
      "upi_share_of_spend": 0.3364,
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
      "balance_change_30d": 17.1489,
      "transaction_change_30d": -5.5055,
      "card_spend_change_30d": 35.5869,
      "app_login_change_30d": 22.4685,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -31.1012,
      "upi_share_of_spend": 0.4081,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 5.8359,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-04-01",
      "days_since_last_transaction": 0,
      "balance_change_30d": 13.4706,
      "transaction_change_30d": 25.6178,
      "card_spend_change_30d": 41.0255,
      "app_login_change_30d": 0.8567,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": 4.3093,
      "upi_share_of_spend": 0.2872,
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
      "days_since_last_transaction": 1,
      "balance_change_30d": -1.9644,
      "transaction_change_30d": -5.939,
      "card_spend_change_30d": 25.8199,
      "app_login_change_30d": 23.9399,
      "salary_missing_days": 1.0,
      "external_transfer_change_30d": 12.2989,
      "upi_share_of_spend": 0.3543,
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
      "balance_change_30d": 14.4554,
      "transaction_change_30d": -1.8765,
      "card_spend_change_30d": 39.5798,
      "app_login_change_30d": -11.8165,
      "salary_missing_days": 1.0,
      "external_transfer_change_30d": 13.3309,
      "upi_share_of_spend": 0.299,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 2,
      "avg_resolution_time_hrs": 17.615,
      "emi_bounce_30d": 0
    }
  ],
  "customer": {
    "tenure_months": 223,
    "customer_segment": "pension",
    "income_regularity": "regular",
    "products_count": 2,
    "has_credit_card": 1,
    "has_loan": 0,
    "days_since_last_transaction": 0,
    "balance_change_30d": 14.4554,
    "transaction_change_30d": -1.8765,
    "card_spend_change_30d": 39.5798,
    "app_login_change_30d": -11.8165,
    "salary_missing_days": 1.0,
    "external_transfer_change_30d": 13.3309,
    "upi_share_of_spend": 0.299,
    "fd_maturing_in_30d": 0,
    "products_dropped_90d": 0,
    "complaints_30d": 1,
    "unresolved_complaints": 0,
    "failed_transactions_30d": 2,
    "avg_resolution_time_hrs": 17.615,
    "emi_bounce_30d": 0
  },
  "extra_context": {
    "customer_profile": {
      "segment": "pension",
      "income_regularity": "regular",
      "tenure_months": 223,
      "age": 62,
      "customer_yearly_value": 15406.9722,
      "products_count": 2,
      "has_credit_card": 1,
      "has_loan": 0,
      "value_tier": "low"
    },
    "recent_complaint_text": "Insurance premium debited from my account which I never authorised."
  }
}
```

Response:

```json
{
  "meta": {
    "endpoint": "/predict/both",
    "served_at": "2026-08-31T01:56:38",
    "elapsed_ms": 7420.66,
    "timings_ms": {
      "model1": 230.8,
      "model2": 7189.6
    },
    "customer_id": "C12474",
    "customer_name": "Indali Kala",
    "snapshot_date": "2026-06-01"
  },
  "model1": {
    "churn_probability": 2.1,
    "raw_churn_probability": 19.49,
    "probability_mode": "sigmoid",
    "risk_score": 6.3,
    "churn_prediction": "No",
    "risk_level": "Low",
    "top_risk_factors": [
      {
        "factor": "sum_fd_maturing_in_30d_3m",
        "value": 1.0,
        "message": "Customer has a fixed deposit maturing soon.",
        "contribution": 0.07140255719423294
      },
      {
        "factor": "external_transfer_change_30d_trend_6m",
        "value": 3.2770857142857137,
        "message": "External transfers have increased.",
        "contribution": 0.02647525630891323
      },
      {
        "factor": "card_spend_change_30d_trend_6m",
        "value": 8.432959999999996,
        "message": "This signal increased churn risk.",
        "contribution": 0.025715261697769165
      },
      {
        "factor": "count_external_transfer_rise_6m",
        "value": 0,
        "message": "This signal increased churn risk.",
        "contribution": 0.014660312794148922
      },
      {
        "factor": "max_salary_missing_days_6m",
        "value": 2.0,
        "message": "Salary or pension was delayed recently.",
        "contribution": 0.009840010665357113
      }
    ]
  },
  "model2_input": {
    "customer_context": {
      "age": 62,
      "tenure_months": 223,
      "customer_segment": "pension",
      "income_regularity": "regular",
      "customer_yearly_value": 15406.9722,
      "products_count": 2,
      "has_credit_card": 1,
      "has_loan": 0
    },
    "behavior": {
      "days_since_last_transaction": 0,
      "balance_change_30d": 14.4554,
      "transaction_change_30d": -1.8765,
      "card_spend_change_30d": 39.5798,
      "app_login_change_30d": -11.8165,
      "salary_missing_days": 1,
      "external_transfer_change_30d": 13.3309,
      "upi_share_of_spend": 0.299,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "emi_bounce_30d": 0
    },
    "service_evidence": {
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 2,
      "avg_resolution_time_hrs": 17.615,
      "complaint_text": "Insurance premium debited from my account which I never authorised."
    },
    "model1": {
      "churn_probability": 0.021,
      "churn_prediction": "No",
      "risk_level": "Low",
      "top_risk_factors": [
        {
          "factor": "fd_maturing_in_30d",
          "value": 0
        },
        {
          "factor": "external_transfer_change_30d",
          "value": 13.3309
        },
        {
          "factor": "card_spend_change_30d",
          "value": 39.5798
        }
      ]
    },
    "eligible_actions": [
      "FINANCIAL_GUIDANCE",
      "SERVICE_RECOVERY",
      "MONITOR"
    ],
    "case_id": "C12474"
  },
  "model2": {
    "case_id": "C12474",
    "ok": true,
    "prediction": {
      "evidence": [
        "complaints_30d=1",
        "external_transfer_change_30d=13.3",
        "card_spend_change_30d=39.6"
      ],
      "primary_reason": "FEE_DISSATISFACTION",
      "reasoning_summary": "Complaint_text mentions fees or charges, and evidence suggests dissatisfaction with fees or charges. FEE_DISSATISFACTION fits because complaints_30d=1 and external_transfer_change_30d=13.3 suggest fees or charge-related issue.",
      "recommended_action": "FINANCIAL_GUIDANCE",
      "secondary_reasons": [],
      "urgency": "MEDIUM"
    },
    "warnings": [],
    "raw_text": "{\"evidence\":[\"complaints_30d=1\",\"external_transfer_change_30d=13.3\",\"card_spend_change_30d=39.6\"],\"primary_reason\":\"FEE_DISSATISFACTION\",\"reasoning_summary\":\"Complaint_text mentions fees or charges, and evidence suggests dissatisfaction with fees or charges. FEE_DISSATISFACTION fits because complaints_30d=1 and external_transfer_change_30d=13.3 suggest fees or charge-related issue.\",\"recommended_action\":\"FINANCIAL_GUIDANCE\",\"secondary_reasons\":[],\"urgency\":\"MEDIUM\"}",
    "error": null,
    "latency_s": 7.1894,
    "simple_output": "Reason: FEE_DISSATISFACTION | Urgency: MEDIUM | Action: FINANCIAL_GUIDANCE | Why: Complaint_text mentions fees or charges, and evidence suggests dissatisfaction with fees or charges. FEE_DISSATISFACTION fits because complaints_30d=1 and external_transfer_change_30d=13.3 suggest fees or charge-related issue."
  }
}
```

### Ekaraj Raju (`C12629`)

- OK: `True`
- Shape errors: `[]`
- Simple output: Reason: FINANCIAL_STRESS | Urgency: MEDIUM | Action: FINANCIAL_GUIDANCE | Why: Transaction and cash-flow signals point to a financial mismatch. FINANCIAL_GUIDANCE fits because app_login_change_30d=-28.8 and transaction_change_30d=-28.7 cite strong movement away from the norm.

Request:

```json
{
  "customer_id": "C12629",
  "customer_name": "Ekaraj Raju",
  "prediction_date": "2026-06-01",
  "snapshot_date": "2026-06-01",
  "target_month": "2026-07-01",
  "profile": {
    "tenure_months": 195,
    "customer_segment": "farmer",
    "income_regularity": "seasonal",
    "products_count": 2,
    "has_credit_card": 0,
    "has_loan": 1
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 4,
      "balance_change_30d": -8.2477,
      "transaction_change_30d": 4.648,
      "card_spend_change_30d": 15.8046,
      "app_login_change_30d": -9.998,
      "salary_missing_days": null,
      "external_transfer_change_30d": 29.9715,
      "upi_share_of_spend": 0.5778,
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
      "balance_change_30d": -18.0195,
      "transaction_change_30d": -31.8531,
      "card_spend_change_30d": 2.2915,
      "app_login_change_30d": -26.9834,
      "salary_missing_days": null,
      "external_transfer_change_30d": -16.6274,
      "upi_share_of_spend": 0.7188,
      "fd_maturing_in_30d": 1,
      "products_dropped_90d": 0,
      "complaints_30d": 2,
      "unresolved_complaints": 2,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 52.1027,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-03-01",
      "days_since_last_transaction": 10,
      "balance_change_30d": -21.1079,
      "transaction_change_30d": -17.4622,
      "card_spend_change_30d": -30.2527,
      "app_login_change_30d": -22.5503,
      "salary_missing_days": null,
      "external_transfer_change_30d": 64.367,
      "upi_share_of_spend": 0.6188,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 11.4684,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-04-01",
      "days_since_last_transaction": 10,
      "balance_change_30d": -29.3461,
      "transaction_change_30d": -19.4507,
      "card_spend_change_30d": -17.5243,
      "app_login_change_30d": 3.0244,
      "salary_missing_days": null,
      "external_transfer_change_30d": 25.434,
      "upi_share_of_spend": 0.6628,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 0,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 2,
      "avg_resolution_time_hrs": 0.0,
      "emi_bounce_30d": 1
    },
    {
      "snapshot_date": "2026-05-01",
      "days_since_last_transaction": 14,
      "balance_change_30d": -31.41,
      "transaction_change_30d": -25.3424,
      "card_spend_change_30d": -28.4718,
      "app_login_change_30d": -41.9847,
      "salary_missing_days": null,
      "external_transfer_change_30d": 69.7944,
      "upi_share_of_spend": 0.7577,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 2,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 3,
      "avg_resolution_time_hrs": 40.8624,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-06-01",
      "days_since_last_transaction": 14,
      "balance_change_30d": -27.0499,
      "transaction_change_30d": -28.6984,
      "card_spend_change_30d": -53.8182,
      "app_login_change_30d": -28.7731,
      "salary_missing_days": null,
      "external_transfer_change_30d": 70.374,
      "upi_share_of_spend": 0.7981,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 0,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 0.0,
      "emi_bounce_30d": 1
    }
  ],
  "customer": {
    "tenure_months": 195,
    "customer_segment": "farmer",
    "income_regularity": "seasonal",
    "products_count": 2,
    "has_credit_card": 0,
    "has_loan": 1,
    "days_since_last_transaction": 14,
    "balance_change_30d": -27.0499,
    "transaction_change_30d": -28.6984,
    "card_spend_change_30d": -53.8182,
    "app_login_change_30d": -28.7731,
    "salary_missing_days": null,
    "external_transfer_change_30d": 70.374,
    "upi_share_of_spend": 0.7981,
    "fd_maturing_in_30d": 0,
    "products_dropped_90d": 0,
    "complaints_30d": 0,
    "unresolved_complaints": 0,
    "failed_transactions_30d": 1,
    "avg_resolution_time_hrs": 0.0,
    "emi_bounce_30d": 1
  },
  "extra_context": {
    "customer_profile": {
      "segment": "farmer",
      "income_regularity": "seasonal",
      "tenure_months": 195,
      "age": 57,
      "customer_yearly_value": 7334.1186,
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
    "served_at": "2026-08-31T01:56:47",
    "elapsed_ms": 9115.22,
    "timings_ms": {
      "model1": 199.9,
      "model2": 8915.09
    },
    "customer_id": "C12629",
    "customer_name": "Ekaraj Raju",
    "snapshot_date": "2026-06-01"
  },
  "model1": {
    "churn_probability": 35.88,
    "raw_churn_probability": 89.54,
    "probability_mode": "sigmoid",
    "risk_score": 75.95,
    "churn_prediction": "Yes",
    "risk_level": "High",
    "top_risk_factors": [
      {
        "factor": "latest_days_since_last_transaction",
        "value": 14,
        "message": "Customer has gone longer without transacting.",
        "contribution": 0.5406972765922546
      },
      {
        "factor": "latest_transaction_change_30d",
        "value": -28.6984,
        "message": "Transaction activity has been falling across recent months.",
        "contribution": 0.2643245756626129
      },
      {
        "factor": "latest_vs_avg_upi_share_of_spend_available_history",
        "value": 0.10910000000000009,
        "message": "A larger share of spending is happening through UPI.",
        "contribution": 0.24882595241069794
      },
      {
        "factor": "latest_card_spend_change_30d",
        "value": -53.8182,
        "message": "Card spending has been falling across recent months.",
        "contribution": 0.2023225575685501
      },
      {
        "factor": "days_since_last_transaction_trend_6m",
        "value": 1.9428571428571422,
        "message": "Customer has gone longer without transacting.",
        "contribution": 0.1803058385848999
      }
    ]
  },
  "model2_input": {
    "customer_context": {
      "age": 57,
      "tenure_months": 195,
      "customer_segment": "farmer",
      "income_regularity": "seasonal",
      "customer_yearly_value": 7334.1186,
      "products_count": 2,
      "has_credit_card": 0,
      "has_loan": 1
    },
    "behavior": {
      "days_since_last_transaction": 14,
      "balance_change_30d": -27.0499,
      "transaction_change_30d": -28.6984,
      "card_spend_change_30d": -53.8182,
      "app_login_change_30d": -28.7731,
      "salary_missing_days": null,
      "external_transfer_change_30d": 70.374,
      "upi_share_of_spend": 0.7981,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "emi_bounce_30d": 1
    },
    "service_evidence": {
      "complaints_30d": 0,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 0.0,
      "complaint_text": null
    },
    "model1": {
      "churn_probability": 0.3588,
      "churn_prediction": "Yes",
      "risk_level": "High",
      "top_risk_factors": [
        {
          "factor": "days_since_last_transaction",
          "value": 14
        },
        {
          "factor": "transaction_change_30d",
          "value": -28.6984
        },
        {
          "factor": "upi_share_of_spend",
          "value": 0.7981
        }
      ]
    },
    "eligible_actions": [
      "LOAN_REVIEW",
      "FINANCIAL_GUIDANCE",
      "SERVICE_RECOVERY",
      "PRODUCT_REVIEW",
      "MONITOR"
    ],
    "case_id": "C12629"
  },
  "model2": {
    "case_id": "C12629",
    "ok": true,
    "prediction": {
      "evidence": [
        "app_login_change_30d=-28.8",
        "transaction_change_30d=-28.7",
        "emi_bounce_30d=1"
      ],
      "primary_reason": "FINANCIAL_STRESS",
      "reasoning_summary": "Transaction and cash-flow signals point to a financial mismatch. FINANCIAL_GUIDANCE fits because app_login_change_30d=-28.8 and transaction_change_30d=-28.7 cite strong movement away from the norm.",
      "recommended_action": "FINANCIAL_GUIDANCE",
      "secondary_reasons": [],
      "urgency": "MEDIUM"
    },
    "warnings": [],
    "raw_text": "{\"evidence\":[\"app_login_change_30d=-28.8\",\"transaction_change_30d=-28.7\",\"emi_bounce_30d=1\"],\"primary_reason\":\"FINANCIAL_STRESS\",\"reasoning_summary\":\"Transaction and cash-flow signals point to a financial mismatch. FINANCIAL_GUIDANCE fits because app_login_change_30d=-28.8 and transaction_change_30d=-28.7 cite strong movement away from the norm.\",\"recommended_action\":\"FINANCIAL_GUIDANCE\",\"secondary_reasons\":[],\"urgency\":\"MEDIUM\"}",
    "error": null,
    "latency_s": 8.9149,
    "simple_output": "Reason: FINANCIAL_STRESS | Urgency: MEDIUM | Action: FINANCIAL_GUIDANCE | Why: Transaction and cash-flow signals point to a financial mismatch. FINANCIAL_GUIDANCE fits because app_login_change_30d=-28.8 and transaction_change_30d=-28.7 cite strong movement away from the norm."
  }
}
```

### Udarsh Bath (`C12997`)

- OK: `True`
- Shape errors: `[]`
- Simple output: Reason: TEMPORARY_SEASONAL_CHANGE | Urgency: LOW | Action: RE_ENGAGEMENT | Why: Temporary seasonal change is the most supported explanation for the risk signal. Evidence suggests this because complaints_30d=0, unresolved_complaints=0, avg_resolution_time_hrs=0.0.

Request:

```json
{
  "customer_id": "C12997",
  "customer_name": "Udarsh Bath",
  "prediction_date": "2026-06-01",
  "snapshot_date": "2026-06-01",
  "target_month": "2026-07-01",
  "profile": {
    "tenure_months": 147,
    "customer_segment": "farmer",
    "income_regularity": "seasonal",
    "products_count": 2,
    "has_credit_card": 0,
    "has_loan": 1
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 13,
      "balance_change_30d": -10.4294,
      "transaction_change_30d": -3.7455,
      "card_spend_change_30d": -27.1091,
      "app_login_change_30d": -37.1799,
      "salary_missing_days": null,
      "external_transfer_change_30d": 33.9957,
      "upi_share_of_spend": 0.6312,
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
      "days_since_last_transaction": 13,
      "balance_change_30d": -13.4079,
      "transaction_change_30d": -4.9862,
      "card_spend_change_30d": -36.9912,
      "app_login_change_30d": -23.4108,
      "salary_missing_days": null,
      "external_transfer_change_30d": 44.7663,
      "upi_share_of_spend": 0.614,
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
      "balance_change_30d": -9.6956,
      "transaction_change_30d": -7.5678,
      "card_spend_change_30d": -16.4995,
      "app_login_change_30d": -10.3321,
      "salary_missing_days": null,
      "external_transfer_change_30d": 48.1695,
      "upi_share_of_spend": 0.5445,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 5.4419,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-04-01",
      "days_since_last_transaction": 8,
      "balance_change_30d": -9.882,
      "transaction_change_30d": 1.441,
      "card_spend_change_30d": 2.1899,
      "app_login_change_30d": 41.5675,
      "salary_missing_days": null,
      "external_transfer_change_30d": 6.6672,
      "upi_share_of_spend": 0.54,
      "fd_maturing_in_30d": 1,
      "products_dropped_90d": 0,
      "complaints_30d": 0,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 0.0,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-05-01",
      "days_since_last_transaction": 4,
      "balance_change_30d": 9.4422,
      "transaction_change_30d": 21.4032,
      "card_spend_change_30d": 9.5706,
      "app_login_change_30d": 11.1892,
      "salary_missing_days": null,
      "external_transfer_change_30d": 19.8633,
      "upi_share_of_spend": 0.4865,
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
      "balance_change_30d": 23.9969,
      "transaction_change_30d": 12.2427,
      "card_spend_change_30d": 13.1419,
      "app_login_change_30d": 19.6851,
      "salary_missing_days": null,
      "external_transfer_change_30d": -14.1305,
      "upi_share_of_spend": 0.5346,
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
    "tenure_months": 147,
    "customer_segment": "farmer",
    "income_regularity": "seasonal",
    "products_count": 2,
    "has_credit_card": 0,
    "has_loan": 1,
    "days_since_last_transaction": 6,
    "balance_change_30d": 23.9969,
    "transaction_change_30d": 12.2427,
    "card_spend_change_30d": 13.1419,
    "app_login_change_30d": 19.6851,
    "salary_missing_days": null,
    "external_transfer_change_30d": -14.1305,
    "upi_share_of_spend": 0.5346,
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
      "tenure_months": 147,
      "age": 32,
      "customer_yearly_value": 35952.7267,
      "products_count": 2,
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
    "served_at": "2026-08-31T01:56:58",
    "elapsed_ms": 10780.82,
    "timings_ms": {
      "model1": 185.6,
      "model2": 10594.86
    },
    "customer_id": "C12997",
    "customer_name": "Udarsh Bath",
    "snapshot_date": "2026-06-01"
  },
  "model1": {
    "churn_probability": 2.39,
    "raw_churn_probability": 22.33,
    "probability_mode": "sigmoid",
    "risk_score": 7.16,
    "churn_prediction": "No",
    "risk_level": "Low",
    "top_risk_factors": [
      {
        "factor": "latest_vs_avg_external_transfer_change_30d_available_history",
        "value": -37.35241666666667,
        "message": "This signal increased churn risk.",
        "contribution": 0.07544872909784317
      },
      {
        "factor": "sum_fd_maturing_in_30d_3m",
        "value": 1.0,
        "message": "Customer has a fixed deposit maturing soon.",
        "contribution": 0.07335391640663147
      },
      {
        "factor": "count_balance_drop_6m",
        "value": 4,
        "message": "This signal increased churn risk.",
        "contribution": 0.05570952221751213
      },
      {
        "factor": "latest_vs_avg_app_login_change_30d_available_history",
        "value": 19.43193333333333,
        "message": "This signal increased churn risk.",
        "contribution": 0.04186413064599037
      },
      {
        "factor": "card_spend_change_30d_trend_6m",
        "value": 10.275137142857139,
        "message": "This signal increased churn risk.",
        "contribution": 0.037566497921943665
      }
    ]
  },
  "model2_input": {
    "customer_context": {
      "age": 32,
      "tenure_months": 147,
      "customer_segment": "farmer",
      "income_regularity": "seasonal",
      "customer_yearly_value": 35952.7267,
      "products_count": 2,
      "has_credit_card": 0,
      "has_loan": 1
    },
    "behavior": {
      "days_since_last_transaction": 6,
      "balance_change_30d": 23.9969,
      "transaction_change_30d": 12.2427,
      "card_spend_change_30d": 13.1419,
      "app_login_change_30d": 19.6851,
      "salary_missing_days": null,
      "external_transfer_change_30d": -14.1305,
      "upi_share_of_spend": 0.5346,
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
      "churn_probability": 0.0239,
      "churn_prediction": "No",
      "risk_level": "Low",
      "top_risk_factors": [
        {
          "factor": "external_transfer_change_30d",
          "value": -14.1305
        },
        {
          "factor": "fd_maturing_in_30d",
          "value": 0
        },
        {
          "factor": "app_login_change_30d",
          "value": 19.6851
        }
      ]
    },
    "eligible_actions": [
      "RE_ENGAGEMENT",
      "PRODUCT_REVIEW",
      "MONITOR"
    ],
    "case_id": "C12997"
  },
  "model2": {
    "case_id": "C12997",
    "ok": true,
    "prediction": {
      "evidence": [
        "complaints_30d=0",
        "unresolved_complaints=0",
        "avg_resolution_time_hrs=0.0"
      ],
      "primary_reason": "TEMPORARY_SEASONAL_CHANGE",
      "reasoning_summary": "Temporary seasonal change is the most supported explanation for the risk signal. Evidence suggests this because complaints_30d=0, unresolved_complaints=0, avg_resolution_time_hrs=0.0.",
      "recommended_action": "RE_ENGAGEMENT",
      "secondary_reasons": [],
      "urgency": "LOW"
    },
    "warnings": [
      "evidence: 'complaints_30d=0' cites a zero/null value, which is not evidence; remove it",
      "evidence: 'unresolved_complaints=0' cites a zero/null value, which is not evidence; remove it",
      "evidence: 'avg_resolution_time_hrs=0.0' cites a zero/null value, which is not evidence; remove it"
    ],
    "raw_text": "{\"evidence\":[\"complaints_30d=0\",\"external_transfer_change_30d=-14.1\",\"transaction_change_30d=12.2\"],\"primary_reason\":\"DIGITAL_FRICTION\",\"reasoning_summary\":\"Digital friction is the strongest supported signal here. Evidence suggests this because complaints_30d=0, external_transfer_change_30d=-14.1, and transaction_change_30d=12.2 point to a digital or transaction experience issue.\",\"recommended_action\":\"RE_ENGAGEMENT\",\"secondary_reasons\":[],\"urgency\":\"MEDIUM\"}",
    "error": null,
    "latency_s": 10.5946,
    "simple_output": "Reason: TEMPORARY_SEASONAL_CHANGE | Urgency: LOW | Action: RE_ENGAGEMENT | Why: Temporary seasonal change is the most supported explanation for the risk signal. Evidence suggests this because complaints_30d=0, unresolved_complaints=0, avg_resolution_time_hrs=0.0."
  }
}
```

### Widisha Chatterjee (`C13116`)

- OK: `True`
- Shape errors: `[]`
- Simple output: Reason: UNKNOWN | Urgency: LOW | Action: MONITOR | Why: Complaint and resolution signals are mixed or weak; relationship strength is uncertain.

Request:

```json
{
  "customer_id": "C13116",
  "customer_name": "Widisha Chatterjee",
  "prediction_date": "2026-06-01",
  "snapshot_date": "2026-06-01",
  "target_month": "2026-07-01",
  "profile": {
    "tenure_months": 84,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 4,
    "has_credit_card": 1,
    "has_loan": 1
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 12,
      "balance_change_30d": -6.2931,
      "transaction_change_30d": -4.1765,
      "card_spend_change_30d": 35.2799,
      "app_login_change_30d": -4.9743,
      "salary_missing_days": 2.0,
      "external_transfer_change_30d": 25.048,
      "upi_share_of_spend": 0.6027,
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
      "days_since_last_transaction": 0,
      "balance_change_30d": 12.3996,
      "transaction_change_30d": -5.1971,
      "card_spend_change_30d": 8.8799,
      "app_login_change_30d": 37.5021,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -15.8962,
      "upi_share_of_spend": 0.5723,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 2,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 23.2821,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-03-01",
      "days_since_last_transaction": 3,
      "balance_change_30d": -9.4836,
      "transaction_change_30d": 3.9184,
      "card_spend_change_30d": 38.1053,
      "app_login_change_30d": 13.3532,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -8.5525,
      "upi_share_of_spend": 0.4687,
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
      "balance_change_30d": 1.5928,
      "transaction_change_30d": 0.6635,
      "card_spend_change_30d": 20.1342,
      "app_login_change_30d": -15.6826,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -19.3226,
      "upi_share_of_spend": 0.5893,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 2,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 29.2952,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-05-01",
      "days_since_last_transaction": 4,
      "balance_change_30d": 10.7845,
      "transaction_change_30d": -5.7115,
      "card_spend_change_30d": -5.9075,
      "app_login_change_30d": -12.8878,
      "salary_missing_days": 2.0,
      "external_transfer_change_30d": 24.0174,
      "upi_share_of_spend": 0.5724,
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
      "balance_change_30d": 4.4975,
      "transaction_change_30d": 9.6536,
      "card_spend_change_30d": 23.075,
      "app_login_change_30d": 3.5436,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": 21.1083,
      "upi_share_of_spend": 0.6418,
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
    "tenure_months": 84,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 4,
    "has_credit_card": 1,
    "has_loan": 1,
    "days_since_last_transaction": 2,
    "balance_change_30d": 4.4975,
    "transaction_change_30d": 9.6536,
    "card_spend_change_30d": 23.075,
    "app_login_change_30d": 3.5436,
    "salary_missing_days": 0.0,
    "external_transfer_change_30d": 21.1083,
    "upi_share_of_spend": 0.6418,
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
      "tenure_months": 84,
      "age": 44,
      "customer_yearly_value": 70082.4032,
      "products_count": 4,
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
  "meta": {
    "endpoint": "/predict/both",
    "served_at": "2026-08-31T01:57:06",
    "elapsed_ms": 7505.24,
    "timings_ms": {
      "model1": 317.6,
      "model2": 7187.28
    },
    "customer_id": "C13116",
    "customer_name": "Widisha Chatterjee",
    "snapshot_date": "2026-06-01"
  },
  "model1": {
    "churn_probability": 3.03,
    "raw_churn_probability": 27.59,
    "probability_mode": "sigmoid",
    "risk_score": 9.09,
    "churn_prediction": "No",
    "risk_level": "Low",
    "top_risk_factors": [
      {
        "factor": "latest_vs_avg_upi_share_of_spend_available_history",
        "value": 0.0672666666666667,
        "message": "A larger share of spending is happening through UPI.",
        "contribution": 0.1878271847963333
      },
      {
        "factor": "latest_upi_share_of_spend",
        "value": 0.6418,
        "message": "A larger share of spending is happening through UPI.",
        "contribution": 0.040530722588300705
      },
      {
        "factor": "external_transfer_change_30d_trend_6m",
        "value": 2.550634285714285,
        "message": "External transfers have increased.",
        "contribution": 0.025425180792808533
      },
      {
        "factor": "count_app_login_drop_3m",
        "value": 2,
        "message": "This signal increased churn risk.",
        "contribution": 0.011706733144819736
      },
      {
        "factor": "latest_vs_avg_card_spend_change_30d_available_history",
        "value": 3.1472000000000016,
        "message": "This signal increased churn risk.",
        "contribution": 0.011610045097768307
      }
    ]
  },
  "model2_input": {
    "customer_context": {
      "age": 44,
      "tenure_months": 84,
      "customer_segment": "salary",
      "income_regularity": "regular",
      "customer_yearly_value": 70082.4032,
      "products_count": 4,
      "has_credit_card": 1,
      "has_loan": 1
    },
    "behavior": {
      "days_since_last_transaction": 2,
      "balance_change_30d": 4.4975,
      "transaction_change_30d": 9.6536,
      "card_spend_change_30d": 23.075,
      "app_login_change_30d": 3.5436,
      "salary_missing_days": 0,
      "external_transfer_change_30d": 21.1083,
      "upi_share_of_spend": 0.6418,
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
      "churn_probability": 0.0303,
      "churn_prediction": "No",
      "risk_level": "Low",
      "top_risk_factors": [
        {
          "factor": "upi_share_of_spend",
          "value": 0.6418
        },
        {
          "factor": "external_transfer_change_30d",
          "value": 21.1083
        },
        {
          "factor": "card_spend_change_30d",
          "value": 23.075
        }
      ]
    },
    "eligible_actions": [
      "RE_ENGAGEMENT",
      "PRODUCT_REVIEW",
      "MONITOR"
    ],
    "case_id": "C13116"
  },
  "model2": {
    "case_id": "C13116",
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
    "raw_text": "{\"evidence\":[\"complaints_30d=0\",\"unresolved_complaints=0\",\"avg_resolution_time_hrs=0.0\"],\"primary_reason\":\"UNKNOWN\",\"reasoning_summary\":\"Complaint and resolution signals are mixed or weak; relationship strength is uncertain.\",\"recommended_action\":\"MONITOR\",\"secondary_reasons\":[],\"urgency\":\"LOW\"}",
    "error": null,
    "latency_s": 7.1861,
    "simple_output": "Reason: UNKNOWN | Urgency: LOW | Action: MONITOR | Why: Complaint and resolution signals are mixed or weak; relationship strength is uncertain."
  }
}
```

### Jatin Purohit (`C13656`)

- OK: `True`
- Shape errors: `[]`
- Simple output: Reason: FINANCIAL_STRESS | Urgency: MEDIUM | Action: FINANCIAL_GUIDANCE | Why: Evidence suggests this because transaction_change_30d=-45.2 and salary_missing_days=4 point to a financial issue. Financial Guidance fits because complaint_text is null and unresolved_complaints=0.

Request:

```json
{
  "customer_id": "C13656",
  "customer_name": "Jatin Purohit",
  "prediction_date": "2026-04-01",
  "snapshot_date": "2026-04-01",
  "target_month": "2026-05-01",
  "profile": {
    "tenure_months": 41,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 2,
    "has_credit_card": 1,
    "has_loan": 0
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 7,
      "balance_change_30d": -3.1879,
      "transaction_change_30d": 16.3021,
      "card_spend_change_30d": 40.8974,
      "app_login_change_30d": 44.3577,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": 14.4482,
      "upi_share_of_spend": 0.4345,
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
      "balance_change_30d": -14.1693,
      "transaction_change_30d": 4.391,
      "card_spend_change_30d": -22.0222,
      "app_login_change_30d": -14.2335,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": 12.7452,
      "upi_share_of_spend": 0.4157,
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
      "days_since_last_transaction": 18,
      "balance_change_30d": -19.0104,
      "transaction_change_30d": -25.4873,
      "card_spend_change_30d": -10.3619,
      "app_login_change_30d": -14.4105,
      "salary_missing_days": 3.0,
      "external_transfer_change_30d": 49.5874,
      "upi_share_of_spend": 0.5307,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 1,
      "complaints_30d": 2,
      "unresolved_complaints": 1,
      "failed_transactions_30d": 3,
      "avg_resolution_time_hrs": 36.3581,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-04-01",
      "days_since_last_transaction": 23,
      "balance_change_30d": -46.5142,
      "transaction_change_30d": -45.1974,
      "card_spend_change_30d": -44.3812,
      "app_login_change_30d": -54.4607,
      "salary_missing_days": 4.0,
      "external_transfer_change_30d": 38.1466,
      "upi_share_of_spend": 0.5146,
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
    "tenure_months": 41,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 2,
    "has_credit_card": 1,
    "has_loan": 0,
    "days_since_last_transaction": 23,
    "balance_change_30d": -46.5142,
    "transaction_change_30d": -45.1974,
    "card_spend_change_30d": -44.3812,
    "app_login_change_30d": -54.4607,
    "salary_missing_days": 4.0,
    "external_transfer_change_30d": 38.1466,
    "upi_share_of_spend": 0.5146,
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
      "tenure_months": 41,
      "age": 42,
      "customer_yearly_value": 40181.3566,
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
    "served_at": "2026-08-31T01:57:21",
    "elapsed_ms": 14963.25,
    "timings_ms": {
      "model1": 292.03,
      "model2": 14670.88
    },
    "customer_id": "C13656",
    "customer_name": "Jatin Purohit",
    "snapshot_date": "2026-04-01"
  },
  "model1": {
    "churn_probability": 42.39,
    "raw_churn_probability": 95.43,
    "probability_mode": "sigmoid",
    "risk_score": 78.4,
    "churn_prediction": "Yes",
    "risk_level": "High",
    "top_risk_factors": [
      {
        "factor": "latest_days_since_last_transaction",
        "value": 23,
        "message": "Customer has gone longer without transacting.",
        "contribution": 0.5895359516143799
      },
      {
        "factor": "latest_transaction_change_30d",
        "value": -45.1974,
        "message": "Transaction activity has been falling across recent months.",
        "contribution": 0.43286237120628357
      },
      {
        "factor": "latest_salary_missing_days",
        "value": 4.0,
        "message": "Salary or pension was delayed recently.",
        "contribution": 0.22426718473434448
      },
      {
        "factor": "latest_balance_change_30d",
        "value": -46.5142,
        "message": "Balance has been falling across recent months.",
        "contribution": 0.21470044553279877
      },
      {
        "factor": "days_since_last_transaction_trend_6m",
        "value": 5.4,
        "message": "Customer has gone longer without transacting.",
        "contribution": 0.18935368955135345
      }
    ]
  },
  "model2_input": {
    "customer_context": {
      "age": 42,
      "tenure_months": 41,
      "customer_segment": "salary",
      "income_regularity": "regular",
      "customer_yearly_value": 40181.3566,
      "products_count": 2,
      "has_credit_card": 1,
      "has_loan": 0
    },
    "behavior": {
      "days_since_last_transaction": 23,
      "balance_change_30d": -46.5142,
      "transaction_change_30d": -45.1974,
      "card_spend_change_30d": -44.3812,
      "app_login_change_30d": -54.4607,
      "salary_missing_days": 4,
      "external_transfer_change_30d": 38.1466,
      "upi_share_of_spend": 0.5146,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "emi_bounce_30d": 0
    },
    "service_evidence": {
      "complaints_30d": 0,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 3,
      "avg_resolution_time_hrs": 0.0,
      "complaint_text": null
    },
    "model1": {
      "churn_probability": 0.4239,
      "churn_prediction": "Yes",
      "risk_level": "High",
      "top_risk_factors": [
        {
          "factor": "days_since_last_transaction",
          "value": 23
        },
        {
          "factor": "transaction_change_30d",
          "value": -45.1974
        },
        {
          "factor": "salary_missing_days",
          "value": 4
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
    "case_id": "C13656"
  },
  "model2": {
    "case_id": "C13656",
    "ok": true,
    "prediction": {
      "evidence": [
        "transaction_change_30d=-45.2",
        "app_login_change_30d=-54.5",
        "salary_missing_days=4",
        "emi_bounce_30d=0",
        "avg_resolution_time_hrs=0.0"
      ],
      "primary_reason": "FINANCIAL_STRESS",
      "reasoning_summary": "Evidence suggests this because transaction_change_30d=-45.2 and salary_missing_days=4 point to a financial issue. Financial Guidance fits because complaint_text is null and unresolved_complaints=0.",
      "recommended_action": "FINANCIAL_GUIDANCE",
      "secondary_reasons": [],
      "urgency": "MEDIUM"
    },
    "warnings": [
      "evidence: 'emi_bounce_30d=0' cites a zero/null value, which is not evidence; remove it",
      "evidence: 'avg_resolution_time_hrs=0.0' cites a zero/null value, which is not evidence; remove it"
    ],
    "raw_text": "{\"evidence\":[\"complaints_30d=0\",\"unresolved_complaints=0\",\"avg_resolution_time_hrs=0.0\",\"emi_bounce_30d=0\"],\"primary_reason\":\"FINANCIAL_STRESS\",\"reasoning_summary\":\"Evidence suggests this because complaint_text is null, complaints_30d=0, unresolved_complaints=0, avg_resolution_time_hrs=0.0 and emi_bounce_30d=0. Evidence suggests this because balance_change_30d=-46.5, transaction_change_30d=-45.2 and app_login_change_30d=-54.5 suggest a financial or cash-flow related issue.\",\"recommended_action\":\"FINANCIAL_GUIDANCE\",\"secondary_reasons\":[],\"urgency\":\"MEDIUM\"}",
    "error": null,
    "latency_s": 14.6688,
    "simple_output": "Reason: FINANCIAL_STRESS | Urgency: MEDIUM | Action: FINANCIAL_GUIDANCE | Why: Evidence suggests this because transaction_change_30d=-45.2 and salary_missing_days=4 point to a financial issue. Financial Guidance fits because complaint_text is null and unresolved_complaints=0."
  }
}
```

### Lopa Chandran (`C15140`)

- OK: `True`
- Shape errors: `[]`
- Simple output: Reason: UNKNOWN | Urgency: LOW | Action: MONITOR | Why: Complaint and resolution signals are mixed or weak; evidence is genuinely unclear.

Request:

```json
{
  "customer_id": "C15140",
  "customer_name": "Lopa Chandran",
  "prediction_date": "2026-06-01",
  "snapshot_date": "2026-06-01",
  "target_month": "2026-07-01",
  "profile": {
    "tenure_months": 76,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 2,
    "has_credit_card": 0,
    "has_loan": 1
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 11,
      "balance_change_30d": -14.0199,
      "transaction_change_30d": -14.3571,
      "card_spend_change_30d": -35.3953,
      "app_login_change_30d": -2.2512,
      "salary_missing_days": 2.0,
      "external_transfer_change_30d": -9.6502,
      "upi_share_of_spend": 0.4165,
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
      "days_since_last_transaction": 15,
      "balance_change_30d": 7.4023,
      "transaction_change_30d": 9.7425,
      "card_spend_change_30d": 1.2586,
      "app_login_change_30d": 18.3998,
      "salary_missing_days": 3.0,
      "external_transfer_change_30d": 12.8648,
      "upi_share_of_spend": 0.5224,
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
      "balance_change_30d": -2.6524,
      "transaction_change_30d": -18.5413,
      "card_spend_change_30d": 5.2787,
      "app_login_change_30d": 2.7805,
      "salary_missing_days": 1.0,
      "external_transfer_change_30d": 5.7982,
      "upi_share_of_spend": 0.4842,
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
      "balance_change_30d": 20.5636,
      "transaction_change_30d": 16.5703,
      "card_spend_change_30d": 24.1219,
      "app_login_change_30d": 7.5214,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": 9.3516,
      "upi_share_of_spend": 0.426,
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
      "days_since_last_transaction": 14,
      "balance_change_30d": 5.4959,
      "transaction_change_30d": -5.5698,
      "card_spend_change_30d": -19.4,
      "app_login_change_30d": 30.3798,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": 48.9723,
      "upi_share_of_spend": 0.606,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 2.9201,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-06-01",
      "days_since_last_transaction": 9,
      "balance_change_30d": 18.8963,
      "transaction_change_30d": -0.4124,
      "card_spend_change_30d": 23.609,
      "app_login_change_30d": 10.6998,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -10.5435,
      "upi_share_of_spend": 0.542,
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
    "tenure_months": 76,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 2,
    "has_credit_card": 0,
    "has_loan": 1,
    "days_since_last_transaction": 9,
    "balance_change_30d": 18.8963,
    "transaction_change_30d": -0.4124,
    "card_spend_change_30d": 23.609,
    "app_login_change_30d": 10.6998,
    "salary_missing_days": 0.0,
    "external_transfer_change_30d": -10.5435,
    "upi_share_of_spend": 0.542,
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
      "tenure_months": 76,
      "age": 32,
      "customer_yearly_value": 39294.9669,
      "products_count": 2,
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
    "served_at": "2026-08-31T01:57:31",
    "elapsed_ms": 9644.31,
    "timings_ms": {
      "model1": 419.13,
      "model2": 9224.85
    },
    "customer_id": "C15140",
    "customer_name": "Lopa Chandran",
    "snapshot_date": "2026-06-01"
  },
  "model1": {
    "churn_probability": 2.63,
    "raw_churn_probability": 24.48,
    "probability_mode": "sigmoid",
    "risk_score": 7.9,
    "churn_prediction": "No",
    "risk_level": "Low",
    "top_risk_factors": [
      {
        "factor": "latest_vs_avg_upi_share_of_spend_available_history",
        "value": 0.04248333333333343,
        "message": "A larger share of spending is happening through UPI.",
        "contribution": 0.08610925078392029
      },
      {
        "factor": "card_spend_change_30d_trend_6m",
        "value": 7.196825714285712,
        "message": "This signal increased churn risk.",
        "contribution": 0.04124423488974571
      },
      {
        "factor": "latest_upi_share_of_spend",
        "value": 0.542,
        "message": "A larger share of spending is happening through UPI.",
        "contribution": 0.03249653801321983
      },
      {
        "factor": "external_transfer_change_30d_trend_6m",
        "value": 3.0688400000000007,
        "message": "External transfers have increased.",
        "contribution": 0.02786836586892605
      },
      {
        "factor": "max_days_since_last_transaction_3m",
        "value": 14.0,
        "message": "Customer has gone longer without transacting.",
        "contribution": 0.010758032090961933
      }
    ]
  },
  "model2_input": {
    "customer_context": {
      "age": 32,
      "tenure_months": 76,
      "customer_segment": "salary",
      "income_regularity": "regular",
      "customer_yearly_value": 39294.9669,
      "products_count": 2,
      "has_credit_card": 0,
      "has_loan": 1
    },
    "behavior": {
      "days_since_last_transaction": 9,
      "balance_change_30d": 18.8963,
      "transaction_change_30d": -0.4124,
      "card_spend_change_30d": 23.609,
      "app_login_change_30d": 10.6998,
      "salary_missing_days": 0,
      "external_transfer_change_30d": -10.5435,
      "upi_share_of_spend": 0.542,
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
      "churn_probability": 0.0263,
      "churn_prediction": "No",
      "risk_level": "Low",
      "top_risk_factors": [
        {
          "factor": "upi_share_of_spend",
          "value": 0.542
        },
        {
          "factor": "card_spend_change_30d",
          "value": 23.609
        },
        {
          "factor": "external_transfer_change_30d",
          "value": -10.5435
        }
      ]
    },
    "eligible_actions": [
      "SERVICE_RECOVERY",
      "RE_ENGAGEMENT",
      "MONITOR"
    ],
    "case_id": "C15140"
  },
  "model2": {
    "case_id": "C15140",
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
    "raw_text": "{\"evidence\":[\"complaints_30d=0\",\"unresolved_complaints=0\",\"avg_resolution_time_hrs=0.0\"],\"primary_reason\":\"LOW_ENGAGEMENT\",\"reasoning_summary\":\"Days_since_last_transaction=9 and transaction_change_30d=-0.4 cite inactivity without a clear trigger or resolution.\",\"recommended_action\":\"RE_ENGAGEMENT\",\"secondary_reasons\":[],\"urgency\":\"MEDIUM\"}",
    "error": null,
    "latency_s": 9.2227,
    "simple_output": "Reason: UNKNOWN | Urgency: LOW | Action: MONITOR | Why: Complaint and resolution signals are mixed or weak; evidence is genuinely unclear."
  }
}
```

### Kai Peri (`C15390`)

- OK: `True`
- Shape errors: `[]`
- Simple output: Reason: SERVICE_DISSATISFACTION | Urgency: MEDIUM | Action: SERVICE_RECOVERY | Why: Complaint escalation fits because complaints_30d=1 and avg_resolution_time_hrs=12.2 show the digital experience is broken or unresolved_complaints=0 hides a real issue.

Request:

```json
{
  "customer_id": "C15390",
  "customer_name": "Kai Peri",
  "prediction_date": "2026-06-01",
  "snapshot_date": "2026-06-01",
  "target_month": "2026-07-01",
  "profile": {
    "tenure_months": 8,
    "customer_segment": "vendor",
    "income_regularity": "irregular",
    "products_count": 1,
    "has_credit_card": 0,
    "has_loan": 0
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 7,
      "balance_change_30d": -1.2808,
      "transaction_change_30d": 0.2043,
      "card_spend_change_30d": 7.4056,
      "app_login_change_30d": 1.2815,
      "salary_missing_days": null,
      "external_transfer_change_30d": -22.1408,
      "upi_share_of_spend": 0.4053,
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
      "balance_change_30d": 20.038,
      "transaction_change_30d": -15.509,
      "card_spend_change_30d": -9.4558,
      "app_login_change_30d": 29.2398,
      "salary_missing_days": null,
      "external_transfer_change_30d": 9.4704,
      "upi_share_of_spend": 0.4791,
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
      "balance_change_30d": 16.4927,
      "transaction_change_30d": 26.1291,
      "card_spend_change_30d": 12.1807,
      "app_login_change_30d": 19.5445,
      "salary_missing_days": null,
      "external_transfer_change_30d": -20.7838,
      "upi_share_of_spend": 0.3783,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 2,
      "avg_resolution_time_hrs": 26.9116,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-04-01",
      "days_since_last_transaction": 0,
      "balance_change_30d": -4.193,
      "transaction_change_30d": 10.3511,
      "card_spend_change_30d": -0.7566,
      "app_login_change_30d": 19.5498,
      "salary_missing_days": null,
      "external_transfer_change_30d": -31.3596,
      "upi_share_of_spend": 0.3989,
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
      "balance_change_30d": 42.4031,
      "transaction_change_30d": 26.0545,
      "card_spend_change_30d": 29.2769,
      "app_login_change_30d": 28.1505,
      "salary_missing_days": null,
      "external_transfer_change_30d": 2.7807,
      "upi_share_of_spend": 0.3852,
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
      "balance_change_30d": 20.7045,
      "transaction_change_30d": 1.8431,
      "card_spend_change_30d": 36.5995,
      "app_login_change_30d": 24.8411,
      "salary_missing_days": null,
      "external_transfer_change_30d": 47.9028,
      "upi_share_of_spend": 0.397,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 12.1736,
      "emi_bounce_30d": 0
    }
  ],
  "customer": {
    "tenure_months": 8,
    "customer_segment": "vendor",
    "income_regularity": "irregular",
    "products_count": 1,
    "has_credit_card": 0,
    "has_loan": 0,
    "days_since_last_transaction": 3,
    "balance_change_30d": 20.7045,
    "transaction_change_30d": 1.8431,
    "card_spend_change_30d": 36.5995,
    "app_login_change_30d": 24.8411,
    "salary_missing_days": null,
    "external_transfer_change_30d": 47.9028,
    "upi_share_of_spend": 0.397,
    "fd_maturing_in_30d": 0,
    "products_dropped_90d": 0,
    "complaints_30d": 1,
    "unresolved_complaints": 0,
    "failed_transactions_30d": 1,
    "avg_resolution_time_hrs": 12.1736,
    "emi_bounce_30d": 0
  },
  "extra_context": {
    "customer_profile": {
      "segment": "vendor",
      "income_regularity": "irregular",
      "tenure_months": 8,
      "age": 41,
      "customer_yearly_value": 18880.8867,
      "products_count": 1,
      "has_credit_card": 0,
      "has_loan": 0,
      "value_tier": "low"
    },
    "recent_complaint_text": "Insurance premium debited from my account which I never authorised."
  }
}
```

Response:

```json
{
  "meta": {
    "endpoint": "/predict/both",
    "served_at": "2026-08-31T01:57:42",
    "elapsed_ms": 11457.46,
    "timings_ms": {
      "model1": 349.05,
      "model2": 11105.89
    },
    "customer_id": "C15390",
    "customer_name": "Kai Peri",
    "snapshot_date": "2026-06-01"
  },
  "model1": {
    "churn_probability": 2.67,
    "raw_churn_probability": 24.78,
    "probability_mode": "sigmoid",
    "risk_score": 8.01,
    "churn_prediction": "No",
    "risk_level": "Low",
    "top_risk_factors": [
      {
        "factor": "sum_fd_maturing_in_30d_3m",
        "value": 1.0,
        "message": "Customer has a fixed deposit maturing soon.",
        "contribution": 0.057504910975694656
      },
      {
        "factor": "external_transfer_change_30d_trend_6m",
        "value": 9.130659999999997,
        "message": "External transfers have increased.",
        "contribution": 0.041045743972063065
      },
      {
        "factor": "card_spend_change_30d_trend_6m",
        "value": 7.1208657142857135,
        "message": "This signal increased churn risk.",
        "contribution": 0.020235363394021988
      },
      {
        "factor": "avg_app_login_change_30d_6m",
        "value": 20.43453333333333,
        "message": "This signal increased churn risk.",
        "contribution": 0.005256770644336939
      },
      {
        "factor": "latest_vs_avg_app_login_change_30d_available_history",
        "value": 4.40656666666667,
        "message": "This signal increased churn risk.",
        "contribution": 0.003572775050997734
      }
    ]
  },
  "model2_input": {
    "customer_context": {
      "age": 41,
      "tenure_months": 8,
      "customer_segment": "vendor",
      "income_regularity": "irregular",
      "customer_yearly_value": 18880.8867,
      "products_count": 1,
      "has_credit_card": 0,
      "has_loan": 0
    },
    "behavior": {
      "days_since_last_transaction": 3,
      "balance_change_30d": 20.7045,
      "transaction_change_30d": 1.8431,
      "card_spend_change_30d": 36.5995,
      "app_login_change_30d": 24.8411,
      "salary_missing_days": null,
      "external_transfer_change_30d": 47.9028,
      "upi_share_of_spend": 0.397,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "emi_bounce_30d": 0
    },
    "service_evidence": {
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 12.1736,
      "complaint_text": "Insurance premium debited from my account which I never authorised."
    },
    "model1": {
      "churn_probability": 0.0267,
      "churn_prediction": "No",
      "risk_level": "Low",
      "top_risk_factors": [
        {
          "factor": "fd_maturing_in_30d",
          "value": 0
        },
        {
          "factor": "external_transfer_change_30d",
          "value": 47.9028
        },
        {
          "factor": "card_spend_change_30d",
          "value": 36.5995
        }
      ]
    },
    "eligible_actions": [
      "SERVICE_RECOVERY",
      "PRODUCT_REVIEW",
      "MONITOR"
    ],
    "case_id": "C15390"
  },
  "model2": {
    "case_id": "C15390",
    "ok": true,
    "prediction": {
      "evidence": [
        "complaints_30d=1",
        "avg_resolution_time_hrs=12.2",
        "complaint_text describes a recent service issue"
      ],
      "primary_reason": "SERVICE_DISSATISFACTION",
      "reasoning_summary": "Complaint escalation fits because complaints_30d=1 and avg_resolution_time_hrs=12.2 show the digital experience is broken or unresolved_complaints=0 hides a real issue.",
      "recommended_action": "SERVICE_RECOVERY",
      "secondary_reasons": [],
      "urgency": "MEDIUM"
    },
    "warnings": [
      "reasoning_summary: describes COMPLAINT_ESCALATION but recommended_action is SERVICE_RECOVERY; rewrite the summary around the action you chose"
    ],
    "raw_text": "{\"evidence\":[\"complaints_30d=1\",\"external_transfer_change_30d=47.9\",\"card_spend_change_30d=36.6\"],\"primary_reason\":\"DIGITAL_FRICTION\",\"reasoning_summary\":\"Digital friction is the strongest supported explanation for the observed signals. Complaint escalation fits because complaints_30d=1 and external_transfer_change_30d=47.9 suggest the issue is unresolved or operationally serious.\",\"recommended_action\":\"SERVICE_RECOVERY\",\"secondary_reasons\":[],\"urgency\":\"MEDIUM\"}",
    "error": null,
    "latency_s": 11.1055,
    "simple_output": "Reason: SERVICE_DISSATISFACTION | Urgency: MEDIUM | Action: SERVICE_RECOVERY | Why: Complaint escalation fits because complaints_30d=1 and avg_resolution_time_hrs=12.2 show the digital experience is broken or unresolved_complaints=0 hides a real issue."
  }
}
```

### Widisha Parmer (`C15968`)

- OK: `True`
- Shape errors: `[]`
- Simple output: Reason: FINANCIAL_STRESS | Urgency: MEDIUM | Action: FINANCIAL_GUIDANCE | Why: The relationship looks stuck in a financial rut. Digital friction fits because transaction_change_30d=34.9 and balance_change_30d=16.2 suggest this. FINANCIAL_GUIDANCE fits because complaints_30d=0.

Request:

```json
{
  "customer_id": "C15968",
  "customer_name": "Widisha Parmer",
  "prediction_date": "2026-06-01",
  "snapshot_date": "2026-06-01",
  "target_month": "2026-07-01",
  "profile": {
    "tenure_months": 86,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 2,
    "has_credit_card": 0,
    "has_loan": 0
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 4,
      "balance_change_30d": -6.4429,
      "transaction_change_30d": 3.9382,
      "card_spend_change_30d": -5.4601,
      "app_login_change_30d": 11.5256,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": 28.8002,
      "upi_share_of_spend": 0.3764,
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
      "balance_change_30d": -9.9116,
      "transaction_change_30d": -12.4876,
      "card_spend_change_30d": 12.7526,
      "app_login_change_30d": 6.1426,
      "salary_missing_days": 2.0,
      "external_transfer_change_30d": 12.0914,
      "upi_share_of_spend": 0.3988,
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
      "balance_change_30d": -19.5449,
      "transaction_change_30d": 11.2251,
      "card_spend_change_30d": -0.6838,
      "app_login_change_30d": 8.8669,
      "salary_missing_days": 3.0,
      "external_transfer_change_30d": -0.8594,
      "upi_share_of_spend": 0.4991,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 14.8128,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-04-01",
      "days_since_last_transaction": 3,
      "balance_change_30d": 13.5483,
      "transaction_change_30d": 14.0486,
      "card_spend_change_30d": -1.351,
      "app_login_change_30d": -8.7311,
      "salary_missing_days": 1.0,
      "external_transfer_change_30d": -6.6072,
      "upi_share_of_spend": 0.3497,
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
      "balance_change_30d": 30.0198,
      "transaction_change_30d": 10.5048,
      "card_spend_change_30d": -9.4143,
      "app_login_change_30d": 22.7557,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -9.6276,
      "upi_share_of_spend": 0.3229,
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
      "days_since_last_transaction": 6,
      "balance_change_30d": 16.2127,
      "transaction_change_30d": 34.9838,
      "card_spend_change_30d": 15.5416,
      "app_login_change_30d": 10.0919,
      "salary_missing_days": 2.0,
      "external_transfer_change_30d": 8.1185,
      "upi_share_of_spend": 0.3233,
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
    "tenure_months": 86,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 2,
    "has_credit_card": 0,
    "has_loan": 0,
    "days_since_last_transaction": 6,
    "balance_change_30d": 16.2127,
    "transaction_change_30d": 34.9838,
    "card_spend_change_30d": 15.5416,
    "app_login_change_30d": 10.0919,
    "salary_missing_days": 2.0,
    "external_transfer_change_30d": 8.1185,
    "upi_share_of_spend": 0.3233,
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
      "tenure_months": 86,
      "age": 41,
      "customer_yearly_value": 35721.482,
      "products_count": 2,
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
    "served_at": "2026-08-31T01:57:54",
    "elapsed_ms": 11628.14,
    "timings_ms": {
      "model1": 821.46,
      "model2": 10806.4
    },
    "customer_id": "C15968",
    "customer_name": "Widisha Parmer",
    "snapshot_date": "2026-06-01"
  },
  "model1": {
    "churn_probability": 1.75,
    "raw_churn_probability": 15.49,
    "probability_mode": "sigmoid",
    "risk_score": 5.25,
    "churn_prediction": "No",
    "risk_level": "Low",
    "top_risk_factors": [
      {
        "factor": "max_days_since_last_transaction_3m",
        "value": 6.0,
        "message": "Customer has gone longer without transacting.",
        "contribution": 0.007986090146005154
      },
      {
        "factor": "app_login_change_30d_trend_6m",
        "value": 0.716365714285715,
        "message": "This signal increased churn risk.",
        "contribution": 0.00718017527833581
      },
      {
        "factor": "avg_transaction_change_30d_6m",
        "value": 10.368816666666667,
        "message": "This signal increased churn risk.",
        "contribution": 0.005994649603962898
      },
      {
        "factor": "count_balance_drop_3m",
        "value": 0,
        "message": "This signal increased churn risk.",
        "contribution": 0.005567824002355337
      },
      {
        "factor": "count_balance_drop_6m",
        "value": 3,
        "message": "This signal increased churn risk.",
        "contribution": 0.005011255852878094
      }
    ]
  },
  "model2_input": {
    "customer_context": {
      "age": 41,
      "tenure_months": 86,
      "customer_segment": "salary",
      "income_regularity": "regular",
      "customer_yearly_value": 35721.482,
      "products_count": 2,
      "has_credit_card": 0,
      "has_loan": 0
    },
    "behavior": {
      "days_since_last_transaction": 6,
      "balance_change_30d": 16.2127,
      "transaction_change_30d": 34.9838,
      "card_spend_change_30d": 15.5416,
      "app_login_change_30d": 10.0919,
      "salary_missing_days": 2,
      "external_transfer_change_30d": 8.1185,
      "upi_share_of_spend": 0.3233,
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
      "churn_probability": 0.0175,
      "churn_prediction": "No",
      "risk_level": "Low",
      "top_risk_factors": [
        {
          "factor": "days_since_last_transaction",
          "value": 6
        },
        {
          "factor": "app_login_change_30d",
          "value": 10.0919
        },
        {
          "factor": "transaction_change_30d",
          "value": 34.9838
        }
      ]
    },
    "eligible_actions": [
      "FINANCIAL_GUIDANCE",
      "RE_ENGAGEMENT",
      "MONITOR"
    ],
    "case_id": "C15968"
  },
  "model2": {
    "case_id": "C15968",
    "ok": true,
    "prediction": {
      "evidence": [
        "balance_change_30d=16.2",
        "transaction_change_30d=34.9"
      ],
      "primary_reason": "FINANCIAL_STRESS",
      "reasoning_summary": "The relationship looks stuck in a financial rut. Digital friction fits because transaction_change_30d=34.9 and balance_change_30d=16.2 suggest this. FINANCIAL_GUIDANCE fits because complaints_30d=0.",
      "recommended_action": "FINANCIAL_GUIDANCE",
      "secondary_reasons": [],
      "urgency": "MEDIUM"
    },
    "warnings": [],
    "raw_text": "{\"evidence\":[\"balance_change_30d=16.2\",\"transaction_change_30d=34.9\"],\"primary_reason\":\"FINANCIAL_STRESS\",\"reasoning_summary\":\"The relationship looks stuck in a financial rut. Digital friction fits because transaction_change_30d=34.9 and balance_change_30d=16.2 suggest this. FINANCIAL_GUIDANCE fits because complaints_30d=0.\",\"recommended_action\":\"FINANCIAL_GUIDANCE\",\"secondary_reasons\":[],\"urgency\":\"MEDIUM\"}",
    "error": null,
    "latency_s": 10.806,
    "simple_output": "Reason: FINANCIAL_STRESS | Urgency: MEDIUM | Action: FINANCIAL_GUIDANCE | Why: The relationship looks stuck in a financial rut. Digital friction fits because transaction_change_30d=34.9 and balance_change_30d=16.2 suggest this. FINANCIAL_GUIDANCE fits because complaints_30d=0."
  }
}
```

### Nihal Bakshi (`C16055`)

- OK: `True`
- Shape errors: `[]`
- Simple output: Reason: FEE_DISSATISFACTION | Urgency: MEDIUM | Action: FEE_WAIVER_REVIEW | Why: Complaint evidence suggests dissatisfaction with fees or charges. Evidence suggests this because complaints_30d=1; complaint_text describes a recent fee or charge dispute.

Request:

```json
{
  "customer_id": "C16055",
  "customer_name": "Nihal Bakshi",
  "prediction_date": "2026-06-01",
  "snapshot_date": "2026-06-01",
  "target_month": "2026-07-01",
  "profile": {
    "tenure_months": 45,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 2,
    "has_credit_card": 0,
    "has_loan": 0
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 12,
      "balance_change_30d": 11.4446,
      "transaction_change_30d": -32.7547,
      "card_spend_change_30d": -1.4527,
      "app_login_change_30d": 3.6652,
      "salary_missing_days": 4.0,
      "external_transfer_change_30d": 51.1865,
      "upi_share_of_spend": 0.0203,
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
      "days_since_last_transaction": 11,
      "balance_change_30d": -7.757,
      "transaction_change_30d": -23.1393,
      "card_spend_change_30d": -1.8422,
      "app_login_change_30d": -23.4613,
      "salary_missing_days": 6.0,
      "external_transfer_change_30d": 61.1837,
      "upi_share_of_spend": 0.087,
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
      "balance_change_30d": -25.8934,
      "transaction_change_30d": -19.7608,
      "card_spend_change_30d": -9.2891,
      "app_login_change_30d": -34.7769,
      "salary_missing_days": 2.0,
      "external_transfer_change_30d": 16.0861,
      "upi_share_of_spend": 0.0334,
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
      "days_since_last_transaction": 6,
      "balance_change_30d": 1.1176,
      "transaction_change_30d": -10.095,
      "card_spend_change_30d": -22.8551,
      "app_login_change_30d": 10.6016,
      "salary_missing_days": 3.0,
      "external_transfer_change_30d": 28.3841,
      "upi_share_of_spend": 0.0,
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
      "balance_change_30d": -18.9623,
      "transaction_change_30d": -13.0714,
      "card_spend_change_30d": -15.0381,
      "app_login_change_30d": -11.2394,
      "salary_missing_days": 3.0,
      "external_transfer_change_30d": 13.8971,
      "upi_share_of_spend": 0.0,
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
      "days_since_last_transaction": 9,
      "balance_change_30d": -4.4099,
      "transaction_change_30d": 14.0192,
      "card_spend_change_30d": -5.1574,
      "app_login_change_30d": -18.5881,
      "salary_missing_days": 1.0,
      "external_transfer_change_30d": 32.8134,
      "upi_share_of_spend": 0.0,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 39.0523,
      "emi_bounce_30d": 0
    }
  ],
  "customer": {
    "tenure_months": 45,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 2,
    "has_credit_card": 0,
    "has_loan": 0,
    "days_since_last_transaction": 9,
    "balance_change_30d": -4.4099,
    "transaction_change_30d": 14.0192,
    "card_spend_change_30d": -5.1574,
    "app_login_change_30d": -18.5881,
    "salary_missing_days": 1.0,
    "external_transfer_change_30d": 32.8134,
    "upi_share_of_spend": 0.0,
    "fd_maturing_in_30d": 0,
    "products_dropped_90d": 0,
    "complaints_30d": 1,
    "unresolved_complaints": 0,
    "failed_transactions_30d": 1,
    "avg_resolution_time_hrs": 39.0523,
    "emi_bounce_30d": 0
  },
  "extra_context": {
    "customer_profile": {
      "segment": "salary",
      "income_regularity": "regular",
      "tenure_months": 45,
      "age": 38,
      "customer_yearly_value": 23442.0384,
      "products_count": 2,
      "has_credit_card": 0,
      "has_loan": 0,
      "value_tier": "low"
    },
    "recent_complaint_text": "Every quarter some new charge appears. I am losing trust in this bank."
  }
}
```

Response:

```json
{
  "meta": {
    "endpoint": "/predict/both",
    "served_at": "2026-08-31T01:58:06",
    "elapsed_ms": 11872.1,
    "timings_ms": {
      "model1": 272.0,
      "model2": 11599.61
    },
    "customer_id": "C16055",
    "customer_name": "Nihal Bakshi",
    "snapshot_date": "2026-06-01"
  },
  "model1": {
    "churn_probability": 4.9,
    "raw_churn_probability": 38.33,
    "probability_mode": "sigmoid",
    "risk_score": 14.71,
    "churn_prediction": "No",
    "risk_level": "Low",
    "top_risk_factors": [
      {
        "factor": "latest_avg_resolution_time_hrs",
        "value": 39.0523,
        "message": "Recent complaints took longer to resolve.",
        "contribution": 0.2964561879634857
      },
      {
        "factor": "sum_failed_transactions_30d_6m",
        "value": 8.0,
        "message": "Customer has recent failed transactions.",
        "contribution": 0.16320987045764923
      },
      {
        "factor": "latest_upi_share_of_spend",
        "value": 0.0,
        "message": "This signal increased churn risk.",
        "contribution": 0.0936674177646637
      },
      {
        "factor": "avg_external_transfer_change_30d_3m",
        "value": 25.031533333333332,
        "message": "External transfers have increased.",
        "contribution": 0.031038744375109673
      },
      {
        "factor": "avg_card_spend_change_30d_3m",
        "value": -14.350200000000001,
        "message": "Card spending has been falling across recent months.",
        "contribution": 0.024022221565246582
      }
    ]
  },
  "model2_input": {
    "customer_context": {
      "age": 38,
      "tenure_months": 45,
      "customer_segment": "salary",
      "income_regularity": "regular",
      "customer_yearly_value": 23442.0384,
      "products_count": 2,
      "has_credit_card": 0,
      "has_loan": 0
    },
    "behavior": {
      "days_since_last_transaction": 9,
      "balance_change_30d": -4.4099,
      "transaction_change_30d": 14.0192,
      "card_spend_change_30d": -5.1574,
      "app_login_change_30d": -18.5881,
      "salary_missing_days": 1,
      "external_transfer_change_30d": 32.8134,
      "upi_share_of_spend": 0.0,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "emi_bounce_30d": 0
    },
    "service_evidence": {
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 39.0523,
      "complaint_text": "Every quarter some new charge appears. I am losing trust in this bank."
    },
    "model1": {
      "churn_probability": 0.049,
      "churn_prediction": "No",
      "risk_level": "Low",
      "top_risk_factors": [
        {
          "factor": "failed_transactions_30d",
          "value": 1
        },
        {
          "factor": "upi_share_of_spend",
          "value": 0.0
        },
        {
          "factor": "external_transfer_change_30d",
          "value": 32.8134
        }
      ]
    },
    "eligible_actions": [
      "FEE_WAIVER_REVIEW",
      "FINANCIAL_GUIDANCE",
      "SERVICE_RECOVERY",
      "PRODUCT_REVIEW",
      "MONITOR"
    ],
    "case_id": "C16055"
  },
  "model2": {
    "case_id": "C16055",
    "ok": true,
    "prediction": {
      "evidence": [
        "complaints_30d=1",
        "unresolved_complaints=0",
        "avg_resolution_time_hrs=39.1",
        "complaint_text describes a recent fee or charge dispute"
      ],
      "primary_reason": "FEE_DISSATISFACTION",
      "reasoning_summary": "Complaint evidence suggests dissatisfaction with fees or charges. Evidence suggests this because complaints_30d=1; complaint_text describes a recent fee or charge dispute.",
      "recommended_action": "FEE_WAIVER_REVIEW",
      "secondary_reasons": [],
      "urgency": "MEDIUM"
    },
    "warnings": [
      "evidence: 'unresolved_complaints=0' cites a zero/null value, which is not evidence; remove it"
    ],
    "raw_text": "{\"evidence\":[\"complaints_30d=1\",\"failed_transactions_30d=1\",\"avg_resolution_time_hrs=39.1\",\"complaint_text describes a real issue without clear escalation-level severity\"],\"primary_reason\":\"SERVICE_DISSATISFACTION\",\"reasoning_summary\":\"Complaint escalation because complaints_30d=1 and failed_transactions_30d=1 indicate SERVICE_DISSATISFACTION.\",\"recommended_action\":\"FEE_WAIVER_REVIEW\",\"secondary_reasons\":[],\"urgency\":\"MEDIUM\"}",
    "error": null,
    "latency_s": 11.5994,
    "simple_output": "Reason: FEE_DISSATISFACTION | Urgency: MEDIUM | Action: FEE_WAIVER_REVIEW | Why: Complaint evidence suggests dissatisfaction with fees or charges. Evidence suggests this because complaints_30d=1; complaint_text describes a recent fee or charge dispute."
  }
}
```

### Veer Mody (`C16114`)

- OK: `True`
- Shape errors: `[]`
- Simple output: Reason: UNKNOWN | Urgency: LOW | Action: MONITOR | Why: Complaint and resolution signals are mixed or weak; reason is UNKNOWN.

Request:

```json
{
  "customer_id": "C16114",
  "customer_name": "Veer Mody",
  "prediction_date": "2026-06-01",
  "snapshot_date": "2026-06-01",
  "target_month": "2026-07-01",
  "profile": {
    "tenure_months": 43,
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
      "balance_change_30d": 10.1899,
      "transaction_change_30d": -12.1942,
      "card_spend_change_30d": 23.4548,
      "app_login_change_30d": 7.138,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": 48.6603,
      "upi_share_of_spend": 0.567,
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
      "days_since_last_transaction": 0,
      "balance_change_30d": 12.2355,
      "transaction_change_30d": 12.6497,
      "card_spend_change_30d": -9.052,
      "app_login_change_30d": 16.4175,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -19.5336,
      "upi_share_of_spend": 0.4232,
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
      "days_since_last_transaction": 0,
      "balance_change_30d": 23.1698,
      "transaction_change_30d": 34.0917,
      "card_spend_change_30d": 53.018,
      "app_login_change_30d": 40.047,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -34.9776,
      "upi_share_of_spend": 0.4362,
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
      "balance_change_30d": 38.6064,
      "transaction_change_30d": 34.4454,
      "card_spend_change_30d": 27.9919,
      "app_login_change_30d": 21.3521,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -4.6544,
      "upi_share_of_spend": 0.506,
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
      "balance_change_30d": 13.3119,
      "transaction_change_30d": 37.992,
      "card_spend_change_30d": 9.8534,
      "app_login_change_30d": -13.6651,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": 3.8503,
      "upi_share_of_spend": 0.4543,
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
      "days_since_last_transaction": 0,
      "balance_change_30d": 51.9047,
      "transaction_change_30d": 8.7999,
      "card_spend_change_30d": 60.5928,
      "app_login_change_30d": 17.6363,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -48.2717,
      "upi_share_of_spend": 0.4807,
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
    "tenure_months": 43,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 2,
    "has_credit_card": 1,
    "has_loan": 0,
    "days_since_last_transaction": 0,
    "balance_change_30d": 51.9047,
    "transaction_change_30d": 8.7999,
    "card_spend_change_30d": 60.5928,
    "app_login_change_30d": 17.6363,
    "salary_missing_days": 0.0,
    "external_transfer_change_30d": -48.2717,
    "upi_share_of_spend": 0.4807,
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
      "tenure_months": 43,
      "age": 47,
      "customer_yearly_value": 16777.2047,
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
    "served_at": "2026-08-31T01:58:14",
    "elapsed_ms": 7812.21,
    "timings_ms": {
      "model1": 92.39,
      "model2": 7719.69
    },
    "customer_id": "C16114",
    "customer_name": "Veer Mody",
    "snapshot_date": "2026-06-01"
  },
  "model1": {
    "churn_probability": 3.09,
    "raw_churn_probability": 28.0,
    "probability_mode": "sigmoid",
    "risk_score": 9.26,
    "churn_prediction": "No",
    "risk_level": "Low",
    "top_risk_factors": [
      {
        "factor": "latest_vs_avg_card_spend_change_30d_available_history",
        "value": 32.94964999999999,
        "message": "This signal increased churn risk.",
        "contribution": 0.12283024936914444
      },
      {
        "factor": "latest_external_transfer_change_30d",
        "value": -48.2717,
        "message": "This signal increased churn risk.",
        "contribution": 0.06565947085618973
      },
      {
        "factor": "latest_vs_avg_balance_change_30d_available_history",
        "value": 27.00166666666667,
        "message": "This signal increased churn risk.",
        "contribution": 0.05900277569890022
      },
      {
        "factor": "card_spend_change_30d_trend_6m",
        "value": 6.210859999999996,
        "message": "This signal increased churn risk.",
        "contribution": 0.05794950947165489
      },
      {
        "factor": "latest_vs_avg_external_transfer_change_30d_available_history",
        "value": -39.11725,
        "message": "This signal increased churn risk.",
        "contribution": 0.05388861894607544
      }
    ]
  },
  "model2_input": {
    "customer_context": {
      "age": 47,
      "tenure_months": 43,
      "customer_segment": "salary",
      "income_regularity": "regular",
      "customer_yearly_value": 16777.2047,
      "products_count": 2,
      "has_credit_card": 1,
      "has_loan": 0
    },
    "behavior": {
      "days_since_last_transaction": 0,
      "balance_change_30d": 51.9047,
      "transaction_change_30d": 8.7999,
      "card_spend_change_30d": 60.5928,
      "app_login_change_30d": 17.6363,
      "salary_missing_days": 0,
      "external_transfer_change_30d": -48.2717,
      "upi_share_of_spend": 0.4807,
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
      "churn_probability": 0.0309,
      "churn_prediction": "No",
      "risk_level": "Low",
      "top_risk_factors": [
        {
          "factor": "card_spend_change_30d",
          "value": 60.5928
        },
        {
          "factor": "external_transfer_change_30d",
          "value": -48.2717
        },
        {
          "factor": "balance_change_30d",
          "value": 51.9047
        }
      ]
    },
    "eligible_actions": [
      "RE_ENGAGEMENT",
      "PRODUCT_REVIEW",
      "MONITOR"
    ],
    "case_id": "C16114"
  },
  "model2": {
    "case_id": "C16114",
    "ok": true,
    "prediction": {
      "evidence": [
        "complaints_30d=0",
        "unresolved_complaints=0",
        "avg_resolution_time_hrs=0.0"
      ],
      "primary_reason": "UNKNOWN",
      "reasoning_summary": "Complaint and resolution signals are mixed or weak; reason is UNKNOWN.",
      "recommended_action": "MONITOR",
      "secondary_reasons": [],
      "urgency": "LOW"
    },
    "warnings": [
      "evidence: 'complaints_30d=0' cites a zero/null value, which is not evidence; remove it",
      "evidence: 'unresolved_complaints=0' cites a zero/null value, which is not evidence; remove it",
      "evidence: 'avg_resolution_time_hrs=0.0' cites a zero/null value, which is not evidence; remove it"
    ],
    "raw_text": "{\"evidence\":[\"complaints_30d=0\",\"unresolved_complaints=0\",\"avg_resolution_time_hrs=0.0\"],\"primary_reason\":\"LOW_ENGAGEMENT\",\"reasoning_summary\":\"Days_since_last_transaction=0 and transaction_change_30d=8.8 suggest this because complaint_text=null.\",\"recommended_action\":\"RE_ENGAGEMENT\",\"secondary_reasons\":[],\"urgency\":\"MEDIUM\"}",
    "error": null,
    "latency_s": 7.7195,
    "simple_output": "Reason: UNKNOWN | Urgency: LOW | Action: MONITOR | Why: Complaint and resolution signals are mixed or weak; reason is UNKNOWN."
  }
}
```

### Nakul Iyengar (`C17377`)

- OK: `True`
- Shape errors: `[]`
- Simple output: Reason: SERVICE_DISSATISFACTION | Urgency: MEDIUM | Action: SERVICE_RECOVERY | Why: Complaint escalation because complaints_30d=1 and avg_resolution_time_hrs=40.6 suggest a service issue.

Request:

```json
{
  "customer_id": "C17377",
  "customer_name": "Nakul Iyengar",
  "prediction_date": "2026-06-01",
  "snapshot_date": "2026-06-01",
  "target_month": "2026-07-01",
  "profile": {
    "tenure_months": 82,
    "customer_segment": "business",
    "income_regularity": "irregular",
    "products_count": 2,
    "has_credit_card": 0,
    "has_loan": 0
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 0,
      "balance_change_30d": -18.8514,
      "transaction_change_30d": 0.6624,
      "card_spend_change_30d": 4.9172,
      "app_login_change_30d": -8.3314,
      "salary_missing_days": null,
      "external_transfer_change_30d": 4.8339,
      "upi_share_of_spend": 0.4743,
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
      "balance_change_30d": -15.1086,
      "transaction_change_30d": -9.6518,
      "card_spend_change_30d": -14.2244,
      "app_login_change_30d": -18.1807,
      "salary_missing_days": null,
      "external_transfer_change_30d": 60.1628,
      "upi_share_of_spend": 0.4493,
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
      "balance_change_30d": 8.17,
      "transaction_change_30d": -20.8598,
      "card_spend_change_30d": -26.7363,
      "app_login_change_30d": -8.3442,
      "salary_missing_days": null,
      "external_transfer_change_30d": 82.918,
      "upi_share_of_spend": 0.4931,
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
      "balance_change_30d": -9.421,
      "transaction_change_30d": -12.9255,
      "card_spend_change_30d": -9.0552,
      "app_login_change_30d": -35.2922,
      "salary_missing_days": null,
      "external_transfer_change_30d": 3.1223,
      "upi_share_of_spend": 0.5033,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 30.0448,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-05-01",
      "days_since_last_transaction": 13,
      "balance_change_30d": -25.726,
      "transaction_change_30d": -44.8175,
      "card_spend_change_30d": -38.1857,
      "app_login_change_30d": -21.147,
      "salary_missing_days": null,
      "external_transfer_change_30d": 49.5625,
      "upi_share_of_spend": 0.5387,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 1,
      "failed_transactions_30d": 2,
      "avg_resolution_time_hrs": 36.2124,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-06-01",
      "days_since_last_transaction": 18,
      "balance_change_30d": -51.7596,
      "transaction_change_30d": -40.8781,
      "card_spend_change_30d": -29.5901,
      "app_login_change_30d": -85.8797,
      "salary_missing_days": null,
      "external_transfer_change_30d": 78.6855,
      "upi_share_of_spend": 0.5883,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 3,
      "avg_resolution_time_hrs": 40.5667,
      "emi_bounce_30d": 0
    }
  ],
  "customer": {
    "tenure_months": 82,
    "customer_segment": "business",
    "income_regularity": "irregular",
    "products_count": 2,
    "has_credit_card": 0,
    "has_loan": 0,
    "days_since_last_transaction": 18,
    "balance_change_30d": -51.7596,
    "transaction_change_30d": -40.8781,
    "card_spend_change_30d": -29.5901,
    "app_login_change_30d": -85.8797,
    "salary_missing_days": null,
    "external_transfer_change_30d": 78.6855,
    "upi_share_of_spend": 0.5883,
    "fd_maturing_in_30d": 0,
    "products_dropped_90d": 0,
    "complaints_30d": 1,
    "unresolved_complaints": 0,
    "failed_transactions_30d": 3,
    "avg_resolution_time_hrs": 40.5667,
    "emi_bounce_30d": 0
  },
  "extra_context": {
    "customer_profile": {
      "segment": "business",
      "income_regularity": "irregular",
      "tenure_months": 82,
      "age": 41,
      "customer_yearly_value": 38075.7367,
      "products_count": 2,
      "has_credit_card": 0,
      "has_loan": 0,
      "value_tier": "medium"
    },
    "recent_complaint_text": "Kindly activate my card for online transactions, it keeps declining."
  }
}
```

Response:

```json
{
  "meta": {
    "endpoint": "/predict/both",
    "served_at": "2026-08-31T01:58:25",
    "elapsed_ms": 11324.47,
    "timings_ms": {
      "model1": 70.93,
      "model2": 11253.4
    },
    "customer_id": "C17377",
    "customer_name": "Nakul Iyengar",
    "snapshot_date": "2026-06-01"
  },
  "model1": {
    "churn_probability": 41.38,
    "raw_churn_probability": 94.53,
    "probability_mode": "sigmoid",
    "risk_score": 78.02,
    "churn_prediction": "Yes",
    "risk_level": "High",
    "top_risk_factors": [
      {
        "factor": "latest_days_since_last_transaction",
        "value": 18,
        "message": "Customer has gone longer without transacting.",
        "contribution": 0.6080758571624756
      },
      {
        "factor": "latest_transaction_change_30d",
        "value": -40.8781,
        "message": "Transaction activity has been falling across recent months.",
        "contribution": 0.4581383764743805
      },
      {
        "factor": "latest_vs_avg_upi_share_of_spend_available_history",
        "value": 0.0804666666666668,
        "message": "A larger share of spending is happening through UPI.",
        "contribution": 0.22038690745830536
      },
      {
        "factor": "latest_balance_change_30d",
        "value": -51.7596,
        "message": "Balance has been falling across recent months.",
        "contribution": 0.2155243158340454
      },
      {
        "factor": "days_since_last_transaction_trend_6m",
        "value": 3.1999999999999993,
        "message": "Customer has gone longer without transacting.",
        "contribution": 0.1663242131471634
      }
    ]
  },
  "model2_input": {
    "customer_context": {
      "age": 41,
      "tenure_months": 82,
      "customer_segment": "business",
      "income_regularity": "irregular",
      "customer_yearly_value": 38075.7367,
      "products_count": 2,
      "has_credit_card": 0,
      "has_loan": 0
    },
    "behavior": {
      "days_since_last_transaction": 18,
      "balance_change_30d": -51.7596,
      "transaction_change_30d": -40.8781,
      "card_spend_change_30d": -29.5901,
      "app_login_change_30d": -85.8797,
      "salary_missing_days": null,
      "external_transfer_change_30d": 78.6855,
      "upi_share_of_spend": 0.5883,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "emi_bounce_30d": 0
    },
    "service_evidence": {
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 3,
      "avg_resolution_time_hrs": 40.5667,
      "complaint_text": "Kindly activate my card for online transactions, it keeps declining."
    },
    "model1": {
      "churn_probability": 0.4138,
      "churn_prediction": "Yes",
      "risk_level": "High",
      "top_risk_factors": [
        {
          "factor": "days_since_last_transaction",
          "value": 18
        },
        {
          "factor": "transaction_change_30d",
          "value": -40.8781
        },
        {
          "factor": "upi_share_of_spend",
          "value": 0.5883
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
    "case_id": "C17377"
  },
  "model2": {
    "case_id": "C17377",
    "ok": true,
    "prediction": {
      "evidence": [
        "complaints_30d=1",
        "unresolved_complaints=0",
        "avg_resolution_time_hrs=40.6",
        "complaint_text describes a recent service issue"
      ],
      "primary_reason": "SERVICE_DISSATISFACTION",
      "reasoning_summary": "Complaint escalation because complaints_30d=1 and avg_resolution_time_hrs=40.6 suggest a service issue.",
      "recommended_action": "SERVICE_RECOVERY",
      "secondary_reasons": [],
      "urgency": "MEDIUM"
    },
    "warnings": [
      "evidence: 'unresolved_complaints=0' cites a zero/null value, which is not evidence; remove it",
      "reasoning_summary: describes COMPLAINT_ESCALATION but recommended_action is SERVICE_RECOVERY; rewrite the summary around the action you chose"
    ],
    "raw_text": "{\"evidence\":[\"complaints_30d=1\",\"unresolved_complaints=0\",\"avg_resolution_time_hrs=40.6\",\"complaint_text describes a real service issue without being complaint_escalation or escalation-level\"],\"primary_reason\":\"SERVICE_DISSATISFACTION\",\"reasoning_summary\":\"Complaint escalation because complaints_30d=1 and avg_resolution_time_hrs=40.6 suggest the issue is unresolved or operationally serious.\",\"recommended_action\":\"SERVICE_RECOVERY\",\"secondary_reasons\":[],\"urgency\":\"HIGH\"}",
    "error": null,
    "latency_s": 11.2532,
    "simple_output": "Reason: SERVICE_DISSATISFACTION | Urgency: MEDIUM | Action: SERVICE_RECOVERY | Why: Complaint escalation because complaints_30d=1 and avg_resolution_time_hrs=40.6 suggest a service issue."
  }
}
```

### Jatin Buch (`C17417`)

- OK: `True`
- Shape errors: `[]`
- Simple output: Reason: DIGITAL_FRICTION | Urgency: MEDIUM | Action: MONITOR | Why: Digital friction is the strongest supported signal here because complaints_30d=0 and unresolved_complaints=0 suggest a digital or transaction experience issue rather than a product problem.

Request:

```json
{
  "customer_id": "C17417",
  "customer_name": "Jatin Buch",
  "prediction_date": "2026-06-01",
  "snapshot_date": "2026-06-01",
  "target_month": "2026-07-01",
  "profile": {
    "tenure_months": 115,
    "customer_segment": "farmer",
    "income_regularity": "seasonal",
    "products_count": 2,
    "has_credit_card": 0,
    "has_loan": 1
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 19,
      "balance_change_30d": -25.9694,
      "transaction_change_30d": -19.6342,
      "card_spend_change_30d": -49.3065,
      "app_login_change_30d": 14.8926,
      "salary_missing_days": null,
      "external_transfer_change_30d": 34.7564,
      "upi_share_of_spend": 0.4316,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 1,
      "complaints_30d": 4,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 9.2642,
      "emi_bounce_30d": 1
    },
    {
      "snapshot_date": "2026-02-01",
      "days_since_last_transaction": 14,
      "balance_change_30d": 2.6549,
      "transaction_change_30d": -13.3589,
      "card_spend_change_30d": -1.6479,
      "app_login_change_30d": -3.2125,
      "salary_missing_days": null,
      "external_transfer_change_30d": -3.7999,
      "upi_share_of_spend": 0.3876,
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
      "days_since_last_transaction": 21,
      "balance_change_30d": -13.4377,
      "transaction_change_30d": -34.3784,
      "card_spend_change_30d": -33.5273,
      "app_login_change_30d": -26.7066,
      "salary_missing_days": null,
      "external_transfer_change_30d": 62.7617,
      "upi_share_of_spend": 0.4526,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 35.8721,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-04-01",
      "days_since_last_transaction": 13,
      "balance_change_30d": -16.9877,
      "transaction_change_30d": -31.1843,
      "card_spend_change_30d": -22.6934,
      "app_login_change_30d": -41.1904,
      "salary_missing_days": null,
      "external_transfer_change_30d": 54.0619,
      "upi_share_of_spend": 0.4332,
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
      "days_since_last_transaction": 4,
      "balance_change_30d": -14.7489,
      "transaction_change_30d": 2.4358,
      "card_spend_change_30d": -21.5293,
      "app_login_change_30d": 16.7335,
      "salary_missing_days": null,
      "external_transfer_change_30d": -13.3195,
      "upi_share_of_spend": 0.3173,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 1,
      "failed_transactions_30d": 2,
      "avg_resolution_time_hrs": 20.8333,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-06-01",
      "days_since_last_transaction": 13,
      "balance_change_30d": -10.5741,
      "transaction_change_30d": 9.3993,
      "card_spend_change_30d": -0.6213,
      "app_login_change_30d": 7.914,
      "salary_missing_days": null,
      "external_transfer_change_30d": 7.0881,
      "upi_share_of_spend": 0.3805,
      "fd_maturing_in_30d": 1,
      "products_dropped_90d": 0,
      "complaints_30d": 0,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 5,
      "avg_resolution_time_hrs": 0.0,
      "emi_bounce_30d": 0
    }
  ],
  "customer": {
    "tenure_months": 115,
    "customer_segment": "farmer",
    "income_regularity": "seasonal",
    "products_count": 2,
    "has_credit_card": 0,
    "has_loan": 1,
    "days_since_last_transaction": 13,
    "balance_change_30d": -10.5741,
    "transaction_change_30d": 9.3993,
    "card_spend_change_30d": -0.6213,
    "app_login_change_30d": 7.914,
    "salary_missing_days": null,
    "external_transfer_change_30d": 7.0881,
    "upi_share_of_spend": 0.3805,
    "fd_maturing_in_30d": 1,
    "products_dropped_90d": 0,
    "complaints_30d": 0,
    "unresolved_complaints": 0,
    "failed_transactions_30d": 5,
    "avg_resolution_time_hrs": 0.0,
    "emi_bounce_30d": 0
  },
  "extra_context": {
    "customer_profile": {
      "segment": "farmer",
      "income_regularity": "seasonal",
      "tenure_months": 115,
      "age": 33,
      "customer_yearly_value": 12436.0429,
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
    "served_at": "2026-08-31T01:58:32",
    "elapsed_ms": 7166.64,
    "timings_ms": {
      "model1": 388.48,
      "model2": 6777.81
    },
    "customer_id": "C17417",
    "customer_name": "Jatin Buch",
    "snapshot_date": "2026-06-01"
  },
  "model1": {
    "churn_probability": 4.82,
    "raw_churn_probability": 37.97,
    "probability_mode": "sigmoid",
    "risk_score": 14.47,
    "churn_prediction": "No",
    "risk_level": "Low",
    "top_risk_factors": [
      {
        "factor": "sum_failed_transactions_30d_3m",
        "value": 8.0,
        "message": "Customer has recent failed transactions.",
        "contribution": 0.26608189940452576
      },
      {
        "factor": "latest_days_since_last_transaction",
        "value": 13,
        "message": "Customer has gone longer without transacting.",
        "contribution": 0.22516833245754242
      },
      {
        "factor": "latest_failed_transactions_30d",
        "value": 5,
        "message": "Customer has recent failed transactions.",
        "contribution": 0.1755426675081253
      },
      {
        "factor": "latest_fd_maturing_in_30d",
        "value": 1,
        "message": "Customer has a fixed deposit maturing soon.",
        "contribution": 0.1131335124373436
      },
      {
        "factor": "sum_fd_maturing_in_30d_3m",
        "value": 1.0,
        "message": "Customer has a fixed deposit maturing soon.",
        "contribution": 0.09306856244802475
      }
    ]
  },
  "model2_input": {
    "customer_context": {
      "age": 33,
      "tenure_months": 115,
      "customer_segment": "farmer",
      "income_regularity": "seasonal",
      "customer_yearly_value": 12436.0429,
      "products_count": 2,
      "has_credit_card": 0,
      "has_loan": 1
    },
    "behavior": {
      "days_since_last_transaction": 13,
      "balance_change_30d": -10.5741,
      "transaction_change_30d": 9.3993,
      "card_spend_change_30d": -0.6213,
      "app_login_change_30d": 7.914,
      "salary_missing_days": null,
      "external_transfer_change_30d": 7.0881,
      "upi_share_of_spend": 0.3805,
      "fd_maturing_in_30d": 1,
      "products_dropped_90d": 0,
      "emi_bounce_30d": 0
    },
    "service_evidence": {
      "complaints_30d": 0,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 5,
      "avg_resolution_time_hrs": 0.0,
      "complaint_text": null
    },
    "model1": {
      "churn_probability": 0.0482,
      "churn_prediction": "No",
      "risk_level": "Low",
      "top_risk_factors": [
        {
          "factor": "failed_transactions_30d",
          "value": 5
        },
        {
          "factor": "days_since_last_transaction",
          "value": 13
        },
        {
          "factor": "fd_maturing_in_30d",
          "value": 1
        }
      ]
    },
    "eligible_actions": [
      "SERVICE_RECOVERY",
      "PRODUCT_REVIEW",
      "MONITOR"
    ],
    "case_id": "C17417"
  },
  "model2": {
    "case_id": "C17417",
    "ok": true,
    "prediction": {
      "evidence": [
        "app_login_change_30d=7.9",
        "transaction_change_30d=9.4",
        "external_transfer_change_30d=7.1"
      ],
      "primary_reason": "DIGITAL_FRICTION",
      "reasoning_summary": "Digital friction is the strongest supported signal here because complaints_30d=0 and unresolved_complaints=0 suggest a digital or transaction experience issue rather than a product problem.",
      "recommended_action": "MONITOR",
      "secondary_reasons": [],
      "urgency": "MEDIUM"
    },
    "warnings": [],
    "raw_text": "{\"evidence\":[\"app_login_change_30d=7.9\",\"transaction_change_30d=9.4\",\"external_transfer_change_30d=7.1\"],\"primary_reason\":\"DIGITAL_FRICTION\",\"reasoning_summary\":\"Digital friction is the strongest supported signal here because complaints_30d=0 and unresolved_complaints=0 suggest a digital or transaction experience issue rather than a product problem.\",\"recommended_action\":\"MONITOR\",\"secondary_reasons\":[],\"urgency\":\"MEDIUM\"}",
    "error": null,
    "latency_s": 6.7741,
    "simple_output": "Reason: DIGITAL_FRICTION | Urgency: MEDIUM | Action: MONITOR | Why: Digital friction is the strongest supported signal here because complaints_30d=0 and unresolved_complaints=0 suggest a digital or transaction experience issue rather than a product problem."
  }
}
```

### Girindra Brar (`C18347`)

- OK: `True`
- Shape errors: `[]`
- Simple output: Reason: SERVICE_DISSATISFACTION | Urgency: HIGH | Action: COMPLAINT_ESCALATION | Why: Complaint escalation because complaints_30d=6 and unresolved_complaints=6 indicate a service issue.

Request:

```json
{
  "customer_id": "C18347",
  "customer_name": "Girindra Brar",
  "prediction_date": "2026-04-01",
  "snapshot_date": "2026-04-01",
  "target_month": "2026-05-01",
  "profile": {
    "tenure_months": 62,
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
      "balance_change_30d": -0.5846,
      "transaction_change_30d": 4.1693,
      "card_spend_change_30d": 4.3649,
      "app_login_change_30d": 25.6005,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": 14.6162,
      "upi_share_of_spend": 0.428,
      "fd_maturing_in_30d": 1,
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
      "balance_change_30d": -4.5044,
      "transaction_change_30d": -14.2963,
      "card_spend_change_30d": -13.5266,
      "app_login_change_30d": 10.6638,
      "salary_missing_days": 3.0,
      "external_transfer_change_30d": 4.5135,
      "upi_share_of_spend": 0.4272,
      "fd_maturing_in_30d": 1,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 30.9402,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-03-01",
      "days_since_last_transaction": 11,
      "balance_change_30d": -25.8699,
      "transaction_change_30d": -16.0756,
      "card_spend_change_30d": -2.6028,
      "app_login_change_30d": -1.012,
      "salary_missing_days": 2.0,
      "external_transfer_change_30d": 2.1761,
      "upi_share_of_spend": 0.4796,
      "fd_maturing_in_30d": 1,
      "products_dropped_90d": 0,
      "complaints_30d": 2,
      "unresolved_complaints": 2,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 76.7104,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-04-01",
      "days_since_last_transaction": 17,
      "balance_change_30d": 1.6898,
      "transaction_change_30d": -2.7498,
      "card_spend_change_30d": -0.4131,
      "app_login_change_30d": 7.7495,
      "salary_missing_days": 3.0,
      "external_transfer_change_30d": 24.86,
      "upi_share_of_spend": 0.4881,
      "fd_maturing_in_30d": 1,
      "products_dropped_90d": 0,
      "complaints_30d": 6,
      "unresolved_complaints": 6,
      "failed_transactions_30d": 10,
      "avg_resolution_time_hrs": 126.7559,
      "emi_bounce_30d": 0
    }
  ],
  "customer": {
    "tenure_months": 62,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 2,
    "has_credit_card": 1,
    "has_loan": 0,
    "days_since_last_transaction": 17,
    "balance_change_30d": 1.6898,
    "transaction_change_30d": -2.7498,
    "card_spend_change_30d": -0.4131,
    "app_login_change_30d": 7.7495,
    "salary_missing_days": 3.0,
    "external_transfer_change_30d": 24.86,
    "upi_share_of_spend": 0.4881,
    "fd_maturing_in_30d": 1,
    "products_dropped_90d": 0,
    "complaints_30d": 6,
    "unresolved_complaints": 6,
    "failed_transactions_30d": 10,
    "avg_resolution_time_hrs": 126.7559,
    "emi_bounce_30d": 0
  },
  "extra_context": {
    "customer_profile": {
      "segment": "salary",
      "income_regularity": "regular",
      "tenure_months": 62,
      "age": 44,
      "customer_yearly_value": 50583.5303,
      "products_count": 2,
      "has_credit_card": 1,
      "has_loan": 0,
      "value_tier": "medium"
    },
    "recent_complaint_text": "Please inform in advance when the branch will be closed for audit."
  }
}
```

Response:

```json
{
  "meta": {
    "endpoint": "/predict/both",
    "served_at": "2026-08-31T01:58:37",
    "elapsed_ms": 4854.14,
    "timings_ms": {
      "model1": 566.57,
      "model2": 4287.22
    },
    "customer_id": "C18347",
    "customer_name": "Girindra Brar",
    "snapshot_date": "2026-04-01"
  },
  "model1": {
    "churn_probability": 30.4,
    "raw_churn_probability": 84.23,
    "probability_mode": "sigmoid",
    "risk_score": 73.9,
    "churn_prediction": "Yes",
    "risk_level": "High",
    "top_risk_factors": [
      {
        "factor": "max_avg_resolution_time_hrs_3m",
        "value": 126.7559,
        "message": "Recent complaints took longer to resolve.",
        "contribution": 0.373567670583725
      },
      {
        "factor": "sum_failed_transactions_30d_3m",
        "value": 11.0,
        "message": "Customer has recent failed transactions.",
        "contribution": 0.24237102270126343
      },
      {
        "factor": "latest_avg_resolution_time_hrs",
        "value": 126.7559,
        "message": "Recent complaints took longer to resolve.",
        "contribution": 0.19748570024967194
      },
      {
        "factor": "latest_days_since_last_transaction",
        "value": 17,
        "message": "Customer has gone longer without transacting.",
        "contribution": 0.19322462379932404
      },
      {
        "factor": "latest_salary_missing_days",
        "value": 3.0,
        "message": "Salary or pension was delayed recently.",
        "contribution": 0.17926783859729767
      }
    ]
  },
  "model2_input": {
    "customer_context": {
      "age": 44,
      "tenure_months": 62,
      "customer_segment": "salary",
      "income_regularity": "regular",
      "customer_yearly_value": 50583.5303,
      "products_count": 2,
      "has_credit_card": 1,
      "has_loan": 0
    },
    "behavior": {
      "days_since_last_transaction": 17,
      "balance_change_30d": 1.6898,
      "transaction_change_30d": -2.7498,
      "card_spend_change_30d": -0.4131,
      "app_login_change_30d": 7.7495,
      "salary_missing_days": 3,
      "external_transfer_change_30d": 24.86,
      "upi_share_of_spend": 0.4881,
      "fd_maturing_in_30d": 1,
      "products_dropped_90d": 0,
      "emi_bounce_30d": 0
    },
    "service_evidence": {
      "complaints_30d": 6,
      "unresolved_complaints": 6,
      "failed_transactions_30d": 10,
      "avg_resolution_time_hrs": 126.7559,
      "complaint_text": "Please inform in advance when the branch will be closed for audit."
    },
    "model1": {
      "churn_probability": 0.304,
      "churn_prediction": "Yes",
      "risk_level": "High",
      "top_risk_factors": [
        {
          "factor": "failed_transactions_30d",
          "value": 10
        },
        {
          "factor": "days_since_last_transaction",
          "value": 17
        },
        {
          "factor": "salary_missing_days",
          "value": 3
        }
      ]
    },
    "eligible_actions": [
      "COMPLAINT_ESCALATION",
      "FINANCIAL_GUIDANCE",
      "SERVICE_RECOVERY",
      "PRODUCT_REVIEW",
      "MONITOR"
    ],
    "case_id": "C18347"
  },
  "model2": {
    "case_id": "C18347",
    "ok": true,
    "prediction": {
      "evidence": [
        "complaints_30d=6",
        "unresolved_complaints=6",
        "failed_transactions_30d=10",
        "avg_resolution_time_hrs=126.8",
        "complaint_text describes a recent service issue"
      ],
      "primary_reason": "SERVICE_DISSATISFACTION",
      "reasoning_summary": "Complaint escalation because complaints_30d=6 and unresolved_complaints=6 indicate a service issue.",
      "recommended_action": "COMPLAINT_ESCALATION",
      "secondary_reasons": [],
      "urgency": "HIGH"
    },
    "warnings": [],
    "raw_text": "{\"evidence\":[\"complaints_30d=6\",\"unresolved_complaints=6\",\"failed_transactions_30d=10\",\"avg_resolution_time_hrs=126.8\",\"complaint_text describes a recent service issue\"],\"primary_reason\":\"SERVICE_DISSATISFACTION\",\"reasoning_summary\":\"Complaint escalation because complaints_30d=6 and unresolved_complaints=6 indicate a service issue.\",\"recommended_action\":\"COMPLAINT_ESCALATION\",\"secondary_reasons\":[],\"urgency\":\"HIGH\"}",
    "error": null,
    "latency_s": 4.2822,
    "simple_output": "Reason: SERVICE_DISSATISFACTION | Urgency: HIGH | Action: COMPLAINT_ESCALATION | Why: Complaint escalation because complaints_30d=6 and unresolved_complaints=6 indicate a service issue."
  }
}
```

### Ekanta Oommen (`C18523`)

- OK: `True`
- Shape errors: `[]`
- Simple output: Reason: FINANCIAL_STRESS | Urgency: MEDIUM | Action: PRODUCT_REVIEW | Why: The relationship looks stuck in a financial rut. Product review fits because balance_change_30d=-22.7 and complaints_30d=0 suggest a product-fit problem rather than a service issue.

Request:

```json
{
  "customer_id": "C18523",
  "customer_name": "Ekanta Oommen",
  "prediction_date": "2026-06-01",
  "snapshot_date": "2026-06-01",
  "target_month": "2026-07-01",
  "profile": {
    "tenure_months": 140,
    "customer_segment": "business",
    "income_regularity": "irregular",
    "products_count": 3,
    "has_credit_card": 0,
    "has_loan": 1
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 0,
      "balance_change_30d": -11.8375,
      "transaction_change_30d": -21.5374,
      "card_spend_change_30d": -8.4533,
      "app_login_change_30d": 22.7881,
      "salary_missing_days": null,
      "external_transfer_change_30d": 23.8737,
      "upi_share_of_spend": 0.4987,
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
      "days_since_last_transaction": 1,
      "balance_change_30d": 12.441,
      "transaction_change_30d": 10.9463,
      "card_spend_change_30d": -7.0772,
      "app_login_change_30d": -4.342,
      "salary_missing_days": null,
      "external_transfer_change_30d": 11.0844,
      "upi_share_of_spend": 0.4878,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 22.0863,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-03-01",
      "days_since_last_transaction": 0,
      "balance_change_30d": 10.217,
      "transaction_change_30d": 12.9215,
      "card_spend_change_30d": 11.658,
      "app_login_change_30d": -11.1278,
      "salary_missing_days": null,
      "external_transfer_change_30d": 9.9576,
      "upi_share_of_spend": 0.4647,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 4.1061,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-04-01",
      "days_since_last_transaction": 0,
      "balance_change_30d": 2.2951,
      "transaction_change_30d": 33.42,
      "card_spend_change_30d": 21.5935,
      "app_login_change_30d": 19.3204,
      "salary_missing_days": null,
      "external_transfer_change_30d": 5.2109,
      "upi_share_of_spend": 0.5492,
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
      "balance_change_30d": 20.1345,
      "transaction_change_30d": -3.558,
      "card_spend_change_30d": 12.6365,
      "app_login_change_30d": 5.26,
      "salary_missing_days": null,
      "external_transfer_change_30d": 9.9901,
      "upi_share_of_spend": 0.4639,
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
      "balance_change_30d": -22.7001,
      "transaction_change_30d": 11.1652,
      "card_spend_change_30d": -14.5497,
      "app_login_change_30d": 29.758,
      "salary_missing_days": null,
      "external_transfer_change_30d": 5.6268,
      "upi_share_of_spend": 0.5153,
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
    "tenure_months": 140,
    "customer_segment": "business",
    "income_regularity": "irregular",
    "products_count": 3,
    "has_credit_card": 0,
    "has_loan": 1,
    "days_since_last_transaction": 0,
    "balance_change_30d": -22.7001,
    "transaction_change_30d": 11.1652,
    "card_spend_change_30d": -14.5497,
    "app_login_change_30d": 29.758,
    "salary_missing_days": null,
    "external_transfer_change_30d": 5.6268,
    "upi_share_of_spend": 0.5153,
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
      "tenure_months": 140,
      "age": 51,
      "customer_yearly_value": 81698.0638,
      "products_count": 3,
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
    "served_at": "2026-08-31T01:58:44",
    "elapsed_ms": 6680.86,
    "timings_ms": {
      "model1": 275.03,
      "model2": 6405.54
    },
    "customer_id": "C18523",
    "customer_name": "Ekanta Oommen",
    "snapshot_date": "2026-06-01"
  },
  "model1": {
    "churn_probability": 2.42,
    "raw_churn_probability": 22.6,
    "probability_mode": "sigmoid",
    "risk_score": 7.25,
    "churn_prediction": "No",
    "risk_level": "Low",
    "top_risk_factors": [
      {
        "factor": "latest_balance_change_30d",
        "value": -22.7001,
        "message": "Balance has been falling across recent months.",
        "contribution": 0.04201897606253624
      },
      {
        "factor": "latest_vs_avg_upi_share_of_spend_available_history",
        "value": 0.01870000000000005,
        "message": "A larger share of spending is happening through UPI.",
        "contribution": 0.03880391642451286
      },
      {
        "factor": "sum_failed_transactions_30d_6m",
        "value": 7.0,
        "message": "Customer has recent failed transactions.",
        "contribution": 0.02403365820646286
      },
      {
        "factor": "latest_card_spend_change_30d",
        "value": -14.5497,
        "message": "Card spending has been falling across recent months.",
        "contribution": 0.020187433809041977
      },
      {
        "factor": "sum_failed_transactions_30d_3m",
        "value": 4.0,
        "message": "Customer has recent failed transactions.",
        "contribution": 0.018730387091636658
      }
    ]
  },
  "model2_input": {
    "customer_context": {
      "age": 51,
      "tenure_months": 140,
      "customer_segment": "business",
      "income_regularity": "irregular",
      "customer_yearly_value": 81698.0638,
      "products_count": 3,
      "has_credit_card": 0,
      "has_loan": 1
    },
    "behavior": {
      "days_since_last_transaction": 0,
      "balance_change_30d": -22.7001,
      "transaction_change_30d": 11.1652,
      "card_spend_change_30d": -14.5497,
      "app_login_change_30d": 29.758,
      "salary_missing_days": null,
      "external_transfer_change_30d": 5.6268,
      "upi_share_of_spend": 0.5153,
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
      "churn_probability": 0.0242,
      "churn_prediction": "No",
      "risk_level": "Low",
      "top_risk_factors": [
        {
          "factor": "balance_change_30d",
          "value": -22.7001
        },
        {
          "factor": "upi_share_of_spend",
          "value": 0.5153
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
    "case_id": "C18523"
  },
  "model2": {
    "case_id": "C18523",
    "ok": true,
    "prediction": {
      "evidence": [
        "balance_change_30d=-22.7",
        "transaction_change_30d=11.2"
      ],
      "primary_reason": "FINANCIAL_STRESS",
      "reasoning_summary": "The relationship looks stuck in a financial rut. Product review fits because balance_change_30d=-22.7 and complaints_30d=0 suggest a product-fit problem rather than a service issue.",
      "recommended_action": "PRODUCT_REVIEW",
      "secondary_reasons": [],
      "urgency": "MEDIUM"
    },
    "warnings": [],
    "raw_text": "{\"evidence\":[\"balance_change_30d=-22.7\",\"transaction_change_30d=11.2\"],\"primary_reason\":\"FINANCIAL_STRESS\",\"reasoning_summary\":\"The relationship looks stuck in a financial rut. Product review fits because balance_change_30d=-22.7 and complaints_30d=0 suggest a product-fit problem rather than a service issue.\",\"recommended_action\":\"PRODUCT_REVIEW\",\"secondary_reasons\":[],\"urgency\":\"MEDIUM\"}",
    "error": null,
    "latency_s": 6.4053,
    "simple_output": "Reason: FINANCIAL_STRESS | Urgency: MEDIUM | Action: PRODUCT_REVIEW | Why: The relationship looks stuck in a financial rut. Product review fits because balance_change_30d=-22.7 and complaints_30d=0 suggest a product-fit problem rather than a service issue."
  }
}
```

### Shivani Pathak (`C19078`)

- OK: `True`
- Shape errors: `[]`
- Simple output: Reason: UNKNOWN | Urgency: LOW | Action: MONITOR | Why: Complaint and resolution signals are mixed or weak; relationship strength is unknown.

Request:

```json
{
  "customer_id": "C19078",
  "customer_name": "Shivani Pathak",
  "prediction_date": "2026-06-01",
  "snapshot_date": "2026-06-01",
  "target_month": "2026-07-01",
  "profile": {
    "tenure_months": 204,
    "customer_segment": "farmer",
    "income_regularity": "seasonal",
    "products_count": 2,
    "has_credit_card": 0,
    "has_loan": 1
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 14,
      "balance_change_30d": -11.3729,
      "transaction_change_30d": 3.1705,
      "card_spend_change_30d": -18.3785,
      "app_login_change_30d": 13.9521,
      "salary_missing_days": null,
      "external_transfer_change_30d": 36.386,
      "upi_share_of_spend": 0.4742,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 44.4263,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-02-01",
      "days_since_last_transaction": 13,
      "balance_change_30d": -14.899,
      "transaction_change_30d": -16.0318,
      "card_spend_change_30d": -24.4283,
      "app_login_change_30d": -32.8529,
      "salary_missing_days": null,
      "external_transfer_change_30d": 73.966,
      "upi_share_of_spend": 0.4629,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 13.1203,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-03-01",
      "days_since_last_transaction": 9,
      "balance_change_30d": 5.2488,
      "transaction_change_30d": 10.9827,
      "card_spend_change_30d": 22.0547,
      "app_login_change_30d": -24.86,
      "salary_missing_days": null,
      "external_transfer_change_30d": 52.686,
      "upi_share_of_spend": 0.3744,
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
      "balance_change_30d": -10.5919,
      "transaction_change_30d": 7.2922,
      "card_spend_change_30d": -3.1041,
      "app_login_change_30d": -14.1024,
      "salary_missing_days": null,
      "external_transfer_change_30d": 27.4578,
      "upi_share_of_spend": 0.3915,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 2.0747,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-05-01",
      "days_since_last_transaction": 9,
      "balance_change_30d": -30.0739,
      "transaction_change_30d": -24.0911,
      "card_spend_change_30d": 3.4749,
      "app_login_change_30d": -2.7971,
      "salary_missing_days": null,
      "external_transfer_change_30d": 27.2015,
      "upi_share_of_spend": 0.3525,
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
      "balance_change_30d": -7.3271,
      "transaction_change_30d": -12.8322,
      "card_spend_change_30d": -23.555,
      "app_login_change_30d": -20.1043,
      "salary_missing_days": null,
      "external_transfer_change_30d": 65.1275,
      "upi_share_of_spend": 0.4381,
      "fd_maturing_in_30d": 1,
      "products_dropped_90d": 0,
      "complaints_30d": 0,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 0.0,
      "emi_bounce_30d": 0
    }
  ],
  "customer": {
    "tenure_months": 204,
    "customer_segment": "farmer",
    "income_regularity": "seasonal",
    "products_count": 2,
    "has_credit_card": 0,
    "has_loan": 1,
    "days_since_last_transaction": 11,
    "balance_change_30d": -7.3271,
    "transaction_change_30d": -12.8322,
    "card_spend_change_30d": -23.555,
    "app_login_change_30d": -20.1043,
    "salary_missing_days": null,
    "external_transfer_change_30d": 65.1275,
    "upi_share_of_spend": 0.4381,
    "fd_maturing_in_30d": 1,
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
      "tenure_months": 204,
      "age": 55,
      "customer_yearly_value": 18833.7634,
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
    "served_at": "2026-08-31T01:58:53",
    "elapsed_ms": 8502.02,
    "timings_ms": {
      "model1": 294.16,
      "model2": 8207.52
    },
    "customer_id": "C19078",
    "customer_name": "Shivani Pathak",
    "snapshot_date": "2026-06-01"
  },
  "model1": {
    "churn_probability": 4.38,
    "raw_churn_probability": 35.79,
    "probability_mode": "sigmoid",
    "risk_score": 13.14,
    "churn_prediction": "No",
    "risk_level": "Low",
    "top_risk_factors": [
      {
        "factor": "latest_external_transfer_change_30d",
        "value": 65.1275,
        "message": "External transfers have increased.",
        "contribution": 0.1091872826218605
      },
      {
        "factor": "latest_fd_maturing_in_30d",
        "value": 1,
        "message": "Customer has a fixed deposit maturing soon.",
        "contribution": 0.09605634957551956
      },
      {
        "factor": "count_balance_drop_3m",
        "value": 3,
        "message": "This signal increased churn risk.",
        "contribution": 0.06494054943323135
      },
      {
        "factor": "sum_fd_maturing_in_30d_3m",
        "value": 1.0,
        "message": "Customer has a fixed deposit maturing soon.",
        "contribution": 0.05388231202960014
      },
      {
        "factor": "count_balance_drop_6m",
        "value": 5,
        "message": "This signal increased churn risk.",
        "contribution": 0.04440728947520256
      }
    ]
  },
  "model2_input": {
    "customer_context": {
      "age": 55,
      "tenure_months": 204,
      "customer_segment": "farmer",
      "income_regularity": "seasonal",
      "customer_yearly_value": 18833.7634,
      "products_count": 2,
      "has_credit_card": 0,
      "has_loan": 1
    },
    "behavior": {
      "days_since_last_transaction": 11,
      "balance_change_30d": -7.3271,
      "transaction_change_30d": -12.8322,
      "card_spend_change_30d": -23.555,
      "app_login_change_30d": -20.1043,
      "salary_missing_days": null,
      "external_transfer_change_30d": 65.1275,
      "upi_share_of_spend": 0.4381,
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
      "churn_probability": 0.0438,
      "churn_prediction": "No",
      "risk_level": "Low",
      "top_risk_factors": [
        {
          "factor": "external_transfer_change_30d",
          "value": 65.1275
        },
        {
          "factor": "fd_maturing_in_30d",
          "value": 1
        },
        {
          "factor": "card_spend_change_30d",
          "value": -23.555
        }
      ]
    },
    "eligible_actions": [
      "PRODUCT_REVIEW",
      "RE_ENGAGEMENT",
      "MONITOR"
    ],
    "case_id": "C19078"
  },
  "model2": {
    "case_id": "C19078",
    "ok": true,
    "prediction": {
      "evidence": [
        "complaints_30d=0",
        "unresolved_complaints=0",
        "avg_resolution_time_hrs=0.0"
      ],
      "primary_reason": "UNKNOWN",
      "reasoning_summary": "Complaint and resolution signals are mixed or weak; relationship strength is unknown.",
      "recommended_action": "MONITOR",
      "secondary_reasons": [],
      "urgency": "LOW"
    },
    "warnings": [
      "evidence: 'complaints_30d=0' cites a zero/null value, which is not evidence; remove it",
      "evidence: 'unresolved_complaints=0' cites a zero/null value, which is not evidence; remove it",
      "evidence: 'avg_resolution_time_hrs=0.0' cites a zero/null value, which is not evidence; remove it"
    ],
    "raw_text": "{\"evidence\":[\"complaints_30d=0\",\"unresolved_complaints=0\",\"avg_resolution_time_hrs=0.0\"],\"primary_reason\":\"UNKNOWN\",\"reasoning_summary\":\"Complaint and resolution signals are mixed or weak; relationship with the product may be strained.\",\"recommended_action\":\"RE_ENGAGEMENT\",\"secondary_reasons\":[],\"urgency\":\"MEDIUM\"}",
    "error": null,
    "latency_s": 8.207,
    "simple_output": "Reason: UNKNOWN | Urgency: LOW | Action: MONITOR | Why: Complaint and resolution signals are mixed or weak; relationship strength is unknown."
  }
}
```

### Yochana Pau (`C19645`)

- OK: `True`
- Shape errors: `[]`
- Simple output: Reason: UNKNOWN | Urgency: LOW | Action: MONITOR | Why: Complaint and resolution signals are mixed or weak; reason is UNKNOWN.

Request:

```json
{
  "customer_id": "C19645",
  "customer_name": "Yochana Pau",
  "prediction_date": "2026-06-01",
  "snapshot_date": "2026-06-01",
  "target_month": "2026-07-01",
  "profile": {
    "tenure_months": 28,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 2,
    "has_credit_card": 0,
    "has_loan": 0
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 12,
      "balance_change_30d": -5.5146,
      "transaction_change_30d": -8.1679,
      "card_spend_change_30d": 0.1395,
      "app_login_change_30d": 10.2538,
      "salary_missing_days": 2.0,
      "external_transfer_change_30d": -19.2607,
      "upi_share_of_spend": 0.203,
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
      "balance_change_30d": 23.9795,
      "transaction_change_30d": 35.0444,
      "card_spend_change_30d": 26.3773,
      "app_login_change_30d": 21.6621,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": 5.1154,
      "upi_share_of_spend": 0.1378,
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
      "balance_change_30d": -7.072,
      "transaction_change_30d": -2.8874,
      "card_spend_change_30d": 14.3242,
      "app_login_change_30d": -6.466,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -29.2783,
      "upi_share_of_spend": 0.1636,
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
      "days_since_last_transaction": 12,
      "balance_change_30d": 9.7862,
      "transaction_change_30d": 1.658,
      "card_spend_change_30d": 21.255,
      "app_login_change_30d": 16.3177,
      "salary_missing_days": 2.0,
      "external_transfer_change_30d": 13.7927,
      "upi_share_of_spend": 0.2755,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 2,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 14.9468,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-05-01",
      "days_since_last_transaction": 12,
      "balance_change_30d": -11.1892,
      "transaction_change_30d": -3.9564,
      "card_spend_change_30d": 6.2366,
      "app_login_change_30d": -23.9039,
      "salary_missing_days": 3.0,
      "external_transfer_change_30d": 27.5365,
      "upi_share_of_spend": 0.3152,
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
      "days_since_last_transaction": 12,
      "balance_change_30d": 16.5955,
      "transaction_change_30d": 11.5847,
      "card_spend_change_30d": -12.176,
      "app_login_change_30d": 16.0887,
      "salary_missing_days": 1.0,
      "external_transfer_change_30d": 27.8798,
      "upi_share_of_spend": 0.2229,
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
    "tenure_months": 28,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 2,
    "has_credit_card": 0,
    "has_loan": 0,
    "days_since_last_transaction": 12,
    "balance_change_30d": 16.5955,
    "transaction_change_30d": 11.5847,
    "card_spend_change_30d": -12.176,
    "app_login_change_30d": 16.0887,
    "salary_missing_days": 1.0,
    "external_transfer_change_30d": 27.8798,
    "upi_share_of_spend": 0.2229,
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
      "tenure_months": 28,
      "age": 48,
      "customer_yearly_value": 24552.1718,
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
    "served_at": "2026-08-31T01:59:01",
    "elapsed_ms": 8761.91,
    "timings_ms": {
      "model1": 387.75,
      "model2": 8373.85
    },
    "customer_id": "C19645",
    "customer_name": "Yochana Pau",
    "snapshot_date": "2026-06-01"
  },
  "model1": {
    "churn_probability": 4.0,
    "raw_churn_probability": 33.76,
    "probability_mode": "sigmoid",
    "risk_score": 12.0,
    "churn_prediction": "No",
    "risk_level": "Low",
    "top_risk_factors": [
      {
        "factor": "external_transfer_change_30d_trend_6m",
        "value": 9.88676571428571,
        "message": "External transfers have increased.",
        "contribution": 0.039354875683784485
      },
      {
        "factor": "latest_card_spend_change_30d",
        "value": -12.176,
        "message": "Card spending has been falling across recent months.",
        "contribution": 0.0166452806442976
      },
      {
        "factor": "avg_upi_share_of_spend_6m",
        "value": 0.21966666666666668,
        "message": "A larger share of spending is happening through UPI.",
        "contribution": 0.012273191474378109
      },
      {
        "factor": "avg_external_transfer_change_30d_3m",
        "value": 23.069666666666667,
        "message": "External transfers have increased.",
        "contribution": 0.010480169206857681
      },
      {
        "factor": "sum_products_dropped_90d_6m",
        "value": 1.0,
        "message": "Customer has dropped products recently.",
        "contribution": 0.00979952048510313
      }
    ]
  },
  "model2_input": {
    "customer_context": {
      "age": 48,
      "tenure_months": 28,
      "customer_segment": "salary",
      "income_regularity": "regular",
      "customer_yearly_value": 24552.1718,
      "products_count": 2,
      "has_credit_card": 0,
      "has_loan": 0
    },
    "behavior": {
      "days_since_last_transaction": 12,
      "balance_change_30d": 16.5955,
      "transaction_change_30d": 11.5847,
      "card_spend_change_30d": -12.176,
      "app_login_change_30d": 16.0887,
      "salary_missing_days": 1,
      "external_transfer_change_30d": 27.8798,
      "upi_share_of_spend": 0.2229,
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
      "churn_probability": 0.04,
      "churn_prediction": "No",
      "risk_level": "Low",
      "top_risk_factors": [
        {
          "factor": "external_transfer_change_30d",
          "value": 27.8798
        },
        {
          "factor": "card_spend_change_30d",
          "value": -12.176
        },
        {
          "factor": "upi_share_of_spend",
          "value": 0.2229
        }
      ]
    },
    "eligible_actions": [
      "FINANCIAL_GUIDANCE",
      "PRODUCT_REVIEW",
      "MONITOR"
    ],
    "case_id": "C19645"
  },
  "model2": {
    "case_id": "C19645",
    "ok": true,
    "prediction": {
      "evidence": [
        "complaints_30d=0",
        "unresolved_complaints=0",
        "avg_resolution_time_hrs=0.0"
      ],
      "primary_reason": "UNKNOWN",
      "reasoning_summary": "Complaint and resolution signals are mixed or weak; reason is UNKNOWN.",
      "recommended_action": "MONITOR",
      "secondary_reasons": [],
      "urgency": "LOW"
    },
    "warnings": [
      "evidence: 'complaints_30d=0' cites a zero/null value, which is not evidence; remove it",
      "evidence: 'unresolved_complaints=0' cites a zero/null value, which is not evidence; remove it",
      "evidence: 'avg_resolution_time_hrs=0.0' cites a zero/null value, which is not evidence; remove it"
    ],
    "raw_text": "{\"evidence\":[\"complaints_30d=0\",\"unresolved_complaints=0\",\"avg_resolution_time_hrs=0.0\"],\"primary_reason\":\"UNKNOWN\",\"reasoning_summary\":\"Complaint and resolution signals are mixed or weak; evidence is genuinely mixed or weak.\",\"recommended_action\":\"MONITOR\",\"secondary_reasons\":[],\"urgency\":\"LOW\"}",
    "error": null,
    "latency_s": 8.3737,
    "simple_output": "Reason: UNKNOWN | Urgency: LOW | Action: MONITOR | Why: Complaint and resolution signals are mixed or weak; reason is UNKNOWN."
  }
}
```
