# Devang Model 1 -> Model 2 API Test Results

- API URL: `http://127.0.0.1:8001`
- Created at: `2026-08-31T01:14:16`
- Customers tested: `20`
- Source CSV: `model_1_v2\data\customers.csv`
- Health OK: `True`
- Ollama model: `devang-model2-q4`
- Model 1 loaded: `True`

## Summary

| # | Customer | Model 1 risk | Prediction | Reason | Urgency | Action | OK | Seconds |
|---:|---|---:|---|---|---|---|---|---:|
| 1 | Lajita Mall (`C10017`) | 1.99 | No | UNKNOWN | MEDIUM | MONITOR | yes | 2.26 |
| 2 | Bhavna Karan (`C10294`) | 3.11 | No | UNKNOWN | MEDIUM | MONITOR | yes | 1.93 |
| 3 | Inaya Mukherjee (`C10445`) | 2.53 | No | UNKNOWN | MEDIUM | MONITOR | yes | 3.63 |
| 4 | Nidra Thakkar (`C10646`) | 2.39 | No | UNKNOWN | MEDIUM | MONITOR | yes | 2.53 |
| 5 | Geetika Mitter (`C11080`) | 39.84 | Yes | SERVICE_DISSATISFACTION | HIGH | COMPLAINT_ESCALATION | yes | 7.19 |
| 6 | Jagat Karpe (`C11383`) | 3.27 | No | SERVICE_DISSATISFACTION | MEDIUM | SERVICE_RECOVERY | yes | 2.89 |
| 7 | Meghana Kibe (`C11525`) | 3.28 | No | SERVICE_DISSATISFACTION | MEDIUM | SERVICE_RECOVERY | yes | 2.36 |
| 8 | Ekani Iyer (`C11749`) | 32.26 | Yes | SERVICE_DISSATISFACTION | HIGH | COMPLAINT_ESCALATION | yes | 7.91 |
| 9 | Vedika Wagle (`C12000`) | 8.99 | No | UNKNOWN | MEDIUM | MONITOR | yes | 2.32 |
| 10 | Warjas Tailor (`C12460`) | 2.27 | No | SERVICE_DISSATISFACTION | MEDIUM | SERVICE_RECOVERY | yes | 2.61 |
| 11 | Pushti Nayar (`C12775`) | 22.93 | Yes | SERVICE_DISSATISFACTION | MEDIUM | COMPLAINT_ESCALATION | yes | 3.39 |
| 12 | Yasti Sagar (`C13034`) | 2.98 | No | UNKNOWN | MEDIUM | MONITOR | yes | 1.85 |
| 13 | Girindra Chaudhry (`C13336`) | 3.74 | No | UNKNOWN | MEDIUM | MONITOR | yes | 2.27 |
| 14 | Nihal Gola (`C13982`) | 16.31 | No | SERVICE_DISSATISFACTION | MEDIUM | SERVICE_RECOVERY | yes | 2.93 |
| 15 | Shivani Ramachandran (`C14465`) | 10.66 | No | SERVICE_DISSATISFACTION | MEDIUM | SERVICE_RECOVERY | yes | 2.59 |
| 16 | Tanmayi Barad (`C15320`) | 4.41 | No | UNKNOWN | MEDIUM | MONITOR | yes | 2.26 |
| 17 | Fiyaz Goel (`C15871`) | 8.9 | No | SERVICE_DISSATISFACTION | MEDIUM | SERVICE_RECOVERY | yes | 2.97 |
| 18 | Tristan Pall (`C16970`) | 42.95 | Yes | UNKNOWN | MEDIUM | MONITOR | yes | 3.57 |
| 19 | Zarna Prabhakar (`C18154`) | 1.49 | No | UNKNOWN | MEDIUM | MONITOR | yes | 2.7 |
| 20 | Forum Dutt (`C19609`) | 34.19 | Yes | UNKNOWN | MEDIUM | MONITOR | yes | 3.46 |

## Details

### Lajita Mall (`C10017`)

- OK: `True`
- Shape errors: `[]`
- Simple output: Reason: UNKNOWN | Urgency: MEDIUM | Action: MONITOR | Why: Evidence is mixed or weak, so the cause remains unknown. The current relationship setup looks okay but there are some minor signals to investigate further.

Request:

```json
{
  "customer_id": "C10017",
  "customer_name": "Lajita Mall",
  "prediction_date": "2026-06-01",
  "snapshot_date": "2026-06-01",
  "target_month": "2026-07-01",
  "profile": {
    "tenure_months": 89,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 3,
    "has_credit_card": 1,
    "has_loan": 1
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 6,
      "balance_change_30d": -0.0132,
      "transaction_change_30d": 3.157,
      "card_spend_change_30d": -14.1708,
      "app_login_change_30d": -6.623,
      "salary_missing_days": 4.0,
      "external_transfer_change_30d": -1.9234,
      "upi_share_of_spend": 0.5119,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 1,
      "failed_transactions_30d": 2,
      "avg_resolution_time_hrs": 18.137,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-02-01",
      "days_since_last_transaction": 8,
      "balance_change_30d": -9.9463,
      "transaction_change_30d": 10.9389,
      "card_spend_change_30d": 33.8539,
      "app_login_change_30d": 18.5075,
      "salary_missing_days": 1.0,
      "external_transfer_change_30d": 22.225,
      "upi_share_of_spend": 0.5189,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 1.0,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-03-01",
      "days_since_last_transaction": 5,
      "balance_change_30d": 20.7578,
      "transaction_change_30d": -11.6717,
      "card_spend_change_30d": 3.4273,
      "app_login_change_30d": 19.0462,
      "salary_missing_days": 1.0,
      "external_transfer_change_30d": -19.0657,
      "upi_share_of_spend": 0.5626,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 12.725,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-04-01",
      "days_since_last_transaction": 7,
      "balance_change_30d": 30.2703,
      "transaction_change_30d": 24.7023,
      "card_spend_change_30d": 34.4121,
      "app_login_change_30d": 3.6335,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": 17.854,
      "upi_share_of_spend": 0.4725,
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
      "balance_change_30d": 29.5166,
      "transaction_change_30d": -5.9508,
      "card_spend_change_30d": 24.3771,
      "app_login_change_30d": 33.3615,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": 14.1451,
      "upi_share_of_spend": 0.3988,
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
      "days_since_last_transaction": 2,
      "balance_change_30d": 53.1929,
      "transaction_change_30d": 38.9711,
      "card_spend_change_30d": 32.3635,
      "app_login_change_30d": 9.3925,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -38.6083,
      "upi_share_of_spend": 0.4304,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 20.4034,
      "emi_bounce_30d": 0
    }
  ],
  "customer": {
    "tenure_months": 89,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 3,
    "has_credit_card": 1,
    "has_loan": 1,
    "days_since_last_transaction": 2,
    "balance_change_30d": 53.1929,
    "transaction_change_30d": 38.9711,
    "card_spend_change_30d": 32.3635,
    "app_login_change_30d": 9.3925,
    "salary_missing_days": 0.0,
    "external_transfer_change_30d": -38.6083,
    "upi_share_of_spend": 0.4304,
    "fd_maturing_in_30d": 0,
    "products_dropped_90d": 0,
    "complaints_30d": 1,
    "unresolved_complaints": 0,
    "failed_transactions_30d": 0,
    "avg_resolution_time_hrs": 20.4034,
    "emi_bounce_30d": 0
  },
  "extra_context": {
    "customer_profile": {
      "segment": "salary",
      "income_regularity": "regular",
      "tenure_months": 89,
      "age": 44,
      "customer_yearly_value": 40964.2704,
      "products_count": 3,
      "has_credit_card": 1,
      "has_loan": 1,
      "value_tier": "medium"
    },
    "recent_complaint_text": "My EMI is debited on 5th but salary comes on 7th. Please shift the date."
  }
}
```

Response:

```json
{
  "meta": {
    "endpoint": "/predict/both",
    "served_at": "2026-08-31T01:13:15",
    "elapsed_ms": 2237.03,
    "timings_ms": {
      "model1": 124.25,
      "model2": 2112.63
    },
    "customer_id": "C10017",
    "customer_name": "Lajita Mall",
    "snapshot_date": "2026-06-01"
  },
  "model1": {
    "churn_probability": 1.99,
    "raw_churn_probability": 18.37,
    "probability_mode": "sigmoid",
    "risk_score": 5.98,
    "churn_prediction": "No",
    "risk_level": "Low",
    "top_risk_factors": [
      {
        "factor": "latest_vs_avg_external_transfer_change_30d_available_history",
        "value": -37.71275,
        "message": "This signal increased churn risk.",
        "contribution": 0.07300715893507004
      },
      {
        "factor": "card_spend_change_30d_trend_6m",
        "value": 6.7207399999999975,
        "message": "This signal increased churn risk.",
        "contribution": 0.0615234337747097
      },
      {
        "factor": "avg_balance_change_30d_3m",
        "value": 37.659933333333335,
        "message": "This signal increased churn risk.",
        "contribution": 0.04920917749404907
      },
      {
        "factor": "avg_transaction_change_30d_6m",
        "value": 10.024466666666667,
        "message": "This signal increased churn risk.",
        "contribution": 0.02445877529680729
      },
      {
        "factor": "max_days_since_last_transaction_3m",
        "value": 7.0,
        "message": "Customer has gone longer without transacting.",
        "contribution": 0.010918193496763706
      }
    ]
  },
  "model2_input": {
    "customer_context": {
      "age": 44,
      "tenure_months": 89,
      "customer_segment": "salary",
      "income_regularity": "regular",
      "customer_yearly_value": 40964.2704,
      "products_count": 3,
      "has_credit_card": 1,
      "has_loan": 1
    },
    "behavior": {
      "days_since_last_transaction": 2,
      "balance_change_30d": 53.1929,
      "transaction_change_30d": 38.9711,
      "card_spend_change_30d": 32.3635,
      "app_login_change_30d": 9.3925,
      "salary_missing_days": 0,
      "external_transfer_change_30d": -38.6083,
      "upi_share_of_spend": 0.4304,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "emi_bounce_30d": 0
    },
    "service_evidence": {
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 20.4034,
      "complaint_text": "My EMI is debited on 5th but salary comes on 7th. Please shift the date."
    },
    "model1": {
      "churn_probability": 0.0199,
      "churn_prediction": "No",
      "risk_level": "Low",
      "top_risk_factors": [
        {
          "factor": "vs_avg_external_transfer_change_30d_available_history",
          "value": -37.71275
        },
        {
          "factor": "card_spend_change_30d_trend_6m",
          "value": 6.7207399999999975
        },
        {
          "factor": "avg_balance_change_30d_3m",
          "value": 37.659933333333335
        },
        {
          "factor": "avg_transaction_change_30d_6m",
          "value": 10.024466666666667
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
    "case_id": "C10017"
  },
  "model2": {
    "case_id": "C10017",
    "ok": true,
    "prediction": {
      "evidence": [
        "complaints_30d=1",
        "failed_transactions_30d=0",
        "avg_resolution_time_hrs=20.4",
        "card_spend_change_30d=-32.4"
      ],
      "primary_reason": "UNKNOWN",
      "reasoning_summary": "Evidence is mixed or weak, so the cause remains unknown. The current relationship setup looks okay but there are some minor signals to investigate further.",
      "recommended_action": "MONITOR",
      "secondary_reasons": [
        "SERVICE_DISSATISFACTION"
      ],
      "urgency": "MEDIUM"
    },
    "raw_text": "{\"evidence\":[\"complaints_30d=1\",\"failed_transactions_30d=0\",\"avg_resolution_time_hrs=20.4\",\"card_spend_change_30d=-32.4\"],\"primary_reason\":\"UNKNOWN\",\"reasoning_summary\":\"Evidence is mixed or weak, so the cause remains unknown. The current relationship setup looks okay but there are some minor signals to investigate further.\",\"recommended_action\":\"MONITOR\",\"secondary_reasons\":[\"SERVICE_DISSATISFACTION\"],\"urgency\":\"MEDIUM\"}",
    "error": null,
    "latency_s": 2.1125,
    "simple_output": "Reason: UNKNOWN | Urgency: MEDIUM | Action: MONITOR | Why: Evidence is mixed or weak, so the cause remains unknown. The current relationship setup looks okay but there are some minor signals to investigate further."
  }
}
```

### Bhavna Karan (`C10294`)

- OK: `True`
- Shape errors: `[]`
- Simple output: Reason: UNKNOWN | Urgency: MEDIUM | Action: MONITOR | Why: Evidence is mixed or weak, so the cause remains unknown. The current experience may be satisfactory despite some indirect signals being mixed.

Request:

```json
{
  "customer_id": "C10294",
  "customer_name": "Bhavna Karan",
  "prediction_date": "2026-06-01",
  "snapshot_date": "2026-06-01",
  "target_month": "2026-07-01",
  "profile": {
    "tenure_months": 52,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 2,
    "has_credit_card": 0,
    "has_loan": 1
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 5,
      "balance_change_30d": -6.6965,
      "transaction_change_30d": 5.6725,
      "card_spend_change_30d": 9.7832,
      "app_login_change_30d": -5.9018,
      "salary_missing_days": 1.0,
      "external_transfer_change_30d": 5.3819,
      "upi_share_of_spend": 0.3127,
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
      "days_since_last_transaction": 2,
      "balance_change_30d": 31.3421,
      "transaction_change_30d": 5.999,
      "card_spend_change_30d": -1.4431,
      "app_login_change_30d": 18.8784,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": 8.0229,
      "upi_share_of_spend": 0.222,
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
      "days_since_last_transaction": 3,
      "balance_change_30d": -6.6331,
      "transaction_change_30d": 19.8209,
      "card_spend_change_30d": -15.8623,
      "app_login_change_30d": 27.5238,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": 3.3613,
      "upi_share_of_spend": 0.2533,
      "fd_maturing_in_30d": 1,
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
      "balance_change_30d": 0.9183,
      "transaction_change_30d": -18.2439,
      "card_spend_change_30d": -12.0904,
      "app_login_change_30d": -18.0333,
      "salary_missing_days": 3.0,
      "external_transfer_change_30d": 37.3819,
      "upi_share_of_spend": 0.2846,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 1,
      "complaints_30d": 2,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 33.9235,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-05-01",
      "days_since_last_transaction": 8,
      "balance_change_30d": -9.8261,
      "transaction_change_30d": -14.1408,
      "card_spend_change_30d": 8.3178,
      "app_login_change_30d": -20.9147,
      "salary_missing_days": 3.0,
      "external_transfer_change_30d": 8.0399,
      "upi_share_of_spend": 0.4293,
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
      "days_since_last_transaction": 6,
      "balance_change_30d": 6.6318,
      "transaction_change_30d": -1.8184,
      "card_spend_change_30d": -34.8147,
      "app_login_change_30d": 0.3794,
      "salary_missing_days": 1.0,
      "external_transfer_change_30d": 1.2222,
      "upi_share_of_spend": 0.2744,
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
    "tenure_months": 52,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 2,
    "has_credit_card": 0,
    "has_loan": 1,
    "days_since_last_transaction": 6,
    "balance_change_30d": 6.6318,
    "transaction_change_30d": -1.8184,
    "card_spend_change_30d": -34.8147,
    "app_login_change_30d": 0.3794,
    "salary_missing_days": 1.0,
    "external_transfer_change_30d": 1.2222,
    "upi_share_of_spend": 0.2744,
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
      "tenure_months": 52,
      "age": 55,
      "customer_yearly_value": 87723.166,
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
    "served_at": "2026-08-31T01:13:17",
    "elapsed_ms": 1926.79,
    "timings_ms": {
      "model1": 76.42,
      "model2": 1850.23
    },
    "customer_id": "C10294",
    "customer_name": "Bhavna Karan",
    "snapshot_date": "2026-06-01"
  },
  "model1": {
    "churn_probability": 3.11,
    "raw_churn_probability": 28.15,
    "probability_mode": "sigmoid",
    "risk_score": 9.32,
    "churn_prediction": "No",
    "risk_level": "Low",
    "top_risk_factors": [
      {
        "factor": "latest_card_spend_change_30d",
        "value": -34.8147,
        "message": "Card spending has been falling across recent months.",
        "contribution": 0.03438824787735939
      },
      {
        "factor": "external_transfer_change_30d_trend_6m",
        "value": 0.3792314285714285,
        "message": "External transfers have increased.",
        "contribution": 0.029279246926307678
      },
      {
        "factor": "avg_card_spend_change_30d_3m",
        "value": -12.862433333333334,
        "message": "Card spending has been falling across recent months.",
        "contribution": 0.023574555292725563
      },
      {
        "factor": "avg_app_login_change_30d_3m",
        "value": -12.856200000000001,
        "message": "App usage has been falling across recent months.",
        "contribution": 0.012659155763685703
      },
      {
        "factor": "count_app_login_drop_3m",
        "value": 2,
        "message": "This signal increased churn risk.",
        "contribution": 0.011301188729703426
      }
    ]
  },
  "model2_input": {
    "customer_context": {
      "age": 55,
      "tenure_months": 52,
      "customer_segment": "salary",
      "income_regularity": "regular",
      "customer_yearly_value": 87723.166,
      "products_count": 2,
      "has_credit_card": 0,
      "has_loan": 1
    },
    "behavior": {
      "days_since_last_transaction": 6,
      "balance_change_30d": 6.6318,
      "transaction_change_30d": -1.8184,
      "card_spend_change_30d": -34.8147,
      "app_login_change_30d": 0.3794,
      "salary_missing_days": 1,
      "external_transfer_change_30d": 1.2222,
      "upi_share_of_spend": 0.2744,
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
      "churn_probability": 0.0311,
      "churn_prediction": "No",
      "risk_level": "Low",
      "top_risk_factors": [
        {
          "factor": "card_spend_change_30d",
          "value": -34.8147
        },
        {
          "factor": "external_transfer_change_30d_trend_6m",
          "value": 0.3792314285714285
        },
        {
          "factor": "avg_card_spend_change_30d_3m",
          "value": -12.862433333333334
        },
        {
          "factor": "avg_app_login_change_30d_3m",
          "value": -12.856200000000001
        },
        {
          "factor": "count_app_login_drop_3m",
          "value": 2
        }
      ]
    },
    "eligible_actions": [
      "MONITOR",
      "RE_ENGAGEMENT",
      "PRODUCT_REVIEW",
      "FINANCIAL_GUIDANCE",
      "RM_CALLBACK"
    ],
    "case_id": "C10294"
  },
  "model2": {
    "case_id": "C10294",
    "ok": true,
    "prediction": {
      "evidence": [
        "complaints_30d=0",
        "unresolved_complaints=0",
        "failed_transactions_30d=0",
        "avg_resolution_time_hrs=0.0"
      ],
      "primary_reason": "UNKNOWN",
      "reasoning_summary": "Evidence is mixed or weak, so the cause remains unknown. The current experience may be satisfactory despite some indirect signals being mixed.",
      "recommended_action": "MONITOR",
      "secondary_reasons": [
        "FINANCIAL_STRESS"
      ],
      "urgency": "MEDIUM"
    },
    "raw_text": "{\"evidence\":[\"complaints_30d=0\",\"unresolved_complaints=0\",\"failed_transactions_30d=0\",\"avg_resolution_time_hrs=0.0\"],\"primary_reason\":\"UNKNOWN\",\"reasoning_summary\":\"Evidence is mixed or weak, so the cause remains unknown. The current experience may be satisfactory despite some indirect signals being mixed.\",\"recommended_action\":\"MONITOR\",\"secondary_reasons\":[\"FINANCIAL_STRESS\"],\"urgency\":\"MEDIUM\"}",
    "error": null,
    "latency_s": 1.8492,
    "simple_output": "Reason: UNKNOWN | Urgency: MEDIUM | Action: MONITOR | Why: Evidence is mixed or weak, so the cause remains unknown. The current experience may be satisfactory despite some indirect signals being mixed."
  }
}
```

### Inaya Mukherjee (`C10445`)

- OK: `True`
- Shape errors: `[]`
- Simple output: Reason: UNKNOWN | Urgency: MEDIUM | Action: MONITOR | Why: Evidence is mixed or weak, so the cause remains unknown. The relationship looks stable overall but there are some concerning signals.

Request:

```json
{
  "customer_id": "C10445",
  "customer_name": "Inaya Mukherjee",
  "prediction_date": "2026-06-01",
  "snapshot_date": "2026-06-01",
  "target_month": "2026-07-01",
  "profile": {
    "tenure_months": 147,
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
      "balance_change_30d": 2.883,
      "transaction_change_30d": 16.2933,
      "card_spend_change_30d": -24.2736,
      "app_login_change_30d": 42.6189,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -29.6269,
      "upi_share_of_spend": 0.6792,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 19.9511,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-02-01",
      "days_since_last_transaction": 2,
      "balance_change_30d": 22.1914,
      "transaction_change_30d": 6.6469,
      "card_spend_change_30d": 60.612,
      "app_login_change_30d": 17.0267,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -8.2153,
      "upi_share_of_spend": 0.6505,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 2,
      "avg_resolution_time_hrs": 11.2184,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-03-01",
      "days_since_last_transaction": 1,
      "balance_change_30d": 9.2353,
      "transaction_change_30d": 14.4086,
      "card_spend_change_30d": 13.708,
      "app_login_change_30d": 25.0075,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -54.2068,
      "upi_share_of_spend": 0.7248,
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
      "days_since_last_transaction": 4,
      "balance_change_30d": 1.2528,
      "transaction_change_30d": 19.596,
      "card_spend_change_30d": 28.9306,
      "app_login_change_30d": 6.3778,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": 7.2647,
      "upi_share_of_spend": 0.6569,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 1,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 32.7627,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-05-01",
      "days_since_last_transaction": 6,
      "balance_change_30d": 36.1324,
      "transaction_change_30d": 21.2844,
      "card_spend_change_30d": 9.8783,
      "app_login_change_30d": 7.0167,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -44.8589,
      "upi_share_of_spend": 0.6669,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 5.5032,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-06-01",
      "days_since_last_transaction": 7,
      "balance_change_30d": -5.2555,
      "transaction_change_30d": -1.8605,
      "card_spend_change_30d": 0.0164,
      "app_login_change_30d": -7.1748,
      "salary_missing_days": 1.0,
      "external_transfer_change_30d": 43.4424,
      "upi_share_of_spend": 0.666,
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
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 2,
    "has_credit_card": 0,
    "has_loan": 1,
    "days_since_last_transaction": 7,
    "balance_change_30d": -5.2555,
    "transaction_change_30d": -1.8605,
    "card_spend_change_30d": 0.0164,
    "app_login_change_30d": -7.1748,
    "salary_missing_days": 1.0,
    "external_transfer_change_30d": 43.4424,
    "upi_share_of_spend": 0.666,
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
      "tenure_months": 147,
      "age": 48,
      "customer_yearly_value": 14107.6675,
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
    "served_at": "2026-08-31T01:13:20",
    "elapsed_ms": 3619.75,
    "timings_ms": {
      "model1": 75.93,
      "model2": 3543.67
    },
    "customer_id": "C10445",
    "customer_name": "Inaya Mukherjee",
    "snapshot_date": "2026-06-01"
  },
  "model1": {
    "churn_probability": 2.53,
    "raw_churn_probability": 23.59,
    "probability_mode": "sigmoid",
    "risk_score": 7.59,
    "churn_prediction": "No",
    "risk_level": "Low",
    "top_risk_factors": [
      {
        "factor": "external_transfer_change_30d_trend_6m",
        "value": 9.053919999999994,
        "message": "External transfers have increased.",
        "contribution": 0.045487772673368454
      },
      {
        "factor": "avg_transaction_change_30d_6m",
        "value": 12.728116666666667,
        "message": "This signal increased churn risk.",
        "contribution": 0.03365663066506386
      },
      {
        "factor": "latest_upi_share_of_spend",
        "value": 0.666,
        "message": "A larger share of spending is happening through UPI.",
        "contribution": 0.027464156970381737
      },
      {
        "factor": "transaction_change_30d_trend_6m",
        "value": -1.1905457142857125,
        "message": "Transaction activity has been falling across recent months.",
        "contribution": 0.016755245625972748
      },
      {
        "factor": "latest_vs_avg_balance_change_30d_available_history",
        "value": -16.328733333333332,
        "message": "Balance has been falling across recent months.",
        "contribution": 0.012296934612095356
      }
    ]
  },
  "model2_input": {
    "customer_context": {
      "age": 48,
      "tenure_months": 147,
      "customer_segment": "salary",
      "income_regularity": "regular",
      "customer_yearly_value": 14107.6675,
      "products_count": 2,
      "has_credit_card": 0,
      "has_loan": 1
    },
    "behavior": {
      "days_since_last_transaction": 7,
      "balance_change_30d": -5.2555,
      "transaction_change_30d": -1.8605,
      "card_spend_change_30d": 0.0164,
      "app_login_change_30d": -7.1748,
      "salary_missing_days": 1,
      "external_transfer_change_30d": 43.4424,
      "upi_share_of_spend": 0.666,
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
      "churn_probability": 0.0253,
      "churn_prediction": "No",
      "risk_level": "Low",
      "top_risk_factors": [
        {
          "factor": "external_transfer_change_30d_trend_6m",
          "value": 9.053919999999994
        },
        {
          "factor": "avg_transaction_change_30d_6m",
          "value": 12.728116666666667
        },
        {
          "factor": "upi_share_of_spend",
          "value": 0.666
        },
        {
          "factor": "transaction_change_30d_trend_6m",
          "value": -1.1905457142857125
        },
        {
          "factor": "vs_avg_balance_change_30d_available_history",
          "value": -16.328733333333332
        }
      ]
    },
    "eligible_actions": [
      "MONITOR",
      "RE_ENGAGEMENT",
      "PRODUCT_REVIEW",
      "FINANCIAL_GUIDANCE",
      "RM_CALLBACK"
    ],
    "case_id": "C10445"
  },
  "model2": {
    "case_id": "C10445",
    "ok": true,
    "prediction": {
      "evidence": [
        "transaction_change_30d=-1.9",
        "balance_change_30d=-5.3",
        "complaints_30d=0",
        "external_transfer_change_30d=43.4",
        "unresolved_complaints=0",
        "avg_transaction_change_30d_6m=12.7",
        "transaction_change_30d_trend_6m=-1.2",
        "complaint_text=None",
        "app_login_change_30d=-7.2"
      ],
      "primary_reason": "UNKNOWN",
      "reasoning_summary": "Evidence is mixed or weak, so the cause remains unknown. The relationship looks stable overall but there are some concerning signals.",
      "recommended_action": "MONITOR",
      "secondary_reasons": [
        "TEMPORARY_SEASONAL_CHANGE",
        "DIGITAL_FRICTION"
      ],
      "urgency": "MEDIUM"
    },
    "raw_text": "{\n    \"evidence\": [\"transaction_change_30d=-1.9\",\"balance_change_30d=-5.3\",\"complaints_30d=0\",\"external_transfer_change_30d=43.4\",\"unresolved_complaints=0\",\"avg_transaction_change_30d_6m=12.7\",\"transaction_change_30d_trend_6m=-1.2\",\"complaint_text=None\",\"app_login_change_30d=-7.2\"],\n    \"primary_reason\": \"UNKNOWN\",\n    \"reasoning_summary\": \"Evidence is mixed or weak, so the cause remains unknown. The relationship looks stable overall but there are some concerning signals.\",\n    \"recommended_action\": \"MONITOR\",\n    \"secondary_reasons\": [\"TEMPORARY_SEASONAL_CHANGE\",\"DIGITAL_FRICTION\"],\n    \"urgency\": \"MEDIUM\"\n}",
    "error": null,
    "latency_s": 3.5434,
    "simple_output": "Reason: UNKNOWN | Urgency: MEDIUM | Action: MONITOR | Why: Evidence is mixed or weak, so the cause remains unknown. The relationship looks stable overall but there are some concerning signals."
  }
}
```

### Nidra Thakkar (`C10646`)

- OK: `True`
- Shape errors: `[]`
- Simple output: Reason: UNKNOWN | Urgency: MEDIUM | Action: MONITOR | Why: Evidence is mixed or weak, so the cause remains unknown. Evidence suggests this because complaints_30d=1; failed_transactions_30d=0.

Request:

```json
{
  "customer_id": "C10646",
  "customer_name": "Nidra Thakkar",
  "prediction_date": "2026-06-01",
  "snapshot_date": "2026-06-01",
  "target_month": "2026-07-01",
  "profile": {
    "tenure_months": 260,
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
      "balance_change_30d": -27.5453,
      "transaction_change_30d": 1.0993,
      "card_spend_change_30d": -7.3999,
      "app_login_change_30d": -37.8573,
      "salary_missing_days": null,
      "external_transfer_change_30d": 56.6202,
      "upi_share_of_spend": 0.1805,
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
      "balance_change_30d": -29.7688,
      "transaction_change_30d": -33.1719,
      "card_spend_change_30d": 0.4527,
      "app_login_change_30d": -35.6349,
      "salary_missing_days": null,
      "external_transfer_change_30d": 42.8605,
      "upi_share_of_spend": 0.253,
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
      "balance_change_30d": -6.9912,
      "transaction_change_30d": -25.1857,
      "card_spend_change_30d": -4.3514,
      "app_login_change_30d": -21.4286,
      "salary_missing_days": null,
      "external_transfer_change_30d": 12.4796,
      "upi_share_of_spend": 0.1561,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 1,
      "failed_transactions_30d": 3,
      "avg_resolution_time_hrs": 34.0192,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-04-01",
      "days_since_last_transaction": 3,
      "balance_change_30d": 11.8278,
      "transaction_change_30d": 2.1309,
      "card_spend_change_30d": 6.1174,
      "app_login_change_30d": -11.1907,
      "salary_missing_days": null,
      "external_transfer_change_30d": 59.9961,
      "upi_share_of_spend": 0.2073,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 0,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 3,
      "avg_resolution_time_hrs": 0.0,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-05-01",
      "days_since_last_transaction": 2,
      "balance_change_30d": 9.2535,
      "transaction_change_30d": -29.5389,
      "card_spend_change_30d": -10.6777,
      "app_login_change_30d": -5.4194,
      "salary_missing_days": null,
      "external_transfer_change_30d": 53.5007,
      "upi_share_of_spend": 0.1634,
      "fd_maturing_in_30d": 1,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 2.025,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-06-01",
      "days_since_last_transaction": 2,
      "balance_change_30d": -2.6053,
      "transaction_change_30d": 13.3474,
      "card_spend_change_30d": -9.3363,
      "app_login_change_30d": -25.3197,
      "salary_missing_days": null,
      "external_transfer_change_30d": 29.6712,
      "upi_share_of_spend": 0.2579,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 18.8927,
      "emi_bounce_30d": 0
    }
  ],
  "customer": {
    "tenure_months": 260,
    "customer_segment": "farmer",
    "income_regularity": "seasonal",
    "products_count": 1,
    "has_credit_card": 0,
    "has_loan": 0,
    "days_since_last_transaction": 2,
    "balance_change_30d": -2.6053,
    "transaction_change_30d": 13.3474,
    "card_spend_change_30d": -9.3363,
    "app_login_change_30d": -25.3197,
    "salary_missing_days": null,
    "external_transfer_change_30d": 29.6712,
    "upi_share_of_spend": 0.2579,
    "fd_maturing_in_30d": 0,
    "products_dropped_90d": 0,
    "complaints_30d": 1,
    "unresolved_complaints": 0,
    "failed_transactions_30d": 0,
    "avg_resolution_time_hrs": 18.8927,
    "emi_bounce_30d": 0
  },
  "extra_context": {
    "customer_profile": {
      "segment": "farmer",
      "income_regularity": "seasonal",
      "tenure_months": 260,
      "age": 52,
      "customer_yearly_value": 53120.033,
      "products_count": 1,
      "has_credit_card": 0,
      "has_loan": 0,
      "value_tier": "medium"
    },
    "recent_complaint_text": "Customer ne bola ki service pehle jaisi nahi rahi. Follow up needed."
  }
}
```

Response:

```json
{
  "meta": {
    "endpoint": "/predict/both",
    "served_at": "2026-08-31T01:13:23",
    "elapsed_ms": 2515.23,
    "timings_ms": {
      "model1": 120.05,
      "model2": 2395.02
    },
    "customer_id": "C10646",
    "customer_name": "Nidra Thakkar",
    "snapshot_date": "2026-06-01"
  },
  "model1": {
    "churn_probability": 2.39,
    "raw_churn_probability": 22.38,
    "probability_mode": "sigmoid",
    "risk_score": 7.18,
    "churn_prediction": "No",
    "risk_level": "Low",
    "top_risk_factors": [
      {
        "factor": "latest_vs_avg_upi_share_of_spend_available_history",
        "value": 0.0548666666666667,
        "message": "A larger share of spending is happening through UPI.",
        "contribution": 0.15991061925888062
      },
      {
        "factor": "sum_fd_maturing_in_30d_3m",
        "value": 1.0,
        "message": "Customer has a fixed deposit maturing soon.",
        "contribution": 0.0776667669415474
      },
      {
        "factor": "avg_external_transfer_change_30d_3m",
        "value": 47.72266666666667,
        "message": "External transfers have increased.",
        "contribution": 0.03243483975529671
      },
      {
        "factor": "avg_upi_share_of_spend_6m",
        "value": 0.20303333333333332,
        "message": "A larger share of spending is happening through UPI.",
        "contribution": 0.023561881855130196
      },
      {
        "factor": "latest_app_login_change_30d",
        "value": -25.3197,
        "message": "App usage has been falling across recent months.",
        "contribution": 0.016546979546546936
      }
    ]
  },
  "model2_input": {
    "customer_context": {
      "age": 52,
      "tenure_months": 260,
      "customer_segment": "farmer",
      "income_regularity": "seasonal",
      "customer_yearly_value": 53120.033,
      "products_count": 1,
      "has_credit_card": 0,
      "has_loan": 0
    },
    "behavior": {
      "days_since_last_transaction": 2,
      "balance_change_30d": -2.6053,
      "transaction_change_30d": 13.3474,
      "card_spend_change_30d": -9.3363,
      "app_login_change_30d": -25.3197,
      "salary_missing_days": null,
      "external_transfer_change_30d": 29.6712,
      "upi_share_of_spend": 0.2579,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "emi_bounce_30d": 0
    },
    "service_evidence": {
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 18.8927,
      "complaint_text": "Customer ne bola ki service pehle jaisi nahi rahi. Follow up needed."
    },
    "model1": {
      "churn_probability": 0.0239,
      "churn_prediction": "No",
      "risk_level": "Low",
      "top_risk_factors": [
        {
          "factor": "vs_avg_upi_share_of_spend_available_history",
          "value": 0.0548666666666667
        },
        {
          "factor": "sum_fd_maturing_in_30d_3m",
          "value": 1.0
        },
        {
          "factor": "avg_external_transfer_change_30d_3m",
          "value": 47.72266666666667
        },
        {
          "factor": "avg_upi_share_of_spend_6m",
          "value": 0.20303333333333332
        },
        {
          "factor": "app_login_change_30d",
          "value": -25.3197
        }
      ]
    },
    "eligible_actions": [
      "MONITOR",
      "RE_ENGAGEMENT",
      "PRODUCT_REVIEW",
      "SERVICE_RECOVERY"
    ],
    "case_id": "C10646"
  },
  "model2": {
    "case_id": "C10646",
    "ok": true,
    "prediction": {
      "evidence": [
        "complaints_30d=1",
        "failed_transactions_30d=0",
        "avg_resolution_time_hrs=18.9",
        "app_login_change_30d=-25.3"
      ],
      "primary_reason": "UNKNOWN",
      "reasoning_summary": "Evidence is mixed or weak, so the cause remains unknown. Evidence suggests this because complaints_30d=1; failed_transactions_30d=0.",
      "recommended_action": "MONITOR",
      "secondary_reasons": [
        "DIGITAL_FRICTION"
      ],
      "urgency": "MEDIUM"
    },
    "raw_text": "{\"evidence\":[\"complaints_30d=1\",\"failed_transactions_30d=0\",\"avg_resolution_time_hrs=18.9\",\"app_login_change_30d=-25.3\"],\"primary_reason\":\"UNKNOWN\",\"reasoning_summary\":\"Evidence is mixed or weak, so the cause remains unknown. Evidence suggests this because complaints_30d=1; failed_transactions_30d=0.\",\"recommended_action\":\"MONITOR\",\"secondary_reasons\":[\"DIGITAL_FRICTION\"],\"urgency\":\"MEDIUM\"}",
    "error": null,
    "latency_s": 2.3938,
    "simple_output": "Reason: UNKNOWN | Urgency: MEDIUM | Action: MONITOR | Why: Evidence is mixed or weak, so the cause remains unknown. Evidence suggests this because complaints_30d=1; failed_transactions_30d=0."
  }
}
```

### Geetika Mitter (`C11080`)

- OK: `True`
- Shape errors: `[]`
- Simple output: Reason: SERVICE_DISSATISFACTION | Urgency: HIGH | Action: COMPLAINT_ESCALATION | Why: Service friction is the clearest risk signal here. Complaint escalation fits because complaint_text points to a service issue and avg_resolution_time_hrs=22.8 point to a serious or unresolved service problem.

Request:

```json
{
  "customer_id": "C11080",
  "customer_name": "Geetika Mitter",
  "prediction_date": "2026-03-01",
  "snapshot_date": "2026-03-01",
  "target_month": "2026-04-01",
  "profile": {
    "tenure_months": 26,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 3,
    "has_credit_card": 1,
    "has_loan": 1
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 12,
      "balance_change_30d": -6.1021,
      "transaction_change_30d": 26.9575,
      "card_spend_change_30d": 13.6015,
      "app_login_change_30d": 11.5132,
      "salary_missing_days": 3.0,
      "external_transfer_change_30d": 23.0147,
      "upi_share_of_spend": 0.3236,
      "fd_maturing_in_30d": 1,
      "products_dropped_90d": 0,
      "complaints_30d": 0,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 3,
      "avg_resolution_time_hrs": 0.0,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-02-01",
      "days_since_last_transaction": 14,
      "balance_change_30d": -11.9453,
      "transaction_change_30d": -34.1201,
      "card_spend_change_30d": -16.4651,
      "app_login_change_30d": -43.5567,
      "salary_missing_days": 4.0,
      "external_transfer_change_30d": 60.2503,
      "upi_share_of_spend": 0.3209,
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
      "days_since_last_transaction": 22,
      "balance_change_30d": -36.0205,
      "transaction_change_30d": -39.7736,
      "card_spend_change_30d": -37.8579,
      "app_login_change_30d": 1.2586,
      "salary_missing_days": 5.0,
      "external_transfer_change_30d": 20.0974,
      "upi_share_of_spend": 0.4998,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 1,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 4,
      "avg_resolution_time_hrs": 22.8199,
      "emi_bounce_30d": 0
    }
  ],
  "customer": {
    "tenure_months": 26,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 3,
    "has_credit_card": 1,
    "has_loan": 1,
    "days_since_last_transaction": 22,
    "balance_change_30d": -36.0205,
    "transaction_change_30d": -39.7736,
    "card_spend_change_30d": -37.8579,
    "app_login_change_30d": 1.2586,
    "salary_missing_days": 5.0,
    "external_transfer_change_30d": 20.0974,
    "upi_share_of_spend": 0.4998,
    "fd_maturing_in_30d": 0,
    "products_dropped_90d": 1,
    "complaints_30d": 1,
    "unresolved_complaints": 0,
    "failed_transactions_30d": 4,
    "avg_resolution_time_hrs": 22.8199,
    "emi_bounce_30d": 0
  },
  "extra_context": {
    "customer_profile": {
      "segment": "salary",
      "income_regularity": "regular",
      "tenure_months": 26,
      "age": 29,
      "customer_yearly_value": 96861.7461,
      "products_count": 3,
      "has_credit_card": 1,
      "has_loan": 1,
      "value_tier": "high"
    },
    "recent_complaint_text": "Account transfer to new branch is taking more than two months."
  }
}
```

Response:

```json
{
  "meta": {
    "endpoint": "/predict/both",
    "served_at": "2026-08-31T01:13:30",
    "elapsed_ms": 7175.06,
    "timings_ms": {
      "model1": 164.33,
      "model2": 7010.54
    },
    "customer_id": "C11080",
    "customer_name": "Geetika Mitter",
    "snapshot_date": "2026-03-01"
  },
  "model1": {
    "churn_probability": 39.84,
    "raw_churn_probability": 93.17,
    "probability_mode": "sigmoid",
    "risk_score": 77.44,
    "churn_prediction": "Yes",
    "risk_level": "High",
    "top_risk_factors": [
      {
        "factor": "latest_days_since_last_transaction",
        "value": 22,
        "message": "Customer has gone longer without transacting.",
        "contribution": 0.5586290955543518
      },
      {
        "factor": "latest_transaction_change_30d",
        "value": -39.7736,
        "message": "Transaction activity has been falling across recent months.",
        "contribution": 0.37199488282203674
      },
      {
        "factor": "latest_salary_missing_days",
        "value": 5.0,
        "message": "Salary or pension was delayed recently.",
        "contribution": 0.22317220270633698
      },
      {
        "factor": "latest_balance_change_30d",
        "value": -36.0205,
        "message": "Balance has been falling across recent months.",
        "contribution": 0.21425633132457733
      },
      {
        "factor": "latest_vs_avg_upi_share_of_spend_available_history",
        "value": 0.11836666666666668,
        "message": "A larger share of spending is happening through UPI.",
        "contribution": 0.1866704225540161
      }
    ]
  },
  "model2_input": {
    "customer_context": {
      "age": 29,
      "tenure_months": 26,
      "customer_segment": "salary",
      "income_regularity": "regular",
      "customer_yearly_value": 96861.7461,
      "products_count": 3,
      "has_credit_card": 1,
      "has_loan": 1
    },
    "behavior": {
      "days_since_last_transaction": 22,
      "balance_change_30d": -36.0205,
      "transaction_change_30d": -39.7736,
      "card_spend_change_30d": -37.8579,
      "app_login_change_30d": 1.2586,
      "salary_missing_days": 5,
      "external_transfer_change_30d": 20.0974,
      "upi_share_of_spend": 0.4998,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 1,
      "emi_bounce_30d": 0
    },
    "service_evidence": {
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 4,
      "avg_resolution_time_hrs": 22.8199,
      "complaint_text": "Account transfer to new branch is taking more than two months."
    },
    "model1": {
      "churn_probability": 0.3984,
      "churn_prediction": "Yes",
      "risk_level": "High",
      "top_risk_factors": [
        {
          "factor": "days_since_last_transaction",
          "value": 22
        },
        {
          "factor": "transaction_change_30d",
          "value": -39.7736
        },
        {
          "factor": "salary_missing_days",
          "value": 5.0
        },
        {
          "factor": "balance_change_30d",
          "value": -36.0205
        },
        {
          "factor": "vs_avg_upi_share_of_spend_available_history",
          "value": 0.11836666666666668
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
    "case_id": "C11080"
  },
  "model2": {
    "case_id": "C11080",
    "ok": true,
    "prediction": {
      "evidence": [
        "complaint_text points to a service issue",
        "avg_resolution_time_hrs=22.8",
        "complaints_30d=1"
      ],
      "primary_reason": "SERVICE_DISSATISFACTION",
      "reasoning_summary": "Service friction is the clearest risk signal here. Complaint escalation fits because complaint_text points to a service issue and avg_resolution_time_hrs=22.8 point to a serious or unresolved service problem.",
      "recommended_action": "COMPLAINT_ESCALATION",
      "secondary_reasons": [
        "UNKNOWN"
      ],
      "urgency": "HIGH"
    },
    "raw_text": "{\"evidence\":[\"complaint_text points to a service issue\",\"avg_resolution_time_hrs=22.8\",\"complaints_30d=1\"],\"primary_reason\":\"SERVICE_DISSATISFACTION\",\"reasoning_summary\":\"Service friction is the clearest risk signal here. Complaint escalation fits because complaint_text points to a service issue and avg_resolution_time_hrs=22.8 point to a serious or unresolved service problem.\",\"recommended_action\":\"COMPLAINT_ESCALATION\",\"secondary_reasons\":[\"UNKNOWN\"],\"urgency\":\"HIGH\"}",
    "error": null,
    "latency_s": 7.01,
    "simple_output": "Reason: SERVICE_DISSATISFACTION | Urgency: HIGH | Action: COMPLAINT_ESCALATION | Why: Service friction is the clearest risk signal here. Complaint escalation fits because complaint_text points to a service issue and avg_resolution_time_hrs=22.8 point to a serious or unresolved service problem."
  }
}
```

### Jagat Karpe (`C11383`)

- OK: `True`
- Shape errors: `[]`
- Simple output: Reason: SERVICE_DISSATISFACTION | Urgency: MEDIUM | Action: SERVICE_RECOVERY | Why: Service friction is the clearest risk signal here. Complaint escalation fits because complaints_30d=1 and failed_transactions_30d=2 indicate the issue is unresolved or operationally serious.

Request:

```json
{
  "customer_id": "C11383",
  "customer_name": "Jagat Karpe",
  "prediction_date": "2026-06-01",
  "snapshot_date": "2026-06-01",
  "target_month": "2026-07-01",
  "profile": {
    "tenure_months": 101,
    "customer_segment": "business",
    "income_regularity": "irregular",
    "products_count": 2,
    "has_credit_card": 0,
    "has_loan": 1
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 0,
      "balance_change_30d": 25.5868,
      "transaction_change_30d": -1.229,
      "card_spend_change_30d": 7.4073,
      "app_login_change_30d": 15.602,
      "salary_missing_days": null,
      "external_transfer_change_30d": -33.8238,
      "upi_share_of_spend": 0.392,
      "fd_maturing_in_30d": 1,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 6.6473,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-02-01",
      "days_since_last_transaction": 0,
      "balance_change_30d": 27.6254,
      "transaction_change_30d": 26.7195,
      "card_spend_change_30d": 24.1026,
      "app_login_change_30d": 16.7973,
      "salary_missing_days": null,
      "external_transfer_change_30d": 16.9743,
      "upi_share_of_spend": 0.4135,
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
      "balance_change_30d": 27.9641,
      "transaction_change_30d": 13.1447,
      "card_spend_change_30d": 15.5765,
      "app_login_change_30d": 1.8588,
      "salary_missing_days": null,
      "external_transfer_change_30d": -29.4054,
      "upi_share_of_spend": 0.3593,
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
      "balance_change_30d": 58.4141,
      "transaction_change_30d": 46.2048,
      "card_spend_change_30d": 62.9426,
      "app_login_change_30d": 47.7141,
      "salary_missing_days": null,
      "external_transfer_change_30d": -4.0565,
      "upi_share_of_spend": 0.2517,
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
      "balance_change_30d": 18.8781,
      "transaction_change_30d": 8.9819,
      "card_spend_change_30d": -8.3782,
      "app_login_change_30d": 0.6689,
      "salary_missing_days": null,
      "external_transfer_change_30d": 16.5152,
      "upi_share_of_spend": 0.3861,
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
      "days_since_last_transaction": 1,
      "balance_change_30d": 12.9161,
      "transaction_change_30d": -0.2397,
      "card_spend_change_30d": 28.1655,
      "app_login_change_30d": -16.1491,
      "salary_missing_days": null,
      "external_transfer_change_30d": 9.1544,
      "upi_share_of_spend": 0.4402,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 2,
      "avg_resolution_time_hrs": 25.703,
      "emi_bounce_30d": 0
    }
  ],
  "customer": {
    "tenure_months": 101,
    "customer_segment": "business",
    "income_regularity": "irregular",
    "products_count": 2,
    "has_credit_card": 0,
    "has_loan": 1,
    "days_since_last_transaction": 1,
    "balance_change_30d": 12.9161,
    "transaction_change_30d": -0.2397,
    "card_spend_change_30d": 28.1655,
    "app_login_change_30d": -16.1491,
    "salary_missing_days": null,
    "external_transfer_change_30d": 9.1544,
    "upi_share_of_spend": 0.4402,
    "fd_maturing_in_30d": 0,
    "products_dropped_90d": 0,
    "complaints_30d": 1,
    "unresolved_complaints": 0,
    "failed_transactions_30d": 2,
    "avg_resolution_time_hrs": 25.703,
    "emi_bounce_30d": 0
  },
  "extra_context": {
    "customer_profile": {
      "segment": "business",
      "income_regularity": "irregular",
      "tenure_months": 101,
      "age": 43,
      "customer_yearly_value": 76437.7635,
      "products_count": 2,
      "has_credit_card": 0,
      "has_loan": 1,
      "value_tier": "medium"
    },
    "recent_complaint_text": "I have raised this three times. Nobody calls back. Extremely frustrating."
  }
}
```

Response:

```json
{
  "meta": {
    "endpoint": "/predict/both",
    "served_at": "2026-08-31T01:13:33",
    "elapsed_ms": 2856.46,
    "timings_ms": {
      "model1": 129.81,
      "model2": 2726.51
    },
    "customer_id": "C11383",
    "customer_name": "Jagat Karpe",
    "snapshot_date": "2026-06-01"
  },
  "model1": {
    "churn_probability": 3.27,
    "raw_churn_probability": 29.27,
    "probability_mode": "sigmoid",
    "risk_score": 9.81,
    "churn_prediction": "No",
    "risk_level": "Low",
    "top_risk_factors": [
      {
        "factor": "latest_vs_avg_upi_share_of_spend_available_history",
        "value": 0.06640000000000001,
        "message": "A larger share of spending is happening through UPI.",
        "contribution": 0.1801825761795044
      },
      {
        "factor": "avg_balance_change_30d_6m",
        "value": 28.564099999999996,
        "message": "This signal increased churn risk.",
        "contribution": 0.17922532558441162
      },
      {
        "factor": "avg_transaction_change_30d_6m",
        "value": 15.597033333333334,
        "message": "This signal increased churn risk.",
        "contribution": 0.0419229157269001
      },
      {
        "factor": "transaction_change_30d_trend_6m",
        "value": -0.4344628571428565,
        "message": "Transaction activity has been falling across recent months.",
        "contribution": 0.03507334366440773
      },
      {
        "factor": "latest_vs_avg_balance_change_30d_available_history",
        "value": -15.647999999999996,
        "message": "Balance has been falling across recent months.",
        "contribution": 0.029896922409534454
      }
    ]
  },
  "model2_input": {
    "customer_context": {
      "age": 43,
      "tenure_months": 101,
      "customer_segment": "business",
      "income_regularity": "irregular",
      "customer_yearly_value": 76437.7635,
      "products_count": 2,
      "has_credit_card": 0,
      "has_loan": 1
    },
    "behavior": {
      "days_since_last_transaction": 1,
      "balance_change_30d": 12.9161,
      "transaction_change_30d": -0.2397,
      "card_spend_change_30d": 28.1655,
      "app_login_change_30d": -16.1491,
      "salary_missing_days": null,
      "external_transfer_change_30d": 9.1544,
      "upi_share_of_spend": 0.4402,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "emi_bounce_30d": 0
    },
    "service_evidence": {
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 2,
      "avg_resolution_time_hrs": 25.703,
      "complaint_text": "I have raised this three times. Nobody calls back. Extremely frustrating."
    },
    "model1": {
      "churn_probability": 0.0327,
      "churn_prediction": "No",
      "risk_level": "Low",
      "top_risk_factors": [
        {
          "factor": "vs_avg_upi_share_of_spend_available_history",
          "value": 0.06640000000000001
        },
        {
          "factor": "avg_balance_change_30d_6m",
          "value": 28.564099999999996
        },
        {
          "factor": "avg_transaction_change_30d_6m",
          "value": 15.597033333333334
        },
        {
          "factor": "transaction_change_30d_trend_6m",
          "value": -0.4344628571428565
        },
        {
          "factor": "vs_avg_balance_change_30d_available_history",
          "value": -15.647999999999996
        }
      ]
    },
    "eligible_actions": [
      "MONITOR",
      "RE_ENGAGEMENT",
      "PRODUCT_REVIEW",
      "SERVICE_RECOVERY"
    ],
    "case_id": "C11383"
  },
  "model2": {
    "case_id": "C11383",
    "ok": true,
    "prediction": {
      "evidence": [
        "complaints_30d=1",
        "failed_transactions_30d=2",
        "avg_resolution_time_hrs=25.7",
        "complaint_text describes a recent service issue"
      ],
      "primary_reason": "SERVICE_DISSATISFACTION",
      "reasoning_summary": "Service friction is the clearest risk signal here. Complaint escalation fits because complaints_30d=1 and failed_transactions_30d=2 indicate the issue is unresolved or operationally serious.",
      "recommended_action": "SERVICE_RECOVERY",
      "secondary_reasons": [
        "UNKNOWN"
      ],
      "urgency": "MEDIUM"
    },
    "raw_text": "{\n\"evidence\":[\"complaints_30d=1\",\"failed_transactions_30d=2\",\"avg_resolution_time_hrs=25.7\",\"complaint_text describes a recent service issue\"],\"primary_reason\":\"SERVICE_DISSATISFACTION\",\"reasoning_summary\":\"Service friction is the clearest risk signal here. Complaint escalation fits because complaints_30d=1 and failed_transactions_30d=2 indicate the issue is unresolved or operationally serious.\",\"recommended_action\":\"SERVICE_RECOVERY\",\"secondary_reasons\":[\"UNKNOWN\"],\"urgency\":\"MEDIUM\"\n}",
    "error": null,
    "latency_s": 2.7261,
    "simple_output": "Reason: SERVICE_DISSATISFACTION | Urgency: MEDIUM | Action: SERVICE_RECOVERY | Why: Service friction is the clearest risk signal here. Complaint escalation fits because complaints_30d=1 and failed_transactions_30d=2 indicate the issue is unresolved or operationally serious."
  }
}
```

### Meghana Kibe (`C11525`)

- OK: `True`
- Shape errors: `[]`
- Simple output: Reason: SERVICE_DISSATISFACTION | Urgency: MEDIUM | Action: SERVICE_RECOVERY | Why: Service friction is the clearest risk signal here given complaints_30d=1 and avg_resolution_time_hrs=34.4.

Request:

```json
{
  "customer_id": "C11525",
  "customer_name": "Meghana Kibe",
  "prediction_date": "2026-06-01",
  "snapshot_date": "2026-06-01",
  "target_month": "2026-07-01",
  "profile": {
    "tenure_months": 99,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 3,
    "has_credit_card": 1,
    "has_loan": 1
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 0,
      "balance_change_30d": -10.6912,
      "transaction_change_30d": -22.8909,
      "card_spend_change_30d": 15.4391,
      "app_login_change_30d": 16.6752,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -16.4713,
      "upi_share_of_spend": 0.3713,
      "fd_maturing_in_30d": 1,
      "products_dropped_90d": 1,
      "complaints_30d": 0,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 0.0,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-02-01",
      "days_since_last_transaction": 2,
      "balance_change_30d": -17.146,
      "transaction_change_30d": -27.5067,
      "card_spend_change_30d": -10.2223,
      "app_login_change_30d": -35.6179,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -15.4878,
      "upi_share_of_spend": 0.3649,
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
      "balance_change_30d": -3.9086,
      "transaction_change_30d": 8.5711,
      "card_spend_change_30d": 38.8188,
      "app_login_change_30d": 13.5572,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -18.9421,
      "upi_share_of_spend": 0.2651,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 11.6928,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-04-01",
      "days_since_last_transaction": 0,
      "balance_change_30d": 15.4349,
      "transaction_change_30d": 18.7316,
      "card_spend_change_30d": 29.8854,
      "app_login_change_30d": 38.0897,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -20.6022,
      "upi_share_of_spend": 0.3046,
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
      "balance_change_30d": 28.8833,
      "transaction_change_30d": 11.0954,
      "card_spend_change_30d": -2.281,
      "app_login_change_30d": 6.3637,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": 30.5984,
      "upi_share_of_spend": 0.3221,
      "fd_maturing_in_30d": 1,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 13.2191,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-06-01",
      "days_since_last_transaction": 0,
      "balance_change_30d": -2.5303,
      "transaction_change_30d": -3.5827,
      "card_spend_change_30d": 43.2625,
      "app_login_change_30d": -12.1998,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": 30.1545,
      "upi_share_of_spend": 0.3999,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 34.3785,
      "emi_bounce_30d": 0
    }
  ],
  "customer": {
    "tenure_months": 99,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 3,
    "has_credit_card": 1,
    "has_loan": 1,
    "days_since_last_transaction": 0,
    "balance_change_30d": -2.5303,
    "transaction_change_30d": -3.5827,
    "card_spend_change_30d": 43.2625,
    "app_login_change_30d": -12.1998,
    "salary_missing_days": 0.0,
    "external_transfer_change_30d": 30.1545,
    "upi_share_of_spend": 0.3999,
    "fd_maturing_in_30d": 0,
    "products_dropped_90d": 0,
    "complaints_30d": 1,
    "unresolved_complaints": 0,
    "failed_transactions_30d": 0,
    "avg_resolution_time_hrs": 34.3785,
    "emi_bounce_30d": 0
  },
  "extra_context": {
    "customer_profile": {
      "segment": "salary",
      "income_regularity": "regular",
      "tenure_months": 99,
      "age": 50,
      "customer_yearly_value": 32117.2664,
      "products_count": 3,
      "has_credit_card": 1,
      "has_loan": 1,
      "value_tier": "low"
    },
    "recent_complaint_text": "Bounce charges of Rs 590 levied though the fault was at bank side."
  }
}
```

Response:

```json
{
  "meta": {
    "endpoint": "/predict/both",
    "served_at": "2026-08-31T01:13:35",
    "elapsed_ms": 2345.9,
    "timings_ms": {
      "model1": 120.08,
      "model2": 2225.59
    },
    "customer_id": "C11525",
    "customer_name": "Meghana Kibe",
    "snapshot_date": "2026-06-01"
  },
  "model1": {
    "churn_probability": 3.28,
    "raw_churn_probability": 29.32,
    "probability_mode": "sigmoid",
    "risk_score": 9.83,
    "churn_prediction": "No",
    "risk_level": "Low",
    "top_risk_factors": [
      {
        "factor": "latest_avg_resolution_time_hrs",
        "value": 34.3785,
        "message": "Recent complaints took longer to resolve.",
        "contribution": 0.22974669933319092
      },
      {
        "factor": "latest_vs_avg_upi_share_of_spend_available_history",
        "value": 0.06191666666666662,
        "message": "A larger share of spending is happening through UPI.",
        "contribution": 0.15791474282741547
      },
      {
        "factor": "sum_fd_maturing_in_30d_3m",
        "value": 1.0,
        "message": "Customer has a fixed deposit maturing soon.",
        "contribution": 0.09229912608861923
      },
      {
        "factor": "external_transfer_change_30d_trend_6m",
        "value": 10.563642857142856,
        "message": "External transfers have increased.",
        "contribution": 0.021774834021925926
      },
      {
        "factor": "sum_fd_maturing_in_30d_6m",
        "value": 2.0,
        "message": "Customer has a fixed deposit maturing soon.",
        "contribution": 0.016627894714474678
      }
    ]
  },
  "model2_input": {
    "customer_context": {
      "age": 50,
      "tenure_months": 99,
      "customer_segment": "salary",
      "income_regularity": "regular",
      "customer_yearly_value": 32117.2664,
      "products_count": 3,
      "has_credit_card": 1,
      "has_loan": 1
    },
    "behavior": {
      "days_since_last_transaction": 0,
      "balance_change_30d": -2.5303,
      "transaction_change_30d": -3.5827,
      "card_spend_change_30d": 43.2625,
      "app_login_change_30d": -12.1998,
      "salary_missing_days": 0,
      "external_transfer_change_30d": 30.1545,
      "upi_share_of_spend": 0.3999,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "emi_bounce_30d": 0
    },
    "service_evidence": {
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 34.3785,
      "complaint_text": "Bounce charges of Rs 590 levied though the fault was at bank side."
    },
    "model1": {
      "churn_probability": 0.0328,
      "churn_prediction": "No",
      "risk_level": "Low",
      "top_risk_factors": [
        {
          "factor": "avg_resolution_time_hrs",
          "value": 34.3785
        },
        {
          "factor": "vs_avg_upi_share_of_spend_available_history",
          "value": 0.06191666666666662
        },
        {
          "factor": "sum_fd_maturing_in_30d_3m",
          "value": 1.0
        },
        {
          "factor": "external_transfer_change_30d_trend_6m",
          "value": 10.563642857142856
        },
        {
          "factor": "sum_fd_maturing_in_30d_6m",
          "value": 2.0
        }
      ]
    },
    "eligible_actions": [
      "MONITOR",
      "RE_ENGAGEMENT",
      "PRODUCT_REVIEW",
      "SERVICE_RECOVERY"
    ],
    "case_id": "C11525"
  },
  "model2": {
    "case_id": "C11525",
    "ok": true,
    "prediction": {
      "evidence": [
        "complaints_30d=1",
        "avg_resolution_time_hrs=34.4",
        "secondary_reasons=[SERVICE_DISSATISFACTION]"
      ],
      "primary_reason": "SERVICE_DISSATISFACTION",
      "reasoning_summary": "Service friction is the clearest risk signal here given complaints_30d=1 and avg_resolution_time_hrs=34.4.",
      "recommended_action": "SERVICE_RECOVERY",
      "secondary_reasons": [
        "UNKNOWN"
      ],
      "urgency": "MEDIUM"
    },
    "raw_text": "{\"evidence\":[\"complaints_30d=1\",\"avg_resolution_time_hrs=34.4\",\"secondary_reasons=[SERVICE_DISSATISFACTION]\"],\"primary_reason\":\"SERVICE_DISSATISFACTION\",\"reasoning_summary\":\"Service friction is the clearest risk signal here given complaints_30d=1 and avg_resolution_time_hrs=34.4.\",\"recommended_action\":\"SERVICE_RECOVERY\",\"secondary_reasons\":[\"UNKNOWN\"],\"urgency\":\"MEDIUM\"}",
    "error": null,
    "latency_s": 2.2253,
    "simple_output": "Reason: SERVICE_DISSATISFACTION | Urgency: MEDIUM | Action: SERVICE_RECOVERY | Why: Service friction is the clearest risk signal here given complaints_30d=1 and avg_resolution_time_hrs=34.4."
  }
}
```

### Ekani Iyer (`C11749`)

- OK: `True`
- Shape errors: `[]`
- Simple output: Reason: SERVICE_DISSATISFACTION | Urgency: HIGH | Action: COMPLAINT_ESCALATION | Why: Service friction is the clearest risk signal here. Complaint escalation fits because complaints_30d=1 and unresolved_complaints=1 indicate the issue is unresolved or operationally serious.

Request:

```json
{
  "customer_id": "C11749",
  "customer_name": "Ekani Iyer",
  "prediction_date": "2026-06-01",
  "snapshot_date": "2026-06-01",
  "target_month": "2026-07-01",
  "profile": {
    "tenure_months": 27,
    "customer_segment": "business",
    "income_regularity": "irregular",
    "products_count": 3,
    "has_credit_card": 1,
    "has_loan": 1
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 8,
      "balance_change_30d": -17.3104,
      "transaction_change_30d": 5.5547,
      "card_spend_change_30d": -3.6908,
      "app_login_change_30d": -6.1043,
      "salary_missing_days": null,
      "external_transfer_change_30d": -9.8673,
      "upi_share_of_spend": 0.2518,
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
      "days_since_last_transaction": 18,
      "balance_change_30d": -16.9502,
      "transaction_change_30d": -8.6352,
      "card_spend_change_30d": 2.4903,
      "app_login_change_30d": -31.2036,
      "salary_missing_days": null,
      "external_transfer_change_30d": 33.4619,
      "upi_share_of_spend": 0.4671,
      "fd_maturing_in_30d": 1,
      "products_dropped_90d": 0,
      "complaints_30d": 0,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 0.0,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-03-01",
      "days_since_last_transaction": 15,
      "balance_change_30d": -20.8408,
      "transaction_change_30d": -18.7657,
      "card_spend_change_30d": -0.2986,
      "app_login_change_30d": -22.1204,
      "salary_missing_days": null,
      "external_transfer_change_30d": 54.0774,
      "upi_share_of_spend": 0.4287,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 3,
      "avg_resolution_time_hrs": 5.4353,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-04-01",
      "days_since_last_transaction": 15,
      "balance_change_30d": -10.947,
      "transaction_change_30d": -0.7743,
      "card_spend_change_30d": -17.3781,
      "app_login_change_30d": -9.8423,
      "salary_missing_days": null,
      "external_transfer_change_30d": 13.1765,
      "upi_share_of_spend": 0.4156,
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
      "days_since_last_transaction": 13,
      "balance_change_30d": -8.9996,
      "transaction_change_30d": -21.2314,
      "card_spend_change_30d": 17.372,
      "app_login_change_30d": -2.0446,
      "salary_missing_days": null,
      "external_transfer_change_30d": 34.7581,
      "upi_share_of_spend": 0.3429,
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
      "days_since_last_transaction": 19,
      "balance_change_30d": -25.7841,
      "transaction_change_30d": -37.9404,
      "card_spend_change_30d": -28.0847,
      "app_login_change_30d": -19.4357,
      "salary_missing_days": null,
      "external_transfer_change_30d": 44.5254,
      "upi_share_of_spend": 0.3686,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 1,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 31.3772,
      "emi_bounce_30d": 0
    }
  ],
  "customer": {
    "tenure_months": 27,
    "customer_segment": "business",
    "income_regularity": "irregular",
    "products_count": 3,
    "has_credit_card": 1,
    "has_loan": 1,
    "days_since_last_transaction": 19,
    "balance_change_30d": -25.7841,
    "transaction_change_30d": -37.9404,
    "card_spend_change_30d": -28.0847,
    "app_login_change_30d": -19.4357,
    "salary_missing_days": null,
    "external_transfer_change_30d": 44.5254,
    "upi_share_of_spend": 0.3686,
    "fd_maturing_in_30d": 0,
    "products_dropped_90d": 0,
    "complaints_30d": 1,
    "unresolved_complaints": 1,
    "failed_transactions_30d": 0,
    "avg_resolution_time_hrs": 31.3772,
    "emi_bounce_30d": 0
  },
  "extra_context": {
    "customer_profile": {
      "segment": "business",
      "income_regularity": "irregular",
      "tenure_months": 27,
      "age": 46,
      "customer_yearly_value": 116451.4621,
      "products_count": 3,
      "has_credit_card": 1,
      "has_loan": 1,
      "value_tier": "high"
    },
    "recent_complaint_text": "Card cloned and used at some other city. Why no SMS alert came?"
  }
}
```

Response:

```json
{
  "meta": {
    "endpoint": "/predict/both",
    "served_at": "2026-08-31T01:13:43",
    "elapsed_ms": 7888.25,
    "timings_ms": {
      "model1": 195.85,
      "model2": 7692.24
    },
    "customer_id": "C11749",
    "customer_name": "Ekani Iyer",
    "snapshot_date": "2026-06-01"
  },
  "model1": {
    "churn_probability": 32.26,
    "raw_churn_probability": 86.08,
    "probability_mode": "sigmoid",
    "risk_score": 74.6,
    "churn_prediction": "Yes",
    "risk_level": "High",
    "top_risk_factors": [
      {
        "factor": "latest_days_since_last_transaction",
        "value": 19,
        "message": "Customer has gone longer without transacting.",
        "contribution": 0.7402741312980652
      },
      {
        "factor": "latest_transaction_change_30d",
        "value": -37.9404,
        "message": "Transaction activity has been falling across recent months.",
        "contribution": 0.4116789400577545
      },
      {
        "factor": "days_since_last_transaction_trend_6m",
        "value": 1.1428571428571426,
        "message": "Customer has gone longer without transacting.",
        "contribution": 0.17090237140655518
      },
      {
        "factor": "latest_balance_change_30d",
        "value": -25.7841,
        "message": "Balance has been falling across recent months.",
        "contribution": 0.1645648032426834
      },
      {
        "factor": "latest_avg_resolution_time_hrs",
        "value": 31.3772,
        "message": "Recent complaints took longer to resolve.",
        "contribution": 0.08202529698610306
      }
    ]
  },
  "model2_input": {
    "customer_context": {
      "age": 46,
      "tenure_months": 27,
      "customer_segment": "business",
      "income_regularity": "irregular",
      "customer_yearly_value": 116451.4621,
      "products_count": 3,
      "has_credit_card": 1,
      "has_loan": 1
    },
    "behavior": {
      "days_since_last_transaction": 19,
      "balance_change_30d": -25.7841,
      "transaction_change_30d": -37.9404,
      "card_spend_change_30d": -28.0847,
      "app_login_change_30d": -19.4357,
      "salary_missing_days": null,
      "external_transfer_change_30d": 44.5254,
      "upi_share_of_spend": 0.3686,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "emi_bounce_30d": 0
    },
    "service_evidence": {
      "complaints_30d": 1,
      "unresolved_complaints": 1,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 31.3772,
      "complaint_text": "Card cloned and used at some other city. Why no SMS alert came?"
    },
    "model1": {
      "churn_probability": 0.3226,
      "churn_prediction": "Yes",
      "risk_level": "High",
      "top_risk_factors": [
        {
          "factor": "days_since_last_transaction",
          "value": 19
        },
        {
          "factor": "transaction_change_30d",
          "value": -37.9404
        },
        {
          "factor": "days_since_last_transaction_trend_6m",
          "value": 1.1428571428571426
        },
        {
          "factor": "balance_change_30d",
          "value": -25.7841
        },
        {
          "factor": "avg_resolution_time_hrs",
          "value": 31.3772
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
    "case_id": "C11749"
  },
  "model2": {
    "case_id": "C11749",
    "ok": true,
    "prediction": {
      "evidence": [
        "complaints_30d=1",
        "unresolved_complaints=1",
        "avg_resolution_time_hrs=31.4",
        "complaint_text describes a recent service issue"
      ],
      "primary_reason": "SERVICE_DISSATISFACTION",
      "reasoning_summary": "Service friction is the clearest risk signal here. Complaint escalation fits because complaints_30d=1 and unresolved_complaints=1 indicate the issue is unresolved or operationally serious.",
      "recommended_action": "COMPLAINT_ESCALATION",
      "secondary_reasons": [
        "UNKNOWN"
      ],
      "urgency": "HIGH"
    },
    "raw_text": "{\"evidence\":[\"complaints_30d=1\",\"unresolved_complaints=1\",\"avg_resolution_time_hrs=31.4\",\"complaint_text describes a recent service issue\"],\"primary_reason\":\"SERVICE_DISSATISFACTION\",\"reasoning_summary\":\"Service friction is the clearest risk signal here. Complaint escalation fits because complaints_30d=1 and unresolved_complaints=1 indicate the issue is unresolved or operationally serious.\",\"recommended_action\":\"COMPLAINT_ESCALATION\",\"secondary_reasons\":[\"UNKNOWN\"],\"urgency\":\"HIGH\"}",
    "error": null,
    "latency_s": 7.6918,
    "simple_output": "Reason: SERVICE_DISSATISFACTION | Urgency: HIGH | Action: COMPLAINT_ESCALATION | Why: Service friction is the clearest risk signal here. Complaint escalation fits because complaints_30d=1 and unresolved_complaints=1 indicate the issue is unresolved or operationally serious."
  }
}
```

### Vedika Wagle (`C12000`)

- OK: `True`
- Shape errors: `[]`
- Simple output: Reason: UNKNOWN | Urgency: MEDIUM | Action: MONITOR | Why: Evidence is mixed or weak, so the cause remains unknown. Evidence suggests this because complaints_30d=0; failed_transactions_30d=2.

Request:

```json
{
  "customer_id": "C12000",
  "customer_name": "Vedika Wagle",
  "prediction_date": "2026-06-01",
  "snapshot_date": "2026-06-01",
  "target_month": "2026-07-01",
  "profile": {
    "tenure_months": 75,
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
      "balance_change_30d": 7.0333,
      "transaction_change_30d": 13.3049,
      "card_spend_change_30d": 11.3708,
      "app_login_change_30d": 17.364,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": 9.8662,
      "upi_share_of_spend": 0.3045,
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
      "days_since_last_transaction": 10,
      "balance_change_30d": 1.1406,
      "transaction_change_30d": -4.1262,
      "card_spend_change_30d": 1.2214,
      "app_login_change_30d": -12.4551,
      "salary_missing_days": 1.0,
      "external_transfer_change_30d": -2.734,
      "upi_share_of_spend": 0.4473,
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
      "days_since_last_transaction": 15,
      "balance_change_30d": 7.4639,
      "transaction_change_30d": 5.2004,
      "card_spend_change_30d": -14.4598,
      "app_login_change_30d": -24.6939,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -8.0395,
      "upi_share_of_spend": 0.4153,
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
      "days_since_last_transaction": 14,
      "balance_change_30d": 2.4933,
      "transaction_change_30d": -10.388,
      "card_spend_change_30d": 9.3597,
      "app_login_change_30d": 13.7799,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": 22.7847,
      "upi_share_of_spend": 0.3445,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 26.7292,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-05-01",
      "days_since_last_transaction": 8,
      "balance_change_30d": 2.1325,
      "transaction_change_30d": -4.1009,
      "card_spend_change_30d": -7.5335,
      "app_login_change_30d": 1.3311,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": 5.808,
      "upi_share_of_spend": 0.3643,
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
      "days_since_last_transaction": 13,
      "balance_change_30d": 5.503,
      "transaction_change_30d": -14.5055,
      "card_spend_change_30d": -20.71,
      "app_login_change_30d": -9.4611,
      "salary_missing_days": 3.0,
      "external_transfer_change_30d": 21.1863,
      "upi_share_of_spend": 0.4565,
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
    "tenure_months": 75,
    "customer_segment": "pension",
    "income_regularity": "regular",
    "products_count": 1,
    "has_credit_card": 0,
    "has_loan": 0,
    "days_since_last_transaction": 13,
    "balance_change_30d": 5.503,
    "transaction_change_30d": -14.5055,
    "card_spend_change_30d": -20.71,
    "app_login_change_30d": -9.4611,
    "salary_missing_days": 3.0,
    "external_transfer_change_30d": 21.1863,
    "upi_share_of_spend": 0.4565,
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
      "segment": "pension",
      "income_regularity": "regular",
      "tenure_months": 75,
      "age": 58,
      "customer_yearly_value": 10878.8876,
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
    "served_at": "2026-08-31T01:13:46",
    "elapsed_ms": 2308.57,
    "timings_ms": {
      "model1": 185.47,
      "model2": 2122.94
    },
    "customer_id": "C12000",
    "customer_name": "Vedika Wagle",
    "snapshot_date": "2026-06-01"
  },
  "model1": {
    "churn_probability": 8.99,
    "raw_churn_probability": 52.3,
    "probability_mode": "sigmoid",
    "risk_score": 26.97,
    "churn_prediction": "No",
    "risk_level": "Low",
    "top_risk_factors": [
      {
        "factor": "latest_days_since_last_transaction",
        "value": 13,
        "message": "Customer has gone longer without transacting.",
        "contribution": 0.3687579929828644
      },
      {
        "factor": "latest_salary_missing_days",
        "value": 3.0,
        "message": "Salary or pension was delayed recently.",
        "contribution": 0.2113594263792038
      },
      {
        "factor": "latest_vs_avg_upi_share_of_spend_available_history",
        "value": 0.06776666666666664,
        "message": "A larger share of spending is happening through UPI.",
        "contribution": 0.18852120637893677
      },
      {
        "factor": "latest_upi_share_of_spend",
        "value": 0.4565,
        "message": "A larger share of spending is happening through UPI.",
        "contribution": 0.018759949132800102
      },
      {
        "factor": "max_salary_missing_days_3m",
        "value": 3.0,
        "message": "Salary or pension was delayed recently.",
        "contribution": 0.018734052777290344
      }
    ]
  },
  "model2_input": {
    "customer_context": {
      "age": 58,
      "tenure_months": 75,
      "customer_segment": "pension",
      "income_regularity": "regular",
      "customer_yearly_value": 10878.8876,
      "products_count": 1,
      "has_credit_card": 0,
      "has_loan": 0
    },
    "behavior": {
      "days_since_last_transaction": 13,
      "balance_change_30d": 5.503,
      "transaction_change_30d": -14.5055,
      "card_spend_change_30d": -20.71,
      "app_login_change_30d": -9.4611,
      "salary_missing_days": 3,
      "external_transfer_change_30d": 21.1863,
      "upi_share_of_spend": 0.4565,
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
      "churn_probability": 0.0899,
      "churn_prediction": "No",
      "risk_level": "Low",
      "top_risk_factors": [
        {
          "factor": "days_since_last_transaction",
          "value": 13
        },
        {
          "factor": "salary_missing_days",
          "value": 3.0
        },
        {
          "factor": "vs_avg_upi_share_of_spend_available_history",
          "value": 0.06776666666666664
        },
        {
          "factor": "upi_share_of_spend",
          "value": 0.4565
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
    "case_id": "C12000"
  },
  "model2": {
    "case_id": "C12000",
    "ok": true,
    "prediction": {
      "evidence": [
        "complaints_30d=0",
        "failed_transactions_30d=2"
      ],
      "primary_reason": "UNKNOWN",
      "reasoning_summary": "Evidence is mixed or weak, so the cause remains unknown. Evidence suggests this because complaints_30d=0; failed_transactions_30d=2.",
      "recommended_action": "MONITOR",
      "secondary_reasons": [
        "FINANCIAL_STRESS"
      ],
      "urgency": "MEDIUM"
    },
    "raw_text": "{\"evidence\":[\"complaints_30d=0\",\"failed_transactions_30d=2\"],\"primary_reason\":\"UNKNOWN\",\"reasoning_summary\":\"Evidence is mixed or weak, so the cause remains unknown. Evidence suggests this because complaints_30d=0; failed_transactions_30d=2.\",\"recommended_action\":\"MONITOR\",\"secondary_reasons\":[\"FINANCIAL_STRESS\"],\"urgency\":\"MEDIUM\"}",
    "error": null,
    "latency_s": 2.1222,
    "simple_output": "Reason: UNKNOWN | Urgency: MEDIUM | Action: MONITOR | Why: Evidence is mixed or weak, so the cause remains unknown. Evidence suggests this because complaints_30d=0; failed_transactions_30d=2."
  }
}
```

### Warjas Tailor (`C12460`)

- OK: `True`
- Shape errors: `[]`
- Simple output: Reason: SERVICE_DISSATISFACTION | Urgency: MEDIUM | Action: SERVICE_RECOVERY | Why: Service friction is the clearest risk signal here. Complaint escalation fits because complaints_30d=0 and unresolved_complaints=0 indicate the issue may be unresolved or operationally related.

Request:

```json
{
  "customer_id": "C12460",
  "customer_name": "Warjas Tailor",
  "prediction_date": "2026-06-01",
  "snapshot_date": "2026-06-01",
  "target_month": "2026-07-01",
  "profile": {
    "tenure_months": 26,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 1,
    "has_credit_card": 0,
    "has_loan": 0
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 13,
      "balance_change_30d": -0.6505,
      "transaction_change_30d": -8.533,
      "card_spend_change_30d": -3.4379,
      "app_login_change_30d": -34.5494,
      "salary_missing_days": 4.0,
      "external_transfer_change_30d": 17.9091,
      "upi_share_of_spend": 0.4349,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 22.4033,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-02-01",
      "days_since_last_transaction": 8,
      "balance_change_30d": 31.6541,
      "transaction_change_30d": 24.8443,
      "card_spend_change_30d": 30.8701,
      "app_login_change_30d": -5.1182,
      "salary_missing_days": 1.0,
      "external_transfer_change_30d": -2.449,
      "upi_share_of_spend": 0.4133,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 26.2877,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-03-01",
      "days_since_last_transaction": 9,
      "balance_change_30d": -8.8319,
      "transaction_change_30d": -10.1019,
      "card_spend_change_30d": -18.433,
      "app_login_change_30d": 7.38,
      "salary_missing_days": 3.0,
      "external_transfer_change_30d": 21.6489,
      "upi_share_of_spend": 0.3978,
      "fd_maturing_in_30d": 1,
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
      "balance_change_30d": 13.3452,
      "transaction_change_30d": 0.9971,
      "card_spend_change_30d": -11.8759,
      "app_login_change_30d": 23.3085,
      "salary_missing_days": 1.0,
      "external_transfer_change_30d": -14.3168,
      "upi_share_of_spend": 0.3114,
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
      "balance_change_30d": -5.4753,
      "transaction_change_30d": 38.0615,
      "card_spend_change_30d": -10.9917,
      "app_login_change_30d": 19.1016,
      "salary_missing_days": 1.0,
      "external_transfer_change_30d": 35.0004,
      "upi_share_of_spend": 0.3163,
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
      "days_since_last_transaction": 1,
      "balance_change_30d": 26.161,
      "transaction_change_30d": 23.7879,
      "card_spend_change_30d": 19.235,
      "app_login_change_30d": 15.3525,
      "salary_missing_days": 1.0,
      "external_transfer_change_30d": -66.8618,
      "upi_share_of_spend": 0.3443,
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
    "tenure_months": 26,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 1,
    "has_credit_card": 0,
    "has_loan": 0,
    "days_since_last_transaction": 1,
    "balance_change_30d": 26.161,
    "transaction_change_30d": 23.7879,
    "card_spend_change_30d": 19.235,
    "app_login_change_30d": 15.3525,
    "salary_missing_days": 1.0,
    "external_transfer_change_30d": -66.8618,
    "upi_share_of_spend": 0.3443,
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
      "tenure_months": 26,
      "age": 40,
      "customer_yearly_value": 55978.1867,
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
    "served_at": "2026-08-31T01:13:48",
    "elapsed_ms": 2596.78,
    "timings_ms": {
      "model1": 170.26,
      "model2": 2426.37
    },
    "customer_id": "C12460",
    "customer_name": "Warjas Tailor",
    "snapshot_date": "2026-06-01"
  },
  "model1": {
    "churn_probability": 2.27,
    "raw_churn_probability": 21.23,
    "probability_mode": "sigmoid",
    "risk_score": 6.82,
    "churn_prediction": "No",
    "risk_level": "Low",
    "top_risk_factors": [
      {
        "factor": "sum_fd_maturing_in_30d_3m",
        "value": 1.0,
        "message": "Customer has a fixed deposit maturing soon.",
        "contribution": 0.06859863549470901
      },
      {
        "factor": "latest_vs_avg_external_transfer_change_30d_available_history",
        "value": -65.35026666666667,
        "message": "This signal increased churn risk.",
        "contribution": 0.060811057686805725
      },
      {
        "factor": "avg_transaction_change_30d_6m",
        "value": 11.509316666666669,
        "message": "This signal increased churn risk.",
        "contribution": 0.027224214747548103
      },
      {
        "factor": "max_days_since_last_transaction_3m",
        "value": 8.0,
        "message": "Customer has gone longer without transacting.",
        "contribution": 0.019624769687652588
      },
      {
        "factor": "latest_vs_avg_app_login_change_30d_available_history",
        "value": 11.106666666666666,
        "message": "This signal increased churn risk.",
        "contribution": 0.014945886097848415
      }
    ]
  },
  "model2_input": {
    "customer_context": {
      "age": 40,
      "tenure_months": 26,
      "customer_segment": "salary",
      "income_regularity": "regular",
      "customer_yearly_value": 55978.1867,
      "products_count": 1,
      "has_credit_card": 0,
      "has_loan": 0
    },
    "behavior": {
      "days_since_last_transaction": 1,
      "balance_change_30d": 26.161,
      "transaction_change_30d": 23.7879,
      "card_spend_change_30d": 19.235,
      "app_login_change_30d": 15.3525,
      "salary_missing_days": 1,
      "external_transfer_change_30d": -66.8618,
      "upi_share_of_spend": 0.3443,
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
      "churn_probability": 0.0227,
      "churn_prediction": "No",
      "risk_level": "Low",
      "top_risk_factors": [
        {
          "factor": "sum_fd_maturing_in_30d_3m",
          "value": 1.0
        },
        {
          "factor": "vs_avg_external_transfer_change_30d_available_history",
          "value": -65.35026666666667
        },
        {
          "factor": "avg_transaction_change_30d_6m",
          "value": 11.509316666666669
        },
        {
          "factor": "max_days_since_last_transaction_3m",
          "value": 8.0
        },
        {
          "factor": "vs_avg_app_login_change_30d_available_history",
          "value": 11.106666666666666
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
    "case_id": "C12460"
  },
  "model2": {
    "case_id": "C12460",
    "ok": true,
    "prediction": {
      "evidence": [
        "complaints_30d=0",
        "unresolved_complaints=0",
        "failed_transactions_30d=1"
      ],
      "primary_reason": "SERVICE_DISSATISFACTION",
      "reasoning_summary": "Service friction is the clearest risk signal here. Complaint escalation fits because complaints_30d=0 and unresolved_complaints=0 indicate the issue may be unresolved or operationally related.",
      "recommended_action": "SERVICE_RECOVERY",
      "secondary_reasons": [
        "DIGITAL_FRICTION"
      ],
      "urgency": "MEDIUM"
    },
    "raw_text": "{\"evidence\":[\"complaints_30d=0\",\"unresolved_complaints=0\",\"failed_transactions_30d=1\"],\"primary_reason\":\"SERVICE_DISSATISFACTION\",\"reasoning_summary\":\"Service friction is the clearest risk signal here. Complaint escalation fits because complaints_30d=0 and unresolved_complaints=0 indicate the issue may be unresolved or operationally related.\",\"recommended_action\":\"SERVICE_RECOVERY\",\"secondary_reasons\":[\"DIGITAL_FRICTION\"],\"urgency\":\"MEDIUM\"}",
    "error": null,
    "latency_s": 2.4261,
    "simple_output": "Reason: SERVICE_DISSATISFACTION | Urgency: MEDIUM | Action: SERVICE_RECOVERY | Why: Service friction is the clearest risk signal here. Complaint escalation fits because complaints_30d=0 and unresolved_complaints=0 indicate the issue may be unresolved or operationally related."
  }
}
```

### Pushti Nayar (`C12775`)

- OK: `True`
- Shape errors: `[]`
- Simple output: Reason: SERVICE_DISSATISFACTION | Urgency: MEDIUM | Action: COMPLAINT_ESCALATION | Why: Service friction is the clearest risk signal here, because complaints_30d=1 and unresolved_complaints=1 suggest a real issue that could be resolved through complaint escalation or service recovery.

Request:

```json
{
  "customer_id": "C12775",
  "customer_name": "Pushti Nayar",
  "prediction_date": "2026-04-01",
  "snapshot_date": "2026-04-01",
  "target_month": "2026-05-01",
  "profile": {
    "tenure_months": 120,
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
      "balance_change_30d": 12.9275,
      "transaction_change_30d": 9.597,
      "card_spend_change_30d": 13.9213,
      "app_login_change_30d": 0.0896,
      "salary_missing_days": 2.0,
      "external_transfer_change_30d": -3.2863,
      "upi_share_of_spend": 0.1205,
      "fd_maturing_in_30d": 1,
      "products_dropped_90d": 0,
      "complaints_30d": 6,
      "unresolved_complaints": 3,
      "failed_transactions_30d": 5,
      "avg_resolution_time_hrs": 67.3389,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-02-01",
      "days_since_last_transaction": 0,
      "balance_change_30d": -18.1842,
      "transaction_change_30d": 19.8369,
      "card_spend_change_30d": -14.143,
      "app_login_change_30d": -5.9839,
      "salary_missing_days": 2.0,
      "external_transfer_change_30d": 18.7964,
      "upi_share_of_spend": 0.0733,
      "fd_maturing_in_30d": 1,
      "products_dropped_90d": 0,
      "complaints_30d": 4,
      "unresolved_complaints": 3,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 77.191,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-03-01",
      "days_since_last_transaction": 4,
      "balance_change_30d": 3.2016,
      "transaction_change_30d": 11.4246,
      "card_spend_change_30d": 18.7729,
      "app_login_change_30d": 8.4484,
      "salary_missing_days": 1.0,
      "external_transfer_change_30d": 31.2,
      "upi_share_of_spend": 0.0,
      "fd_maturing_in_30d": 1,
      "products_dropped_90d": 0,
      "complaints_30d": 4,
      "unresolved_complaints": 3,
      "failed_transactions_30d": 3,
      "avg_resolution_time_hrs": 80.1593,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-04-01",
      "days_since_last_transaction": 2,
      "balance_change_30d": -2.4953,
      "transaction_change_30d": 8.1167,
      "card_spend_change_30d": 10.1464,
      "app_login_change_30d": -8.1874,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": 6.1242,
      "upi_share_of_spend": 0.0633,
      "fd_maturing_in_30d": 1,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 1,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 43.4689,
      "emi_bounce_30d": 0
    }
  ],
  "customer": {
    "tenure_months": 120,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 2,
    "has_credit_card": 0,
    "has_loan": 1,
    "days_since_last_transaction": 2,
    "balance_change_30d": -2.4953,
    "transaction_change_30d": 8.1167,
    "card_spend_change_30d": 10.1464,
    "app_login_change_30d": -8.1874,
    "salary_missing_days": 0.0,
    "external_transfer_change_30d": 6.1242,
    "upi_share_of_spend": 0.0633,
    "fd_maturing_in_30d": 1,
    "products_dropped_90d": 0,
    "complaints_30d": 1,
    "unresolved_complaints": 1,
    "failed_transactions_30d": 1,
    "avg_resolution_time_hrs": 43.4689,
    "emi_bounce_30d": 0
  },
  "extra_context": {
    "customer_profile": {
      "segment": "salary",
      "income_regularity": "regular",
      "tenure_months": 120,
      "age": 28,
      "customer_yearly_value": 11926.4788,
      "products_count": 2,
      "has_credit_card": 0,
      "has_loan": 1,
      "value_tier": "low"
    },
    "recent_complaint_text": "ATM receipt shows balance different from passbook. Please clarify."
  }
}
```

Response:

```json
{
  "meta": {
    "endpoint": "/predict/both",
    "served_at": "2026-08-31T01:13:52",
    "elapsed_ms": 3384.61,
    "timings_ms": {
      "model1": 200.29,
      "model2": 3184.2
    },
    "customer_id": "C12775",
    "customer_name": "Pushti Nayar",
    "snapshot_date": "2026-04-01"
  },
  "model1": {
    "churn_probability": 22.93,
    "raw_churn_probability": 75.98,
    "probability_mode": "sigmoid",
    "risk_score": 71.1,
    "churn_prediction": "Yes",
    "risk_level": "Medium",
    "top_risk_factors": [
      {
        "factor": "max_avg_resolution_time_hrs_3m",
        "value": 80.1593,
        "message": "Recent complaints took longer to resolve.",
        "contribution": 0.49015486240386963
      },
      {
        "factor": "latest_avg_resolution_time_hrs",
        "value": 43.4689,
        "message": "Recent complaints took longer to resolve.",
        "contribution": 0.4596184194087982
      },
      {
        "factor": "latest_fd_maturing_in_30d",
        "value": 1,
        "message": "Customer has a fixed deposit maturing soon.",
        "contribution": 0.1720765382051468
      },
      {
        "factor": "sum_fd_maturing_in_30d_3m",
        "value": 3.0,
        "message": "Customer has a fixed deposit maturing soon.",
        "contribution": 0.14877669513225555
      },
      {
        "factor": "sum_complaints_30d_6m",
        "value": 15.0,
        "message": "Customer has recent complaint activity.",
        "contribution": 0.10563117265701294
      }
    ]
  },
  "model2_input": {
    "customer_context": {
      "age": 28,
      "tenure_months": 120,
      "customer_segment": "salary",
      "income_regularity": "regular",
      "customer_yearly_value": 11926.4788,
      "products_count": 2,
      "has_credit_card": 0,
      "has_loan": 1
    },
    "behavior": {
      "days_since_last_transaction": 2,
      "balance_change_30d": -2.4953,
      "transaction_change_30d": 8.1167,
      "card_spend_change_30d": 10.1464,
      "app_login_change_30d": -8.1874,
      "salary_missing_days": 0,
      "external_transfer_change_30d": 6.1242,
      "upi_share_of_spend": 0.0633,
      "fd_maturing_in_30d": 1,
      "products_dropped_90d": 0,
      "emi_bounce_30d": 0
    },
    "service_evidence": {
      "complaints_30d": 1,
      "unresolved_complaints": 1,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 43.4689,
      "complaint_text": "ATM receipt shows balance different from passbook. Please clarify."
    },
    "model1": {
      "churn_probability": 0.2293,
      "churn_prediction": "Yes",
      "risk_level": "Medium",
      "top_risk_factors": [
        {
          "factor": "max_avg_resolution_time_hrs_3m",
          "value": 80.1593
        },
        {
          "factor": "avg_resolution_time_hrs",
          "value": 43.4689
        },
        {
          "factor": "fd_maturing_in_30d",
          "value": 1
        },
        {
          "factor": "sum_fd_maturing_in_30d_3m",
          "value": 3.0
        },
        {
          "factor": "sum_complaints_30d_6m",
          "value": 15.0
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
    "case_id": "C12775"
  },
  "model2": {
    "case_id": "C12775",
    "ok": true,
    "prediction": {
      "evidence": [
        "complaints_30d=1",
        "unresolved_complaints=1",
        "avg_resolution_time_hrs=43.5",
        "complaint_text describes a recent service issue"
      ],
      "primary_reason": "SERVICE_DISSATISFACTION",
      "reasoning_summary": "Service friction is the clearest risk signal here, because complaints_30d=1 and unresolved_complaints=1 suggest a real issue that could be resolved through complaint escalation or service recovery.",
      "recommended_action": "COMPLAINT_ESCALATION",
      "secondary_reasons": [
        "UNKNOWN"
      ],
      "urgency": "MEDIUM"
    },
    "raw_text": "{\n    \"evidence\": [\n        \"complaints_30d=1\", \"unresolved_complaints=1\", \"avg_resolution_time_hrs=43.5\",\n        \"complaint_text describes a recent service issue\"\n    ],\n    \"primary_reason\": \"SERVICE_DISSATISFACTION\",\n    \"reasoning_summary\": \"Service friction is the clearest risk signal here, because complaints_30d=1 and unresolved_complaints=1 suggest a real issue that could be resolved through complaint escalation or service recovery.\",\n    \"recommended_action\": \"COMPLAINT_ESCALATION\",\n    \"secondary_reasons\": [\"UNKNOWN\"],\n    \"urgency\": \"MEDIUM\"\n}",
    "error": null,
    "latency_s": 3.1839,
    "simple_output": "Reason: SERVICE_DISSATISFACTION | Urgency: MEDIUM | Action: COMPLAINT_ESCALATION | Why: Service friction is the clearest risk signal here, because complaints_30d=1 and unresolved_complaints=1 suggest a real issue that could be resolved through complaint escalation or service recovery."
  }
}
```

### Yasti Sagar (`C13034`)

- OK: `True`
- Shape errors: `[]`
- Simple output: Reason: UNKNOWN | Urgency: MEDIUM | Action: MONITOR | Why: Evidence is mixed or weak, so the cause remains unknown. The current relationship looks healthy overall.

Request:

```json
{
  "customer_id": "C13034",
  "customer_name": "Yasti Sagar",
  "prediction_date": "2026-06-01",
  "snapshot_date": "2026-06-01",
  "target_month": "2026-07-01",
  "profile": {
    "tenure_months": 57,
    "customer_segment": "vendor",
    "income_regularity": "irregular",
    "products_count": 2,
    "has_credit_card": 1,
    "has_loan": 0
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 7,
      "balance_change_30d": 15.987,
      "transaction_change_30d": -4.9119,
      "card_spend_change_30d": -13.1648,
      "app_login_change_30d": -5.7516,
      "salary_missing_days": null,
      "external_transfer_change_30d": 5.6137,
      "upi_share_of_spend": 0.4763,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 1,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 8.9909,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-02-01",
      "days_since_last_transaction": 7,
      "balance_change_30d": 7.0949,
      "transaction_change_30d": -6.4955,
      "card_spend_change_30d": -6.8832,
      "app_login_change_30d": 0.2957,
      "salary_missing_days": null,
      "external_transfer_change_30d": 21.6329,
      "upi_share_of_spend": 0.4151,
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
      "balance_change_30d": 17.9029,
      "transaction_change_30d": -26.8274,
      "card_spend_change_30d": 37.7081,
      "app_login_change_30d": 8.3575,
      "salary_missing_days": null,
      "external_transfer_change_30d": -16.2662,
      "upi_share_of_spend": 0.4643,
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
      "balance_change_30d": -10.0292,
      "transaction_change_30d": -8.6277,
      "card_spend_change_30d": 16.1586,
      "app_login_change_30d": -23.1836,
      "salary_missing_days": null,
      "external_transfer_change_30d": 46.3816,
      "upi_share_of_spend": 0.4884,
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
      "days_since_last_transaction": 12,
      "balance_change_30d": -15.1198,
      "transaction_change_30d": -8.3348,
      "card_spend_change_30d": 5.7341,
      "app_login_change_30d": -21.9992,
      "salary_missing_days": null,
      "external_transfer_change_30d": -8.3656,
      "upi_share_of_spend": 0.4905,
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
      "days_since_last_transaction": 11,
      "balance_change_30d": 19.924,
      "transaction_change_30d": 17.5425,
      "card_spend_change_30d": 14.5251,
      "app_login_change_30d": -8.3426,
      "salary_missing_days": null,
      "external_transfer_change_30d": -14.1294,
      "upi_share_of_spend": 0.4364,
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
    "products_count": 2,
    "has_credit_card": 1,
    "has_loan": 0,
    "days_since_last_transaction": 11,
    "balance_change_30d": 19.924,
    "transaction_change_30d": 17.5425,
    "card_spend_change_30d": 14.5251,
    "app_login_change_30d": -8.3426,
    "salary_missing_days": null,
    "external_transfer_change_30d": -14.1294,
    "upi_share_of_spend": 0.4364,
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
      "age": 43,
      "customer_yearly_value": 3726.1127,
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
    "served_at": "2026-08-31T01:13:54",
    "elapsed_ms": 1846.48,
    "timings_ms": {
      "model1": 136.87,
      "model2": 1709.45
    },
    "customer_id": "C13034",
    "customer_name": "Yasti Sagar",
    "snapshot_date": "2026-06-01"
  },
  "model1": {
    "churn_probability": 2.98,
    "raw_churn_probability": 27.24,
    "probability_mode": "sigmoid",
    "risk_score": 8.95,
    "churn_prediction": "No",
    "risk_level": "Low",
    "top_risk_factors": [
      {
        "factor": "days_since_last_transaction_trend_6m",
        "value": 1.0857142857142852,
        "message": "Customer has gone longer without transacting.",
        "contribution": 0.05171413719654083
      },
      {
        "factor": "count_app_login_drop_3m",
        "value": 2,
        "message": "This signal increased churn risk.",
        "contribution": 0.015128307044506073
      },
      {
        "factor": "max_days_since_last_transaction_3m",
        "value": 12.0,
        "message": "Customer has gone longer without transacting.",
        "contribution": 0.015020850114524364
      },
      {
        "factor": "avg_app_login_change_30d_3m",
        "value": -17.8418,
        "message": "App usage has been falling across recent months.",
        "contribution": 0.011690217070281506
      },
      {
        "factor": "latest_vs_avg_card_spend_change_30d_available_history",
        "value": 5.512116666666667,
        "message": "This signal increased churn risk.",
        "contribution": 0.008267940953373909
      }
    ]
  },
  "model2_input": {
    "customer_context": {
      "age": 43,
      "tenure_months": 57,
      "customer_segment": "vendor",
      "income_regularity": "irregular",
      "customer_yearly_value": 3726.1127,
      "products_count": 2,
      "has_credit_card": 1,
      "has_loan": 0
    },
    "behavior": {
      "days_since_last_transaction": 11,
      "balance_change_30d": 19.924,
      "transaction_change_30d": 17.5425,
      "card_spend_change_30d": 14.5251,
      "app_login_change_30d": -8.3426,
      "salary_missing_days": null,
      "external_transfer_change_30d": -14.1294,
      "upi_share_of_spend": 0.4364,
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
      "churn_probability": 0.0298,
      "churn_prediction": "No",
      "risk_level": "Low",
      "top_risk_factors": [
        {
          "factor": "days_since_last_transaction_trend_6m",
          "value": 1.0857142857142852
        },
        {
          "factor": "count_app_login_drop_3m",
          "value": 2
        },
        {
          "factor": "max_days_since_last_transaction_3m",
          "value": 12.0
        },
        {
          "factor": "avg_app_login_change_30d_3m",
          "value": -17.8418
        },
        {
          "factor": "vs_avg_card_spend_change_30d_available_history",
          "value": 5.512116666666667
        }
      ]
    },
    "eligible_actions": [
      "MONITOR",
      "RE_ENGAGEMENT",
      "PRODUCT_REVIEW"
    ],
    "case_id": "C13034"
  },
  "model2": {
    "case_id": "C13034",
    "ok": true,
    "prediction": {
      "evidence": [
        "complaints_30d=0",
        "failed_transactions_30d=0",
        "avg_resolution_time_hrs=0.0"
      ],
      "primary_reason": "UNKNOWN",
      "reasoning_summary": "Evidence is mixed or weak, so the cause remains unknown. The current relationship looks healthy overall.",
      "recommended_action": "MONITOR",
      "secondary_reasons": [
        "DIGITAL_FRICTION"
      ],
      "urgency": "MEDIUM"
    },
    "raw_text": "{\n\"evidence\":[\"complaints_30d=0\",\"failed_transactions_30d=0\",\"avg_resolution_time_hrs=0.0\"],\"primary_reason\":\"UNKNOWN\",\"reasoning_summary\":\"Evidence is mixed or weak, so the cause remains unknown. The current relationship looks healthy overall.\",\"recommended_action\":\"MONITOR\",\"secondary_reasons\":[\"DIGITAL_FRICTION\"],\"urgency\":\"MEDIUM\"\n}",
    "error": null,
    "latency_s": 1.7092,
    "simple_output": "Reason: UNKNOWN | Urgency: MEDIUM | Action: MONITOR | Why: Evidence is mixed or weak, so the cause remains unknown. The current relationship looks healthy overall."
  }
}
```

### Girindra Chaudhry (`C13336`)

- OK: `True`
- Shape errors: `[]`
- Simple output: Reason: UNKNOWN | Urgency: MEDIUM | Action: MONITOR | Why: Evidence is mixed or weak, so the cause remains unknown. Evidence suggests this because transaction_change_30d_trend_6m=-12.0; balance_change_30d_trend_6m=-18.3.

Request:

```json
{
  "customer_id": "C13336",
  "customer_name": "Girindra Chaudhry",
  "prediction_date": "2026-03-01",
  "snapshot_date": "2026-03-01",
  "target_month": "2026-04-01",
  "profile": {
    "tenure_months": 67,
    "customer_segment": "vendor",
    "income_regularity": "irregular",
    "products_count": 1,
    "has_credit_card": 0,
    "has_loan": 0
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 2,
      "balance_change_30d": 38.2424,
      "transaction_change_30d": 26.4818,
      "card_spend_change_30d": 28.9071,
      "app_login_change_30d": -2.59,
      "salary_missing_days": null,
      "external_transfer_change_30d": -10.2569,
      "upi_share_of_spend": 0.436,
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
      "days_since_last_transaction": 0,
      "balance_change_30d": 21.1453,
      "transaction_change_30d": 17.5897,
      "card_spend_change_30d": 17.255,
      "app_login_change_30d": -2.6354,
      "salary_missing_days": null,
      "external_transfer_change_30d": -47.9824,
      "upi_share_of_spend": 0.6054,
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
      "balance_change_30d": 1.714,
      "transaction_change_30d": 2.4638,
      "card_spend_change_30d": 17.7295,
      "app_login_change_30d": -15.2672,
      "salary_missing_days": null,
      "external_transfer_change_30d": -2.5061,
      "upi_share_of_spend": 0.5931,
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
    "customer_segment": "vendor",
    "income_regularity": "irregular",
    "products_count": 1,
    "has_credit_card": 0,
    "has_loan": 0,
    "days_since_last_transaction": 0,
    "balance_change_30d": 1.714,
    "transaction_change_30d": 2.4638,
    "card_spend_change_30d": 17.7295,
    "app_login_change_30d": -15.2672,
    "salary_missing_days": null,
    "external_transfer_change_30d": -2.5061,
    "upi_share_of_spend": 0.5931,
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
      "tenure_months": 67,
      "age": 27,
      "customer_yearly_value": 11975.4318,
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
    "served_at": "2026-08-31T01:13:56",
    "elapsed_ms": 2253.16,
    "timings_ms": {
      "model1": 73.19,
      "model2": 2179.8
    },
    "customer_id": "C13336",
    "customer_name": "Girindra Chaudhry",
    "snapshot_date": "2026-03-01"
  },
  "model1": {
    "churn_probability": 3.74,
    "raw_churn_probability": 32.26,
    "probability_mode": "sigmoid",
    "risk_score": 11.22,
    "churn_prediction": "No",
    "risk_level": "Low",
    "top_risk_factors": [
      {
        "factor": "latest_vs_avg_upi_share_of_spend_available_history",
        "value": 0.04826666666666657,
        "message": "A larger share of spending is happening through UPI.",
        "contribution": 0.18225407600402832
      },
      {
        "factor": "sum_fd_maturing_in_30d_3m",
        "value": 1.0,
        "message": "Customer has a fixed deposit maturing soon.",
        "contribution": 0.0836273729801178
      },
      {
        "factor": "transaction_change_30d_trend_6m",
        "value": -12.009,
        "message": "Transaction activity has been falling across recent months.",
        "contribution": 0.07971802353858948
      },
      {
        "factor": "balance_change_30d_trend_6m",
        "value": -18.2642,
        "message": "Balance has been falling across recent months.",
        "contribution": 0.03673006221652031
      },
      {
        "factor": "latest_upi_share_of_spend",
        "value": 0.5931,
        "message": "A larger share of spending is happening through UPI.",
        "contribution": 0.034017812460660934
      }
    ]
  },
  "model2_input": {
    "customer_context": {
      "age": 27,
      "tenure_months": 67,
      "customer_segment": "vendor",
      "income_regularity": "irregular",
      "customer_yearly_value": 11975.4318,
      "products_count": 1,
      "has_credit_card": 0,
      "has_loan": 0
    },
    "behavior": {
      "days_since_last_transaction": 0,
      "balance_change_30d": 1.714,
      "transaction_change_30d": 2.4638,
      "card_spend_change_30d": 17.7295,
      "app_login_change_30d": -15.2672,
      "salary_missing_days": null,
      "external_transfer_change_30d": -2.5061,
      "upi_share_of_spend": 0.5931,
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
      "churn_probability": 0.0374,
      "churn_prediction": "No",
      "risk_level": "Low",
      "top_risk_factors": [
        {
          "factor": "vs_avg_upi_share_of_spend_available_history",
          "value": 0.04826666666666657
        },
        {
          "factor": "sum_fd_maturing_in_30d_3m",
          "value": 1.0
        },
        {
          "factor": "transaction_change_30d_trend_6m",
          "value": -12.009
        },
        {
          "factor": "balance_change_30d_trend_6m",
          "value": -18.2642
        },
        {
          "factor": "upi_share_of_spend",
          "value": 0.5931
        }
      ]
    },
    "eligible_actions": [
      "MONITOR",
      "RE_ENGAGEMENT",
      "PRODUCT_REVIEW",
      "SERVICE_RECOVERY"
    ],
    "case_id": "C13336"
  },
  "model2": {
    "case_id": "C13336",
    "ok": true,
    "prediction": {
      "evidence": [
        "transaction_change_30d_trend_6m=-12.0",
        "balance_change_30d_trend_6m=-18.3"
      ],
      "primary_reason": "UNKNOWN",
      "reasoning_summary": "Evidence is mixed or weak, so the cause remains unknown. Evidence suggests this because transaction_change_30d_trend_6m=-12.0; balance_change_30d_trend_6m=-18.3.",
      "recommended_action": "MONITOR",
      "secondary_reasons": [
        "FINANCIAL_STRESS"
      ],
      "urgency": "MEDIUM"
    },
    "raw_text": "{\"evidence\":[\"transaction_change_30d_trend_6m=-12.0\",\"balance_change_30d_trend_6m=-18.3\"],\"primary_reason\":\"UNKNOWN\",\"reasoning_summary\":\"Evidence is mixed or weak, so the cause remains unknown. Evidence suggests this because transaction_change_30d_trend_6m=-12.0; balance_change_30d_trend_6m=-18.3.\",\"recommended_action\":\"MONITOR\",\"secondary_reasons\":[\"FINANCIAL_STRESS\"],\"urgency\":\"MEDIUM\"}",
    "error": null,
    "latency_s": 2.1795,
    "simple_output": "Reason: UNKNOWN | Urgency: MEDIUM | Action: MONITOR | Why: Evidence is mixed or weak, so the cause remains unknown. Evidence suggests this because transaction_change_30d_trend_6m=-12.0; balance_change_30d_trend_6m=-18.3."
  }
}
```

### Nihal Gola (`C13982`)

- OK: `True`
- Shape errors: `[]`
- Simple output: Reason: SERVICE_DISSATISFACTION | Urgency: MEDIUM | Action: SERVICE_RECOVERY | Why: Service friction is the clearest risk signal here, though complaints evidence is mixed or weak so a recovery-oriented approach fits better than escalation or fee review.

Request:

```json
{
  "customer_id": "C13982",
  "customer_name": "Nihal Gola",
  "prediction_date": "2026-01-01",
  "snapshot_date": "2026-01-01",
  "target_month": "2026-02-01",
  "profile": {
    "tenure_months": 85,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 2,
    "has_credit_card": 1,
    "has_loan": 0
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 5,
      "balance_change_30d": -15.3714,
      "transaction_change_30d": 13.2697,
      "card_spend_change_30d": 6.333,
      "app_login_change_30d": 32.1157,
      "salary_missing_days": 2.0,
      "external_transfer_change_30d": -24.3553,
      "upi_share_of_spend": 0.4167,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 3,
      "unresolved_complaints": 1,
      "failed_transactions_30d": 3,
      "avg_resolution_time_hrs": 64.5551,
      "emi_bounce_30d": 0
    }
  ],
  "customer": {
    "tenure_months": 85,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 2,
    "has_credit_card": 1,
    "has_loan": 0,
    "days_since_last_transaction": 5,
    "balance_change_30d": -15.3714,
    "transaction_change_30d": 13.2697,
    "card_spend_change_30d": 6.333,
    "app_login_change_30d": 32.1157,
    "salary_missing_days": 2.0,
    "external_transfer_change_30d": -24.3553,
    "upi_share_of_spend": 0.4167,
    "fd_maturing_in_30d": 0,
    "products_dropped_90d": 0,
    "complaints_30d": 3,
    "unresolved_complaints": 1,
    "failed_transactions_30d": 3,
    "avg_resolution_time_hrs": 64.5551,
    "emi_bounce_30d": 0
  },
  "extra_context": {
    "customer_profile": {
      "segment": "salary",
      "income_regularity": "regular",
      "tenure_months": 85,
      "age": 30,
      "customer_yearly_value": 106264.9139,
      "products_count": 2,
      "has_credit_card": 1,
      "has_loan": 0,
      "value_tier": "high"
    },
    "recent_complaint_text": "Charges are deducted instantly but refunds take three weeks. Unfair."
  }
}
```

Response:

```json
{
  "meta": {
    "endpoint": "/predict/both",
    "served_at": "2026-08-31T01:13:59",
    "elapsed_ms": 2928.28,
    "timings_ms": {
      "model1": 71.92,
      "model2": 2856.23
    },
    "customer_id": "C13982",
    "customer_name": "Nihal Gola",
    "snapshot_date": "2026-01-01"
  },
  "model1": {
    "churn_probability": 16.31,
    "raw_churn_probability": 66.89,
    "probability_mode": "sigmoid",
    "risk_score": 55.23,
    "churn_prediction": "No",
    "risk_level": "Medium",
    "top_risk_factors": [
      {
        "factor": "max_avg_resolution_time_hrs_3m",
        "value": 64.5551,
        "message": "Recent complaints took longer to resolve.",
        "contribution": 0.4877869188785553
      },
      {
        "factor": "latest_avg_resolution_time_hrs",
        "value": 64.5551,
        "message": "Recent complaints took longer to resolve.",
        "contribution": 0.3985517919063568
      },
      {
        "factor": "latest_failed_transactions_30d",
        "value": 3,
        "message": "Customer has recent failed transactions.",
        "contribution": 0.15070092678070068
      },
      {
        "factor": "latest_salary_missing_days",
        "value": 2.0,
        "message": "Salary or pension was delayed recently.",
        "contribution": 0.08310206979513168
      },
      {
        "factor": "transaction_change_30d_trend_6m",
        "value": 0.0,
        "message": "This signal increased churn risk.",
        "contribution": 0.06042433902621269
      }
    ]
  },
  "model2_input": {
    "customer_context": {
      "age": 30,
      "tenure_months": 85,
      "customer_segment": "salary",
      "income_regularity": "regular",
      "customer_yearly_value": 106264.9139,
      "products_count": 2,
      "has_credit_card": 1,
      "has_loan": 0
    },
    "behavior": {
      "days_since_last_transaction": 5,
      "balance_change_30d": -15.3714,
      "transaction_change_30d": 13.2697,
      "card_spend_change_30d": 6.333,
      "app_login_change_30d": 32.1157,
      "salary_missing_days": 2,
      "external_transfer_change_30d": -24.3553,
      "upi_share_of_spend": 0.4167,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "emi_bounce_30d": 0
    },
    "service_evidence": {
      "complaints_30d": 3,
      "unresolved_complaints": 1,
      "failed_transactions_30d": 3,
      "avg_resolution_time_hrs": 64.5551,
      "complaint_text": "Charges are deducted instantly but refunds take three weeks. Unfair."
    },
    "model1": {
      "churn_probability": 0.1631,
      "churn_prediction": "No",
      "risk_level": "Medium",
      "top_risk_factors": [
        {
          "factor": "max_avg_resolution_time_hrs_3m",
          "value": 64.5551
        },
        {
          "factor": "avg_resolution_time_hrs",
          "value": 64.5551
        },
        {
          "factor": "failed_transactions_30d",
          "value": 3
        },
        {
          "factor": "salary_missing_days",
          "value": 2.0
        },
        {
          "factor": "transaction_change_30d_trend_6m",
          "value": 0.0
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
    "case_id": "C13982"
  },
  "model2": {
    "case_id": "C13982",
    "ok": true,
    "prediction": {
      "evidence": [
        "complaints_30d=3",
        "unresolved_complaints=1",
        "avg_resolution_time_hrs=64.6",
        "failed_transactions_30d=3"
      ],
      "primary_reason": "SERVICE_DISSATISFACTION",
      "reasoning_summary": "Service friction is the clearest risk signal here, though complaints evidence is mixed or weak so a recovery-oriented approach fits better than escalation or fee review.",
      "recommended_action": "SERVICE_RECOVERY",
      "secondary_reasons": [
        "COMPETITOR_MIGRATION",
        "FEE_DISSATISFACTION",
        "UNKNOWN"
      ],
      "urgency": "MEDIUM"
    },
    "raw_text": "{\n    \"evidence\": [\n        \"complaints_30d=3\",\n        \"unresolved_complaints=1\",\n        \"avg_resolution_time_hrs=64.6\",\n        \"failed_transactions_30d=3\"\n    ],\n    \"primary_reason\": \"SERVICE_DISSATISFACTION\",\n    \"reasoning_summary\": \"Service friction is the clearest risk signal here, though complaints evidence is mixed or weak so a recovery-oriented approach fits better than escalation or fee review.\",\n    \"recommended_action\": \"SERVICE_RECOVERY\",\n    \"secondary_reasons\": [\n        \"COMPETITOR_MIGRATION\",\n        \"FEE_DISSATISFACTION\",\n        \"UNKNOWN\"\n    ],\n    \"urgency\": \"MEDIUM\"\n}",
    "error": null,
    "latency_s": 2.856,
    "simple_output": "Reason: SERVICE_DISSATISFACTION | Urgency: MEDIUM | Action: SERVICE_RECOVERY | Why: Service friction is the clearest risk signal here, though complaints evidence is mixed or weak so a recovery-oriented approach fits better than escalation or fee review."
  }
}
```

### Shivani Ramachandran (`C14465`)

- OK: `True`
- Shape errors: `[]`
- Simple output: Reason: SERVICE_DISSATISFACTION | Urgency: MEDIUM | Action: SERVICE_RECOVERY | Why: Service friction is the clearest risk signal here given complaints_30d=1 and unresolved_complaints=1 despite the mixed evidence overall.

Request:

```json
{
  "customer_id": "C14465",
  "customer_name": "Shivani Ramachandran",
  "prediction_date": "2026-06-01",
  "snapshot_date": "2026-06-01",
  "target_month": "2026-07-01",
  "profile": {
    "tenure_months": 163,
    "customer_segment": "pension",
    "income_regularity": "regular",
    "products_count": 1,
    "has_credit_card": 0,
    "has_loan": 0
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 12,
      "balance_change_30d": 6.1626,
      "transaction_change_30d": 15.6793,
      "card_spend_change_30d": -19.1781,
      "app_login_change_30d": 8.8559,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -2.5532,
      "upi_share_of_spend": 0.3146,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 2,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 21.4691,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-02-01",
      "days_since_last_transaction": 18,
      "balance_change_30d": -12.3669,
      "transaction_change_30d": -7.6662,
      "card_spend_change_30d": -30.7787,
      "app_login_change_30d": -0.1965,
      "salary_missing_days": 1.0,
      "external_transfer_change_30d": 43.518,
      "upi_share_of_spend": 0.4122,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 21.7624,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-03-01",
      "days_since_last_transaction": 19,
      "balance_change_30d": -2.4002,
      "transaction_change_30d": -28.3197,
      "card_spend_change_30d": -14.4041,
      "app_login_change_30d": -32.0054,
      "salary_missing_days": 3.0,
      "external_transfer_change_30d": 37.8684,
      "upi_share_of_spend": 0.3736,
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
      "days_since_last_transaction": 10,
      "balance_change_30d": -36.0357,
      "transaction_change_30d": -24.1396,
      "card_spend_change_30d": -1.0261,
      "app_login_change_30d": 9.1859,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": 20.6485,
      "upi_share_of_spend": 0.2415,
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
      "balance_change_30d": -8.4464,
      "transaction_change_30d": 2.7961,
      "card_spend_change_30d": -16.2718,
      "app_login_change_30d": -0.2743,
      "salary_missing_days": 1.0,
      "external_transfer_change_30d": 27.8548,
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
      "balance_change_30d": -12.341,
      "transaction_change_30d": -7.0296,
      "card_spend_change_30d": 7.6196,
      "app_login_change_30d": -11.5287,
      "salary_missing_days": 1.0,
      "external_transfer_change_30d": 24.8288,
      "upi_share_of_spend": 0.3548,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 1,
      "failed_transactions_30d": 2,
      "avg_resolution_time_hrs": 52.6753,
      "emi_bounce_30d": 0
    }
  ],
  "customer": {
    "tenure_months": 163,
    "customer_segment": "pension",
    "income_regularity": "regular",
    "products_count": 1,
    "has_credit_card": 0,
    "has_loan": 0,
    "days_since_last_transaction": 11,
    "balance_change_30d": -12.341,
    "transaction_change_30d": -7.0296,
    "card_spend_change_30d": 7.6196,
    "app_login_change_30d": -11.5287,
    "salary_missing_days": 1.0,
    "external_transfer_change_30d": 24.8288,
    "upi_share_of_spend": 0.3548,
    "fd_maturing_in_30d": 0,
    "products_dropped_90d": 0,
    "complaints_30d": 1,
    "unresolved_complaints": 1,
    "failed_transactions_30d": 2,
    "avg_resolution_time_hrs": 52.6753,
    "emi_bounce_30d": 0
  },
  "extra_context": {
    "customer_profile": {
      "segment": "pension",
      "income_regularity": "regular",
      "tenure_months": 163,
      "age": 78,
      "customer_yearly_value": 27627.9841,
      "products_count": 1,
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
    "served_at": "2026-08-31T01:14:01",
    "elapsed_ms": 2588.69,
    "timings_ms": {
      "model1": 64.13,
      "model2": 2524.3
    },
    "customer_id": "C14465",
    "customer_name": "Shivani Ramachandran",
    "snapshot_date": "2026-06-01"
  },
  "model1": {
    "churn_probability": 10.66,
    "raw_churn_probability": 56.37,
    "probability_mode": "sigmoid",
    "risk_score": 32.65,
    "churn_prediction": "No",
    "risk_level": "Low",
    "top_risk_factors": [
      {
        "factor": "max_avg_resolution_time_hrs_3m",
        "value": 52.6753,
        "message": "Recent complaints took longer to resolve.",
        "contribution": 0.4023066759109497
      },
      {
        "factor": "latest_avg_resolution_time_hrs",
        "value": 52.6753,
        "message": "Recent complaints took longer to resolve.",
        "contribution": 0.32901063561439514
      },
      {
        "factor": "count_balance_drop_3m",
        "value": 3,
        "message": "This signal increased churn risk.",
        "contribution": 0.06389997899532318
      },
      {
        "factor": "count_balance_drop_6m",
        "value": 4,
        "message": "This signal increased churn risk.",
        "contribution": 0.0471075177192688
      },
      {
        "factor": "card_spend_change_30d_trend_6m",
        "value": 5.453919999999998,
        "message": "This signal increased churn risk.",
        "contribution": 0.02954336442053318
      }
    ]
  },
  "model2_input": {
    "customer_context": {
      "age": 78,
      "tenure_months": 163,
      "customer_segment": "pension",
      "income_regularity": "regular",
      "customer_yearly_value": 27627.9841,
      "products_count": 1,
      "has_credit_card": 0,
      "has_loan": 0
    },
    "behavior": {
      "days_since_last_transaction": 11,
      "balance_change_30d": -12.341,
      "transaction_change_30d": -7.0296,
      "card_spend_change_30d": 7.6196,
      "app_login_change_30d": -11.5287,
      "salary_missing_days": 1,
      "external_transfer_change_30d": 24.8288,
      "upi_share_of_spend": 0.3548,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "emi_bounce_30d": 0
    },
    "service_evidence": {
      "complaints_30d": 1,
      "unresolved_complaints": 1,
      "failed_transactions_30d": 2,
      "avg_resolution_time_hrs": 52.6753,
      "complaint_text": "Kindly train your staff, the new clerk did not know the FD process."
    },
    "model1": {
      "churn_probability": 0.1066,
      "churn_prediction": "No",
      "risk_level": "Low",
      "top_risk_factors": [
        {
          "factor": "max_avg_resolution_time_hrs_3m",
          "value": 52.6753
        },
        {
          "factor": "avg_resolution_time_hrs",
          "value": 52.6753
        },
        {
          "factor": "count_balance_drop_3m",
          "value": 3
        },
        {
          "factor": "count_balance_drop_6m",
          "value": 4
        },
        {
          "factor": "card_spend_change_30d_trend_6m",
          "value": 5.453919999999998
        }
      ]
    },
    "eligible_actions": [
      "MONITOR",
      "RE_ENGAGEMENT",
      "PRODUCT_REVIEW",
      "SERVICE_RECOVERY",
      "COMPLAINT_ESCALATION",
      "FINANCIAL_GUIDANCE",
      "RM_CALLBACK"
    ],
    "case_id": "C14465"
  },
  "model2": {
    "case_id": "C14465",
    "ok": true,
    "prediction": {
      "evidence": [
        "complaints_30d=1",
        "unresolved_complaints=1",
        "avg_resolution_time_hrs=52.7",
        "complaint_text describes a recent service issue"
      ],
      "primary_reason": "SERVICE_DISSATISFACTION",
      "reasoning_summary": "Service friction is the clearest risk signal here given complaints_30d=1 and unresolved_complaints=1 despite the mixed evidence overall.",
      "recommended_action": "SERVICE_RECOVERY",
      "secondary_reasons": [
        "UNKNOWN"
      ],
      "urgency": "MEDIUM"
    },
    "raw_text": "{\n    \"evidence\": [\n        \"complaints_30d=1\", \"unresolved_complaints=1\", \"avg_resolution_time_hrs=52.7\", \"complaint_text describes a recent service issue\"\n    ],\n    \"primary_reason\": \"SERVICE_DISSATISFACTION\",\n    \"reasoning_summary\": \"Service friction is the clearest risk signal here given complaints_30d=1 and unresolved_complaints=1 despite the mixed evidence overall.\",\n    \"recommended_action\": \"SERVICE_RECOVERY\",\n    \"secondary_reasons\": [\n        \"UNKNOWN\"\n    ],\n    \"urgency\": \"MEDIUM\"\n}",
    "error": null,
    "latency_s": 2.524,
    "simple_output": "Reason: SERVICE_DISSATISFACTION | Urgency: MEDIUM | Action: SERVICE_RECOVERY | Why: Service friction is the clearest risk signal here given complaints_30d=1 and unresolved_complaints=1 despite the mixed evidence overall."
  }
}
```

### Tanmayi Barad (`C15320`)

- OK: `True`
- Shape errors: `[]`
- Simple output: Reason: UNKNOWN | Urgency: MEDIUM | Action: MONITOR | Why: Evidence is mixed or weak, so the cause remains unknown. The current relationship looks stable overall.

Request:

```json
{
  "customer_id": "C15320",
  "customer_name": "Tanmayi Barad",
  "prediction_date": "2026-06-01",
  "snapshot_date": "2026-06-01",
  "target_month": "2026-07-01",
  "profile": {
    "tenure_months": 1,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 3,
    "has_credit_card": 0,
    "has_loan": 0
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 9,
      "balance_change_30d": -0.8796,
      "transaction_change_30d": 25.5141,
      "card_spend_change_30d": 5.6981,
      "app_login_change_30d": 0.4688,
      "salary_missing_days": 1.0,
      "external_transfer_change_30d": -1.7996,
      "upi_share_of_spend": 0.6522,
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
      "days_since_last_transaction": 6,
      "balance_change_30d": 0.8139,
      "transaction_change_30d": 34.0721,
      "card_spend_change_30d": 33.3655,
      "app_login_change_30d": 47.4547,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -56.0706,
      "upi_share_of_spend": 0.535,
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
      "balance_change_30d": 20.1784,
      "transaction_change_30d": 19.022,
      "card_spend_change_30d": 29.6772,
      "app_login_change_30d": 13.6799,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -12.0191,
      "upi_share_of_spend": 0.6159,
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
      "balance_change_30d": -13.8543,
      "transaction_change_30d": 14.6349,
      "card_spend_change_30d": -9.574,
      "app_login_change_30d": -3.5887,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": 21.8248,
      "upi_share_of_spend": 0.7153,
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
      "balance_change_30d": -24.957,
      "transaction_change_30d": -29.0311,
      "card_spend_change_30d": -17.6073,
      "app_login_change_30d": 7.3149,
      "salary_missing_days": 4.0,
      "external_transfer_change_30d": -7.7578,
      "upi_share_of_spend": 0.7251,
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
      "balance_change_30d": 23.2716,
      "transaction_change_30d": 26.49,
      "card_spend_change_30d": 16.4971,
      "app_login_change_30d": 2.1351,
      "salary_missing_days": 2.0,
      "external_transfer_change_30d": -12.719,
      "upi_share_of_spend": 0.6794,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 25.6692,
      "emi_bounce_30d": 0
    }
  ],
  "customer": {
    "tenure_months": 1,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 3,
    "has_credit_card": 0,
    "has_loan": 0,
    "days_since_last_transaction": 7,
    "balance_change_30d": 23.2716,
    "transaction_change_30d": 26.49,
    "card_spend_change_30d": 16.4971,
    "app_login_change_30d": 2.1351,
    "salary_missing_days": 2.0,
    "external_transfer_change_30d": -12.719,
    "upi_share_of_spend": 0.6794,
    "fd_maturing_in_30d": 0,
    "products_dropped_90d": 0,
    "complaints_30d": 1,
    "unresolved_complaints": 0,
    "failed_transactions_30d": 0,
    "avg_resolution_time_hrs": 25.6692,
    "emi_bounce_30d": 0
  },
  "extra_context": {
    "customer_profile": {
      "segment": "salary",
      "income_regularity": "regular",
      "tenure_months": 1,
      "age": 48,
      "customer_yearly_value": 185807.3263,
      "products_count": 3,
      "has_credit_card": 0,
      "has_loan": 0,
      "value_tier": "high"
    },
    "recent_complaint_text": "Transaction pending since Monday. Rs 4,500 stuck. Please reverse it."
  }
}
```

Response:

```json
{
  "meta": {
    "endpoint": "/predict/both",
    "served_at": "2026-08-31T01:14:04",
    "elapsed_ms": 2250.43,
    "timings_ms": {
      "model1": 90.89,
      "model2": 2159.42
    },
    "customer_id": "C15320",
    "customer_name": "Tanmayi Barad",
    "snapshot_date": "2026-06-01"
  },
  "model1": {
    "churn_probability": 4.41,
    "raw_churn_probability": 35.95,
    "probability_mode": "sigmoid",
    "risk_score": 13.23,
    "churn_prediction": "No",
    "risk_level": "Low",
    "top_risk_factors": [
      {
        "factor": "latest_salary_missing_days",
        "value": 2.0,
        "message": "Salary or pension was delayed recently.",
        "contribution": 0.04667772352695465
      },
      {
        "factor": "external_transfer_change_30d_trend_6m",
        "value": 3.548151428571429,
        "message": "External transfers have increased.",
        "contribution": 0.03908498212695122
      },
      {
        "factor": "latest_upi_share_of_spend",
        "value": 0.6794,
        "message": "A larger share of spending is happening through UPI.",
        "contribution": 0.03590921312570572
      },
      {
        "factor": "transaction_change_30d_trend_6m",
        "value": -5.394777142857144,
        "message": "Transaction activity has been falling across recent months.",
        "contribution": 0.02444448322057724
      },
      {
        "factor": "latest_vs_avg_upi_share_of_spend_available_history",
        "value": 0.02558333333333329,
        "message": "A larger share of spending is happening through UPI.",
        "contribution": 0.022976433858275414
      }
    ]
  },
  "model2_input": {
    "customer_context": {
      "age": 48,
      "tenure_months": 1,
      "customer_segment": "salary",
      "income_regularity": "regular",
      "customer_yearly_value": 185807.3263,
      "products_count": 3,
      "has_credit_card": 0,
      "has_loan": 0
    },
    "behavior": {
      "days_since_last_transaction": 7,
      "balance_change_30d": 23.2716,
      "transaction_change_30d": 26.49,
      "card_spend_change_30d": 16.4971,
      "app_login_change_30d": 2.1351,
      "salary_missing_days": 2,
      "external_transfer_change_30d": -12.719,
      "upi_share_of_spend": 0.6794,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "emi_bounce_30d": 0
    },
    "service_evidence": {
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 25.6692,
      "complaint_text": "Transaction pending since Monday. Rs 4,500 stuck. Please reverse it."
    },
    "model1": {
      "churn_probability": 0.0441,
      "churn_prediction": "No",
      "risk_level": "Low",
      "top_risk_factors": [
        {
          "factor": "salary_missing_days",
          "value": 2.0
        },
        {
          "factor": "external_transfer_change_30d_trend_6m",
          "value": 3.548151428571429
        },
        {
          "factor": "upi_share_of_spend",
          "value": 0.6794
        },
        {
          "factor": "transaction_change_30d_trend_6m",
          "value": -5.394777142857144
        },
        {
          "factor": "vs_avg_upi_share_of_spend_available_history",
          "value": 0.02558333333333329
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
    "case_id": "C15320"
  },
  "model2": {
    "case_id": "C15320",
    "ok": true,
    "prediction": {
      "evidence": [
        "complaints_30d=1",
        "failed_transactions_30d=0",
        "avg_resolution_time_hrs=25.7",
        "transaction_change_30d_trend_6m=-5.4"
      ],
      "primary_reason": "UNKNOWN",
      "reasoning_summary": "Evidence is mixed or weak, so the cause remains unknown. The current relationship looks stable overall.",
      "recommended_action": "MONITOR",
      "secondary_reasons": [
        "FINANCIAL_STRESS"
      ],
      "urgency": "MEDIUM"
    },
    "raw_text": "{\n\"evidence\":[\"complaints_30d=1\",\"failed_transactions_30d=0\",\"avg_resolution_time_hrs=25.7\",\"transaction_change_30d_trend_6m=-5.4\"],\"primary_reason\":\"UNKNOWN\",\"reasoning_summary\":\"Evidence is mixed or weak, so the cause remains unknown. The current relationship looks stable overall.\",\"recommended_action\":\"MONITOR\",\"secondary_reasons\":[\"FINANCIAL_STRESS\"],\"urgency\":\"MEDIUM\"\n}",
    "error": null,
    "latency_s": 2.1574,
    "simple_output": "Reason: UNKNOWN | Urgency: MEDIUM | Action: MONITOR | Why: Evidence is mixed or weak, so the cause remains unknown. The current relationship looks stable overall."
  }
}
```

### Fiyaz Goel (`C15871`)

- OK: `True`
- Shape errors: `[]`
- Simple output: Reason: SERVICE_DISSATISFACTION | Urgency: MEDIUM | Action: SERVICE_RECOVERY | Why: Service friction is the clearest risk signal here. Complaint escalation fits because complaints_30d=1 and failed_transactions_30d=1 indicate the issue is unresolved or operationally serious.

Request:

```json
{
  "customer_id": "C15871",
  "customer_name": "Fiyaz Goel",
  "prediction_date": "2026-06-01",
  "snapshot_date": "2026-06-01",
  "target_month": "2026-07-01",
  "profile": {
    "tenure_months": 49,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 3,
    "has_credit_card": 0,
    "has_loan": 1
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 11,
      "balance_change_30d": -6.7622,
      "transaction_change_30d": -13.0825,
      "card_spend_change_30d": -5.4518,
      "app_login_change_30d": -15.4852,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": 7.3173,
      "upi_share_of_spend": 0.0516,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 1,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 18.7235,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-02-01",
      "days_since_last_transaction": 5,
      "balance_change_30d": 21.6196,
      "transaction_change_30d": -7.3247,
      "card_spend_change_30d": 39.7109,
      "app_login_change_30d": 34.9384,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": 8.1015,
      "upi_share_of_spend": 0.1073,
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
      "days_since_last_transaction": 9,
      "balance_change_30d": 4.0063,
      "transaction_change_30d": -7.6916,
      "card_spend_change_30d": 26.404,
      "app_login_change_30d": 35.2852,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -39.1468,
      "upi_share_of_spend": 0.2329,
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
      "balance_change_30d": -12.1398,
      "transaction_change_30d": 5.3148,
      "card_spend_change_30d": 20.9081,
      "app_login_change_30d": 2.2108,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -5.6672,
      "upi_share_of_spend": 0.2583,
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
      "days_since_last_transaction": 12,
      "balance_change_30d": 4.8655,
      "transaction_change_30d": 4.6658,
      "card_spend_change_30d": 22.9204,
      "app_login_change_30d": 10.6134,
      "salary_missing_days": 1.0,
      "external_transfer_change_30d": 19.0364,
      "upi_share_of_spend": 0.1908,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 3,
      "avg_resolution_time_hrs": 2.1709,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-06-01",
      "days_since_last_transaction": 14,
      "balance_change_30d": -19.1275,
      "transaction_change_30d": -9.1929,
      "card_spend_change_30d": 0.7227,
      "app_login_change_30d": -1.4837,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": 3.3687,
      "upi_share_of_spend": 0.1655,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 19.9487,
      "emi_bounce_30d": 0
    }
  ],
  "customer": {
    "tenure_months": 49,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 3,
    "has_credit_card": 0,
    "has_loan": 1,
    "days_since_last_transaction": 14,
    "balance_change_30d": -19.1275,
    "transaction_change_30d": -9.1929,
    "card_spend_change_30d": 0.7227,
    "app_login_change_30d": -1.4837,
    "salary_missing_days": 0.0,
    "external_transfer_change_30d": 3.3687,
    "upi_share_of_spend": 0.1655,
    "fd_maturing_in_30d": 0,
    "products_dropped_90d": 0,
    "complaints_30d": 1,
    "unresolved_complaints": 0,
    "failed_transactions_30d": 1,
    "avg_resolution_time_hrs": 19.9487,
    "emi_bounce_30d": 0
  },
  "extra_context": {
    "customer_profile": {
      "segment": "salary",
      "income_regularity": "regular",
      "tenure_months": 49,
      "age": 41,
      "customer_yearly_value": 79598.4039,
      "products_count": 3,
      "has_credit_card": 0,
      "has_loan": 1,
      "value_tier": "medium"
    },
    "recent_complaint_text": "ATM receipt shows balance different from passbook. Please clarify."
  }
}
```

Response:

```json
{
  "meta": {
    "endpoint": "/predict/both",
    "served_at": "2026-08-31T01:14:07",
    "elapsed_ms": 2965.09,
    "timings_ms": {
      "model1": 188.71,
      "model2": 2776.26
    },
    "customer_id": "C15871",
    "customer_name": "Fiyaz Goel",
    "snapshot_date": "2026-06-01"
  },
  "model1": {
    "churn_probability": 8.9,
    "raw_churn_probability": 52.06,
    "probability_mode": "sigmoid",
    "risk_score": 26.69,
    "churn_prediction": "No",
    "risk_level": "Low",
    "top_risk_factors": [
      {
        "factor": "latest_days_since_last_transaction",
        "value": 14,
        "message": "Customer has gone longer without transacting.",
        "contribution": 0.4865199029445648
      },
      {
        "factor": "days_since_last_transaction_trend_6m",
        "value": 1.257142857142857,
        "message": "Customer has gone longer without transacting.",
        "contribution": 0.14686331152915955
      },
      {
        "factor": "latest_balance_change_30d",
        "value": -19.1275,
        "message": "Balance has been falling across recent months.",
        "contribution": 0.11221093684434891
      },
      {
        "factor": "latest_vs_avg_balance_change_30d_available_history",
        "value": -17.87115,
        "message": "Balance has been falling across recent months.",
        "contribution": 0.0393618606030941
      },
      {
        "factor": "max_days_since_last_transaction_3m",
        "value": 17.0,
        "message": "Customer has gone longer without transacting.",
        "contribution": 0.024669550359249115
      }
    ]
  },
  "model2_input": {
    "customer_context": {
      "age": 41,
      "tenure_months": 49,
      "customer_segment": "salary",
      "income_regularity": "regular",
      "customer_yearly_value": 79598.4039,
      "products_count": 3,
      "has_credit_card": 0,
      "has_loan": 1
    },
    "behavior": {
      "days_since_last_transaction": 14,
      "balance_change_30d": -19.1275,
      "transaction_change_30d": -9.1929,
      "card_spend_change_30d": 0.7227,
      "app_login_change_30d": -1.4837,
      "salary_missing_days": 0,
      "external_transfer_change_30d": 3.3687,
      "upi_share_of_spend": 0.1655,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "emi_bounce_30d": 0
    },
    "service_evidence": {
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 19.9487,
      "complaint_text": "ATM receipt shows balance different from passbook. Please clarify."
    },
    "model1": {
      "churn_probability": 0.089,
      "churn_prediction": "No",
      "risk_level": "Low",
      "top_risk_factors": [
        {
          "factor": "days_since_last_transaction",
          "value": 14
        },
        {
          "factor": "days_since_last_transaction_trend_6m",
          "value": 1.257142857142857
        },
        {
          "factor": "balance_change_30d",
          "value": -19.1275
        },
        {
          "factor": "vs_avg_balance_change_30d_available_history",
          "value": -17.87115
        },
        {
          "factor": "max_days_since_last_transaction_3m",
          "value": 17.0
        }
      ]
    },
    "eligible_actions": [
      "MONITOR",
      "RE_ENGAGEMENT",
      "PRODUCT_REVIEW",
      "SERVICE_RECOVERY"
    ],
    "case_id": "C15871"
  },
  "model2": {
    "case_id": "C15871",
    "ok": true,
    "prediction": {
      "evidence": [
        "complaints_30d=1",
        "failed_transactions_30d=1",
        "avg_resolution_time_hrs=19.9",
        "complaint_text describes a recent service issue"
      ],
      "primary_reason": "SERVICE_DISSATISFACTION",
      "reasoning_summary": "Service friction is the clearest risk signal here. Complaint escalation fits because complaints_30d=1 and failed_transactions_30d=1 indicate the issue is unresolved or operationally serious.",
      "recommended_action": "SERVICE_RECOVERY",
      "secondary_reasons": [
        "UNKNOWN"
      ],
      "urgency": "MEDIUM"
    },
    "raw_text": "{\"evidence\":[\"complaints_30d=1\",\"failed_transactions_30d=1\",\"avg_resolution_time_hrs=19.9\",\"complaint_text describes a recent service issue\"],\"primary_reason\":\"SERVICE_DISSATISFACTION\",\"reasoning_summary\":\"Service friction is the clearest risk signal here. Complaint escalation fits because complaints_30d=1 and failed_transactions_30d=1 indicate the issue is unresolved or operationally serious.\",\"recommended_action\":\"SERVICE_RECOVERY\",\"secondary_reasons\":[\"UNKNOWN\"],\"urgency\":\"MEDIUM\"}",
    "error": null,
    "latency_s": 2.7761,
    "simple_output": "Reason: SERVICE_DISSATISFACTION | Urgency: MEDIUM | Action: SERVICE_RECOVERY | Why: Service friction is the clearest risk signal here. Complaint escalation fits because complaints_30d=1 and failed_transactions_30d=1 indicate the issue is unresolved or operationally serious."
  }
}
```

### Tristan Pall (`C16970`)

- OK: `True`
- Shape errors: `[]`
- Simple output: Reason: UNKNOWN | Urgency: MEDIUM | Action: MONITOR | Why: Evidence is mixed or weak, so the cause remains unknown. The relationship looks stable overall but there are some concerning signals too.

Request:

```json
{
  "customer_id": "C16970",
  "customer_name": "Tristan Pall",
  "prediction_date": "2026-06-01",
  "snapshot_date": "2026-06-01",
  "target_month": "2026-07-01",
  "profile": {
    "tenure_months": 42,
    "customer_segment": "vendor",
    "income_regularity": "irregular",
    "products_count": 2,
    "has_credit_card": 1,
    "has_loan": 0
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 2,
      "balance_change_30d": -6.6723,
      "transaction_change_30d": 11.3767,
      "card_spend_change_30d": -7.7254,
      "app_login_change_30d": 1.5836,
      "salary_missing_days": null,
      "external_transfer_change_30d": -2.3974,
      "upi_share_of_spend": 0.0848,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 1,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 44.8804,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-02-01",
      "days_since_last_transaction": 3,
      "balance_change_30d": 0.8481,
      "transaction_change_30d": 27.9081,
      "card_spend_change_30d": -21.2266,
      "app_login_change_30d": 19.7439,
      "salary_missing_days": null,
      "external_transfer_change_30d": 17.9605,
      "upi_share_of_spend": 0.1386,
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
      "balance_change_30d": -34.6659,
      "transaction_change_30d": -33.3782,
      "card_spend_change_30d": -42.2044,
      "app_login_change_30d": -64.4417,
      "salary_missing_days": null,
      "external_transfer_change_30d": 96.5751,
      "upi_share_of_spend": 0.2549,
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
      "days_since_last_transaction": 24,
      "balance_change_30d": -44.3858,
      "transaction_change_30d": -66.1006,
      "card_spend_change_30d": -31.2479,
      "app_login_change_30d": -58.9628,
      "salary_missing_days": null,
      "external_transfer_change_30d": 52.8415,
      "upi_share_of_spend": 0.3413,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 1,
      "complaints_30d": 3,
      "unresolved_complaints": 2,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 53.5858,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-05-01",
      "days_since_last_transaction": 19,
      "balance_change_30d": -67.1957,
      "transaction_change_30d": -60.9774,
      "card_spend_change_30d": -48.3481,
      "app_login_change_30d": -56.4896,
      "salary_missing_days": null,
      "external_transfer_change_30d": 104.3897,
      "upi_share_of_spend": 0.3947,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 1,
      "complaints_30d": 0,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 5,
      "avg_resolution_time_hrs": 0.0,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-06-01",
      "days_since_last_transaction": 26,
      "balance_change_30d": -82.8568,
      "transaction_change_30d": -78.4709,
      "card_spend_change_30d": -73.3071,
      "app_login_change_30d": -94.2098,
      "salary_missing_days": null,
      "external_transfer_change_30d": 107.3782,
      "upi_share_of_spend": 0.4907,
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
    "tenure_months": 42,
    "customer_segment": "vendor",
    "income_regularity": "irregular",
    "products_count": 2,
    "has_credit_card": 1,
    "has_loan": 0,
    "days_since_last_transaction": 26,
    "balance_change_30d": -82.8568,
    "transaction_change_30d": -78.4709,
    "card_spend_change_30d": -73.3071,
    "app_login_change_30d": -94.2098,
    "salary_missing_days": null,
    "external_transfer_change_30d": 107.3782,
    "upi_share_of_spend": 0.4907,
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
      "tenure_months": 42,
      "age": 39,
      "customer_yearly_value": 17350.6937,
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
    "served_at": "2026-08-31T01:14:10",
    "elapsed_ms": 3558.19,
    "timings_ms": {
      "model1": 157.65,
      "model2": 3400.41
    },
    "customer_id": "C16970",
    "customer_name": "Tristan Pall",
    "snapshot_date": "2026-06-01"
  },
  "model1": {
    "churn_probability": 42.95,
    "raw_churn_probability": 95.92,
    "probability_mode": "sigmoid",
    "risk_score": 78.61,
    "churn_prediction": "Yes",
    "risk_level": "High",
    "top_risk_factors": [
      {
        "factor": "latest_days_since_last_transaction",
        "value": 26,
        "message": "Customer has gone longer without transacting.",
        "contribution": 0.5748643279075623
      },
      {
        "factor": "latest_transaction_change_30d",
        "value": -78.4709,
        "message": "Transaction activity has been falling across recent months.",
        "contribution": 0.4159342050552368
      },
      {
        "factor": "latest_vs_avg_upi_share_of_spend_available_history",
        "value": 0.20653333333333335,
        "message": "A larger share of spending is happening through UPI.",
        "contribution": 0.24237416684627533
      },
      {
        "factor": "latest_balance_change_30d",
        "value": -82.8568,
        "message": "Balance has been falling across recent months.",
        "contribution": 0.22838260233402252
      },
      {
        "factor": "sum_failed_transactions_30d_3m",
        "value": 7.0,
        "message": "Customer has recent failed transactions.",
        "contribution": 0.20134897530078888
      }
    ]
  },
  "model2_input": {
    "customer_context": {
      "age": 39,
      "tenure_months": 42,
      "customer_segment": "vendor",
      "income_regularity": "irregular",
      "customer_yearly_value": 17350.6937,
      "products_count": 2,
      "has_credit_card": 1,
      "has_loan": 0
    },
    "behavior": {
      "days_since_last_transaction": 26,
      "balance_change_30d": -82.8568,
      "transaction_change_30d": -78.4709,
      "card_spend_change_30d": -73.3071,
      "app_login_change_30d": -94.2098,
      "salary_missing_days": null,
      "external_transfer_change_30d": 107.3782,
      "upi_share_of_spend": 0.4907,
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
      "churn_probability": 0.4295,
      "churn_prediction": "Yes",
      "risk_level": "High",
      "top_risk_factors": [
        {
          "factor": "days_since_last_transaction",
          "value": 26
        },
        {
          "factor": "transaction_change_30d",
          "value": -78.4709
        },
        {
          "factor": "vs_avg_upi_share_of_spend_available_history",
          "value": 0.20653333333333335
        },
        {
          "factor": "balance_change_30d",
          "value": -82.8568
        },
        {
          "factor": "sum_failed_transactions_30d_3m",
          "value": 7.0
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
    "case_id": "C16970"
  },
  "model2": {
    "case_id": "C16970",
    "ok": true,
    "prediction": {
      "evidence": [
        "complaints_30d=0",
        "unresolved_complaints=0",
        "avg_resolution_time_hrs=0.0",
        "failed_transactions_30d=1"
      ],
      "primary_reason": "UNKNOWN",
      "reasoning_summary": "Evidence is mixed or weak, so the cause remains unknown. The relationship looks stable overall but there are some concerning signals too.",
      "recommended_action": "MONITOR",
      "secondary_reasons": [
        "SERVICE_DISSATISFACTION",
        "TEMPORARY_SEASONAL_CHANGE"
      ],
      "urgency": "MEDIUM"
    },
    "raw_text": "{\n    \"evidence\": [\n        \"complaints_30d=0\",\n        \"unresolved_complaints=0\",\n        \"avg_resolution_time_hrs=0.0\",\n        \"failed_transactions_30d=1\"\n    ],\n    \"primary_reason\": \"UNKNOWN\",\n    \"reasoning_summary\": \"Evidence is mixed or weak, so the cause remains unknown. The relationship looks stable overall but there are some concerning signals too.\",\n    \"recommended_action\": \"MONITOR\",\n    \"secondary_reasons\": [\n        \"SERVICE_DISSATISFACTION\",\n        \"TEMPORARY_SEASONAL_CHANGE\"\n    ],\n    \"urgency\": \"MEDIUM\"\n}",
    "error": null,
    "latency_s": 3.4001,
    "simple_output": "Reason: UNKNOWN | Urgency: MEDIUM | Action: MONITOR | Why: Evidence is mixed or weak, so the cause remains unknown. The relationship looks stable overall but there are some concerning signals too."
  }
}
```

### Zarna Prabhakar (`C18154`)

- OK: `True`
- Shape errors: `[]`
- Simple output: Reason: UNKNOWN | Urgency: MEDIUM | Action: MONITOR | Why: Evidence is mixed or weak, so the cause remains unknown. The current relationship looks healthy overall but warrants further monitoring.

Request:

```json
{
  "customer_id": "C18154",
  "customer_name": "Zarna Prabhakar",
  "prediction_date": "2026-06-01",
  "snapshot_date": "2026-06-01",
  "target_month": "2026-07-01",
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
      "days_since_last_transaction": 5,
      "balance_change_30d": 24.2033,
      "transaction_change_30d": -15.536,
      "card_spend_change_30d": 58.643,
      "app_login_change_30d": 16.0031,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -42.4196,
      "upi_share_of_spend": 0.6355,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 2,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 2,
      "avg_resolution_time_hrs": 22.5488,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-02-01",
      "days_since_last_transaction": 5,
      "balance_change_30d": 27.5817,
      "transaction_change_30d": 23.8266,
      "card_spend_change_30d": 24.3969,
      "app_login_change_30d": 28.3756,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -55.7039,
      "upi_share_of_spend": 0.6054,
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
      "balance_change_30d": 16.8651,
      "transaction_change_30d": 27.8394,
      "card_spend_change_30d": 29.101,
      "app_login_change_30d": 25.0769,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": 13.0901,
      "upi_share_of_spend": 0.5958,
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
      "balance_change_30d": 44.9414,
      "transaction_change_30d": 22.7767,
      "card_spend_change_30d": 9.3605,
      "app_login_change_30d": 44.4745,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -33.6293,
      "upi_share_of_spend": 0.6676,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 8.1876,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-05-01",
      "days_since_last_transaction": 2,
      "balance_change_30d": 34.6264,
      "transaction_change_30d": 36.8215,
      "card_spend_change_30d": 41.2484,
      "app_login_change_30d": 30.9759,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -20.2613,
      "upi_share_of_spend": 0.5395,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 17.3335,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-06-01",
      "days_since_last_transaction": 0,
      "balance_change_30d": 41.3829,
      "transaction_change_30d": 44.5675,
      "card_spend_change_30d": 48.4477,
      "app_login_change_30d": 34.7381,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -45.5328,
      "upi_share_of_spend": 0.5576,
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
    "tenure_months": 41,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 2,
    "has_credit_card": 1,
    "has_loan": 0,
    "days_since_last_transaction": 0,
    "balance_change_30d": 41.3829,
    "transaction_change_30d": 44.5675,
    "card_spend_change_30d": 48.4477,
    "app_login_change_30d": 34.7381,
    "salary_missing_days": 0.0,
    "external_transfer_change_30d": -45.5328,
    "upi_share_of_spend": 0.5576,
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
      "tenure_months": 41,
      "age": 44,
      "customer_yearly_value": 46841.7135,
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
    "served_at": "2026-08-31T01:14:13",
    "elapsed_ms": 2666.58,
    "timings_ms": {
      "model1": 149.99,
      "model2": 2516.43
    },
    "customer_id": "C18154",
    "customer_name": "Zarna Prabhakar",
    "snapshot_date": "2026-06-01"
  },
  "model1": {
    "churn_probability": 1.49,
    "raw_churn_probability": 11.98,
    "probability_mode": "sigmoid",
    "risk_score": 4.47,
    "churn_prediction": "No",
    "risk_level": "Low",
    "top_risk_factors": [
      {
        "factor": "avg_balance_change_30d_6m",
        "value": 31.600133333333332,
        "message": "This signal increased churn risk.",
        "contribution": 0.054283689707517624
      },
      {
        "factor": "latest_external_transfer_change_30d",
        "value": -45.5328,
        "message": "This signal increased churn risk.",
        "contribution": 0.0542822889983654
      },
      {
        "factor": "max_salary_missing_days_6m",
        "value": 0.0,
        "message": "This signal increased churn risk.",
        "contribution": 0.03678969666361809
      },
      {
        "factor": "latest_upi_share_of_spend",
        "value": 0.5576,
        "message": "A larger share of spending is happening through UPI.",
        "contribution": 0.03624255582690239
      },
      {
        "factor": "avg_transaction_change_30d_6m",
        "value": 23.382616666666667,
        "message": "This signal increased churn risk.",
        "contribution": 0.02878054976463318
      }
    ]
  },
  "model2_input": {
    "customer_context": {
      "age": 44,
      "tenure_months": 41,
      "customer_segment": "salary",
      "income_regularity": "regular",
      "customer_yearly_value": 46841.7135,
      "products_count": 2,
      "has_credit_card": 1,
      "has_loan": 0
    },
    "behavior": {
      "days_since_last_transaction": 0,
      "balance_change_30d": 41.3829,
      "transaction_change_30d": 44.5675,
      "card_spend_change_30d": 48.4477,
      "app_login_change_30d": 34.7381,
      "salary_missing_days": 0,
      "external_transfer_change_30d": -45.5328,
      "upi_share_of_spend": 0.5576,
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
      "churn_probability": 0.0149,
      "churn_prediction": "No",
      "risk_level": "Low",
      "top_risk_factors": [
        {
          "factor": "avg_balance_change_30d_6m",
          "value": 31.600133333333332
        },
        {
          "factor": "external_transfer_change_30d",
          "value": -45.5328
        },
        {
          "factor": "max_salary_missing_days_6m",
          "value": 0.0
        },
        {
          "factor": "upi_share_of_spend",
          "value": 0.5576
        },
        {
          "factor": "avg_transaction_change_30d_6m",
          "value": 23.382616666666667
        }
      ]
    },
    "eligible_actions": [
      "MONITOR",
      "RE_ENGAGEMENT",
      "PRODUCT_REVIEW"
    ],
    "case_id": "C18154"
  },
  "model2": {
    "case_id": "C18154",
    "ok": true,
    "prediction": {
      "evidence": [
        "complaints_30d=0",
        "failed_transactions_30d=0",
        "avg_resolution_time_hrs=0.0"
      ],
      "primary_reason": "UNKNOWN",
      "reasoning_summary": "Evidence is mixed or weak, so the cause remains unknown. The current relationship looks healthy overall but warrants further monitoring.",
      "recommended_action": "MONITOR",
      "secondary_reasons": [
        "SERVICE_DISSATISFACTION"
      ],
      "urgency": "MEDIUM"
    },
    "raw_text": "{\n    \"evidence\": [\"complaints_30d=0\", \"failed_transactions_30d=0\", \"avg_resolution_time_hrs=0.0\"],\n    \"primary_reason\": \"UNKNOWN\",\n    \"reasoning_summary\": \"Evidence is mixed or weak, so the cause remains unknown. The current relationship looks healthy overall but warrants further monitoring.\",\n    \"recommended_action\": \"MONITOR\",\n    \"secondary_reasons\": [\"SERVICE_DISSATISFACTION\"],\n    \"urgency\": \"MEDIUM\"\n}",
    "error": null,
    "latency_s": 2.5161,
    "simple_output": "Reason: UNKNOWN | Urgency: MEDIUM | Action: MONITOR | Why: Evidence is mixed or weak, so the cause remains unknown. The current relationship looks healthy overall but warrants further monitoring."
  }
}
```

### Forum Dutt (`C19609`)

- OK: `True`
- Shape errors: `[]`
- Simple output: Reason: UNKNOWN | Urgency: MEDIUM | Action: MONITOR | Why: Evidence is mixed or weak, so the cause remains unknown. The current relationship stage and product setup suggest this could be a monitoring-level issue.

Request:

```json
{
  "customer_id": "C19609",
  "customer_name": "Forum Dutt",
  "prediction_date": "2026-05-01",
  "snapshot_date": "2026-05-01",
  "target_month": "2026-06-01",
  "profile": {
    "tenure_months": 53,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 2,
    "has_credit_card": 0,
    "has_loan": 0
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 7,
      "balance_change_30d": 5.7468,
      "transaction_change_30d": 11.9504,
      "card_spend_change_30d": 15.9127,
      "app_login_change_30d": -5.0089,
      "salary_missing_days": 3.0,
      "external_transfer_change_30d": -0.8198,
      "upi_share_of_spend": 0.1795,
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
      "balance_change_30d": -6.025,
      "transaction_change_30d": 18.7029,
      "card_spend_change_30d": 24.8677,
      "app_login_change_30d": -21.4585,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -13.0369,
      "upi_share_of_spend": 0.1739,
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
      "days_since_last_transaction": 17,
      "balance_change_30d": -20.1884,
      "transaction_change_30d": -21.0332,
      "card_spend_change_30d": -28.8765,
      "app_login_change_30d": -11.9269,
      "salary_missing_days": 3.0,
      "external_transfer_change_30d": 46.4837,
      "upi_share_of_spend": 0.2292,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 4,
      "avg_resolution_time_hrs": 7.1475,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-04-01",
      "days_since_last_transaction": 14,
      "balance_change_30d": -4.893,
      "transaction_change_30d": -26.5677,
      "card_spend_change_30d": -36.2893,
      "app_login_change_30d": -33.5483,
      "salary_missing_days": 4.0,
      "external_transfer_change_30d": 37.414,
      "upi_share_of_spend": 0.2295,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 0,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 3,
      "avg_resolution_time_hrs": 0.0,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-05-01",
      "days_since_last_transaction": 15,
      "balance_change_30d": -28.5224,
      "transaction_change_30d": -4.5432,
      "card_spend_change_30d": -37.9867,
      "app_login_change_30d": -18.7497,
      "salary_missing_days": 5.0,
      "external_transfer_change_30d": 17.0272,
      "upi_share_of_spend": 0.2765,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 1,
      "complaints_30d": 0,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 3,
      "avg_resolution_time_hrs": 0.0,
      "emi_bounce_30d": 0
    }
  ],
  "customer": {
    "tenure_months": 53,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 2,
    "has_credit_card": 0,
    "has_loan": 0,
    "days_since_last_transaction": 15,
    "balance_change_30d": -28.5224,
    "transaction_change_30d": -4.5432,
    "card_spend_change_30d": -37.9867,
    "app_login_change_30d": -18.7497,
    "salary_missing_days": 5.0,
    "external_transfer_change_30d": 17.0272,
    "upi_share_of_spend": 0.2765,
    "fd_maturing_in_30d": 0,
    "products_dropped_90d": 1,
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
      "tenure_months": 53,
      "age": 30,
      "customer_yearly_value": 53615.6652,
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
    "served_at": "2026-08-31T01:14:16",
    "elapsed_ms": 3441.39,
    "timings_ms": {
      "model1": 157.94,
      "model2": 3283.31
    },
    "customer_id": "C19609",
    "customer_name": "Forum Dutt",
    "snapshot_date": "2026-05-01"
  },
  "model1": {
    "churn_probability": 34.19,
    "raw_churn_probability": 87.96,
    "probability_mode": "sigmoid",
    "risk_score": 75.32,
    "churn_prediction": "Yes",
    "risk_level": "High",
    "top_risk_factors": [
      {
        "factor": "latest_days_since_last_transaction",
        "value": 15,
        "message": "Customer has gone longer without transacting.",
        "contribution": 0.4645664691925049
      },
      {
        "factor": "latest_salary_missing_days",
        "value": 5.0,
        "message": "Salary or pension was delayed recently.",
        "contribution": 0.24654217064380646
      },
      {
        "factor": "sum_failed_transactions_30d_3m",
        "value": 10.0,
        "message": "Customer has recent failed transactions.",
        "contribution": 0.23348432779312134
      },
      {
        "factor": "days_since_last_transaction_trend_6m",
        "value": 2.5,
        "message": "Customer has gone longer without transacting.",
        "contribution": 0.21917486190795898
      },
      {
        "factor": "latest_vs_avg_upi_share_of_spend_available_history",
        "value": 0.05878000000000003,
        "message": "A larger share of spending is happening through UPI.",
        "contribution": 0.18760992586612701
      }
    ]
  },
  "model2_input": {
    "customer_context": {
      "age": 30,
      "tenure_months": 53,
      "customer_segment": "salary",
      "income_regularity": "regular",
      "customer_yearly_value": 53615.6652,
      "products_count": 2,
      "has_credit_card": 0,
      "has_loan": 0
    },
    "behavior": {
      "days_since_last_transaction": 15,
      "balance_change_30d": -28.5224,
      "transaction_change_30d": -4.5432,
      "card_spend_change_30d": -37.9867,
      "app_login_change_30d": -18.7497,
      "salary_missing_days": 5,
      "external_transfer_change_30d": 17.0272,
      "upi_share_of_spend": 0.2765,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 1,
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
      "churn_probability": 0.3419,
      "churn_prediction": "Yes",
      "risk_level": "High",
      "top_risk_factors": [
        {
          "factor": "days_since_last_transaction",
          "value": 15
        },
        {
          "factor": "salary_missing_days",
          "value": 5.0
        },
        {
          "factor": "sum_failed_transactions_30d_3m",
          "value": 10.0
        },
        {
          "factor": "days_since_last_transaction_trend_6m",
          "value": 2.5
        },
        {
          "factor": "vs_avg_upi_share_of_spend_available_history",
          "value": 0.05878000000000003
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
    "case_id": "C19609"
  },
  "model2": {
    "case_id": "C19609",
    "ok": true,
    "prediction": {
      "evidence": [
        "complaints_30d=0",
        "unresolved_complaints=0",
        "avg_resolution_time_hrs=0.0",
        "failed_transactions_30d=3"
      ],
      "primary_reason": "UNKNOWN",
      "reasoning_summary": "Evidence is mixed or weak, so the cause remains unknown. The current relationship stage and product setup suggest this could be a monitoring-level issue.",
      "recommended_action": "MONITOR",
      "secondary_reasons": [
        "SERVICE_DISSATISFACTION",
        "TEMPORARY_SEASONAL_CHANGE"
      ],
      "urgency": "MEDIUM"
    },
    "raw_text": "{\n    \"evidence\": [\n        \"complaints_30d=0\",\n        \"unresolved_complaints=0\",\n        \"avg_resolution_time_hrs=0.0\",\n        \"failed_transactions_30d=3\"\n    ],\n    \"primary_reason\": \"UNKNOWN\",\n    \"reasoning_summary\": \"Evidence is mixed or weak, so the cause remains unknown. The current relationship stage and product setup suggest this could be a monitoring-level issue.\",\n    \"recommended_action\": \"MONITOR\",\n    \"secondary_reasons\": [\n        \"SERVICE_DISSATISFACTION\",\n        \"TEMPORARY_SEASONAL_CHANGE\"\n    ],\n    \"urgency\": \"MEDIUM\"\n}",
    "error": null,
    "latency_s": 3.2829,
    "simple_output": "Reason: UNKNOWN | Urgency: MEDIUM | Action: MONITOR | Why: Evidence is mixed or weak, so the cause remains unknown. The current relationship stage and product setup suggest this could be a monitoring-level issue."
  }
}
```
