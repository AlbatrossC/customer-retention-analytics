# Devang Model 1 -> Model 2 API Test Results

- API URL: `http://127.0.0.1:8001`
- Created at: `2026-08-31T00:57:11`
- Customers tested: `30`
- Source CSV: `model_1_v2\data\customers.csv`
- Health OK: `True`
- Ollama model: `devang-model2-q4`
- Model 1 loaded: `True`

## Summary

| # | Customer | Model 1 risk | Prediction | Reason | Urgency | Action | OK | Seconds |
|---:|---|---:|---|---|---|---|---|---:|
| 1 | Aishani Pau (`C10577`) | 4.55 | No | LOW_ENGAGEMENT | MEDIUM | RE_ENGAGEMENT | yes | 10.48 |
| 2 | Ishani Prashad (`C10754`) | 2.05 | No | LOW_ENGAGEMENT | MEDIUM | RE_ENGAGEMENT | yes | 6.04 |
| 3 | Gopal Bawa (`C11042`) | 2.32 | No | SERVICE_DISSATISFACTION | HIGH | SERVICE_RECOVERY | yes | 2.49 |
| 4 | Bakhshi Thakkar (`C11061`) | 34.74 | Yes | FEE_DISSATISFACTION | HIGH | FEE_WAIVER_REVIEW | yes | 2.71 |
| 5 | Vamakshi Barad (`C11364`) | 4.33 | No | LOW_ENGAGEMENT | MEDIUM | RE_ENGAGEMENT | yes | 3.24 |
| 6 | Nihal Hans (`C11655`) | 41.53 | Yes | FEE_DISSATISFACTION | HIGH | FEE_WAIVER_REVIEW | yes | 2.27 |
| 7 | Odika Rout (`C12376`) | 1.68 | No | SERVICE_DISSATISFACTION | HIGH | SERVICE_RECOVERY | yes | 2.57 |
| 8 | Dalbir Venkatesh (`C12383`) | 20.03 | Yes | FEE_DISSATISFACTION | HIGH | FEE_WAIVER_REVIEW | yes | 2.72 |
| 9 | Urmi Choudhary (`C13333`) | 3.72 | No | NA | NA | NA | no | 5.97 |
| 10 | Rohan Krishnan (`C13438`) | 3.0 | No | PRODUCT_MISMATCH | HIGH | PRODUCT_REVIEW | yes | 2.84 |
| 11 | Leena Mital (`C13500`) | 41.02 | Yes | FEE_DISSATISFACTION | HIGH | FEE_WAIVER_REVIEW | yes | 3.18 |
| 12 | Yashawini Konda (`C13668`) | 2.45 | No | LOW_ENGAGEMENT | MEDIUM | RE_ENGAGEMENT | yes | 3.44 |
| 13 | Lavanya Nanda (`C14004`) | 22.6 | Yes | FEE_DISSATISFACTION | HIGH | FEE_WAIVER_REVIEW | yes | 2.09 |
| 14 | Qabil Nori (`C14037`) | 33.33 | Yes | FEE_DISSATISFACTION | HIGH | FEE_WAIVER_REVIEW | yes | 2.38 |
| 15 | Bishakha Kar (`C14151`) | 1.37 | No | SERVICE_DISSATISFACTION | HIGH | SERVICE_RECOVERY | yes | 3.98 |
| 16 | Girish Babu (`C14437`) | 3.28 | No | LOW_ENGAGEMENT | MEDIUM | RE_ENGAGEMENT | yes | 2.05 |
| 17 | Bhavna D’Alia (`C14891`) | 15.58 | No | FEE_DISSATISFACTION | HIGH | FEE_WAIVER_REVIEW | yes | 2.25 |
| 18 | Warjas Dani (`C15022`) | 41.19 | Yes | FEE_DISSATISFACTION | HIGH | FEE_WAIVER_REVIEW | yes | 2.06 |
| 19 | Parth Salvi (`C15042`) | 2.71 | No | NA | NA | NA | no | 4.56 |
| 20 | Benjamin Kumer (`C15712`) | 34.24 | Yes | FEE_DISSATISFACTION | HIGH | FEE_WAIVER_REVIEW | yes | 2.5 |
| 21 | Xavier Atwal (`C15921`) | 1.97 | No | SERVICE_DISSATISFACTION | HIGH | SERVICE_RECOVERY | yes | 2.56 |
| 22 | Yashodhara Majumdar (`C15952`) | 44.32 | Yes | DIGITAL_FRICTION | HIGH | COMPLAINT_ESCALATION | yes | 4.68 |
| 23 | Anamika Bhat (`C17024`) | 27.07 | Yes | SERVICE_DISSATISFACTION | HIGH | SERVICE_RECOVERY | yes | 2.1 |
| 24 | Garima Nagi (`C17447`) | 27.76 | Yes | FEE_DISSATISFACTION | HIGH | FEE_WAIVER_REVIEW | yes | 2.2 |
| 25 | Aishani Vala (`C17772`) | 3.53 | No | SERVICE_DISSATISFACTION | HIGH | SERVICE_RECOVERY | yes | 2.12 |
| 26 | Amrita Bansal (`C18515`) | 2.04 | No | NA | NA | NA | no | 5.49 |
| 27 | Niharika Parekh (`C18846`) | 1.53 | No | SERVICE_DISSATISFACTION | HIGH | SERVICE_RECOVERY | yes | 3.08 |
| 28 | Vamakshi Kulkarni (`C19250`) | 6.99 | No | SERVICE_DISSATISFACTION | HIGH | SERVICE_RECOVERY | yes | 2.07 |
| 29 | Reva Kadakia (`C19323`) | 15.05 | No | DIGITAL_FRICTION | HIGH | COMPLAINT_ESCALATION | yes | 2.61 |
| 30 | Jagrati Chaudhry (`C19353`) | 2.42 | No | SERVICE_DISSATISFACTION | HIGH | SERVICE_RECOVERY | yes | 2.48 |

## Details

### Aishani Pau (`C10577`)

- OK: `True`
- Shape errors: `[]`
- Simple output: Reason: LOW_ENGAGEMENT | Urgency: MEDIUM | Action: RE_ENGAGEMENT | Why: Digital engagement decline without a clear issue suggests the relationship is losing momentum.

Request:

```json
{
  "customer_id": "C10577",
  "customer_name": "Aishani Pau",
  "prediction_date": "2026-06-01",
  "snapshot_date": "2026-06-01",
  "target_month": "2026-07-01",
  "profile": {
    "tenure_months": 42,
    "customer_segment": "pension",
    "income_regularity": "regular",
    "products_count": 2,
    "has_credit_card": 0,
    "has_loan": 0
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 6,
      "balance_change_30d": 8.8807,
      "transaction_change_30d": 3.1435,
      "card_spend_change_30d": 14.0269,
      "app_login_change_30d": 10.7566,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": 17.4951,
      "upi_share_of_spend": 0.4236,
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
      "balance_change_30d": 10.9717,
      "transaction_change_30d": 17.4973,
      "card_spend_change_30d": 29.7384,
      "app_login_change_30d": 3.8002,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": 22.7848,
      "upi_share_of_spend": 0.4586,
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
      "balance_change_30d": 20.7521,
      "transaction_change_30d": 22.7891,
      "card_spend_change_30d": 46.6292,
      "app_login_change_30d": 32.1168,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -14.8689,
      "upi_share_of_spend": 0.512,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 3,
      "unresolved_complaints": 1,
      "failed_transactions_30d": 3,
      "avg_resolution_time_hrs": 39.4301,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-04-01",
      "days_since_last_transaction": 11,
      "balance_change_30d": 7.4786,
      "transaction_change_30d": 24.0202,
      "card_spend_change_30d": -2.7,
      "app_login_change_30d": 22.486,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": 22.8578,
      "upi_share_of_spend": 0.5397,
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
      "balance_change_30d": -17.1742,
      "transaction_change_30d": 2.1151,
      "card_spend_change_30d": -8.7903,
      "app_login_change_30d": -34.6332,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -5.6689,
      "upi_share_of_spend": 0.5649,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 37.4584,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-06-01",
      "days_since_last_transaction": 11,
      "balance_change_30d": 15.5431,
      "transaction_change_30d": -10.0639,
      "card_spend_change_30d": -3.9848,
      "app_login_change_30d": -23.5861,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": 8.094,
      "upi_share_of_spend": 0.4912,
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
    "tenure_months": 42,
    "customer_segment": "pension",
    "income_regularity": "regular",
    "products_count": 2,
    "has_credit_card": 0,
    "has_loan": 0,
    "days_since_last_transaction": 11,
    "balance_change_30d": 15.5431,
    "transaction_change_30d": -10.0639,
    "card_spend_change_30d": -3.9848,
    "app_login_change_30d": -23.5861,
    "salary_missing_days": 0.0,
    "external_transfer_change_30d": 8.094,
    "upi_share_of_spend": 0.4912,
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
      "tenure_months": 42,
      "age": 58,
      "customer_yearly_value": 40064.0326,
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
    "served_at": "2026-08-31T00:55:42",
    "elapsed_ms": 10467.38,
    "timings_ms": {
      "model1": 102.84,
      "model2": 10364.39
    },
    "customer_id": "C10577",
    "customer_name": "Aishani Pau",
    "snapshot_date": "2026-06-01"
  },
  "model1": {
    "churn_probability": 4.55,
    "raw_churn_probability": 36.67,
    "probability_mode": "sigmoid",
    "risk_score": 13.66,
    "churn_prediction": "No",
    "risk_level": "Low",
    "top_risk_factors": [
      {
        "factor": "days_since_last_transaction_trend_6m",
        "value": 1.2285714285714284,
        "message": "Customer has gone longer without transacting.",
        "contribution": 0.14387959241867065
      },
      {
        "factor": "latest_app_login_change_30d",
        "value": -23.5861,
        "message": "App usage has been falling across recent months.",
        "contribution": 0.04681089147925377
      },
      {
        "factor": "avg_app_login_change_30d_3m",
        "value": -11.9111,
        "message": "App usage has been falling across recent months.",
        "contribution": 0.019846314564347267
      },
      {
        "factor": "avg_app_login_change_30d_6m",
        "value": 1.823383333333333,
        "message": "This signal increased churn risk.",
        "contribution": 0.015005537308752537
      },
      {
        "factor": "avg_card_spend_change_30d_3m",
        "value": -5.158366666666667,
        "message": "Card spending has been falling across recent months.",
        "contribution": 0.011882332153618336
      }
    ]
  },
  "model2_input": {
    "customer_context": {
      "age": 58,
      "tenure_months": 42,
      "customer_segment": "pension",
      "income_regularity": "regular",
      "customer_yearly_value": 40064.0326,
      "products_count": 2,
      "has_credit_card": 0,
      "has_loan": 0
    },
    "behavior": {
      "days_since_last_transaction": 11,
      "balance_change_30d": 15.5431,
      "transaction_change_30d": -10.0639,
      "card_spend_change_30d": -3.9848,
      "app_login_change_30d": -23.5861,
      "salary_missing_days": 0,
      "external_transfer_change_30d": 8.094,
      "upi_share_of_spend": 0.4912,
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
      "churn_probability": 0.0455,
      "churn_prediction": "No",
      "risk_level": "Low",
      "top_risk_factors": [
        {
          "factor": "days_since_last_transaction_trend_6m",
          "value": 1.2285714285714284
        },
        {
          "factor": "app_login_change_30d",
          "value": -23.5861
        },
        {
          "factor": "avg_app_login_change_30d_3m",
          "value": -11.9111
        },
        {
          "factor": "avg_app_login_change_30d_6m",
          "value": 1.823383333333333
        },
        {
          "factor": "avg_card_spend_change_30d_3m",
          "value": -5.158366666666667
        }
      ]
    },
    "eligible_actions": [
      "MONITOR",
      "RE_ENGAGEMENT",
      "PRODUCT_REVIEW"
    ],
    "case_id": "C10577"
  },
  "model2": {
    "case_id": "C10577",
    "ok": true,
    "prediction": {
      "evidence": [
        "complaints_30d=0",
        "unresolved_complaints=0",
        "avg_resolution_time_hrs=0.0",
        "complaint_text=None",
        "transaction_change_30d=-10.1",
        "balance_change_30d=15.5",
        "card_spend_change_30d=-4.0",
        "days_since_last_transaction=11"
      ],
      "primary_reason": "LOW_ENGAGEMENT",
      "reasoning_summary": "Digital engagement decline without a clear issue suggests the relationship is losing momentum.",
      "recommended_action": "RE_ENGAGEMENT",
      "secondary_reasons": [],
      "urgency": "MEDIUM"
    },
    "raw_text": "{\n  \"evidence\":[\"complaints_30d=0\",\"unresolved_complaints=0\",\"avg_resolution_time_hrs=0.0\",\"complaint_text=None\",\"transaction_change_30d=-10.1\",\"balance_change_30d=15.5\",\"card_spend_change_30d=-4.0\",\"days_since_last_transaction=11\"],\"primary_reason\":\"LOW_ENGAGEMENT\",\"reasoning_summary\":\"Digital engagement decline without a clear issue suggests the relationship is losing momentum.\",\"recommended_action\":\"RE_ENGAGEMENT\",\"secondary_reasons\":[],\"urgency\":\"MEDIUM\"}",
    "error": null,
    "latency_s": 10.3636,
    "simple_output": "Reason: LOW_ENGAGEMENT | Urgency: MEDIUM | Action: RE_ENGAGEMENT | Why: Digital engagement decline without a clear issue suggests the relationship is losing momentum."
  }
}
```

### Ishani Prashad (`C10754`)

- OK: `True`
- Shape errors: `[]`
- Simple output: Reason: LOW_ENGAGEMENT | Urgency: MEDIUM | Action: RE_ENGAGEMENT | Why: Digital engagement signals are weak or declining without a stronger problem signal to justify escalation. Evidence suggests this because complaints_30d=0, unresolved_complaints=0, failed_transactions_30d=0, avg_resolution_time_hrs=0.0.

Request:

```json
{
  "customer_id": "C10754",
  "customer_name": "Ishani Prashad",
  "prediction_date": "2026-06-01",
  "snapshot_date": "2026-06-01",
  "target_month": "2026-07-01",
  "profile": {
    "tenure_months": 50,
    "customer_segment": "farmer",
    "income_regularity": "seasonal",
    "products_count": 2,
    "has_credit_card": 0,
    "has_loan": 1
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 7,
      "balance_change_30d": -21.9337,
      "transaction_change_30d": -35.1033,
      "card_spend_change_30d": -20.8097,
      "app_login_change_30d": -24.994,
      "salary_missing_days": null,
      "external_transfer_change_30d": 40.5412,
      "upi_share_of_spend": 0.4197,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 10.4928,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-02-01",
      "days_since_last_transaction": 10,
      "balance_change_30d": -9.0244,
      "transaction_change_30d": -10.7045,
      "card_spend_change_30d": -5.8763,
      "app_login_change_30d": -11.32,
      "salary_missing_days": null,
      "external_transfer_change_30d": 0.233,
      "upi_share_of_spend": 0.4406,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 20.513,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-03-01",
      "days_since_last_transaction": 3,
      "balance_change_30d": 5.0652,
      "transaction_change_30d": 8.0013,
      "card_spend_change_30d": -23.3802,
      "app_login_change_30d": 17.9569,
      "salary_missing_days": null,
      "external_transfer_change_30d": -3.827,
      "upi_share_of_spend": 0.3712,
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
      "days_since_last_transaction": 4,
      "balance_change_30d": 10.3378,
      "transaction_change_30d": 9.0015,
      "card_spend_change_30d": -0.2486,
      "app_login_change_30d": -3.1384,
      "salary_missing_days": null,
      "external_transfer_change_30d": -21.7414,
      "upi_share_of_spend": 0.3858,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 1,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 14.5478,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-05-01",
      "days_since_last_transaction": 3,
      "balance_change_30d": -5.6741,
      "transaction_change_30d": 9.4867,
      "card_spend_change_30d": 6.7515,
      "app_login_change_30d": 10.4592,
      "salary_missing_days": null,
      "external_transfer_change_30d": 17.4983,
      "upi_share_of_spend": 0.3953,
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
      "days_since_last_transaction": 5,
      "balance_change_30d": -10.7914,
      "transaction_change_30d": 2.648,
      "card_spend_change_30d": 6.1116,
      "app_login_change_30d": 10.4398,
      "salary_missing_days": null,
      "external_transfer_change_30d": -28.453,
      "upi_share_of_spend": 0.3266,
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
    "tenure_months": 50,
    "customer_segment": "farmer",
    "income_regularity": "seasonal",
    "products_count": 2,
    "has_credit_card": 0,
    "has_loan": 1,
    "days_since_last_transaction": 5,
    "balance_change_30d": -10.7914,
    "transaction_change_30d": 2.648,
    "card_spend_change_30d": 6.1116,
    "app_login_change_30d": 10.4398,
    "salary_missing_days": null,
    "external_transfer_change_30d": -28.453,
    "upi_share_of_spend": 0.3266,
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
      "tenure_months": 50,
      "age": 44,
      "customer_yearly_value": 6883.3402,
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
    "served_at": "2026-08-31T00:55:48",
    "elapsed_ms": 6032.84,
    "timings_ms": {
      "model1": 165.95,
      "model2": 5866.74
    },
    "customer_id": "C10754",
    "customer_name": "Ishani Prashad",
    "snapshot_date": "2026-06-01"
  },
  "model1": {
    "churn_probability": 2.05,
    "raw_churn_probability": 19.02,
    "probability_mode": "sigmoid",
    "risk_score": 6.16,
    "churn_prediction": "No",
    "risk_level": "Low",
    "top_risk_factors": [
      {
        "factor": "count_balance_drop_6m",
        "value": 4,
        "message": "This signal increased churn risk.",
        "contribution": 0.05400794371962547
      },
      {
        "factor": "latest_vs_avg_external_transfer_change_30d_available_history",
        "value": -29.161516666666667,
        "message": "This signal increased churn risk.",
        "contribution": 0.034552909433841705
      },
      {
        "factor": "card_spend_change_30d_trend_6m",
        "value": 5.589185714285712,
        "message": "This signal increased churn risk.",
        "contribution": 0.02746511809527874
      },
      {
        "factor": "latest_vs_avg_balance_change_30d_available_history",
        "value": -5.454633333333333,
        "message": "Balance has been falling across recent months.",
        "contribution": 0.010233497247099876
      },
      {
        "factor": "avg_app_login_change_30d_6m",
        "value": -0.09941666666666678,
        "message": "App usage has been falling across recent months.",
        "contribution": 0.008675807155668736
      }
    ]
  },
  "model2_input": {
    "customer_context": {
      "age": 44,
      "tenure_months": 50,
      "customer_segment": "farmer",
      "income_regularity": "seasonal",
      "customer_yearly_value": 6883.3402,
      "products_count": 2,
      "has_credit_card": 0,
      "has_loan": 1
    },
    "behavior": {
      "days_since_last_transaction": 5,
      "balance_change_30d": -10.7914,
      "transaction_change_30d": 2.648,
      "card_spend_change_30d": 6.1116,
      "app_login_change_30d": 10.4398,
      "salary_missing_days": null,
      "external_transfer_change_30d": -28.453,
      "upi_share_of_spend": 0.3266,
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
      "churn_probability": 0.0205,
      "churn_prediction": "No",
      "risk_level": "Low",
      "top_risk_factors": [
        {
          "factor": "count_balance_drop_6m",
          "value": 4
        },
        {
          "factor": "vs_avg_external_transfer_change_30d_available_history",
          "value": -29.161516666666667
        },
        {
          "factor": "card_spend_change_30d_trend_6m",
          "value": 5.589185714285712
        },
        {
          "factor": "vs_avg_balance_change_30d_available_history",
          "value": -5.454633333333333
        },
        {
          "factor": "avg_app_login_change_30d_6m",
          "value": -0.09941666666666678
        }
      ]
    },
    "eligible_actions": [
      "MONITOR",
      "RE_ENGAGEMENT",
      "PRODUCT_REVIEW"
    ],
    "case_id": "C10754"
  },
  "model2": {
    "case_id": "C10754",
    "ok": true,
    "prediction": {
      "evidence": [
        "complaints_30d=0",
        "unresolved_complaints=0",
        "failed_transactions_30d=0",
        "avg_resolution_time_hrs=0.0"
      ],
      "primary_reason": "LOW_ENGAGEMENT",
      "reasoning_summary": "Digital engagement signals are weak or declining without a stronger problem signal to justify escalation. Evidence suggests this because complaints_30d=0, unresolved_complaints=0, failed_transactions_30d=0, avg_resolution_time_hrs=0.0.",
      "recommended_action": "RE_ENGAGEMENT",
      "secondary_reasons": [],
      "urgency": "MEDIUM"
    },
    "raw_text": "{\"evidence\":[\"complaints_30d=0\",\"unresolved_complaints=0\",\"failed_transactions_30d=0\",\"avg_resolution_time_hrs=0.0\"],\"primary_reason\":\"LOW_ENGAGEMENT\",\"reasoning_summary\":\"Digital engagement signals are weak or declining without a stronger problem signal to justify escalation. Evidence suggests this because complaints_30d=0, unresolved_complaints=0, failed_transactions_30d=0, avg_resolution_time_hrs=0.0.\",\"recommended_action\":\"RE_ENGAGEMENT\",\"secondary_reasons\":[],\"urgency\":\"MEDIUM\"}",
    "error": null,
    "latency_s": 5.8665,
    "simple_output": "Reason: LOW_ENGAGEMENT | Urgency: MEDIUM | Action: RE_ENGAGEMENT | Why: Digital engagement signals are weak or declining without a stronger problem signal to justify escalation. Evidence suggests this because complaints_30d=0, unresolved_complaints=0, failed_transactions_30d=0, avg_resolution_time_hrs=0.0."
  }
}
```

### Gopal Bawa (`C11042`)

- OK: `True`
- Shape errors: `[]`
- Simple output: Reason: SERVICE_DISSATISFACTION | Urgency: HIGH | Action: SERVICE_RECOVERY | Why: Complaint and resolution data suggest a real service problem without clear escalation-level severity.

Request:

```json
{
  "customer_id": "C11042",
  "customer_name": "Gopal Bawa",
  "prediction_date": "2026-06-01",
  "snapshot_date": "2026-06-01",
  "target_month": "2026-07-01",
  "profile": {
    "tenure_months": 109,
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
      "balance_change_30d": -1.3933,
      "transaction_change_30d": -2.0828,
      "card_spend_change_30d": -6.9643,
      "app_login_change_30d": -26.6632,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -10.2893,
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
      "days_since_last_transaction": 11,
      "balance_change_30d": 1.4635,
      "transaction_change_30d": -18.0654,
      "card_spend_change_30d": 12.0049,
      "app_login_change_30d": 13.6539,
      "salary_missing_days": 2.0,
      "external_transfer_change_30d": 41.6508,
      "upi_share_of_spend": 0.594,
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
      "balance_change_30d": -1.1378,
      "transaction_change_30d": -6.9074,
      "card_spend_change_30d": 2.5723,
      "app_login_change_30d": -5.5588,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": 23.9716,
      "upi_share_of_spend": 0.4782,
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
      "balance_change_30d": 17.3071,
      "transaction_change_30d": -7.7405,
      "card_spend_change_30d": 2.8971,
      "app_login_change_30d": -8.9273,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -8.7473,
      "upi_share_of_spend": 0.4784,
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
      "balance_change_30d": -3.9089,
      "transaction_change_30d": -10.4326,
      "card_spend_change_30d": -2.6851,
      "app_login_change_30d": 20.9864,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": 2.8261,
      "upi_share_of_spend": 0.5828,
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
      "balance_change_30d": -1.3802,
      "transaction_change_30d": 8.315,
      "card_spend_change_30d": 43.7201,
      "app_login_change_30d": -5.7209,
      "salary_missing_days": 1.0,
      "external_transfer_change_30d": 19.2263,
      "upi_share_of_spend": 0.4537,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 24.126,
      "emi_bounce_30d": 0
    }
  ],
  "customer": {
    "tenure_months": 109,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 1,
    "has_credit_card": 0,
    "has_loan": 0,
    "days_since_last_transaction": 10,
    "balance_change_30d": -1.3802,
    "transaction_change_30d": 8.315,
    "card_spend_change_30d": 43.7201,
    "app_login_change_30d": -5.7209,
    "salary_missing_days": 1.0,
    "external_transfer_change_30d": 19.2263,
    "upi_share_of_spend": 0.4537,
    "fd_maturing_in_30d": 0,
    "products_dropped_90d": 0,
    "complaints_30d": 1,
    "unresolved_complaints": 0,
    "failed_transactions_30d": 1,
    "avg_resolution_time_hrs": 24.126,
    "emi_bounce_30d": 0
  },
  "extra_context": {
    "customer_profile": {
      "segment": "salary",
      "income_regularity": "regular",
      "tenure_months": 109,
      "age": 38,
      "customer_yearly_value": 58723.6538,
      "products_count": 1,
      "has_credit_card": 0,
      "has_loan": 0,
      "value_tier": "medium"
    },
    "recent_complaint_text": "App update ke baad UPI kaam hi nahi kar raha. Purana version chahiye."
  }
}
```

Response:

```json
{
  "meta": {
    "endpoint": "/predict/both",
    "served_at": "2026-08-31T00:55:51",
    "elapsed_ms": 2477.95,
    "timings_ms": {
      "model1": 161.2,
      "model2": 2316.6
    },
    "customer_id": "C11042",
    "customer_name": "Gopal Bawa",
    "snapshot_date": "2026-06-01"
  },
  "model1": {
    "churn_probability": 2.32,
    "raw_churn_probability": 21.73,
    "probability_mode": "sigmoid",
    "risk_score": 6.97,
    "churn_prediction": "No",
    "risk_level": "Low",
    "top_risk_factors": [
      {
        "factor": "card_spend_change_30d_trend_6m",
        "value": 5.990765714285712,
        "message": "This signal increased churn risk.",
        "contribution": 0.024399040266871452
      },
      {
        "factor": "max_days_since_last_transaction_3m",
        "value": 10.0,
        "message": "Customer has gone longer without transacting.",
        "contribution": 0.023954005911946297
      },
      {
        "factor": "latest_vs_avg_card_spend_change_30d_available_history",
        "value": 35.129266666666666,
        "message": "This signal increased churn risk.",
        "contribution": 0.013659712858498096
      },
      {
        "factor": "avg_app_login_change_30d_6m",
        "value": -2.038316666666667,
        "message": "App usage has been falling across recent months.",
        "contribution": 0.0048133921809494495
      },
      {
        "factor": "max_salary_missing_days_6m",
        "value": 2.0,
        "message": "Salary or pension was delayed recently.",
        "contribution": 0.004640386439859867
      }
    ]
  },
  "model2_input": {
    "customer_context": {
      "age": 38,
      "tenure_months": 109,
      "customer_segment": "salary",
      "income_regularity": "regular",
      "customer_yearly_value": 58723.6538,
      "products_count": 1,
      "has_credit_card": 0,
      "has_loan": 0
    },
    "behavior": {
      "days_since_last_transaction": 10,
      "balance_change_30d": -1.3802,
      "transaction_change_30d": 8.315,
      "card_spend_change_30d": 43.7201,
      "app_login_change_30d": -5.7209,
      "salary_missing_days": 1,
      "external_transfer_change_30d": 19.2263,
      "upi_share_of_spend": 0.4537,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "emi_bounce_30d": 0
    },
    "service_evidence": {
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 24.126,
      "complaint_text": "App update ke baad UPI kaam hi nahi kar raha. Purana version chahiye."
    },
    "model1": {
      "churn_probability": 0.0232,
      "churn_prediction": "No",
      "risk_level": "Low",
      "top_risk_factors": [
        {
          "factor": "card_spend_change_30d_trend_6m",
          "value": 5.990765714285712
        },
        {
          "factor": "max_days_since_last_transaction_3m",
          "value": 10.0
        },
        {
          "factor": "vs_avg_card_spend_change_30d_available_history",
          "value": 35.129266666666666
        },
        {
          "factor": "avg_app_login_change_30d_6m",
          "value": -2.038316666666667
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
    "case_id": "C11042"
  },
  "model2": {
    "case_id": "C11042",
    "ok": true,
    "prediction": {
      "evidence": [
        "complaints_30d=1",
        "unresolved_complaints=0",
        "avg_resolution_time_hrs=24.1",
        "complaint_text describes a recent service issue"
      ],
      "primary_reason": "SERVICE_DISSATISFACTION",
      "reasoning_summary": "Complaint and resolution data suggest a real service problem without clear escalation-level severity.",
      "recommended_action": "SERVICE_RECOVERY",
      "secondary_reasons": [
        "DIGITAL_FRICTION"
      ],
      "urgency": "HIGH"
    },
    "raw_text": "{\n  \"evidence\":[\"complaints_30d=1\",\"unresolved_complaints=0\",\"avg_resolution_time_hrs=24.1\",\"complaint_text describes a recent service issue\"],\"primary_reason\":\"SERVICE_DISSATISFACTION\",\"reasoning_summary\":\"Complaint and resolution data suggest a real service problem without clear escalation-level severity.\",\"recommended_action\":\"SERVICE_RECOVERY\",\"secondary_reasons\":[\"DIGITAL_FRICTION\"],\"urgency\":\"HIGH\"}",
    "error": null,
    "latency_s": 2.3163,
    "simple_output": "Reason: SERVICE_DISSATISFACTION | Urgency: HIGH | Action: SERVICE_RECOVERY | Why: Complaint and resolution data suggest a real service problem without clear escalation-level severity."
  }
}
```

### Bakhshi Thakkar (`C11061`)

- OK: `True`
- Shape errors: `[]`
- Simple output: Reason: FEE_DISSATISFACTION | Urgency: HIGH | Action: FEE_WAIVER_REVIEW | Why: Complaint evidence suggests dissatisfaction with fees or charges. Evidence suggests this because complaints_30d=2; complaint_text mentions fees or charges.

Request:

```json
{
  "customer_id": "C11061",
  "customer_name": "Bakhshi Thakkar",
  "prediction_date": "2026-03-01",
  "snapshot_date": "2026-03-01",
  "target_month": "2026-04-01",
  "profile": {
    "tenure_months": 145,
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
      "balance_change_30d": 30.6055,
      "transaction_change_30d": 16.389,
      "card_spend_change_30d": 14.1075,
      "app_login_change_30d": 4.6536,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": 4.3305,
      "upi_share_of_spend": 0.6662,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 32.7457,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-02-01",
      "days_since_last_transaction": 11,
      "balance_change_30d": -1.4617,
      "transaction_change_30d": -3.3169,
      "card_spend_change_30d": -17.0352,
      "app_login_change_30d": -37.0109,
      "salary_missing_days": 2.0,
      "external_transfer_change_30d": -5.2254,
      "upi_share_of_spend": 0.7563,
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
      "balance_change_30d": -24.3985,
      "transaction_change_30d": -35.7917,
      "card_spend_change_30d": -22.8299,
      "app_login_change_30d": -22.341,
      "salary_missing_days": 3.0,
      "external_transfer_change_30d": 54.5198,
      "upi_share_of_spend": 0.8724,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 1,
      "complaints_30d": 2,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 2,
      "avg_resolution_time_hrs": 2.1086,
      "emi_bounce_30d": 0
    }
  ],
  "customer": {
    "tenure_months": 145,
    "customer_segment": "pension",
    "income_regularity": "regular",
    "products_count": 2,
    "has_credit_card": 0,
    "has_loan": 0,
    "days_since_last_transaction": 14,
    "balance_change_30d": -24.3985,
    "transaction_change_30d": -35.7917,
    "card_spend_change_30d": -22.8299,
    "app_login_change_30d": -22.341,
    "salary_missing_days": 3.0,
    "external_transfer_change_30d": 54.5198,
    "upi_share_of_spend": 0.8724,
    "fd_maturing_in_30d": 0,
    "products_dropped_90d": 1,
    "complaints_30d": 2,
    "unresolved_complaints": 0,
    "failed_transactions_30d": 2,
    "avg_resolution_time_hrs": 2.1086,
    "emi_bounce_30d": 0
  },
  "extra_context": {
    "customer_profile": {
      "segment": "pension",
      "income_regularity": "regular",
      "tenure_months": 145,
      "age": 63,
      "customer_yearly_value": 18561.1891,
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
    "served_at": "2026-08-31T00:55:53",
    "elapsed_ms": 2707.93,
    "timings_ms": {
      "model1": 163.58,
      "model2": 2544.23
    },
    "customer_id": "C11061",
    "customer_name": "Bakhshi Thakkar",
    "snapshot_date": "2026-03-01"
  },
  "model1": {
    "churn_probability": 34.74,
    "raw_churn_probability": 88.48,
    "probability_mode": "sigmoid",
    "risk_score": 75.53,
    "churn_prediction": "Yes",
    "risk_level": "High",
    "top_risk_factors": [
      {
        "factor": "latest_days_since_last_transaction",
        "value": 14,
        "message": "Customer has gone longer without transacting.",
        "contribution": 0.4299756586551666
      },
      {
        "factor": "latest_transaction_change_30d",
        "value": -35.7917,
        "message": "Transaction activity has been falling across recent months.",
        "contribution": 0.41689762473106384
      },
      {
        "factor": "latest_vs_avg_upi_share_of_spend_available_history",
        "value": 0.10743333333333338,
        "message": "A larger share of spending is happening through UPI.",
        "contribution": 0.26510944962501526
      },
      {
        "factor": "days_since_last_transaction_trend_6m",
        "value": 6.0,
        "message": "Customer has gone longer without transacting.",
        "contribution": 0.23835255205631256
      },
      {
        "factor": "latest_salary_missing_days",
        "value": 3.0,
        "message": "Salary or pension was delayed recently.",
        "contribution": 0.19862861931324005
      }
    ]
  },
  "model2_input": {
    "customer_context": {
      "age": 63,
      "tenure_months": 145,
      "customer_segment": "pension",
      "income_regularity": "regular",
      "customer_yearly_value": 18561.1891,
      "products_count": 2,
      "has_credit_card": 0,
      "has_loan": 0
    },
    "behavior": {
      "days_since_last_transaction": 14,
      "balance_change_30d": -24.3985,
      "transaction_change_30d": -35.7917,
      "card_spend_change_30d": -22.8299,
      "app_login_change_30d": -22.341,
      "salary_missing_days": 3,
      "external_transfer_change_30d": 54.5198,
      "upi_share_of_spend": 0.8724,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 1,
      "emi_bounce_30d": 0
    },
    "service_evidence": {
      "complaints_30d": 2,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 2,
      "avg_resolution_time_hrs": 2.1086,
      "complaint_text": "Every quarter some new charge appears. I am losing trust in this bank."
    },
    "model1": {
      "churn_probability": 0.3474,
      "churn_prediction": "Yes",
      "risk_level": "High",
      "top_risk_factors": [
        {
          "factor": "days_since_last_transaction",
          "value": 14
        },
        {
          "factor": "transaction_change_30d",
          "value": -35.7917
        },
        {
          "factor": "vs_avg_upi_share_of_spend_available_history",
          "value": 0.10743333333333338
        },
        {
          "factor": "days_since_last_transaction_trend_6m",
          "value": 6.0
        },
        {
          "factor": "salary_missing_days",
          "value": 3.0
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
    "case_id": "C11061"
  },
  "model2": {
    "case_id": "C11061",
    "ok": true,
    "prediction": {
      "evidence": [
        "complaints_30d=2",
        "unresolved_complaints=0",
        "avg_resolution_time_hrs=2.1",
        "complaint_text mentions fees or charges"
      ],
      "primary_reason": "FEE_DISSATISFACTION",
      "reasoning_summary": "Complaint evidence suggests dissatisfaction with fees or charges. Evidence suggests this because complaints_30d=2; complaint_text mentions fees or charges.",
      "recommended_action": "FEE_WAIVER_REVIEW",
      "secondary_reasons": [
        "LOW_ENGAGEMENT"
      ],
      "urgency": "HIGH"
    },
    "raw_text": "{\n  \"evidence\":[\"complaints_30d=2\",\"unresolved_complaints=0\",\"avg_resolution_time_hrs=2.1\",\"complaint_text mentions fees or charges\"],\"primary_reason\":\"FEE_DISSATISFACTION\",\"reasoning_summary\":\"Complaint evidence suggests dissatisfaction with fees or charges. Evidence suggests this because complaints_30d=2; complaint_text mentions fees or charges.\",\"recommended_action\":\"FEE_WAIVER_REVIEW\",\"secondary_reasons\":[\"LOW_ENGAGEMENT\"],\"urgency\":\"HIGH\"}",
    "error": null,
    "latency_s": 2.5441,
    "simple_output": "Reason: FEE_DISSATISFACTION | Urgency: HIGH | Action: FEE_WAIVER_REVIEW | Why: Complaint evidence suggests dissatisfaction with fees or charges. Evidence suggests this because complaints_30d=2; complaint_text mentions fees or charges."
  }
}
```

### Vamakshi Barad (`C11364`)

- OK: `True`
- Shape errors: `[]`
- Simple output: Reason: LOW_ENGAGEMENT | Urgency: MEDIUM | Action: RE_ENGAGEMENT | Why: Digital engagement looks low without clear explanation. Relationship narrowing or product-fit stress are less supported than a decline in digital activity.

Request:

```json
{
  "customer_id": "C11364",
  "customer_name": "Vamakshi Barad",
  "prediction_date": "2026-06-01",
  "snapshot_date": "2026-06-01",
  "target_month": "2026-07-01",
  "profile": {
    "tenure_months": 63,
    "customer_segment": "vendor",
    "income_regularity": "irregular",
    "products_count": 2,
    "has_credit_card": 0,
    "has_loan": 1
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 9,
      "balance_change_30d": 12.4855,
      "transaction_change_30d": 0.66,
      "card_spend_change_30d": -6.9421,
      "app_login_change_30d": 3.1855,
      "salary_missing_days": null,
      "external_transfer_change_30d": 5.8723,
      "upi_share_of_spend": 0.4464,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 1,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 30.0964,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-02-01",
      "days_since_last_transaction": 3,
      "balance_change_30d": 19.7908,
      "transaction_change_30d": -3.2494,
      "card_spend_change_30d": -6.7477,
      "app_login_change_30d": 20.4521,
      "salary_missing_days": null,
      "external_transfer_change_30d": -7.5088,
      "upi_share_of_spend": 0.3689,
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
      "days_since_last_transaction": 9,
      "balance_change_30d": 3.6667,
      "transaction_change_30d": 0.7397,
      "card_spend_change_30d": -3.3523,
      "app_login_change_30d": 0.175,
      "salary_missing_days": null,
      "external_transfer_change_30d": 9.3851,
      "upi_share_of_spend": 0.4087,
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
      "days_since_last_transaction": 13,
      "balance_change_30d": -2.3016,
      "transaction_change_30d": 11.7183,
      "card_spend_change_30d": -4.7396,
      "app_login_change_30d": -39.3744,
      "salary_missing_days": null,
      "external_transfer_change_30d": 28.9494,
      "upi_share_of_spend": 0.4633,
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
      "days_since_last_transaction": 12,
      "balance_change_30d": -22.4983,
      "transaction_change_30d": -33.0687,
      "card_spend_change_30d": -36.3777,
      "app_login_change_30d": -1.0295,
      "salary_missing_days": null,
      "external_transfer_change_30d": -20.0866,
      "upi_share_of_spend": 0.485,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 2,
      "unresolved_complaints": 1,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 44.2784,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-06-01",
      "days_since_last_transaction": 8,
      "balance_change_30d": 8.2183,
      "transaction_change_30d": -8.9646,
      "card_spend_change_30d": -0.3904,
      "app_login_change_30d": -22.2719,
      "salary_missing_days": null,
      "external_transfer_change_30d": 17.8008,
      "upi_share_of_spend": 0.4827,
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
    "tenure_months": 63,
    "customer_segment": "vendor",
    "income_regularity": "irregular",
    "products_count": 2,
    "has_credit_card": 0,
    "has_loan": 1,
    "days_since_last_transaction": 8,
    "balance_change_30d": 8.2183,
    "transaction_change_30d": -8.9646,
    "card_spend_change_30d": -0.3904,
    "app_login_change_30d": -22.2719,
    "salary_missing_days": null,
    "external_transfer_change_30d": 17.8008,
    "upi_share_of_spend": 0.4827,
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
      "tenure_months": 63,
      "age": 47,
      "customer_yearly_value": 16403.4933,
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
    "served_at": "2026-08-31T00:55:57",
    "elapsed_ms": 3222.05,
    "timings_ms": {
      "model1": 62.52,
      "model2": 3159.41
    },
    "customer_id": "C11364",
    "customer_name": "Vamakshi Barad",
    "snapshot_date": "2026-06-01"
  },
  "model1": {
    "churn_probability": 4.33,
    "raw_churn_probability": 35.54,
    "probability_mode": "sigmoid",
    "risk_score": 12.99,
    "churn_prediction": "No",
    "risk_level": "Low",
    "top_risk_factors": [
      {
        "factor": "latest_vs_avg_upi_share_of_spend_available_history",
        "value": 0.04020000000000007,
        "message": "A larger share of spending is happening through UPI.",
        "contribution": 0.087846539914608
      },
      {
        "factor": "max_avg_resolution_time_hrs_3m",
        "value": 44.2784,
        "message": "Recent complaints took longer to resolve.",
        "contribution": 0.03400033339858055
      },
      {
        "factor": "external_transfer_change_30d_trend_6m",
        "value": 1.1849542857142839,
        "message": "External transfers have increased.",
        "contribution": 0.0336851067841053
      },
      {
        "factor": "latest_app_login_change_30d",
        "value": -22.2719,
        "message": "App usage has been falling across recent months.",
        "contribution": 0.03211672231554985
      },
      {
        "factor": "avg_card_spend_change_30d_3m",
        "value": -13.8359,
        "message": "Card spending has been falling across recent months.",
        "contribution": 0.028838494792580605
      }
    ]
  },
  "model2_input": {
    "customer_context": {
      "age": 47,
      "tenure_months": 63,
      "customer_segment": "vendor",
      "income_regularity": "irregular",
      "customer_yearly_value": 16403.4933,
      "products_count": 2,
      "has_credit_card": 0,
      "has_loan": 1
    },
    "behavior": {
      "days_since_last_transaction": 8,
      "balance_change_30d": 8.2183,
      "transaction_change_30d": -8.9646,
      "card_spend_change_30d": -0.3904,
      "app_login_change_30d": -22.2719,
      "salary_missing_days": null,
      "external_transfer_change_30d": 17.8008,
      "upi_share_of_spend": 0.4827,
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
      "churn_probability": 0.0433,
      "churn_prediction": "No",
      "risk_level": "Low",
      "top_risk_factors": [
        {
          "factor": "vs_avg_upi_share_of_spend_available_history",
          "value": 0.04020000000000007
        },
        {
          "factor": "max_avg_resolution_time_hrs_3m",
          "value": 44.2784
        },
        {
          "factor": "external_transfer_change_30d_trend_6m",
          "value": 1.1849542857142839
        },
        {
          "factor": "app_login_change_30d",
          "value": -22.2719
        },
        {
          "factor": "avg_card_spend_change_30d_3m",
          "value": -13.8359
        }
      ]
    },
    "eligible_actions": [
      "MONITOR",
      "RE_ENGAGEMENT",
      "PRODUCT_REVIEW"
    ],
    "case_id": "C11364"
  },
  "model2": {
    "case_id": "C11364",
    "ok": true,
    "prediction": {
      "evidence": [
        "complaints_30d=0",
        "unresolved_complaints=0",
        "avg_resolution_time_hrs=0.0",
        "complaint_text=None",
        "transaction_change_30d=-8.96",
        "balance_change_30d=8.22",
        "card_spend_change_30d=-0.4",
        "app_login_change_30d=-22.3",
        "salary_missing_days=None",
        "emi_bounce_30d=0",
        "external_transfer_change_30d=17.8"
      ],
      "primary_reason": "LOW_ENGAGEMENT",
      "reasoning_summary": "Digital engagement looks low without clear explanation. Relationship narrowing or product-fit stress are less supported than a decline in digital activity.",
      "recommended_action": "RE_ENGAGEMENT",
      "secondary_reasons": [
        "DIGITAL_FRICTION"
      ],
      "urgency": "MEDIUM"
    },
    "raw_text": "{\n  \"evidence\":[\"complaints_30d=0\",\"unresolved_complaints=0\",\"avg_resolution_time_hrs=0.0\",\"complaint_text=None\",\"transaction_change_30d=-8.96\",\"balance_change_30d=8.22\",\"card_spend_change_30d=-0.4\",\"app_login_change_30d=-22.3\",\"salary_missing_days=None\",\"emi_bounce_30d=0\",\"external_transfer_change_30d=17.8\"],\"primary_reason\":\"LOW_ENGAGEMENT\",\"reasoning_summary\":\"Digital engagement looks low without clear explanation. Relationship narrowing or product-fit stress are less supported than a decline in digital activity.\",\"recommended_action\":\"RE_ENGAGEMENT\",\"secondary_reasons\":[\"DIGITAL_FRICTION\"],\"urgency\":\"MEDIUM\"}",
    "error": null,
    "latency_s": 3.1592,
    "simple_output": "Reason: LOW_ENGAGEMENT | Urgency: MEDIUM | Action: RE_ENGAGEMENT | Why: Digital engagement looks low without clear explanation. Relationship narrowing or product-fit stress are less supported than a decline in digital activity."
  }
}
```

### Nihal Hans (`C11655`)

- OK: `True`
- Shape errors: `[]`
- Simple output: Reason: FEE_DISSATISFACTION | Urgency: HIGH | Action: FEE_WAIVER_REVIEW | Why: Complaint evidence suggests dissatisfaction with fees or charges.

Request:

```json
{
  "customer_id": "C11655",
  "customer_name": "Nihal Hans",
  "prediction_date": "2026-05-01",
  "snapshot_date": "2026-05-01",
  "target_month": "2026-06-01",
  "profile": {
    "tenure_months": 215,
    "customer_segment": "farmer",
    "income_regularity": "seasonal",
    "products_count": 4,
    "has_credit_card": 1,
    "has_loan": 1
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 10,
      "balance_change_30d": 28.2468,
      "transaction_change_30d": -0.2384,
      "card_spend_change_30d": -14.7787,
      "app_login_change_30d": 26.9829,
      "salary_missing_days": null,
      "external_transfer_change_30d": -7.5891,
      "upi_share_of_spend": 0.4524,
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
      "days_since_last_transaction": 15,
      "balance_change_30d": -30.7148,
      "transaction_change_30d": -9.482,
      "card_spend_change_30d": -27.1201,
      "app_login_change_30d": -18.1765,
      "salary_missing_days": null,
      "external_transfer_change_30d": 39.201,
      "upi_share_of_spend": 0.5852,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 2,
      "avg_resolution_time_hrs": 17.9414,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-03-01",
      "days_since_last_transaction": 18,
      "balance_change_30d": -26.1046,
      "transaction_change_30d": -17.1692,
      "card_spend_change_30d": -32.8199,
      "app_login_change_30d": -9.4378,
      "salary_missing_days": null,
      "external_transfer_change_30d": 64.0207,
      "upi_share_of_spend": 0.5299,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 2,
      "avg_resolution_time_hrs": 30.8929,
      "emi_bounce_30d": 1
    },
    {
      "snapshot_date": "2026-04-01",
      "days_since_last_transaction": 17,
      "balance_change_30d": -12.6717,
      "transaction_change_30d": -16.2233,
      "card_spend_change_30d": 5.4306,
      "app_login_change_30d": -31.8208,
      "salary_missing_days": null,
      "external_transfer_change_30d": 49.1068,
      "upi_share_of_spend": 0.502,
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
      "days_since_last_transaction": 23,
      "balance_change_30d": -43.7214,
      "transaction_change_30d": -41.5356,
      "card_spend_change_30d": -79.332,
      "app_login_change_30d": -53.0808,
      "salary_missing_days": null,
      "external_transfer_change_30d": 96.5362,
      "upi_share_of_spend": 0.6356,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 1,
      "complaints_30d": 1,
      "unresolved_complaints": 1,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 26.8272,
      "emi_bounce_30d": 0
    }
  ],
  "customer": {
    "tenure_months": 215,
    "customer_segment": "farmer",
    "income_regularity": "seasonal",
    "products_count": 4,
    "has_credit_card": 1,
    "has_loan": 1,
    "days_since_last_transaction": 23,
    "balance_change_30d": -43.7214,
    "transaction_change_30d": -41.5356,
    "card_spend_change_30d": -79.332,
    "app_login_change_30d": -53.0808,
    "salary_missing_days": null,
    "external_transfer_change_30d": 96.5362,
    "upi_share_of_spend": 0.6356,
    "fd_maturing_in_30d": 0,
    "products_dropped_90d": 1,
    "complaints_30d": 1,
    "unresolved_complaints": 1,
    "failed_transactions_30d": 1,
    "avg_resolution_time_hrs": 26.8272,
    "emi_bounce_30d": 0
  },
  "extra_context": {
    "customer_profile": {
      "segment": "farmer",
      "income_regularity": "seasonal",
      "tenure_months": 215,
      "age": 53,
      "customer_yearly_value": 18786.8612,
      "products_count": 4,
      "has_credit_card": 1,
      "has_loan": 1,
      "value_tier": "low"
    },
    "recent_complaint_text": "Nobody informed me my account became dormant. Found out at counter."
  }
}
```

Response:

```json
{
  "meta": {
    "endpoint": "/predict/both",
    "served_at": "2026-08-31T00:55:59",
    "elapsed_ms": 2250.91,
    "timings_ms": {
      "model1": 59.87,
      "model2": 2190.94
    },
    "customer_id": "C11655",
    "customer_name": "Nihal Hans",
    "snapshot_date": "2026-05-01"
  },
  "model1": {
    "churn_probability": 41.53,
    "raw_churn_probability": 94.67,
    "probability_mode": "sigmoid",
    "risk_score": 78.07,
    "churn_prediction": "Yes",
    "risk_level": "High",
    "top_risk_factors": [
      {
        "factor": "latest_days_since_last_transaction",
        "value": 23,
        "message": "Customer has gone longer without transacting.",
        "contribution": 0.680933952331543
      },
      {
        "factor": "latest_transaction_change_30d",
        "value": -41.5356,
        "message": "Transaction activity has been falling across recent months.",
        "contribution": 0.5213063359260559
      },
      {
        "factor": "latest_vs_avg_upi_share_of_spend_available_history",
        "value": 0.09458,
        "message": "A larger share of spending is happening through UPI.",
        "contribution": 0.26763954758644104
      },
      {
        "factor": "latest_balance_change_30d",
        "value": -43.7214,
        "message": "Balance has been falling across recent months.",
        "contribution": 0.229611337184906
      },
      {
        "factor": "latest_card_spend_change_30d",
        "value": -79.332,
        "message": "Card spending has been falling across recent months.",
        "contribution": 0.19998838007450104
      }
    ]
  },
  "model2_input": {
    "customer_context": {
      "age": 53,
      "tenure_months": 215,
      "customer_segment": "farmer",
      "income_regularity": "seasonal",
      "customer_yearly_value": 18786.8612,
      "products_count": 4,
      "has_credit_card": 1,
      "has_loan": 1
    },
    "behavior": {
      "days_since_last_transaction": 23,
      "balance_change_30d": -43.7214,
      "transaction_change_30d": -41.5356,
      "card_spend_change_30d": -79.332,
      "app_login_change_30d": -53.0808,
      "salary_missing_days": null,
      "external_transfer_change_30d": 96.5362,
      "upi_share_of_spend": 0.6356,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 1,
      "emi_bounce_30d": 0
    },
    "service_evidence": {
      "complaints_30d": 1,
      "unresolved_complaints": 1,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 26.8272,
      "complaint_text": "Nobody informed me my account became dormant. Found out at counter."
    },
    "model1": {
      "churn_probability": 0.4153,
      "churn_prediction": "Yes",
      "risk_level": "High",
      "top_risk_factors": [
        {
          "factor": "days_since_last_transaction",
          "value": 23
        },
        {
          "factor": "transaction_change_30d",
          "value": -41.5356
        },
        {
          "factor": "vs_avg_upi_share_of_spend_available_history",
          "value": 0.09458
        },
        {
          "factor": "balance_change_30d",
          "value": -43.7214
        },
        {
          "factor": "card_spend_change_30d",
          "value": -79.332
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
    "case_id": "C11655"
  },
  "model2": {
    "case_id": "C11655",
    "ok": true,
    "prediction": {
      "evidence": [
        "complaints_30d=1",
        "unresolved_complaints=1",
        "complaint_text mentions fees or charges",
        "avg_resolution_time_hrs=26.8",
        "secondary_reasons=SERVICE_DISSATISFACTION"
      ],
      "primary_reason": "FEE_DISSATISFACTION",
      "reasoning_summary": "Complaint evidence suggests dissatisfaction with fees or charges.",
      "recommended_action": "FEE_WAIVER_REVIEW",
      "secondary_reasons": [
        "SERVICE_DISSATISFACTION"
      ],
      "urgency": "HIGH"
    },
    "raw_text": "{\n  \"evidence\":[\"complaints_30d=1\",\"unresolved_complaints=1\",\"complaint_text mentions fees or charges\",\"avg_resolution_time_hrs=26.8\",\"secondary_reasons=SERVICE_DISSATISFACTION\"],\"primary_reason\":\"FEE_DISSATISFACTION\",\"reasoning_summary\":\"Complaint evidence suggests dissatisfaction with fees or charges.\",\"recommended_action\":\"FEE_WAIVER_REVIEW\",\"secondary_reasons\":[\"SERVICE_DISSATISFACTION\"],\"urgency\":\"HIGH\"}",
    "error": null,
    "latency_s": 2.1908,
    "simple_output": "Reason: FEE_DISSATISFACTION | Urgency: HIGH | Action: FEE_WAIVER_REVIEW | Why: Complaint evidence suggests dissatisfaction with fees or charges."
  }
}
```

### Odika Rout (`C12376`)

- OK: `True`
- Shape errors: `[]`
- Simple output: Reason: SERVICE_DISSATISFACTION | Urgency: HIGH | Action: SERVICE_RECOVERY | Why: Service friction is the most supported explanation because complaints_30d=0, unresolved_complaints=0, avg_resolution_time_hrs=0.0, and complaint_text does not mention a product-fit issue.

Request:

```json
{
  "customer_id": "C12376",
  "customer_name": "Odika Rout",
  "prediction_date": "2026-06-01",
  "snapshot_date": "2026-06-01",
  "target_month": "2026-07-01",
  "profile": {
    "tenure_months": 115,
    "customer_segment": "business",
    "income_regularity": "irregular",
    "products_count": 1,
    "has_credit_card": 0,
    "has_loan": 0
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 5,
      "balance_change_30d": 14.5309,
      "transaction_change_30d": 26.0856,
      "card_spend_change_30d": 34.705,
      "app_login_change_30d": 42.8543,
      "salary_missing_days": null,
      "external_transfer_change_30d": -0.0361,
      "upi_share_of_spend": 0.65,
      "fd_maturing_in_30d": 1,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 12.5662,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-02-01",
      "days_since_last_transaction": 3,
      "balance_change_30d": 18.2445,
      "transaction_change_30d": 20.7933,
      "card_spend_change_30d": 9.9033,
      "app_login_change_30d": 1.4297,
      "salary_missing_days": null,
      "external_transfer_change_30d": -9.2171,
      "upi_share_of_spend": 0.6481,
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
      "balance_change_30d": 16.9975,
      "transaction_change_30d": 9.2539,
      "card_spend_change_30d": 6.375,
      "app_login_change_30d": 33.0537,
      "salary_missing_days": null,
      "external_transfer_change_30d": 42.665,
      "upi_share_of_spend": 0.5448,
      "fd_maturing_in_30d": 1,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 15.8163,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-04-01",
      "days_since_last_transaction": 6,
      "balance_change_30d": 5.4372,
      "transaction_change_30d": 21.9151,
      "card_spend_change_30d": 5.7033,
      "app_login_change_30d": 9.3557,
      "salary_missing_days": null,
      "external_transfer_change_30d": 2.7807,
      "upi_share_of_spend": 0.5015,
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
      "days_since_last_transaction": 2,
      "balance_change_30d": 16.1619,
      "transaction_change_30d": 36.566,
      "card_spend_change_30d": 38.2512,
      "app_login_change_30d": 22.6419,
      "salary_missing_days": null,
      "external_transfer_change_30d": -5.5361,
      "upi_share_of_spend": 0.684,
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
      "balance_change_30d": 43.4308,
      "transaction_change_30d": 39.6708,
      "card_spend_change_30d": 47.2342,
      "app_login_change_30d": 50.2268,
      "salary_missing_days": null,
      "external_transfer_change_30d": -32.915,
      "upi_share_of_spend": 0.3525,
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
    "tenure_months": 115,
    "customer_segment": "business",
    "income_regularity": "irregular",
    "products_count": 1,
    "has_credit_card": 0,
    "has_loan": 0,
    "days_since_last_transaction": 0,
    "balance_change_30d": 43.4308,
    "transaction_change_30d": 39.6708,
    "card_spend_change_30d": 47.2342,
    "app_login_change_30d": 50.2268,
    "salary_missing_days": null,
    "external_transfer_change_30d": -32.915,
    "upi_share_of_spend": 0.3525,
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
      "tenure_months": 115,
      "age": 43,
      "customer_yearly_value": 163010.5415,
      "products_count": 1,
      "has_credit_card": 0,
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
    "served_at": "2026-08-31T00:56:01",
    "elapsed_ms": 2554.93,
    "timings_ms": {
      "model1": 125.94,
      "model2": 2428.85
    },
    "customer_id": "C12376",
    "customer_name": "Odika Rout",
    "snapshot_date": "2026-06-01"
  },
  "model1": {
    "churn_probability": 1.68,
    "raw_churn_probability": 14.65,
    "probability_mode": "sigmoid",
    "risk_score": 5.05,
    "churn_prediction": "No",
    "risk_level": "Low",
    "top_risk_factors": [
      {
        "factor": "latest_vs_avg_external_transfer_change_30d_available_history",
        "value": -32.53856666666667,
        "message": "This signal increased churn risk.",
        "contribution": 0.11120647192001343
      },
      {
        "factor": "latest_vs_avg_balance_change_30d_available_history",
        "value": 24.297,
        "message": "This signal increased churn risk.",
        "contribution": 0.06878913193941116
      },
      {
        "factor": "avg_transaction_change_30d_6m",
        "value": 25.714116666666666,
        "message": "This signal increased churn risk.",
        "contribution": 0.03741363435983658
      },
      {
        "factor": "app_login_change_30d_trend_6m",
        "value": 2.1943171428571415,
        "message": "This signal increased churn risk.",
        "contribution": 0.030258841812610626
      },
      {
        "factor": "sum_failed_transactions_30d_6m",
        "value": 5.0,
        "message": "Customer has recent failed transactions.",
        "contribution": 0.022281892597675323
      }
    ]
  },
  "model2_input": {
    "customer_context": {
      "age": 43,
      "tenure_months": 115,
      "customer_segment": "business",
      "income_regularity": "irregular",
      "customer_yearly_value": 163010.5415,
      "products_count": 1,
      "has_credit_card": 0,
      "has_loan": 0
    },
    "behavior": {
      "days_since_last_transaction": 0,
      "balance_change_30d": 43.4308,
      "transaction_change_30d": 39.6708,
      "card_spend_change_30d": 47.2342,
      "app_login_change_30d": 50.2268,
      "salary_missing_days": null,
      "external_transfer_change_30d": -32.915,
      "upi_share_of_spend": 0.3525,
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
      "churn_probability": 0.0168,
      "churn_prediction": "No",
      "risk_level": "Low",
      "top_risk_factors": [
        {
          "factor": "vs_avg_external_transfer_change_30d_available_history",
          "value": -32.53856666666667
        },
        {
          "factor": "vs_avg_balance_change_30d_available_history",
          "value": 24.297
        },
        {
          "factor": "avg_transaction_change_30d_6m",
          "value": 25.714116666666666
        },
        {
          "factor": "app_login_change_30d_trend_6m",
          "value": 2.1943171428571415
        },
        {
          "factor": "sum_failed_transactions_30d_6m",
          "value": 5.0
        }
      ]
    },
    "eligible_actions": [
      "MONITOR",
      "RE_ENGAGEMENT",
      "PRODUCT_REVIEW",
      "SERVICE_RECOVERY"
    ],
    "case_id": "C12376"
  },
  "model2": {
    "case_id": "C12376",
    "ok": true,
    "prediction": {
      "evidence": [
        "complaints_30d=0",
        "unresolved_complaints=0",
        "avg_resolution_time_hrs=0.0",
        "complaint_text does not mention a product-fit issue or complaint text is vague"
      ],
      "primary_reason": "SERVICE_DISSATISFACTION",
      "reasoning_summary": "Service friction is the most supported explanation because complaints_30d=0, unresolved_complaints=0, avg_resolution_time_hrs=0.0, and complaint_text does not mention a product-fit issue.",
      "recommended_action": "SERVICE_RECOVERY",
      "secondary_reasons": [],
      "urgency": "HIGH"
    },
    "raw_text": "{\n  \"evidence\":[\"complaints_30d=0\",\"unresolved_complaints=0\",\"avg_resolution_time_hrs=0.0\",\"complaint_text does not mention a product-fit issue or complaint text is vague\"],\"primary_reason\":\"SERVICE_DISSATISFACTION\",\"reasoning_summary\":\"Service friction is the most supported explanation because complaints_30d=0, unresolved_complaints=0, avg_resolution_time_hrs=0.0, and complaint_text does not mention a product-fit issue.\",\"recommended_action\":\"SERVICE_RECOVERY\",\"secondary_reasons\":[],\"urgency\":\"HIGH\"}",
    "error": null,
    "latency_s": 2.4286,
    "simple_output": "Reason: SERVICE_DISSATISFACTION | Urgency: HIGH | Action: SERVICE_RECOVERY | Why: Service friction is the most supported explanation because complaints_30d=0, unresolved_complaints=0, avg_resolution_time_hrs=0.0, and complaint_text does not mention a product-fit issue."
  }
}
```

### Dalbir Venkatesh (`C12383`)

- OK: `True`
- Shape errors: `[]`
- Simple output: Reason: FEE_DISSATISFACTION | Urgency: HIGH | Action: FEE_WAIVER_REVIEW | Why: Complaint evidence suggests dissatisfaction with fees or charges.

Request:

```json
{
  "customer_id": "C12383",
  "customer_name": "Dalbir Venkatesh",
  "prediction_date": "2026-01-01",
  "snapshot_date": "2026-01-01",
  "target_month": "2026-02-01",
  "profile": {
    "tenure_months": 132,
    "customer_segment": "farmer",
    "income_regularity": "seasonal",
    "products_count": 5,
    "has_credit_card": 1,
    "has_loan": 1
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 14,
      "balance_change_30d": -19.5613,
      "transaction_change_30d": 5.7178,
      "card_spend_change_30d": -6.4433,
      "app_login_change_30d": 30.0182,
      "salary_missing_days": null,
      "external_transfer_change_30d": 11.3523,
      "upi_share_of_spend": 0.6463,
      "fd_maturing_in_30d": 1,
      "products_dropped_90d": 0,
      "complaints_30d": 6,
      "unresolved_complaints": 5,
      "failed_transactions_30d": 4,
      "avg_resolution_time_hrs": 99.6322,
      "emi_bounce_30d": 0
    }
  ],
  "customer": {
    "tenure_months": 132,
    "customer_segment": "farmer",
    "income_regularity": "seasonal",
    "products_count": 5,
    "has_credit_card": 1,
    "has_loan": 1,
    "days_since_last_transaction": 14,
    "balance_change_30d": -19.5613,
    "transaction_change_30d": 5.7178,
    "card_spend_change_30d": -6.4433,
    "app_login_change_30d": 30.0182,
    "salary_missing_days": null,
    "external_transfer_change_30d": 11.3523,
    "upi_share_of_spend": 0.6463,
    "fd_maturing_in_30d": 1,
    "products_dropped_90d": 0,
    "complaints_30d": 6,
    "unresolved_complaints": 5,
    "failed_transactions_30d": 4,
    "avg_resolution_time_hrs": 99.6322,
    "emi_bounce_30d": 0
  },
  "extra_context": {
    "customer_profile": {
      "segment": "farmer",
      "income_regularity": "seasonal",
      "tenure_months": 132,
      "age": 36,
      "customer_yearly_value": 6590.8812,
      "products_count": 5,
      "has_credit_card": 1,
      "has_loan": 1,
      "value_tier": "low"
    },
    "recent_complaint_text": "Requesting your help, the app shows technical error code every time."
  }
}
```

Response:

```json
{
  "meta": {
    "endpoint": "/predict/both",
    "served_at": "2026-08-31T00:56:04",
    "elapsed_ms": 2703.96,
    "timings_ms": {
      "model1": 75.42,
      "model2": 2628.42
    },
    "customer_id": "C12383",
    "customer_name": "Dalbir Venkatesh",
    "snapshot_date": "2026-01-01"
  },
  "model1": {
    "churn_probability": 20.03,
    "raw_churn_probability": 72.28,
    "probability_mode": "sigmoid",
    "risk_score": 70.01,
    "churn_prediction": "Yes",
    "risk_level": "Medium",
    "top_risk_factors": [
      {
        "factor": "max_avg_resolution_time_hrs_3m",
        "value": 99.6322,
        "message": "Recent complaints took longer to resolve.",
        "contribution": 0.4157710373401642
      },
      {
        "factor": "latest_avg_resolution_time_hrs",
        "value": 99.6322,
        "message": "Recent complaints took longer to resolve.",
        "contribution": 0.3719501495361328
      },
      {
        "factor": "latest_failed_transactions_30d",
        "value": 4,
        "message": "Customer has recent failed transactions.",
        "contribution": 0.16492301225662231
      },
      {
        "factor": "latest_fd_maturing_in_30d",
        "value": 1,
        "message": "Customer has a fixed deposit maturing soon.",
        "contribution": 0.10215100646018982
      },
      {
        "factor": "sum_fd_maturing_in_30d_3m",
        "value": 1.0,
        "message": "Customer has a fixed deposit maturing soon.",
        "contribution": 0.08452878147363663
      }
    ]
  },
  "model2_input": {
    "customer_context": {
      "age": 36,
      "tenure_months": 132,
      "customer_segment": "farmer",
      "income_regularity": "seasonal",
      "customer_yearly_value": 6590.8812,
      "products_count": 5,
      "has_credit_card": 1,
      "has_loan": 1
    },
    "behavior": {
      "days_since_last_transaction": 14,
      "balance_change_30d": -19.5613,
      "transaction_change_30d": 5.7178,
      "card_spend_change_30d": -6.4433,
      "app_login_change_30d": 30.0182,
      "salary_missing_days": null,
      "external_transfer_change_30d": 11.3523,
      "upi_share_of_spend": 0.6463,
      "fd_maturing_in_30d": 1,
      "products_dropped_90d": 0,
      "emi_bounce_30d": 0
    },
    "service_evidence": {
      "complaints_30d": 6,
      "unresolved_complaints": 5,
      "failed_transactions_30d": 4,
      "avg_resolution_time_hrs": 99.6322,
      "complaint_text": "Requesting your help, the app shows technical error code every time."
    },
    "model1": {
      "churn_probability": 0.2003,
      "churn_prediction": "Yes",
      "risk_level": "Medium",
      "top_risk_factors": [
        {
          "factor": "max_avg_resolution_time_hrs_3m",
          "value": 99.6322
        },
        {
          "factor": "avg_resolution_time_hrs",
          "value": 99.6322
        },
        {
          "factor": "failed_transactions_30d",
          "value": 4
        },
        {
          "factor": "fd_maturing_in_30d",
          "value": 1
        },
        {
          "factor": "sum_fd_maturing_in_30d_3m",
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
    "case_id": "C12383"
  },
  "model2": {
    "case_id": "C12383",
    "ok": true,
    "prediction": {
      "evidence": [
        "complaints_30d=6",
        "unresolved_complaints=5",
        "complaint_text mentions fees or charges",
        "avg_resolution_time_hrs=99.6",
        "secondary_reasons=SERVICE_DISSATISFACTION"
      ],
      "primary_reason": "FEE_DISSATISFACTION",
      "reasoning_summary": "Complaint evidence suggests dissatisfaction with fees or charges.",
      "recommended_action": "FEE_WAIVER_REVIEW",
      "secondary_reasons": [
        "SERVICE_DISSATISFACTION"
      ],
      "urgency": "HIGH"
    },
    "raw_text": "{\n  \"evidence\":[\"complaints_30d=6\",\"unresolved_complaints=5\",\"complaint_text mentions fees or charges\",\"avg_resolution_time_hrs=99.6\",\"secondary_reasons=SERVICE_DISSATISFACTION\"],\"primary_reason\":\"FEE_DISSATISFACTION\",\"reasoning_summary\":\"Complaint evidence suggests dissatisfaction with fees or charges.\",\"recommended_action\":\"FEE_WAIVER_REVIEW\",\"secondary_reasons\":[\"SERVICE_DISSATISFACTION\"],\"urgency\":\"HIGH\"}",
    "error": null,
    "latency_s": 2.6283,
    "simple_output": "Reason: FEE_DISSATISFACTION | Urgency: HIGH | Action: FEE_WAIVER_REVIEW | Why: Complaint evidence suggests dissatisfaction with fees or charges."
  }
}
```

### Urmi Choudhary (`C13333`)

- OK: `False`
- Shape errors: `["model2 returned ok=false: recommended_action: 'FINANCIAL_GUIDANCE' not in eligible_actions ['MONITOR', 'RE_ENGAGEMENT', 'PRODUCT_REVIEW']", 'model2.prediction is missing or not an object']`
- Simple output: Prediction failed: recommended_action: 'FINANCIAL_GUIDANCE' not in eligible_actions ['MONITOR', 'RE_ENGAGEMENT', 'PRODUCT_REVIEW']

Request:

```json
{
  "customer_id": "C13333",
  "customer_name": "Urmi Choudhary",
  "prediction_date": "2026-06-01",
  "snapshot_date": "2026-06-01",
  "target_month": "2026-07-01",
  "profile": {
    "tenure_months": 11,
    "customer_segment": "vendor",
    "income_regularity": "irregular",
    "products_count": 2,
    "has_credit_card": 0,
    "has_loan": 0
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 0,
      "balance_change_30d": 32.9949,
      "transaction_change_30d": 30.73,
      "card_spend_change_30d": 24.4515,
      "app_login_change_30d": -2.6133,
      "salary_missing_days": null,
      "external_transfer_change_30d": 1.6378,
      "upi_share_of_spend": 0.1746,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 2,
      "unresolved_complaints": 1,
      "failed_transactions_30d": 2,
      "avg_resolution_time_hrs": 30.4011,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-02-01",
      "days_since_last_transaction": 0,
      "balance_change_30d": 10.4518,
      "transaction_change_30d": 24.5117,
      "card_spend_change_30d": 19.5026,
      "app_login_change_30d": 20.6538,
      "salary_missing_days": null,
      "external_transfer_change_30d": -4.4139,
      "upi_share_of_spend": 0.1491,
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
      "balance_change_30d": 13.8357,
      "transaction_change_30d": 13.3817,
      "card_spend_change_30d": 14.1633,
      "app_login_change_30d": -13.2552,
      "salary_missing_days": null,
      "external_transfer_change_30d": -13.164,
      "upi_share_of_spend": 0.1062,
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
      "balance_change_30d": 13.8731,
      "transaction_change_30d": 12.7281,
      "card_spend_change_30d": -7.4471,
      "app_login_change_30d": -25.1038,
      "salary_missing_days": null,
      "external_transfer_change_30d": -22.6377,
      "upi_share_of_spend": 0.1812,
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
      "days_since_last_transaction": 7,
      "balance_change_30d": -14.9941,
      "transaction_change_30d": -7.9797,
      "card_spend_change_30d": -21.9716,
      "app_login_change_30d": 2.1533,
      "salary_missing_days": null,
      "external_transfer_change_30d": 16.6527,
      "upi_share_of_spend": 0.1446,
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
      "balance_change_30d": -3.3271,
      "transaction_change_30d": 13.3629,
      "card_spend_change_30d": 33.0832,
      "app_login_change_30d": 8.3421,
      "salary_missing_days": null,
      "external_transfer_change_30d": 17.0797,
      "upi_share_of_spend": 0.1707,
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
    "tenure_months": 11,
    "customer_segment": "vendor",
    "income_regularity": "irregular",
    "products_count": 2,
    "has_credit_card": 0,
    "has_loan": 0,
    "days_since_last_transaction": 0,
    "balance_change_30d": -3.3271,
    "transaction_change_30d": 13.3629,
    "card_spend_change_30d": 33.0832,
    "app_login_change_30d": 8.3421,
    "salary_missing_days": null,
    "external_transfer_change_30d": 17.0797,
    "upi_share_of_spend": 0.1707,
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
      "tenure_months": 11,
      "age": 28,
      "customer_yearly_value": 7831.0298,
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
    "served_at": "2026-08-31T00:56:10",
    "elapsed_ms": 5941.22,
    "timings_ms": {
      "model1": 202.19,
      "model2": 5738.88
    },
    "customer_id": "C13333",
    "customer_name": "Urmi Choudhary",
    "snapshot_date": "2026-06-01"
  },
  "model1": {
    "churn_probability": 3.72,
    "raw_churn_probability": 32.13,
    "probability_mode": "sigmoid",
    "risk_score": 11.15,
    "churn_prediction": "No",
    "risk_level": "Low",
    "top_risk_factors": [
      {
        "factor": "external_transfer_change_30d_trend_6m",
        "value": 3.7410171428571415,
        "message": "External transfers have increased.",
        "contribution": 0.04103630781173706
      },
      {
        "factor": "balance_change_30d_trend_6m",
        "value": -7.368865714285714,
        "message": "Balance has been falling across recent months.",
        "contribution": 0.031122645363211632
      },
      {
        "factor": "avg_upi_share_of_spend_6m",
        "value": 0.1544,
        "message": "A larger share of spending is happening through UPI.",
        "contribution": 0.024919213727116585
      },
      {
        "factor": "latest_vs_avg_balance_change_30d_available_history",
        "value": -12.132816666666663,
        "message": "Balance has been falling across recent months.",
        "contribution": 0.020708763971924782
      },
      {
        "factor": "transaction_change_30d_trend_6m",
        "value": -5.284665714285714,
        "message": "Transaction activity has been falling across recent months.",
        "contribution": 0.01761775277554989
      }
    ]
  },
  "model2_input": {
    "customer_context": {
      "age": 28,
      "tenure_months": 11,
      "customer_segment": "vendor",
      "income_regularity": "irregular",
      "customer_yearly_value": 7831.0298,
      "products_count": 2,
      "has_credit_card": 0,
      "has_loan": 0
    },
    "behavior": {
      "days_since_last_transaction": 0,
      "balance_change_30d": -3.3271,
      "transaction_change_30d": 13.3629,
      "card_spend_change_30d": 33.0832,
      "app_login_change_30d": 8.3421,
      "salary_missing_days": null,
      "external_transfer_change_30d": 17.0797,
      "upi_share_of_spend": 0.1707,
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
          "factor": "external_transfer_change_30d_trend_6m",
          "value": 3.7410171428571415
        },
        {
          "factor": "balance_change_30d_trend_6m",
          "value": -7.368865714285714
        },
        {
          "factor": "avg_upi_share_of_spend_6m",
          "value": 0.1544
        },
        {
          "factor": "vs_avg_balance_change_30d_available_history",
          "value": -12.132816666666663
        },
        {
          "factor": "transaction_change_30d_trend_6m",
          "value": -5.284665714285714
        }
      ]
    },
    "eligible_actions": [
      "MONITOR",
      "RE_ENGAGEMENT",
      "PRODUCT_REVIEW"
    ],
    "case_id": "C13333"
  },
  "model2": {
    "case_id": "C13333",
    "ok": false,
    "prediction": null,
    "raw_text": "{\n  \"evidence\": [\n    \"balance_change_30d=-3.3\",\n    \"external_transfer_change_30d=17.1\",\n    \"products_count=2\"\n  ],\n  \"primary_reason\": \"FINANCIAL_STRESS\",\n  \"reasoning_summary\": \"Evidence suggests this because balance_change_30d=-3.3 and external_transfer_change_30d=17.1 suggest a financial stress situation without a clear product mismatch or relationship issue.\",\n  \"recommended_action\": \"FINANCIAL_GUIDANCE\",\n  \"secondary_reasons\": [\n    \"LOW_ENGAGEMENT\"\n  ],\n  \"urgency\": \"HIGH\"\n}",
    "error": "recommended_action: 'FINANCIAL_GUIDANCE' not in eligible_actions ['MONITOR', 'RE_ENGAGEMENT', 'PRODUCT_REVIEW']",
    "latency_s": 5.7386,
    "simple_output": "Prediction failed: recommended_action: 'FINANCIAL_GUIDANCE' not in eligible_actions ['MONITOR', 'RE_ENGAGEMENT', 'PRODUCT_REVIEW']"
  }
}
```

### Rohan Krishnan (`C13438`)

- OK: `True`
- Shape errors: `[]`
- Simple output: Reason: PRODUCT_MISMATCH | Urgency: HIGH | Action: PRODUCT_REVIEW | Why: The relationship looks stressed from product friction or a product gap. Product review fits because products_dropped_90d=1 and transaction_change_30d=9.5 suggest relationship narrowing or a product-fit issue.

Request:

```json
{
  "customer_id": "C13438",
  "customer_name": "Rohan Krishnan",
  "prediction_date": "2026-06-01",
  "snapshot_date": "2026-06-01",
  "target_month": "2026-07-01",
  "profile": {
    "tenure_months": 143,
    "customer_segment": "farmer",
    "income_regularity": "seasonal",
    "products_count": 2,
    "has_credit_card": 0,
    "has_loan": 1
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 6,
      "balance_change_30d": -18.6906,
      "transaction_change_30d": -28.1497,
      "card_spend_change_30d": -21.2229,
      "app_login_change_30d": -9.8423,
      "salary_missing_days": null,
      "external_transfer_change_30d": 61.9893,
      "upi_share_of_spend": 0.022,
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
      "balance_change_30d": -10.0166,
      "transaction_change_30d": -10.6277,
      "card_spend_change_30d": -25.9344,
      "app_login_change_30d": -21.3149,
      "salary_missing_days": null,
      "external_transfer_change_30d": 2.5959,
      "upi_share_of_spend": 0.0506,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 2,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 3.7899,
      "emi_bounce_30d": 1
    },
    {
      "snapshot_date": "2026-03-01",
      "days_since_last_transaction": 0,
      "balance_change_30d": 8.4218,
      "transaction_change_30d": 17.5469,
      "card_spend_change_30d": 63.866,
      "app_login_change_30d": 38.3859,
      "salary_missing_days": null,
      "external_transfer_change_30d": -7.4714,
      "upi_share_of_spend": 0.0,
      "fd_maturing_in_30d": 1,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 13.6935,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-04-01",
      "days_since_last_transaction": 0,
      "balance_change_30d": -10.3916,
      "transaction_change_30d": -21.9804,
      "card_spend_change_30d": -5.1441,
      "app_login_change_30d": 16.6167,
      "salary_missing_days": null,
      "external_transfer_change_30d": 27.4094,
      "upi_share_of_spend": 0.0137,
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
      "days_since_last_transaction": 6,
      "balance_change_30d": -4.5525,
      "transaction_change_30d": -2.4568,
      "card_spend_change_30d": -11.2009,
      "app_login_change_30d": -7.2437,
      "salary_missing_days": null,
      "external_transfer_change_30d": 43.5797,
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
      "days_since_last_transaction": 0,
      "balance_change_30d": -1.9621,
      "transaction_change_30d": 9.4761,
      "card_spend_change_30d": -30.4329,
      "app_login_change_30d": -6.6995,
      "salary_missing_days": null,
      "external_transfer_change_30d": 31.3384,
      "upi_share_of_spend": 0.0696,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 1,
      "complaints_30d": 0,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 0.0,
      "emi_bounce_30d": 0
    }
  ],
  "customer": {
    "tenure_months": 143,
    "customer_segment": "farmer",
    "income_regularity": "seasonal",
    "products_count": 2,
    "has_credit_card": 0,
    "has_loan": 1,
    "days_since_last_transaction": 0,
    "balance_change_30d": -1.9621,
    "transaction_change_30d": 9.4761,
    "card_spend_change_30d": -30.4329,
    "app_login_change_30d": -6.6995,
    "salary_missing_days": null,
    "external_transfer_change_30d": 31.3384,
    "upi_share_of_spend": 0.0696,
    "fd_maturing_in_30d": 0,
    "products_dropped_90d": 1,
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
      "tenure_months": 143,
      "age": 57,
      "customer_yearly_value": 9264.8115,
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
    "served_at": "2026-08-31T00:56:13",
    "elapsed_ms": 2836.99,
    "timings_ms": {
      "model1": 191.64,
      "model2": 2645.22
    },
    "customer_id": "C13438",
    "customer_name": "Rohan Krishnan",
    "snapshot_date": "2026-06-01"
  },
  "model1": {
    "churn_probability": 3.0,
    "raw_churn_probability": 27.36,
    "probability_mode": "sigmoid",
    "risk_score": 9.0,
    "churn_prediction": "No",
    "risk_level": "Low",
    "top_risk_factors": [
      {
        "factor": "latest_vs_avg_upi_share_of_spend_available_history",
        "value": 0.043616666666666665,
        "message": "A larger share of spending is happening through UPI.",
        "contribution": 0.08896859735250473
      },
      {
        "factor": "avg_card_spend_change_30d_3m",
        "value": -15.592633333333334,
        "message": "Card spending has been falling across recent months.",
        "contribution": 0.055776506662368774
      },
      {
        "factor": "latest_card_spend_change_30d",
        "value": -30.4329,
        "message": "Card spending has been falling across recent months.",
        "contribution": 0.04630555585026741
      },
      {
        "factor": "latest_upi_share_of_spend",
        "value": 0.0696,
        "message": "A larger share of spending is happening through UPI.",
        "contribution": 0.029216336086392403
      },
      {
        "factor": "external_transfer_change_30d_trend_6m",
        "value": 0.13079142857142984,
        "message": "External transfers have increased.",
        "contribution": 0.023755399510264397
      }
    ]
  },
  "model2_input": {
    "customer_context": {
      "age": 57,
      "tenure_months": 143,
      "customer_segment": "farmer",
      "income_regularity": "seasonal",
      "customer_yearly_value": 9264.8115,
      "products_count": 2,
      "has_credit_card": 0,
      "has_loan": 1
    },
    "behavior": {
      "days_since_last_transaction": 0,
      "balance_change_30d": -1.9621,
      "transaction_change_30d": 9.4761,
      "card_spend_change_30d": -30.4329,
      "app_login_change_30d": -6.6995,
      "salary_missing_days": null,
      "external_transfer_change_30d": 31.3384,
      "upi_share_of_spend": 0.0696,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 1,
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
      "churn_probability": 0.03,
      "churn_prediction": "No",
      "risk_level": "Low",
      "top_risk_factors": [
        {
          "factor": "vs_avg_upi_share_of_spend_available_history",
          "value": 0.043616666666666665
        },
        {
          "factor": "avg_card_spend_change_30d_3m",
          "value": -15.592633333333334
        },
        {
          "factor": "card_spend_change_30d",
          "value": -30.4329
        },
        {
          "factor": "upi_share_of_spend",
          "value": 0.0696
        },
        {
          "factor": "external_transfer_change_30d_trend_6m",
          "value": 0.13079142857142984
        }
      ]
    },
    "eligible_actions": [
      "MONITOR",
      "RE_ENGAGEMENT",
      "PRODUCT_REVIEW"
    ],
    "case_id": "C13438"
  },
  "model2": {
    "case_id": "C13438",
    "ok": true,
    "prediction": {
      "evidence": [
        "products_dropped_90d=1",
        "transaction_change_30d=9.5",
        "balance_change_30d=-2.0"
      ],
      "primary_reason": "PRODUCT_MISMATCH",
      "reasoning_summary": "The relationship looks stressed from product friction or a product gap. Product review fits because products_dropped_90d=1 and transaction_change_30d=9.5 suggest relationship narrowing or a product-fit issue.",
      "recommended_action": "PRODUCT_REVIEW",
      "secondary_reasons": [
        "LOW_ENGAGEMENT"
      ],
      "urgency": "HIGH"
    },
    "raw_text": "{\n  \"evidence\":[\"products_dropped_90d=1\",\"transaction_change_30d=9.5\",\"balance_change_30d=-2.0\"],\"primary_reason\":\"PRODUCT_MISMATCH\",\"reasoning_summary\":\"The relationship looks stressed from product friction or a product gap. Product review fits because products_dropped_90d=1 and transaction_change_30d=9.5 suggest relationship narrowing or a product-fit issue.\",\"recommended_action\":\"PRODUCT_REVIEW\",\"secondary_reasons\":[\"LOW_ENGAGEMENT\"],\"urgency\":\"HIGH\"}",
    "error": null,
    "latency_s": 2.645,
    "simple_output": "Reason: PRODUCT_MISMATCH | Urgency: HIGH | Action: PRODUCT_REVIEW | Why: The relationship looks stressed from product friction or a product gap. Product review fits because products_dropped_90d=1 and transaction_change_30d=9.5 suggest relationship narrowing or a product-fit issue."
  }
}
```

### Leena Mital (`C13500`)

- OK: `True`
- Shape errors: `[]`
- Simple output: Reason: FEE_DISSATISFACTION | Urgency: HIGH | Action: FEE_WAIVER_REVIEW | Why: Complaint evidence suggests dissatisfaction with fees or charges. Evidence suggests this because complaints_30d=1; complaint_text mentions fees or charges.

Request:

```json
{
  "customer_id": "C13500",
  "customer_name": "Leena Mital",
  "prediction_date": "2026-05-01",
  "snapshot_date": "2026-05-01",
  "target_month": "2026-06-01",
  "profile": {
    "tenure_months": 162,
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
      "balance_change_30d": 27.2563,
      "transaction_change_30d": 0.7227,
      "card_spend_change_30d": 11.7301,
      "app_login_change_30d": 8.0093,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": 2.8057,
      "upi_share_of_spend": 0.3836,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 1,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 39.7097,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-02-01",
      "days_since_last_transaction": 2,
      "balance_change_30d": 8.9644,
      "transaction_change_30d": 11.4278,
      "card_spend_change_30d": 17.9794,
      "app_login_change_30d": 1.2632,
      "salary_missing_days": 1.0,
      "external_transfer_change_30d": 4.2848,
      "upi_share_of_spend": 0.4561,
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
      "days_since_last_transaction": 1,
      "balance_change_30d": 5.1675,
      "transaction_change_30d": -9.6466,
      "card_spend_change_30d": 2.8997,
      "app_login_change_30d": -3.9056,
      "salary_missing_days": 3.0,
      "external_transfer_change_30d": 6.0681,
      "upi_share_of_spend": 0.5018,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 1,
      "complaints_30d": 3,
      "unresolved_complaints": 1,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 21.7724,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-04-01",
      "days_since_last_transaction": 8,
      "balance_change_30d": -9.1837,
      "transaction_change_30d": -40.5895,
      "card_spend_change_30d": -2.9351,
      "app_login_change_30d": -30.8572,
      "salary_missing_days": 5.0,
      "external_transfer_change_30d": 55.1989,
      "upi_share_of_spend": 0.5518,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 1,
      "complaints_30d": 0,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 2,
      "avg_resolution_time_hrs": 0.0,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-05-01",
      "days_since_last_transaction": 18,
      "balance_change_30d": -40.5578,
      "transaction_change_30d": -56.2394,
      "card_spend_change_30d": -16.7453,
      "app_login_change_30d": -33.846,
      "salary_missing_days": 9.0,
      "external_transfer_change_30d": 55.655,
      "upi_share_of_spend": 0.5663,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 1,
      "failed_transactions_30d": 2,
      "avg_resolution_time_hrs": 16.9274,
      "emi_bounce_30d": 0
    }
  ],
  "customer": {
    "tenure_months": 162,
    "customer_segment": "pension",
    "income_regularity": "regular",
    "products_count": 3,
    "has_credit_card": 1,
    "has_loan": 0,
    "days_since_last_transaction": 18,
    "balance_change_30d": -40.5578,
    "transaction_change_30d": -56.2394,
    "card_spend_change_30d": -16.7453,
    "app_login_change_30d": -33.846,
    "salary_missing_days": 9.0,
    "external_transfer_change_30d": 55.655,
    "upi_share_of_spend": 0.5663,
    "fd_maturing_in_30d": 0,
    "products_dropped_90d": 0,
    "complaints_30d": 1,
    "unresolved_complaints": 1,
    "failed_transactions_30d": 2,
    "avg_resolution_time_hrs": 16.9274,
    "emi_bounce_30d": 0
  },
  "extra_context": {
    "customer_profile": {
      "segment": "pension",
      "income_regularity": "regular",
      "tenure_months": 162,
      "age": 64,
      "customer_yearly_value": 12423.5458,
      "products_count": 3,
      "has_credit_card": 1,
      "has_loan": 0,
      "value_tier": "low"
    },
    "recent_complaint_text": "Customer wants locker but waitlist is long. Considering another bank."
  }
}
```

Response:

```json
{
  "meta": {
    "endpoint": "/predict/both",
    "served_at": "2026-08-31T00:56:16",
    "elapsed_ms": 3172.43,
    "timings_ms": {
      "model1": 264.56,
      "model2": 2907.73
    },
    "customer_id": "C13500",
    "customer_name": "Leena Mital",
    "snapshot_date": "2026-05-01"
  },
  "model1": {
    "churn_probability": 41.02,
    "raw_churn_probability": 94.22,
    "probability_mode": "sigmoid",
    "risk_score": 77.88,
    "churn_prediction": "Yes",
    "risk_level": "High",
    "top_risk_factors": [
      {
        "factor": "latest_days_since_last_transaction",
        "value": 18,
        "message": "Customer has gone longer without transacting.",
        "contribution": 0.6040659546852112
      },
      {
        "factor": "latest_transaction_change_30d",
        "value": -56.2394,
        "message": "Transaction activity has been falling across recent months.",
        "contribution": 0.4595436751842499
      },
      {
        "factor": "latest_salary_missing_days",
        "value": 9.0,
        "message": "Salary or pension was delayed recently.",
        "contribution": 0.29568278789520264
      },
      {
        "factor": "max_salary_missing_days_3m",
        "value": 9.0,
        "message": "Salary or pension was delayed recently.",
        "contribution": 0.282967209815979
      },
      {
        "factor": "latest_vs_avg_upi_share_of_spend_available_history",
        "value": 0.07438,
        "message": "A larger share of spending is happening through UPI.",
        "contribution": 0.2586367428302765
      }
    ]
  },
  "model2_input": {
    "customer_context": {
      "age": 64,
      "tenure_months": 162,
      "customer_segment": "pension",
      "income_regularity": "regular",
      "customer_yearly_value": 12423.5458,
      "products_count": 3,
      "has_credit_card": 1,
      "has_loan": 0
    },
    "behavior": {
      "days_since_last_transaction": 18,
      "balance_change_30d": -40.5578,
      "transaction_change_30d": -56.2394,
      "card_spend_change_30d": -16.7453,
      "app_login_change_30d": -33.846,
      "salary_missing_days": 9,
      "external_transfer_change_30d": 55.655,
      "upi_share_of_spend": 0.5663,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "emi_bounce_30d": 0
    },
    "service_evidence": {
      "complaints_30d": 1,
      "unresolved_complaints": 1,
      "failed_transactions_30d": 2,
      "avg_resolution_time_hrs": 16.9274,
      "complaint_text": "Customer wants locker but waitlist is long. Considering another bank."
    },
    "model1": {
      "churn_probability": 0.4102,
      "churn_prediction": "Yes",
      "risk_level": "High",
      "top_risk_factors": [
        {
          "factor": "days_since_last_transaction",
          "value": 18
        },
        {
          "factor": "transaction_change_30d",
          "value": -56.2394
        },
        {
          "factor": "salary_missing_days",
          "value": 9.0
        },
        {
          "factor": "max_salary_missing_days_3m",
          "value": 9.0
        },
        {
          "factor": "vs_avg_upi_share_of_spend_available_history",
          "value": 0.07438
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
    "case_id": "C13500"
  },
  "model2": {
    "case_id": "C13500",
    "ok": true,
    "prediction": {
      "evidence": [
        "complaints_30d=1",
        "unresolved_complaints=1",
        "complaint_text mentions fees or charges",
        "avg_resolution_time_hrs=17.0",
        "secondary_reasons=COMPETITOR_MIGRATION"
      ],
      "primary_reason": "FEE_DISSATISFACTION",
      "reasoning_summary": "Complaint evidence suggests dissatisfaction with fees or charges. Evidence suggests this because complaints_30d=1; complaint_text mentions fees or charges.",
      "recommended_action": "FEE_WAIVER_REVIEW",
      "secondary_reasons": [
        "COMPETITOR_MIGRATION"
      ],
      "urgency": "HIGH"
    },
    "raw_text": "{\n  \"evidence\":[\"complaints_30d=1\",\"unresolved_complaints=1\",\"complaint_text mentions fees or charges\",\"avg_resolution_time_hrs=17.0\",\"secondary_reasons=COMPETITOR_MIGRATION\"],\"primary_reason\":\"FEE_DISSATISFACTION\",\"reasoning_summary\":\"Complaint evidence suggests dissatisfaction with fees or charges. Evidence suggests this because complaints_30d=1; complaint_text mentions fees or charges.\",\"recommended_action\":\"FEE_WAIVER_REVIEW\",\"secondary_reasons\":[\"COMPETITOR_MIGRATION\"],\"urgency\":\"HIGH\"}",
    "error": null,
    "latency_s": 2.9075,
    "simple_output": "Reason: FEE_DISSATISFACTION | Urgency: HIGH | Action: FEE_WAIVER_REVIEW | Why: Complaint evidence suggests dissatisfaction with fees or charges. Evidence suggests this because complaints_30d=1; complaint_text mentions fees or charges."
  }
}
```

### Yashawini Konda (`C13668`)

- OK: `True`
- Shape errors: `[]`
- Simple output: Reason: LOW_ENGAGEMENT | Urgency: MEDIUM | Action: RE_ENGAGEMENT | Why: Recent digital engagement decline and transaction trends suggest the relationship may be losing momentum without a clear issue to address.

Request:

```json
{
  "customer_id": "C13668",
  "customer_name": "Yashawini Konda",
  "prediction_date": "2026-06-01",
  "snapshot_date": "2026-06-01",
  "target_month": "2026-07-01",
  "profile": {
    "tenure_months": 40,
    "customer_segment": "vendor",
    "income_regularity": "irregular",
    "products_count": 4,
    "has_credit_card": 1,
    "has_loan": 1
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 7,
      "balance_change_30d": -7.4809,
      "transaction_change_30d": 5.4698,
      "card_spend_change_30d": 3.1603,
      "app_login_change_30d": 1.9297,
      "salary_missing_days": null,
      "external_transfer_change_30d": 5.8599,
      "upi_share_of_spend": 0.2992,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 1.9724,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-02-01",
      "days_since_last_transaction": 3,
      "balance_change_30d": 8.2454,
      "transaction_change_30d": -0.641,
      "card_spend_change_30d": 21.4729,
      "app_login_change_30d": 2.5378,
      "salary_missing_days": null,
      "external_transfer_change_30d": 42.7035,
      "upi_share_of_spend": 0.2539,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 35.3795,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-03-01",
      "days_since_last_transaction": 2,
      "balance_change_30d": 12.4351,
      "transaction_change_30d": 31.3556,
      "card_spend_change_30d": -12.5267,
      "app_login_change_30d": 3.8368,
      "salary_missing_days": null,
      "external_transfer_change_30d": -4.3816,
      "upi_share_of_spend": 0.2906,
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
      "days_since_last_transaction": 4,
      "balance_change_30d": -3.4153,
      "transaction_change_30d": 5.1921,
      "card_spend_change_30d": 4.8723,
      "app_login_change_30d": -3.4006,
      "salary_missing_days": null,
      "external_transfer_change_30d": 6.646,
      "upi_share_of_spend": 0.2736,
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
      "days_since_last_transaction": 7,
      "balance_change_30d": -14.3955,
      "transaction_change_30d": -10.1404,
      "card_spend_change_30d": -9.0391,
      "app_login_change_30d": 2.6858,
      "salary_missing_days": null,
      "external_transfer_change_30d": 31.6914,
      "upi_share_of_spend": 0.4297,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 4,
      "avg_resolution_time_hrs": 22.7155,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-06-01",
      "days_since_last_transaction": 1,
      "balance_change_30d": -5.7408,
      "transaction_change_30d": 9.1371,
      "card_spend_change_30d": -6.8072,
      "app_login_change_30d": -6.1315,
      "salary_missing_days": null,
      "external_transfer_change_30d": -7.1534,
      "upi_share_of_spend": 0.2773,
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
    "tenure_months": 40,
    "customer_segment": "vendor",
    "income_regularity": "irregular",
    "products_count": 4,
    "has_credit_card": 1,
    "has_loan": 1,
    "days_since_last_transaction": 1,
    "balance_change_30d": -5.7408,
    "transaction_change_30d": 9.1371,
    "card_spend_change_30d": -6.8072,
    "app_login_change_30d": -6.1315,
    "salary_missing_days": null,
    "external_transfer_change_30d": -7.1534,
    "upi_share_of_spend": 0.2773,
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
      "tenure_months": 40,
      "age": 39,
      "customer_yearly_value": 10405.2197,
      "products_count": 4,
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
    "served_at": "2026-08-31T00:56:20",
    "elapsed_ms": 3427.25,
    "timings_ms": {
      "model1": 178.04,
      "model2": 3249.09
    },
    "customer_id": "C13668",
    "customer_name": "Yashawini Konda",
    "snapshot_date": "2026-06-01"
  },
  "model1": {
    "churn_probability": 2.45,
    "raw_churn_probability": 22.85,
    "probability_mode": "sigmoid",
    "risk_score": 7.34,
    "churn_prediction": "No",
    "risk_level": "Low",
    "top_risk_factors": [
      {
        "factor": "transaction_change_30d_trend_6m",
        "value": -1.0378628571428574,
        "message": "Transaction activity has been falling across recent months.",
        "contribution": 0.014037690125405788
      },
      {
        "factor": "avg_app_login_change_30d_6m",
        "value": 0.24299999999999988,
        "message": "This signal increased churn risk.",
        "contribution": 0.009071312844753265
      },
      {
        "factor": "avg_app_login_change_30d_3m",
        "value": -2.2821,
        "message": "App usage has been falling across recent months.",
        "contribution": 0.008666628040373325
      },
      {
        "factor": "count_balance_drop_3m",
        "value": 2,
        "message": "This signal increased churn risk.",
        "contribution": 0.005545476451516151
      },
      {
        "factor": "sum_failed_transactions_30d_3m",
        "value": 4.0,
        "message": "Customer has recent failed transactions.",
        "contribution": 0.0027263907250016928
      }
    ]
  },
  "model2_input": {
    "customer_context": {
      "age": 39,
      "tenure_months": 40,
      "customer_segment": "vendor",
      "income_regularity": "irregular",
      "customer_yearly_value": 10405.2197,
      "products_count": 4,
      "has_credit_card": 1,
      "has_loan": 1
    },
    "behavior": {
      "days_since_last_transaction": 1,
      "balance_change_30d": -5.7408,
      "transaction_change_30d": 9.1371,
      "card_spend_change_30d": -6.8072,
      "app_login_change_30d": -6.1315,
      "salary_missing_days": null,
      "external_transfer_change_30d": -7.1534,
      "upi_share_of_spend": 0.2773,
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
      "churn_probability": 0.0245,
      "churn_prediction": "No",
      "risk_level": "Low",
      "top_risk_factors": [
        {
          "factor": "transaction_change_30d_trend_6m",
          "value": -1.0378628571428574
        },
        {
          "factor": "avg_app_login_change_30d_6m",
          "value": 0.24299999999999988
        },
        {
          "factor": "avg_app_login_change_30d_3m",
          "value": -2.2821
        },
        {
          "factor": "count_balance_drop_3m",
          "value": 2
        },
        {
          "factor": "sum_failed_transactions_30d_3m",
          "value": 4.0
        }
      ]
    },
    "eligible_actions": [
      "MONITOR",
      "RE_ENGAGEMENT",
      "PRODUCT_REVIEW"
    ],
    "case_id": "C13668"
  },
  "model2": {
    "case_id": "C13668",
    "ok": true,
    "prediction": {
      "evidence": [
        "transaction_change_30d_trend_6m=-1.0",
        "avg_app_login_change_30d_6m=0.2",
        "complaints_30d=0",
        "unresolved_complaints=0",
        "failed_transactions_30d=0",
        "app_login_change_30d=-6.1"
      ],
      "primary_reason": "LOW_ENGAGEMENT",
      "reasoning_summary": "Recent digital engagement decline and transaction trends suggest the relationship may be losing momentum without a clear issue to address.",
      "recommended_action": "RE_ENGAGEMENT",
      "secondary_reasons": [
        "DIGITAL_FRICTION"
      ],
      "urgency": "MEDIUM"
    },
    "raw_text": "{\n  \"evidence\":[\"transaction_change_30d_trend_6m=-1.0\",\"avg_app_login_change_30d_6m=0.2\",\"complaints_30d=0\",\"unresolved_complaints=0\",\"failed_transactions_30d=0\",\"app_login_change_30d=-6.1\"],\"primary_reason\":\"LOW_ENGAGEMENT\",\"reasoning_summary\":\"Recent digital engagement decline and transaction trends suggest the relationship may be losing momentum without a clear issue to address.\",\"recommended_action\":\"RE_ENGAGEMENT\",\"secondary_reasons\":[\"DIGITAL_FRICTION\"],\"urgency\":\"MEDIUM\"}",
    "error": null,
    "latency_s": 3.249,
    "simple_output": "Reason: LOW_ENGAGEMENT | Urgency: MEDIUM | Action: RE_ENGAGEMENT | Why: Recent digital engagement decline and transaction trends suggest the relationship may be losing momentum without a clear issue to address."
  }
}
```

### Lavanya Nanda (`C14004`)

- OK: `True`
- Shape errors: `[]`
- Simple output: Reason: FEE_DISSATISFACTION | Urgency: HIGH | Action: FEE_WAIVER_REVIEW | Why: Complaint evidence suggests a fee or charge issue is unresolved.

Request:

```json
{
  "customer_id": "C14004",
  "customer_name": "Lavanya Nanda",
  "prediction_date": "2026-06-01",
  "snapshot_date": "2026-06-01",
  "target_month": "2026-07-01",
  "profile": {
    "tenure_months": 23,
    "customer_segment": "business",
    "income_regularity": "irregular",
    "products_count": 2,
    "has_credit_card": 0,
    "has_loan": 1
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 7,
      "balance_change_30d": 33.7494,
      "transaction_change_30d": 13.4845,
      "card_spend_change_30d": -0.5689,
      "app_login_change_30d": 5.2331,
      "salary_missing_days": null,
      "external_transfer_change_30d": -12.4026,
      "upi_share_of_spend": 0.43,
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
      "days_since_last_transaction": 16,
      "balance_change_30d": -8.2568,
      "transaction_change_30d": 8.7564,
      "card_spend_change_30d": 3.5459,
      "app_login_change_30d": -34.1216,
      "salary_missing_days": null,
      "external_transfer_change_30d": -2.6039,
      "upi_share_of_spend": 0.4395,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 1,
      "complaints_30d": 3,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 23.7954,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-03-01",
      "days_since_last_transaction": 16,
      "balance_change_30d": -16.3009,
      "transaction_change_30d": -4.1341,
      "card_spend_change_30d": -8.2929,
      "app_login_change_30d": 8.5136,
      "salary_missing_days": null,
      "external_transfer_change_30d": 39.5091,
      "upi_share_of_spend": 0.3496,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 2,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 20.4635,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-04-01",
      "days_since_last_transaction": 13,
      "balance_change_30d": 33.5628,
      "transaction_change_30d": 17.4912,
      "card_spend_change_30d": 28.9655,
      "app_login_change_30d": 1.5288,
      "salary_missing_days": null,
      "external_transfer_change_30d": -15.348,
      "upi_share_of_spend": 0.3668,
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
      "balance_change_30d": 11.3818,
      "transaction_change_30d": -13.7562,
      "card_spend_change_30d": -8.1183,
      "app_login_change_30d": -16.7053,
      "salary_missing_days": null,
      "external_transfer_change_30d": 13.0738,
      "upi_share_of_spend": 0.4735,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 21.1181,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-06-01",
      "days_since_last_transaction": 17,
      "balance_change_30d": -24.4767,
      "transaction_change_30d": -17.7211,
      "card_spend_change_30d": -16.5191,
      "app_login_change_30d": -5.7807,
      "salary_missing_days": null,
      "external_transfer_change_30d": 12.1399,
      "upi_share_of_spend": 0.4926,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 1,
      "complaints_30d": 3,
      "unresolved_complaints": 1,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 43.5014,
      "emi_bounce_30d": 0
    }
  ],
  "customer": {
    "tenure_months": 23,
    "customer_segment": "business",
    "income_regularity": "irregular",
    "products_count": 2,
    "has_credit_card": 0,
    "has_loan": 1,
    "days_since_last_transaction": 17,
    "balance_change_30d": -24.4767,
    "transaction_change_30d": -17.7211,
    "card_spend_change_30d": -16.5191,
    "app_login_change_30d": -5.7807,
    "salary_missing_days": null,
    "external_transfer_change_30d": 12.1399,
    "upi_share_of_spend": 0.4926,
    "fd_maturing_in_30d": 0,
    "products_dropped_90d": 1,
    "complaints_30d": 3,
    "unresolved_complaints": 1,
    "failed_transactions_30d": 0,
    "avg_resolution_time_hrs": 43.5014,
    "emi_bounce_30d": 0
  },
  "extra_context": {
    "customer_profile": {
      "segment": "business",
      "income_regularity": "irregular",
      "tenure_months": 23,
      "age": 33,
      "customer_yearly_value": 45763.5017,
      "products_count": 2,
      "has_credit_card": 0,
      "has_loan": 1,
      "value_tier": "medium"
    },
    "recent_complaint_text": "ATM did not dispense cash but account was debited Rs 10,000."
  }
}
```

Response:

```json
{
  "meta": {
    "endpoint": "/predict/both",
    "served_at": "2026-08-31T00:56:22",
    "elapsed_ms": 2089.26,
    "timings_ms": {
      "model1": 67.43,
      "model2": 2021.69
    },
    "customer_id": "C14004",
    "customer_name": "Lavanya Nanda",
    "snapshot_date": "2026-06-01"
  },
  "model1": {
    "churn_probability": 22.6,
    "raw_churn_probability": 75.58,
    "probability_mode": "sigmoid",
    "risk_score": 70.98,
    "churn_prediction": "Yes",
    "risk_level": "Medium",
    "top_risk_factors": [
      {
        "factor": "latest_days_since_last_transaction",
        "value": 17,
        "message": "Customer has gone longer without transacting.",
        "contribution": 0.5550735592842102
      },
      {
        "factor": "latest_avg_resolution_time_hrs",
        "value": 43.5014,
        "message": "Recent complaints took longer to resolve.",
        "contribution": 0.26235803961753845
      },
      {
        "factor": "latest_vs_avg_upi_share_of_spend_available_history",
        "value": 0.06726666666666664,
        "message": "A larger share of spending is happening through UPI.",
        "contribution": 0.1563936322927475
      },
      {
        "factor": "latest_balance_change_30d",
        "value": -24.4767,
        "message": "Balance has been falling across recent months.",
        "contribution": 0.09182748943567276
      },
      {
        "factor": "latest_transaction_change_30d",
        "value": -17.7211,
        "message": "Transaction activity has been falling across recent months.",
        "contribution": 0.08263587951660156
      }
    ]
  },
  "model2_input": {
    "customer_context": {
      "age": 33,
      "tenure_months": 23,
      "customer_segment": "business",
      "income_regularity": "irregular",
      "customer_yearly_value": 45763.5017,
      "products_count": 2,
      "has_credit_card": 0,
      "has_loan": 1
    },
    "behavior": {
      "days_since_last_transaction": 17,
      "balance_change_30d": -24.4767,
      "transaction_change_30d": -17.7211,
      "card_spend_change_30d": -16.5191,
      "app_login_change_30d": -5.7807,
      "salary_missing_days": null,
      "external_transfer_change_30d": 12.1399,
      "upi_share_of_spend": 0.4926,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 1,
      "emi_bounce_30d": 0
    },
    "service_evidence": {
      "complaints_30d": 3,
      "unresolved_complaints": 1,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 43.5014,
      "complaint_text": "ATM did not dispense cash but account was debited Rs 10,000."
    },
    "model1": {
      "churn_probability": 0.226,
      "churn_prediction": "Yes",
      "risk_level": "Medium",
      "top_risk_factors": [
        {
          "factor": "days_since_last_transaction",
          "value": 17
        },
        {
          "factor": "avg_resolution_time_hrs",
          "value": 43.5014
        },
        {
          "factor": "vs_avg_upi_share_of_spend_available_history",
          "value": 0.06726666666666664
        },
        {
          "factor": "balance_change_30d",
          "value": -24.4767
        },
        {
          "factor": "transaction_change_30d",
          "value": -17.7211
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
    "case_id": "C14004"
  },
  "model2": {
    "case_id": "C14004",
    "ok": true,
    "prediction": {
      "evidence": [
        "complaints_30d=3",
        "unresolved_complaints=1",
        "avg_resolution_time_hrs=43.5",
        "complaint_text mentions fees or charges"
      ],
      "primary_reason": "FEE_DISSATISFACTION",
      "reasoning_summary": "Complaint evidence suggests a fee or charge issue is unresolved.",
      "recommended_action": "FEE_WAIVER_REVIEW",
      "secondary_reasons": [
        "UNKNOWN"
      ],
      "urgency": "HIGH"
    },
    "raw_text": "{\n  \"evidence\":[\"complaints_30d=3\",\"unresolved_complaints=1\",\"avg_resolution_time_hrs=43.5\",\"complaint_text mentions fees or charges\"],\"primary_reason\":\"FEE_DISSATISFACTION\",\"reasoning_summary\":\"Complaint evidence suggests a fee or charge issue is unresolved.\",\"recommended_action\":\"FEE_WAIVER_REVIEW\",\"secondary_reasons\":[\"UNKNOWN\"],\"urgency\":\"HIGH\"}",
    "error": null,
    "latency_s": 2.0214,
    "simple_output": "Reason: FEE_DISSATISFACTION | Urgency: HIGH | Action: FEE_WAIVER_REVIEW | Why: Complaint evidence suggests a fee or charge issue is unresolved."
  }
}
```

### Qabil Nori (`C14037`)

- OK: `True`
- Shape errors: `[]`
- Simple output: Reason: FEE_DISSATISFACTION | Urgency: HIGH | Action: FEE_WAIVER_REVIEW | Why: Complaint evidence suggests dissatisfaction with fees or charges. Evidence suggests this because complaints_30d=2; unresolved_complaints=1.

Request:

```json
{
  "customer_id": "C14037",
  "customer_name": "Qabil Nori",
  "prediction_date": "2026-02-01",
  "snapshot_date": "2026-02-01",
  "target_month": "2026-03-01",
  "profile": {
    "tenure_months": 85,
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
      "balance_change_30d": 0.9107,
      "transaction_change_30d": -2.9653,
      "card_spend_change_30d": 0.8498,
      "app_login_change_30d": -17.2309,
      "salary_missing_days": 2.0,
      "external_transfer_change_30d": 5.5412,
      "upi_share_of_spend": 0.4319,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 1,
      "complaints_30d": 0,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 2,
      "avg_resolution_time_hrs": 0.0,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-02-01",
      "days_since_last_transaction": 15,
      "balance_change_30d": -19.1244,
      "transaction_change_30d": -12.0905,
      "card_spend_change_30d": -51.7954,
      "app_login_change_30d": -25.526,
      "salary_missing_days": 7.0,
      "external_transfer_change_30d": 55.8934,
      "upi_share_of_spend": 0.5399,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 2,
      "unresolved_complaints": 1,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 22.3248,
      "emi_bounce_30d": 0
    }
  ],
  "customer": {
    "tenure_months": 85,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 2,
    "has_credit_card": 0,
    "has_loan": 0,
    "days_since_last_transaction": 15,
    "balance_change_30d": -19.1244,
    "transaction_change_30d": -12.0905,
    "card_spend_change_30d": -51.7954,
    "app_login_change_30d": -25.526,
    "salary_missing_days": 7.0,
    "external_transfer_change_30d": 55.8934,
    "upi_share_of_spend": 0.5399,
    "fd_maturing_in_30d": 0,
    "products_dropped_90d": 0,
    "complaints_30d": 2,
    "unresolved_complaints": 1,
    "failed_transactions_30d": 1,
    "avg_resolution_time_hrs": 22.3248,
    "emi_bounce_30d": 0
  },
  "extra_context": {
    "customer_profile": {
      "segment": "salary",
      "income_regularity": "regular",
      "tenure_months": 85,
      "age": 37,
      "customer_yearly_value": 26798.9548,
      "products_count": 2,
      "has_credit_card": 0,
      "has_loan": 0,
      "value_tier": "low"
    },
    "recent_complaint_text": "GST charged on a fee that itself should not have been levied."
  }
}
```

Response:

```json
{
  "meta": {
    "endpoint": "/predict/both",
    "served_at": "2026-08-31T00:56:24",
    "elapsed_ms": 2362.08,
    "timings_ms": {
      "model1": 82.56,
      "model2": 2279.37
    },
    "customer_id": "C14037",
    "customer_name": "Qabil Nori",
    "snapshot_date": "2026-02-01"
  },
  "model1": {
    "churn_probability": 33.33,
    "raw_churn_probability": 87.13,
    "probability_mode": "sigmoid",
    "risk_score": 75.0,
    "churn_prediction": "Yes",
    "risk_level": "High",
    "top_risk_factors": [
      {
        "factor": "latest_days_since_last_transaction",
        "value": 15,
        "message": "Customer has gone longer without transacting.",
        "contribution": 0.4275207817554474
      },
      {
        "factor": "max_salary_missing_days_3m",
        "value": 7.0,
        "message": "Salary or pension was delayed recently.",
        "contribution": 0.38817325234413147
      },
      {
        "factor": "latest_salary_missing_days",
        "value": 7.0,
        "message": "Salary or pension was delayed recently.",
        "contribution": 0.37302306294441223
      },
      {
        "factor": "latest_vs_avg_upi_share_of_spend_available_history",
        "value": 0.05400000000000005,
        "message": "A larger share of spending is happening through UPI.",
        "contribution": 0.2374798208475113
      },
      {
        "factor": "latest_card_spend_change_30d",
        "value": -51.7954,
        "message": "Card spending has been falling across recent months.",
        "contribution": 0.20412690937519073
      }
    ]
  },
  "model2_input": {
    "customer_context": {
      "age": 37,
      "tenure_months": 85,
      "customer_segment": "salary",
      "income_regularity": "regular",
      "customer_yearly_value": 26798.9548,
      "products_count": 2,
      "has_credit_card": 0,
      "has_loan": 0
    },
    "behavior": {
      "days_since_last_transaction": 15,
      "balance_change_30d": -19.1244,
      "transaction_change_30d": -12.0905,
      "card_spend_change_30d": -51.7954,
      "app_login_change_30d": -25.526,
      "salary_missing_days": 7,
      "external_transfer_change_30d": 55.8934,
      "upi_share_of_spend": 0.5399,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "emi_bounce_30d": 0
    },
    "service_evidence": {
      "complaints_30d": 2,
      "unresolved_complaints": 1,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 22.3248,
      "complaint_text": "GST charged on a fee that itself should not have been levied."
    },
    "model1": {
      "churn_probability": 0.3333,
      "churn_prediction": "Yes",
      "risk_level": "High",
      "top_risk_factors": [
        {
          "factor": "days_since_last_transaction",
          "value": 15
        },
        {
          "factor": "max_salary_missing_days_3m",
          "value": 7.0
        },
        {
          "factor": "salary_missing_days",
          "value": 7.0
        },
        {
          "factor": "vs_avg_upi_share_of_spend_available_history",
          "value": 0.05400000000000005
        },
        {
          "factor": "card_spend_change_30d",
          "value": -51.7954
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
    "case_id": "C14037"
  },
  "model2": {
    "case_id": "C14037",
    "ok": true,
    "prediction": {
      "evidence": [
        "complaints_30d=2",
        "unresolved_complaints=1",
        "avg_resolution_time_hrs=22.3",
        "complaint_text mentions fees or charges"
      ],
      "primary_reason": "FEE_DISSATISFACTION",
      "reasoning_summary": "Complaint evidence suggests dissatisfaction with fees or charges. Evidence suggests this because complaints_30d=2; unresolved_complaints=1.",
      "recommended_action": "FEE_WAIVER_REVIEW",
      "secondary_reasons": [
        "LOW_ENGAGEMENT"
      ],
      "urgency": "HIGH"
    },
    "raw_text": "{\n  \"evidence\":[\"complaints_30d=2\",\"unresolved_complaints=1\",\"avg_resolution_time_hrs=22.3\",\"complaint_text mentions fees or charges\"],\"primary_reason\":\"FEE_DISSATISFACTION\",\"reasoning_summary\":\"Complaint evidence suggests dissatisfaction with fees or charges. Evidence suggests this because complaints_30d=2; unresolved_complaints=1.\",\"recommended_action\":\"FEE_WAIVER_REVIEW\",\"secondary_reasons\":[\"LOW_ENGAGEMENT\"],\"urgency\":\"HIGH\"}",
    "error": null,
    "latency_s": 2.2791,
    "simple_output": "Reason: FEE_DISSATISFACTION | Urgency: HIGH | Action: FEE_WAIVER_REVIEW | Why: Complaint evidence suggests dissatisfaction with fees or charges. Evidence suggests this because complaints_30d=2; unresolved_complaints=1."
  }
}
```

### Bishakha Kar (`C14151`)

- OK: `True`
- Shape errors: `[]`
- Simple output: Reason: SERVICE_DISSATISFACTION | Urgency: HIGH | Action: SERVICE_RECOVERY | Why: Complaint and resolution data suggest a service friction without a clear fee-related issue.

Request:

```json
{
  "customer_id": "C14151",
  "customer_name": "Bishakha Kar",
  "prediction_date": "2026-06-01",
  "snapshot_date": "2026-06-01",
  "target_month": "2026-07-01",
  "profile": {
    "tenure_months": 183,
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
      "balance_change_30d": -18.1063,
      "transaction_change_30d": -19.352,
      "card_spend_change_30d": -35.4375,
      "app_login_change_30d": -20.2657,
      "salary_missing_days": null,
      "external_transfer_change_30d": 42.6953,
      "upi_share_of_spend": 0.7205,
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
      "days_since_last_transaction": 4,
      "balance_change_30d": -10.724,
      "transaction_change_30d": -9.5783,
      "card_spend_change_30d": -7.4359,
      "app_login_change_30d": -26.6593,
      "salary_missing_days": null,
      "external_transfer_change_30d": 6.4613,
      "upi_share_of_spend": 0.5905,
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
      "days_since_last_transaction": 0,
      "balance_change_30d": 1.3868,
      "transaction_change_30d": 22.6025,
      "card_spend_change_30d": 34.749,
      "app_login_change_30d": 18.3825,
      "salary_missing_days": null,
      "external_transfer_change_30d": -8.5725,
      "upi_share_of_spend": 0.5779,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 10.7202,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-04-01",
      "days_since_last_transaction": 0,
      "balance_change_30d": 35.5986,
      "transaction_change_30d": 27.2353,
      "card_spend_change_30d": 51.6682,
      "app_login_change_30d": 49.2352,
      "salary_missing_days": null,
      "external_transfer_change_30d": -26.1259,
      "upi_share_of_spend": 0.4549,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 17.9755,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-05-01",
      "days_since_last_transaction": 0,
      "balance_change_30d": 56.2564,
      "transaction_change_30d": 46.9438,
      "card_spend_change_30d": 60.1381,
      "app_login_change_30d": 56.5734,
      "salary_missing_days": null,
      "external_transfer_change_30d": -41.1977,
      "upi_share_of_spend": 0.3745,
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
      "balance_change_30d": 35.7215,
      "transaction_change_30d": 56.8624,
      "card_spend_change_30d": 45.3905,
      "app_login_change_30d": -11.8459,
      "salary_missing_days": null,
      "external_transfer_change_30d": -39.1476,
      "upi_share_of_spend": 0.3708,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 13.2846,
      "emi_bounce_30d": 0
    }
  ],
  "customer": {
    "tenure_months": 183,
    "customer_segment": "farmer",
    "income_regularity": "seasonal",
    "products_count": 3,
    "has_credit_card": 0,
    "has_loan": 1,
    "days_since_last_transaction": 0,
    "balance_change_30d": 35.7215,
    "transaction_change_30d": 56.8624,
    "card_spend_change_30d": 45.3905,
    "app_login_change_30d": -11.8459,
    "salary_missing_days": null,
    "external_transfer_change_30d": -39.1476,
    "upi_share_of_spend": 0.3708,
    "fd_maturing_in_30d": 0,
    "products_dropped_90d": 0,
    "complaints_30d": 1,
    "unresolved_complaints": 0,
    "failed_transactions_30d": 0,
    "avg_resolution_time_hrs": 13.2846,
    "emi_bounce_30d": 0
  },
  "extra_context": {
    "customer_profile": {
      "segment": "farmer",
      "income_regularity": "seasonal",
      "tenure_months": 183,
      "age": 60,
      "customer_yearly_value": 8590.9913,
      "products_count": 3,
      "has_credit_card": 0,
      "has_loan": 1,
      "value_tier": "low"
    },
    "recent_complaint_text": "Requesting a separate counter for farmers during mandi season."
  }
}
```

Response:

```json
{
  "meta": {
    "endpoint": "/predict/both",
    "served_at": "2026-08-31T00:56:28",
    "elapsed_ms": 3953.92,
    "timings_ms": {
      "model1": 66.99,
      "model2": 3886.82
    },
    "customer_id": "C14151",
    "customer_name": "Bishakha Kar",
    "snapshot_date": "2026-06-01"
  },
  "model1": {
    "churn_probability": 1.37,
    "raw_churn_probability": 10.24,
    "probability_mode": "sigmoid",
    "risk_score": 4.12,
    "churn_prediction": "No",
    "risk_level": "Low",
    "top_risk_factors": [
      {
        "factor": "sum_failed_transactions_30d_6m",
        "value": 8.0,
        "message": "Customer has recent failed transactions.",
        "contribution": 0.09396960586309433
      },
      {
        "factor": "avg_transaction_change_30d_6m",
        "value": 20.785616666666666,
        "message": "This signal increased churn risk.",
        "contribution": 0.04391248896718025
      },
      {
        "factor": "count_app_login_drop_6m",
        "value": 3,
        "message": "This signal increased churn risk.",
        "contribution": 0.026329508051276207
      },
      {
        "factor": "latest_vs_avg_external_transfer_change_30d_available_history",
        "value": -28.166416666666663,
        "message": "This signal increased churn risk.",
        "contribution": 0.026057226583361626
      },
      {
        "factor": "count_balance_drop_3m",
        "value": 0,
        "message": "This signal increased churn risk.",
        "contribution": 0.0046772425994277
      }
    ]
  },
  "model2_input": {
    "customer_context": {
      "age": 60,
      "tenure_months": 183,
      "customer_segment": "farmer",
      "income_regularity": "seasonal",
      "customer_yearly_value": 8590.9913,
      "products_count": 3,
      "has_credit_card": 0,
      "has_loan": 1
    },
    "behavior": {
      "days_since_last_transaction": 0,
      "balance_change_30d": 35.7215,
      "transaction_change_30d": 56.8624,
      "card_spend_change_30d": 45.3905,
      "app_login_change_30d": -11.8459,
      "salary_missing_days": null,
      "external_transfer_change_30d": -39.1476,
      "upi_share_of_spend": 0.3708,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "emi_bounce_30d": 0
    },
    "service_evidence": {
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 13.2846,
      "complaint_text": "Requesting a separate counter for farmers during mandi season."
    },
    "model1": {
      "churn_probability": 0.0137,
      "churn_prediction": "No",
      "risk_level": "Low",
      "top_risk_factors": [
        {
          "factor": "sum_failed_transactions_30d_6m",
          "value": 8.0
        },
        {
          "factor": "avg_transaction_change_30d_6m",
          "value": 20.785616666666666
        },
        {
          "factor": "count_app_login_drop_6m",
          "value": 3
        },
        {
          "factor": "vs_avg_external_transfer_change_30d_available_history",
          "value": -28.166416666666663
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
      "PRODUCT_REVIEW",
      "SERVICE_RECOVERY"
    ],
    "case_id": "C14151"
  },
  "model2": {
    "case_id": "C14151",
    "ok": true,
    "prediction": {
      "evidence": [
        "complaints_30d=1",
        "unresolved_complaints=0",
        "avg_resolution_time_hrs=13.3"
      ],
      "primary_reason": "SERVICE_DISSATISFACTION",
      "reasoning_summary": "Complaint and resolution data suggest a service friction without a clear fee-related issue.",
      "recommended_action": "SERVICE_RECOVERY",
      "secondary_reasons": [
        "DIGITAL_FRICTION"
      ],
      "urgency": "HIGH"
    },
    "raw_text": "{\"evidence\":[\"complaints_30d=1\",\"unresolved_complaints=0\",\"avg_resolution_time_hrs=13.3\"],\"primary_reason\":\"SERVICE_DISSATISFACTION\",\"reasoning_summary\":\"Complaint and resolution data suggest a service friction without a clear fee-related issue.\",\"recommended_action\":\"SERVICE_RECOVERY\",\"secondary_reasons\":[\"DIGITAL_FRICTION\"],\"urgency\":\"HIGH\"}",
    "error": null,
    "latency_s": 3.8866,
    "simple_output": "Reason: SERVICE_DISSATISFACTION | Urgency: HIGH | Action: SERVICE_RECOVERY | Why: Complaint and resolution data suggest a service friction without a clear fee-related issue."
  }
}
```

### Girish Babu (`C14437`)

- OK: `True`
- Shape errors: `[]`
- Simple output: Reason: LOW_ENGAGEMENT | Urgency: MEDIUM | Action: RE_ENGAGEMENT | Why: Digital engagement signals decline without clear cause. Relationship touchpoints may be appropriate before narrowing the issue.

Request:

```json
{
  "customer_id": "C14437",
  "customer_name": "Girish Babu",
  "prediction_date": "2026-06-01",
  "snapshot_date": "2026-06-01",
  "target_month": "2026-07-01",
  "profile": {
    "tenure_months": 27,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 1,
    "has_credit_card": 0,
    "has_loan": 0
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 2,
      "balance_change_30d": -2.1859,
      "transaction_change_30d": -4.4097,
      "card_spend_change_30d": -15.2629,
      "app_login_change_30d": 16.4165,
      "salary_missing_days": 2.0,
      "external_transfer_change_30d": -3.8792,
      "upi_share_of_spend": 0.7792,
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
      "balance_change_30d": 23.0996,
      "transaction_change_30d": 18.4029,
      "card_spend_change_30d": 34.9371,
      "app_login_change_30d": 14.8961,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -4.8058,
      "upi_share_of_spend": 0.666,
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
      "days_since_last_transaction": 6,
      "balance_change_30d": -21.7182,
      "transaction_change_30d": -9.1173,
      "card_spend_change_30d": -18.0735,
      "app_login_change_30d": 3.8308,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": 3.1022,
      "upi_share_of_spend": 0.6986,
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
      "days_since_last_transaction": 2,
      "balance_change_30d": -27.746,
      "transaction_change_30d": -0.5546,
      "card_spend_change_30d": 28.452,
      "app_login_change_30d": -13.6117,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -9.8916,
      "upi_share_of_spend": 0.6668,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 17.2422,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-05-01",
      "days_since_last_transaction": 1,
      "balance_change_30d": 25.5934,
      "transaction_change_30d": 11.4341,
      "card_spend_change_30d": 23.1812,
      "app_login_change_30d": 5.6936,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -1.9422,
      "upi_share_of_spend": 0.6385,
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
      "balance_change_30d": -13.8154,
      "transaction_change_30d": 2.159,
      "card_spend_change_30d": 27.1085,
      "app_login_change_30d": -16.9894,
      "salary_missing_days": 1.0,
      "external_transfer_change_30d": -9.215,
      "upi_share_of_spend": 0.6824,
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
    "tenure_months": 27,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 1,
    "has_credit_card": 0,
    "has_loan": 0,
    "days_since_last_transaction": 9,
    "balance_change_30d": -13.8154,
    "transaction_change_30d": 2.159,
    "card_spend_change_30d": 27.1085,
    "app_login_change_30d": -16.9894,
    "salary_missing_days": 1.0,
    "external_transfer_change_30d": -9.215,
    "upi_share_of_spend": 0.6824,
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
      "tenure_months": 27,
      "age": 28,
      "customer_yearly_value": 42527.9377,
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
    "served_at": "2026-08-31T00:56:30",
    "elapsed_ms": 2032.29,
    "timings_ms": {
      "model1": 76.04,
      "model2": 1956.14
    },
    "customer_id": "C14437",
    "customer_name": "Girish Babu",
    "snapshot_date": "2026-06-01"
  },
  "model1": {
    "churn_probability": 3.28,
    "raw_churn_probability": 29.35,
    "probability_mode": "sigmoid",
    "risk_score": 9.84,
    "churn_prediction": "No",
    "risk_level": "Low",
    "top_risk_factors": [
      {
        "factor": "card_spend_change_30d_trend_6m",
        "value": 6.3747085714285685,
        "message": "This signal increased churn risk.",
        "contribution": 0.036984339356422424
      },
      {
        "factor": "latest_upi_share_of_spend",
        "value": 0.6824,
        "message": "A larger share of spending is happening through UPI.",
        "contribution": 0.036893635988235474
      },
      {
        "factor": "latest_vs_avg_balance_change_30d_available_history",
        "value": -11.019983333333334,
        "message": "Balance has been falling across recent months.",
        "contribution": 0.017745545133948326
      },
      {
        "factor": "count_app_login_drop_3m",
        "value": 2,
        "message": "This signal increased churn risk.",
        "contribution": 0.015977714210748672
      },
      {
        "factor": "latest_app_login_change_30d",
        "value": -16.9894,
        "message": "App usage has been falling across recent months.",
        "contribution": 0.013372932560741901
      }
    ]
  },
  "model2_input": {
    "customer_context": {
      "age": 28,
      "tenure_months": 27,
      "customer_segment": "salary",
      "income_regularity": "regular",
      "customer_yearly_value": 42527.9377,
      "products_count": 1,
      "has_credit_card": 0,
      "has_loan": 0
    },
    "behavior": {
      "days_since_last_transaction": 9,
      "balance_change_30d": -13.8154,
      "transaction_change_30d": 2.159,
      "card_spend_change_30d": 27.1085,
      "app_login_change_30d": -16.9894,
      "salary_missing_days": 1,
      "external_transfer_change_30d": -9.215,
      "upi_share_of_spend": 0.6824,
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
      "churn_probability": 0.0328,
      "churn_prediction": "No",
      "risk_level": "Low",
      "top_risk_factors": [
        {
          "factor": "card_spend_change_30d_trend_6m",
          "value": 6.3747085714285685
        },
        {
          "factor": "upi_share_of_spend",
          "value": 0.6824
        },
        {
          "factor": "vs_avg_balance_change_30d_available_history",
          "value": -11.019983333333334
        },
        {
          "factor": "count_app_login_drop_3m",
          "value": 2
        },
        {
          "factor": "app_login_change_30d",
          "value": -16.9894
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
    "case_id": "C14437"
  },
  "model2": {
    "case_id": "C14437",
    "ok": true,
    "prediction": {
      "evidence": [
        "complaints_30d=0",
        "unresolved_complaints=0",
        "failed_transactions_30d=0",
        "avg_resolution_time_hrs=0.0"
      ],
      "primary_reason": "LOW_ENGAGEMENT",
      "reasoning_summary": "Digital engagement signals decline without clear cause. Relationship touchpoints may be appropriate before narrowing the issue.",
      "recommended_action": "RE_ENGAGEMENT",
      "secondary_reasons": [
        "DIGITAL_FRICTION"
      ],
      "urgency": "MEDIUM"
    },
    "raw_text": "{\n  \"evidence\":[\"complaints_30d=0\",\"unresolved_complaints=0\",\"failed_transactions_30d=0\",\"avg_resolution_time_hrs=0.0\"],\"primary_reason\":\"LOW_ENGAGEMENT\",\"reasoning_summary\":\"Digital engagement signals decline without clear cause. Relationship touchpoints may be appropriate before narrowing the issue.\",\"recommended_action\":\"RE_ENGAGEMENT\",\"secondary_reasons\":[\"DIGITAL_FRICTION\"],\"urgency\":\"MEDIUM\"}",
    "error": null,
    "latency_s": 1.956,
    "simple_output": "Reason: LOW_ENGAGEMENT | Urgency: MEDIUM | Action: RE_ENGAGEMENT | Why: Digital engagement signals decline without clear cause. Relationship touchpoints may be appropriate before narrowing the issue."
  }
}
```

### Bhavna D’Alia (`C14891`)

- OK: `True`
- Shape errors: `[]`
- Simple output: Reason: FEE_DISSATISFACTION | Urgency: HIGH | Action: FEE_WAIVER_REVIEW | Why: Complaint evidence suggests dissatisfaction with fees or charges. Evidence is mixed or limited, so the cause remains uncertain.

Request:

```json
{
  "customer_id": "C14891",
  "customer_name": "Bhavna D’Alia",
  "prediction_date": "2026-02-01",
  "snapshot_date": "2026-02-01",
  "target_month": "2026-03-01",
  "profile": {
    "tenure_months": 21,
    "customer_segment": "vendor",
    "income_regularity": "irregular",
    "products_count": 2,
    "has_credit_card": 0,
    "has_loan": 1
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 5,
      "balance_change_30d": -6.8962,
      "transaction_change_30d": -5.4895,
      "card_spend_change_30d": -28.7874,
      "app_login_change_30d": 18.8334,
      "salary_missing_days": null,
      "external_transfer_change_30d": 6.3114,
      "upi_share_of_spend": 0.3044,
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
      "days_since_last_transaction": 9,
      "balance_change_30d": -9.7658,
      "transaction_change_30d": -23.8646,
      "card_spend_change_30d": -35.9441,
      "app_login_change_30d": -32.741,
      "salary_missing_days": null,
      "external_transfer_change_30d": 41.5876,
      "upi_share_of_spend": 0.4702,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 1,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 2,
      "avg_resolution_time_hrs": 23.4102,
      "emi_bounce_30d": 1
    }
  ],
  "customer": {
    "tenure_months": 21,
    "customer_segment": "vendor",
    "income_regularity": "irregular",
    "products_count": 2,
    "has_credit_card": 0,
    "has_loan": 1,
    "days_since_last_transaction": 9,
    "balance_change_30d": -9.7658,
    "transaction_change_30d": -23.8646,
    "card_spend_change_30d": -35.9441,
    "app_login_change_30d": -32.741,
    "salary_missing_days": null,
    "external_transfer_change_30d": 41.5876,
    "upi_share_of_spend": 0.4702,
    "fd_maturing_in_30d": 0,
    "products_dropped_90d": 1,
    "complaints_30d": 1,
    "unresolved_complaints": 0,
    "failed_transactions_30d": 2,
    "avg_resolution_time_hrs": 23.4102,
    "emi_bounce_30d": 1
  },
  "extra_context": {
    "customer_profile": {
      "segment": "vendor",
      "income_regularity": "irregular",
      "tenure_months": 21,
      "age": 27,
      "customer_yearly_value": 77797.1615,
      "products_count": 2,
      "has_credit_card": 0,
      "has_loan": 1,
      "value_tier": "medium"
    },
    "recent_complaint_text": "Card ka number galat print hua hai. Branch ne bola online complaint karo."
  }
}
```

Response:

```json
{
  "meta": {
    "endpoint": "/predict/both",
    "served_at": "2026-08-31T00:56:32",
    "elapsed_ms": 2231.66,
    "timings_ms": {
      "model1": 63.89,
      "model2": 2167.67
    },
    "customer_id": "C14891",
    "customer_name": "Bhavna D’Alia",
    "snapshot_date": "2026-02-01"
  },
  "model1": {
    "churn_probability": 15.58,
    "raw_churn_probability": 65.73,
    "probability_mode": "sigmoid",
    "risk_score": 52.33,
    "churn_prediction": "No",
    "risk_level": "Medium",
    "top_risk_factors": [
      {
        "factor": "latest_transaction_change_30d",
        "value": -23.8646,
        "message": "Transaction activity has been falling across recent months.",
        "contribution": 0.22102272510528564
      },
      {
        "factor": "latest_vs_avg_upi_share_of_spend_available_history",
        "value": 0.08290000000000003,
        "message": "A larger share of spending is happening through UPI.",
        "contribution": 0.2173532396554947
      },
      {
        "factor": "transaction_change_30d_trend_6m",
        "value": -18.375099999999996,
        "message": "Transaction activity has been falling across recent months.",
        "contribution": 0.17375731468200684
      },
      {
        "factor": "days_since_last_transaction_trend_6m",
        "value": 3.9999999999999982,
        "message": "Customer has gone longer without transacting.",
        "contribution": 0.16044025123119354
      },
      {
        "factor": "latest_card_spend_change_30d",
        "value": -35.9441,
        "message": "Card spending has been falling across recent months.",
        "contribution": 0.09214038401842117
      }
    ]
  },
  "model2_input": {
    "customer_context": {
      "age": 27,
      "tenure_months": 21,
      "customer_segment": "vendor",
      "income_regularity": "irregular",
      "customer_yearly_value": 77797.1615,
      "products_count": 2,
      "has_credit_card": 0,
      "has_loan": 1
    },
    "behavior": {
      "days_since_last_transaction": 9,
      "balance_change_30d": -9.7658,
      "transaction_change_30d": -23.8646,
      "card_spend_change_30d": -35.9441,
      "app_login_change_30d": -32.741,
      "salary_missing_days": null,
      "external_transfer_change_30d": 41.5876,
      "upi_share_of_spend": 0.4702,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 1,
      "emi_bounce_30d": 1
    },
    "service_evidence": {
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 2,
      "avg_resolution_time_hrs": 23.4102,
      "complaint_text": "Card ka number galat print hua hai. Branch ne bola online complaint karo."
    },
    "model1": {
      "churn_probability": 0.1558,
      "churn_prediction": "No",
      "risk_level": "Medium",
      "top_risk_factors": [
        {
          "factor": "transaction_change_30d",
          "value": -23.8646
        },
        {
          "factor": "vs_avg_upi_share_of_spend_available_history",
          "value": 0.08290000000000003
        },
        {
          "factor": "transaction_change_30d_trend_6m",
          "value": -18.375099999999996
        },
        {
          "factor": "days_since_last_transaction_trend_6m",
          "value": 3.9999999999999982
        },
        {
          "factor": "card_spend_change_30d",
          "value": -35.9441
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
    "case_id": "C14891"
  },
  "model2": {
    "case_id": "C14891",
    "ok": true,
    "prediction": {
      "evidence": [
        "complaints_30d=1",
        "unresolved_complaints=0",
        "avg_resolution_time_hrs=23.4",
        "complaint_text mentions fees or charges"
      ],
      "primary_reason": "FEE_DISSATISFACTION",
      "reasoning_summary": "Complaint evidence suggests dissatisfaction with fees or charges. Evidence is mixed or limited, so the cause remains uncertain.",
      "recommended_action": "FEE_WAIVER_REVIEW",
      "secondary_reasons": [],
      "urgency": "HIGH"
    },
    "raw_text": "{\n  \"evidence\":[\"complaints_30d=1\",\"unresolved_complaints=0\",\"avg_resolution_time_hrs=23.4\",\"complaint_text mentions fees or charges\"],\"primary_reason\":\"FEE_DISSATISFACTION\",\"reasoning_summary\":\"Complaint evidence suggests dissatisfaction with fees or charges. Evidence is mixed or limited, so the cause remains uncertain.\",\"recommended_action\":\"FEE_WAIVER_REVIEW\",\"secondary_reasons\":[],\"urgency\":\"HIGH\"}",
    "error": null,
    "latency_s": 2.1674,
    "simple_output": "Reason: FEE_DISSATISFACTION | Urgency: HIGH | Action: FEE_WAIVER_REVIEW | Why: Complaint evidence suggests dissatisfaction with fees or charges. Evidence is mixed or limited, so the cause remains uncertain."
  }
}
```

### Warjas Dani (`C15022`)

- OK: `True`
- Shape errors: `[]`
- Simple output: Reason: FEE_DISSATISFACTION | Urgency: HIGH | Action: FEE_WAIVER_REVIEW | Why: Complaint evidence suggests dissatisfaction with fees or charges.

Request:

```json
{
  "customer_id": "C15022",
  "customer_name": "Warjas Dani",
  "prediction_date": "2026-06-01",
  "snapshot_date": "2026-06-01",
  "target_month": "2026-07-01",
  "profile": {
    "tenure_months": 200,
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
      "balance_change_30d": -17.1141,
      "transaction_change_30d": -6.7303,
      "card_spend_change_30d": -21.0055,
      "app_login_change_30d": 12.0307,
      "salary_missing_days": null,
      "external_transfer_change_30d": -5.5921,
      "upi_share_of_spend": 0.1373,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 2,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 22.2379,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-02-01",
      "days_since_last_transaction": 14,
      "balance_change_30d": -22.3234,
      "transaction_change_30d": -28.2391,
      "card_spend_change_30d": 6.9192,
      "app_login_change_30d": -16.3475,
      "salary_missing_days": null,
      "external_transfer_change_30d": 25.4721,
      "upi_share_of_spend": 0.3194,
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
      "balance_change_30d": -17.3922,
      "transaction_change_30d": -26.688,
      "card_spend_change_30d": -14.601,
      "app_login_change_30d": -13.6222,
      "salary_missing_days": null,
      "external_transfer_change_30d": 72.7862,
      "upi_share_of_spend": 0.3282,
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
      "days_since_last_transaction": 11,
      "balance_change_30d": -23.7253,
      "transaction_change_30d": -33.0741,
      "card_spend_change_30d": -33.8742,
      "app_login_change_30d": -36.3612,
      "salary_missing_days": null,
      "external_transfer_change_30d": 43.5799,
      "upi_share_of_spend": 0.3346,
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
      "days_since_last_transaction": 17,
      "balance_change_30d": -22.9219,
      "transaction_change_30d": -35.3928,
      "card_spend_change_30d": -69.0806,
      "app_login_change_30d": -40.6129,
      "salary_missing_days": null,
      "external_transfer_change_30d": 84.6179,
      "upi_share_of_spend": 0.2976,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 1,
      "complaints_30d": 2,
      "unresolved_complaints": 1,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 43.4358,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-06-01",
      "days_since_last_transaction": 22,
      "balance_change_30d": -49.3237,
      "transaction_change_30d": -71.0705,
      "card_spend_change_30d": -51.0771,
      "app_login_change_30d": -75.8739,
      "salary_missing_days": null,
      "external_transfer_change_30d": 100.5435,
      "upi_share_of_spend": 0.3884,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 1,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 2,
      "avg_resolution_time_hrs": 24.0532,
      "emi_bounce_30d": 0
    }
  ],
  "customer": {
    "tenure_months": 200,
    "customer_segment": "farmer",
    "income_regularity": "seasonal",
    "products_count": 2,
    "has_credit_card": 0,
    "has_loan": 1,
    "days_since_last_transaction": 22,
    "balance_change_30d": -49.3237,
    "transaction_change_30d": -71.0705,
    "card_spend_change_30d": -51.0771,
    "app_login_change_30d": -75.8739,
    "salary_missing_days": null,
    "external_transfer_change_30d": 100.5435,
    "upi_share_of_spend": 0.3884,
    "fd_maturing_in_30d": 0,
    "products_dropped_90d": 1,
    "complaints_30d": 1,
    "unresolved_complaints": 0,
    "failed_transactions_30d": 2,
    "avg_resolution_time_hrs": 24.0532,
    "emi_bounce_30d": 0
  },
  "extra_context": {
    "customer_profile": {
      "segment": "farmer",
      "income_regularity": "seasonal",
      "tenure_months": 200,
      "age": 47,
      "customer_yearly_value": 30088.3252,
      "products_count": 2,
      "has_credit_card": 0,
      "has_loan": 1,
      "value_tier": "low"
    },
    "recent_complaint_text": "SMS charge, card charge, AMC charge. Har mahine kuch na kuch kat ta hai."
  }
}
```

Response:

```json
{
  "meta": {
    "endpoint": "/predict/both",
    "served_at": "2026-08-31T00:56:35",
    "elapsed_ms": 2040.1,
    "timings_ms": {
      "model1": 99.83,
      "model2": 1940.15
    },
    "customer_id": "C15022",
    "customer_name": "Warjas Dani",
    "snapshot_date": "2026-06-01"
  },
  "model1": {
    "churn_probability": 41.19,
    "raw_churn_probability": 94.37,
    "probability_mode": "sigmoid",
    "risk_score": 77.95,
    "churn_prediction": "Yes",
    "risk_level": "High",
    "top_risk_factors": [
      {
        "factor": "latest_days_since_last_transaction",
        "value": 22,
        "message": "Customer has gone longer without transacting.",
        "contribution": 0.701685905456543
      },
      {
        "factor": "latest_transaction_change_30d",
        "value": -71.0705,
        "message": "Transaction activity has been falling across recent months.",
        "contribution": 0.500750720500946
      },
      {
        "factor": "latest_vs_avg_upi_share_of_spend_available_history",
        "value": 0.08748333333333336,
        "message": "A larger share of spending is happening through UPI.",
        "contribution": 0.26149970293045044
      },
      {
        "factor": "latest_balance_change_30d",
        "value": -49.3237,
        "message": "Balance has been falling across recent months.",
        "contribution": 0.23652184009552002
      },
      {
        "factor": "latest_card_spend_change_30d",
        "value": -51.0771,
        "message": "Card spending has been falling across recent months.",
        "contribution": 0.18308348953723907
      }
    ]
  },
  "model2_input": {
    "customer_context": {
      "age": 47,
      "tenure_months": 200,
      "customer_segment": "farmer",
      "income_regularity": "seasonal",
      "customer_yearly_value": 30088.3252,
      "products_count": 2,
      "has_credit_card": 0,
      "has_loan": 1
    },
    "behavior": {
      "days_since_last_transaction": 22,
      "balance_change_30d": -49.3237,
      "transaction_change_30d": -71.0705,
      "card_spend_change_30d": -51.0771,
      "app_login_change_30d": -75.8739,
      "salary_missing_days": null,
      "external_transfer_change_30d": 100.5435,
      "upi_share_of_spend": 0.3884,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 1,
      "emi_bounce_30d": 0
    },
    "service_evidence": {
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 2,
      "avg_resolution_time_hrs": 24.0532,
      "complaint_text": "SMS charge, card charge, AMC charge. Har mahine kuch na kuch kat ta hai."
    },
    "model1": {
      "churn_probability": 0.4119,
      "churn_prediction": "Yes",
      "risk_level": "High",
      "top_risk_factors": [
        {
          "factor": "days_since_last_transaction",
          "value": 22
        },
        {
          "factor": "transaction_change_30d",
          "value": -71.0705
        },
        {
          "factor": "vs_avg_upi_share_of_spend_available_history",
          "value": 0.08748333333333336
        },
        {
          "factor": "balance_change_30d",
          "value": -49.3237
        },
        {
          "factor": "card_spend_change_30d",
          "value": -51.0771
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
    "case_id": "C15022"
  },
  "model2": {
    "case_id": "C15022",
    "ok": true,
    "prediction": {
      "evidence": [
        "complaints_30d=1",
        "unresolved_complaints=0",
        "avg_resolution_time_hrs=24.1",
        "complaint_text mentions fees"
      ],
      "primary_reason": "FEE_DISSATISFACTION",
      "reasoning_summary": "Complaint evidence suggests dissatisfaction with fees or charges.",
      "recommended_action": "FEE_WAIVER_REVIEW",
      "secondary_reasons": [
        "LOW_ENGAGEMENT"
      ],
      "urgency": "HIGH"
    },
    "raw_text": "{\n  \"evidence\":[\"complaints_30d=1\",\"unresolved_complaints=0\",\"avg_resolution_time_hrs=24.1\",\"complaint_text mentions fees\"],\"primary_reason\":\"FEE_DISSATISFACTION\",\"reasoning_summary\":\"Complaint evidence suggests dissatisfaction with fees or charges.\",\"recommended_action\":\"FEE_WAIVER_REVIEW\",\"secondary_reasons\":[\"LOW_ENGAGEMENT\"],\"urgency\":\"HIGH\"}",
    "error": null,
    "latency_s": 1.94,
    "simple_output": "Reason: FEE_DISSATISFACTION | Urgency: HIGH | Action: FEE_WAIVER_REVIEW | Why: Complaint evidence suggests dissatisfaction with fees or charges."
  }
}
```

### Parth Salvi (`C15042`)

- OK: `False`
- Shape errors: `["model2 returned ok=false: recommended_action: 'FINANCIAL_GUIDANCE' not in eligible_actions ['MONITOR', 'RE_ENGAGEMENT', 'PRODUCT_REVIEW']", 'model2.prediction is missing or not an object']`
- Simple output: Prediction failed: recommended_action: 'FINANCIAL_GUIDANCE' not in eligible_actions ['MONITOR', 'RE_ENGAGEMENT', 'PRODUCT_REVIEW']

Request:

```json
{
  "customer_id": "C15042",
  "customer_name": "Parth Salvi",
  "prediction_date": "2026-01-01",
  "snapshot_date": "2026-01-01",
  "target_month": "2026-02-01",
  "profile": {
    "tenure_months": 111,
    "customer_segment": "business",
    "income_regularity": "irregular",
    "products_count": 3,
    "has_credit_card": 1,
    "has_loan": 0
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 4,
      "balance_change_30d": -4.5785,
      "transaction_change_30d": 4.971,
      "card_spend_change_30d": 14.0608,
      "app_login_change_30d": 15.1598,
      "salary_missing_days": null,
      "external_transfer_change_30d": 53.9834,
      "upi_share_of_spend": 0.4915,
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
    "tenure_months": 111,
    "customer_segment": "business",
    "income_regularity": "irregular",
    "products_count": 3,
    "has_credit_card": 1,
    "has_loan": 0,
    "days_since_last_transaction": 4,
    "balance_change_30d": -4.5785,
    "transaction_change_30d": 4.971,
    "card_spend_change_30d": 14.0608,
    "app_login_change_30d": 15.1598,
    "salary_missing_days": null,
    "external_transfer_change_30d": 53.9834,
    "upi_share_of_spend": 0.4915,
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
      "tenure_months": 111,
      "age": 53,
      "customer_yearly_value": 266399.0763,
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
    "served_at": "2026-08-31T00:56:39",
    "elapsed_ms": 4551.31,
    "timings_ms": {
      "model1": 90.69,
      "model2": 4460.51
    },
    "customer_id": "C15042",
    "customer_name": "Parth Salvi",
    "snapshot_date": "2026-01-01"
  },
  "model1": {
    "churn_probability": 2.71,
    "raw_churn_probability": 25.15,
    "probability_mode": "sigmoid",
    "risk_score": 8.14,
    "churn_prediction": "No",
    "risk_level": "Low",
    "top_risk_factors": [
      {
        "factor": "external_transfer_change_30d_trend_6m",
        "value": 0.0,
        "message": "This signal increased churn risk.",
        "contribution": 0.03379914537072182
      },
      {
        "factor": "avg_external_transfer_change_30d_6m",
        "value": 53.9834,
        "message": "External transfers have increased.",
        "contribution": 0.032580696046352386
      },
      {
        "factor": "transaction_change_30d_trend_6m",
        "value": 0.0,
        "message": "This signal increased churn risk.",
        "contribution": 0.023309921845793724
      },
      {
        "factor": "avg_external_transfer_change_30d_3m",
        "value": 53.9834,
        "message": "External transfers have increased.",
        "contribution": 0.020437220111489296
      },
      {
        "factor": "latest_external_transfer_change_30d",
        "value": 53.9834,
        "message": "External transfers have increased.",
        "contribution": 0.01623467169702053
      }
    ]
  },
  "model2_input": {
    "customer_context": {
      "age": 53,
      "tenure_months": 111,
      "customer_segment": "business",
      "income_regularity": "irregular",
      "customer_yearly_value": 266399.0763,
      "products_count": 3,
      "has_credit_card": 1,
      "has_loan": 0
    },
    "behavior": {
      "days_since_last_transaction": 4,
      "balance_change_30d": -4.5785,
      "transaction_change_30d": 4.971,
      "card_spend_change_30d": 14.0608,
      "app_login_change_30d": 15.1598,
      "salary_missing_days": null,
      "external_transfer_change_30d": 53.9834,
      "upi_share_of_spend": 0.4915,
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
      "churn_probability": 0.0271,
      "churn_prediction": "No",
      "risk_level": "Low",
      "top_risk_factors": [
        {
          "factor": "external_transfer_change_30d_trend_6m",
          "value": 0.0
        },
        {
          "factor": "avg_external_transfer_change_30d_6m",
          "value": 53.9834
        },
        {
          "factor": "transaction_change_30d_trend_6m",
          "value": 0.0
        },
        {
          "factor": "avg_external_transfer_change_30d_3m",
          "value": 53.9834
        },
        {
          "factor": "external_transfer_change_30d",
          "value": 53.9834
        }
      ]
    },
    "eligible_actions": [
      "MONITOR",
      "RE_ENGAGEMENT",
      "PRODUCT_REVIEW"
    ],
    "case_id": "C15042"
  },
  "model2": {
    "case_id": "C15042",
    "ok": false,
    "prediction": null,
    "raw_text": "{\"evidence\":[\"transaction_change_30d=4.97\",\"balance_change_30d=-4.58\"],\"primary_reason\":\"FINANCIAL_STRESS\",\"reasoning_summary\":\"The evidence suggests this because transaction_change_30d=4.97 and balance_change_30d=-4.58 point to a financial stress issue.\",\"recommended_action\":\"FINANCIAL_GUIDANCE\",\"secondary_reasons\":[\"LOW_ENGAGEMENT\"],\"urgency\":\"HIGH\"}",
    "error": "recommended_action: 'FINANCIAL_GUIDANCE' not in eligible_actions ['MONITOR', 'RE_ENGAGEMENT', 'PRODUCT_REVIEW']",
    "latency_s": 4.4604,
    "simple_output": "Prediction failed: recommended_action: 'FINANCIAL_GUIDANCE' not in eligible_actions ['MONITOR', 'RE_ENGAGEMENT', 'PRODUCT_REVIEW']"
  }
}
```

### Benjamin Kumer (`C15712`)

- OK: `True`
- Shape errors: `[]`
- Simple output: Reason: FEE_DISSATISFACTION | Urgency: HIGH | Action: FEE_WAIVER_REVIEW | Why: Complaint evidence suggests dissatisfaction with fees or charges. Evidence suggests this because complaints_30d=6; unresolved_complaints=5.

Request:

```json
{
  "customer_id": "C15712",
  "customer_name": "Benjamin Kumer",
  "prediction_date": "2026-04-01",
  "snapshot_date": "2026-04-01",
  "target_month": "2026-05-01",
  "profile": {
    "tenure_months": 33,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 3,
    "has_credit_card": 1,
    "has_loan": 0
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 7,
      "balance_change_30d": 10.0081,
      "transaction_change_30d": 17.6367,
      "card_spend_change_30d": -20.1167,
      "app_login_change_30d": 2.2812,
      "salary_missing_days": 1.0,
      "external_transfer_change_30d": 17.1027,
      "upi_share_of_spend": 0.4604,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 6,
      "unresolved_complaints": 5,
      "failed_transactions_30d": 4,
      "avg_resolution_time_hrs": 99.8597,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-02-01",
      "days_since_last_transaction": 10,
      "balance_change_30d": -9.4968,
      "transaction_change_30d": -11.6162,
      "card_spend_change_30d": -4.3503,
      "app_login_change_30d": 2.9281,
      "salary_missing_days": 1.0,
      "external_transfer_change_30d": 26.9036,
      "upi_share_of_spend": 0.4626,
      "fd_maturing_in_30d": 1,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 1,
      "failed_transactions_30d": 3,
      "avg_resolution_time_hrs": 69.1325,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-03-01",
      "days_since_last_transaction": 3,
      "balance_change_30d": 31.4497,
      "transaction_change_30d": 9.7545,
      "card_spend_change_30d": 22.4259,
      "app_login_change_30d": 7.4142,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": 19.6791,
      "upi_share_of_spend": 0.4023,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 2,
      "unresolved_complaints": 1,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 38.0573,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-04-01",
      "days_since_last_transaction": 3,
      "balance_change_30d": 19.9398,
      "transaction_change_30d": 5.9852,
      "card_spend_change_30d": 6.5251,
      "app_login_change_30d": -9.0624,
      "salary_missing_days": 1.0,
      "external_transfer_change_30d": 13.7628,
      "upi_share_of_spend": 0.5257,
      "fd_maturing_in_30d": 1,
      "products_dropped_90d": 0,
      "complaints_30d": 6,
      "unresolved_complaints": 5,
      "failed_transactions_30d": 8,
      "avg_resolution_time_hrs": 127.2192,
      "emi_bounce_30d": 0
    }
  ],
  "customer": {
    "tenure_months": 33,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 3,
    "has_credit_card": 1,
    "has_loan": 0,
    "days_since_last_transaction": 3,
    "balance_change_30d": 19.9398,
    "transaction_change_30d": 5.9852,
    "card_spend_change_30d": 6.5251,
    "app_login_change_30d": -9.0624,
    "salary_missing_days": 1.0,
    "external_transfer_change_30d": 13.7628,
    "upi_share_of_spend": 0.5257,
    "fd_maturing_in_30d": 1,
    "products_dropped_90d": 0,
    "complaints_30d": 6,
    "unresolved_complaints": 5,
    "failed_transactions_30d": 8,
    "avg_resolution_time_hrs": 127.2192,
    "emi_bounce_30d": 0
  },
  "extra_context": {
    "customer_profile": {
      "segment": "salary",
      "income_regularity": "regular",
      "tenure_months": 33,
      "age": 24,
      "customer_yearly_value": 57278.7768,
      "products_count": 3,
      "has_credit_card": 1,
      "has_loan": 0,
      "value_tier": "medium"
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
    "served_at": "2026-08-31T00:56:42",
    "elapsed_ms": 2482.88,
    "timings_ms": {
      "model1": 110.6,
      "model2": 2372.18
    },
    "customer_id": "C15712",
    "customer_name": "Benjamin Kumer",
    "snapshot_date": "2026-04-01"
  },
  "model1": {
    "churn_probability": 34.24,
    "raw_churn_probability": 88.01,
    "probability_mode": "sigmoid",
    "risk_score": 75.34,
    "churn_prediction": "Yes",
    "risk_level": "High",
    "top_risk_factors": [
      {
        "factor": "max_avg_resolution_time_hrs_3m",
        "value": 127.2192,
        "message": "Recent complaints took longer to resolve.",
        "contribution": 0.5943911671638489
      },
      {
        "factor": "latest_avg_resolution_time_hrs",
        "value": 127.2192,
        "message": "Recent complaints took longer to resolve.",
        "contribution": 0.37605658173561096
      },
      {
        "factor": "sum_failed_transactions_30d_3m",
        "value": 12.0,
        "message": "Customer has recent failed transactions.",
        "contribution": 0.3342980444431305
      },
      {
        "factor": "sum_failed_transactions_30d_6m",
        "value": 16.0,
        "message": "Customer has recent failed transactions.",
        "contribution": 0.14342807233333588
      },
      {
        "factor": "latest_fd_maturing_in_30d",
        "value": 1,
        "message": "Customer has a fixed deposit maturing soon.",
        "contribution": 0.13961893320083618
      }
    ]
  },
  "model2_input": {
    "customer_context": {
      "age": 24,
      "tenure_months": 33,
      "customer_segment": "salary",
      "income_regularity": "regular",
      "customer_yearly_value": 57278.7768,
      "products_count": 3,
      "has_credit_card": 1,
      "has_loan": 0
    },
    "behavior": {
      "days_since_last_transaction": 3,
      "balance_change_30d": 19.9398,
      "transaction_change_30d": 5.9852,
      "card_spend_change_30d": 6.5251,
      "app_login_change_30d": -9.0624,
      "salary_missing_days": 1,
      "external_transfer_change_30d": 13.7628,
      "upi_share_of_spend": 0.5257,
      "fd_maturing_in_30d": 1,
      "products_dropped_90d": 0,
      "emi_bounce_30d": 0
    },
    "service_evidence": {
      "complaints_30d": 6,
      "unresolved_complaints": 5,
      "failed_transactions_30d": 8,
      "avg_resolution_time_hrs": 127.2192,
      "complaint_text": "Card cloned and used at some other city. Why no SMS alert came?"
    },
    "model1": {
      "churn_probability": 0.3424,
      "churn_prediction": "Yes",
      "risk_level": "High",
      "top_risk_factors": [
        {
          "factor": "max_avg_resolution_time_hrs_3m",
          "value": 127.2192
        },
        {
          "factor": "avg_resolution_time_hrs",
          "value": 127.2192
        },
        {
          "factor": "sum_failed_transactions_30d_3m",
          "value": 12.0
        },
        {
          "factor": "sum_failed_transactions_30d_6m",
          "value": 16.0
        },
        {
          "factor": "fd_maturing_in_30d",
          "value": 1
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
    "case_id": "C15712"
  },
  "model2": {
    "case_id": "C15712",
    "ok": true,
    "prediction": {
      "evidence": [
        "complaints_30d=6",
        "unresolved_complaints=5",
        "avg_resolution_time_hrs=127.2",
        "complaint_text mentions fees or charges",
        "complaint_text mentions digital or app issues"
      ],
      "primary_reason": "FEE_DISSATISFACTION",
      "reasoning_summary": "Complaint evidence suggests dissatisfaction with fees or charges. Evidence suggests this because complaints_30d=6; unresolved_complaints=5.",
      "recommended_action": "FEE_WAIVER_REVIEW",
      "secondary_reasons": [
        "DIGITAL_FRICTION"
      ],
      "urgency": "HIGH"
    },
    "raw_text": "{\n  \"evidence\":[\"complaints_30d=6\",\"unresolved_complaints=5\",\"avg_resolution_time_hrs=127.2\",\"complaint_text mentions fees or charges\",\"complaint_text mentions digital or app issues\"],\"primary_reason\":\"FEE_DISSATISFACTION\",\"reasoning_summary\":\"Complaint evidence suggests dissatisfaction with fees or charges. Evidence suggests this because complaints_30d=6; unresolved_complaints=5.\",\"recommended_action\":\"FEE_WAIVER_REVIEW\",\"secondary_reasons\":[\"DIGITAL_FRICTION\"],\"urgency\":\"HIGH\"}",
    "error": null,
    "latency_s": 2.372,
    "simple_output": "Reason: FEE_DISSATISFACTION | Urgency: HIGH | Action: FEE_WAIVER_REVIEW | Why: Complaint evidence suggests dissatisfaction with fees or charges. Evidence suggests this because complaints_30d=6; unresolved_complaints=5."
  }
}
```

### Xavier Atwal (`C15921`)

- OK: `True`
- Shape errors: `[]`
- Simple output: Reason: SERVICE_DISSATISFACTION | Urgency: HIGH | Action: SERVICE_RECOVERY | Why: Service friction is the most supported explanation for the current relationship issue. Service recovery fits because complaints_30d=0 and unresolved_complaints=0 suggest the issue is unresolved or operationally based rather than product-specific.

Request:

```json
{
  "customer_id": "C15921",
  "customer_name": "Xavier Atwal",
  "prediction_date": "2026-06-01",
  "snapshot_date": "2026-06-01",
  "target_month": "2026-07-01",
  "profile": {
    "tenure_months": 148,
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
      "balance_change_30d": -17.1424,
      "transaction_change_30d": 18.6706,
      "card_spend_change_30d": 25.6372,
      "app_login_change_30d": -1.6517,
      "salary_missing_days": 2.0,
      "external_transfer_change_30d": 19.9654,
      "upi_share_of_spend": 0.6592,
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
      "balance_change_30d": 6.8283,
      "transaction_change_30d": -3.4803,
      "card_spend_change_30d": -8.4036,
      "app_login_change_30d": -8.4189,
      "salary_missing_days": 2.0,
      "external_transfer_change_30d": -11.1321,
      "upi_share_of_spend": 0.6803,
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
      "balance_change_30d": -19.8627,
      "transaction_change_30d": -17.1877,
      "card_spend_change_30d": 1.9032,
      "app_login_change_30d": 19.0779,
      "salary_missing_days": 4.0,
      "external_transfer_change_30d": 92.3213,
      "upi_share_of_spend": 0.7801,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 7.1654,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-04-01",
      "days_since_last_transaction": 9,
      "balance_change_30d": -25.7632,
      "transaction_change_30d": -6.1839,
      "card_spend_change_30d": -11.4764,
      "app_login_change_30d": -15.8699,
      "salary_missing_days": 4.0,
      "external_transfer_change_30d": 60.7745,
      "upi_share_of_spend": 0.7635,
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
      "balance_change_30d": 10.5267,
      "transaction_change_30d": 17.8685,
      "card_spend_change_30d": -11.3831,
      "app_login_change_30d": -19.9805,
      "salary_missing_days": 1.0,
      "external_transfer_change_30d": -29.1106,
      "upi_share_of_spend": 0.7489,
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
      "balance_change_30d": 3.2877,
      "transaction_change_30d": 4.6801,
      "card_spend_change_30d": 18.6044,
      "app_login_change_30d": -12.4994,
      "salary_missing_days": 2.0,
      "external_transfer_change_30d": -29.4008,
      "upi_share_of_spend": 0.5639,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 1,
      "complaints_30d": 0,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 2,
      "avg_resolution_time_hrs": 0.0,
      "emi_bounce_30d": 0
    }
  ],
  "customer": {
    "tenure_months": 148,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 2,
    "has_credit_card": 0,
    "has_loan": 0,
    "days_since_last_transaction": 2,
    "balance_change_30d": 3.2877,
    "transaction_change_30d": 4.6801,
    "card_spend_change_30d": 18.6044,
    "app_login_change_30d": -12.4994,
    "salary_missing_days": 2.0,
    "external_transfer_change_30d": -29.4008,
    "upi_share_of_spend": 0.5639,
    "fd_maturing_in_30d": 0,
    "products_dropped_90d": 1,
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
      "tenure_months": 148,
      "age": 32,
      "customer_yearly_value": 14733.2626,
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
    "served_at": "2026-08-31T00:56:44",
    "elapsed_ms": 2551.74,
    "timings_ms": {
      "model1": 69.76,
      "model2": 2481.85
    },
    "customer_id": "C15921",
    "customer_name": "Xavier Atwal",
    "snapshot_date": "2026-06-01"
  },
  "model1": {
    "churn_probability": 1.97,
    "raw_churn_probability": 18.1,
    "probability_mode": "sigmoid",
    "risk_score": 5.91,
    "churn_prediction": "No",
    "risk_level": "Low",
    "top_risk_factors": [
      {
        "factor": "latest_vs_avg_external_transfer_change_30d_available_history",
        "value": -46.63708333333334,
        "message": "This signal increased churn risk.",
        "contribution": 0.053830113261938095
      },
      {
        "factor": "latest_upi_share_of_spend",
        "value": 0.5639,
        "message": "A larger share of spending is happening through UPI.",
        "contribution": 0.02368553914129734
      },
      {
        "factor": "avg_upi_share_of_spend_6m",
        "value": 0.6993166666666667,
        "message": "A larger share of spending is happening through UPI.",
        "contribution": 0.022527307271957397
      },
      {
        "factor": "avg_app_login_change_30d_3m",
        "value": -16.116600000000002,
        "message": "App usage has been falling across recent months.",
        "contribution": 0.022417904809117317
      },
      {
        "factor": "max_days_since_last_transaction_3m",
        "value": 9.0,
        "message": "Customer has gone longer without transacting.",
        "contribution": 0.017192000523209572
      }
    ]
  },
  "model2_input": {
    "customer_context": {
      "age": 32,
      "tenure_months": 148,
      "customer_segment": "salary",
      "income_regularity": "regular",
      "customer_yearly_value": 14733.2626,
      "products_count": 2,
      "has_credit_card": 0,
      "has_loan": 0
    },
    "behavior": {
      "days_since_last_transaction": 2,
      "balance_change_30d": 3.2877,
      "transaction_change_30d": 4.6801,
      "card_spend_change_30d": 18.6044,
      "app_login_change_30d": -12.4994,
      "salary_missing_days": 2,
      "external_transfer_change_30d": -29.4008,
      "upi_share_of_spend": 0.5639,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 1,
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
          "factor": "vs_avg_external_transfer_change_30d_available_history",
          "value": -46.63708333333334
        },
        {
          "factor": "upi_share_of_spend",
          "value": 0.5639
        },
        {
          "factor": "avg_upi_share_of_spend_6m",
          "value": 0.6993166666666667
        },
        {
          "factor": "avg_app_login_change_30d_3m",
          "value": -16.116600000000002
        },
        {
          "factor": "max_days_since_last_transaction_3m",
          "value": 9.0
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
    "case_id": "C15921"
  },
  "model2": {
    "case_id": "C15921",
    "ok": true,
    "prediction": {
      "evidence": [
        "complaints_30d=0",
        "unresolved_complaints=0",
        "failed_transactions_30d=2",
        "avg_resolution_time_hrs=0.0"
      ],
      "primary_reason": "SERVICE_DISSATISFACTION",
      "reasoning_summary": "Service friction is the most supported explanation for the current relationship issue. Service recovery fits because complaints_30d=0 and unresolved_complaints=0 suggest the issue is unresolved or operationally based rather than product-specific.",
      "recommended_action": "SERVICE_RECOVERY",
      "secondary_reasons": [
        "DIGITAL_FRICTION"
      ],
      "urgency": "HIGH"
    },
    "raw_text": "{\n  \"evidence\":[\"complaints_30d=0\",\"unresolved_complaints=0\",\"failed_transactions_30d=2\",\"avg_resolution_time_hrs=0.0\"],\"primary_reason\":\"SERVICE_DISSATISFACTION\",\"reasoning_summary\":\"Service friction is the most supported explanation for the current relationship issue. Service recovery fits because complaints_30d=0 and unresolved_complaints=0 suggest the issue is unresolved or operationally based rather than product-specific.\",\"recommended_action\":\"SERVICE_RECOVERY\",\"secondary_reasons\":[\"DIGITAL_FRICTION\"],\"urgency\":\"HIGH\"}",
    "error": null,
    "latency_s": 2.4816,
    "simple_output": "Reason: SERVICE_DISSATISFACTION | Urgency: HIGH | Action: SERVICE_RECOVERY | Why: Service friction is the most supported explanation for the current relationship issue. Service recovery fits because complaints_30d=0 and unresolved_complaints=0 suggest the issue is unresolved or operationally based rather than product-specific."
  }
}
```

### Yashodhara Majumdar (`C15952`)

- OK: `True`
- Shape errors: `[]`
- Simple output: Reason: DIGITAL_FRICTION | Urgency: HIGH | Action: COMPLAINT_ESCALATION | Why: Digital friction is the most supported explanation for the observed service issue pattern. Complaint escalation fits because complaints_30d=0 and unresolved_complaints=0 suggest the complaints are unresolved or operationally serious.

Request:

```json
{
  "customer_id": "C15952",
  "customer_name": "Yashodhara Majumdar",
  "prediction_date": "2026-06-01",
  "snapshot_date": "2026-06-01",
  "target_month": "2026-07-01",
  "profile": {
    "tenure_months": 57,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 4,
    "has_credit_card": 1,
    "has_loan": 0
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 3,
      "balance_change_30d": -9.8613,
      "transaction_change_30d": 31.8142,
      "card_spend_change_30d": 7.2631,
      "app_login_change_30d": -0.7921,
      "salary_missing_days": 1.0,
      "external_transfer_change_30d": 24.2219,
      "upi_share_of_spend": 0.3957,
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
      "balance_change_30d": -21.8383,
      "transaction_change_30d": -3.6674,
      "card_spend_change_30d": -25.3285,
      "app_login_change_30d": -10.2013,
      "salary_missing_days": 4.0,
      "external_transfer_change_30d": 77.8106,
      "upi_share_of_spend": 0.5445,
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
      "balance_change_30d": -18.4563,
      "transaction_change_30d": -24.7198,
      "card_spend_change_30d": -38.5794,
      "app_login_change_30d": -17.4858,
      "salary_missing_days": 2.0,
      "external_transfer_change_30d": 69.8222,
      "upi_share_of_spend": 0.5862,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 1,
      "failed_transactions_30d": 3,
      "avg_resolution_time_hrs": 32.9705,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-04-01",
      "days_since_last_transaction": 13,
      "balance_change_30d": -19.4292,
      "transaction_change_30d": -32.9277,
      "card_spend_change_30d": -26.2504,
      "app_login_change_30d": -32.3184,
      "salary_missing_days": 7.0,
      "external_transfer_change_30d": 40.7491,
      "upi_share_of_spend": 0.5215,
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
      "balance_change_30d": -33.6048,
      "transaction_change_30d": -63.3146,
      "card_spend_change_30d": -33.6176,
      "app_login_change_30d": -51.6674,
      "salary_missing_days": 9.0,
      "external_transfer_change_30d": 43.7905,
      "upi_share_of_spend": 0.6047,
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
      "days_since_last_transaction": 21,
      "balance_change_30d": -67.3269,
      "transaction_change_30d": -53.2162,
      "card_spend_change_30d": -61.5297,
      "app_login_change_30d": -63.0777,
      "salary_missing_days": 8.0,
      "external_transfer_change_30d": 85.9056,
      "upi_share_of_spend": 0.5879,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 0,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 5,
      "avg_resolution_time_hrs": 0.0,
      "emi_bounce_30d": 0
    }
  ],
  "customer": {
    "tenure_months": 57,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 4,
    "has_credit_card": 1,
    "has_loan": 0,
    "days_since_last_transaction": 21,
    "balance_change_30d": -67.3269,
    "transaction_change_30d": -53.2162,
    "card_spend_change_30d": -61.5297,
    "app_login_change_30d": -63.0777,
    "salary_missing_days": 8.0,
    "external_transfer_change_30d": 85.9056,
    "upi_share_of_spend": 0.5879,
    "fd_maturing_in_30d": 0,
    "products_dropped_90d": 0,
    "complaints_30d": 0,
    "unresolved_complaints": 0,
    "failed_transactions_30d": 5,
    "avg_resolution_time_hrs": 0.0,
    "emi_bounce_30d": 0
  },
  "extra_context": {
    "customer_profile": {
      "segment": "salary",
      "income_regularity": "regular",
      "tenure_months": 57,
      "age": 34,
      "customer_yearly_value": 31350.6245,
      "products_count": 4,
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
    "served_at": "2026-08-31T00:56:49",
    "elapsed_ms": 4675.97,
    "timings_ms": {
      "model1": 61.99,
      "model2": 4613.88
    },
    "customer_id": "C15952",
    "customer_name": "Yashodhara Majumdar",
    "snapshot_date": "2026-06-01"
  },
  "model1": {
    "churn_probability": 44.32,
    "raw_churn_probability": 97.11,
    "probability_mode": "sigmoid",
    "risk_score": 79.12,
    "churn_prediction": "Yes",
    "risk_level": "High",
    "top_risk_factors": [
      {
        "factor": "latest_days_since_last_transaction",
        "value": 21,
        "message": "Customer has gone longer without transacting.",
        "contribution": 0.6060196757316589
      },
      {
        "factor": "latest_transaction_change_30d",
        "value": -53.2162,
        "message": "Transaction activity has been falling across recent months.",
        "contribution": 0.42691707611083984
      },
      {
        "factor": "max_salary_missing_days_3m",
        "value": 9.0,
        "message": "Salary or pension was delayed recently.",
        "contribution": 0.29357922077178955
      },
      {
        "factor": "latest_salary_missing_days",
        "value": 8.0,
        "message": "Salary or pension was delayed recently.",
        "contribution": 0.2606256902217865
      },
      {
        "factor": "latest_balance_change_30d",
        "value": -67.3269,
        "message": "Balance has been falling across recent months.",
        "contribution": 0.22201959788799286
      }
    ]
  },
  "model2_input": {
    "customer_context": {
      "age": 34,
      "tenure_months": 57,
      "customer_segment": "salary",
      "income_regularity": "regular",
      "customer_yearly_value": 31350.6245,
      "products_count": 4,
      "has_credit_card": 1,
      "has_loan": 0
    },
    "behavior": {
      "days_since_last_transaction": 21,
      "balance_change_30d": -67.3269,
      "transaction_change_30d": -53.2162,
      "card_spend_change_30d": -61.5297,
      "app_login_change_30d": -63.0777,
      "salary_missing_days": 8,
      "external_transfer_change_30d": 85.9056,
      "upi_share_of_spend": 0.5879,
      "fd_maturing_in_30d": 0,
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
      "churn_probability": 0.4432,
      "churn_prediction": "Yes",
      "risk_level": "High",
      "top_risk_factors": [
        {
          "factor": "days_since_last_transaction",
          "value": 21
        },
        {
          "factor": "transaction_change_30d",
          "value": -53.2162
        },
        {
          "factor": "max_salary_missing_days_3m",
          "value": 9.0
        },
        {
          "factor": "salary_missing_days",
          "value": 8.0
        },
        {
          "factor": "balance_change_30d",
          "value": -67.3269
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
    "case_id": "C15952"
  },
  "model2": {
    "case_id": "C15952",
    "ok": true,
    "prediction": {
      "evidence": [
        "complaints_30d=0",
        "unresolved_complaints=0",
        "failed_transactions_30d=5"
      ],
      "primary_reason": "DIGITAL_FRICTION",
      "reasoning_summary": "Digital friction is the most supported explanation for the observed service issue pattern. Complaint escalation fits because complaints_30d=0 and unresolved_complaints=0 suggest the complaints are unresolved or operationally serious.",
      "recommended_action": "COMPLAINT_ESCALATION",
      "secondary_reasons": [],
      "urgency": "HIGH"
    },
    "raw_text": "{\"evidence\":[\"complaints_30d=0\",\"unresolved_complaints=0\",\"failed_transactions_30d=5\"],\"primary_reason\":\"DIGITAL_FRICTION\",\"reasoning_summary\":\"Digital friction is the most supported explanation for the observed service issue pattern. Complaint escalation fits because complaints_30d=0 and unresolved_complaints=0 suggest the complaints are unresolved or operationally serious.\",\"recommended_action\":\"COMPLAINT_ESCALATION\",\"secondary_reasons\":[],\"urgency\":\"HIGH\"}",
    "error": null,
    "latency_s": 4.6134,
    "simple_output": "Reason: DIGITAL_FRICTION | Urgency: HIGH | Action: COMPLAINT_ESCALATION | Why: Digital friction is the most supported explanation for the observed service issue pattern. Complaint escalation fits because complaints_30d=0 and unresolved_complaints=0 suggest the complaints are unresolved or operationally serious."
  }
}
```

### Anamika Bhat (`C17024`)

- OK: `True`
- Shape errors: `[]`
- Simple output: Reason: SERVICE_DISSATISFACTION | Urgency: HIGH | Action: SERVICE_RECOVERY | Why: Complaint and transaction data suggest a real-service issue without clear escalation-level severity or volume.

Request:

```json
{
  "customer_id": "C17024",
  "customer_name": "Anamika Bhat",
  "prediction_date": "2026-06-01",
  "snapshot_date": "2026-06-01",
  "target_month": "2026-07-01",
  "profile": {
    "tenure_months": 81,
    "customer_segment": "pension",
    "income_regularity": "regular",
    "products_count": 2,
    "has_credit_card": 0,
    "has_loan": 1
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 6,
      "balance_change_30d": -7.1115,
      "transaction_change_30d": 28.362,
      "card_spend_change_30d": -6.5924,
      "app_login_change_30d": 21.216,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -17.0584,
      "upi_share_of_spend": 0.5797,
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
      "balance_change_30d": 20.6709,
      "transaction_change_30d": 5.5229,
      "card_spend_change_30d": -7.5874,
      "app_login_change_30d": 5.6751,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": 49.5093,
      "upi_share_of_spend": 0.5709,
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
      "days_since_last_transaction": 11,
      "balance_change_30d": -27.3491,
      "transaction_change_30d": -28.4288,
      "card_spend_change_30d": -7.8717,
      "app_login_change_30d": -16.8698,
      "salary_missing_days": 2.0,
      "external_transfer_change_30d": 23.1637,
      "upi_share_of_spend": 0.747,
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
      "days_since_last_transaction": 18,
      "balance_change_30d": -17.6156,
      "transaction_change_30d": -1.6385,
      "card_spend_change_30d": -36.2967,
      "app_login_change_30d": -48.9987,
      "salary_missing_days": 1.0,
      "external_transfer_change_30d": 19.3956,
      "upi_share_of_spend": 0.7931,
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
      "days_since_last_transaction": 7,
      "balance_change_30d": -14.5181,
      "transaction_change_30d": 0.6265,
      "card_spend_change_30d": -9.6111,
      "app_login_change_30d": -13.812,
      "salary_missing_days": 1.0,
      "external_transfer_change_30d": 50.9103,
      "upi_share_of_spend": 0.6889,
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
      "days_since_last_transaction": 12,
      "balance_change_30d": -21.4619,
      "transaction_change_30d": -33.5997,
      "card_spend_change_30d": -19.6677,
      "app_login_change_30d": -43.753,
      "salary_missing_days": 2.0,
      "external_transfer_change_30d": 38.2632,
      "upi_share_of_spend": 0.8138,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 2,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 4,
      "avg_resolution_time_hrs": 16.9234,
      "emi_bounce_30d": 0
    }
  ],
  "customer": {
    "tenure_months": 81,
    "customer_segment": "pension",
    "income_regularity": "regular",
    "products_count": 2,
    "has_credit_card": 0,
    "has_loan": 1,
    "days_since_last_transaction": 12,
    "balance_change_30d": -21.4619,
    "transaction_change_30d": -33.5997,
    "card_spend_change_30d": -19.6677,
    "app_login_change_30d": -43.753,
    "salary_missing_days": 2.0,
    "external_transfer_change_30d": 38.2632,
    "upi_share_of_spend": 0.8138,
    "fd_maturing_in_30d": 0,
    "products_dropped_90d": 0,
    "complaints_30d": 2,
    "unresolved_complaints": 0,
    "failed_transactions_30d": 4,
    "avg_resolution_time_hrs": 16.9234,
    "emi_bounce_30d": 0
  },
  "extra_context": {
    "customer_profile": {
      "segment": "pension",
      "income_regularity": "regular",
      "tenure_months": 81,
      "age": 66,
      "customer_yearly_value": 9539.0069,
      "products_count": 2,
      "has_credit_card": 0,
      "has_loan": 1,
      "value_tier": "low"
    },
    "recent_complaint_text": "Mera UPI PIN reset nahi ho raha. Branch me bhi koi help nahi mili."
  }
}
```

Response:

```json
{
  "meta": {
    "endpoint": "/predict/both",
    "served_at": "2026-08-31T00:56:51",
    "elapsed_ms": 2071.03,
    "timings_ms": {
      "model1": 90.56,
      "model2": 1980.38
    },
    "customer_id": "C17024",
    "customer_name": "Anamika Bhat",
    "snapshot_date": "2026-06-01"
  },
  "model1": {
    "churn_probability": 27.07,
    "raw_churn_probability": 80.73,
    "probability_mode": "sigmoid",
    "risk_score": 72.65,
    "churn_prediction": "Yes",
    "risk_level": "High",
    "top_risk_factors": [
      {
        "factor": "latest_transaction_change_30d",
        "value": -33.5997,
        "message": "Transaction activity has been falling across recent months.",
        "contribution": 0.24604962766170502
      },
      {
        "factor": "latest_vs_avg_upi_share_of_spend_available_history",
        "value": 0.1149,
        "message": "A larger share of spending is happening through UPI.",
        "contribution": 0.2051452249288559
      },
      {
        "factor": "latest_failed_transactions_30d",
        "value": 4,
        "message": "Customer has recent failed transactions.",
        "contribution": 0.16617758572101593
      },
      {
        "factor": "latest_balance_change_30d",
        "value": -21.4619,
        "message": "Balance has been falling across recent months.",
        "contribution": 0.1327434927225113
      },
      {
        "factor": "sum_failed_transactions_30d_6m",
        "value": 8.0,
        "message": "Customer has recent failed transactions.",
        "contribution": 0.13205230236053467
      }
    ]
  },
  "model2_input": {
    "customer_context": {
      "age": 66,
      "tenure_months": 81,
      "customer_segment": "pension",
      "income_regularity": "regular",
      "customer_yearly_value": 9539.0069,
      "products_count": 2,
      "has_credit_card": 0,
      "has_loan": 1
    },
    "behavior": {
      "days_since_last_transaction": 12,
      "balance_change_30d": -21.4619,
      "transaction_change_30d": -33.5997,
      "card_spend_change_30d": -19.6677,
      "app_login_change_30d": -43.753,
      "salary_missing_days": 2,
      "external_transfer_change_30d": 38.2632,
      "upi_share_of_spend": 0.8138,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "emi_bounce_30d": 0
    },
    "service_evidence": {
      "complaints_30d": 2,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 4,
      "avg_resolution_time_hrs": 16.9234,
      "complaint_text": "Mera UPI PIN reset nahi ho raha. Branch me bhi koi help nahi mili."
    },
    "model1": {
      "churn_probability": 0.2707,
      "churn_prediction": "Yes",
      "risk_level": "High",
      "top_risk_factors": [
        {
          "factor": "transaction_change_30d",
          "value": -33.5997
        },
        {
          "factor": "vs_avg_upi_share_of_spend_available_history",
          "value": 0.1149
        },
        {
          "factor": "failed_transactions_30d",
          "value": 4
        },
        {
          "factor": "balance_change_30d",
          "value": -21.4619
        },
        {
          "factor": "sum_failed_transactions_30d_6m",
          "value": 8.0
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
    "case_id": "C17024"
  },
  "model2": {
    "case_id": "C17024",
    "ok": true,
    "prediction": {
      "evidence": [
        "complaints_30d=2",
        "unresolved_complaints=0",
        "avg_resolution_time_hrs=16.9",
        "complaint_text describes a recent service issue"
      ],
      "primary_reason": "SERVICE_DISSATISFACTION",
      "reasoning_summary": "Complaint and transaction data suggest a real-service issue without clear escalation-level severity or volume.",
      "recommended_action": "SERVICE_RECOVERY",
      "secondary_reasons": [
        "DIGITAL_FRICTION"
      ],
      "urgency": "HIGH"
    },
    "raw_text": "{\n  \"evidence\":[\"complaints_30d=2\",\"unresolved_complaints=0\",\"avg_resolution_time_hrs=16.9\",\"complaint_text describes a recent service issue\"],\"primary_reason\":\"SERVICE_DISSATISFACTION\",\"reasoning_summary\":\"Complaint and transaction data suggest a real-service issue without clear escalation-level severity or volume.\",\"recommended_action\":\"SERVICE_RECOVERY\",\"secondary_reasons\":[\"DIGITAL_FRICTION\"],\"urgency\":\"HIGH\"}",
    "error": null,
    "latency_s": 1.9802,
    "simple_output": "Reason: SERVICE_DISSATISFACTION | Urgency: HIGH | Action: SERVICE_RECOVERY | Why: Complaint and transaction data suggest a real-service issue without clear escalation-level severity or volume."
  }
}
```

### Garima Nagi (`C17447`)

- OK: `True`
- Shape errors: `[]`
- Simple output: Reason: FEE_DISSATISFACTION | Urgency: HIGH | Action: FEE_WAIVER_REVIEW | Why: Complaint evidence suggests dissatisfaction with fees or charges.

Request:

```json
{
  "customer_id": "C17447",
  "customer_name": "Garima Nagi",
  "prediction_date": "2026-04-01",
  "snapshot_date": "2026-04-01",
  "target_month": "2026-05-01",
  "profile": {
    "tenure_months": 43,
    "customer_segment": "farmer",
    "income_regularity": "seasonal",
    "products_count": 3,
    "has_credit_card": 0,
    "has_loan": 1
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 4,
      "balance_change_30d": -2.2147,
      "transaction_change_30d": 12.9272,
      "card_spend_change_30d": 3.5893,
      "app_login_change_30d": 26.0012,
      "salary_missing_days": null,
      "external_transfer_change_30d": 10.8657,
      "upi_share_of_spend": 0.5669,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 3,
      "unresolved_complaints": 3,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 90.8833,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-02-01",
      "days_since_last_transaction": 8,
      "balance_change_30d": 10.325,
      "transaction_change_30d": -1.9588,
      "card_spend_change_30d": -16.4743,
      "app_login_change_30d": -13.8991,
      "salary_missing_days": null,
      "external_transfer_change_30d": 19.9327,
      "upi_share_of_spend": 0.5261,
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
      "days_since_last_transaction": 1,
      "balance_change_30d": 6.4065,
      "transaction_change_30d": 21.7554,
      "card_spend_change_30d": 33.0602,
      "app_login_change_30d": 11.3879,
      "salary_missing_days": null,
      "external_transfer_change_30d": 14.5062,
      "upi_share_of_spend": 0.6072,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 3,
      "unresolved_complaints": 3,
      "failed_transactions_30d": 2,
      "avg_resolution_time_hrs": 74.9097,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-04-01",
      "days_since_last_transaction": 0,
      "balance_change_30d": 9.414,
      "transaction_change_30d": 21.8115,
      "card_spend_change_30d": 11.1721,
      "app_login_change_30d": 16.5729,
      "salary_missing_days": null,
      "external_transfer_change_30d": 42.4233,
      "upi_share_of_spend": 0.5099,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 4,
      "unresolved_complaints": 3,
      "failed_transactions_30d": 7,
      "avg_resolution_time_hrs": 99.0341,
      "emi_bounce_30d": 0
    }
  ],
  "customer": {
    "tenure_months": 43,
    "customer_segment": "farmer",
    "income_regularity": "seasonal",
    "products_count": 3,
    "has_credit_card": 0,
    "has_loan": 1,
    "days_since_last_transaction": 0,
    "balance_change_30d": 9.414,
    "transaction_change_30d": 21.8115,
    "card_spend_change_30d": 11.1721,
    "app_login_change_30d": 16.5729,
    "salary_missing_days": null,
    "external_transfer_change_30d": 42.4233,
    "upi_share_of_spend": 0.5099,
    "fd_maturing_in_30d": 0,
    "products_dropped_90d": 0,
    "complaints_30d": 4,
    "unresolved_complaints": 3,
    "failed_transactions_30d": 7,
    "avg_resolution_time_hrs": 99.0341,
    "emi_bounce_30d": 0
  },
  "extra_context": {
    "customer_profile": {
      "segment": "farmer",
      "income_regularity": "seasonal",
      "tenure_months": 43,
      "age": 34,
      "customer_yearly_value": 16052.0473,
      "products_count": 3,
      "has_credit_card": 0,
      "has_loan": 1,
      "value_tier": "low"
    },
    "recent_complaint_text": "Bank walon ne bola system update hai, teen din se yehi sun raha hoon."
  }
}
```

Response:

```json
{
  "meta": {
    "endpoint": "/predict/both",
    "served_at": "2026-08-31T00:56:53",
    "elapsed_ms": 2176.03,
    "timings_ms": {
      "model1": 75.02,
      "model2": 2100.88
    },
    "customer_id": "C17447",
    "customer_name": "Garima Nagi",
    "snapshot_date": "2026-04-01"
  },
  "model1": {
    "churn_probability": 27.76,
    "raw_churn_probability": 81.48,
    "probability_mode": "sigmoid",
    "risk_score": 72.91,
    "churn_prediction": "Yes",
    "risk_level": "High",
    "top_risk_factors": [
      {
        "factor": "max_avg_resolution_time_hrs_3m",
        "value": 99.0341,
        "message": "Recent complaints took longer to resolve.",
        "contribution": 0.5913301706314087
      },
      {
        "factor": "latest_avg_resolution_time_hrs",
        "value": 99.0341,
        "message": "Recent complaints took longer to resolve.",
        "contribution": 0.40492507815361023
      },
      {
        "factor": "sum_failed_transactions_30d_3m",
        "value": 11.0,
        "message": "Customer has recent failed transactions.",
        "contribution": 0.3480205535888672
      },
      {
        "factor": "sum_failed_transactions_30d_6m",
        "value": 11.0,
        "message": "Customer has recent failed transactions.",
        "contribution": 0.17818380892276764
      },
      {
        "factor": "latest_failed_transactions_30d",
        "value": 7,
        "message": "Customer has recent failed transactions.",
        "contribution": 0.1775924414396286
      }
    ]
  },
  "model2_input": {
    "customer_context": {
      "age": 34,
      "tenure_months": 43,
      "customer_segment": "farmer",
      "income_regularity": "seasonal",
      "customer_yearly_value": 16052.0473,
      "products_count": 3,
      "has_credit_card": 0,
      "has_loan": 1
    },
    "behavior": {
      "days_since_last_transaction": 0,
      "balance_change_30d": 9.414,
      "transaction_change_30d": 21.8115,
      "card_spend_change_30d": 11.1721,
      "app_login_change_30d": 16.5729,
      "salary_missing_days": null,
      "external_transfer_change_30d": 42.4233,
      "upi_share_of_spend": 0.5099,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "emi_bounce_30d": 0
    },
    "service_evidence": {
      "complaints_30d": 4,
      "unresolved_complaints": 3,
      "failed_transactions_30d": 7,
      "avg_resolution_time_hrs": 99.0341,
      "complaint_text": "Bank walon ne bola system update hai, teen din se yehi sun raha hoon."
    },
    "model1": {
      "churn_probability": 0.2776,
      "churn_prediction": "Yes",
      "risk_level": "High",
      "top_risk_factors": [
        {
          "factor": "max_avg_resolution_time_hrs_3m",
          "value": 99.0341
        },
        {
          "factor": "avg_resolution_time_hrs",
          "value": 99.0341
        },
        {
          "factor": "sum_failed_transactions_30d_3m",
          "value": 11.0
        },
        {
          "factor": "sum_failed_transactions_30d_6m",
          "value": 11.0
        },
        {
          "factor": "failed_transactions_30d",
          "value": 7
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
    "case_id": "C17447"
  },
  "model2": {
    "case_id": "C17447",
    "ok": true,
    "prediction": {
      "evidence": [
        "complaints_30d=4",
        "unresolved_complaints=3",
        "complaint_text mentions fees or charges",
        "avg_resolution_time_hrs=99.0",
        "secondary_reasons=SERVICE_DISSATISFACTION"
      ],
      "primary_reason": "FEE_DISSATISFACTION",
      "reasoning_summary": "Complaint evidence suggests dissatisfaction with fees or charges.",
      "recommended_action": "FEE_WAIVER_REVIEW",
      "secondary_reasons": [
        "SERVICE_DISSATISFACTION"
      ],
      "urgency": "HIGH"
    },
    "raw_text": "{\n  \"evidence\":[\"complaints_30d=4\",\"unresolved_complaints=3\",\"complaint_text mentions fees or charges\",\"avg_resolution_time_hrs=99.0\",\"secondary_reasons=SERVICE_DISSATISFACTION\"],\"primary_reason\":\"FEE_DISSATISFACTION\",\"reasoning_summary\":\"Complaint evidence suggests dissatisfaction with fees or charges.\",\"recommended_action\":\"FEE_WAIVER_REVIEW\",\"secondary_reasons\":[\"SERVICE_DISSATISFACTION\"],\"urgency\":\"HIGH\"}",
    "error": null,
    "latency_s": 2.1007,
    "simple_output": "Reason: FEE_DISSATISFACTION | Urgency: HIGH | Action: FEE_WAIVER_REVIEW | Why: Complaint evidence suggests dissatisfaction with fees or charges."
  }
}
```

### Aishani Vala (`C17772`)

- OK: `True`
- Shape errors: `[]`
- Simple output: Reason: SERVICE_DISSATISFACTION | Urgency: HIGH | Action: SERVICE_RECOVERY | Why: Complaint and resolution data suggest a real service friction without a clear escalation-level problem.

Request:

```json
{
  "customer_id": "C17772",
  "customer_name": "Aishani Vala",
  "prediction_date": "2026-02-01",
  "snapshot_date": "2026-02-01",
  "target_month": "2026-03-01",
  "profile": {
    "tenure_months": 167,
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
      "balance_change_30d": -0.9979,
      "transaction_change_30d": -16.2402,
      "card_spend_change_30d": -23.5925,
      "app_login_change_30d": 15.317,
      "salary_missing_days": 2.0,
      "external_transfer_change_30d": 3.6645,
      "upi_share_of_spend": 0.4665,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 1,
      "failed_transactions_30d": 2,
      "avg_resolution_time_hrs": 37.8131,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-02-01",
      "days_since_last_transaction": 1,
      "balance_change_30d": 0.1435,
      "transaction_change_30d": -18.484,
      "card_spend_change_30d": -0.0536,
      "app_login_change_30d": -5.2681,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": 28.8843,
      "upi_share_of_spend": 0.3337,
      "fd_maturing_in_30d": 1,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 2,
      "avg_resolution_time_hrs": 33.217,
      "emi_bounce_30d": 0
    }
  ],
  "customer": {
    "tenure_months": 167,
    "customer_segment": "pension",
    "income_regularity": "regular",
    "products_count": 1,
    "has_credit_card": 0,
    "has_loan": 0,
    "days_since_last_transaction": 1,
    "balance_change_30d": 0.1435,
    "transaction_change_30d": -18.484,
    "card_spend_change_30d": -0.0536,
    "app_login_change_30d": -5.2681,
    "salary_missing_days": 0.0,
    "external_transfer_change_30d": 28.8843,
    "upi_share_of_spend": 0.3337,
    "fd_maturing_in_30d": 1,
    "products_dropped_90d": 0,
    "complaints_30d": 1,
    "unresolved_complaints": 0,
    "failed_transactions_30d": 2,
    "avg_resolution_time_hrs": 33.217,
    "emi_bounce_30d": 0
  },
  "extra_context": {
    "customer_profile": {
      "segment": "pension",
      "income_regularity": "regular",
      "tenure_months": 167,
      "age": 79,
      "customer_yearly_value": 9718.6471,
      "products_count": 1,
      "has_credit_card": 0,
      "has_loan": 0,
      "value_tier": "low"
    },
    "recent_complaint_text": "I have banked here 20 years and today I was treated like a stranger."
  }
}
```

Response:

```json
{
  "meta": {
    "endpoint": "/predict/both",
    "served_at": "2026-08-31T00:56:55",
    "elapsed_ms": 2103.74,
    "timings_ms": {
      "model1": 88.0,
      "model2": 2015.63
    },
    "customer_id": "C17772",
    "customer_name": "Aishani Vala",
    "snapshot_date": "2026-02-01"
  },
  "model1": {
    "churn_probability": 3.53,
    "raw_churn_probability": 30.98,
    "probability_mode": "sigmoid",
    "risk_score": 10.59,
    "churn_prediction": "No",
    "risk_level": "Low",
    "top_risk_factors": [
      {
        "factor": "latest_avg_resolution_time_hrs",
        "value": 33.217,
        "message": "Recent complaints took longer to resolve.",
        "contribution": 0.2437105029821396
      },
      {
        "factor": "latest_fd_maturing_in_30d",
        "value": 1,
        "message": "Customer has a fixed deposit maturing soon.",
        "contribution": 0.14606881141662598
      },
      {
        "factor": "sum_fd_maturing_in_30d_3m",
        "value": 1.0,
        "message": "Customer has a fixed deposit maturing soon.",
        "contribution": 0.07387875765562057
      },
      {
        "factor": "external_transfer_change_30d_trend_6m",
        "value": 25.219799999999992,
        "message": "External transfers have increased.",
        "contribution": 0.06737423688173294
      },
      {
        "factor": "latest_transaction_change_30d",
        "value": -18.484,
        "message": "Transaction activity has been falling across recent months.",
        "contribution": 0.052640657871961594
      }
    ]
  },
  "model2_input": {
    "customer_context": {
      "age": 79,
      "tenure_months": 167,
      "customer_segment": "pension",
      "income_regularity": "regular",
      "customer_yearly_value": 9718.6471,
      "products_count": 1,
      "has_credit_card": 0,
      "has_loan": 0
    },
    "behavior": {
      "days_since_last_transaction": 1,
      "balance_change_30d": 0.1435,
      "transaction_change_30d": -18.484,
      "card_spend_change_30d": -0.0536,
      "app_login_change_30d": -5.2681,
      "salary_missing_days": 0,
      "external_transfer_change_30d": 28.8843,
      "upi_share_of_spend": 0.3337,
      "fd_maturing_in_30d": 1,
      "products_dropped_90d": 0,
      "emi_bounce_30d": 0
    },
    "service_evidence": {
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 2,
      "avg_resolution_time_hrs": 33.217,
      "complaint_text": "I have banked here 20 years and today I was treated like a stranger."
    },
    "model1": {
      "churn_probability": 0.0353,
      "churn_prediction": "No",
      "risk_level": "Low",
      "top_risk_factors": [
        {
          "factor": "avg_resolution_time_hrs",
          "value": 33.217
        },
        {
          "factor": "fd_maturing_in_30d",
          "value": 1
        },
        {
          "factor": "sum_fd_maturing_in_30d_3m",
          "value": 1.0
        },
        {
          "factor": "external_transfer_change_30d_trend_6m",
          "value": 25.219799999999992
        },
        {
          "factor": "transaction_change_30d",
          "value": -18.484
        }
      ]
    },
    "eligible_actions": [
      "MONITOR",
      "RE_ENGAGEMENT",
      "PRODUCT_REVIEW",
      "SERVICE_RECOVERY"
    ],
    "case_id": "C17772"
  },
  "model2": {
    "case_id": "C17772",
    "ok": true,
    "prediction": {
      "evidence": [
        "complaints_30d=1",
        "unresolved_complaints=0",
        "avg_resolution_time_hrs=33.2",
        "complaint_text describes a recent service issue"
      ],
      "primary_reason": "SERVICE_DISSATISFACTION",
      "reasoning_summary": "Complaint and resolution data suggest a real service friction without a clear escalation-level problem.",
      "recommended_action": "SERVICE_RECOVERY",
      "secondary_reasons": [
        "DIGITAL_FRICTION"
      ],
      "urgency": "HIGH"
    },
    "raw_text": "{\n  \"evidence\":[\"complaints_30d=1\",\"unresolved_complaints=0\",\"avg_resolution_time_hrs=33.2\",\"complaint_text describes a recent service issue\"],\"primary_reason\":\"SERVICE_DISSATISFACTION\",\"reasoning_summary\":\"Complaint and resolution data suggest a real service friction without a clear escalation-level problem.\",\"recommended_action\":\"SERVICE_RECOVERY\",\"secondary_reasons\":[\"DIGITAL_FRICTION\"],\"urgency\":\"HIGH\"}",
    "error": null,
    "latency_s": 2.0154,
    "simple_output": "Reason: SERVICE_DISSATISFACTION | Urgency: HIGH | Action: SERVICE_RECOVERY | Why: Complaint and resolution data suggest a real service friction without a clear escalation-level problem."
  }
}
```

### Amrita Bansal (`C18515`)

- OK: `False`
- Shape errors: `["model2 returned ok=false: recommended_action: 'FINANCIAL_GUIDANCE' not in eligible_actions ['MONITOR', 'RE_ENGAGEMENT', 'PRODUCT_REVIEW']", 'model2.prediction is missing or not an object']`
- Simple output: Prediction failed: recommended_action: 'FINANCIAL_GUIDANCE' not in eligible_actions ['MONITOR', 'RE_ENGAGEMENT', 'PRODUCT_REVIEW']

Request:

```json
{
  "customer_id": "C18515",
  "customer_name": "Amrita Bansal",
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
      "balance_change_30d": -16.304,
      "transaction_change_30d": -13.82,
      "card_spend_change_30d": -32.0365,
      "app_login_change_30d": -29.6807,
      "salary_missing_days": null,
      "external_transfer_change_30d": 61.6498,
      "upi_share_of_spend": 0.3405,
      "fd_maturing_in_30d": 1,
      "products_dropped_90d": 1,
      "complaints_30d": 0,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 2,
      "avg_resolution_time_hrs": 0.0,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-02-01",
      "days_since_last_transaction": 5,
      "balance_change_30d": -19.3925,
      "transaction_change_30d": 11.7215,
      "card_spend_change_30d": 20.3294,
      "app_login_change_30d": 32.8466,
      "salary_missing_days": null,
      "external_transfer_change_30d": -31.7708,
      "upi_share_of_spend": 0.2271,
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
      "balance_change_30d": 46.5342,
      "transaction_change_30d": 27.4274,
      "card_spend_change_30d": 34.8688,
      "app_login_change_30d": 40.9851,
      "salary_missing_days": null,
      "external_transfer_change_30d": -23.3598,
      "upi_share_of_spend": 0.2412,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 2,
      "unresolved_complaints": 1,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 43.6711,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-04-01",
      "days_since_last_transaction": 3,
      "balance_change_30d": 14.5684,
      "transaction_change_30d": 10.0772,
      "card_spend_change_30d": -26.5912,
      "app_login_change_30d": -6.1868,
      "salary_missing_days": null,
      "external_transfer_change_30d": 9.771,
      "upi_share_of_spend": 0.2461,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 31.6902,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-05-01",
      "days_since_last_transaction": 0,
      "balance_change_30d": 1.3286,
      "transaction_change_30d": 29.6953,
      "card_spend_change_30d": 15.2524,
      "app_login_change_30d": 10.0702,
      "salary_missing_days": null,
      "external_transfer_change_30d": 1.8108,
      "upi_share_of_spend": 0.2,
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
      "balance_change_30d": 1.4728,
      "transaction_change_30d": 12.3671,
      "card_spend_change_30d": 16.9737,
      "app_login_change_30d": 33.141,
      "salary_missing_days": null,
      "external_transfer_change_30d": -43.3899,
      "upi_share_of_spend": 0.1846,
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
    "tenure_months": 80,
    "customer_segment": "farmer",
    "income_regularity": "seasonal",
    "products_count": 2,
    "has_credit_card": 0,
    "has_loan": 1,
    "days_since_last_transaction": 2,
    "balance_change_30d": 1.4728,
    "transaction_change_30d": 12.3671,
    "card_spend_change_30d": 16.9737,
    "app_login_change_30d": 33.141,
    "salary_missing_days": null,
    "external_transfer_change_30d": -43.3899,
    "upi_share_of_spend": 0.1846,
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
      "tenure_months": 80,
      "age": 49,
      "customer_yearly_value": 13104.4138,
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
    "served_at": "2026-08-31T00:57:01",
    "elapsed_ms": 5462.7,
    "timings_ms": {
      "model1": 95.27,
      "model2": 5367.29
    },
    "customer_id": "C18515",
    "customer_name": "Amrita Bansal",
    "snapshot_date": "2026-06-01"
  },
  "model1": {
    "churn_probability": 2.04,
    "raw_churn_probability": 18.91,
    "probability_mode": "sigmoid",
    "risk_score": 6.13,
    "churn_prediction": "No",
    "risk_level": "Low",
    "top_risk_factors": [
      {
        "factor": "latest_external_transfer_change_30d",
        "value": -43.3899,
        "message": "This signal increased churn risk.",
        "contribution": 0.05822226405143738
      },
      {
        "factor": "latest_vs_avg_external_transfer_change_30d_available_history",
        "value": -39.17508333333333,
        "message": "This signal increased churn risk.",
        "contribution": 0.05253124237060547
      },
      {
        "factor": "avg_upi_share_of_spend_6m",
        "value": 0.23991666666666664,
        "message": "A larger share of spending is happening through UPI.",
        "contribution": 0.03221657872200012
      },
      {
        "factor": "avg_transaction_change_30d_6m",
        "value": 12.911416666666668,
        "message": "This signal increased churn risk.",
        "contribution": 0.020737437531352043
      },
      {
        "factor": "count_balance_drop_3m",
        "value": 0,
        "message": "This signal increased churn risk.",
        "contribution": 0.007458306383341551
      }
    ]
  },
  "model2_input": {
    "customer_context": {
      "age": 49,
      "tenure_months": 80,
      "customer_segment": "farmer",
      "income_regularity": "seasonal",
      "customer_yearly_value": 13104.4138,
      "products_count": 2,
      "has_credit_card": 0,
      "has_loan": 1
    },
    "behavior": {
      "days_since_last_transaction": 2,
      "balance_change_30d": 1.4728,
      "transaction_change_30d": 12.3671,
      "card_spend_change_30d": 16.9737,
      "app_login_change_30d": 33.141,
      "salary_missing_days": null,
      "external_transfer_change_30d": -43.3899,
      "upi_share_of_spend": 0.1846,
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
      "churn_probability": 0.0204,
      "churn_prediction": "No",
      "risk_level": "Low",
      "top_risk_factors": [
        {
          "factor": "external_transfer_change_30d",
          "value": -43.3899
        },
        {
          "factor": "vs_avg_external_transfer_change_30d_available_history",
          "value": -39.17508333333333
        },
        {
          "factor": "avg_upi_share_of_spend_6m",
          "value": 0.23991666666666664
        },
        {
          "factor": "avg_transaction_change_30d_6m",
          "value": 12.911416666666668
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
    "case_id": "C18515"
  },
  "model2": {
    "case_id": "C18515",
    "ok": false,
    "prediction": null,
    "raw_text": "{\n  \"evidence\": [\n    \"balance_change_30d=1.47\",\n    \"external_transfer_change_30d=-43.40\",\n    \"transaction_change_30d=12.37\"\n  ],\n  \"primary_reason\": \"FINANCIAL_STRESS\",\n  \"reasoning_summary\": \"Evidence suggests this because balance_change_30d=1.5 and external_transfer_change_30d=-43.4 suggest a financial stress situation without a stronger cause.\",\n  \"recommended_action\": \"FINANCIAL_GUIDANCE\",\n  \"secondary_reasons\": [\n    \"SERVICE_DISSATISFACTION\"\n  ],\n  \"urgency\": \"HIGH\"\n}",
    "error": "recommended_action: 'FINANCIAL_GUIDANCE' not in eligible_actions ['MONITOR', 'RE_ENGAGEMENT', 'PRODUCT_REVIEW']",
    "latency_s": 5.3671,
    "simple_output": "Prediction failed: recommended_action: 'FINANCIAL_GUIDANCE' not in eligible_actions ['MONITOR', 'RE_ENGAGEMENT', 'PRODUCT_REVIEW']"
  }
}
```

### Niharika Parekh (`C18846`)

- OK: `True`
- Shape errors: `[]`
- Simple output: Reason: SERVICE_DISSATISFACTION | Urgency: HIGH | Action: SERVICE_RECOVERY | Why: Complaint and transaction evidence suggests a product-fit or service friction issue without clear escalation-level problem-solving scope.

Request:

```json
{
  "customer_id": "C18846",
  "customer_name": "Niharika Parekh",
  "prediction_date": "2026-06-01",
  "snapshot_date": "2026-06-01",
  "target_month": "2026-07-01",
  "profile": {
    "tenure_months": 114,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 2,
    "has_credit_card": 0,
    "has_loan": 1
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 6,
      "balance_change_30d": 2.5314,
      "transaction_change_30d": -9.8909,
      "card_spend_change_30d": 1.8255,
      "app_login_change_30d": 1.5947,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -9.7617,
      "upi_share_of_spend": 0.6407,
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
      "balance_change_30d": 24.4289,
      "transaction_change_30d": 39.8102,
      "card_spend_change_30d": 36.3097,
      "app_login_change_30d": 33.665,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -62.1133,
      "upi_share_of_spend": 0.5386,
      "fd_maturing_in_30d": 1,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 1,
      "failed_transactions_30d": 5,
      "avg_resolution_time_hrs": 31.9774,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-03-01",
      "days_since_last_transaction": 0,
      "balance_change_30d": 49.0868,
      "transaction_change_30d": 15.7305,
      "card_spend_change_30d": 51.3576,
      "app_login_change_30d": 17.3758,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -19.9339,
      "upi_share_of_spend": 0.5315,
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
      "balance_change_30d": 38.7814,
      "transaction_change_30d": 30.913,
      "card_spend_change_30d": 29.058,
      "app_login_change_30d": 52.5991,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -47.8358,
      "upi_share_of_spend": 0.5086,
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
      "balance_change_30d": 58.8621,
      "transaction_change_30d": 34.4906,
      "card_spend_change_30d": 59.1909,
      "app_login_change_30d": 44.915,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -39.9516,
      "upi_share_of_spend": 0.5822,
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
      "days_since_last_transaction": 0,
      "balance_change_30d": 32.8784,
      "transaction_change_30d": 40.6433,
      "card_spend_change_30d": 51.7551,
      "app_login_change_30d": 63.8028,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -100.0,
      "upi_share_of_spend": 0.478,
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
    "tenure_months": 114,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 2,
    "has_credit_card": 0,
    "has_loan": 1,
    "days_since_last_transaction": 0,
    "balance_change_30d": 32.8784,
    "transaction_change_30d": 40.6433,
    "card_spend_change_30d": 51.7551,
    "app_login_change_30d": 63.8028,
    "salary_missing_days": 0.0,
    "external_transfer_change_30d": -100.0,
    "upi_share_of_spend": 0.478,
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
      "tenure_months": 114,
      "age": 47,
      "customer_yearly_value": 47018.3205,
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
    "served_at": "2026-08-31T00:57:04",
    "elapsed_ms": 3064.0,
    "timings_ms": {
      "model1": 114.21,
      "model2": 2949.65
    },
    "customer_id": "C18846",
    "customer_name": "Niharika Parekh",
    "snapshot_date": "2026-06-01"
  },
  "model1": {
    "churn_probability": 1.53,
    "raw_churn_probability": 12.6,
    "probability_mode": "sigmoid",
    "risk_score": 4.6,
    "churn_prediction": "No",
    "risk_level": "Low",
    "top_risk_factors": [
      {
        "factor": "latest_vs_avg_external_transfer_change_30d_available_history",
        "value": -53.40061666666667,
        "message": "This signal increased churn risk.",
        "contribution": 0.1484098881483078
      },
      {
        "factor": "sum_failed_transactions_30d_6m",
        "value": 9.0,
        "message": "Customer has recent failed transactions.",
        "contribution": 0.10820788145065308
      },
      {
        "factor": "avg_app_login_change_30d_6m",
        "value": 35.65873333333333,
        "message": "This signal increased churn risk.",
        "contribution": 0.08639863133430481
      },
      {
        "factor": "avg_balance_change_30d_6m",
        "value": 34.42816666666666,
        "message": "This signal increased churn risk.",
        "contribution": 0.08578422665596008
      },
      {
        "factor": "sum_fd_maturing_in_30d_3m",
        "value": 1.0,
        "message": "Customer has a fixed deposit maturing soon.",
        "contribution": 0.06542368978261948
      }
    ]
  },
  "model2_input": {
    "customer_context": {
      "age": 47,
      "tenure_months": 114,
      "customer_segment": "salary",
      "income_regularity": "regular",
      "customer_yearly_value": 47018.3205,
      "products_count": 2,
      "has_credit_card": 0,
      "has_loan": 1
    },
    "behavior": {
      "days_since_last_transaction": 0,
      "balance_change_30d": 32.8784,
      "transaction_change_30d": 40.6433,
      "card_spend_change_30d": 51.7551,
      "app_login_change_30d": 63.8028,
      "salary_missing_days": 0,
      "external_transfer_change_30d": -100.0,
      "upi_share_of_spend": 0.478,
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
      "churn_probability": 0.0153,
      "churn_prediction": "No",
      "risk_level": "Low",
      "top_risk_factors": [
        {
          "factor": "vs_avg_external_transfer_change_30d_available_history",
          "value": -53.40061666666667
        },
        {
          "factor": "sum_failed_transactions_30d_6m",
          "value": 9.0
        },
        {
          "factor": "avg_app_login_change_30d_6m",
          "value": 35.65873333333333
        },
        {
          "factor": "avg_balance_change_30d_6m",
          "value": 34.42816666666666
        },
        {
          "factor": "sum_fd_maturing_in_30d_3m",
          "value": 1.0
        }
      ]
    },
    "eligible_actions": [
      "MONITOR",
      "RE_ENGAGEMENT",
      "PRODUCT_REVIEW",
      "SERVICE_RECOVERY"
    ],
    "case_id": "C18846"
  },
  "model2": {
    "case_id": "C18846",
    "ok": true,
    "prediction": {
      "evidence": [
        "complaints_30d=0",
        "unresolved_complaints=0",
        "app_login_change_30d=63.8",
        "balance_change_30d=32.9",
        "transaction_change_30d=40.6",
        "failed_transactions_30d=1",
        "complaint_text does not mention a product or service",
        "complaint_text does not mention fees or charges"
      ],
      "primary_reason": "SERVICE_DISSATISFACTION",
      "reasoning_summary": "Complaint and transaction evidence suggests a product-fit or service friction issue without clear escalation-level problem-solving scope.",
      "recommended_action": "SERVICE_RECOVERY",
      "secondary_reasons": [
        "DIGITAL_FRICTION"
      ],
      "urgency": "HIGH"
    },
    "raw_text": "{\n  \"evidence\":[\"complaints_30d=0\",\"unresolved_complaints=0\",\"app_login_change_30d=63.8\",\"balance_change_30d=32.9\",\"transaction_change_30d=40.6\",\"failed_transactions_30d=1\",\"complaint_text does not mention a product or service\",\"complaint_text does not mention fees or charges\"],\"primary_reason\":\"SERVICE_DISSATISFACTION\",\"reasoning_summary\":\"Complaint and transaction evidence suggests a product-fit or service friction issue without clear escalation-level problem-solving scope.\",\"recommended_action\":\"SERVICE_RECOVERY\",\"secondary_reasons\":[\"DIGITAL_FRICTION\"],\"urgency\":\"HIGH\"}",
    "error": null,
    "latency_s": 2.9495,
    "simple_output": "Reason: SERVICE_DISSATISFACTION | Urgency: HIGH | Action: SERVICE_RECOVERY | Why: Complaint and transaction evidence suggests a product-fit or service friction issue without clear escalation-level problem-solving scope."
  }
}
```

### Vamakshi Kulkarni (`C19250`)

- OK: `True`
- Shape errors: `[]`
- Simple output: Reason: SERVICE_DISSATISFACTION | Urgency: HIGH | Action: SERVICE_RECOVERY | Why: Complaint and resolution evidence suggests a service problem without a clear product mismatch.

Request:

```json
{
  "customer_id": "C19250",
  "customer_name": "Vamakshi Kulkarni",
  "prediction_date": "2026-06-01",
  "snapshot_date": "2026-06-01",
  "target_month": "2026-07-01",
  "profile": {
    "tenure_months": 1,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 3,
    "has_credit_card": 1,
    "has_loan": 0
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 5,
      "balance_change_30d": -4.3843,
      "transaction_change_30d": -11.2376,
      "card_spend_change_30d": -10.6619,
      "app_login_change_30d": 2.7334,
      "salary_missing_days": 1.0,
      "external_transfer_change_30d": 35.5569,
      "upi_share_of_spend": 0.4818,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 13.006,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-02-01",
      "days_since_last_transaction": 3,
      "balance_change_30d": -1.5426,
      "transaction_change_30d": -2.5338,
      "card_spend_change_30d": -2.5356,
      "app_login_change_30d": 17.8402,
      "salary_missing_days": 2.0,
      "external_transfer_change_30d": -52.2551,
      "upi_share_of_spend": 0.4315,
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
      "balance_change_30d": 19.0124,
      "transaction_change_30d": 11.9753,
      "card_spend_change_30d": 7.3623,
      "app_login_change_30d": -2.2732,
      "salary_missing_days": 2.0,
      "external_transfer_change_30d": 0.4405,
      "upi_share_of_spend": 0.52,
      "fd_maturing_in_30d": 1,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 1,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 21.8849,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-04-01",
      "days_since_last_transaction": 1,
      "balance_change_30d": 11.9439,
      "transaction_change_30d": 11.4911,
      "card_spend_change_30d": 18.3256,
      "app_login_change_30d": -18.7757,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -82.0018,
      "upi_share_of_spend": 0.4694,
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
      "balance_change_30d": 36.8602,
      "transaction_change_30d": -7.5534,
      "card_spend_change_30d": 0.086,
      "app_login_change_30d": 12.1393,
      "salary_missing_days": 2.0,
      "external_transfer_change_30d": 1.2101,
      "upi_share_of_spend": 0.5027,
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
      "balance_change_30d": 7.6811,
      "transaction_change_30d": 4.6252,
      "card_spend_change_30d": -23.0338,
      "app_login_change_30d": -0.9909,
      "salary_missing_days": 2.0,
      "external_transfer_change_30d": 26.2625,
      "upi_share_of_spend": 0.5207,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 1,
      "failed_transactions_30d": 2,
      "avg_resolution_time_hrs": 40.8072,
      "emi_bounce_30d": 0
    }
  ],
  "customer": {
    "tenure_months": 1,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 3,
    "has_credit_card": 1,
    "has_loan": 0,
    "days_since_last_transaction": 7,
    "balance_change_30d": 7.6811,
    "transaction_change_30d": 4.6252,
    "card_spend_change_30d": -23.0338,
    "app_login_change_30d": -0.9909,
    "salary_missing_days": 2.0,
    "external_transfer_change_30d": 26.2625,
    "upi_share_of_spend": 0.5207,
    "fd_maturing_in_30d": 0,
    "products_dropped_90d": 0,
    "complaints_30d": 1,
    "unresolved_complaints": 1,
    "failed_transactions_30d": 2,
    "avg_resolution_time_hrs": 40.8072,
    "emi_bounce_30d": 0
  },
  "extra_context": {
    "customer_profile": {
      "segment": "salary",
      "income_regularity": "regular",
      "tenure_months": 1,
      "age": 28,
      "customer_yearly_value": 67725.757,
      "products_count": 3,
      "has_credit_card": 1,
      "has_loan": 0,
      "value_tier": "medium"
    },
    "recent_complaint_text": "Staff told me to come after 3 pm and then said system is down."
  }
}
```

Response:

```json
{
  "meta": {
    "endpoint": "/predict/both",
    "served_at": "2026-08-31T00:57:06",
    "elapsed_ms": 2067.47,
    "timings_ms": {
      "model1": 60.92,
      "model2": 2006.43
    },
    "customer_id": "C19250",
    "customer_name": "Vamakshi Kulkarni",
    "snapshot_date": "2026-06-01"
  },
  "model1": {
    "churn_probability": 6.99,
    "raw_churn_probability": 46.44,
    "probability_mode": "sigmoid",
    "risk_score": 20.98,
    "churn_prediction": "No",
    "risk_level": "Low",
    "top_risk_factors": [
      {
        "factor": "latest_avg_resolution_time_hrs",
        "value": 40.8072,
        "message": "Recent complaints took longer to resolve.",
        "contribution": 0.3371247351169586
      },
      {
        "factor": "latest_vs_avg_upi_share_of_spend_available_history",
        "value": 0.03301666666666664,
        "message": "A larger share of spending is happening through UPI.",
        "contribution": 0.08003614097833633
      },
      {
        "factor": "sum_failed_transactions_30d_3m",
        "value": 4.0,
        "message": "Customer has recent failed transactions.",
        "contribution": 0.044883619993925095
      },
      {
        "factor": "latest_salary_missing_days",
        "value": 2.0,
        "message": "Salary or pension was delayed recently.",
        "contribution": 0.04439915344119072
      },
      {
        "factor": "latest_card_spend_change_30d",
        "value": -23.0338,
        "message": "Card spending has been falling across recent months.",
        "contribution": 0.029725603759288788
      }
    ]
  },
  "model2_input": {
    "customer_context": {
      "age": 28,
      "tenure_months": 1,
      "customer_segment": "salary",
      "income_regularity": "regular",
      "customer_yearly_value": 67725.757,
      "products_count": 3,
      "has_credit_card": 1,
      "has_loan": 0
    },
    "behavior": {
      "days_since_last_transaction": 7,
      "balance_change_30d": 7.6811,
      "transaction_change_30d": 4.6252,
      "card_spend_change_30d": -23.0338,
      "app_login_change_30d": -0.9909,
      "salary_missing_days": 2,
      "external_transfer_change_30d": 26.2625,
      "upi_share_of_spend": 0.5207,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "emi_bounce_30d": 0
    },
    "service_evidence": {
      "complaints_30d": 1,
      "unresolved_complaints": 1,
      "failed_transactions_30d": 2,
      "avg_resolution_time_hrs": 40.8072,
      "complaint_text": "Staff told me to come after 3 pm and then said system is down."
    },
    "model1": {
      "churn_probability": 0.0699,
      "churn_prediction": "No",
      "risk_level": "Low",
      "top_risk_factors": [
        {
          "factor": "avg_resolution_time_hrs",
          "value": 40.8072
        },
        {
          "factor": "vs_avg_upi_share_of_spend_available_history",
          "value": 0.03301666666666664
        },
        {
          "factor": "sum_failed_transactions_30d_3m",
          "value": 4.0
        },
        {
          "factor": "salary_missing_days",
          "value": 2.0
        },
        {
          "factor": "card_spend_change_30d",
          "value": -23.0338
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
    "case_id": "C19250"
  },
  "model2": {
    "case_id": "C19250",
    "ok": true,
    "prediction": {
      "evidence": [
        "complaints_30d=1",
        "unresolved_complaints=1",
        "complaint_text mentions a service issue",
        "avg_resolution_time_hrs=40.8",
        "complaint_text mentions failed transactions"
      ],
      "primary_reason": "SERVICE_DISSATISFACTION",
      "reasoning_summary": "Complaint and resolution evidence suggests a service problem without a clear product mismatch.",
      "recommended_action": "SERVICE_RECOVERY",
      "secondary_reasons": [
        "DIGITAL_FRICTION"
      ],
      "urgency": "HIGH"
    },
    "raw_text": "{\n\"evidence\":[\"complaints_30d=1\",\"unresolved_complaints=1\",\"complaint_text mentions a service issue\",\"avg_resolution_time_hrs=40.8\",\"complaint_text mentions failed transactions\"],\"primary_reason\":\"SERVICE_DISSATISFACTION\",\"reasoning_summary\":\"Complaint and resolution evidence suggests a service problem without a clear product mismatch.\",\"recommended_action\":\"SERVICE_RECOVERY\",\"secondary_reasons\":[\"DIGITAL_FRICTION\"],\"urgency\":\"HIGH\"}",
    "error": null,
    "latency_s": 2.0062,
    "simple_output": "Reason: SERVICE_DISSATISFACTION | Urgency: HIGH | Action: SERVICE_RECOVERY | Why: Complaint and resolution evidence suggests a service problem without a clear product mismatch."
  }
}
```

### Reva Kadakia (`C19323`)

- OK: `True`
- Shape errors: `[]`
- Simple output: Reason: DIGITAL_FRICTION | Urgency: HIGH | Action: COMPLAINT_ESCALATION | Why: Digital-service friction is the most supported explanation for the issue signal seen in this case. Complaint escalation fits because complaints_30d=2 and failed_transactions_30d=1 point to a real problem.

Request:

```json
{
  "customer_id": "C19323",
  "customer_name": "Reva Kadakia",
  "prediction_date": "2026-02-01",
  "snapshot_date": "2026-02-01",
  "target_month": "2026-03-01",
  "profile": {
    "tenure_months": 29,
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
      "balance_change_30d": -0.9225,
      "transaction_change_30d": 16.2413,
      "card_spend_change_30d": 14.831,
      "app_login_change_30d": -1.8,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": 9.3294,
      "upi_share_of_spend": 0.5213,
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
      "days_since_last_transaction": 17,
      "balance_change_30d": 10.56,
      "transaction_change_30d": -1.3796,
      "card_spend_change_30d": -25.2373,
      "app_login_change_30d": -2.7111,
      "salary_missing_days": 4.0,
      "external_transfer_change_30d": 8.4267,
      "upi_share_of_spend": 0.5293,
      "fd_maturing_in_30d": 1,
      "products_dropped_90d": 0,
      "complaints_30d": 2,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 22.219,
      "emi_bounce_30d": 0
    }
  ],
  "customer": {
    "tenure_months": 29,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 2,
    "has_credit_card": 1,
    "has_loan": 0,
    "days_since_last_transaction": 17,
    "balance_change_30d": 10.56,
    "transaction_change_30d": -1.3796,
    "card_spend_change_30d": -25.2373,
    "app_login_change_30d": -2.7111,
    "salary_missing_days": 4.0,
    "external_transfer_change_30d": 8.4267,
    "upi_share_of_spend": 0.5293,
    "fd_maturing_in_30d": 1,
    "products_dropped_90d": 0,
    "complaints_30d": 2,
    "unresolved_complaints": 0,
    "failed_transactions_30d": 1,
    "avg_resolution_time_hrs": 22.219,
    "emi_bounce_30d": 0
  },
  "extra_context": {
    "customer_profile": {
      "segment": "salary",
      "income_regularity": "regular",
      "tenure_months": 29,
      "age": 27,
      "customer_yearly_value": 40812.4068,
      "products_count": 2,
      "has_credit_card": 1,
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
    "served_at": "2026-08-31T00:57:09",
    "elapsed_ms": 2602.78,
    "timings_ms": {
      "model1": 82.7,
      "model2": 2519.97
    },
    "customer_id": "C19323",
    "customer_name": "Reva Kadakia",
    "snapshot_date": "2026-02-01"
  },
  "model1": {
    "churn_probability": 15.05,
    "raw_churn_probability": 64.84,
    "probability_mode": "sigmoid",
    "risk_score": 50.18,
    "churn_prediction": "No",
    "risk_level": "Medium",
    "top_risk_factors": [
      {
        "factor": "latest_days_since_last_transaction",
        "value": 17,
        "message": "Customer has gone longer without transacting.",
        "contribution": 0.4725840091705322
      },
      {
        "factor": "latest_salary_missing_days",
        "value": 4.0,
        "message": "Salary or pension was delayed recently.",
        "contribution": 0.2551282048225403
      },
      {
        "factor": "transaction_change_30d_trend_6m",
        "value": -17.6209,
        "message": "Transaction activity has been falling across recent months.",
        "contribution": 0.15539735555648804
      },
      {
        "factor": "latest_fd_maturing_in_30d",
        "value": 1,
        "message": "Customer has a fixed deposit maturing soon.",
        "contribution": 0.09723731130361557
      },
      {
        "factor": "sum_fd_maturing_in_30d_3m",
        "value": 1.0,
        "message": "Customer has a fixed deposit maturing soon.",
        "contribution": 0.05338093638420105
      }
    ]
  },
  "model2_input": {
    "customer_context": {
      "age": 27,
      "tenure_months": 29,
      "customer_segment": "salary",
      "income_regularity": "regular",
      "customer_yearly_value": 40812.4068,
      "products_count": 2,
      "has_credit_card": 1,
      "has_loan": 0
    },
    "behavior": {
      "days_since_last_transaction": 17,
      "balance_change_30d": 10.56,
      "transaction_change_30d": -1.3796,
      "card_spend_change_30d": -25.2373,
      "app_login_change_30d": -2.7111,
      "salary_missing_days": 4,
      "external_transfer_change_30d": 8.4267,
      "upi_share_of_spend": 0.5293,
      "fd_maturing_in_30d": 1,
      "products_dropped_90d": 0,
      "emi_bounce_30d": 0
    },
    "service_evidence": {
      "complaints_30d": 2,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 22.219,
      "complaint_text": "Kindly activate my card for online transactions, it keeps declining."
    },
    "model1": {
      "churn_probability": 0.1505,
      "churn_prediction": "No",
      "risk_level": "Medium",
      "top_risk_factors": [
        {
          "factor": "days_since_last_transaction",
          "value": 17
        },
        {
          "factor": "salary_missing_days",
          "value": 4.0
        },
        {
          "factor": "transaction_change_30d_trend_6m",
          "value": -17.6209
        },
        {
          "factor": "fd_maturing_in_30d",
          "value": 1
        },
        {
          "factor": "sum_fd_maturing_in_30d_3m",
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
    "case_id": "C19323"
  },
  "model2": {
    "case_id": "C19323",
    "ok": true,
    "prediction": {
      "evidence": [
        "complaints_30d=2",
        "failed_transactions_30d=1",
        "avg_resolution_time_hrs=22.2",
        "complaint_text mentions failed transactions or digital friction"
      ],
      "primary_reason": "DIGITAL_FRICTION",
      "reasoning_summary": "Digital-service friction is the most supported explanation for the issue signal seen in this case. Complaint escalation fits because complaints_30d=2 and failed_transactions_30d=1 point to a real problem.",
      "recommended_action": "COMPLAINT_ESCALATION",
      "secondary_reasons": [
        "SERVICE_DISSATISFACTION"
      ],
      "urgency": "HIGH"
    },
    "raw_text": "{\n  \"evidence\":[\"complaints_30d=2\",\"failed_transactions_30d=1\",\"avg_resolution_time_hrs=22.2\",\"complaint_text mentions failed transactions or digital friction\"],\"primary_reason\":\"DIGITAL_FRICTION\",\"reasoning_summary\":\"Digital-service friction is the most supported explanation for the issue signal seen in this case. Complaint escalation fits because complaints_30d=2 and failed_transactions_30d=1 point to a real problem.\",\"recommended_action\":\"COMPLAINT_ESCALATION\",\"secondary_reasons\":[\"SERVICE_DISSATISFACTION\"],\"urgency\":\"HIGH\"}",
    "error": null,
    "latency_s": 2.5198,
    "simple_output": "Reason: DIGITAL_FRICTION | Urgency: HIGH | Action: COMPLAINT_ESCALATION | Why: Digital-service friction is the most supported explanation for the issue signal seen in this case. Complaint escalation fits because complaints_30d=2 and failed_transactions_30d=1 point to a real problem."
  }
}
```

### Jagrati Chaudhry (`C19353`)

- OK: `True`
- Shape errors: `[]`
- Simple output: Reason: SERVICE_DISSATISFACTION | Urgency: HIGH | Action: SERVICE_RECOVERY | Why: Service friction is the clearest risk signal here, supported by complaints_30d=1 and unresolved_complaints=1 with avg_resolution_time_hrs=24.7 indicating a real service issue.

Request:

```json
{
  "customer_id": "C19353",
  "customer_name": "Jagrati Chaudhry",
  "prediction_date": "2026-06-01",
  "snapshot_date": "2026-06-01",
  "target_month": "2026-07-01",
  "profile": {
    "tenure_months": 36,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 2,
    "has_credit_card": 0,
    "has_loan": 1
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 8,
      "balance_change_30d": 12.6863,
      "transaction_change_30d": 16.9138,
      "card_spend_change_30d": -7.304,
      "app_login_change_30d": 14.4426,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -33.9597,
      "upi_share_of_spend": 0.1096,
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
      "balance_change_30d": 34.6168,
      "transaction_change_30d": 21.7488,
      "card_spend_change_30d": 5.5813,
      "app_login_change_30d": -9.6738,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -29.6914,
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
      "snapshot_date": "2026-03-01",
      "days_since_last_transaction": 4,
      "balance_change_30d": 22.0543,
      "transaction_change_30d": 34.2104,
      "card_spend_change_30d": -5.9764,
      "app_login_change_30d": -2.4633,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -11.822,
      "upi_share_of_spend": 0.0274,
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
      "balance_change_30d": 28.154,
      "transaction_change_30d": 54.3236,
      "card_spend_change_30d": 19.3909,
      "app_login_change_30d": 2.2804,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -11.4283,
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
      "days_since_last_transaction": 0,
      "balance_change_30d": 25.1746,
      "transaction_change_30d": 28.5384,
      "card_spend_change_30d": 47.0431,
      "app_login_change_30d": 39.5401,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -55.6769,
      "upi_share_of_spend": 0.0,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 1,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 22.8942,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-06-01",
      "days_since_last_transaction": 3,
      "balance_change_30d": 33.433,
      "transaction_change_30d": 5.4586,
      "card_spend_change_30d": 16.5241,
      "app_login_change_30d": 39.4398,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -73.9745,
      "upi_share_of_spend": 0.0544,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 1,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 24.6523,
      "emi_bounce_30d": 0
    }
  ],
  "customer": {
    "tenure_months": 36,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 2,
    "has_credit_card": 0,
    "has_loan": 1,
    "days_since_last_transaction": 3,
    "balance_change_30d": 33.433,
    "transaction_change_30d": 5.4586,
    "card_spend_change_30d": 16.5241,
    "app_login_change_30d": 39.4398,
    "salary_missing_days": 0.0,
    "external_transfer_change_30d": -73.9745,
    "upi_share_of_spend": 0.0544,
    "fd_maturing_in_30d": 0,
    "products_dropped_90d": 0,
    "complaints_30d": 1,
    "unresolved_complaints": 1,
    "failed_transactions_30d": 0,
    "avg_resolution_time_hrs": 24.6523,
    "emi_bounce_30d": 0
  },
  "extra_context": {
    "customer_profile": {
      "segment": "salary",
      "income_regularity": "regular",
      "tenure_months": 36,
      "age": 31,
      "customer_yearly_value": 31256.2526,
      "products_count": 2,
      "has_credit_card": 0,
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
    "served_at": "2026-08-31T00:57:11",
    "elapsed_ms": 2472.01,
    "timings_ms": {
      "model1": 76.8,
      "model2": 2395.09
    },
    "customer_id": "C19353",
    "customer_name": "Jagrati Chaudhry",
    "snapshot_date": "2026-06-01"
  },
  "model1": {
    "churn_probability": 2.42,
    "raw_churn_probability": 22.62,
    "probability_mode": "sigmoid",
    "risk_score": 7.26,
    "churn_prediction": "No",
    "risk_level": "Low",
    "top_risk_factors": [
      {
        "factor": "latest_vs_avg_external_transfer_change_30d_available_history",
        "value": -37.88236666666667,
        "message": "This signal increased churn risk.",
        "contribution": 0.10801789909601212
      },
      {
        "factor": "transaction_change_30d_trend_6m",
        "value": -0.4798285714285727,
        "message": "Transaction activity has been falling across recent months.",
        "contribution": 0.05962801352143288
      },
      {
        "factor": "card_spend_change_30d_trend_6m",
        "value": 7.682662857142857,
        "message": "This signal increased churn risk.",
        "contribution": 0.046061962842941284
      },
      {
        "factor": "latest_vs_avg_upi_share_of_spend_available_history",
        "value": 0.022499999999999992,
        "message": "A larger share of spending is happening through UPI.",
        "contribution": 0.0323636494576931
      },
      {
        "factor": "max_salary_missing_days_6m",
        "value": 0.0,
        "message": "This signal increased churn risk.",
        "contribution": 0.02831270545721054
      }
    ]
  },
  "model2_input": {
    "customer_context": {
      "age": 31,
      "tenure_months": 36,
      "customer_segment": "salary",
      "income_regularity": "regular",
      "customer_yearly_value": 31256.2526,
      "products_count": 2,
      "has_credit_card": 0,
      "has_loan": 1
    },
    "behavior": {
      "days_since_last_transaction": 3,
      "balance_change_30d": 33.433,
      "transaction_change_30d": 5.4586,
      "card_spend_change_30d": 16.5241,
      "app_login_change_30d": 39.4398,
      "salary_missing_days": 0,
      "external_transfer_change_30d": -73.9745,
      "upi_share_of_spend": 0.0544,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "emi_bounce_30d": 0
    },
    "service_evidence": {
      "complaints_30d": 1,
      "unresolved_complaints": 1,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 24.6523,
      "complaint_text": "Please confirm whether Saturday banking is available at this branch."
    },
    "model1": {
      "churn_probability": 0.0242,
      "churn_prediction": "No",
      "risk_level": "Low",
      "top_risk_factors": [
        {
          "factor": "vs_avg_external_transfer_change_30d_available_history",
          "value": -37.88236666666667
        },
        {
          "factor": "transaction_change_30d_trend_6m",
          "value": -0.4798285714285727
        },
        {
          "factor": "card_spend_change_30d_trend_6m",
          "value": 7.682662857142857
        },
        {
          "factor": "vs_avg_upi_share_of_spend_available_history",
          "value": 0.022499999999999992
        },
        {
          "factor": "max_salary_missing_days_6m",
          "value": 0.0
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
    "case_id": "C19353"
  },
  "model2": {
    "case_id": "C19353",
    "ok": true,
    "prediction": {
      "evidence": [
        "complaints_30d=1",
        "unresolved_complaints=1",
        "avg_resolution_time_hrs=24.7",
        "complaint_text mentions a service issue"
      ],
      "primary_reason": "SERVICE_DISSATISFACTION",
      "reasoning_summary": "Service friction is the clearest risk signal here, supported by complaints_30d=1 and unresolved_complaints=1 with avg_resolution_time_hrs=24.7 indicating a real service issue.",
      "recommended_action": "SERVICE_RECOVERY",
      "secondary_reasons": [],
      "urgency": "HIGH"
    },
    "raw_text": "{\n  \"evidence\":[\"complaints_30d=1\",\"unresolved_complaints=1\",\"avg_resolution_time_hrs=24.7\",\"complaint_text mentions a service issue\"],\"primary_reason\":\"SERVICE_DISSATISFACTION\",\"reasoning_summary\":\"Service friction is the clearest risk signal here, supported by complaints_30d=1 and unresolved_complaints=1 with avg_resolution_time_hrs=24.7 indicating a real service issue.\",\"recommended_action\":\"SERVICE_RECOVERY\",\"secondary_reasons\":[],\"urgency\":\"HIGH\"}",
    "error": null,
    "latency_s": 2.3948,
    "simple_output": "Reason: SERVICE_DISSATISFACTION | Urgency: HIGH | Action: SERVICE_RECOVERY | Why: Service friction is the clearest risk signal here, supported by complaints_30d=1 and unresolved_complaints=1 with avg_resolution_time_hrs=24.7 indicating a real service issue."
  }
}
```
