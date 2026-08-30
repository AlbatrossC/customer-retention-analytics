# Devang Model 1 -> Model 2 API Test Results

- API URL: `http://127.0.0.1:8001`
- Created at: `2026-08-31T01:08:14`
- Customers tested: `20`
- Source CSV: `model_1_v2\data\customers.csv`
- Health OK: `True`
- Ollama model: `devang-model2-q4`
- Model 1 loaded: `True`

## Summary

| # | Customer | Model 1 risk | Prediction | Reason | Urgency | Action | OK | Seconds |
|---:|---|---:|---|---|---|---|---|---:|
| 1 | Osha Raghavan (`C10134`) | 6.44 | No | NA | NA | NA | no | 11.58 |
| 2 | Hardik Nayak (`C10474`) | 3.09 | No | NA | NA | NA | no | 4.81 |
| 3 | Lila Goyal (`C11051`) | 4.47 | No | SERVICE_DISSATISFACTION | MEDIUM | SERVICE_RECOVERY | yes | 2.26 |
| 4 | Chanakya Chokshi (`C11159`) | 2.38 | No | SERVICE_DISSATISFACTION | MEDIUM | SERVICE_RECOVERY | yes | 1.98 |
| 5 | Deepa Nigam (`C11757`) | 2.22 | No | PRODUCT_MISMATCH | MEDIUM | PRODUCT_REVIEW | yes | 3.9 |
| 6 | Janya Shere (`C12174`) | 4.15 | No | NA | NA | NA | no | 11.93 |
| 7 | Daniel Nanda (`C12454`) | 2.56 | No | LOW_ENGAGEMENT | MEDIUM | RE_ENGAGEMENT | yes | 2.11 |
| 8 | Kamya Samra (`C13091`) | 11.27 | No | NA | NA | NA | no | 4.28 |
| 9 | Mohini Lad (`C13637`) | 3.72 | No | LOW_ENGAGEMENT | MEDIUM | RE_ENGAGEMENT | yes | 2.06 |
| 10 | Raagini Deol (`C14216`) | 5.37 | No | NA | NA | NA | no | 5.99 |
| 11 | Robert Patla (`C14339`) | 31.49 | Yes | SERVICE_DISSATISFACTION | HIGH | COMPLAINT_ESCALATION | yes | 2.81 |
| 12 | Waida Chanda (`C14830`) | 24.25 | Yes | SERVICE_DISSATISFACTION | MEDIUM | COMPLAINT_ESCALATION | yes | 2.65 |
| 13 | Isaiah Yohannan (`C16863`) | 2.5 | No | NA | NA | NA | no | 5.25 |
| 14 | Charvi Dara (`C17253`) | 3.84 | No | NA | NA | NA | no | 5.27 |
| 15 | Urvashi Agate (`C17317`) | 39.84 | Yes | SERVICE_DISSATISFACTION | HIGH | COMPLAINT_ESCALATION | yes | 2.73 |
| 16 | Rayaan Trivedi (`C17474`) | 6.16 | No | NA | NA | NA | no | 5.08 |
| 17 | Vritti Rai (`C17868`) | 2.33 | No | NA | NA | NA | no | 5.06 |
| 18 | Shaurya Naidu (`C18598`) | 1.87 | No | NA | NA | NA | no | 4.1 |
| 19 | Aayush Barad (`C18602`) | 1.68 | No | LOW_ENGAGEMENT | MEDIUM | RE_ENGAGEMENT | yes | 2.29 |
| 20 | Owen Kota (`C19841`) | 1.86 | No | LOW_ENGAGEMENT | MEDIUM | RE_ENGAGEMENT | yes | 2.02 |

## Details

### Osha Raghavan (`C10134`)

- OK: `False`
- Shape errors: `["model2 returned ok=false: recommended_action: 'COMPLAINT_ESCALATION' not in eligible_actions ['MONITOR', 'RE_ENGAGEMENT', 'PRODUCT_REVIEW', 'SERVICE_RECOVERY']", 'model2.prediction is missing or not an object']`
- Simple output: Prediction failed: recommended_action: 'COMPLAINT_ESCALATION' not in eligible_actions ['MONITOR', 'RE_ENGAGEMENT', 'PRODUCT_REVIEW', 'SERVICE_RECOVERY']

Request:

```json
{
  "customer_id": "C10134",
  "customer_name": "Osha Raghavan",
  "prediction_date": "2026-06-01",
  "snapshot_date": "2026-06-01",
  "target_month": "2026-07-01",
  "profile": {
    "tenure_months": 20,
    "customer_segment": "vendor",
    "income_regularity": "irregular",
    "products_count": 1,
    "has_credit_card": 0,
    "has_loan": 0
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 5,
      "balance_change_30d": 12.2182,
      "transaction_change_30d": -0.9069,
      "card_spend_change_30d": -16.7517,
      "app_login_change_30d": 7.653,
      "salary_missing_days": null,
      "external_transfer_change_30d": 28.4344,
      "upi_share_of_spend": 0.403,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 2,
      "unresolved_complaints": 1,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 52.5293,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-02-01",
      "days_since_last_transaction": 7,
      "balance_change_30d": 4.1511,
      "transaction_change_30d": -21.0479,
      "card_spend_change_30d": 6.6514,
      "app_login_change_30d": -13.499,
      "salary_missing_days": null,
      "external_transfer_change_30d": 99.4256,
      "upi_share_of_spend": 0.4587,
      "fd_maturing_in_30d": 1,
      "products_dropped_90d": 0,
      "complaints_30d": 0,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 0.0,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-03-01",
      "days_since_last_transaction": 8,
      "balance_change_30d": 4.3747,
      "transaction_change_30d": 8.3875,
      "card_spend_change_30d": 28.797,
      "app_login_change_30d": 6.7283,
      "salary_missing_days": null,
      "external_transfer_change_30d": -21.2003,
      "upi_share_of_spend": 0.4903,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 11.2782,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-04-01",
      "days_since_last_transaction": 9,
      "balance_change_30d": -11.6648,
      "transaction_change_30d": 3.2936,
      "card_spend_change_30d": 7.836,
      "app_login_change_30d": 3.9056,
      "salary_missing_days": null,
      "external_transfer_change_30d": 12.5,
      "upi_share_of_spend": 0.4394,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 4,
      "unresolved_complaints": 1,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 59.4833,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-05-01",
      "days_since_last_transaction": 9,
      "balance_change_30d": -9.5129,
      "transaction_change_30d": 20.1522,
      "card_spend_change_30d": 15.1627,
      "app_login_change_30d": 13.3616,
      "salary_missing_days": null,
      "external_transfer_change_30d": 12.5454,
      "upi_share_of_spend": 0.3323,
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
      "days_since_last_transaction": 6,
      "balance_change_30d": 18.166,
      "transaction_change_30d": 17.1338,
      "card_spend_change_30d": 10.7927,
      "app_login_change_30d": -20.3046,
      "salary_missing_days": null,
      "external_transfer_change_30d": 0.2447,
      "upi_share_of_spend": 0.4655,
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
    "tenure_months": 20,
    "customer_segment": "vendor",
    "income_regularity": "irregular",
    "products_count": 1,
    "has_credit_card": 0,
    "has_loan": 0,
    "days_since_last_transaction": 6,
    "balance_change_30d": 18.166,
    "transaction_change_30d": 17.1338,
    "card_spend_change_30d": 10.7927,
    "app_login_change_30d": -20.3046,
    "salary_missing_days": null,
    "external_transfer_change_30d": 0.2447,
    "upi_share_of_spend": 0.4655,
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
      "segment": "vendor",
      "income_regularity": "irregular",
      "tenure_months": 20,
      "age": 42,
      "customer_yearly_value": 19360.7545,
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
    "served_at": "2026-08-31T01:06:57",
    "elapsed_ms": 11564.18,
    "timings_ms": {
      "model1": 109.78,
      "model2": 11454.23
    },
    "customer_id": "C10134",
    "customer_name": "Osha Raghavan",
    "snapshot_date": "2026-06-01"
  },
  "model1": {
    "churn_probability": 6.44,
    "raw_churn_probability": 44.56,
    "probability_mode": "sigmoid",
    "risk_score": 19.33,
    "churn_prediction": "No",
    "risk_level": "Low",
    "top_risk_factors": [
      {
        "factor": "max_avg_resolution_time_hrs_3m",
        "value": 59.4833,
        "message": "Recent complaints took longer to resolve.",
        "contribution": 0.42371830344200134
      },
      {
        "factor": "latest_failed_transactions_30d",
        "value": 3,
        "message": "Customer has recent failed transactions.",
        "contribution": 0.142882838845253
      },
      {
        "factor": "latest_vs_avg_upi_share_of_spend_available_history",
        "value": 0.0339666666666667,
        "message": "A larger share of spending is happening through UPI.",
        "contribution": 0.1091550663113594
      },
      {
        "factor": "sum_fd_maturing_in_30d_3m",
        "value": 1.0,
        "message": "Customer has a fixed deposit maturing soon.",
        "contribution": 0.07893671840429306
      },
      {
        "factor": "sum_complaints_30d_6m",
        "value": 7.0,
        "message": "Customer has recent complaint activity.",
        "contribution": 0.07771056145429611
      }
    ]
  },
  "model2_input": {
    "customer_context": {
      "age": 42,
      "tenure_months": 20,
      "customer_segment": "vendor",
      "income_regularity": "irregular",
      "customer_yearly_value": 19360.7545,
      "products_count": 1,
      "has_credit_card": 0,
      "has_loan": 0
    },
    "behavior": {
      "days_since_last_transaction": 6,
      "balance_change_30d": 18.166,
      "transaction_change_30d": 17.1338,
      "card_spend_change_30d": 10.7927,
      "app_login_change_30d": -20.3046,
      "salary_missing_days": null,
      "external_transfer_change_30d": 0.2447,
      "upi_share_of_spend": 0.4655,
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
      "churn_probability": 0.0644,
      "churn_prediction": "No",
      "risk_level": "Low",
      "top_risk_factors": [
        {
          "factor": "max_avg_resolution_time_hrs_3m",
          "value": 59.4833
        },
        {
          "factor": "failed_transactions_30d",
          "value": 3
        },
        {
          "factor": "vs_avg_upi_share_of_spend_available_history",
          "value": 0.0339666666666667
        },
        {
          "factor": "sum_fd_maturing_in_30d_3m",
          "value": 1.0
        },
        {
          "factor": "sum_complaints_30d_6m",
          "value": 7.0
        }
      ]
    },
    "eligible_actions": [
      "MONITOR",
      "RE_ENGAGEMENT",
      "PRODUCT_REVIEW",
      "SERVICE_RECOVERY"
    ],
    "case_id": "C10134"
  },
  "model2": {
    "case_id": "C10134",
    "ok": false,
    "prediction": null,
    "raw_text": "{\"evidence\":[\"complaints_30d=0\",\"failed_transactions_30d=3\",\"avg_resolution_time_hrs=0.0\"],\"primary_reason\":\"SERVICE_DISSATISFACTION\",\"reasoning_summary\":\"Service friction is the clearest risk signal here. Complaint escalation fits because complaints_30d=0 and failed_transactions_30d=3 indicate the issue is unresolved or operationally serious.\",\"recommended_action\":\"COMPLAINT_ESCALATION\",\"secondary_reasons\":[\"UNKNOWN\"],\"urgency\":\"MEDIUM\"}",
    "error": "recommended_action: 'COMPLAINT_ESCALATION' not in eligible_actions ['MONITOR', 'RE_ENGAGEMENT', 'PRODUCT_REVIEW', 'SERVICE_RECOVERY']",
    "latency_s": 11.454,
    "simple_output": "Prediction failed: recommended_action: 'COMPLAINT_ESCALATION' not in eligible_actions ['MONITOR', 'RE_ENGAGEMENT', 'PRODUCT_REVIEW', 'SERVICE_RECOVERY']"
  }
}
```

### Hardik Nayak (`C10474`)

- OK: `False`
- Shape errors: `["model2 returned ok=false: recommended_action: 'FEE_WAIVER_REVIEW' not in eligible_actions ['MONITOR', 'RE_ENGAGEMENT', 'PRODUCT_REVIEW']", 'model2.prediction is missing or not an object']`
- Simple output: Prediction failed: recommended_action: 'FEE_WAIVER_REVIEW' not in eligible_actions ['MONITOR', 'RE_ENGAGEMENT', 'PRODUCT_REVIEW']

Request:

```json
{
  "customer_id": "C10474",
  "customer_name": "Hardik Nayak",
  "prediction_date": "2026-06-01",
  "snapshot_date": "2026-06-01",
  "target_month": "2026-07-01",
  "profile": {
    "tenure_months": 180,
    "customer_segment": "pension",
    "income_regularity": "regular",
    "products_count": 1,
    "has_credit_card": 0,
    "has_loan": 0
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 3,
      "balance_change_30d": 9.464,
      "transaction_change_30d": 22.5514,
      "card_spend_change_30d": -11.3377,
      "app_login_change_30d": 13.6237,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": 19.1367,
      "upi_share_of_spend": 0.3246,
      "fd_maturing_in_30d": 1,
      "products_dropped_90d": 1,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 13.6801,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-02-01",
      "days_since_last_transaction": 9,
      "balance_change_30d": -3.9346,
      "transaction_change_30d": 10.83,
      "card_spend_change_30d": -12.8295,
      "app_login_change_30d": -19.4591,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": 3.3428,
      "upi_share_of_spend": 0.3962,
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
      "balance_change_30d": 7.7192,
      "transaction_change_30d": -17.3798,
      "card_spend_change_30d": 8.6856,
      "app_login_change_30d": -1.2036,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -21.2962,
      "upi_share_of_spend": 0.2593,
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
      "days_since_last_transaction": 6,
      "balance_change_30d": 9.4405,
      "transaction_change_30d": -26.12,
      "card_spend_change_30d": 11.1577,
      "app_login_change_30d": -4.9087,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": 21.2246,
      "upi_share_of_spend": 0.3005,
      "fd_maturing_in_30d": 1,
      "products_dropped_90d": 0,
      "complaints_30d": 4,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 2.0556,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-05-01",
      "days_since_last_transaction": 9,
      "balance_change_30d": -6.9206,
      "transaction_change_30d": -6.9481,
      "card_spend_change_30d": 6.1796,
      "app_login_change_30d": 1.939,
      "salary_missing_days": 2.0,
      "external_transfer_change_30d": 7.3362,
      "upi_share_of_spend": 0.4087,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 1,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 2,
      "avg_resolution_time_hrs": 29.3664,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-06-01",
      "days_since_last_transaction": 10,
      "balance_change_30d": 17.4283,
      "transaction_change_30d": 8.5751,
      "card_spend_change_30d": -42.675,
      "app_login_change_30d": -2.9247,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": 34.0052,
      "upi_share_of_spend": 0.2983,
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
    "customer_segment": "pension",
    "income_regularity": "regular",
    "products_count": 1,
    "has_credit_card": 0,
    "has_loan": 0,
    "days_since_last_transaction": 10,
    "balance_change_30d": 17.4283,
    "transaction_change_30d": 8.5751,
    "card_spend_change_30d": -42.675,
    "app_login_change_30d": -2.9247,
    "salary_missing_days": 0.0,
    "external_transfer_change_30d": 34.0052,
    "upi_share_of_spend": 0.2983,
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
      "tenure_months": 180,
      "age": 73,
      "customer_yearly_value": 24637.2492,
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
    "served_at": "2026-08-31T01:07:02",
    "elapsed_ms": 4795.02,
    "timings_ms": {
      "model1": 187.84,
      "model2": 4607.04
    },
    "customer_id": "C10474",
    "customer_name": "Hardik Nayak",
    "snapshot_date": "2026-06-01"
  },
  "model1": {
    "churn_probability": 3.09,
    "raw_churn_probability": 28.04,
    "probability_mode": "sigmoid",
    "risk_score": 9.28,
    "churn_prediction": "No",
    "risk_level": "Low",
    "top_risk_factors": [
      {
        "factor": "latest_card_spend_change_30d",
        "value": -42.675,
        "message": "Card spending has been falling across recent months.",
        "contribution": 0.1808045506477356
      },
      {
        "factor": "sum_complaints_30d_6m",
        "value": 6.0,
        "message": "Customer has recent complaint activity.",
        "contribution": 0.07052449136972427
      },
      {
        "factor": "days_since_last_transaction_trend_6m",
        "value": 0.9999999999999998,
        "message": "Customer has gone longer without transacting.",
        "contribution": 0.05832737684249878
      },
      {
        "factor": "sum_fd_maturing_in_30d_3m",
        "value": 1.0,
        "message": "Customer has a fixed deposit maturing soon.",
        "contribution": 0.05196322500705719
      },
      {
        "factor": "sum_complaints_30d_3m",
        "value": 5.0,
        "message": "Customer has recent complaint activity.",
        "contribution": 0.03129623457789421
      }
    ]
  },
  "model2_input": {
    "customer_context": {
      "age": 73,
      "tenure_months": 180,
      "customer_segment": "pension",
      "income_regularity": "regular",
      "customer_yearly_value": 24637.2492,
      "products_count": 1,
      "has_credit_card": 0,
      "has_loan": 0
    },
    "behavior": {
      "days_since_last_transaction": 10,
      "balance_change_30d": 17.4283,
      "transaction_change_30d": 8.5751,
      "card_spend_change_30d": -42.675,
      "app_login_change_30d": -2.9247,
      "salary_missing_days": 0,
      "external_transfer_change_30d": 34.0052,
      "upi_share_of_spend": 0.2983,
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
          "value": -42.675
        },
        {
          "factor": "sum_complaints_30d_6m",
          "value": 6.0
        },
        {
          "factor": "days_since_last_transaction_trend_6m",
          "value": 0.9999999999999998
        },
        {
          "factor": "sum_fd_maturing_in_30d_3m",
          "value": 1.0
        },
        {
          "factor": "sum_complaints_30d_3m",
          "value": 5.0
        }
      ]
    },
    "eligible_actions": [
      "MONITOR",
      "RE_ENGAGEMENT",
      "PRODUCT_REVIEW"
    ],
    "case_id": "C10474"
  },
  "model2": {
    "case_id": "C10474",
    "ok": false,
    "prediction": null,
    "raw_text": "{\"evidence\":[\"transaction_change_30d=8.6\",\"card_spend_change_30d=-42.7\",\"complaints_30d=0\",\"failed_transactions_30d=0\",\"avg_resolution_time_hrs=0.0\"],\"primary_reason\":\"FEE_DISSATISFACTION\",\"reasoning_summary\":\"The relationship looks stressed around fees or charges, though the evidence is mixed or limited. Evidence suggests this because complaint_text=None; complaints_30d=0; card_spend_change_30d=-42.7.\",\"recommended_action\":\"FEE_WAIVER_REVIEW\",\"secondary_reasons\":[\"UNKNOWN\"],\"urgency\":\"MEDIUM\"}",
    "error": "recommended_action: 'FEE_WAIVER_REVIEW' not in eligible_actions ['MONITOR', 'RE_ENGAGEMENT', 'PRODUCT_REVIEW']",
    "latency_s": 4.6069,
    "simple_output": "Prediction failed: recommended_action: 'FEE_WAIVER_REVIEW' not in eligible_actions ['MONITOR', 'RE_ENGAGEMENT', 'PRODUCT_REVIEW']"
  }
}
```

### Lila Goyal (`C11051`)

- OK: `True`
- Shape errors: `[]`
- Simple output: Reason: SERVICE_DISSATISFACTION | Urgency: MEDIUM | Action: SERVICE_RECOVERY | Why: Service friction is the clearest risk signal here based on complaints_30d=1, unresolved_complaints=1, and failed_transactions_30d=1.

Request:

```json
{
  "customer_id": "C11051",
  "customer_name": "Lila Goyal",
  "prediction_date": "2026-06-01",
  "snapshot_date": "2026-06-01",
  "target_month": "2026-07-01",
  "profile": {
    "tenure_months": 8,
    "customer_segment": "business",
    "income_regularity": "irregular",
    "products_count": 3,
    "has_credit_card": 1,
    "has_loan": 0
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 0,
      "balance_change_30d": 30.1101,
      "transaction_change_30d": 10.4249,
      "card_spend_change_30d": 17.1978,
      "app_login_change_30d": 22.7182,
      "salary_missing_days": null,
      "external_transfer_change_30d": -26.9904,
      "upi_share_of_spend": 0.4584,
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
      "days_since_last_transaction": 1,
      "balance_change_30d": 24.0403,
      "transaction_change_30d": 0.9854,
      "card_spend_change_30d": 36.2803,
      "app_login_change_30d": -0.2266,
      "salary_missing_days": null,
      "external_transfer_change_30d": 1.2938,
      "upi_share_of_spend": 0.4317,
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
      "days_since_last_transaction": 0,
      "balance_change_30d": 13.4156,
      "transaction_change_30d": 22.6479,
      "card_spend_change_30d": 38.689,
      "app_login_change_30d": 33.8441,
      "salary_missing_days": null,
      "external_transfer_change_30d": 3.3292,
      "upi_share_of_spend": 0.4062,
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
      "balance_change_30d": 24.6928,
      "transaction_change_30d": 10.9474,
      "card_spend_change_30d": -11.4772,
      "app_login_change_30d": -19.7565,
      "salary_missing_days": null,
      "external_transfer_change_30d": 12.4635,
      "upi_share_of_spend": 0.4742,
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
      "balance_change_30d": -10.0322,
      "transaction_change_30d": -16.9484,
      "card_spend_change_30d": -14.4563,
      "app_login_change_30d": 6.0746,
      "salary_missing_days": null,
      "external_transfer_change_30d": 36.5955,
      "upi_share_of_spend": 0.4959,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 26.4759,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-06-01",
      "days_since_last_transaction": 2,
      "balance_change_30d": -13.9604,
      "transaction_change_30d": 1.5175,
      "card_spend_change_30d": -4.473,
      "app_login_change_30d": 7.3498,
      "salary_missing_days": null,
      "external_transfer_change_30d": -0.4861,
      "upi_share_of_spend": 0.5768,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 1,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 21.1686,
      "emi_bounce_30d": 0
    }
  ],
  "customer": {
    "tenure_months": 8,
    "customer_segment": "business",
    "income_regularity": "irregular",
    "products_count": 3,
    "has_credit_card": 1,
    "has_loan": 0,
    "days_since_last_transaction": 2,
    "balance_change_30d": -13.9604,
    "transaction_change_30d": 1.5175,
    "card_spend_change_30d": -4.473,
    "app_login_change_30d": 7.3498,
    "salary_missing_days": null,
    "external_transfer_change_30d": -0.4861,
    "upi_share_of_spend": 0.5768,
    "fd_maturing_in_30d": 0,
    "products_dropped_90d": 0,
    "complaints_30d": 1,
    "unresolved_complaints": 1,
    "failed_transactions_30d": 1,
    "avg_resolution_time_hrs": 21.1686,
    "emi_bounce_30d": 0
  },
  "extra_context": {
    "customer_profile": {
      "segment": "business",
      "income_regularity": "irregular",
      "tenure_months": 8,
      "age": 30,
      "customer_yearly_value": 40339.792,
      "products_count": 3,
      "has_credit_card": 1,
      "has_loan": 0,
      "value_tier": "medium"
    },
    "recent_complaint_text": "Kindly increase my daily ATM withdrawal limit for business needs."
  }
}
```

Response:

```json
{
  "meta": {
    "endpoint": "/predict/both",
    "served_at": "2026-08-31T01:07:04",
    "elapsed_ms": 2261.26,
    "timings_ms": {
      "model1": 82.5,
      "model2": 2178.64
    },
    "customer_id": "C11051",
    "customer_name": "Lila Goyal",
    "snapshot_date": "2026-06-01"
  },
  "model1": {
    "churn_probability": 4.47,
    "raw_churn_probability": 36.27,
    "probability_mode": "sigmoid",
    "risk_score": 13.42,
    "churn_prediction": "No",
    "risk_level": "Low",
    "top_risk_factors": [
      {
        "factor": "latest_vs_avg_upi_share_of_spend_available_history",
        "value": 0.10293333333333332,
        "message": "A larger share of spending is happening through UPI.",
        "contribution": 0.1926679164171219
      },
      {
        "factor": "latest_upi_share_of_spend",
        "value": 0.5768,
        "message": "A larger share of spending is happening through UPI.",
        "contribution": 0.038256462663412094
      },
      {
        "factor": "external_transfer_change_30d_trend_6m",
        "value": 7.07316857142857,
        "message": "External transfers have increased.",
        "contribution": 0.037742648273706436
      },
      {
        "factor": "balance_change_30d_trend_6m",
        "value": -8.894079999999995,
        "message": "Balance has been falling across recent months.",
        "contribution": 0.027284866198897362
      },
      {
        "factor": "transaction_change_30d_trend_6m",
        "value": -3.1439685714285717,
        "message": "Transaction activity has been falling across recent months.",
        "contribution": 0.022104283794760704
      }
    ]
  },
  "model2_input": {
    "customer_context": {
      "age": 30,
      "tenure_months": 8,
      "customer_segment": "business",
      "income_regularity": "irregular",
      "customer_yearly_value": 40339.792,
      "products_count": 3,
      "has_credit_card": 1,
      "has_loan": 0
    },
    "behavior": {
      "days_since_last_transaction": 2,
      "balance_change_30d": -13.9604,
      "transaction_change_30d": 1.5175,
      "card_spend_change_30d": -4.473,
      "app_login_change_30d": 7.3498,
      "salary_missing_days": null,
      "external_transfer_change_30d": -0.4861,
      "upi_share_of_spend": 0.5768,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "emi_bounce_30d": 0
    },
    "service_evidence": {
      "complaints_30d": 1,
      "unresolved_complaints": 1,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 21.1686,
      "complaint_text": "Kindly increase my daily ATM withdrawal limit for business needs."
    },
    "model1": {
      "churn_probability": 0.0447,
      "churn_prediction": "No",
      "risk_level": "Low",
      "top_risk_factors": [
        {
          "factor": "vs_avg_upi_share_of_spend_available_history",
          "value": 0.10293333333333332
        },
        {
          "factor": "upi_share_of_spend",
          "value": 0.5768
        },
        {
          "factor": "external_transfer_change_30d_trend_6m",
          "value": 7.07316857142857
        },
        {
          "factor": "balance_change_30d_trend_6m",
          "value": -8.894079999999995
        },
        {
          "factor": "transaction_change_30d_trend_6m",
          "value": -3.1439685714285717
        }
      ]
    },
    "eligible_actions": [
      "MONITOR",
      "RE_ENGAGEMENT",
      "PRODUCT_REVIEW",
      "SERVICE_RECOVERY",
      "COMPLAINT_ESCALATION"
    ],
    "case_id": "C11051"
  },
  "model2": {
    "case_id": "C11051",
    "ok": true,
    "prediction": {
      "evidence": [
        "complaints_30d=1",
        "unresolved_complaints=1",
        "failed_transactions_30d=1",
        "avg_resolution_time_hrs=21.2",
        "complaint_text describes a recent service issue"
      ],
      "primary_reason": "SERVICE_DISSATISFACTION",
      "reasoning_summary": "Service friction is the clearest risk signal here based on complaints_30d=1, unresolved_complaints=1, and failed_transactions_30d=1.",
      "recommended_action": "SERVICE_RECOVERY",
      "secondary_reasons": [
        "UNKNOWN"
      ],
      "urgency": "MEDIUM"
    },
    "raw_text": "{\n\"evidence\":[\"complaints_30d=1\",\"unresolved_complaints=1\",\"failed_transactions_30d=1\",\"avg_resolution_time_hrs=21.2\",\"complaint_text describes a recent service issue\"],\"primary_reason\":\"SERVICE_DISSATISFACTION\",\"reasoning_summary\":\"Service friction is the clearest risk signal here based on complaints_30d=1, unresolved_complaints=1, and failed_transactions_30d=1.\",\"recommended_action\":\"SERVICE_RECOVERY\",\"secondary_reasons\":[\"UNKNOWN\"],\"urgency\":\"MEDIUM\"\n}",
    "error": null,
    "latency_s": 2.1785,
    "simple_output": "Reason: SERVICE_DISSATISFACTION | Urgency: MEDIUM | Action: SERVICE_RECOVERY | Why: Service friction is the clearest risk signal here based on complaints_30d=1, unresolved_complaints=1, and failed_transactions_30d=1."
  }
}
```

### Chanakya Chokshi (`C11159`)

- OK: `True`
- Shape errors: `[]`
- Simple output: Reason: SERVICE_DISSATISFACTION | Urgency: MEDIUM | Action: SERVICE_RECOVERY | Why: Service friction is the clearest risk signal here, though the relationship looks otherwise healthy.

Request:

```json
{
  "customer_id": "C11159",
  "customer_name": "Chanakya Chokshi",
  "prediction_date": "2026-06-01",
  "snapshot_date": "2026-06-01",
  "target_month": "2026-07-01",
  "profile": {
    "tenure_months": 67,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 1,
    "has_credit_card": 0,
    "has_loan": 0
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 14,
      "balance_change_30d": -3.0208,
      "transaction_change_30d": -9.2326,
      "card_spend_change_30d": -20.1122,
      "app_login_change_30d": -0.5734,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": 38.5468,
      "upi_share_of_spend": 0.5642,
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
      "days_since_last_transaction": 9,
      "balance_change_30d": 5.8889,
      "transaction_change_30d": -4.4577,
      "card_spend_change_30d": -20.2082,
      "app_login_change_30d": 7.3576,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": 35.127,
      "upi_share_of_spend": 0.546,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 1,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 41.742,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-03-01",
      "days_since_last_transaction": 15,
      "balance_change_30d": 5.5929,
      "transaction_change_30d": 19.7901,
      "card_spend_change_30d": -9.5452,
      "app_login_change_30d": -6.8025,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": 57.2649,
      "upi_share_of_spend": 0.5289,
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
      "balance_change_30d": -7.5661,
      "transaction_change_30d": 8.1337,
      "card_spend_change_30d": -4.1425,
      "app_login_change_30d": -12.3257,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -7.486,
      "upi_share_of_spend": 0.5171,
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
      "balance_change_30d": -9.5988,
      "transaction_change_30d": 8.5596,
      "card_spend_change_30d": -20.8595,
      "app_login_change_30d": 25.2291,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -31.2328,
      "upi_share_of_spend": 0.4733,
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
      "days_since_last_transaction": 9,
      "balance_change_30d": 10.8702,
      "transaction_change_30d": 14.2733,
      "card_spend_change_30d": -0.3477,
      "app_login_change_30d": 3.7617,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -32.0054,
      "upi_share_of_spend": 0.3746,
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
    "tenure_months": 67,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 1,
    "has_credit_card": 0,
    "has_loan": 0,
    "days_since_last_transaction": 9,
    "balance_change_30d": 10.8702,
    "transaction_change_30d": 14.2733,
    "card_spend_change_30d": -0.3477,
    "app_login_change_30d": 3.7617,
    "salary_missing_days": 0.0,
    "external_transfer_change_30d": -32.0054,
    "upi_share_of_spend": 0.3746,
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
      "tenure_months": 67,
      "age": 34,
      "customer_yearly_value": 36593.8617,
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
    "served_at": "2026-08-31T01:07:06",
    "elapsed_ms": 1976.28,
    "timings_ms": {
      "model1": 51.89,
      "model2": 1924.26
    },
    "customer_id": "C11159",
    "customer_name": "Chanakya Chokshi",
    "snapshot_date": "2026-06-01"
  },
  "model1": {
    "churn_probability": 2.38,
    "raw_churn_probability": 22.23,
    "probability_mode": "sigmoid",
    "risk_score": 7.13,
    "churn_prediction": "No",
    "risk_level": "Low",
    "top_risk_factors": [
      {
        "factor": "sum_failed_transactions_30d_3m",
        "value": 6.0,
        "message": "Customer has recent failed transactions.",
        "contribution": 0.09200986474752426
      },
      {
        "factor": "sum_failed_transactions_30d_6m",
        "value": 8.0,
        "message": "Customer has recent failed transactions.",
        "contribution": 0.06269454210996628
      },
      {
        "factor": "latest_vs_avg_external_transfer_change_30d_available_history",
        "value": -42.04115,
        "message": "This signal increased churn risk.",
        "contribution": 0.039854828268289566
      },
      {
        "factor": "max_salary_missing_days_6m",
        "value": 0.0,
        "message": "This signal increased churn risk.",
        "contribution": 0.02795764058828354
      },
      {
        "factor": "max_days_since_last_transaction_3m",
        "value": 11.0,
        "message": "Customer has gone longer without transacting.",
        "contribution": 0.026527322828769684
      }
    ]
  },
  "model2_input": {
    "customer_context": {
      "age": 34,
      "tenure_months": 67,
      "customer_segment": "salary",
      "income_regularity": "regular",
      "customer_yearly_value": 36593.8617,
      "products_count": 1,
      "has_credit_card": 0,
      "has_loan": 0
    },
    "behavior": {
      "days_since_last_transaction": 9,
      "balance_change_30d": 10.8702,
      "transaction_change_30d": 14.2733,
      "card_spend_change_30d": -0.3477,
      "app_login_change_30d": 3.7617,
      "salary_missing_days": 0,
      "external_transfer_change_30d": -32.0054,
      "upi_share_of_spend": 0.3746,
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
      "churn_probability": 0.0238,
      "churn_prediction": "No",
      "risk_level": "Low",
      "top_risk_factors": [
        {
          "factor": "sum_failed_transactions_30d_3m",
          "value": 6.0
        },
        {
          "factor": "sum_failed_transactions_30d_6m",
          "value": 8.0
        },
        {
          "factor": "vs_avg_external_transfer_change_30d_available_history",
          "value": -42.04115
        },
        {
          "factor": "max_salary_missing_days_6m",
          "value": 0.0
        },
        {
          "factor": "max_days_since_last_transaction_3m",
          "value": 11.0
        }
      ]
    },
    "eligible_actions": [
      "MONITOR",
      "RE_ENGAGEMENT",
      "PRODUCT_REVIEW",
      "SERVICE_RECOVERY"
    ],
    "case_id": "C11159"
  },
  "model2": {
    "case_id": "C11159",
    "ok": true,
    "prediction": {
      "evidence": [
        "transaction_change_30d=14.3",
        "balance_change_30d=10.9",
        "complaints_30d=0",
        "avg_resolution_time_hrs=0.0"
      ],
      "primary_reason": "SERVICE_DISSATISFACTION",
      "reasoning_summary": "Service friction is the clearest risk signal here, though the relationship looks otherwise healthy.",
      "recommended_action": "SERVICE_RECOVERY",
      "secondary_reasons": [
        "UNKNOWN"
      ],
      "urgency": "MEDIUM"
    },
    "raw_text": "{\n\"evidence\":[\"transaction_change_30d=14.3\",\"balance_change_30d=10.9\",\"complaints_30d=0\",\"avg_resolution_time_hrs=0.0\"],\"primary_reason\":\"SERVICE_DISSATISFACTION\",\"reasoning_summary\":\"Service friction is the clearest risk signal here, though the relationship looks otherwise healthy.\",\"recommended_action\":\"SERVICE_RECOVERY\",\"secondary_reasons\":[\"UNKNOWN\"],\"urgency\":\"MEDIUM\"}",
    "error": null,
    "latency_s": 1.9241,
    "simple_output": "Reason: SERVICE_DISSATISFACTION | Urgency: MEDIUM | Action: SERVICE_RECOVERY | Why: Service friction is the clearest risk signal here, though the relationship looks otherwise healthy."
  }
}
```

### Deepa Nigam (`C11757`)

- OK: `True`
- Shape errors: `[]`
- Simple output: Reason: PRODUCT_MISMATCH | Urgency: MEDIUM | Action: PRODUCT_REVIEW | Why: Complaint text suggests a product-fit issue. Product review fits because complaint_text points to a product-fit issue and secondary_reasons match.

Request:

```json
{
  "customer_id": "C11757",
  "customer_name": "Deepa Nigam",
  "prediction_date": "2026-06-01",
  "snapshot_date": "2026-06-01",
  "target_month": "2026-07-01",
  "profile": {
    "tenure_months": 107,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 2,
    "has_credit_card": 1,
    "has_loan": 0
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 4,
      "balance_change_30d": 13.8317,
      "transaction_change_30d": 16.164,
      "card_spend_change_30d": 6.3782,
      "app_login_change_30d": -2.0798,
      "salary_missing_days": 2.0,
      "external_transfer_change_30d": -8.775,
      "upi_share_of_spend": 0.6093,
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
      "balance_change_30d": 0.1363,
      "transaction_change_30d": 0.7071,
      "card_spend_change_30d": 33.2157,
      "app_login_change_30d": 31.668,
      "salary_missing_days": 1.0,
      "external_transfer_change_30d": 1.8114,
      "upi_share_of_spend": 0.514,
      "fd_maturing_in_30d": 1,
      "products_dropped_90d": 0,
      "complaints_30d": 0,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 0.0,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-03-01",
      "days_since_last_transaction": 1,
      "balance_change_30d": 25.4298,
      "transaction_change_30d": 22.6619,
      "card_spend_change_30d": 26.9713,
      "app_login_change_30d": 11.221,
      "salary_missing_days": 1.0,
      "external_transfer_change_30d": 13.9154,
      "upi_share_of_spend": 0.581,
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
      "balance_change_30d": 23.9457,
      "transaction_change_30d": 34.491,
      "card_spend_change_30d": 15.5785,
      "app_login_change_30d": 23.4526,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": 0.1124,
      "upi_share_of_spend": 0.5528,
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
      "balance_change_30d": 16.9337,
      "transaction_change_30d": 9.8118,
      "card_spend_change_30d": 36.733,
      "app_login_change_30d": 14.9534,
      "salary_missing_days": 1.0,
      "external_transfer_change_30d": 9.0315,
      "upi_share_of_spend": 0.5578,
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
      "balance_change_30d": 28.5384,
      "transaction_change_30d": 16.936,
      "card_spend_change_30d": 37.6865,
      "app_login_change_30d": -11.943,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -48.5365,
      "upi_share_of_spend": 0.5621,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 8.7717,
      "emi_bounce_30d": 0
    }
  ],
  "customer": {
    "tenure_months": 107,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 2,
    "has_credit_card": 1,
    "has_loan": 0,
    "days_since_last_transaction": 0,
    "balance_change_30d": 28.5384,
    "transaction_change_30d": 16.936,
    "card_spend_change_30d": 37.6865,
    "app_login_change_30d": -11.943,
    "salary_missing_days": 0.0,
    "external_transfer_change_30d": -48.5365,
    "upi_share_of_spend": 0.5621,
    "fd_maturing_in_30d": 0,
    "products_dropped_90d": 0,
    "complaints_30d": 1,
    "unresolved_complaints": 0,
    "failed_transactions_30d": 1,
    "avg_resolution_time_hrs": 8.7717,
    "emi_bounce_30d": 0
  },
  "extra_context": {
    "customer_profile": {
      "segment": "salary",
      "income_regularity": "regular",
      "tenure_months": 107,
      "age": 55,
      "customer_yearly_value": 24914.515,
      "products_count": 2,
      "has_credit_card": 1,
      "has_loan": 0,
      "value_tier": "low"
    },
    "recent_complaint_text": "Debit card EMI option promised at branch but not showing anywhere."
  }
}
```

Response:

```json
{
  "meta": {
    "endpoint": "/predict/both",
    "served_at": "2026-08-31T01:07:10",
    "elapsed_ms": 3877.01,
    "timings_ms": {
      "model1": 70.84,
      "model2": 3806.05
    },
    "customer_id": "C11757",
    "customer_name": "Deepa Nigam",
    "snapshot_date": "2026-06-01"
  },
  "model1": {
    "churn_probability": 2.22,
    "raw_churn_probability": 20.75,
    "probability_mode": "sigmoid",
    "risk_score": 6.67,
    "churn_prediction": "No",
    "risk_level": "Low",
    "top_risk_factors": [
      {
        "factor": "latest_vs_avg_external_transfer_change_30d_available_history",
        "value": -43.1297,
        "message": "This signal increased churn risk.",
        "contribution": 0.052301693707704544
      },
      {
        "factor": "latest_upi_share_of_spend",
        "value": 0.5621,
        "message": "A larger share of spending is happening through UPI.",
        "contribution": 0.04514400288462639
      },
      {
        "factor": "avg_transaction_change_30d_6m",
        "value": 16.7953,
        "message": "This signal increased churn risk.",
        "contribution": 0.01968487724661827
      },
      {
        "factor": "card_spend_change_30d_trend_6m",
        "value": 4.44858857142857,
        "message": "This signal increased churn risk.",
        "contribution": 0.01916625164449215
      },
      {
        "factor": "count_external_transfer_rise_6m",
        "value": 0,
        "message": "This signal increased churn risk.",
        "contribution": 0.01610436663031578
      }
    ]
  },
  "model2_input": {
    "customer_context": {
      "age": 55,
      "tenure_months": 107,
      "customer_segment": "salary",
      "income_regularity": "regular",
      "customer_yearly_value": 24914.515,
      "products_count": 2,
      "has_credit_card": 1,
      "has_loan": 0
    },
    "behavior": {
      "days_since_last_transaction": 0,
      "balance_change_30d": 28.5384,
      "transaction_change_30d": 16.936,
      "card_spend_change_30d": 37.6865,
      "app_login_change_30d": -11.943,
      "salary_missing_days": 0,
      "external_transfer_change_30d": -48.5365,
      "upi_share_of_spend": 0.5621,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "emi_bounce_30d": 0
    },
    "service_evidence": {
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 8.7717,
      "complaint_text": "Debit card EMI option promised at branch but not showing anywhere."
    },
    "model1": {
      "churn_probability": 0.0222,
      "churn_prediction": "No",
      "risk_level": "Low",
      "top_risk_factors": [
        {
          "factor": "vs_avg_external_transfer_change_30d_available_history",
          "value": -43.1297
        },
        {
          "factor": "upi_share_of_spend",
          "value": 0.5621
        },
        {
          "factor": "avg_transaction_change_30d_6m",
          "value": 16.7953
        },
        {
          "factor": "card_spend_change_30d_trend_6m",
          "value": 4.44858857142857
        },
        {
          "factor": "count_external_transfer_rise_6m",
          "value": 0
        }
      ]
    },
    "eligible_actions": [
      "MONITOR",
      "RE_ENGAGEMENT",
      "PRODUCT_REVIEW",
      "SERVICE_RECOVERY"
    ],
    "case_id": "C11757"
  },
  "model2": {
    "case_id": "C11757",
    "ok": true,
    "prediction": {
      "evidence": [
        "complaint_text points to a product-fit issue",
        "secondary_reasons match"
      ],
      "primary_reason": "PRODUCT_MISMATCH",
      "reasoning_summary": "Complaint text suggests a product-fit issue. Product review fits because complaint_text points to a product-fit issue and secondary_reasons match.",
      "recommended_action": "PRODUCT_REVIEW",
      "secondary_reasons": [
        "SERVICE_DISSATISFACTION"
      ],
      "urgency": "MEDIUM"
    },
    "raw_text": "{\"evidence\":[\"complaint_text points to a product-fit issue\",\"secondary_reasons match\"],\"primary_reason\":\"PRODUCT_MISMATCH\",\"reasoning_summary\":\"Complaint text suggests a product-fit issue. Product review fits because complaint_text points to a product-fit issue and secondary_reasons match.\",\"recommended_action\":\"PRODUCT_REVIEW\",\"secondary_reasons\":[\"SERVICE_DISSATISFACTION\"],\"urgency\":\"MEDIUM\"}",
    "error": null,
    "latency_s": 3.8059,
    "simple_output": "Reason: PRODUCT_MISMATCH | Urgency: MEDIUM | Action: PRODUCT_REVIEW | Why: Complaint text suggests a product-fit issue. Product review fits because complaint_text points to a product-fit issue and secondary_reasons match."
  }
}
```

### Janya Shere (`C12174`)

- OK: `False`
- Shape errors: `["model2 returned ok=false: recommended_action: 'COMPLAINT_ESCALATION' not in eligible_actions ['MONITOR', 'RE_ENGAGEMENT', 'PRODUCT_REVIEW', 'SERVICE_RECOVERY']", 'model2.prediction is missing or not an object']`
- Simple output: Prediction failed: recommended_action: 'COMPLAINT_ESCALATION' not in eligible_actions ['MONITOR', 'RE_ENGAGEMENT', 'PRODUCT_REVIEW', 'SERVICE_RECOVERY']

Request:

```json
{
  "customer_id": "C12174",
  "customer_name": "Janya Shere",
  "prediction_date": "2026-06-01",
  "snapshot_date": "2026-06-01",
  "target_month": "2026-07-01",
  "profile": {
    "tenure_months": 14,
    "customer_segment": "pension",
    "income_regularity": "regular",
    "products_count": 1,
    "has_credit_card": 0,
    "has_loan": 0
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 0,
      "balance_change_30d": -3.7914,
      "transaction_change_30d": -14.2724,
      "card_spend_change_30d": 8.6772,
      "app_login_change_30d": -0.9019,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -8.1142,
      "upi_share_of_spend": 0.4625,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 2,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 38.5849,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-02-01",
      "days_since_last_transaction": 0,
      "balance_change_30d": 1.4807,
      "transaction_change_30d": 21.65,
      "card_spend_change_30d": -32.394,
      "app_login_change_30d": 8.4807,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": 10.5461,
      "upi_share_of_spend": 0.3313,
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
      "days_since_last_transaction": 0,
      "balance_change_30d": -8.6511,
      "transaction_change_30d": 4.8635,
      "card_spend_change_30d": -13.0914,
      "app_login_change_30d": -18.834,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": 5.6906,
      "upi_share_of_spend": 0.3609,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 1,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 19.4464,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-04-01",
      "days_since_last_transaction": 11,
      "balance_change_30d": 2.8992,
      "transaction_change_30d": -9.5362,
      "card_spend_change_30d": 19.417,
      "app_login_change_30d": -1.6021,
      "salary_missing_days": 2.0,
      "external_transfer_change_30d": 36.068,
      "upi_share_of_spend": 0.4757,
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
      "balance_change_30d": -0.159,
      "transaction_change_30d": -4.525,
      "card_spend_change_30d": -15.0199,
      "app_login_change_30d": 9.5007,
      "salary_missing_days": 1.0,
      "external_transfer_change_30d": 8.4028,
      "upi_share_of_spend": 0.4354,
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
      "days_since_last_transaction": 7,
      "balance_change_30d": -12.9505,
      "transaction_change_30d": -9.4562,
      "card_spend_change_30d": -20.1014,
      "app_login_change_30d": 17.9435,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": 38.9543,
      "upi_share_of_spend": 0.3514,
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
    "tenure_months": 14,
    "customer_segment": "pension",
    "income_regularity": "regular",
    "products_count": 1,
    "has_credit_card": 0,
    "has_loan": 0,
    "days_since_last_transaction": 7,
    "balance_change_30d": -12.9505,
    "transaction_change_30d": -9.4562,
    "card_spend_change_30d": -20.1014,
    "app_login_change_30d": 17.9435,
    "salary_missing_days": 0.0,
    "external_transfer_change_30d": 38.9543,
    "upi_share_of_spend": 0.3514,
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
      "tenure_months": 14,
      "age": 78,
      "customer_yearly_value": 25061.7319,
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
    "served_at": "2026-08-31T01:07:22",
    "elapsed_ms": 11906.31,
    "timings_ms": {
      "model1": 77.54,
      "model2": 11828.66
    },
    "customer_id": "C12174",
    "customer_name": "Janya Shere",
    "snapshot_date": "2026-06-01"
  },
  "model1": {
    "churn_probability": 4.15,
    "raw_churn_probability": 34.59,
    "probability_mode": "sigmoid",
    "risk_score": 12.45,
    "churn_prediction": "No",
    "risk_level": "Low",
    "top_risk_factors": [
      {
        "factor": "days_since_last_transaction_trend_6m",
        "value": 2.0857142857142854,
        "message": "Customer has gone longer without transacting.",
        "contribution": 0.11947407573461533
      },
      {
        "factor": "external_transfer_change_30d_trend_6m",
        "value": 7.408285714285712,
        "message": "External transfers have increased.",
        "contribution": 0.04182475432753563
      },
      {
        "factor": "avg_balance_change_30d_3m",
        "value": -3.4034333333333335,
        "message": "Balance has been falling across recent months.",
        "contribution": 0.032789550721645355
      },
      {
        "factor": "latest_vs_avg_balance_change_30d_available_history",
        "value": -9.421816666666667,
        "message": "Balance has been falling across recent months.",
        "contribution": 0.026231760159134865
      },
      {
        "factor": "latest_card_spend_change_30d",
        "value": -20.1014,
        "message": "Card spending has been falling across recent months.",
        "contribution": 0.02490082196891308
      }
    ]
  },
  "model2_input": {
    "customer_context": {
      "age": 78,
      "tenure_months": 14,
      "customer_segment": "pension",
      "income_regularity": "regular",
      "customer_yearly_value": 25061.7319,
      "products_count": 1,
      "has_credit_card": 0,
      "has_loan": 0
    },
    "behavior": {
      "days_since_last_transaction": 7,
      "balance_change_30d": -12.9505,
      "transaction_change_30d": -9.4562,
      "card_spend_change_30d": -20.1014,
      "app_login_change_30d": 17.9435,
      "salary_missing_days": 0,
      "external_transfer_change_30d": 38.9543,
      "upi_share_of_spend": 0.3514,
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
      "churn_probability": 0.0415,
      "churn_prediction": "No",
      "risk_level": "Low",
      "top_risk_factors": [
        {
          "factor": "days_since_last_transaction_trend_6m",
          "value": 2.0857142857142854
        },
        {
          "factor": "external_transfer_change_30d_trend_6m",
          "value": 7.408285714285712
        },
        {
          "factor": "avg_balance_change_30d_3m",
          "value": -3.4034333333333335
        },
        {
          "factor": "vs_avg_balance_change_30d_available_history",
          "value": -9.421816666666667
        },
        {
          "factor": "card_spend_change_30d",
          "value": -20.1014
        }
      ]
    },
    "eligible_actions": [
      "MONITOR",
      "RE_ENGAGEMENT",
      "PRODUCT_REVIEW",
      "SERVICE_RECOVERY"
    ],
    "case_id": "C12174"
  },
  "model2": {
    "case_id": "C12174",
    "ok": false,
    "prediction": null,
    "raw_text": "{\"evidence\":[\"complaints_30d=0\",\"failed_transactions_30d=1\"],\"primary_reason\":\"SERVICE_DISSATISFACTION\",\"reasoning_summary\":\"Service friction is the clearest risk signal here. Complaint escalation fits because complaints_30d=0 and failed_transactions_30d=1 indicate a service issue without a clear resolution or closure.\",\"recommended_action\":\"COMPLAINT_ESCALATION\",\"secondary_reasons\":[\"UNKNOWN\"],\"urgency\":\"MEDIUM\"}",
    "error": "recommended_action: 'COMPLAINT_ESCALATION' not in eligible_actions ['MONITOR', 'RE_ENGAGEMENT', 'PRODUCT_REVIEW', 'SERVICE_RECOVERY']",
    "latency_s": 11.8286,
    "simple_output": "Prediction failed: recommended_action: 'COMPLAINT_ESCALATION' not in eligible_actions ['MONITOR', 'RE_ENGAGEMENT', 'PRODUCT_REVIEW', 'SERVICE_RECOVERY']"
  }
}
```

### Daniel Nanda (`C12454`)

- OK: `True`
- Shape errors: `[]`
- Simple output: Reason: LOW_ENGAGEMENT | Urgency: MEDIUM | Action: RE_ENGAGEMENT | Why: The main signal is broad engagement decline without a stronger cause. Evidence suggests this because transaction_change_30d=1.8; comaints_30d=0.

Request:

```json
{
  "customer_id": "C12454",
  "customer_name": "Daniel Nanda",
  "prediction_date": "2026-06-01",
  "snapshot_date": "2026-06-01",
  "target_month": "2026-07-01",
  "profile": {
    "tenure_months": 35,
    "customer_segment": "vendor",
    "income_regularity": "irregular",
    "products_count": 1,
    "has_credit_card": 0,
    "has_loan": 0
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 9,
      "balance_change_30d": 10.4016,
      "transaction_change_30d": 13.0219,
      "card_spend_change_30d": 27.0524,
      "app_login_change_30d": -10.1098,
      "salary_missing_days": null,
      "external_transfer_change_30d": 27.6163,
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
      "snapshot_date": "2026-02-01",
      "days_since_last_transaction": 0,
      "balance_change_30d": 9.14,
      "transaction_change_30d": 6.1041,
      "card_spend_change_30d": 63.5254,
      "app_login_change_30d": 27.7733,
      "salary_missing_days": null,
      "external_transfer_change_30d": -9.4708,
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
      "snapshot_date": "2026-03-01",
      "days_since_last_transaction": 5,
      "balance_change_30d": -4.5075,
      "transaction_change_30d": 6.0337,
      "card_spend_change_30d": 15.4394,
      "app_login_change_30d": 18.7049,
      "salary_missing_days": null,
      "external_transfer_change_30d": -21.9745,
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
      "snapshot_date": "2026-04-01",
      "days_since_last_transaction": 7,
      "balance_change_30d": -8.8768,
      "transaction_change_30d": -9.268,
      "card_spend_change_30d": 22.1104,
      "app_login_change_30d": -8.4873,
      "salary_missing_days": null,
      "external_transfer_change_30d": 24.5782,
      "upi_share_of_spend": 0.0,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 1.0,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-05-01",
      "days_since_last_transaction": 3,
      "balance_change_30d": 25.9907,
      "transaction_change_30d": 13.0597,
      "card_spend_change_30d": 32.1545,
      "app_login_change_30d": -12.5154,
      "salary_missing_days": null,
      "external_transfer_change_30d": -33.4431,
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
      "snapshot_date": "2026-06-01",
      "days_since_last_transaction": 4,
      "balance_change_30d": 19.8167,
      "transaction_change_30d": 1.758,
      "card_spend_change_30d": 28.2509,
      "app_login_change_30d": 27.123,
      "salary_missing_days": null,
      "external_transfer_change_30d": -17.4898,
      "upi_share_of_spend": 0.0,
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
    "tenure_months": 35,
    "customer_segment": "vendor",
    "income_regularity": "irregular",
    "products_count": 1,
    "has_credit_card": 0,
    "has_loan": 0,
    "days_since_last_transaction": 4,
    "balance_change_30d": 19.8167,
    "transaction_change_30d": 1.758,
    "card_spend_change_30d": 28.2509,
    "app_login_change_30d": 27.123,
    "salary_missing_days": null,
    "external_transfer_change_30d": -17.4898,
    "upi_share_of_spend": 0.0,
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
      "tenure_months": 35,
      "age": 55,
      "customer_yearly_value": 45577.7973,
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
    "served_at": "2026-08-31T01:07:24",
    "elapsed_ms": 2092.57,
    "timings_ms": {
      "model1": 66.91,
      "model2": 2025.55
    },
    "customer_id": "C12454",
    "customer_name": "Daniel Nanda",
    "snapshot_date": "2026-06-01"
  },
  "model1": {
    "churn_probability": 2.56,
    "raw_churn_probability": 23.86,
    "probability_mode": "sigmoid",
    "risk_score": 7.68,
    "churn_prediction": "No",
    "risk_level": "Low",
    "top_risk_factors": [
      {
        "factor": "latest_upi_share_of_spend",
        "value": 0.0,
        "message": "This signal increased churn risk.",
        "contribution": 0.06550946831703186
      },
      {
        "factor": "latest_vs_avg_external_transfer_change_30d_available_history",
        "value": -12.459183333333332,
        "message": "This signal increased churn risk.",
        "contribution": 0.03101067990064621
      },
      {
        "factor": "transaction_change_30d_trend_6m",
        "value": -1.4501257142857136,
        "message": "Transaction activity has been falling across recent months.",
        "contribution": 0.02892669104039669
      },
      {
        "factor": "sum_failed_transactions_30d_6m",
        "value": 4.0,
        "message": "Customer has recent failed transactions.",
        "contribution": 0.008641685359179974
      },
      {
        "factor": "count_balance_drop_3m",
        "value": 1,
        "message": "This signal increased churn risk.",
        "contribution": 0.0060357521288096905
      }
    ]
  },
  "model2_input": {
    "customer_context": {
      "age": 55,
      "tenure_months": 35,
      "customer_segment": "vendor",
      "income_regularity": "irregular",
      "customer_yearly_value": 45577.7973,
      "products_count": 1,
      "has_credit_card": 0,
      "has_loan": 0
    },
    "behavior": {
      "days_since_last_transaction": 4,
      "balance_change_30d": 19.8167,
      "transaction_change_30d": 1.758,
      "card_spend_change_30d": 28.2509,
      "app_login_change_30d": 27.123,
      "salary_missing_days": null,
      "external_transfer_change_30d": -17.4898,
      "upi_share_of_spend": 0.0,
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
          "factor": "upi_share_of_spend",
          "value": 0.0
        },
        {
          "factor": "vs_avg_external_transfer_change_30d_available_history",
          "value": -12.459183333333332
        },
        {
          "factor": "transaction_change_30d_trend_6m",
          "value": -1.4501257142857136
        },
        {
          "factor": "sum_failed_transactions_30d_6m",
          "value": 4.0
        },
        {
          "factor": "count_balance_drop_3m",
          "value": 1
        }
      ]
    },
    "eligible_actions": [
      "MONITOR",
      "RE_ENGAGEMENT",
      "PRODUCT_REVIEW"
    ],
    "case_id": "C12454"
  },
  "model2": {
    "case_id": "C12454",
    "ok": true,
    "prediction": {
      "evidence": [
        "transaction_change_30d=1.8",
        "complaints_30d=0",
        "external_transfer_change_30d=-17.5"
      ],
      "primary_reason": "LOW_ENGAGEMENT",
      "reasoning_summary": "The main signal is broad engagement decline without a stronger cause. Evidence suggests this because transaction_change_30d=1.8; comaints_30d=0.",
      "recommended_action": "RE_ENGAGEMENT",
      "secondary_reasons": [
        "UNKNOWN"
      ],
      "urgency": "MEDIUM"
    },
    "raw_text": "{\n\"evidence\":[\"transaction_change_30d=1.8\",\"complaints_30d=0\",\"external_transfer_change_30d=-17.5\"],\"primary_reason\":\"LOW_ENGAGEMENT\",\"reasoning_summary\":\"The main signal is broad engagement decline without a stronger cause. Evidence suggests this because transaction_change_30d=1.8; comaints_30d=0.\",\"recommended_action\":\"RE_ENGAGEMENT\",\"secondary_reasons\":[\"UNKNOWN\"],\"urgency\":\"MEDIUM\"}",
    "error": null,
    "latency_s": 2.0254,
    "simple_output": "Reason: LOW_ENGAGEMENT | Urgency: MEDIUM | Action: RE_ENGAGEMENT | Why: The main signal is broad engagement decline without a stronger cause. Evidence suggests this because transaction_change_30d=1.8; comaints_30d=0."
  }
}
```

### Kamya Samra (`C13091`)

- OK: `False`
- Shape errors: `["model2 returned ok=false: recommended_action: 'COMPLAINT_ESCALATION' not in eligible_actions ['MONITOR', 'RE_ENGAGEMENT', 'PRODUCT_REVIEW', 'SERVICE_RECOVERY']", 'model2.prediction is missing or not an object']`
- Simple output: Prediction failed: recommended_action: 'COMPLAINT_ESCALATION' not in eligible_actions ['MONITOR', 'RE_ENGAGEMENT', 'PRODUCT_REVIEW', 'SERVICE_RECOVERY']

Request:

```json
{
  "customer_id": "C13091",
  "customer_name": "Kamya Samra",
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
      "days_since_last_transaction": 8,
      "balance_change_30d": -28.1562,
      "transaction_change_30d": -8.3429,
      "card_spend_change_30d": 11.2428,
      "app_login_change_30d": 5.0671,
      "salary_missing_days": null,
      "external_transfer_change_30d": 42.3703,
      "upi_share_of_spend": 0.3199,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 4,
      "unresolved_complaints": 2,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 52.5571,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-02-01",
      "days_since_last_transaction": 5,
      "balance_change_30d": -25.9339,
      "transaction_change_30d": 6.7223,
      "card_spend_change_30d": 5.5851,
      "app_login_change_30d": 4.5842,
      "salary_missing_days": null,
      "external_transfer_change_30d": -10.492,
      "upi_share_of_spend": 0.1951,
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
      "days_since_last_transaction": 7,
      "balance_change_30d": 7.6855,
      "transaction_change_30d": -0.812,
      "card_spend_change_30d": 19.0862,
      "app_login_change_30d": 21.6241,
      "salary_missing_days": null,
      "external_transfer_change_30d": -6.1708,
      "upi_share_of_spend": 0.3181,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 1,
      "complaints_30d": 1,
      "unresolved_complaints": 1,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 49.7194,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-04-01",
      "days_since_last_transaction": 9,
      "balance_change_30d": 14.1855,
      "transaction_change_30d": -2.9918,
      "card_spend_change_30d": 4.0771,
      "app_login_change_30d": -4.9994,
      "salary_missing_days": null,
      "external_transfer_change_30d": 0.9084,
      "upi_share_of_spend": 0.3242,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 15.2648,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-05-01",
      "days_since_last_transaction": 8,
      "balance_change_30d": -41.2326,
      "transaction_change_30d": -13.3282,
      "card_spend_change_30d": -30.9601,
      "app_login_change_30d": -35.0149,
      "salary_missing_days": null,
      "external_transfer_change_30d": 28.7453,
      "upi_share_of_spend": 0.4972,
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
      "days_since_last_transaction": 13,
      "balance_change_30d": -13.6486,
      "transaction_change_30d": -5.8422,
      "card_spend_change_30d": -13.1384,
      "app_login_change_30d": -15.0782,
      "salary_missing_days": null,
      "external_transfer_change_30d": 37.3623,
      "upi_share_of_spend": 0.3798,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 4.7686,
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
    "days_since_last_transaction": 13,
    "balance_change_30d": -13.6486,
    "transaction_change_30d": -5.8422,
    "card_spend_change_30d": -13.1384,
    "app_login_change_30d": -15.0782,
    "salary_missing_days": null,
    "external_transfer_change_30d": 37.3623,
    "upi_share_of_spend": 0.3798,
    "fd_maturing_in_30d": 0,
    "products_dropped_90d": 0,
    "complaints_30d": 1,
    "unresolved_complaints": 0,
    "failed_transactions_30d": 0,
    "avg_resolution_time_hrs": 4.7686,
    "emi_bounce_30d": 0
  },
  "extra_context": {
    "customer_profile": {
      "segment": "vendor",
      "income_regularity": "irregular",
      "tenure_months": 8,
      "age": 49,
      "customer_yearly_value": 22147.0865,
      "products_count": 1,
      "has_credit_card": 0,
      "has_loan": 0,
      "value_tier": "low"
    },
    "recent_complaint_text": "Card swallow ho gaya machine me. Branch ne kaha 15 din lagenge."
  }
}
```

Response:

```json
{
  "meta": {
    "endpoint": "/predict/both",
    "served_at": "2026-08-31T01:07:28",
    "elapsed_ms": 4257.2,
    "timings_ms": {
      "model1": 52.53,
      "model2": 4204.56
    },
    "customer_id": "C13091",
    "customer_name": "Kamya Samra",
    "snapshot_date": "2026-06-01"
  },
  "model1": {
    "churn_probability": 11.27,
    "raw_churn_probability": 57.7,
    "probability_mode": "sigmoid",
    "risk_score": 35.09,
    "churn_prediction": "No",
    "risk_level": "Low",
    "top_risk_factors": [
      {
        "factor": "latest_days_since_last_transaction",
        "value": 13,
        "message": "Customer has gone longer without transacting.",
        "contribution": 0.3379683494567871
      },
      {
        "factor": "sum_complaints_30d_6m",
        "value": 7.0,
        "message": "Customer has recent complaint activity.",
        "contribution": 0.07859405875205994
      },
      {
        "factor": "sum_fd_maturing_in_30d_3m",
        "value": 1.0,
        "message": "Customer has a fixed deposit maturing soon.",
        "contribution": 0.07209261506795883
      },
      {
        "factor": "latest_vs_avg_upi_share_of_spend_available_history",
        "value": 0.04075000000000001,
        "message": "A larger share of spending is happening through UPI.",
        "contribution": 0.06970048695802689
      },
      {
        "factor": "count_balance_drop_6m",
        "value": 4,
        "message": "This signal increased churn risk.",
        "contribution": 0.04047052189707756
      }
    ]
  },
  "model2_input": {
    "customer_context": {
      "age": 49,
      "tenure_months": 8,
      "customer_segment": "vendor",
      "income_regularity": "irregular",
      "customer_yearly_value": 22147.0865,
      "products_count": 1,
      "has_credit_card": 0,
      "has_loan": 0
    },
    "behavior": {
      "days_since_last_transaction": 13,
      "balance_change_30d": -13.6486,
      "transaction_change_30d": -5.8422,
      "card_spend_change_30d": -13.1384,
      "app_login_change_30d": -15.0782,
      "salary_missing_days": null,
      "external_transfer_change_30d": 37.3623,
      "upi_share_of_spend": 0.3798,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "emi_bounce_30d": 0
    },
    "service_evidence": {
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 4.7686,
      "complaint_text": "Card swallow ho gaya machine me. Branch ne kaha 15 din lagenge."
    },
    "model1": {
      "churn_probability": 0.1127,
      "churn_prediction": "No",
      "risk_level": "Low",
      "top_risk_factors": [
        {
          "factor": "days_since_last_transaction",
          "value": 13
        },
        {
          "factor": "sum_complaints_30d_6m",
          "value": 7.0
        },
        {
          "factor": "sum_fd_maturing_in_30d_3m",
          "value": 1.0
        },
        {
          "factor": "vs_avg_upi_share_of_spend_available_history",
          "value": 0.04075000000000001
        },
        {
          "factor": "count_balance_drop_6m",
          "value": 4
        }
      ]
    },
    "eligible_actions": [
      "MONITOR",
      "RE_ENGAGEMENT",
      "PRODUCT_REVIEW",
      "SERVICE_RECOVERY"
    ],
    "case_id": "C13091"
  },
  "model2": {
    "case_id": "C13091",
    "ok": false,
    "prediction": null,
    "raw_text": "{\"evidence\":[\"complaints_30d=1\",\"failed_transactions_30d=0\",\"avg_resolution_time_hrs=4.8\",\"complaint_text describes a recent service issue\"],\"primary_reason\":\"SERVICE_DISSATISFACTION\",\"reasoning_summary\":\"Service friction is the clearest risk signal here. Complaint escalation fits because complaints_30d=1 and avg_resolution_time_hrs=4.8 indicate the issue is unresolved or operationally serious.\",\"recommended_action\":\"COMPLAINT_ESCALATION\",\"secondary_reasons\":[\"UNKNOWN\"],\"urgency\":\"MEDIUM\"}",
    "error": "recommended_action: 'COMPLAINT_ESCALATION' not in eligible_actions ['MONITOR', 'RE_ENGAGEMENT', 'PRODUCT_REVIEW', 'SERVICE_RECOVERY']",
    "latency_s": 4.2045,
    "simple_output": "Prediction failed: recommended_action: 'COMPLAINT_ESCALATION' not in eligible_actions ['MONITOR', 'RE_ENGAGEMENT', 'PRODUCT_REVIEW', 'SERVICE_RECOVERY']"
  }
}
```

### Mohini Lad (`C13637`)

- OK: `True`
- Shape errors: `[]`
- Simple output: Reason: LOW_ENGAGEMENT | Urgency: MEDIUM | Action: RE_ENGAGEMENT | Why: The main signal is broad engagement decline without a stronger cause. Service evidence is mixed or insufficient.

Request:

```json
{
  "customer_id": "C13637",
  "customer_name": "Mohini Lad",
  "prediction_date": "2026-06-01",
  "snapshot_date": "2026-06-01",
  "target_month": "2026-07-01",
  "profile": {
    "tenure_months": 166,
    "customer_segment": "business",
    "income_regularity": "irregular",
    "products_count": 2,
    "has_credit_card": 1,
    "has_loan": 0
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 0,
      "balance_change_30d": 13.4211,
      "transaction_change_30d": 33.1711,
      "card_spend_change_30d": 10.9117,
      "app_login_change_30d": -25.7076,
      "salary_missing_days": null,
      "external_transfer_change_30d": -6.0965,
      "upi_share_of_spend": 0.373,
      "fd_maturing_in_30d": 1,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 5.3378,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-02-01",
      "days_since_last_transaction": 5,
      "balance_change_30d": -7.0594,
      "transaction_change_30d": -6.7954,
      "card_spend_change_30d": 1.3817,
      "app_login_change_30d": 7.3222,
      "salary_missing_days": null,
      "external_transfer_change_30d": 72.94,
      "upi_share_of_spend": 0.3717,
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
      "days_since_last_transaction": 2,
      "balance_change_30d": 21.1518,
      "transaction_change_30d": 29.3041,
      "card_spend_change_30d": 13.6036,
      "app_login_change_30d": 3.8521,
      "salary_missing_days": null,
      "external_transfer_change_30d": -16.8253,
      "upi_share_of_spend": 0.4279,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 2,
      "unresolved_complaints": 1,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 16.8076,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-04-01",
      "days_since_last_transaction": 9,
      "balance_change_30d": 5.8017,
      "transaction_change_30d": 6.11,
      "card_spend_change_30d": 10.4475,
      "app_login_change_30d": 0.356,
      "salary_missing_days": null,
      "external_transfer_change_30d": 5.0242,
      "upi_share_of_spend": 0.3436,
      "fd_maturing_in_30d": 1,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 62.0037,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-05-01",
      "days_since_last_transaction": 5,
      "balance_change_30d": 26.2114,
      "transaction_change_30d": 32.5567,
      "card_spend_change_30d": 29.3243,
      "app_login_change_30d": 28.3234,
      "salary_missing_days": null,
      "external_transfer_change_30d": -18.664,
      "upi_share_of_spend": 0.4255,
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
      "days_since_last_transaction": 2,
      "balance_change_30d": 0.8587,
      "transaction_change_30d": 8.9479,
      "card_spend_change_30d": 41.5812,
      "app_login_change_30d": -4.4888,
      "salary_missing_days": null,
      "external_transfer_change_30d": 6.1068,
      "upi_share_of_spend": 0.3955,
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
    "customer_segment": "business",
    "income_regularity": "irregular",
    "products_count": 2,
    "has_credit_card": 1,
    "has_loan": 0,
    "days_since_last_transaction": 2,
    "balance_change_30d": 0.8587,
    "transaction_change_30d": 8.9479,
    "card_spend_change_30d": 41.5812,
    "app_login_change_30d": -4.4888,
    "salary_missing_days": null,
    "external_transfer_change_30d": 6.1068,
    "upi_share_of_spend": 0.3955,
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
      "tenure_months": 166,
      "age": 51,
      "customer_yearly_value": 155485.3032,
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
    "served_at": "2026-08-31T01:07:31",
    "elapsed_ms": 2038.84,
    "timings_ms": {
      "model1": 80.36,
      "model2": 1958.34
    },
    "customer_id": "C13637",
    "customer_name": "Mohini Lad",
    "snapshot_date": "2026-06-01"
  },
  "model1": {
    "churn_probability": 3.72,
    "raw_churn_probability": 32.15,
    "probability_mode": "sigmoid",
    "risk_score": 11.17,
    "churn_prediction": "No",
    "risk_level": "Low",
    "top_risk_factors": [
      {
        "factor": "max_avg_resolution_time_hrs_3m",
        "value": 62.0037,
        "message": "Recent complaints took longer to resolve.",
        "contribution": 0.42455461621284485
      },
      {
        "factor": "sum_fd_maturing_in_30d_3m",
        "value": 1.0,
        "message": "Customer has a fixed deposit maturing soon.",
        "contribution": 0.06816527992486954
      },
      {
        "factor": "card_spend_change_30d_trend_6m",
        "value": 6.686262857142856,
        "message": "This signal increased churn risk.",
        "contribution": 0.03684447333216667
      },
      {
        "factor": "avg_transaction_change_30d_6m",
        "value": 17.215733333333333,
        "message": "This signal increased churn risk.",
        "contribution": 0.02896474301815033
      },
      {
        "factor": "latest_vs_avg_upi_share_of_spend_available_history",
        "value": 0.005966666666666676,
        "message": "A larger share of spending is happening through UPI.",
        "contribution": 0.018912145867943764
      }
    ]
  },
  "model2_input": {
    "customer_context": {
      "age": 51,
      "tenure_months": 166,
      "customer_segment": "business",
      "income_regularity": "irregular",
      "customer_yearly_value": 155485.3032,
      "products_count": 2,
      "has_credit_card": 1,
      "has_loan": 0
    },
    "behavior": {
      "days_since_last_transaction": 2,
      "balance_change_30d": 0.8587,
      "transaction_change_30d": 8.9479,
      "card_spend_change_30d": 41.5812,
      "app_login_change_30d": -4.4888,
      "salary_missing_days": null,
      "external_transfer_change_30d": 6.1068,
      "upi_share_of_spend": 0.3955,
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
      "churn_probability": 0.0372,
      "churn_prediction": "No",
      "risk_level": "Low",
      "top_risk_factors": [
        {
          "factor": "max_avg_resolution_time_hrs_3m",
          "value": 62.0037
        },
        {
          "factor": "sum_fd_maturing_in_30d_3m",
          "value": 1.0
        },
        {
          "factor": "card_spend_change_30d_trend_6m",
          "value": 6.686262857142856
        },
        {
          "factor": "avg_transaction_change_30d_6m",
          "value": 17.215733333333333
        },
        {
          "factor": "vs_avg_upi_share_of_spend_available_history",
          "value": 0.005966666666666676
        }
      ]
    },
    "eligible_actions": [
      "MONITOR",
      "RE_ENGAGEMENT",
      "PRODUCT_REVIEW"
    ],
    "case_id": "C13637"
  },
  "model2": {
    "case_id": "C13637",
    "ok": true,
    "prediction": {
      "evidence": [
        "transaction_change_30d=8.9",
        "balance_change_30d=0.9",
        "complaints_30d=0",
        "failed_transactions_30d=0",
        "avg_resolution_time_hrs=0.0"
      ],
      "primary_reason": "LOW_ENGAGEMENT",
      "reasoning_summary": "The main signal is broad engagement decline without a stronger cause. Service evidence is mixed or insufficient.",
      "recommended_action": "RE_ENGAGEMENT",
      "secondary_reasons": [
        "UNKNOWN"
      ],
      "urgency": "MEDIUM"
    },
    "raw_text": "{\"evidence\":[\"transaction_change_30d=8.9\",\"balance_change_30d=0.9\",\"complaints_30d=0\",\"failed_transactions_30d=0\",\"avg_resolution_time_hrs=0.0\"],\"primary_reason\":\"LOW_ENGAGEMENT\",\"reasoning_summary\":\"The main signal is broad engagement decline without a stronger cause. Service evidence is mixed or insufficient.\",\"recommended_action\":\"RE_ENGAGEMENT\",\"secondary_reasons\":[\"UNKNOWN\"],\"urgency\":\"MEDIUM\"}",
    "error": null,
    "latency_s": 1.9554,
    "simple_output": "Reason: LOW_ENGAGEMENT | Urgency: MEDIUM | Action: RE_ENGAGEMENT | Why: The main signal is broad engagement decline without a stronger cause. Service evidence is mixed or insufficient."
  }
}
```

### Raagini Deol (`C14216`)

- OK: `False`
- Shape errors: `["model2 returned ok=false: recommended_action: 'COMPLAINT_ESCALATION' not in eligible_actions ['MONITOR', 'RE_ENGAGEMENT', 'PRODUCT_REVIEW', 'SERVICE_RECOVERY', 'FINANCIAL_GUIDANCE', 'RM_CALLBACK']", 'model2.prediction is missing or not an object']`
- Simple output: Prediction failed: recommended_action: 'COMPLAINT_ESCALATION' not in eligible_actions ['MONITOR', 'RE_ENGAGEMENT', 'PRODUCT_REVIEW', 'SERVICE_RECOVERY', 'FINANCIAL_GUIDANCE', 'RM_CALLBACK']

Request:

```json
{
  "customer_id": "C14216",
  "customer_name": "Raagini Deol",
  "prediction_date": "2026-06-01",
  "snapshot_date": "2026-06-01",
  "target_month": "2026-07-01",
  "profile": {
    "tenure_months": 94,
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
      "balance_change_30d": -0.92,
      "transaction_change_30d": -28.5262,
      "card_spend_change_30d": -11.6131,
      "app_login_change_30d": 1.3164,
      "salary_missing_days": 2.0,
      "external_transfer_change_30d": -3.3734,
      "upi_share_of_spend": 0.4173,
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
      "balance_change_30d": 1.3191,
      "transaction_change_30d": 2.7263,
      "card_spend_change_30d": -15.0004,
      "app_login_change_30d": 15.3412,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": 12.9832,
      "upi_share_of_spend": 0.3585,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 0,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 2,
      "avg_resolution_time_hrs": 0.0,
      "emi_bounce_30d": 1
    },
    {
      "snapshot_date": "2026-03-01",
      "days_since_last_transaction": 6,
      "balance_change_30d": 21.7436,
      "transaction_change_30d": -7.0607,
      "card_spend_change_30d": 23.275,
      "app_login_change_30d": 29.612,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": 3.661,
      "upi_share_of_spend": 0.3382,
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
      "balance_change_30d": 10.3878,
      "transaction_change_30d": 11.1398,
      "card_spend_change_30d": 32.0148,
      "app_login_change_30d": 24.8362,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -0.8422,
      "upi_share_of_spend": 0.3524,
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
      "days_since_last_transaction": 11,
      "balance_change_30d": -22.0243,
      "transaction_change_30d": -14.4186,
      "card_spend_change_30d": 12.1451,
      "app_login_change_30d": -9.5603,
      "salary_missing_days": 1.0,
      "external_transfer_change_30d": 14.2159,
      "upi_share_of_spend": 0.4709,
      "fd_maturing_in_30d": 1,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 25.2369,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-06-01",
      "days_since_last_transaction": 10,
      "balance_change_30d": -7.8647,
      "transaction_change_30d": -3.0136,
      "card_spend_change_30d": 6.5818,
      "app_login_change_30d": 0.063,
      "salary_missing_days": 4.0,
      "external_transfer_change_30d": 11.6202,
      "upi_share_of_spend": 0.5056,
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
    "tenure_months": 94,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 3,
    "has_credit_card": 0,
    "has_loan": 1,
    "days_since_last_transaction": 10,
    "balance_change_30d": -7.8647,
    "transaction_change_30d": -3.0136,
    "card_spend_change_30d": 6.5818,
    "app_login_change_30d": 0.063,
    "salary_missing_days": 4.0,
    "external_transfer_change_30d": 11.6202,
    "upi_share_of_spend": 0.5056,
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
      "tenure_months": 94,
      "age": 46,
      "customer_yearly_value": 8773.6892,
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
    "served_at": "2026-08-31T01:07:37",
    "elapsed_ms": 5979.96,
    "timings_ms": {
      "model1": 170.28,
      "model2": 5809.55
    },
    "customer_id": "C14216",
    "customer_name": "Raagini Deol",
    "snapshot_date": "2026-06-01"
  },
  "model1": {
    "churn_probability": 5.37,
    "raw_churn_probability": 40.41,
    "probability_mode": "sigmoid",
    "risk_score": 16.12,
    "churn_prediction": "No",
    "risk_level": "Low",
    "top_risk_factors": [
      {
        "factor": "latest_salary_missing_days",
        "value": 4.0,
        "message": "Salary or pension was delayed recently.",
        "contribution": 0.2644919455051422
      },
      {
        "factor": "latest_vs_avg_upi_share_of_spend_available_history",
        "value": 0.09845000000000009,
        "message": "A larger share of spending is happening through UPI.",
        "contribution": 0.17964798212051392
      },
      {
        "factor": "days_since_last_transaction_trend_6m",
        "value": 1.1428571428571426,
        "message": "Customer has gone longer without transacting.",
        "contribution": 0.11521219462156296
      },
      {
        "factor": "sum_fd_maturing_in_30d_3m",
        "value": 1.0,
        "message": "Customer has a fixed deposit maturing soon.",
        "contribution": 0.08475742489099503
      },
      {
        "factor": "card_spend_change_30d_trend_6m",
        "value": 5.175737142857141,
        "message": "This signal increased churn risk.",
        "contribution": 0.018214033916592598
      }
    ]
  },
  "model2_input": {
    "customer_context": {
      "age": 46,
      "tenure_months": 94,
      "customer_segment": "salary",
      "income_regularity": "regular",
      "customer_yearly_value": 8773.6892,
      "products_count": 3,
      "has_credit_card": 0,
      "has_loan": 1
    },
    "behavior": {
      "days_since_last_transaction": 10,
      "balance_change_30d": -7.8647,
      "transaction_change_30d": -3.0136,
      "card_spend_change_30d": 6.5818,
      "app_login_change_30d": 0.063,
      "salary_missing_days": 4,
      "external_transfer_change_30d": 11.6202,
      "upi_share_of_spend": 0.5056,
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
      "churn_probability": 0.0537,
      "churn_prediction": "No",
      "risk_level": "Low",
      "top_risk_factors": [
        {
          "factor": "salary_missing_days",
          "value": 4.0
        },
        {
          "factor": "vs_avg_upi_share_of_spend_available_history",
          "value": 0.09845000000000009
        },
        {
          "factor": "days_since_last_transaction_trend_6m",
          "value": 1.1428571428571426
        },
        {
          "factor": "sum_fd_maturing_in_30d_3m",
          "value": 1.0
        },
        {
          "factor": "card_spend_change_30d_trend_6m",
          "value": 5.175737142857141
        }
      ]
    },
    "eligible_actions": [
      "MONITOR",
      "RE_ENGAGEMENT",
      "PRODUCT_REVIEW",
      "SERVICE_RECOVERY",
      "FINANCIAL_GUIDANCE",
      "RM_CALLBACK"
    ],
    "case_id": "C14216"
  },
  "model2": {
    "case_id": "C14216",
    "ok": false,
    "prediction": null,
    "raw_text": "{\"evidence\":[\"transaction_change_30d=-3.0\",\"balance_change_30d=-7.9\",\"complaints_30d=0\",\"failed_transactions_30d=1\",\"avg_resolution_time_hrs=0.0\"],\"primary_reason\":\"SERVICE_DISSATISFACTION\",\"reasoning_summary\":\"Service friction is the clearest risk signal here. Complaint escalation fits because complaints_30d=0 and failed_transactions_30d=1 suggest a service issue with unresolved_complaints=0.\",\"recommended_action\":\"COMPLAINT_ESCALATION\",\"secondary_reasons\":[\"UNKNOWN\"],\"urgency\":\"MEDIUM\"}",
    "error": "recommended_action: 'COMPLAINT_ESCALATION' not in eligible_actions ['MONITOR', 'RE_ENGAGEMENT', 'PRODUCT_REVIEW', 'SERVICE_RECOVERY', 'FINANCIAL_GUIDANCE', 'RM_CALLBACK']",
    "latency_s": 5.8094,
    "simple_output": "Prediction failed: recommended_action: 'COMPLAINT_ESCALATION' not in eligible_actions ['MONITOR', 'RE_ENGAGEMENT', 'PRODUCT_REVIEW', 'SERVICE_RECOVERY', 'FINANCIAL_GUIDANCE', 'RM_CALLBACK']"
  }
}
```

### Robert Patla (`C14339`)

- OK: `True`
- Shape errors: `[]`
- Simple output: Reason: SERVICE_DISSATISFACTION | Urgency: HIGH | Action: COMPLAINT_ESCALATION | Why: Service friction is the clearest risk signal here. Complaint escalation fits because complaints_30d=0 and unresolved_complaints=0 indicate the issue is unresolved or operationally related rather than a product problem.

Request:

```json
{
  "customer_id": "C14339",
  "customer_name": "Robert Patla",
  "prediction_date": "2026-04-01",
  "snapshot_date": "2026-04-01",
  "target_month": "2026-05-01",
  "profile": {
    "tenure_months": 184,
    "customer_segment": "pension",
    "income_regularity": "regular",
    "products_count": 1,
    "has_credit_card": 0,
    "has_loan": 0
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 1,
      "balance_change_30d": 24.0814,
      "transaction_change_30d": 24.736,
      "card_spend_change_30d": 35.6967,
      "app_login_change_30d": 6.6018,
      "salary_missing_days": 2.0,
      "external_transfer_change_30d": 12.1198,
      "upi_share_of_spend": 0.569,
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
      "balance_change_30d": -0.5862,
      "transaction_change_30d": 9.6067,
      "card_spend_change_30d": 14.6831,
      "app_login_change_30d": 15.9697,
      "salary_missing_days": 2.0,
      "external_transfer_change_30d": -25.9493,
      "upi_share_of_spend": 0.5832,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 38.1966,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-03-01",
      "days_since_last_transaction": 12,
      "balance_change_30d": -29.8054,
      "transaction_change_30d": -24.3406,
      "card_spend_change_30d": -31.678,
      "app_login_change_30d": -35.0653,
      "salary_missing_days": 5.0,
      "external_transfer_change_30d": 21.9408,
      "upi_share_of_spend": 0.6562,
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
      "days_since_last_transaction": 16,
      "balance_change_30d": -40.6337,
      "transaction_change_30d": -15.3609,
      "card_spend_change_30d": -40.9608,
      "app_login_change_30d": -14.4443,
      "salary_missing_days": 6.0,
      "external_transfer_change_30d": 93.9715,
      "upi_share_of_spend": 0.7146,
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
    "tenure_months": 184,
    "customer_segment": "pension",
    "income_regularity": "regular",
    "products_count": 1,
    "has_credit_card": 0,
    "has_loan": 0,
    "days_since_last_transaction": 16,
    "balance_change_30d": -40.6337,
    "transaction_change_30d": -15.3609,
    "card_spend_change_30d": -40.9608,
    "app_login_change_30d": -14.4443,
    "salary_missing_days": 6.0,
    "external_transfer_change_30d": 93.9715,
    "upi_share_of_spend": 0.7146,
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
      "tenure_months": 184,
      "age": 76,
      "customer_yearly_value": 10053.4074,
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
    "served_at": "2026-08-31T01:07:39",
    "elapsed_ms": 2808.67,
    "timings_ms": {
      "model1": 184.49,
      "model2": 2624.04
    },
    "customer_id": "C14339",
    "customer_name": "Robert Patla",
    "snapshot_date": "2026-04-01"
  },
  "model1": {
    "churn_probability": 31.49,
    "raw_churn_probability": 85.32,
    "probability_mode": "sigmoid",
    "risk_score": 74.31,
    "churn_prediction": "Yes",
    "risk_level": "High",
    "top_risk_factors": [
      {
        "factor": "latest_days_since_last_transaction",
        "value": 16,
        "message": "Customer has gone longer without transacting.",
        "contribution": 0.4520149230957031
      },
      {
        "factor": "latest_salary_missing_days",
        "value": 6.0,
        "message": "Salary or pension was delayed recently.",
        "contribution": 0.3030191957950592
      },
      {
        "factor": "latest_vs_avg_upi_share_of_spend_available_history",
        "value": 0.08384999999999998,
        "message": "A larger share of spending is happening through UPI.",
        "contribution": 0.24637103080749512
      },
      {
        "factor": "days_since_last_transaction_trend_6m",
        "value": 5.0,
        "message": "Customer has gone longer without transacting.",
        "contribution": 0.19076867401599884
      },
      {
        "factor": "latest_balance_change_30d",
        "value": -40.6337,
        "message": "Balance has been falling across recent months.",
        "contribution": 0.17922760546207428
      }
    ]
  },
  "model2_input": {
    "customer_context": {
      "age": 76,
      "tenure_months": 184,
      "customer_segment": "pension",
      "income_regularity": "regular",
      "customer_yearly_value": 10053.4074,
      "products_count": 1,
      "has_credit_card": 0,
      "has_loan": 0
    },
    "behavior": {
      "days_since_last_transaction": 16,
      "balance_change_30d": -40.6337,
      "transaction_change_30d": -15.3609,
      "card_spend_change_30d": -40.9608,
      "app_login_change_30d": -14.4443,
      "salary_missing_days": 6,
      "external_transfer_change_30d": 93.9715,
      "upi_share_of_spend": 0.7146,
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
      "churn_probability": 0.3149,
      "churn_prediction": "Yes",
      "risk_level": "High",
      "top_risk_factors": [
        {
          "factor": "days_since_last_transaction",
          "value": 16
        },
        {
          "factor": "salary_missing_days",
          "value": 6.0
        },
        {
          "factor": "vs_avg_upi_share_of_spend_available_history",
          "value": 0.08384999999999998
        },
        {
          "factor": "days_since_last_transaction_trend_6m",
          "value": 5.0
        },
        {
          "factor": "balance_change_30d",
          "value": -40.6337
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
    "case_id": "C14339"
  },
  "model2": {
    "case_id": "C14339",
    "ok": true,
    "prediction": {
      "evidence": [
        "complaints_30d=0",
        "unresolved_complaints=0",
        "failed_transactions_30d=1",
        "avg_resolution_time_hrs=0.0"
      ],
      "primary_reason": "SERVICE_DISSATISFACTION",
      "reasoning_summary": "Service friction is the clearest risk signal here. Complaint escalation fits because complaints_30d=0 and unresolved_complaints=0 indicate the issue is unresolved or operationally related rather than a product problem.",
      "recommended_action": "COMPLAINT_ESCALATION",
      "secondary_reasons": [
        "UNKNOWN"
      ],
      "urgency": "HIGH"
    },
    "raw_text": "{\"evidence\":[\"complaints_30d=0\",\"unresolved_complaints=0\",\"failed_transactions_30d=1\",\"avg_resolution_time_hrs=0.0\"],\"primary_reason\":\"SERVICE_DISSATISFACTION\",\"reasoning_summary\":\"Service friction is the clearest risk signal here. Complaint escalation fits because complaints_30d=0 and unresolved_complaints=0 indicate the issue is unresolved or operationally related rather than a product problem.\",\"recommended_action\":\"COMPLAINT_ESCALATION\",\"secondary_reasons\":[\"UNKNOWN\"],\"urgency\":\"HIGH\"}",
    "error": null,
    "latency_s": 2.6238,
    "simple_output": "Reason: SERVICE_DISSATISFACTION | Urgency: HIGH | Action: COMPLAINT_ESCALATION | Why: Service friction is the clearest risk signal here. Complaint escalation fits because complaints_30d=0 and unresolved_complaints=0 indicate the issue is unresolved or operationally related rather than a product problem."
  }
}
```

### Waida Chanda (`C14830`)

- OK: `True`
- Shape errors: `[]`
- Simple output: Reason: SERVICE_DISSATISFACTION | Urgency: MEDIUM | Action: COMPLAINT_ESCALATION | Why: Service friction is the clearest risk signal here. Complaint escalation fits because complaints_30d=0 and unresolved_complaints=0 suggest the issue is unresolved or operationally related rather than product-specific.

Request:

```json
{
  "customer_id": "C14830",
  "customer_name": "Waida Chanda",
  "prediction_date": "2026-05-01",
  "snapshot_date": "2026-05-01",
  "target_month": "2026-06-01",
  "profile": {
    "tenure_months": 140,
    "customer_segment": "farmer",
    "income_regularity": "seasonal",
    "products_count": 3,
    "has_credit_card": 0,
    "has_loan": 1
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 13,
      "balance_change_30d": -25.4414,
      "transaction_change_30d": -21.4852,
      "card_spend_change_30d": -5.3527,
      "app_login_change_30d": -15.3665,
      "salary_missing_days": null,
      "external_transfer_change_30d": 6.0607,
      "upi_share_of_spend": 0.2327,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 0,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 0.0,
      "emi_bounce_30d": 1
    },
    {
      "snapshot_date": "2026-02-01",
      "days_since_last_transaction": 16,
      "balance_change_30d": -35.6085,
      "transaction_change_30d": -31.6568,
      "card_spend_change_30d": -42.0978,
      "app_login_change_30d": -40.734,
      "salary_missing_days": null,
      "external_transfer_change_30d": 82.3013,
      "upi_share_of_spend": 0.2565,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 27.6142,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-03-01",
      "days_since_last_transaction": 18,
      "balance_change_30d": -35.0039,
      "transaction_change_30d": -33.8138,
      "card_spend_change_30d": -16.219,
      "app_login_change_30d": -49.5998,
      "salary_missing_days": null,
      "external_transfer_change_30d": 57.8801,
      "upi_share_of_spend": 0.302,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 1,
      "complaints_30d": 2,
      "unresolved_complaints": 1,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 27.8879,
      "emi_bounce_30d": 1
    },
    {
      "snapshot_date": "2026-04-01",
      "days_since_last_transaction": 13,
      "balance_change_30d": -50.236,
      "transaction_change_30d": -20.9024,
      "card_spend_change_30d": -24.2314,
      "app_login_change_30d": -37.3287,
      "salary_missing_days": null,
      "external_transfer_change_30d": 31.5922,
      "upi_share_of_spend": 0.3284,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 1,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 8.9828,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-05-01",
      "days_since_last_transaction": 20,
      "balance_change_30d": -38.7287,
      "transaction_change_30d": -20.153,
      "card_spend_change_30d": -47.5748,
      "app_login_change_30d": -21.7931,
      "salary_missing_days": null,
      "external_transfer_change_30d": 53.1969,
      "upi_share_of_spend": 0.2838,
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
    "tenure_months": 140,
    "customer_segment": "farmer",
    "income_regularity": "seasonal",
    "products_count": 3,
    "has_credit_card": 0,
    "has_loan": 1,
    "days_since_last_transaction": 20,
    "balance_change_30d": -38.7287,
    "transaction_change_30d": -20.153,
    "card_spend_change_30d": -47.5748,
    "app_login_change_30d": -21.7931,
    "salary_missing_days": null,
    "external_transfer_change_30d": 53.1969,
    "upi_share_of_spend": 0.2838,
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
      "tenure_months": 140,
      "age": 35,
      "customer_yearly_value": 32960.0223,
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
    "served_at": "2026-08-31T01:07:42",
    "elapsed_ms": 2639.79,
    "timings_ms": {
      "model1": 193.87,
      "model2": 2445.79
    },
    "customer_id": "C14830",
    "customer_name": "Waida Chanda",
    "snapshot_date": "2026-05-01"
  },
  "model1": {
    "churn_probability": 24.25,
    "raw_churn_probability": 77.55,
    "probability_mode": "sigmoid",
    "risk_score": 71.59,
    "churn_prediction": "Yes",
    "risk_level": "Medium",
    "top_risk_factors": [
      {
        "factor": "latest_days_since_last_transaction",
        "value": 20,
        "message": "Customer has gone longer without transacting.",
        "contribution": 0.6609362959861755
      },
      {
        "factor": "latest_balance_change_30d",
        "value": -38.7287,
        "message": "Balance has been falling across recent months.",
        "contribution": 0.23861749470233917
      },
      {
        "factor": "latest_card_spend_change_30d",
        "value": -47.5748,
        "message": "Card spending has been falling across recent months.",
        "contribution": 0.1583106964826584
      },
      {
        "factor": "days_since_last_transaction_trend_6m",
        "value": 1.0999999999999979,
        "message": "Customer has gone longer without transacting.",
        "contribution": 0.1384669691324234
      },
      {
        "factor": "latest_transaction_change_30d",
        "value": -20.153,
        "message": "Transaction activity has been falling across recent months.",
        "contribution": 0.11163725703954697
      }
    ]
  },
  "model2_input": {
    "customer_context": {
      "age": 35,
      "tenure_months": 140,
      "customer_segment": "farmer",
      "income_regularity": "seasonal",
      "customer_yearly_value": 32960.0223,
      "products_count": 3,
      "has_credit_card": 0,
      "has_loan": 1
    },
    "behavior": {
      "days_since_last_transaction": 20,
      "balance_change_30d": -38.7287,
      "transaction_change_30d": -20.153,
      "card_spend_change_30d": -47.5748,
      "app_login_change_30d": -21.7931,
      "salary_missing_days": null,
      "external_transfer_change_30d": 53.1969,
      "upi_share_of_spend": 0.2838,
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
      "churn_probability": 0.2425,
      "churn_prediction": "Yes",
      "risk_level": "Medium",
      "top_risk_factors": [
        {
          "factor": "days_since_last_transaction",
          "value": 20
        },
        {
          "factor": "balance_change_30d",
          "value": -38.7287
        },
        {
          "factor": "card_spend_change_30d",
          "value": -47.5748
        },
        {
          "factor": "days_since_last_transaction_trend_6m",
          "value": 1.0999999999999979
        },
        {
          "factor": "transaction_change_30d",
          "value": -20.153
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
    "case_id": "C14830"
  },
  "model2": {
    "case_id": "C14830",
    "ok": true,
    "prediction": {
      "evidence": [
        "complaints_30d=0",
        "unresolved_complaints=0",
        "failed_transactions_30d=1"
      ],
      "primary_reason": "SERVICE_DISSATISFACTION",
      "reasoning_summary": "Service friction is the clearest risk signal here. Complaint escalation fits because complaints_30d=0 and unresolved_complaints=0 suggest the issue is unresolved or operationally related rather than product-specific.",
      "recommended_action": "COMPLAINT_ESCALATION",
      "secondary_reasons": [
        "UNKNOWN"
      ],
      "urgency": "MEDIUM"
    },
    "raw_text": "{\"evidence\":[\"complaints_30d=0\",\"unresolved_complaints=0\",\"failed_transactions_30d=1\"],\"primary_reason\":\"SERVICE_DISSATISFACTION\",\"reasoning_summary\":\"Service friction is the clearest risk signal here. Complaint escalation fits because complaints_30d=0 and unresolved_complaints=0 suggest the issue is unresolved or operationally related rather than product-specific.\",\"recommended_action\":\"COMPLAINT_ESCALATION\",\"secondary_reasons\":[\"UNKNOWN\"],\"urgency\":\"MEDIUM\"}",
    "error": null,
    "latency_s": 2.4456,
    "simple_output": "Reason: SERVICE_DISSATISFACTION | Urgency: MEDIUM | Action: COMPLAINT_ESCALATION | Why: Service friction is the clearest risk signal here. Complaint escalation fits because complaints_30d=0 and unresolved_complaints=0 suggest the issue is unresolved or operationally related rather than product-specific."
  }
}
```

### Isaiah Yohannan (`C16863`)

- OK: `False`
- Shape errors: `["model2 returned ok=false: recommended_action: 'COMPLAINT_ESCALATION' not in eligible_actions ['MONITOR', 'RE_ENGAGEMENT', 'PRODUCT_REVIEW', 'SERVICE_RECOVERY']", 'model2.prediction is missing or not an object']`
- Simple output: Prediction failed: recommended_action: 'COMPLAINT_ESCALATION' not in eligible_actions ['MONITOR', 'RE_ENGAGEMENT', 'PRODUCT_REVIEW', 'SERVICE_RECOVERY']

Request:

```json
{
  "customer_id": "C16863",
  "customer_name": "Isaiah Yohannan",
  "prediction_date": "2026-06-01",
  "snapshot_date": "2026-06-01",
  "target_month": "2026-07-01",
  "profile": {
    "tenure_months": 94,
    "customer_segment": "business",
    "income_regularity": "irregular",
    "products_count": 2,
    "has_credit_card": 1,
    "has_loan": 0
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 2,
      "balance_change_30d": 11.9191,
      "transaction_change_30d": 21.2682,
      "card_spend_change_30d": -4.1708,
      "app_login_change_30d": 9.4276,
      "salary_missing_days": null,
      "external_transfer_change_30d": 32.1156,
      "upi_share_of_spend": 0.2031,
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
      "days_since_last_transaction": 5,
      "balance_change_30d": 12.8639,
      "transaction_change_30d": -4.8263,
      "card_spend_change_30d": 12.5032,
      "app_login_change_30d": -4.2788,
      "salary_missing_days": null,
      "external_transfer_change_30d": -19.1492,
      "upi_share_of_spend": 0.2765,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 2,
      "unresolved_complaints": 1,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 25.6364,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-03-01",
      "days_since_last_transaction": 4,
      "balance_change_30d": 3.7278,
      "transaction_change_30d": 1.7673,
      "card_spend_change_30d": 13.387,
      "app_login_change_30d": 5.7172,
      "salary_missing_days": null,
      "external_transfer_change_30d": 21.009,
      "upi_share_of_spend": 0.3511,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 2,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 14.4024,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-04-01",
      "days_since_last_transaction": 5,
      "balance_change_30d": 3.6645,
      "transaction_change_30d": 41.9621,
      "card_spend_change_30d": 11.7819,
      "app_login_change_30d": 37.7652,
      "salary_missing_days": null,
      "external_transfer_change_30d": -18.2873,
      "upi_share_of_spend": 0.2682,
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
      "balance_change_30d": 17.6663,
      "transaction_change_30d": -2.0867,
      "card_spend_change_30d": 40.7082,
      "app_login_change_30d": 0.4918,
      "salary_missing_days": null,
      "external_transfer_change_30d": 20.6957,
      "upi_share_of_spend": 0.3005,
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
      "balance_change_30d": 6.4484,
      "transaction_change_30d": 13.0838,
      "card_spend_change_30d": 31.7862,
      "app_login_change_30d": 3.9013,
      "salary_missing_days": null,
      "external_transfer_change_30d": -21.94,
      "upi_share_of_spend": 0.2753,
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
    "tenure_months": 94,
    "customer_segment": "business",
    "income_regularity": "irregular",
    "products_count": 2,
    "has_credit_card": 1,
    "has_loan": 0,
    "days_since_last_transaction": 3,
    "balance_change_30d": 6.4484,
    "transaction_change_30d": 13.0838,
    "card_spend_change_30d": 31.7862,
    "app_login_change_30d": 3.9013,
    "salary_missing_days": null,
    "external_transfer_change_30d": -21.94,
    "upi_share_of_spend": 0.2753,
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
      "tenure_months": 94,
      "age": 58,
      "customer_yearly_value": 84627.8968,
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
    "served_at": "2026-08-31T01:07:47",
    "elapsed_ms": 5245.21,
    "timings_ms": {
      "model1": 259.3,
      "model2": 4985.7
    },
    "customer_id": "C16863",
    "customer_name": "Isaiah Yohannan",
    "snapshot_date": "2026-06-01"
  },
  "model1": {
    "churn_probability": 2.5,
    "raw_churn_probability": 23.33,
    "probability_mode": "sigmoid",
    "risk_score": 7.5,
    "churn_prediction": "No",
    "risk_level": "Low",
    "top_risk_factors": [
      {
        "factor": "sum_fd_maturing_in_30d_3m",
        "value": 1.0,
        "message": "Customer has a fixed deposit maturing soon.",
        "contribution": 0.07248955219984055
      },
      {
        "factor": "card_spend_change_30d_trend_6m",
        "value": 7.508425714285712,
        "message": "This signal increased churn risk.",
        "contribution": 0.041764844208955765
      },
      {
        "factor": "latest_vs_avg_card_spend_change_30d_available_history",
        "value": 14.120250000000002,
        "message": "This signal increased churn risk.",
        "contribution": 0.026998495683073997
      },
      {
        "factor": "avg_upi_share_of_spend_6m",
        "value": 0.2791166666666667,
        "message": "A larger share of spending is happening through UPI.",
        "contribution": 0.0203054528683424
      },
      {
        "factor": "avg_transaction_change_30d_6m",
        "value": 11.861400000000001,
        "message": "This signal increased churn risk.",
        "contribution": 0.019139539450407028
      }
    ]
  },
  "model2_input": {
    "customer_context": {
      "age": 58,
      "tenure_months": 94,
      "customer_segment": "business",
      "income_regularity": "irregular",
      "customer_yearly_value": 84627.8968,
      "products_count": 2,
      "has_credit_card": 1,
      "has_loan": 0
    },
    "behavior": {
      "days_since_last_transaction": 3,
      "balance_change_30d": 6.4484,
      "transaction_change_30d": 13.0838,
      "card_spend_change_30d": 31.7862,
      "app_login_change_30d": 3.9013,
      "salary_missing_days": null,
      "external_transfer_change_30d": -21.94,
      "upi_share_of_spend": 0.2753,
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
      "churn_probability": 0.025,
      "churn_prediction": "No",
      "risk_level": "Low",
      "top_risk_factors": [
        {
          "factor": "sum_fd_maturing_in_30d_3m",
          "value": 1.0
        },
        {
          "factor": "card_spend_change_30d_trend_6m",
          "value": 7.508425714285712
        },
        {
          "factor": "vs_avg_card_spend_change_30d_available_history",
          "value": 14.120250000000002
        },
        {
          "factor": "avg_upi_share_of_spend_6m",
          "value": 0.2791166666666667
        },
        {
          "factor": "avg_transaction_change_30d_6m",
          "value": 11.861400000000001
        }
      ]
    },
    "eligible_actions": [
      "MONITOR",
      "RE_ENGAGEMENT",
      "PRODUCT_REVIEW",
      "SERVICE_RECOVERY"
    ],
    "case_id": "C16863"
  },
  "model2": {
    "case_id": "C16863",
    "ok": false,
    "prediction": null,
    "raw_text": "{\"evidence\":[\"complaints_30d=0\",\"failed_transactions_30d=1\"],\"primary_reason\":\"SERVICE_DISSATISFACTION\",\"reasoning_summary\":\"Service friction is the clearest risk signal here. Complaint escalation fits because complaints_30d=0 and failed_transactions_30d=1 indicate a service issue with unresolved consequences.\",\"recommended_action\":\"COMPLAINT_ESCALATION\",\"secondary_reasons\":[\"UNKNOWN\"],\"urgency\":\"MEDIUM\"}",
    "error": "recommended_action: 'COMPLAINT_ESCALATION' not in eligible_actions ['MONITOR', 'RE_ENGAGEMENT', 'PRODUCT_REVIEW', 'SERVICE_RECOVERY']",
    "latency_s": 4.9854,
    "simple_output": "Prediction failed: recommended_action: 'COMPLAINT_ESCALATION' not in eligible_actions ['MONITOR', 'RE_ENGAGEMENT', 'PRODUCT_REVIEW', 'SERVICE_RECOVERY']"
  }
}
```

### Charvi Dara (`C17253`)

- OK: `False`
- Shape errors: `["model2 returned ok=false: recommended_action: 'COMPLAINT_ESCALATION' not in eligible_actions ['MONITOR', 'RE_ENGAGEMENT', 'PRODUCT_REVIEW', 'SERVICE_RECOVERY']", 'model2.prediction is missing or not an object']`
- Simple output: Prediction failed: recommended_action: 'COMPLAINT_ESCALATION' not in eligible_actions ['MONITOR', 'RE_ENGAGEMENT', 'PRODUCT_REVIEW', 'SERVICE_RECOVERY']

Request:

```json
{
  "customer_id": "C17253",
  "customer_name": "Charvi Dara",
  "prediction_date": "2026-06-01",
  "snapshot_date": "2026-06-01",
  "target_month": "2026-07-01",
  "profile": {
    "tenure_months": 80,
    "customer_segment": "farmer",
    "income_regularity": "seasonal",
    "products_count": 2,
    "has_credit_card": 0,
    "has_loan": 1
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 8,
      "balance_change_30d": -14.9728,
      "transaction_change_30d": 10.6799,
      "card_spend_change_30d": 19.1402,
      "app_login_change_30d": 27.847,
      "salary_missing_days": null,
      "external_transfer_change_30d": -26.9863,
      "upi_share_of_spend": 0.022,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 3,
      "complaints_30d": 0,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 0.0,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-02-01",
      "days_since_last_transaction": 15,
      "balance_change_30d": -20.1194,
      "transaction_change_30d": -0.4033,
      "card_spend_change_30d": -39.8278,
      "app_login_change_30d": 1.7772,
      "salary_missing_days": null,
      "external_transfer_change_30d": 32.5629,
      "upi_share_of_spend": 0.1966,
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
      "balance_change_30d": 11.332,
      "transaction_change_30d": 6.9794,
      "card_spend_change_30d": 31.5437,
      "app_login_change_30d": 11.1667,
      "salary_missing_days": null,
      "external_transfer_change_30d": 17.2845,
      "upi_share_of_spend": 0.023,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 1.0,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-04-01",
      "days_since_last_transaction": 8,
      "balance_change_30d": 5.1636,
      "transaction_change_30d": 31.5824,
      "card_spend_change_30d": 39.4739,
      "app_login_change_30d": 8.5442,
      "salary_missing_days": null,
      "external_transfer_change_30d": -15.9911,
      "upi_share_of_spend": 0.0323,
      "fd_maturing_in_30d": 1,
      "products_dropped_90d": 0,
      "complaints_30d": 2,
      "unresolved_complaints": 2,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 53.8278,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-05-01",
      "days_since_last_transaction": 8,
      "balance_change_30d": 38.4306,
      "transaction_change_30d": 21.983,
      "card_spend_change_30d": 28.483,
      "app_login_change_30d": 46.1305,
      "salary_missing_days": null,
      "external_transfer_change_30d": -25.3427,
      "upi_share_of_spend": 0.1163,
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
      "balance_change_30d": 23.4612,
      "transaction_change_30d": 38.1267,
      "card_spend_change_30d": 34.4678,
      "app_login_change_30d": 32.0993,
      "salary_missing_days": null,
      "external_transfer_change_30d": -31.704,
      "upi_share_of_spend": 0.0,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 2,
      "avg_resolution_time_hrs": 27.8839,
      "emi_bounce_30d": 0
    }
  ],
  "customer": {
    "tenure_months": 80,
    "customer_segment": "farmer",
    "income_regularity": "seasonal",
    "products_count": 2,
    "has_credit_card": 0,
    "has_loan": 1,
    "days_since_last_transaction": 0,
    "balance_change_30d": 23.4612,
    "transaction_change_30d": 38.1267,
    "card_spend_change_30d": 34.4678,
    "app_login_change_30d": 32.0993,
    "salary_missing_days": null,
    "external_transfer_change_30d": -31.704,
    "upi_share_of_spend": 0.0,
    "fd_maturing_in_30d": 0,
    "products_dropped_90d": 0,
    "complaints_30d": 1,
    "unresolved_complaints": 0,
    "failed_transactions_30d": 2,
    "avg_resolution_time_hrs": 27.8839,
    "emi_bounce_30d": 0
  },
  "extra_context": {
    "customer_profile": {
      "segment": "farmer",
      "income_regularity": "seasonal",
      "tenure_months": 80,
      "age": 33,
      "customer_yearly_value": 16991.2165,
      "products_count": 2,
      "has_credit_card": 0,
      "has_loan": 1,
      "value_tier": "low"
    },
    "recent_complaint_text": "Fertiliser shop payment failed at last moment. Had to borrow cash."
  }
}
```

Response:

```json
{
  "meta": {
    "endpoint": "/predict/both",
    "served_at": "2026-08-31T01:07:53",
    "elapsed_ms": 5259.13,
    "timings_ms": {
      "model1": 152.29,
      "model2": 5106.69
    },
    "customer_id": "C17253",
    "customer_name": "Charvi Dara",
    "snapshot_date": "2026-06-01"
  },
  "model1": {
    "churn_probability": 3.84,
    "raw_churn_probability": 32.86,
    "probability_mode": "sigmoid",
    "risk_score": 11.53,
    "churn_prediction": "No",
    "risk_level": "Low",
    "top_risk_factors": [
      {
        "factor": "max_avg_resolution_time_hrs_3m",
        "value": 53.8278,
        "message": "Recent complaints took longer to resolve.",
        "contribution": 0.3293083906173706
      },
      {
        "factor": "latest_upi_share_of_spend",
        "value": 0.0,
        "message": "This signal increased churn risk.",
        "contribution": 0.10624685883522034
      },
      {
        "factor": "latest_avg_resolution_time_hrs",
        "value": 27.8839,
        "message": "Recent complaints took longer to resolve.",
        "contribution": 0.10457522422075272
      },
      {
        "factor": "sum_fd_maturing_in_30d_3m",
        "value": 1.0,
        "message": "Customer has a fixed deposit maturing soon.",
        "contribution": 0.0945553109049797
      },
      {
        "factor": "avg_transaction_change_30d_6m",
        "value": 18.158016666666665,
        "message": "This signal increased churn risk.",
        "contribution": 0.03934389725327492
      }
    ]
  },
  "model2_input": {
    "customer_context": {
      "age": 33,
      "tenure_months": 80,
      "customer_segment": "farmer",
      "income_regularity": "seasonal",
      "customer_yearly_value": 16991.2165,
      "products_count": 2,
      "has_credit_card": 0,
      "has_loan": 1
    },
    "behavior": {
      "days_since_last_transaction": 0,
      "balance_change_30d": 23.4612,
      "transaction_change_30d": 38.1267,
      "card_spend_change_30d": 34.4678,
      "app_login_change_30d": 32.0993,
      "salary_missing_days": null,
      "external_transfer_change_30d": -31.704,
      "upi_share_of_spend": 0.0,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "emi_bounce_30d": 0
    },
    "service_evidence": {
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 2,
      "avg_resolution_time_hrs": 27.8839,
      "complaint_text": "Fertiliser shop payment failed at last moment. Had to borrow cash."
    },
    "model1": {
      "churn_probability": 0.0384,
      "churn_prediction": "No",
      "risk_level": "Low",
      "top_risk_factors": [
        {
          "factor": "max_avg_resolution_time_hrs_3m",
          "value": 53.8278
        },
        {
          "factor": "upi_share_of_spend",
          "value": 0.0
        },
        {
          "factor": "avg_resolution_time_hrs",
          "value": 27.8839
        },
        {
          "factor": "sum_fd_maturing_in_30d_3m",
          "value": 1.0
        },
        {
          "factor": "avg_transaction_change_30d_6m",
          "value": 18.158016666666665
        }
      ]
    },
    "eligible_actions": [
      "MONITOR",
      "RE_ENGAGEMENT",
      "PRODUCT_REVIEW",
      "SERVICE_RECOVERY"
    ],
    "case_id": "C17253"
  },
  "model2": {
    "case_id": "C17253",
    "ok": false,
    "prediction": null,
    "raw_text": "{\"evidence\":[\"complaints_30d=1\",\"failed_transactions_30d=2\",\"avg_resolution_time_hrs=27.9\",\"complaint_text describes a recent service issue\"],\"primary_reason\":\"SERVICE_DISSATISFACTION\",\"reasoning_summary\":\"Service friction is the clearest risk signal here. Complaint escalation fits because complaints_30d=1 and failed_transactions_30d=2 indicate the issue is unresolved or operationally serious.\",\"recommended_action\":\"COMPLAINT_ESCALATION\",\"secondary_reasons\":[\"UNKNOWN\"],\"urgency\":\"MEDIUM\"}",
    "error": "recommended_action: 'COMPLAINT_ESCALATION' not in eligible_actions ['MONITOR', 'RE_ENGAGEMENT', 'PRODUCT_REVIEW', 'SERVICE_RECOVERY']",
    "latency_s": 5.1064,
    "simple_output": "Prediction failed: recommended_action: 'COMPLAINT_ESCALATION' not in eligible_actions ['MONITOR', 'RE_ENGAGEMENT', 'PRODUCT_REVIEW', 'SERVICE_RECOVERY']"
  }
}
```

### Urvashi Agate (`C17317`)

- OK: `True`
- Shape errors: `[]`
- Simple output: Reason: SERVICE_DISSATISFACTION | Urgency: HIGH | Action: COMPLAINT_ESCALATION | Why: Service friction is the clearest risk signal here. Complaint escalation fits because complaints_30d=2 and unresolved_complaints=1 indicate the issue is unresolved or operationally serious.

Request:

```json
{
  "customer_id": "C17317",
  "customer_name": "Urvashi Agate",
  "prediction_date": "2026-06-01",
  "snapshot_date": "2026-06-01",
  "target_month": "2026-07-01",
  "profile": {
    "tenure_months": 25,
    "customer_segment": "vendor",
    "income_regularity": "irregular",
    "products_count": 2,
    "has_credit_card": 0,
    "has_loan": 0
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 9,
      "balance_change_30d": -9.9263,
      "transaction_change_30d": 6.11,
      "card_spend_change_30d": 21.1598,
      "app_login_change_30d": 8.4481,
      "salary_missing_days": null,
      "external_transfer_change_30d": -0.8465,
      "upi_share_of_spend": 0.4032,
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
      "balance_change_30d": 30.8525,
      "transaction_change_30d": 19.1567,
      "card_spend_change_30d": -15.0005,
      "app_login_change_30d": -12.3779,
      "salary_missing_days": null,
      "external_transfer_change_30d": 19.378,
      "upi_share_of_spend": 0.5192,
      "fd_maturing_in_30d": 1,
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
      "balance_change_30d": -8.7409,
      "transaction_change_30d": -25.4386,
      "card_spend_change_30d": -8.971,
      "app_login_change_30d": -40.2195,
      "salary_missing_days": null,
      "external_transfer_change_30d": 24.5895,
      "upi_share_of_spend": 0.54,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 33.5163,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-04-01",
      "days_since_last_transaction": 12,
      "balance_change_30d": 2.157,
      "transaction_change_30d": 10.5741,
      "card_spend_change_30d": 8.4561,
      "app_login_change_30d": -7.1772,
      "salary_missing_days": null,
      "external_transfer_change_30d": 64.5678,
      "upi_share_of_spend": 0.5699,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 1,
      "failed_transactions_30d": 4,
      "avg_resolution_time_hrs": 32.5054,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-05-01",
      "days_since_last_transaction": 16,
      "balance_change_30d": -15.4229,
      "transaction_change_30d": -54.2714,
      "card_spend_change_30d": -21.5196,
      "app_login_change_30d": -3.4371,
      "salary_missing_days": null,
      "external_transfer_change_30d": 54.3398,
      "upi_share_of_spend": 0.589,
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
      "days_since_last_transaction": 26,
      "balance_change_30d": -45.8629,
      "transaction_change_30d": -13.0497,
      "card_spend_change_30d": -54.5939,
      "app_login_change_30d": -44.8278,
      "salary_missing_days": null,
      "external_transfer_change_30d": 100.2574,
      "upi_share_of_spend": 0.6923,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 3,
      "complaints_30d": 2,
      "unresolved_complaints": 1,
      "failed_transactions_30d": 6,
      "avg_resolution_time_hrs": 53.9471,
      "emi_bounce_30d": 0
    }
  ],
  "customer": {
    "tenure_months": 25,
    "customer_segment": "vendor",
    "income_regularity": "irregular",
    "products_count": 2,
    "has_credit_card": 0,
    "has_loan": 0,
    "days_since_last_transaction": 26,
    "balance_change_30d": -45.8629,
    "transaction_change_30d": -13.0497,
    "card_spend_change_30d": -54.5939,
    "app_login_change_30d": -44.8278,
    "salary_missing_days": null,
    "external_transfer_change_30d": 100.2574,
    "upi_share_of_spend": 0.6923,
    "fd_maturing_in_30d": 0,
    "products_dropped_90d": 3,
    "complaints_30d": 2,
    "unresolved_complaints": 1,
    "failed_transactions_30d": 6,
    "avg_resolution_time_hrs": 53.9471,
    "emi_bounce_30d": 0
  },
  "extra_context": {
    "customer_profile": {
      "segment": "vendor",
      "income_regularity": "irregular",
      "tenure_months": 25,
      "age": 37,
      "customer_yearly_value": 6788.6261,
      "products_count": 2,
      "has_credit_card": 0,
      "has_loan": 0,
      "value_tier": "low"
    },
    "recent_complaint_text": "Requesting a fee free account variant, my income is seasonal."
  }
}
```

Response:

```json
{
  "meta": {
    "endpoint": "/predict/both",
    "served_at": "2026-08-31T01:07:55",
    "elapsed_ms": 2724.36,
    "timings_ms": {
      "model1": 150.05,
      "model2": 2574.19
    },
    "customer_id": "C17317",
    "customer_name": "Urvashi Agate",
    "snapshot_date": "2026-06-01"
  },
  "model1": {
    "churn_probability": 39.84,
    "raw_churn_probability": 93.16,
    "probability_mode": "sigmoid",
    "risk_score": 77.44,
    "churn_prediction": "Yes",
    "risk_level": "High",
    "top_risk_factors": [
      {
        "factor": "latest_days_since_last_transaction",
        "value": 26,
        "message": "Customer has gone longer without transacting.",
        "contribution": 0.45424094796180725
      },
      {
        "factor": "sum_failed_transactions_30d_3m",
        "value": 10.0,
        "message": "Customer has recent failed transactions.",
        "contribution": 0.25163426995277405
      },
      {
        "factor": "max_avg_resolution_time_hrs_3m",
        "value": 53.9471,
        "message": "Recent complaints took longer to resolve.",
        "contribution": 0.23646245896816254
      },
      {
        "factor": "latest_balance_change_30d",
        "value": -45.8629,
        "message": "Balance has been falling across recent months.",
        "contribution": 0.1819092482328415
      },
      {
        "factor": "latest_vs_avg_upi_share_of_spend_available_history",
        "value": 0.14003333333333334,
        "message": "A larger share of spending is happening through UPI.",
        "contribution": 0.17982511222362518
      }
    ]
  },
  "model2_input": {
    "customer_context": {
      "age": 37,
      "tenure_months": 25,
      "customer_segment": "vendor",
      "income_regularity": "irregular",
      "customer_yearly_value": 6788.6261,
      "products_count": 2,
      "has_credit_card": 0,
      "has_loan": 0
    },
    "behavior": {
      "days_since_last_transaction": 26,
      "balance_change_30d": -45.8629,
      "transaction_change_30d": -13.0497,
      "card_spend_change_30d": -54.5939,
      "app_login_change_30d": -44.8278,
      "salary_missing_days": null,
      "external_transfer_change_30d": 100.2574,
      "upi_share_of_spend": 0.6923,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 3,
      "emi_bounce_30d": 0
    },
    "service_evidence": {
      "complaints_30d": 2,
      "unresolved_complaints": 1,
      "failed_transactions_30d": 6,
      "avg_resolution_time_hrs": 53.9471,
      "complaint_text": "Requesting a fee free account variant, my income is seasonal."
    },
    "model1": {
      "churn_probability": 0.3984,
      "churn_prediction": "Yes",
      "risk_level": "High",
      "top_risk_factors": [
        {
          "factor": "days_since_last_transaction",
          "value": 26
        },
        {
          "factor": "sum_failed_transactions_30d_3m",
          "value": 10.0
        },
        {
          "factor": "max_avg_resolution_time_hrs_3m",
          "value": 53.9471
        },
        {
          "factor": "balance_change_30d",
          "value": -45.8629
        },
        {
          "factor": "vs_avg_upi_share_of_spend_available_history",
          "value": 0.14003333333333334
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
    "case_id": "C17317"
  },
  "model2": {
    "case_id": "C17317",
    "ok": true,
    "prediction": {
      "evidence": [
        "complaints_30d=2",
        "unresolved_complaints=1",
        "avg_resolution_time_hrs=54.0",
        "complaint_text describes a recent service issue"
      ],
      "primary_reason": "SERVICE_DISSATISFACTION",
      "reasoning_summary": "Service friction is the clearest risk signal here. Complaint escalation fits because complaints_30d=2 and unresolved_complaints=1 indicate the issue is unresolved or operationally serious.",
      "recommended_action": "COMPLAINT_ESCALATION",
      "secondary_reasons": [
        "UNKNOWN"
      ],
      "urgency": "HIGH"
    },
    "raw_text": "{\n\"evidence\":[\"complaints_30d=2\",\"unresolved_complaints=1\",\"avg_resolution_time_hrs=54.0\",\"complaint_text describes a recent service issue\"],\"primary_reason\":\"SERVICE_DISSATISFACTION\",\"reasoning_summary\":\"Service friction is the clearest risk signal here. Complaint escalation fits because complaints_30d=2 and unresolved_complaints=1 indicate the issue is unresolved or operationally serious.\",\"recommended_action\":\"COMPLAINT_ESCALATION\",\"secondary_reasons\":[\"UNKNOWN\"],\"urgency\":\"HIGH\"}",
    "error": null,
    "latency_s": 2.5738,
    "simple_output": "Reason: SERVICE_DISSATISFACTION | Urgency: HIGH | Action: COMPLAINT_ESCALATION | Why: Service friction is the clearest risk signal here. Complaint escalation fits because complaints_30d=2 and unresolved_complaints=1 indicate the issue is unresolved or operationally serious."
  }
}
```

### Rayaan Trivedi (`C17474`)

- OK: `False`
- Shape errors: `["model2 returned ok=false: recommended_action: 'COMPLAINT_ESCALATION' not in eligible_actions ['MONITOR', 'RE_ENGAGEMENT', 'PRODUCT_REVIEW', 'SERVICE_RECOVERY', 'FINANCIAL_GUIDANCE', 'RM_CALLBACK']", 'model2.prediction is missing or not an object']`
- Simple output: Prediction failed: recommended_action: 'COMPLAINT_ESCALATION' not in eligible_actions ['MONITOR', 'RE_ENGAGEMENT', 'PRODUCT_REVIEW', 'SERVICE_RECOVERY', 'FINANCIAL_GUIDANCE', 'RM_CALLBACK']

Request:

```json
{
  "customer_id": "C17474",
  "customer_name": "Rayaan Trivedi",
  "prediction_date": "2026-01-01",
  "snapshot_date": "2026-01-01",
  "target_month": "2026-02-01",
  "profile": {
    "tenure_months": 132,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 1,
    "has_credit_card": 0,
    "has_loan": 0
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 7,
      "balance_change_30d": -0.0128,
      "transaction_change_30d": 11.9044,
      "card_spend_change_30d": 22.1056,
      "app_login_change_30d": -13.9849,
      "salary_missing_days": 3.0,
      "external_transfer_change_30d": 38.2641,
      "upi_share_of_spend": 0.3409,
      "fd_maturing_in_30d": 1,
      "products_dropped_90d": 0,
      "complaints_30d": 0,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 3,
      "avg_resolution_time_hrs": 0.0,
      "emi_bounce_30d": 0
    }
  ],
  "customer": {
    "tenure_months": 132,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 1,
    "has_credit_card": 0,
    "has_loan": 0,
    "days_since_last_transaction": 7,
    "balance_change_30d": -0.0128,
    "transaction_change_30d": 11.9044,
    "card_spend_change_30d": 22.1056,
    "app_login_change_30d": -13.9849,
    "salary_missing_days": 3.0,
    "external_transfer_change_30d": 38.2641,
    "upi_share_of_spend": 0.3409,
    "fd_maturing_in_30d": 1,
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
      "tenure_months": 132,
      "age": 29,
      "customer_yearly_value": 23939.8804,
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
    "served_at": "2026-08-31T01:08:00",
    "elapsed_ms": 5069.17,
    "timings_ms": {
      "model1": 147.73,
      "model2": 4921.3
    },
    "customer_id": "C17474",
    "customer_name": "Rayaan Trivedi",
    "snapshot_date": "2026-01-01"
  },
  "model1": {
    "churn_probability": 6.16,
    "raw_churn_probability": 43.54,
    "probability_mode": "sigmoid",
    "risk_score": 18.49,
    "churn_prediction": "No",
    "risk_level": "Low",
    "top_risk_factors": [
      {
        "factor": "latest_salary_missing_days",
        "value": 3.0,
        "message": "Salary or pension was delayed recently.",
        "contribution": 0.20475047826766968
      },
      {
        "factor": "latest_fd_maturing_in_30d",
        "value": 1,
        "message": "Customer has a fixed deposit maturing soon.",
        "contribution": 0.18593673408031464
      },
      {
        "factor": "latest_failed_transactions_30d",
        "value": 3,
        "message": "Customer has recent failed transactions.",
        "contribution": 0.16675926744937897
      },
      {
        "factor": "sum_fd_maturing_in_30d_3m",
        "value": 1.0,
        "message": "Customer has a fixed deposit maturing soon.",
        "contribution": 0.08490154892206192
      },
      {
        "factor": "max_salary_missing_days_3m",
        "value": 3.0,
        "message": "Salary or pension was delayed recently.",
        "contribution": 0.022676914930343628
      }
    ]
  },
  "model2_input": {
    "customer_context": {
      "age": 29,
      "tenure_months": 132,
      "customer_segment": "salary",
      "income_regularity": "regular",
      "customer_yearly_value": 23939.8804,
      "products_count": 1,
      "has_credit_card": 0,
      "has_loan": 0
    },
    "behavior": {
      "days_since_last_transaction": 7,
      "balance_change_30d": -0.0128,
      "transaction_change_30d": 11.9044,
      "card_spend_change_30d": 22.1056,
      "app_login_change_30d": -13.9849,
      "salary_missing_days": 3,
      "external_transfer_change_30d": 38.2641,
      "upi_share_of_spend": 0.3409,
      "fd_maturing_in_30d": 1,
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
      "churn_probability": 0.0616,
      "churn_prediction": "No",
      "risk_level": "Low",
      "top_risk_factors": [
        {
          "factor": "salary_missing_days",
          "value": 3.0
        },
        {
          "factor": "fd_maturing_in_30d",
          "value": 1
        },
        {
          "factor": "failed_transactions_30d",
          "value": 3
        },
        {
          "factor": "sum_fd_maturing_in_30d_3m",
          "value": 1.0
        },
        {
          "factor": "max_salary_missing_days_3m",
          "value": 3.0
        }
      ]
    },
    "eligible_actions": [
      "MONITOR",
      "RE_ENGAGEMENT",
      "PRODUCT_REVIEW",
      "SERVICE_RECOVERY",
      "FINANCIAL_GUIDANCE",
      "RM_CALLBACK"
    ],
    "case_id": "C17474"
  },
  "model2": {
    "case_id": "C17474",
    "ok": false,
    "prediction": null,
    "raw_text": "{\"evidence\":[\"complaints_30d=0\",\"failed_transactions_30d=3\"],\"primary_reason\":\"SERVICE_DISSATISFACTION\",\"reasoning_summary\":\"Service friction is the clearest risk signal here. Complaint escalation fits because complaints_30d=0 and failed_transactions_30d=3 indicate the issue is unresolved or operationally serious.\",\"recommended_action\":\"COMPLAINT_ESCALATION\",\"secondary_reasons\":[\"UNKNOWN\"],\"urgency\":\"MEDIUM\"}",
    "error": "recommended_action: 'COMPLAINT_ESCALATION' not in eligible_actions ['MONITOR', 'RE_ENGAGEMENT', 'PRODUCT_REVIEW', 'SERVICE_RECOVERY', 'FINANCIAL_GUIDANCE', 'RM_CALLBACK']",
    "latency_s": 4.9208,
    "simple_output": "Prediction failed: recommended_action: 'COMPLAINT_ESCALATION' not in eligible_actions ['MONITOR', 'RE_ENGAGEMENT', 'PRODUCT_REVIEW', 'SERVICE_RECOVERY', 'FINANCIAL_GUIDANCE', 'RM_CALLBACK']"
  }
}
```

### Vritti Rai (`C17868`)

- OK: `False`
- Shape errors: `["model2 returned ok=false: recommended_action: 'COMPLAINT_ESCALATION' not in eligible_actions ['MONITOR', 'RE_ENGAGEMENT', 'PRODUCT_REVIEW', 'SERVICE_RECOVERY', 'FINANCIAL_GUIDANCE', 'RM_CALLBACK']", 'model2.prediction is missing or not an object']`
- Simple output: Prediction failed: recommended_action: 'COMPLAINT_ESCALATION' not in eligible_actions ['MONITOR', 'RE_ENGAGEMENT', 'PRODUCT_REVIEW', 'SERVICE_RECOVERY', 'FINANCIAL_GUIDANCE', 'RM_CALLBACK']

Request:

```json
{
  "customer_id": "C17868",
  "customer_name": "Vritti Rai",
  "prediction_date": "2026-06-01",
  "snapshot_date": "2026-06-01",
  "target_month": "2026-07-01",
  "profile": {
    "tenure_months": 162,
    "customer_segment": "pension",
    "income_regularity": "regular",
    "products_count": 2,
    "has_credit_card": 0,
    "has_loan": 0
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 13,
      "balance_change_30d": 5.4654,
      "transaction_change_30d": 7.4287,
      "card_spend_change_30d": 7.6783,
      "app_login_change_30d": 0.2957,
      "salary_missing_days": 2.0,
      "external_transfer_change_30d": 15.2168,
      "upi_share_of_spend": 0.2926,
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
      "balance_change_30d": -12.2462,
      "transaction_change_30d": -13.1047,
      "card_spend_change_30d": -15.6971,
      "app_login_change_30d": -6.4978,
      "salary_missing_days": 1.0,
      "external_transfer_change_30d": 25.5729,
      "upi_share_of_spend": 0.3958,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 23.1542,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-03-01",
      "days_since_last_transaction": 9,
      "balance_change_30d": 2.3679,
      "transaction_change_30d": -14.4183,
      "card_spend_change_30d": -8.7037,
      "app_login_change_30d": -20.0468,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": 13.7491,
      "upi_share_of_spend": 0.2999,
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
      "balance_change_30d": -16.2746,
      "transaction_change_30d": -6.2787,
      "card_spend_change_30d": 1.7193,
      "app_login_change_30d": -20.3007,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": 6.2227,
      "upi_share_of_spend": 0.2576,
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
      "balance_change_30d": -3.3719,
      "transaction_change_30d": 11.6043,
      "card_spend_change_30d": 11.8694,
      "app_login_change_30d": 19.9476,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -17.5573,
      "upi_share_of_spend": 0.2286,
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
      "balance_change_30d": -5.5377,
      "transaction_change_30d": -0.7943,
      "card_spend_change_30d": -2.2595,
      "app_login_change_30d": 15.7036,
      "salary_missing_days": 1.0,
      "external_transfer_change_30d": -5.9072,
      "upi_share_of_spend": 0.2761,
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
    "tenure_months": 162,
    "customer_segment": "pension",
    "income_regularity": "regular",
    "products_count": 2,
    "has_credit_card": 0,
    "has_loan": 0,
    "days_since_last_transaction": 5,
    "balance_change_30d": -5.5377,
    "transaction_change_30d": -0.7943,
    "card_spend_change_30d": -2.2595,
    "app_login_change_30d": 15.7036,
    "salary_missing_days": 1.0,
    "external_transfer_change_30d": -5.9072,
    "upi_share_of_spend": 0.2761,
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
      "tenure_months": 162,
      "age": 69,
      "customer_yearly_value": 22273.5966,
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
    "served_at": "2026-08-31T01:08:06",
    "elapsed_ms": 5051.22,
    "timings_ms": {
      "model1": 132.32,
      "model2": 4918.78
    },
    "customer_id": "C17868",
    "customer_name": "Vritti Rai",
    "snapshot_date": "2026-06-01"
  },
  "model1": {
    "churn_probability": 2.33,
    "raw_churn_probability": 21.79,
    "probability_mode": "sigmoid",
    "risk_score": 6.99,
    "churn_prediction": "No",
    "risk_level": "Low",
    "top_risk_factors": [
      {
        "factor": "latest_vs_avg_external_transfer_change_30d_available_history",
        "value": -12.123366666666666,
        "message": "This signal increased churn risk.",
        "contribution": 0.02444329299032688
      },
      {
        "factor": "avg_upi_share_of_spend_6m",
        "value": 0.2917666666666667,
        "message": "A larger share of spending is happening through UPI.",
        "contribution": 0.015339714474976063
      },
      {
        "factor": "latest_vs_avg_app_login_change_30d_available_history",
        "value": 17.52,
        "message": "This signal increased churn risk.",
        "contribution": 0.013139807619154453
      },
      {
        "factor": "avg_app_login_change_30d_6m",
        "value": -1.8163999999999996,
        "message": "App usage has been falling across recent months.",
        "contribution": 0.010604764334857464
      },
      {
        "factor": "max_salary_missing_days_6m",
        "value": 2.0,
        "message": "Salary or pension was delayed recently.",
        "contribution": 0.008639250881969929
      }
    ]
  },
  "model2_input": {
    "customer_context": {
      "age": 69,
      "tenure_months": 162,
      "customer_segment": "pension",
      "income_regularity": "regular",
      "customer_yearly_value": 22273.5966,
      "products_count": 2,
      "has_credit_card": 0,
      "has_loan": 0
    },
    "behavior": {
      "days_since_last_transaction": 5,
      "balance_change_30d": -5.5377,
      "transaction_change_30d": -0.7943,
      "card_spend_change_30d": -2.2595,
      "app_login_change_30d": 15.7036,
      "salary_missing_days": 1,
      "external_transfer_change_30d": -5.9072,
      "upi_share_of_spend": 0.2761,
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
      "churn_probability": 0.0233,
      "churn_prediction": "No",
      "risk_level": "Low",
      "top_risk_factors": [
        {
          "factor": "vs_avg_external_transfer_change_30d_available_history",
          "value": -12.123366666666666
        },
        {
          "factor": "avg_upi_share_of_spend_6m",
          "value": 0.2917666666666667
        },
        {
          "factor": "vs_avg_app_login_change_30d_available_history",
          "value": 17.52
        },
        {
          "factor": "avg_app_login_change_30d_6m",
          "value": -1.8163999999999996
        },
        {
          "factor": "max_salary_missing_days_6m",
          "value": 2.0
        }
      ]
    },
    "eligible_actions": [
      "MONITOR",
      "RE_ENGAGEMENT",
      "PRODUCT_REVIEW",
      "SERVICE_RECOVERY",
      "FINANCIAL_GUIDANCE",
      "RM_CALLBACK"
    ],
    "case_id": "C17868"
  },
  "model2": {
    "case_id": "C17868",
    "ok": false,
    "prediction": null,
    "raw_text": "{\"evidence\":[\"transaction_change_30d=-0.8\",\"complaints_30d=0\",\"failed_transactions_30d=1\"],\"primary_reason\":\"SERVICE_DISSATISFACTION\",\"reasoning_summary\":\"Service friction is the clearest risk signal here. Complaint escalation fits because complaints_30d=0 and failed_transactions_30d=1 suggest a service issue with unescalated complaints or a higher severity problem.\",\"recommended_action\":\"COMPLAINT_ESCALATION\",\"secondary_reasons\":[\"UNKNOWN\"],\"urgency\":\"MEDIUM\"}",
    "error": "recommended_action: 'COMPLAINT_ESCALATION' not in eligible_actions ['MONITOR', 'RE_ENGAGEMENT', 'PRODUCT_REVIEW', 'SERVICE_RECOVERY', 'FINANCIAL_GUIDANCE', 'RM_CALLBACK']",
    "latency_s": 4.9187,
    "simple_output": "Prediction failed: recommended_action: 'COMPLAINT_ESCALATION' not in eligible_actions ['MONITOR', 'RE_ENGAGEMENT', 'PRODUCT_REVIEW', 'SERVICE_RECOVERY', 'FINANCIAL_GUIDANCE', 'RM_CALLBACK']"
  }
}
```

### Shaurya Naidu (`C18598`)

- OK: `False`
- Shape errors: `["model2 returned ok=false: recommended_action: 'COMPLAINT_ESCALATION' not in eligible_actions ['MONITOR', 'RE_ENGAGEMENT', 'PRODUCT_REVIEW', 'SERVICE_RECOVERY']", 'model2.prediction is missing or not an object']`
- Simple output: Prediction failed: recommended_action: 'COMPLAINT_ESCALATION' not in eligible_actions ['MONITOR', 'RE_ENGAGEMENT', 'PRODUCT_REVIEW', 'SERVICE_RECOVERY']

Request:

```json
{
  "customer_id": "C18598",
  "customer_name": "Shaurya Naidu",
  "prediction_date": "2026-06-01",
  "snapshot_date": "2026-06-01",
  "target_month": "2026-07-01",
  "profile": {
    "tenure_months": 77,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 2,
    "has_credit_card": 1,
    "has_loan": 0
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 16,
      "balance_change_30d": -14.5037,
      "transaction_change_30d": -1.8496,
      "card_spend_change_30d": -11.4829,
      "app_login_change_30d": 4.2589,
      "salary_missing_days": 3.0,
      "external_transfer_change_30d": 45.1205,
      "upi_share_of_spend": 0.4768,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 2,
      "avg_resolution_time_hrs": 21.2083,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-02-01",
      "days_since_last_transaction": 16,
      "balance_change_30d": -2.1307,
      "transaction_change_30d": -27.4855,
      "card_spend_change_30d": 6.1959,
      "app_login_change_30d": -3.3414,
      "salary_missing_days": 1.0,
      "external_transfer_change_30d": -1.7305,
      "upi_share_of_spend": 0.5505,
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
      "balance_change_30d": 3.3673,
      "transaction_change_30d": -2.3299,
      "card_spend_change_30d": -13.1704,
      "app_login_change_30d": 21.0775,
      "salary_missing_days": 2.0,
      "external_transfer_change_30d": 21.7273,
      "upi_share_of_spend": 0.4735,
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
      "days_since_last_transaction": 7,
      "balance_change_30d": 0.9174,
      "transaction_change_30d": 2.4081,
      "card_spend_change_30d": -16.9315,
      "app_login_change_30d": -7.0016,
      "salary_missing_days": 2.0,
      "external_transfer_change_30d": 1.4225,
      "upi_share_of_spend": 0.5088,
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
      "balance_change_30d": 12.3695,
      "transaction_change_30d": 29.5678,
      "card_spend_change_30d": 34.8683,
      "app_login_change_30d": 34.3486,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -14.8543,
      "upi_share_of_spend": 0.4734,
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
      "balance_change_30d": 15.4208,
      "transaction_change_30d": -2.8467,
      "card_spend_change_30d": 12.1917,
      "app_login_change_30d": 31.0764,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": 15.1877,
      "upi_share_of_spend": 0.3677,
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
    "tenure_months": 77,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 2,
    "has_credit_card": 1,
    "has_loan": 0,
    "days_since_last_transaction": 5,
    "balance_change_30d": 15.4208,
    "transaction_change_30d": -2.8467,
    "card_spend_change_30d": 12.1917,
    "app_login_change_30d": 31.0764,
    "salary_missing_days": 0.0,
    "external_transfer_change_30d": 15.1877,
    "upi_share_of_spend": 0.3677,
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
      "tenure_months": 77,
      "age": 31,
      "customer_yearly_value": 28589.1684,
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
    "served_at": "2026-08-31T01:08:10",
    "elapsed_ms": 4080.1,
    "timings_ms": {
      "model1": 58.57,
      "model2": 4021.41
    },
    "customer_id": "C18598",
    "customer_name": "Shaurya Naidu",
    "snapshot_date": "2026-06-01"
  },
  "model1": {
    "churn_probability": 1.87,
    "raw_churn_probability": 16.91,
    "probability_mode": "sigmoid",
    "risk_score": 5.6,
    "churn_prediction": "No",
    "risk_level": "Low",
    "top_risk_factors": [
      {
        "factor": "card_spend_change_30d_trend_6m",
        "value": 5.732259999999999,
        "message": "This signal increased churn risk.",
        "contribution": 0.027845783159136772
      },
      {
        "factor": "latest_vs_avg_app_login_change_30d_available_history",
        "value": 17.673333333333332,
        "message": "This signal increased churn risk.",
        "contribution": 0.01833144947886467
      },
      {
        "factor": "max_salary_missing_days_3m",
        "value": 2.0,
        "message": "Salary or pension was delayed recently.",
        "contribution": 0.01202604454010725
      },
      {
        "factor": "sum_failed_transactions_30d_6m",
        "value": 5.0,
        "message": "Customer has recent failed transactions.",
        "contribution": 0.006693183910101652
      },
      {
        "factor": "max_days_since_last_transaction_3m",
        "value": 7.0,
        "message": "Customer has gone longer without transacting.",
        "contribution": 0.004795522894710302
      }
    ]
  },
  "model2_input": {
    "customer_context": {
      "age": 31,
      "tenure_months": 77,
      "customer_segment": "salary",
      "income_regularity": "regular",
      "customer_yearly_value": 28589.1684,
      "products_count": 2,
      "has_credit_card": 1,
      "has_loan": 0
    },
    "behavior": {
      "days_since_last_transaction": 5,
      "balance_change_30d": 15.4208,
      "transaction_change_30d": -2.8467,
      "card_spend_change_30d": 12.1917,
      "app_login_change_30d": 31.0764,
      "salary_missing_days": 0,
      "external_transfer_change_30d": 15.1877,
      "upi_share_of_spend": 0.3677,
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
      "churn_probability": 0.0187,
      "churn_prediction": "No",
      "risk_level": "Low",
      "top_risk_factors": [
        {
          "factor": "card_spend_change_30d_trend_6m",
          "value": 5.732259999999999
        },
        {
          "factor": "vs_avg_app_login_change_30d_available_history",
          "value": 17.673333333333332
        },
        {
          "factor": "max_salary_missing_days_3m",
          "value": 2.0
        },
        {
          "factor": "sum_failed_transactions_30d_6m",
          "value": 5.0
        },
        {
          "factor": "max_days_since_last_transaction_3m",
          "value": 7.0
        }
      ]
    },
    "eligible_actions": [
      "MONITOR",
      "RE_ENGAGEMENT",
      "PRODUCT_REVIEW",
      "SERVICE_RECOVERY"
    ],
    "case_id": "C18598"
  },
  "model2": {
    "case_id": "C18598",
    "ok": false,
    "prediction": null,
    "raw_text": "{\"evidence\":[\"complaints_30d=0\",\"failed_transactions_30d=1\"],\"primary_reason\":\"SERVICE_DISSATISFACTION\",\"reasoning_summary\":\"Service friction is the clearest risk signal here. Complaint escalation fits because complaints_30d=0 and failed_transactions_30d=1 indicate a real issue that hasn't been resolved.\",\"recommended_action\":\"COMPLAINT_ESCALATION\",\"secondary_reasons\":[\"UNKNOWN\"],\"urgency\":\"MEDIUM\"}",
    "error": "recommended_action: 'COMPLAINT_ESCALATION' not in eligible_actions ['MONITOR', 'RE_ENGAGEMENT', 'PRODUCT_REVIEW', 'SERVICE_RECOVERY']",
    "latency_s": 4.0213,
    "simple_output": "Prediction failed: recommended_action: 'COMPLAINT_ESCALATION' not in eligible_actions ['MONITOR', 'RE_ENGAGEMENT', 'PRODUCT_REVIEW', 'SERVICE_RECOVERY']"
  }
}
```

### Aayush Barad (`C18602`)

- OK: `True`
- Shape errors: `[]`
- Simple output: Reason: LOW_ENGAGEMENT | Urgency: MEDIUM | Action: RE_ENGAGEMENT | Why: The relationship looks stale or the product-fit may be wrong because transaction_change_30d=26.4 and balance_change_30d=19.0 suggest the customer might be disengaged.

Request:

```json
{
  "customer_id": "C18602",
  "customer_name": "Aayush Barad",
  "prediction_date": "2026-06-01",
  "snapshot_date": "2026-06-01",
  "target_month": "2026-07-01",
  "profile": {
    "tenure_months": 130,
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
      "balance_change_30d": -39.3652,
      "transaction_change_30d": -43.7855,
      "card_spend_change_30d": 1.1459,
      "app_login_change_30d": 9.9917,
      "salary_missing_days": null,
      "external_transfer_change_30d": 6.0573,
      "upi_share_of_spend": 0.4163,
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
      "days_since_last_transaction": 10,
      "balance_change_30d": -13.8402,
      "transaction_change_30d": -18.6638,
      "card_spend_change_30d": -40.7493,
      "app_login_change_30d": -9.1384,
      "salary_missing_days": null,
      "external_transfer_change_30d": 41.5083,
      "upi_share_of_spend": 0.3999,
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
      "balance_change_30d": 30.8066,
      "transaction_change_30d": 28.572,
      "card_spend_change_30d": 6.1302,
      "app_login_change_30d": -8.7152,
      "salary_missing_days": null,
      "external_transfer_change_30d": 16.0269,
      "upi_share_of_spend": 0.3139,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 10.7391,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-04-01",
      "days_since_last_transaction": 0,
      "balance_change_30d": 35.8229,
      "transaction_change_30d": 3.1544,
      "card_spend_change_30d": 22.9319,
      "app_login_change_30d": 15.3661,
      "salary_missing_days": null,
      "external_transfer_change_30d": 29.1501,
      "upi_share_of_spend": 0.278,
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
      "balance_change_30d": 1.4501,
      "transaction_change_30d": 10.9022,
      "card_spend_change_30d": 19.8195,
      "app_login_change_30d": 11.1174,
      "salary_missing_days": null,
      "external_transfer_change_30d": 25.7489,
      "upi_share_of_spend": 0.3837,
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
      "balance_change_30d": 18.9151,
      "transaction_change_30d": 26.4405,
      "card_spend_change_30d": 23.7246,
      "app_login_change_30d": 26.4203,
      "salary_missing_days": null,
      "external_transfer_change_30d": -24.0339,
      "upi_share_of_spend": 0.234,
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
    "tenure_months": 130,
    "customer_segment": "farmer",
    "income_regularity": "seasonal",
    "products_count": 1,
    "has_credit_card": 0,
    "has_loan": 0,
    "days_since_last_transaction": 0,
    "balance_change_30d": 18.9151,
    "transaction_change_30d": 26.4405,
    "card_spend_change_30d": 23.7246,
    "app_login_change_30d": 26.4203,
    "salary_missing_days": null,
    "external_transfer_change_30d": -24.0339,
    "upi_share_of_spend": 0.234,
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
      "tenure_months": 130,
      "age": 55,
      "customer_yearly_value": 37683.9299,
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
    "served_at": "2026-08-31T01:08:12",
    "elapsed_ms": 2276.28,
    "timings_ms": {
      "model1": 65.03,
      "model2": 2211.14
    },
    "customer_id": "C18602",
    "customer_name": "Aayush Barad",
    "snapshot_date": "2026-06-01"
  },
  "model1": {
    "churn_probability": 1.68,
    "raw_churn_probability": 14.61,
    "probability_mode": "sigmoid",
    "risk_score": 5.04,
    "churn_prediction": "No",
    "risk_level": "Low",
    "top_risk_factors": [
      {
        "factor": "latest_vs_avg_external_transfer_change_30d_available_history",
        "value": -39.77683333333333,
        "message": "This signal increased churn risk.",
        "contribution": 0.06466741114854813
      },
      {
        "factor": "latest_vs_avg_app_login_change_30d_available_history",
        "value": 18.913316666666667,
        "message": "This signal increased churn risk.",
        "contribution": 0.05303025245666504
      },
      {
        "factor": "card_spend_change_30d_trend_6m",
        "value": 8.89718857142857,
        "message": "This signal increased churn risk.",
        "contribution": 0.04728706181049347
      },
      {
        "factor": "max_days_since_last_transaction_6m",
        "value": 10.0,
        "message": "Customer has gone longer without transacting.",
        "contribution": 0.0069934227503836155
      },
      {
        "factor": "count_balance_drop_3m",
        "value": 0,
        "message": "This signal increased churn risk.",
        "contribution": 0.005054573528468609
      }
    ]
  },
  "model2_input": {
    "customer_context": {
      "age": 55,
      "tenure_months": 130,
      "customer_segment": "farmer",
      "income_regularity": "seasonal",
      "customer_yearly_value": 37683.9299,
      "products_count": 1,
      "has_credit_card": 0,
      "has_loan": 0
    },
    "behavior": {
      "days_since_last_transaction": 0,
      "balance_change_30d": 18.9151,
      "transaction_change_30d": 26.4405,
      "card_spend_change_30d": 23.7246,
      "app_login_change_30d": 26.4203,
      "salary_missing_days": null,
      "external_transfer_change_30d": -24.0339,
      "upi_share_of_spend": 0.234,
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
      "churn_probability": 0.0168,
      "churn_prediction": "No",
      "risk_level": "Low",
      "top_risk_factors": [
        {
          "factor": "vs_avg_external_transfer_change_30d_available_history",
          "value": -39.77683333333333
        },
        {
          "factor": "vs_avg_app_login_change_30d_available_history",
          "value": 18.913316666666667
        },
        {
          "factor": "card_spend_change_30d_trend_6m",
          "value": 8.89718857142857
        },
        {
          "factor": "max_days_since_last_transaction_6m",
          "value": 10.0
        },
        {
          "factor": "count_balance_drop_3m",
          "value": 0
        }
      ]
    },
    "eligible_actions": [
      "MONITOR",
      "RE_ENGAGEMENT",
      "PRODUCT_REVIEW"
    ],
    "case_id": "C18602"
  },
  "model2": {
    "case_id": "C18602",
    "ok": true,
    "prediction": {
      "evidence": [
        "transaction_change_30d=26.4",
        "balance_change_30d=19.0",
        "vs_avg_balance_change_30d_available_history=-18.7"
      ],
      "primary_reason": "LOW_ENGAGEMENT",
      "reasoning_summary": "The relationship looks stale or the product-fit may be wrong because transaction_change_30d=26.4 and balance_change_30d=19.0 suggest the customer might be disengaged.",
      "recommended_action": "RE_ENGAGEMENT",
      "secondary_reasons": [
        "PRODUCT_MISMATCH"
      ],
      "urgency": "MEDIUM"
    },
    "raw_text": "{\"evidence\":[\"transaction_change_30d=26.4\",\"balance_change_30d=19.0\",\"vs_avg_balance_change_30d_available_history=-18.7\"],\"primary_reason\":\"LOW_ENGAGEMENT\",\"reasoning_summary\":\"The relationship looks stale or the product-fit may be wrong because transaction_change_30d=26.4 and balance_change_30d=19.0 suggest the customer might be disengaged.\",\"recommended_action\":\"RE_ENGAGEMENT\",\"secondary_reasons\":[\"PRODUCT_MISMATCH\"],\"urgency\":\"MEDIUM\"}",
    "error": null,
    "latency_s": 2.2109,
    "simple_output": "Reason: LOW_ENGAGEMENT | Urgency: MEDIUM | Action: RE_ENGAGEMENT | Why: The relationship looks stale or the product-fit may be wrong because transaction_change_30d=26.4 and balance_change_30d=19.0 suggest the customer might be disengaged."
  }
}
```

### Owen Kota (`C19841`)

- OK: `True`
- Shape errors: `[]`
- Simple output: Reason: LOW_ENGAGEMENT | Urgency: MEDIUM | Action: RE_ENGAGEMENT | Why: The relationship looks inactive or disconnected. Service evidence is mixed or insufficient, so engagement-focused action is the best choice.

Request:

```json
{
  "customer_id": "C19841",
  "customer_name": "Owen Kota",
  "prediction_date": "2026-06-01",
  "snapshot_date": "2026-06-01",
  "target_month": "2026-07-01",
  "profile": {
    "tenure_months": 121,
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
      "balance_change_30d": -12.1633,
      "transaction_change_30d": -14.2554,
      "card_spend_change_30d": -17.4097,
      "app_login_change_30d": -9.0471,
      "salary_missing_days": 2.0,
      "external_transfer_change_30d": -1.2786,
      "upi_share_of_spend": 0.1919,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 2,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 2,
      "avg_resolution_time_hrs": 37.6353,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-02-01",
      "days_since_last_transaction": 6,
      "balance_change_30d": 2.3882,
      "transaction_change_30d": 0.3005,
      "card_spend_change_30d": -27.9418,
      "app_login_change_30d": 4.7399,
      "salary_missing_days": 2.0,
      "external_transfer_change_30d": -9.5463,
      "upi_share_of_spend": 0.0363,
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
      "days_since_last_transaction": 8,
      "balance_change_30d": 14.583,
      "transaction_change_30d": 16.4921,
      "card_spend_change_30d": 17.8296,
      "app_login_change_30d": 24.292,
      "salary_missing_days": 2.0,
      "external_transfer_change_30d": 21.4327,
      "upi_share_of_spend": 0.0407,
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
      "days_since_last_transaction": 0,
      "balance_change_30d": 24.0061,
      "transaction_change_30d": 36.8753,
      "card_spend_change_30d": 16.2599,
      "app_login_change_30d": 25.938,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -21.4494,
      "upi_share_of_spend": 0.0,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 9.5981,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-05-01",
      "days_since_last_transaction": 5,
      "balance_change_30d": -10.7594,
      "transaction_change_30d": -12.4015,
      "card_spend_change_30d": 2.2674,
      "app_login_change_30d": 23.3737,
      "salary_missing_days": 2.0,
      "external_transfer_change_30d": -33.7053,
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
      "snapshot_date": "2026-06-01",
      "days_since_last_transaction": 3,
      "balance_change_30d": -36.7038,
      "transaction_change_30d": -3.0991,
      "card_spend_change_30d": 23.6302,
      "app_login_change_30d": 5.3859,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": 12.2041,
      "upi_share_of_spend": 0.0126,
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
    "tenure_months": 121,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 2,
    "has_credit_card": 1,
    "has_loan": 0,
    "days_since_last_transaction": 3,
    "balance_change_30d": -36.7038,
    "transaction_change_30d": -3.0991,
    "card_spend_change_30d": 23.6302,
    "app_login_change_30d": 5.3859,
    "salary_missing_days": 0.0,
    "external_transfer_change_30d": 12.2041,
    "upi_share_of_spend": 0.0126,
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
      "tenure_months": 121,
      "age": 48,
      "customer_yearly_value": 32207.2786,
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
    "served_at": "2026-08-31T01:08:14",
    "elapsed_ms": 2016.07,
    "timings_ms": {
      "model1": 70.57,
      "model2": 1945.41
    },
    "customer_id": "C19841",
    "customer_name": "Owen Kota",
    "snapshot_date": "2026-06-01"
  },
  "model1": {
    "churn_probability": 1.86,
    "raw_churn_probability": 16.86,
    "probability_mode": "sigmoid",
    "risk_score": 5.58,
    "churn_prediction": "No",
    "risk_level": "Low",
    "top_risk_factors": [
      {
        "factor": "latest_balance_change_30d",
        "value": -36.7038,
        "message": "Balance has been falling across recent months.",
        "contribution": 0.08260656893253326
      },
      {
        "factor": "latest_upi_share_of_spend",
        "value": 0.0126,
        "message": "A larger share of spending is happening through UPI.",
        "contribution": 0.0473187081515789
      },
      {
        "factor": "avg_upi_share_of_spend_6m",
        "value": 0.04691666666666666,
        "message": "A larger share of spending is happening through UPI.",
        "contribution": 0.02257099747657776
      },
      {
        "factor": "sum_failed_transactions_30d_6m",
        "value": 5.0,
        "message": "Customer has recent failed transactions.",
        "contribution": 0.022209400311112404
      },
      {
        "factor": "max_salary_missing_days_6m",
        "value": 2.0,
        "message": "Salary or pension was delayed recently.",
        "contribution": 0.008568930439651012
      }
    ]
  },
  "model2_input": {
    "customer_context": {
      "age": 48,
      "tenure_months": 121,
      "customer_segment": "salary",
      "income_regularity": "regular",
      "customer_yearly_value": 32207.2786,
      "products_count": 2,
      "has_credit_card": 1,
      "has_loan": 0
    },
    "behavior": {
      "days_since_last_transaction": 3,
      "balance_change_30d": -36.7038,
      "transaction_change_30d": -3.0991,
      "card_spend_change_30d": 23.6302,
      "app_login_change_30d": 5.3859,
      "salary_missing_days": 0,
      "external_transfer_change_30d": 12.2041,
      "upi_share_of_spend": 0.0126,
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
      "churn_probability": 0.0186,
      "churn_prediction": "No",
      "risk_level": "Low",
      "top_risk_factors": [
        {
          "factor": "balance_change_30d",
          "value": -36.7038
        },
        {
          "factor": "upi_share_of_spend",
          "value": 0.0126
        },
        {
          "factor": "avg_upi_share_of_spend_6m",
          "value": 0.04691666666666666
        },
        {
          "factor": "sum_failed_transactions_30d_6m",
          "value": 5.0
        },
        {
          "factor": "max_salary_missing_days_6m",
          "value": 2.0
        }
      ]
    },
    "eligible_actions": [
      "MONITOR",
      "RE_ENGAGEMENT",
      "PRODUCT_REVIEW"
    ],
    "case_id": "C19841"
  },
  "model2": {
    "case_id": "C19841",
    "ok": true,
    "prediction": {
      "evidence": [
        "transaction_change_30d=-3.1",
        "balance_change_30d=-36.7",
        "complaints_30d=0",
        "external_transfer_change_30d=12.2"
      ],
      "primary_reason": "LOW_ENGAGEMENT",
      "reasoning_summary": "The relationship looks inactive or disconnected. Service evidence is mixed or insufficient, so engagement-focused action is the best choice.",
      "recommended_action": "RE_ENGAGEMENT",
      "secondary_reasons": [
        "UNKNOWN"
      ],
      "urgency": "MEDIUM"
    },
    "raw_text": "{\n\"evidence\":[\"transaction_change_30d=-3.1\",\"balance_change_30d=-36.7\",\"complaints_30d=0\",\"external_transfer_change_30d=12.2\"],\"primary_reason\":\"LOW_ENGAGEMENT\",\"reasoning_summary\":\"The relationship looks inactive or disconnected. Service evidence is mixed or insufficient, so engagement-focused action is the best choice.\",\"recommended_action\":\"RE_ENGAGEMENT\",\"secondary_reasons\":[\"UNKNOWN\"],\"urgency\":\"MEDIUM\"}",
    "error": null,
    "latency_s": 1.9453,
    "simple_output": "Reason: LOW_ENGAGEMENT | Urgency: MEDIUM | Action: RE_ENGAGEMENT | Why: The relationship looks inactive or disconnected. Service evidence is mixed or insufficient, so engagement-focused action is the best choice."
  }
}
```
