# Model 1 vs Model 1 v2 Report

- Created at: `2026-08-30T18:36:29`
- Customers tested: `30`

## Important Note

These models answer different questions, so their metrics are not perfectly apples-to-apples.

- Model 1 predicts current snapshot churn using one monthly row.
- Model 1 v2 predicts next-month churn using history features.

## Metrics

### model_1_current_month

- Question: Is this customer churning in this snapshot?
- Accuracy: `0.9182`
- Precision: `0.3843`
- Recall: `0.5954`
- ROC-AUC: `0.8332`
- PR-AUC: `0.4473`
- Flagged rows: `739`
- Rows evaluated: `7921`
- Positive rows: `477`
- Confusion matrix: `[[6989, 455], [193, 284]]`
- Unique rounded probability values: `66`
- Most common probabilities: `[{'probability_percent': 1.9600000381469727, 'count': 3757}, {'probability_percent': 2.390000104904175, 'count': 788}, {'probability_percent': 3.740000009536743, 'count': 500}, {'probability_percent': 1.649999976158142, 'count': 452}, {'probability_percent': 1.9299999475479126, 'count': 388}]`
- Probability percentiles: `[0.0, 1.65, 1.96, 1.96, 2.39, 9.94, 20.69, 75.0, 100.0]`

### model_1_v2_next_month

- Question: Is this customer likely to churn next month?
- Accuracy: `0.8953`
- Precision: `0.2985`
- Recall: `0.4306`
- ROC-AUC: `0.7751`
- PR-AUC: `0.2921`
- Flagged rows: `613`
- Rows evaluated: `6417`
- Positive rows: `425`
- Confusion matrix: `[[5562, 430], [242, 183]]`
- Unique rounded probability values: `1612`
- Most common probabilities: `[{'probability_percent': 2.25, 'count': 37}, {'probability_percent': 2.29, 'count': 37}, {'probability_percent': 2.3, 'count': 35}, {'probability_percent': 2.2, 'count': 34}, {'probability_percent': 2.23, 'count': 34}]`
- Probability percentiles: `[1.1, 1.73, 2.16, 2.92, 5.51, 17.008, 27.296, 42.6564, 49.29]`

## 30 Customer Test

| # | Customer | Model 1 Current Risk | Model 1 v2 Next-Month Risk | Actual Current | Actual Next Month |
|---:|---|---:|---:|---:|---:|
| 1 | Ayaan D’Alia (`C10122`) | 1.65% | 2.34% | 0 | 0 |
| 2 | Theodore Bahri (`C11005`) | 100.0% | 46.78% | 1 | 1 |
| 3 | Edhitha Palan (`C11532`) | 100.0% | 34.32% | 1 | 1 |
| 4 | Oliver Kade (`C11837`) | 1.96% | 8.94% | 1 | 1 |
| 5 | Madhavi Date (`C12391`) | 81.4% | 46.14% | 1 | 1 |
| 6 | Netra Ravi (`C12607`) | 1.96% | 2.77% | 0 | 0 |
| 7 | Lohit Jayaraman (`C12715`) | 16.1% | 21.95% | 1 | 1 |
| 8 | Madhavi Rattan (`C12991`) | 1.96% | 1.84% | 0 | 0 |
| 9 | Tamanna Murty (`C13555`) | 100.0% | 39.32% | 1 | 1 |
| 10 | Jatin Purohit (`C13656`) | 53.49% | 39.93% | 1 | 1 |
| 11 | Abha Yogi (`C13919`) | 1.96% | 3.12% | 0 | 0 |
| 12 | Ishanvi Bose (`C14204`) | 2.39% | 3.4% | 0 | 0 |
| 13 | Ethan Bahri (`C14321`) | 36.3% | 28.23% | 0 | 0 |
| 14 | Gautami Peri (`C14388`) | 9.94% | 17.12% | 1 | 1 |
| 15 | Wyatt Modi (`C15182`) | 2.39% | 4.15% | 0 | 0 |
| 16 | Krisha Rajagopal (`C15597`) | 7.29% | 7.94% | 0 | 0 |
| 17 | Vasana Talwar (`C15682`) | 3.74% | 2.44% | 1 | 1 |
| 18 | Ekalinga Ram (`C15711`) | 1.96% | 2.7% | 0 | 0 |
| 19 | Neel Wadhwa (`C16175`) | 1.96% | 1.89% | 0 | 0 |
| 20 | Diya Chandra (`C16671`) | 1.96% | 1.88% | 0 | 0 |
| 21 | Elijah Mitra (`C16902`) | 45.95% | 31.89% | 1 | 1 |
| 22 | Amara Parikh (`C17639`) | 2.25% | 2.47% | 1 | 1 |
| 23 | Nikita Ganguly (`C17907`) | 16.1% | 27.49% | 1 | 1 |
| 24 | Sneha Mahajan (`C17950`) | 2.39% | 8.65% | 0 | 0 |
| 25 | Thomas Kothari (`C18055`) | 1.96% | 3.46% | 0 | 0 |
| 26 | Warda Kalita (`C18307`) | 2.39% | 5.69% | 0 | 0 |
| 27 | Arin Pandya (`C18434`) | 0.0% | 1.87% | 0 | 0 |
| 28 | Anirudh Shukla (`C19179`) | 1.93% | 2.34% | 0 | 0 |
| 29 | Ekaraj Gokhale (`C19185`) | 1.96% | 2.46% | 0 | 0 |
| 30 | Irya Ramakrishnan (`C19406`) | 7.29% | 3.64% | 0 | 0 |

## Customer Details

### 1. Ayaan D’Alia (`C10122`)

#### Model 1 Input

```json
{
  "customer_id": "C10122",
  "customer_name": "Ayaan D’Alia",
  "snapshot_date": "2026-06-01",
  "customer": {
    "age": 65,
    "tenure_months": 62,
    "customer_segment": "farmer",
    "income_regularity": "seasonal",
    "products_count": 1,
    "has_credit_card": 0,
    "has_loan": 0,
    "days_since_last_transaction": 6,
    "balance_change_30d": 9.2642,
    "transaction_change_30d": -22.2205,
    "card_spend_change_30d": -5.4925,
    "app_login_change_30d": 4.1405,
    "salary_missing_days": null,
    "external_transfer_change_30d": 47.3552,
    "upi_share_of_spend": 0.486,
    "fd_maturing_in_30d": 0,
    "products_dropped_90d": 0,
    "complaints_30d": 0,
    "unresolved_complaints": 0,
    "failed_transactions_30d": 1,
    "avg_resolution_time_hrs": 0.0,
    "emi_bounce_30d": 0,
    "branch_code": "BR-110",
    "card_colour": "black"
  },
  "actual_current_month_churn": 0
}
```

#### Model 1 Output

```json
{
  "churn_probability": 1.65,
  "raw_churn_probability": 1.23,
  "risk_score": 4.96,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "tenure_months",
      "value": 62
    },
    {
      "factor": "external_transfer_change_30d",
      "value": 47.3552
    },
    {
      "factor": "products_count",
      "value": 1
    },
    {
      "factor": "age",
      "value": 65
    },
    {
      "factor": "has_loan",
      "value": 0
    }
  ]
}
```

#### Model 1 v2 Input

```json
{
  "customer_id": "C10122",
  "customer_name": "Ayaan D’Alia",
  "prediction_date": "2026-05-01",
  "target_month": "2026-06-01",
  "profile": {
    "tenure_months": 62,
    "customer_segment": "farmer",
    "income_regularity": "seasonal",
    "products_count": 1,
    "has_credit_card": 0,
    "has_loan": 0
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 6,
      "balance_change_30d": 8.7298,
      "transaction_change_30d": -3.3466,
      "card_spend_change_30d": -31.9489,
      "app_login_change_30d": -10.2254,
      "salary_missing_days": null,
      "external_transfer_change_30d": 35.3105,
      "upi_share_of_spend": 0.4443,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 17.7318,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-02-01",
      "days_since_last_transaction": 8,
      "balance_change_30d": -28.4438,
      "transaction_change_30d": -20.3489,
      "card_spend_change_30d": -19.1785,
      "app_login_change_30d": -18.0791,
      "salary_missing_days": null,
      "external_transfer_change_30d": 33.3374,
      "upi_share_of_spend": 0.4701,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 1,
      "complaints_30d": 2,
      "unresolved_complaints": 1,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 30.8911,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-03-01",
      "days_since_last_transaction": 6,
      "balance_change_30d": -12.7914,
      "transaction_change_30d": -15.8763,
      "card_spend_change_30d": -27.5438,
      "app_login_change_30d": -2.1854,
      "salary_missing_days": null,
      "external_transfer_change_30d": 20.2691,
      "upi_share_of_spend": 0.4494,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 14.1215,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-04-01",
      "days_since_last_transaction": 7,
      "balance_change_30d": 4.5254,
      "transaction_change_30d": -20.6609,
      "card_spend_change_30d": -4.8879,
      "app_login_change_30d": -10.8731,
      "salary_missing_days": null,
      "external_transfer_change_30d": -6.6126,
      "upi_share_of_spend": 0.4566,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 35.4696,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-05-01",
      "days_since_last_transaction": 7,
      "balance_change_30d": -24.8127,
      "transaction_change_30d": 4.8818,
      "card_spend_change_30d": -31.6215,
      "app_login_change_30d": -54.9605,
      "salary_missing_days": null,
      "external_transfer_change_30d": 34.5376,
      "upi_share_of_spend": 0.3778,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 0,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 0.0,
      "emi_bounce_30d": 0
    }
  ],
  "actual_next_month_churn": 0
}
```

#### Model 1 v2 Output

```json
{
  "churn_probability": 2.34,
  "raw_churn_probability": 26.98,
  "probability_mode": "sigmoid",
  "risk_score": 7.01,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "latest_balance_change_30d",
      "value": -24.8127,
      "message": "Balance has been falling across recent months.",
      "contribution": 0.1410766988992691
    },
    {
      "factor": "latest_card_spend_change_30d",
      "value": -31.6215,
      "message": "Card spending has been falling across recent months.",
      "contribution": 0.06384024024009705
    },
    {
      "factor": "avg_card_spend_change_30d_3m",
      "value": -21.351066666666668,
      "message": "Card spending has been falling across recent months.",
      "contribution": 0.05451587587594986
    },
    {
      "factor": "avg_card_spend_change_30d_6m",
      "value": -23.03612,
      "message": "Card spending has been falling across recent months.",
      "contribution": 0.03989051282405853
    },
    {
      "factor": "latest_vs_avg_balance_change_30d_available_history",
      "value": -14.25416,
      "message": "Balance has been falling across recent months.",
      "contribution": 0.029423490166664124
    }
  ]
}
```

### 2. Theodore Bahri (`C11005`)

#### Model 1 Input

```json
{
  "customer_id": "C11005",
  "customer_name": "Theodore Bahri",
  "snapshot_date": "2026-06-01",
  "customer": {
    "age": 54,
    "tenure_months": 107,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 3,
    "has_credit_card": 1,
    "has_loan": 1,
    "days_since_last_transaction": 21,
    "balance_change_30d": -75.6987,
    "transaction_change_30d": -57.6559,
    "card_spend_change_30d": -68.1285,
    "app_login_change_30d": -64.4349,
    "salary_missing_days": 11.0,
    "external_transfer_change_30d": 97.2702,
    "upi_share_of_spend": 0.8169,
    "fd_maturing_in_30d": 0,
    "products_dropped_90d": 0,
    "complaints_30d": 1,
    "unresolved_complaints": 0,
    "failed_transactions_30d": 3,
    "avg_resolution_time_hrs": 26.1241,
    "emi_bounce_30d": 1,
    "branch_code": "BR-101",
    "card_colour": "gold"
  },
  "actual_current_month_churn": 1
}
```

#### Model 1 Output

```json
{
  "churn_probability": 100.0,
  "raw_churn_probability": 88.7,
  "risk_score": 100.0,
  "churn_prediction": "Yes",
  "risk_level": "High",
  "top_risk_factors": [
    {
      "factor": "balance_change_30d",
      "value": -75.6987
    },
    {
      "factor": "card_spend_change_30d",
      "value": -68.1285
    },
    {
      "factor": "days_since_last_transaction",
      "value": 21
    },
    {
      "factor": "salary_missing_days",
      "value": 11.0
    },
    {
      "factor": "transaction_change_30d",
      "value": -57.6559
    }
  ]
}
```

#### Model 1 v2 Input

```json
{
  "customer_id": "C11005",
  "customer_name": "Theodore Bahri",
  "prediction_date": "2026-05-01",
  "target_month": "2026-06-01",
  "profile": {
    "tenure_months": 107,
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
      "balance_change_30d": -4.6119,
      "transaction_change_30d": -5.2684,
      "card_spend_change_30d": -8.4731,
      "app_login_change_30d": 8.0069,
      "salary_missing_days": 4.0,
      "external_transfer_change_30d": 24.1167,
      "upi_share_of_spend": 0.6315,
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
      "balance_change_30d": -3.5927,
      "transaction_change_30d": -7.5878,
      "card_spend_change_30d": -11.0105,
      "app_login_change_30d": 4.1888,
      "salary_missing_days": 6.0,
      "external_transfer_change_30d": -36.5226,
      "upi_share_of_spend": 0.6093,
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
      "balance_change_30d": -23.8636,
      "transaction_change_30d": -2.6367,
      "card_spend_change_30d": -13.7173,
      "app_login_change_30d": -16.9867,
      "salary_missing_days": 6.0,
      "external_transfer_change_30d": 50.1085,
      "upi_share_of_spend": 0.6707,
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
      "balance_change_30d": -17.459,
      "transaction_change_30d": -29.7016,
      "card_spend_change_30d": -32.7163,
      "app_login_change_30d": -35.6275,
      "salary_missing_days": 8.0,
      "external_transfer_change_30d": 67.4384,
      "upi_share_of_spend": 0.6627,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 1,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 44.9432,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-05-01",
      "days_since_last_transaction": 14,
      "balance_change_30d": -36.8811,
      "transaction_change_30d": -29.5789,
      "card_spend_change_30d": -31.1808,
      "app_login_change_30d": -46.0569,
      "salary_missing_days": 7.0,
      "external_transfer_change_30d": 58.5597,
      "upi_share_of_spend": 0.7185,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 0,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 2,
      "avg_resolution_time_hrs": 0.0,
      "emi_bounce_30d": 0
    }
  ],
  "actual_next_month_churn": 1
}
```

#### Model 1 v2 Output

```json
{
  "churn_probability": 46.78,
  "raw_churn_probability": 93.9,
  "probability_mode": "sigmoid",
  "risk_score": 80.04,
  "churn_prediction": "Yes",
  "risk_level": "High",
  "top_risk_factors": [
    {
      "factor": "latest_days_since_last_transaction",
      "value": 14,
      "message": "Customer has gone longer without transacting.",
      "contribution": 0.49777480959892273
    },
    {
      "factor": "latest_salary_missing_days",
      "value": 7.0,
      "message": "This signal increased churn risk.",
      "contribution": 0.39943093061447144
    },
    {
      "factor": "latest_vs_avg_upi_share_of_spend_available_history",
      "value": 0.05996,
      "message": "This signal increased churn risk.",
      "contribution": 0.2696836292743683
    },
    {
      "factor": "latest_balance_change_30d",
      "value": -36.8811,
      "message": "Balance has been falling across recent months.",
      "contribution": 0.23984529078006744
    },
    {
      "factor": "latest_transaction_change_30d",
      "value": -29.5789,
      "message": "Transaction activity has been falling across recent months.",
      "contribution": 0.23175759613513947
    }
  ]
}
```

### 3. Edhitha Palan (`C11532`)

#### Model 1 Input

```json
{
  "customer_id": "C11532",
  "customer_name": "Edhitha Palan",
  "snapshot_date": "2026-06-01",
  "customer": {
    "age": 40,
    "tenure_months": 61,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 3,
    "has_credit_card": 1,
    "has_loan": 0,
    "days_since_last_transaction": 23,
    "balance_change_30d": -44.5847,
    "transaction_change_30d": -57.4898,
    "card_spend_change_30d": -76.6279,
    "app_login_change_30d": -34.2758,
    "salary_missing_days": 6.0,
    "external_transfer_change_30d": 53.0361,
    "upi_share_of_spend": 0.7289,
    "fd_maturing_in_30d": 1,
    "products_dropped_90d": 0,
    "complaints_30d": 4,
    "unresolved_complaints": 1,
    "failed_transactions_30d": 6,
    "avg_resolution_time_hrs": 39.596,
    "emi_bounce_30d": 0,
    "branch_code": "BR-110",
    "card_colour": "blue"
  },
  "actual_current_month_churn": 1
}
```

#### Model 1 Output

```json
{
  "churn_probability": 100.0,
  "raw_churn_probability": 95.2,
  "risk_score": 100.0,
  "churn_prediction": "Yes",
  "risk_level": "High",
  "top_risk_factors": [
    {
      "factor": "balance_change_30d",
      "value": -44.5847
    },
    {
      "factor": "card_spend_change_30d",
      "value": -76.6279
    },
    {
      "factor": "days_since_last_transaction",
      "value": 23
    },
    {
      "factor": "failed_transactions_30d",
      "value": 6
    },
    {
      "factor": "fd_maturing_in_30d",
      "value": 1
    }
  ]
}
```

#### Model 1 v2 Input

```json
{
  "customer_id": "C11532",
  "customer_name": "Edhitha Palan",
  "prediction_date": "2026-05-01",
  "target_month": "2026-06-01",
  "profile": {
    "tenure_months": 61,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 3,
    "has_credit_card": 1,
    "has_loan": 0
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 6,
      "balance_change_30d": -26.0465,
      "transaction_change_30d": -23.1322,
      "card_spend_change_30d": -2.3604,
      "app_login_change_30d": -2.2308,
      "salary_missing_days": 2.0,
      "external_transfer_change_30d": 49.8113,
      "upi_share_of_spend": 0.509,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 1,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 39.856,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-02-01",
      "days_since_last_transaction": 9,
      "balance_change_30d": -7.9621,
      "transaction_change_30d": -29.7591,
      "card_spend_change_30d": 5.8372,
      "app_login_change_30d": -15.164,
      "salary_missing_days": 3.0,
      "external_transfer_change_30d": 18.2333,
      "upi_share_of_spend": 0.5291,
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
      "balance_change_30d": -4.0984,
      "transaction_change_30d": -6.5119,
      "card_spend_change_30d": -24.5217,
      "app_login_change_30d": -7.4108,
      "salary_missing_days": 3.0,
      "external_transfer_change_30d": 10.4084,
      "upi_share_of_spend": 0.6014,
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
      "days_since_last_transaction": 13,
      "balance_change_30d": -7.0758,
      "transaction_change_30d": -8.574,
      "card_spend_change_30d": -24.9536,
      "app_login_change_30d": 14.3318,
      "salary_missing_days": 3.0,
      "external_transfer_change_30d": 22.7633,
      "upi_share_of_spend": 0.5626,
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
      "days_since_last_transaction": 13,
      "balance_change_30d": -25.8761,
      "transaction_change_30d": -22.8099,
      "card_spend_change_30d": -48.4717,
      "app_login_change_30d": -57.5871,
      "salary_missing_days": 3.0,
      "external_transfer_change_30d": -4.8255,
      "upi_share_of_spend": 0.5934,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 3,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 3,
      "avg_resolution_time_hrs": 8.264,
      "emi_bounce_30d": 0
    }
  ],
  "actual_next_month_churn": 1
}
```

#### Model 1 v2 Output

```json
{
  "churn_probability": 34.32,
  "raw_churn_probability": 84.24,
  "probability_mode": "sigmoid",
  "risk_score": 75.37,
  "churn_prediction": "Yes",
  "risk_level": "High",
  "top_risk_factors": [
    {
      "factor": "latest_days_since_last_transaction",
      "value": 13,
      "message": "Customer has gone longer without transacting.",
      "contribution": 0.3093003034591675
    },
    {
      "factor": "latest_balance_change_30d",
      "value": -25.8761,
      "message": "Balance has been falling across recent months.",
      "contribution": 0.21932950615882874
    },
    {
      "factor": "latest_card_spend_change_30d",
      "value": -48.4717,
      "message": "Card spending has been falling across recent months.",
      "contribution": 0.2114126980304718
    },
    {
      "factor": "latest_salary_missing_days",
      "value": 3.0,
      "message": "This signal increased churn risk.",
      "contribution": 0.1625441163778305
    },
    {
      "factor": "days_since_last_transaction_trend_6m",
      "value": 1.7999999999999987,
      "message": "Customer has gone longer without transacting.",
      "contribution": 0.1574673056602478
    }
  ]
}
```

### 4. Oliver Kade (`C11837`)

#### Model 1 Input

```json
{
  "customer_id": "C11837",
  "customer_name": "Oliver Kade",
  "snapshot_date": "2026-06-01",
  "customer": {
    "age": 47,
    "tenure_months": 53,
    "customer_segment": "vendor",
    "income_regularity": "irregular",
    "products_count": 2,
    "has_credit_card": 0,
    "has_loan": 1,
    "days_since_last_transaction": 4,
    "balance_change_30d": -3.3329,
    "transaction_change_30d": -4.6275,
    "card_spend_change_30d": 2.3674,
    "app_login_change_30d": -11.7026,
    "salary_missing_days": null,
    "external_transfer_change_30d": 15.1687,
    "upi_share_of_spend": 0.5236,
    "fd_maturing_in_30d": 0,
    "products_dropped_90d": 0,
    "complaints_30d": 0,
    "unresolved_complaints": 0,
    "failed_transactions_30d": 1,
    "avg_resolution_time_hrs": 0.0,
    "emi_bounce_30d": 0,
    "branch_code": "BR-129",
    "card_colour": "black"
  },
  "actual_current_month_churn": 1
}
```

#### Model 1 Output

```json
{
  "churn_probability": 1.96,
  "raw_churn_probability": 1.69,
  "risk_score": 5.87,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "branch_code",
      "value": "BR-129"
    },
    {
      "factor": "tenure_months",
      "value": 53
    },
    {
      "factor": "external_transfer_change_30d",
      "value": 15.1687
    },
    {
      "factor": "customer_segment",
      "value": "vendor"
    },
    {
      "factor": "card_colour",
      "value": "black"
    }
  ]
}
```

#### Model 1 v2 Input

```json
{
  "customer_id": "C11837",
  "customer_name": "Oliver Kade",
  "prediction_date": "2026-05-01",
  "target_month": "2026-06-01",
  "profile": {
    "tenure_months": 53,
    "customer_segment": "vendor",
    "income_regularity": "irregular",
    "products_count": 2,
    "has_credit_card": 0,
    "has_loan": 1
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 0,
      "balance_change_30d": -16.0675,
      "transaction_change_30d": 3.2704,
      "card_spend_change_30d": -17.8224,
      "app_login_change_30d": 1.577,
      "salary_missing_days": null,
      "external_transfer_change_30d": -36.1385,
      "upi_share_of_spend": 0.5475,
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
      "balance_change_30d": -38.4596,
      "transaction_change_30d": -21.7662,
      "card_spend_change_30d": -9.1065,
      "app_login_change_30d": -26.7851,
      "salary_missing_days": null,
      "external_transfer_change_30d": 55.9396,
      "upi_share_of_spend": 0.6934,
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
      "days_since_last_transaction": 10,
      "balance_change_30d": -22.3013,
      "transaction_change_30d": -34.2433,
      "card_spend_change_30d": 1.3504,
      "app_login_change_30d": -0.2064,
      "salary_missing_days": null,
      "external_transfer_change_30d": 23.2544,
      "upi_share_of_spend": 0.5266,
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
      "balance_change_30d": -14.4385,
      "transaction_change_30d": 2.2436,
      "card_spend_change_30d": -10.5737,
      "app_login_change_30d": 5.1377,
      "salary_missing_days": null,
      "external_transfer_change_30d": 7.4798,
      "upi_share_of_spend": 0.6023,
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
      "days_since_last_transaction": 4,
      "balance_change_30d": 0.8429,
      "transaction_change_30d": -0.974,
      "card_spend_change_30d": -4.7784,
      "app_login_change_30d": -14.7406,
      "salary_missing_days": null,
      "external_transfer_change_30d": 79.4736,
      "upi_share_of_spend": 0.6192,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 1,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 40.909,
      "emi_bounce_30d": 0
    }
  ],
  "actual_next_month_churn": 1
}
```

#### Model 1 v2 Output

```json
{
  "churn_probability": 8.94,
  "raw_churn_probability": 53.2,
  "probability_mode": "sigmoid",
  "risk_score": 26.83,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "latest_avg_resolution_time_hrs",
      "value": 40.909,
      "message": "This signal increased churn risk.",
      "contribution": 0.43182307481765747
    },
    {
      "factor": "latest_external_transfer_change_30d",
      "value": 79.4736,
      "message": "External transfers have increased.",
      "contribution": 0.18398408591747284
    },
    {
      "factor": "external_transfer_change_30d_trend_6m",
      "value": 18.276440000000004,
      "message": "External transfers have increased.",
      "contribution": 0.06843428313732147
    },
    {
      "factor": "latest_vs_avg_upi_share_of_spend_available_history",
      "value": 0.0213999999999999,
      "message": "This signal increased churn risk.",
      "contribution": 0.04049156978726387
    },
    {
      "factor": "sum_fd_maturing_in_30d_6m",
      "value": 1.0,
      "message": "Customer has a fixed deposit maturing soon.",
      "contribution": 0.026459410786628723
    }
  ]
}
```

### 5. Madhavi Date (`C12391`)

#### Model 1 Input

```json
{
  "customer_id": "C12391",
  "customer_name": "Madhavi Date",
  "snapshot_date": "2026-05-01",
  "customer": {
    "age": 54,
    "tenure_months": 82,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 1,
    "has_credit_card": 0,
    "has_loan": 0,
    "days_since_last_transaction": 25,
    "balance_change_30d": -41.609,
    "transaction_change_30d": -53.2875,
    "card_spend_change_30d": -56.2011,
    "app_login_change_30d": -34.1603,
    "salary_missing_days": 7.0,
    "external_transfer_change_30d": 95.9949,
    "upi_share_of_spend": 0.744,
    "fd_maturing_in_30d": 0,
    "products_dropped_90d": 3,
    "complaints_30d": 2,
    "unresolved_complaints": 0,
    "failed_transactions_30d": 5,
    "avg_resolution_time_hrs": 16.1477,
    "emi_bounce_30d": 0,
    "branch_code": "BR-109",
    "card_colour": "black"
  },
  "actual_current_month_churn": 1
}
```

#### Model 1 Output

```json
{
  "churn_probability": 81.4,
  "raw_churn_probability": 78.75,
  "risk_score": 93.02,
  "churn_prediction": "Yes",
  "risk_level": "High",
  "top_risk_factors": [
    {
      "factor": "balance_change_30d",
      "value": -41.609
    },
    {
      "factor": "days_since_last_transaction",
      "value": 25
    },
    {
      "factor": "card_spend_change_30d",
      "value": -56.2011
    },
    {
      "factor": "salary_missing_days",
      "value": 7.0
    },
    {
      "factor": "failed_transactions_30d",
      "value": 5
    }
  ]
}
```

#### Model 1 v2 Input

```json
{
  "customer_id": "C12391",
  "customer_name": "Madhavi Date",
  "prediction_date": "2026-04-01",
  "target_month": "2026-05-01",
  "profile": {
    "tenure_months": 82,
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
      "balance_change_30d": -6.7673,
      "transaction_change_30d": 24.2481,
      "card_spend_change_30d": 6.8897,
      "app_login_change_30d": -24.8708,
      "salary_missing_days": 2.0,
      "external_transfer_change_30d": 27.1066,
      "upi_share_of_spend": 0.4776,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 1,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 27.6237,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-02-01",
      "days_since_last_transaction": 5,
      "balance_change_30d": -23.2981,
      "transaction_change_30d": -11.0151,
      "card_spend_change_30d": -36.086,
      "app_login_change_30d": -20.8039,
      "salary_missing_days": 1.0,
      "external_transfer_change_30d": 17.0443,
      "upi_share_of_spend": 0.4537,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 5.6749,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-03-01",
      "days_since_last_transaction": 13,
      "balance_change_30d": -23.8574,
      "transaction_change_30d": -24.0926,
      "card_spend_change_30d": -50.2275,
      "app_login_change_30d": -8.6486,
      "salary_missing_days": 2.0,
      "external_transfer_change_30d": 35.5487,
      "upi_share_of_spend": 0.6046,
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
      "balance_change_30d": -27.2062,
      "transaction_change_30d": -46.3738,
      "card_spend_change_30d": -42.1893,
      "app_login_change_30d": -46.1912,
      "salary_missing_days": 5.0,
      "external_transfer_change_30d": 48.2173,
      "upi_share_of_spend": 0.6483,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 0,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 3,
      "avg_resolution_time_hrs": 0.0,
      "emi_bounce_30d": 0
    }
  ],
  "actual_next_month_churn": 1
}
```

#### Model 1 v2 Output

```json
{
  "churn_probability": 46.14,
  "raw_churn_probability": 93.42,
  "probability_mode": "sigmoid",
  "risk_score": 79.8,
  "churn_prediction": "Yes",
  "risk_level": "High",
  "top_risk_factors": [
    {
      "factor": "latest_days_since_last_transaction",
      "value": 14,
      "message": "Customer has gone longer without transacting.",
      "contribution": 0.47059866786003113
    },
    {
      "factor": "latest_transaction_change_30d",
      "value": -46.3738,
      "message": "Transaction activity has been falling across recent months.",
      "contribution": 0.4608912765979767
    },
    {
      "factor": "latest_salary_missing_days",
      "value": 5.0,
      "message": "This signal increased churn risk.",
      "contribution": 0.28499454259872437
    },
    {
      "factor": "latest_vs_avg_upi_share_of_spend_available_history",
      "value": 0.1022499999999999,
      "message": "This signal increased churn risk.",
      "contribution": 0.24127480387687683
    },
    {
      "factor": "latest_balance_change_30d",
      "value": -27.2062,
      "message": "Balance has been falling across recent months.",
      "contribution": 0.20741435885429382
    }
  ]
}
```

### 6. Netra Ravi (`C12607`)

#### Model 1 Input

```json
{
  "customer_id": "C12607",
  "customer_name": "Netra Ravi",
  "snapshot_date": "2026-06-01",
  "customer": {
    "age": 49,
    "tenure_months": 21,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 2,
    "has_credit_card": 0,
    "has_loan": 1,
    "days_since_last_transaction": 8,
    "balance_change_30d": -16.6076,
    "transaction_change_30d": 18.9563,
    "card_spend_change_30d": 0.7674,
    "app_login_change_30d": 12.7275,
    "salary_missing_days": 0.0,
    "external_transfer_change_30d": -27.1126,
    "upi_share_of_spend": 0.336,
    "fd_maturing_in_30d": 0,
    "products_dropped_90d": 0,
    "complaints_30d": 0,
    "unresolved_complaints": 0,
    "failed_transactions_30d": 0,
    "avg_resolution_time_hrs": 0.0,
    "emi_bounce_30d": 0,
    "branch_code": "BR-116",
    "card_colour": "silver"
  },
  "actual_current_month_churn": 0
}
```

#### Model 1 Output

```json
{
  "churn_probability": 1.96,
  "raw_churn_probability": 2.24,
  "risk_score": 5.87,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "tenure_months",
      "value": 21
    },
    {
      "factor": "app_login_change_30d",
      "value": 12.7275
    },
    {
      "factor": "upi_share_of_spend",
      "value": 0.336
    },
    {
      "factor": "customer_segment",
      "value": "salary"
    },
    {
      "factor": "income_regularity",
      "value": "regular"
    }
  ]
}
```

#### Model 1 v2 Input

```json
{
  "customer_id": "C12607",
  "customer_name": "Netra Ravi",
  "prediction_date": "2026-05-01",
  "target_month": "2026-06-01",
  "profile": {
    "tenure_months": 21,
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
      "balance_change_30d": 23.6471,
      "transaction_change_30d": -10.4074,
      "card_spend_change_30d": 13.9055,
      "app_login_change_30d": 18.5656,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": 12.67,
      "upi_share_of_spend": 0.2683,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 22.0894,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-02-01",
      "days_since_last_transaction": 2,
      "balance_change_30d": 28.847,
      "transaction_change_30d": 22.0006,
      "card_spend_change_30d": 30.4281,
      "app_login_change_30d": 0.5208,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": 11.3984,
      "upi_share_of_spend": 0.2045,
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
      "balance_change_30d": -5.0749,
      "transaction_change_30d": 14.3161,
      "card_spend_change_30d": 12.1789,
      "app_login_change_30d": 19.5437,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": 8.2572,
      "upi_share_of_spend": 0.2756,
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
      "days_since_last_transaction": 11,
      "balance_change_30d": -6.5623,
      "transaction_change_30d": -12.5284,
      "card_spend_change_30d": -40.3146,
      "app_login_change_30d": -17.8899,
      "salary_missing_days": 4.0,
      "external_transfer_change_30d": 5.1042,
      "upi_share_of_spend": 0.312,
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
      "days_since_last_transaction": 9,
      "balance_change_30d": 28.8862,
      "transaction_change_30d": 18.3649,
      "card_spend_change_30d": 18.8729,
      "app_login_change_30d": 12.4461,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -34.9321,
      "upi_share_of_spend": 0.2795,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 0,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 0.0,
      "emi_bounce_30d": 0
    }
  ],
  "actual_next_month_churn": 0
}
```

#### Model 1 v2 Output

```json
{
  "churn_probability": 2.77,
  "raw_churn_probability": 30.25,
  "probability_mode": "sigmoid",
  "risk_score": 8.32,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "days_since_last_transaction_trend_6m",
      "value": 1.499999999999999,
      "message": "Customer has gone longer without transacting.",
      "contribution": 0.09060919284820557
    },
    {
      "factor": "latest_vs_avg_external_transfer_change_30d_available_history",
      "value": -35.43164,
      "message": "This signal increased churn risk.",
      "contribution": 0.028371213003993034
    },
    {
      "factor": "sum_failed_transactions_30d_3m",
      "value": 4.0,
      "message": "Customer has recent failed transactions.",
      "contribution": 0.025434620678424835
    },
    {
      "factor": "latest_vs_avg_upi_share_of_spend_available_history",
      "value": 0.01152,
      "message": "This signal increased churn risk.",
      "contribution": 0.010190991684794426
    },
    {
      "factor": "avg_card_spend_change_30d_3m",
      "value": -3.0876,
      "message": "Card spending has been falling across recent months.",
      "contribution": 0.008111226372420788
    }
  ]
}
```

### 7. Lohit Jayaraman (`C12715`)

#### Model 1 Input

```json
{
  "customer_id": "C12715",
  "customer_name": "Lohit Jayaraman",
  "snapshot_date": "2026-03-01",
  "customer": {
    "age": 51,
    "tenure_months": 50,
    "customer_segment": "business",
    "income_regularity": "irregular",
    "products_count": 3,
    "has_credit_card": 1,
    "has_loan": 1,
    "days_since_last_transaction": 25,
    "balance_change_30d": -22.1309,
    "transaction_change_30d": -24.0058,
    "card_spend_change_30d": -8.0086,
    "app_login_change_30d": -31.6872,
    "salary_missing_days": null,
    "external_transfer_change_30d": 33.6531,
    "upi_share_of_spend": 0.4158,
    "fd_maturing_in_30d": 1,
    "products_dropped_90d": 1,
    "complaints_30d": 0,
    "unresolved_complaints": 0,
    "failed_transactions_30d": 0,
    "avg_resolution_time_hrs": 0.0,
    "emi_bounce_30d": 1,
    "branch_code": "BR-139",
    "card_colour": "silver"
  },
  "actual_current_month_churn": 1
}
```

#### Model 1 Output

```json
{
  "churn_probability": 16.1,
  "raw_churn_probability": 16.51,
  "risk_score": 54.41,
  "churn_prediction": "Yes",
  "risk_level": "Medium",
  "top_risk_factors": [
    {
      "factor": "days_since_last_transaction",
      "value": 25
    },
    {
      "factor": "fd_maturing_in_30d",
      "value": 1
    },
    {
      "factor": "balance_change_30d",
      "value": -22.1309
    },
    {
      "factor": "tenure_months",
      "value": 50
    },
    {
      "factor": "emi_bounce_30d",
      "value": 1
    }
  ]
}
```

#### Model 1 v2 Input

```json
{
  "customer_id": "C12715",
  "customer_name": "Lohit Jayaraman",
  "prediction_date": "2026-02-01",
  "target_month": "2026-03-01",
  "profile": {
    "tenure_months": 50,
    "customer_segment": "business",
    "income_regularity": "irregular",
    "products_count": 3,
    "has_credit_card": 1,
    "has_loan": 1
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 7,
      "balance_change_30d": 6.0645,
      "transaction_change_30d": -0.8841,
      "card_spend_change_30d": -19.3599,
      "app_login_change_30d": -25.4778,
      "salary_missing_days": null,
      "external_transfer_change_30d": -8.0515,
      "upi_share_of_spend": 0.163,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 2,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 2,
      "avg_resolution_time_hrs": 17.2465,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-02-01",
      "days_since_last_transaction": 9,
      "balance_change_30d": 1.0129,
      "transaction_change_30d": 16.074,
      "card_spend_change_30d": 11.3491,
      "app_login_change_30d": -13.6431,
      "salary_missing_days": null,
      "external_transfer_change_30d": -15.6801,
      "upi_share_of_spend": 0.2598,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 3,
      "unresolved_complaints": 1,
      "failed_transactions_30d": 4,
      "avg_resolution_time_hrs": 56.5525,
      "emi_bounce_30d": 1
    }
  ],
  "actual_next_month_churn": 1
}
```

#### Model 1 v2 Output

```json
{
  "churn_probability": 21.95,
  "raw_churn_probability": 72.74,
  "probability_mode": "sigmoid",
  "risk_score": 70.73,
  "churn_prediction": "Yes",
  "risk_level": "Medium",
  "top_risk_factors": [
    {
      "factor": "max_avg_resolution_time_hrs_3m",
      "value": 56.5525,
      "message": "This signal increased churn risk.",
      "contribution": 0.4918763041496277
    },
    {
      "factor": "latest_avg_resolution_time_hrs",
      "value": 56.5525,
      "message": "This signal increased churn risk.",
      "contribution": 0.35371047258377075
    },
    {
      "factor": "sum_failed_transactions_30d_3m",
      "value": 6.0,
      "message": "Customer has recent failed transactions.",
      "contribution": 0.2402317076921463
    },
    {
      "factor": "latest_vs_avg_upi_share_of_spend_available_history",
      "value": 0.0484,
      "message": "This signal increased churn risk.",
      "contribution": 0.14897848665714264
    },
    {
      "factor": "latest_failed_transactions_30d",
      "value": 4,
      "message": "Customer has recent failed transactions.",
      "contribution": 0.1364619880914688
    }
  ]
}
```

### 8. Madhavi Rattan (`C12991`)

#### Model 1 Input

```json
{
  "customer_id": "C12991",
  "customer_name": "Madhavi Rattan",
  "snapshot_date": "2026-06-01",
  "customer": {
    "age": 78,
    "tenure_months": 214,
    "customer_segment": "pension",
    "income_regularity": "regular",
    "products_count": 1,
    "has_credit_card": 0,
    "has_loan": 0,
    "days_since_last_transaction": 0,
    "balance_change_30d": 28.1762,
    "transaction_change_30d": 27.7459,
    "card_spend_change_30d": 18.7561,
    "app_login_change_30d": 24.8195,
    "salary_missing_days": 0.0,
    "external_transfer_change_30d": -9.0908,
    "upi_share_of_spend": 0.0508,
    "fd_maturing_in_30d": 0,
    "products_dropped_90d": 0,
    "complaints_30d": 0,
    "unresolved_complaints": 0,
    "failed_transactions_30d": 0,
    "avg_resolution_time_hrs": 0.0,
    "emi_bounce_30d": 0,
    "branch_code": "BR-133",
    "card_colour": "gold"
  },
  "actual_current_month_churn": 0
}
```

#### Model 1 Output

```json
{
  "churn_probability": 1.96,
  "raw_churn_probability": 1.52,
  "risk_score": 5.87,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "branch_code",
      "value": "BR-133"
    },
    {
      "factor": "app_login_change_30d",
      "value": 24.8195
    },
    {
      "factor": "age",
      "value": 78
    },
    {
      "factor": "upi_share_of_spend",
      "value": 0.0508
    },
    {
      "factor": "products_count",
      "value": 1
    }
  ]
}
```

#### Model 1 v2 Input

```json
{
  "customer_id": "C12991",
  "customer_name": "Madhavi Rattan",
  "prediction_date": "2026-05-01",
  "target_month": "2026-06-01",
  "profile": {
    "tenure_months": 214,
    "customer_segment": "pension",
    "income_regularity": "regular",
    "products_count": 1,
    "has_credit_card": 0,
    "has_loan": 0
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 8,
      "balance_change_30d": 2.4462,
      "transaction_change_30d": -2.0459,
      "card_spend_change_30d": 5.5188,
      "app_login_change_30d": -19.449,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": 9.0587,
      "upi_share_of_spend": 0.0944,
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
      "balance_change_30d": -15.8283,
      "transaction_change_30d": 5.0014,
      "card_spend_change_30d": -20.4409,
      "app_login_change_30d": -42.8882,
      "salary_missing_days": 3.0,
      "external_transfer_change_30d": -5.987,
      "upi_share_of_spend": 0.1022,
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
      "balance_change_30d": -13.8014,
      "transaction_change_30d": -11.1363,
      "card_spend_change_30d": 3.1417,
      "app_login_change_30d": 5.4324,
      "salary_missing_days": 1.0,
      "external_transfer_change_30d": 22.7492,
      "upi_share_of_spend": 0.0669,
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
      "balance_change_30d": 8.3915,
      "transaction_change_30d": 2.3827,
      "card_spend_change_30d": 0.8484,
      "app_login_change_30d": -1.9606,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": 4.1634,
      "upi_share_of_spend": 0.1842,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 23.5837,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-05-01",
      "days_since_last_transaction": 3,
      "balance_change_30d": 1.7707,
      "transaction_change_30d": 1.5388,
      "card_spend_change_30d": 5.551,
      "app_login_change_30d": 21.1746,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": 17.5343,
      "upi_share_of_spend": 0.0,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 0,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 3,
      "avg_resolution_time_hrs": 0.0,
      "emi_bounce_30d": 0
    }
  ],
  "actual_next_month_churn": 0
}
```

#### Model 1 v2 Output

```json
{
  "churn_probability": 1.84,
  "raw_churn_probability": 22.49,
  "probability_mode": "sigmoid",
  "risk_score": 5.53,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "latest_upi_share_of_spend",
      "value": 0.0,
      "message": "This signal increased churn risk.",
      "contribution": 0.10050525516271591
    },
    {
      "factor": "latest_failed_transactions_30d",
      "value": 3,
      "message": "Customer has recent failed transactions.",
      "contribution": 0.06136566773056984
    },
    {
      "factor": "external_transfer_change_30d_trend_6m",
      "value": 2.71016,
      "message": "External transfers have increased.",
      "contribution": 0.04886738583445549
    },
    {
      "factor": "latest_salary_missing_days",
      "value": 0.0,
      "message": "This signal increased churn risk.",
      "contribution": 0.018124224618077278
    },
    {
      "factor": "sum_failed_transactions_30d_3m",
      "value": 4.0,
      "message": "Customer has recent failed transactions.",
      "contribution": 0.013707131147384644
    }
  ]
}
```

### 9. Tamanna Murty (`C13555`)

#### Model 1 Input

```json
{
  "customer_id": "C13555",
  "customer_name": "Tamanna Murty",
  "snapshot_date": "2026-05-01",
  "customer": {
    "age": 66,
    "tenure_months": 125,
    "customer_segment": "pension",
    "income_regularity": "regular",
    "products_count": 3,
    "has_credit_card": 0,
    "has_loan": 1,
    "days_since_last_transaction": 21,
    "balance_change_30d": -30.5057,
    "transaction_change_30d": -43.031,
    "card_spend_change_30d": -54.8974,
    "app_login_change_30d": -24.4885,
    "salary_missing_days": 8.0,
    "external_transfer_change_30d": 92.2303,
    "upi_share_of_spend": 0.5772,
    "fd_maturing_in_30d": 1,
    "products_dropped_90d": 0,
    "complaints_30d": 6,
    "unresolved_complaints": 5,
    "failed_transactions_30d": 3,
    "avg_resolution_time_hrs": 118.2462,
    "emi_bounce_30d": 0,
    "branch_code": "BR-120",
    "card_colour": "silver"
  },
  "actual_current_month_churn": 1
}
```

#### Model 1 Output

```json
{
  "churn_probability": 100.0,
  "raw_churn_probability": 89.23,
  "risk_score": 100.0,
  "churn_prediction": "Yes",
  "risk_level": "High",
  "top_risk_factors": [
    {
      "factor": "avg_resolution_time_hrs",
      "value": 118.2462
    },
    {
      "factor": "salary_missing_days",
      "value": 8.0
    },
    {
      "factor": "balance_change_30d",
      "value": -30.5057
    },
    {
      "factor": "fd_maturing_in_30d",
      "value": 1
    },
    {
      "factor": "card_spend_change_30d",
      "value": -54.8974
    }
  ]
}
```

#### Model 1 v2 Input

```json
{
  "customer_id": "C13555",
  "customer_name": "Tamanna Murty",
  "prediction_date": "2026-04-01",
  "target_month": "2026-05-01",
  "profile": {
    "tenure_months": 125,
    "customer_segment": "pension",
    "income_regularity": "regular",
    "products_count": 3,
    "has_credit_card": 0,
    "has_loan": 1
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 3,
      "balance_change_30d": 6.6616,
      "transaction_change_30d": 4.0608,
      "card_spend_change_30d": -20.2198,
      "app_login_change_30d": 16.8205,
      "salary_missing_days": 1.0,
      "external_transfer_change_30d": -16.9832,
      "upi_share_of_spend": 0.3696,
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
      "balance_change_30d": 22.7021,
      "transaction_change_30d": -9.0353,
      "card_spend_change_30d": 23.251,
      "app_login_change_30d": 20.3238,
      "salary_missing_days": 1.0,
      "external_transfer_change_30d": -23.6858,
      "upi_share_of_spend": 0.3336,
      "fd_maturing_in_30d": 1,
      "products_dropped_90d": 0,
      "complaints_30d": 3,
      "unresolved_complaints": 1,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 27.4163,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-03-01",
      "days_since_last_transaction": 14,
      "balance_change_30d": -18.3111,
      "transaction_change_30d": -35.1455,
      "card_spend_change_30d": -22.2129,
      "app_login_change_30d": -26.0273,
      "salary_missing_days": 3.0,
      "external_transfer_change_30d": 34.6743,
      "upi_share_of_spend": 0.4614,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 3,
      "unresolved_complaints": 2,
      "failed_transactions_30d": 2,
      "avg_resolution_time_hrs": 65.7882,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-04-01",
      "days_since_last_transaction": 9,
      "balance_change_30d": -39.49,
      "transaction_change_30d": -35.2966,
      "card_spend_change_30d": -25.0329,
      "app_login_change_30d": -41.6588,
      "salary_missing_days": 4.0,
      "external_transfer_change_30d": 34.4005,
      "upi_share_of_spend": 0.3922,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 1,
      "complaints_30d": 3,
      "unresolved_complaints": 1,
      "failed_transactions_30d": 6,
      "avg_resolution_time_hrs": 39.8896,
      "emi_bounce_30d": 0
    }
  ],
  "actual_next_month_churn": 1
}
```

#### Model 1 v2 Output

```json
{
  "churn_probability": 39.32,
  "raw_churn_probability": 88.24,
  "probability_mode": "sigmoid",
  "risk_score": 77.24,
  "churn_prediction": "Yes",
  "risk_level": "High",
  "top_risk_factors": [
    {
      "factor": "max_avg_resolution_time_hrs_3m",
      "value": 65.7882,
      "message": "This signal increased churn risk.",
      "contribution": 0.337237149477005
    },
    {
      "factor": "sum_failed_transactions_30d_3m",
      "value": 9.0,
      "message": "Customer has recent failed transactions.",
      "contribution": 0.3077526390552521
    },
    {
      "factor": "latest_salary_missing_days",
      "value": 4.0,
      "message": "This signal increased churn risk.",
      "contribution": 0.24265816807746887
    },
    {
      "factor": "latest_avg_resolution_time_hrs",
      "value": 39.8896,
      "message": "This signal increased churn risk.",
      "contribution": 0.2414616197347641
    },
    {
      "factor": "latest_balance_change_30d",
      "value": -39.49,
      "message": "Balance has been falling across recent months.",
      "contribution": 0.1816871613264084
    }
  ]
}
```

### 10. Jatin Purohit (`C13656`)

#### Model 1 Input

```json
{
  "customer_id": "C13656",
  "customer_name": "Jatin Purohit",
  "snapshot_date": "2026-04-01",
  "customer": {
    "age": 42,
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
    "emi_bounce_30d": 0,
    "branch_code": "BR-133",
    "card_colour": "blue"
  },
  "actual_current_month_churn": 1
}
```

#### Model 1 Output

```json
{
  "churn_probability": 53.49,
  "raw_churn_probability": 59.49,
  "risk_score": 82.56,
  "churn_prediction": "Yes",
  "risk_level": "High",
  "top_risk_factors": [
    {
      "factor": "balance_change_30d",
      "value": -46.5142
    },
    {
      "factor": "days_since_last_transaction",
      "value": 23
    },
    {
      "factor": "card_spend_change_30d",
      "value": -44.3812
    },
    {
      "factor": "salary_missing_days",
      "value": 4.0
    },
    {
      "factor": "failed_transactions_30d",
      "value": 3
    }
  ]
}
```

#### Model 1 v2 Input

```json
{
  "customer_id": "C13656",
  "customer_name": "Jatin Purohit",
  "prediction_date": "2026-03-01",
  "target_month": "2026-04-01",
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
    }
  ],
  "actual_next_month_churn": 1
}
```

#### Model 1 v2 Output

```json
{
  "churn_probability": 39.93,
  "raw_churn_probability": 88.71,
  "probability_mode": "sigmoid",
  "risk_score": 77.47,
  "churn_prediction": "Yes",
  "risk_level": "High",
  "top_risk_factors": [
    {
      "factor": "latest_days_since_last_transaction",
      "value": 18,
      "message": "Customer has gone longer without transacting.",
      "contribution": 0.6097189784049988
    },
    {
      "factor": "latest_transaction_change_30d",
      "value": -25.4873,
      "message": "Transaction activity has been falling across recent months.",
      "contribution": 0.2762247920036316
    },
    {
      "factor": "latest_salary_missing_days",
      "value": 3.0,
      "message": "This signal increased churn risk.",
      "contribution": 0.24984236061573029
    },
    {
      "factor": "latest_vs_avg_upi_share_of_spend_available_history",
      "value": 0.0703999999999999,
      "message": "This signal increased churn risk.",
      "contribution": 0.15872031450271606
    },
    {
      "factor": "days_since_last_transaction_trend_6m",
      "value": 5.499999999999999,
      "message": "Customer has gone longer without transacting.",
      "contribution": 0.13960617780685425
    }
  ]
}
```

### 11. Abha Yogi (`C13919`)

#### Model 1 Input

```json
{
  "customer_id": "C13919",
  "customer_name": "Abha Yogi",
  "snapshot_date": "2026-06-01",
  "customer": {
    "age": 40,
    "tenure_months": 45,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 2,
    "has_credit_card": 1,
    "has_loan": 0,
    "days_since_last_transaction": 4,
    "balance_change_30d": 15.0669,
    "transaction_change_30d": 15.7947,
    "card_spend_change_30d": 13.6489,
    "app_login_change_30d": 18.0197,
    "salary_missing_days": 0.0,
    "external_transfer_change_30d": 8.9253,
    "upi_share_of_spend": 0.1486,
    "fd_maturing_in_30d": 0,
    "products_dropped_90d": 0,
    "complaints_30d": 0,
    "unresolved_complaints": 0,
    "failed_transactions_30d": 0,
    "avg_resolution_time_hrs": 0.0,
    "emi_bounce_30d": 0,
    "branch_code": "BR-105",
    "card_colour": "black"
  },
  "actual_current_month_churn": 0
}
```

#### Model 1 Output

```json
{
  "churn_probability": 1.96,
  "raw_churn_probability": 1.77,
  "risk_score": 5.87,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "branch_code",
      "value": "BR-105"
    },
    {
      "factor": "tenure_months",
      "value": 45
    },
    {
      "factor": "upi_share_of_spend",
      "value": 0.1486
    },
    {
      "factor": "app_login_change_30d",
      "value": 18.0197
    },
    {
      "factor": "external_transfer_change_30d",
      "value": 8.9253
    }
  ]
}
```

#### Model 1 v2 Input

```json
{
  "customer_id": "C13919",
  "customer_name": "Abha Yogi",
  "prediction_date": "2026-05-01",
  "target_month": "2026-06-01",
  "profile": {
    "tenure_months": 45,
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
      "balance_change_30d": 1.8017,
      "transaction_change_30d": -5.4952,
      "card_spend_change_30d": 12.9388,
      "app_login_change_30d": 4.0409,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -4.2955,
      "upi_share_of_spend": 0.3751,
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
      "days_since_last_transaction": 8,
      "balance_change_30d": 5.6255,
      "transaction_change_30d": -9.5776,
      "card_spend_change_30d": -19.3791,
      "app_login_change_30d": -18.7433,
      "salary_missing_days": 2.0,
      "external_transfer_change_30d": 41.0991,
      "upi_share_of_spend": 0.3324,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 23.865,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-03-01",
      "days_since_last_transaction": 6,
      "balance_change_30d": 16.1023,
      "transaction_change_30d": -2.2248,
      "card_spend_change_30d": 8.5309,
      "app_login_change_30d": 16.0498,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": 5.8064,
      "upi_share_of_spend": 0.2669,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 9.885,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-04-01",
      "days_since_last_transaction": 5,
      "balance_change_30d": 12.2348,
      "transaction_change_30d": 12.9275,
      "card_spend_change_30d": 7.6656,
      "app_login_change_30d": 5.8701,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -4.7775,
      "upi_share_of_spend": 0.2668,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 2,
      "avg_resolution_time_hrs": 10.3982,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-05-01",
      "days_since_last_transaction": 6,
      "balance_change_30d": 21.3937,
      "transaction_change_30d": 6.344,
      "card_spend_change_30d": -13.9221,
      "app_login_change_30d": 9.6592,
      "salary_missing_days": 1.0,
      "external_transfer_change_30d": 2.2055,
      "upi_share_of_spend": 0.2305,
      "fd_maturing_in_30d": 1,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 3,
      "avg_resolution_time_hrs": 2.4131,
      "emi_bounce_30d": 0
    }
  ],
  "actual_next_month_churn": 0
}
```

#### Model 1 v2 Output

```json
{
  "churn_probability": 3.12,
  "raw_churn_probability": 32.47,
  "probability_mode": "sigmoid",
  "risk_score": 9.35,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "latest_fd_maturing_in_30d",
      "value": 1,
      "message": "Customer has a fixed deposit maturing soon.",
      "contribution": 0.18134522438049316
    },
    {
      "factor": "sum_fd_maturing_in_30d_3m",
      "value": 1.0,
      "message": "Customer has a fixed deposit maturing soon.",
      "contribution": 0.10154124349355698
    },
    {
      "factor": "latest_failed_transactions_30d",
      "value": 3,
      "message": "Customer has recent failed transactions.",
      "contribution": 0.07548364251852036
    },
    {
      "factor": "latest_vs_avg_app_login_change_30d_available_history",
      "value": 6.283860000000001,
      "message": "This signal increased churn risk.",
      "contribution": 0.02259858325123787
    },
    {
      "factor": "latest_card_spend_change_30d",
      "value": -13.9221,
      "message": "Card spending has been falling across recent months.",
      "contribution": 0.021990619599819183
    }
  ]
}
```

### 12. Ishanvi Bose (`C14204`)

#### Model 1 Input

```json
{
  "customer_id": "C14204",
  "customer_name": "Ishanvi Bose",
  "snapshot_date": "2026-06-01",
  "customer": {
    "age": 36,
    "tenure_months": 51,
    "customer_segment": "business",
    "income_regularity": "irregular",
    "products_count": 1,
    "has_credit_card": 0,
    "has_loan": 0,
    "days_since_last_transaction": 0,
    "balance_change_30d": -12.2705,
    "transaction_change_30d": -0.8135,
    "card_spend_change_30d": 24.6247,
    "app_login_change_30d": -11.2049,
    "salary_missing_days": null,
    "external_transfer_change_30d": -6.5775,
    "upi_share_of_spend": 0.1554,
    "fd_maturing_in_30d": 0,
    "products_dropped_90d": 0,
    "complaints_30d": 4,
    "unresolved_complaints": 1,
    "failed_transactions_30d": 0,
    "avg_resolution_time_hrs": 37.7972,
    "emi_bounce_30d": 0,
    "branch_code": "BR-124",
    "card_colour": "gold"
  },
  "actual_current_month_churn": 0
}
```

#### Model 1 Output

```json
{
  "churn_probability": 2.39,
  "raw_churn_probability": 2.93,
  "risk_score": 7.18,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "complaints_30d",
      "value": 4
    },
    {
      "factor": "unresolved_complaints",
      "value": 1
    },
    {
      "factor": "tenure_months",
      "value": 51
    },
    {
      "factor": "upi_share_of_spend",
      "value": 0.1554
    },
    {
      "factor": "products_count",
      "value": 1
    }
  ]
}
```

#### Model 1 v2 Input

```json
{
  "customer_id": "C14204",
  "customer_name": "Ishanvi Bose",
  "prediction_date": "2026-05-01",
  "target_month": "2026-06-01",
  "profile": {
    "tenure_months": 51,
    "customer_segment": "business",
    "income_regularity": "irregular",
    "products_count": 1,
    "has_credit_card": 0,
    "has_loan": 0
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 2,
      "balance_change_30d": 22.6355,
      "transaction_change_30d": 14.9194,
      "card_spend_change_30d": 6.5496,
      "app_login_change_30d": 14.5554,
      "salary_missing_days": null,
      "external_transfer_change_30d": -28.5665,
      "upi_share_of_spend": 0.2249,
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
      "balance_change_30d": -1.2473,
      "transaction_change_30d": -6.3456,
      "card_spend_change_30d": 9.5666,
      "app_login_change_30d": 19.2077,
      "salary_missing_days": null,
      "external_transfer_change_30d": 32.5573,
      "upi_share_of_spend": 0.1585,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 2,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 2,
      "avg_resolution_time_hrs": 29.8272,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-03-01",
      "days_since_last_transaction": 1,
      "balance_change_30d": 26.0602,
      "transaction_change_30d": 12.6384,
      "card_spend_change_30d": -1.3779,
      "app_login_change_30d": 10.7144,
      "salary_missing_days": null,
      "external_transfer_change_30d": 4.5551,
      "upi_share_of_spend": 0.2311,
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
      "days_since_last_transaction": 2,
      "balance_change_30d": 9.4309,
      "transaction_change_30d": 28.3666,
      "card_spend_change_30d": 1.902,
      "app_login_change_30d": 8.3459,
      "salary_missing_days": null,
      "external_transfer_change_30d": 18.8984,
      "upi_share_of_spend": 0.2607,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 2,
      "complaints_30d": 0,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 0.0,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-05-01",
      "days_since_last_transaction": 9,
      "balance_change_30d": 4.967,
      "transaction_change_30d": 14.9439,
      "card_spend_change_30d": -12.5405,
      "app_login_change_30d": 2.8495,
      "salary_missing_days": null,
      "external_transfer_change_30d": 21.2957,
      "upi_share_of_spend": 0.209,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 2,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 29.6081,
      "emi_bounce_30d": 0
    }
  ],
  "actual_next_month_churn": 0
}
```

#### Model 1 v2 Output

```json
{
  "churn_probability": 3.4,
  "raw_churn_probability": 34.17,
  "probability_mode": "sigmoid",
  "risk_score": 10.21,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "latest_avg_resolution_time_hrs",
      "value": 29.6081,
      "message": "This signal increased churn risk.",
      "contribution": 0.1243017315864563
    },
    {
      "factor": "external_transfer_change_30d_trend_6m",
      "value": 8.606550000000002,
      "message": "External transfers have increased.",
      "contribution": 0.04495110735297203
    },
    {
      "factor": "latest_card_spend_change_30d",
      "value": -12.5405,
      "message": "Card spending has been falling across recent months.",
      "contribution": 0.025477828457951546
    },
    {
      "factor": "latest_vs_avg_balance_change_30d_available_history",
      "value": -7.402260000000001,
      "message": "Balance has been falling across recent months.",
      "contribution": 0.017422033473849297
    },
    {
      "factor": "avg_transaction_change_30d_6m",
      "value": 12.90454,
      "message": "This signal increased churn risk.",
      "contribution": 0.011197972111403942
    }
  ]
}
```

### 13. Ethan Bahri (`C14321`)

#### Model 1 Input

```json
{
  "customer_id": "C14321",
  "customer_name": "Ethan Bahri",
  "snapshot_date": "2026-06-01",
  "customer": {
    "age": 72,
    "tenure_months": 6,
    "customer_segment": "pension",
    "income_regularity": "regular",
    "products_count": 2,
    "has_credit_card": 1,
    "has_loan": 0,
    "days_since_last_transaction": 13,
    "balance_change_30d": 0.5393,
    "transaction_change_30d": 0.142,
    "card_spend_change_30d": 6.2521,
    "app_login_change_30d": -5.1804,
    "salary_missing_days": 1.0,
    "external_transfer_change_30d": -12.8326,
    "upi_share_of_spend": 0.3275,
    "fd_maturing_in_30d": 0,
    "products_dropped_90d": 0,
    "complaints_30d": 6,
    "unresolved_complaints": 6,
    "failed_transactions_30d": 3,
    "avg_resolution_time_hrs": 133.3904,
    "emi_bounce_30d": 0,
    "branch_code": "BR-114",
    "card_colour": "black"
  },
  "actual_current_month_churn": 0
}
```

#### Model 1 Output

```json
{
  "churn_probability": 36.3,
  "raw_churn_probability": 35.85,
  "risk_score": 76.11,
  "churn_prediction": "Yes",
  "risk_level": "High",
  "top_risk_factors": [
    {
      "factor": "avg_resolution_time_hrs",
      "value": 133.3904
    },
    {
      "factor": "tenure_months",
      "value": 6
    },
    {
      "factor": "complaints_30d",
      "value": 6
    },
    {
      "factor": "failed_transactions_30d",
      "value": 3
    },
    {
      "factor": "unresolved_complaints",
      "value": 6
    }
  ]
}
```

#### Model 1 v2 Input

```json
{
  "customer_id": "C14321",
  "customer_name": "Ethan Bahri",
  "prediction_date": "2026-05-01",
  "target_month": "2026-06-01",
  "profile": {
    "tenure_months": 6,
    "customer_segment": "pension",
    "income_regularity": "regular",
    "products_count": 2,
    "has_credit_card": 1,
    "has_loan": 0
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 2,
      "balance_change_30d": 7.9099,
      "transaction_change_30d": 42.1594,
      "card_spend_change_30d": 41.0969,
      "app_login_change_30d": 21.1743,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -1.4362,
      "upi_share_of_spend": 0.2795,
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
      "balance_change_30d": 16.4985,
      "transaction_change_30d": 0.0437,
      "card_spend_change_30d": 10.5324,
      "app_login_change_30d": 7.9332,
      "salary_missing_days": 3.0,
      "external_transfer_change_30d": 7.188,
      "upi_share_of_spend": 0.3298,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 6,
      "unresolved_complaints": 2,
      "failed_transactions_30d": 3,
      "avg_resolution_time_hrs": 58.5673,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-03-01",
      "days_since_last_transaction": 4,
      "balance_change_30d": 5.2138,
      "transaction_change_30d": 9.6317,
      "card_spend_change_30d": -7.8306,
      "app_login_change_30d": 37.16,
      "salary_missing_days": 2.0,
      "external_transfer_change_30d": -1.9913,
      "upi_share_of_spend": 0.3366,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 6,
      "unresolved_complaints": 5,
      "failed_transactions_30d": 5,
      "avg_resolution_time_hrs": 126.7058,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-04-01",
      "days_since_last_transaction": 5,
      "balance_change_30d": 3.245,
      "transaction_change_30d": -6.9767,
      "card_spend_change_30d": -1.2925,
      "app_login_change_30d": -7.4456,
      "salary_missing_days": 3.0,
      "external_transfer_change_30d": -20.9619,
      "upi_share_of_spend": 0.4678,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 6,
      "unresolved_complaints": 5,
      "failed_transactions_30d": 3,
      "avg_resolution_time_hrs": 86.1837,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-05-01",
      "days_since_last_transaction": 10,
      "balance_change_30d": -30.2961,
      "transaction_change_30d": -10.6722,
      "card_spend_change_30d": 11.6345,
      "app_login_change_30d": 19.73,
      "salary_missing_days": 1.0,
      "external_transfer_change_30d": -32.4322,
      "upi_share_of_spend": 0.3843,
      "fd_maturing_in_30d": 1,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 1,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 55.5174,
      "emi_bounce_30d": 0
    }
  ],
  "actual_next_month_churn": 0
}
```

#### Model 1 v2 Output

```json
{
  "churn_probability": 28.23,
  "raw_churn_probability": 78.97,
  "probability_mode": "sigmoid",
  "risk_score": 73.09,
  "churn_prediction": "Yes",
  "risk_level": "High",
  "top_risk_factors": [
    {
      "factor": "max_avg_resolution_time_hrs_3m",
      "value": 126.7058,
      "message": "This signal increased churn risk.",
      "contribution": 0.5451186895370483
    },
    {
      "factor": "sum_failed_transactions_30d_3m",
      "value": 8.0,
      "message": "Customer has recent failed transactions.",
      "contribution": 0.33097389340400696
    },
    {
      "factor": "latest_avg_resolution_time_hrs",
      "value": 55.5174,
      "message": "This signal increased churn risk.",
      "contribution": 0.3302701413631439
    },
    {
      "factor": "latest_fd_maturing_in_30d",
      "value": 1,
      "message": "Customer has a fixed deposit maturing soon.",
      "contribution": 0.11580221354961395
    },
    {
      "factor": "sum_failed_transactions_30d_6m",
      "value": 12.0,
      "message": "Customer has recent failed transactions.",
      "contribution": 0.11232583969831467
    }
  ]
}
```

### 14. Gautami Peri (`C14388`)

#### Model 1 Input

```json
{
  "customer_id": "C14388",
  "customer_name": "Gautami Peri",
  "snapshot_date": "2026-04-01",
  "customer": {
    "age": 39,
    "tenure_months": 26,
    "customer_segment": "vendor",
    "income_regularity": "irregular",
    "products_count": 2,
    "has_credit_card": 0,
    "has_loan": 1,
    "days_since_last_transaction": 19,
    "balance_change_30d": -11.3324,
    "transaction_change_30d": -29.8608,
    "card_spend_change_30d": -40.0076,
    "app_login_change_30d": -5.5841,
    "salary_missing_days": null,
    "external_transfer_change_30d": 111.1098,
    "upi_share_of_spend": 0.4314,
    "fd_maturing_in_30d": 0,
    "products_dropped_90d": 0,
    "complaints_30d": 0,
    "unresolved_complaints": 0,
    "failed_transactions_30d": 0,
    "avg_resolution_time_hrs": 0.0,
    "emi_bounce_30d": 0,
    "branch_code": "BR-140",
    "card_colour": "silver"
  },
  "actual_current_month_churn": 1
}
```

#### Model 1 Output

```json
{
  "churn_probability": 9.94,
  "raw_churn_probability": 12.06,
  "risk_score": 29.81,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "days_since_last_transaction",
      "value": 19
    },
    {
      "factor": "card_spend_change_30d",
      "value": -40.0076
    },
    {
      "factor": "tenure_months",
      "value": 26
    },
    {
      "factor": "branch_code",
      "value": "BR-140"
    },
    {
      "factor": "app_login_change_30d",
      "value": -5.5841
    }
  ]
}
```

#### Model 1 v2 Input

```json
{
  "customer_id": "C14388",
  "customer_name": "Gautami Peri",
  "prediction_date": "2026-03-01",
  "target_month": "2026-04-01",
  "profile": {
    "tenure_months": 26,
    "customer_segment": "vendor",
    "income_regularity": "irregular",
    "products_count": 2,
    "has_credit_card": 0,
    "has_loan": 1
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 7,
      "balance_change_30d": -0.2764,
      "transaction_change_30d": 15.0123,
      "card_spend_change_30d": 22.6325,
      "app_login_change_30d": 23.3922,
      "salary_missing_days": null,
      "external_transfer_change_30d": 10.2663,
      "upi_share_of_spend": 0.3205,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 1,
      "failed_transactions_30d": 2,
      "avg_resolution_time_hrs": 36.1265,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-02-01",
      "days_since_last_transaction": 12,
      "balance_change_30d": 3.5873,
      "transaction_change_30d": -16.2265,
      "card_spend_change_30d": 0.0843,
      "app_login_change_30d": 4.7369,
      "salary_missing_days": null,
      "external_transfer_change_30d": -11.4572,
      "upi_share_of_spend": 0.334,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 23.5067,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-03-01",
      "days_since_last_transaction": 15,
      "balance_change_30d": -10.5658,
      "transaction_change_30d": -10.2918,
      "card_spend_change_30d": -7.4962,
      "app_login_change_30d": -12.7224,
      "salary_missing_days": null,
      "external_transfer_change_30d": -8.4162,
      "upi_share_of_spend": 0.3484,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 0,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 5,
      "avg_resolution_time_hrs": 0.0,
      "emi_bounce_30d": 0
    }
  ],
  "actual_next_month_churn": 1
}
```

#### Model 1 v2 Output

```json
{
  "churn_probability": 17.12,
  "raw_churn_probability": 67.01,
  "probability_mode": "sigmoid",
  "risk_score": 58.48,
  "churn_prediction": "Yes",
  "risk_level": "Medium",
  "top_risk_factors": [
    {
      "factor": "latest_days_since_last_transaction",
      "value": 15,
      "message": "Customer has gone longer without transacting.",
      "contribution": 0.5190284848213196
    },
    {
      "factor": "sum_failed_transactions_30d_3m",
      "value": 7.0,
      "message": "Customer has recent failed transactions.",
      "contribution": 0.2874694764614105
    },
    {
      "factor": "latest_failed_transactions_30d",
      "value": 5,
      "message": "Customer has recent failed transactions.",
      "contribution": 0.12015756219625473
    },
    {
      "factor": "transaction_change_30d_trend_6m",
      "value": -12.652050000000004,
      "message": "Transaction activity has been falling across recent months.",
      "contribution": 0.09615618735551834
    },
    {
      "factor": "days_since_last_transaction_trend_6m",
      "value": 3.999999999999999,
      "message": "Customer has gone longer without transacting.",
      "contribution": 0.08947237581014633
    }
  ]
}
```

### 15. Wyatt Modi (`C15182`)

#### Model 1 Input

```json
{
  "customer_id": "C15182",
  "customer_name": "Wyatt Modi",
  "snapshot_date": "2026-06-01",
  "customer": {
    "age": 43,
    "tenure_months": 28,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 1,
    "has_credit_card": 0,
    "has_loan": 0,
    "days_since_last_transaction": 4,
    "balance_change_30d": 0.6005,
    "transaction_change_30d": -1.6015,
    "card_spend_change_30d": -11.3179,
    "app_login_change_30d": 15.6077,
    "salary_missing_days": 0.0,
    "external_transfer_change_30d": 24.1207,
    "upi_share_of_spend": 0.6494,
    "fd_maturing_in_30d": 1,
    "products_dropped_90d": 0,
    "complaints_30d": 1,
    "unresolved_complaints": 0,
    "failed_transactions_30d": 2,
    "avg_resolution_time_hrs": 15.8884,
    "emi_bounce_30d": 0,
    "branch_code": "BR-110",
    "card_colour": "blue"
  },
  "actual_current_month_churn": 0
}
```

#### Model 1 Output

```json
{
  "churn_probability": 2.39,
  "raw_churn_probability": 3.19,
  "risk_score": 7.18,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "fd_maturing_in_30d",
      "value": 1
    },
    {
      "factor": "tenure_months",
      "value": 28
    },
    {
      "factor": "failed_transactions_30d",
      "value": 2
    },
    {
      "factor": "external_transfer_change_30d",
      "value": 24.1207
    },
    {
      "factor": "card_colour",
      "value": "blue"
    }
  ]
}
```

#### Model 1 v2 Input

```json
{
  "customer_id": "C15182",
  "customer_name": "Wyatt Modi",
  "prediction_date": "2026-05-01",
  "target_month": "2026-06-01",
  "profile": {
    "tenure_months": 28,
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
      "balance_change_30d": -1.3738,
      "transaction_change_30d": 8.3765,
      "card_spend_change_30d": 34.8293,
      "app_login_change_30d": 10.9308,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": 28.0457,
      "upi_share_of_spend": 0.6345,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 1,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 36.8551,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-02-01",
      "days_since_last_transaction": 3,
      "balance_change_30d": -10.0885,
      "transaction_change_30d": -15.5818,
      "card_spend_change_30d": -19.6067,
      "app_login_change_30d": -0.7204,
      "salary_missing_days": 1.0,
      "external_transfer_change_30d": 24.2262,
      "upi_share_of_spend": 0.5984,
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
      "balance_change_30d": 4.609,
      "transaction_change_30d": -3.6475,
      "card_spend_change_30d": 15.5513,
      "app_login_change_30d": -3.2959,
      "salary_missing_days": 1.0,
      "external_transfer_change_30d": -0.0111,
      "upi_share_of_spend": 0.5658,
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
      "balance_change_30d": 13.0872,
      "transaction_change_30d": 8.3294,
      "card_spend_change_30d": 5.1749,
      "app_login_change_30d": -7.2267,
      "salary_missing_days": 1.0,
      "external_transfer_change_30d": -8.86,
      "upi_share_of_spend": 0.6125,
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
      "balance_change_30d": 8.524,
      "transaction_change_30d": -7.0375,
      "card_spend_change_30d": -11.9554,
      "app_login_change_30d": -2.4107,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": 7.6118,
      "upi_share_of_spend": 0.5528,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 2,
      "unresolved_complaints": 1,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 40.5862,
      "emi_bounce_30d": 0
    }
  ],
  "actual_next_month_churn": 0
}
```

#### Model 1 v2 Output

```json
{
  "churn_probability": 4.15,
  "raw_churn_probability": 38.01,
  "probability_mode": "sigmoid",
  "risk_score": 12.46,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "latest_avg_resolution_time_hrs",
      "value": 40.5862,
      "message": "This signal increased churn risk.",
      "contribution": 0.35857895016670227
    },
    {
      "factor": "transaction_change_30d_trend_6m",
      "value": -0.6916799999999997,
      "message": "Transaction activity has been falling across recent months.",
      "contribution": 0.025034982711076736
    },
    {
      "factor": "latest_upi_share_of_spend",
      "value": 0.5528,
      "message": "This signal increased churn risk.",
      "contribution": 0.0232772808521986
    },
    {
      "factor": "latest_card_spend_change_30d",
      "value": -11.9554,
      "message": "Card spending has been falling across recent months.",
      "contribution": 0.01632802002131939
    },
    {
      "factor": "avg_app_login_change_30d_6m",
      "value": -0.54458,
      "message": "App usage has been falling across recent months.",
      "contribution": 0.0077149104326963425
    }
  ]
}
```

### 16. Krisha Rajagopal (`C15597`)

#### Model 1 Input

```json
{
  "customer_id": "C15597",
  "customer_name": "Krisha Rajagopal",
  "snapshot_date": "2026-06-01",
  "customer": {
    "age": 58,
    "tenure_months": 132,
    "customer_segment": "pension",
    "income_regularity": "regular",
    "products_count": 2,
    "has_credit_card": 1,
    "has_loan": 0,
    "days_since_last_transaction": 10,
    "balance_change_30d": -38.1042,
    "transaction_change_30d": -1.9202,
    "card_spend_change_30d": -29.0742,
    "app_login_change_30d": -30.144,
    "salary_missing_days": 0.0,
    "external_transfer_change_30d": 26.3526,
    "upi_share_of_spend": 0.0696,
    "fd_maturing_in_30d": 0,
    "products_dropped_90d": 1,
    "complaints_30d": 0,
    "unresolved_complaints": 0,
    "failed_transactions_30d": 0,
    "avg_resolution_time_hrs": 0.0,
    "emi_bounce_30d": 0,
    "branch_code": "BR-127",
    "card_colour": "black"
  },
  "actual_current_month_churn": 0
}
```

#### Model 1 Output

```json
{
  "churn_probability": 7.29,
  "raw_churn_probability": 6.83,
  "risk_score": 21.86,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "balance_change_30d",
      "value": -38.1042
    },
    {
      "factor": "card_spend_change_30d",
      "value": -29.0742
    },
    {
      "factor": "branch_code",
      "value": "BR-127"
    },
    {
      "factor": "customer_segment",
      "value": "pension"
    },
    {
      "factor": "upi_share_of_spend",
      "value": 0.0696
    }
  ]
}
```

#### Model 1 v2 Input

```json
{
  "customer_id": "C15597",
  "customer_name": "Krisha Rajagopal",
  "prediction_date": "2026-05-01",
  "target_month": "2026-06-01",
  "profile": {
    "tenure_months": 132,
    "customer_segment": "pension",
    "income_regularity": "regular",
    "products_count": 2,
    "has_credit_card": 1,
    "has_loan": 0
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 13,
      "balance_change_30d": -22.2064,
      "transaction_change_30d": 14.0245,
      "card_spend_change_30d": -32.3838,
      "app_login_change_30d": 13.3052,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -17.5795,
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
      "days_since_last_transaction": 14,
      "balance_change_30d": -25.616,
      "transaction_change_30d": -10.3382,
      "card_spend_change_30d": -24.3313,
      "app_login_change_30d": 2.8522,
      "salary_missing_days": 2.0,
      "external_transfer_change_30d": 36.8788,
      "upi_share_of_spend": 0.0719,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 2,
      "avg_resolution_time_hrs": 26.4925,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-03-01",
      "days_since_last_transaction": 17,
      "balance_change_30d": -4.2441,
      "transaction_change_30d": -26.8697,
      "card_spend_change_30d": 0.7105,
      "app_login_change_30d": -8.2222,
      "salary_missing_days": 3.0,
      "external_transfer_change_30d": 32.9756,
      "upi_share_of_spend": 0.2167,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 2,
      "unresolved_complaints": 1,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 43.4083,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-04-01",
      "days_since_last_transaction": 17,
      "balance_change_30d": -16.5165,
      "transaction_change_30d": -19.8651,
      "card_spend_change_30d": -4.1255,
      "app_login_change_30d": 0.2587,
      "salary_missing_days": 3.0,
      "external_transfer_change_30d": -10.5109,
      "upi_share_of_spend": 0.1064,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 15.6786,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-05-01",
      "days_since_last_transaction": 11,
      "balance_change_30d": 6.8193,
      "transaction_change_30d": -22.3872,
      "card_spend_change_30d": -7.9398,
      "app_login_change_30d": -10.6856,
      "salary_missing_days": 1.0,
      "external_transfer_change_30d": 19.159,
      "upi_share_of_spend": 0.1062,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 2,
      "avg_resolution_time_hrs": 47.2211,
      "emi_bounce_30d": 0
    }
  ],
  "actual_next_month_churn": 0
}
```

#### Model 1 v2 Output

```json
{
  "churn_probability": 7.94,
  "raw_churn_probability": 50.8,
  "probability_mode": "sigmoid",
  "risk_score": 23.83,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "latest_avg_resolution_time_hrs",
      "value": 47.2211,
      "message": "This signal increased churn risk.",
      "contribution": 0.40745753049850464
    },
    {
      "factor": "latest_transaction_change_30d",
      "value": -22.3872,
      "message": "Transaction activity has been falling across recent months.",
      "contribution": 0.11810664087533951
    },
    {
      "factor": "count_quiet_customer_3m",
      "value": 3,
      "message": "This signal increased churn risk.",
      "contribution": 0.04512219503521919
    },
    {
      "factor": "transaction_change_30d_trend_6m",
      "value": -8.235030000000002,
      "message": "Transaction activity has been falling across recent months.",
      "contribution": 0.04209461808204651
    },
    {
      "factor": "external_transfer_change_30d_trend_6m",
      "value": 2.6087300000000018,
      "message": "External transfers have increased.",
      "contribution": 0.035636626183986664
    }
  ]
}
```

### 17. Vasana Talwar (`C15682`)

#### Model 1 Input

```json
{
  "customer_id": "C15682",
  "customer_name": "Vasana Talwar",
  "snapshot_date": "2026-03-01",
  "customer": {
    "age": 67,
    "tenure_months": 246,
    "customer_segment": "pension",
    "income_regularity": "regular",
    "products_count": 1,
    "has_credit_card": 0,
    "has_loan": 0,
    "days_since_last_transaction": 4,
    "balance_change_30d": -8.6078,
    "transaction_change_30d": -22.5897,
    "card_spend_change_30d": -30.0339,
    "app_login_change_30d": -4.8292,
    "salary_missing_days": 4.0,
    "external_transfer_change_30d": 61.8672,
    "upi_share_of_spend": 0.5896,
    "fd_maturing_in_30d": 0,
    "products_dropped_90d": 1,
    "complaints_30d": 0,
    "unresolved_complaints": 0,
    "failed_transactions_30d": 2,
    "avg_resolution_time_hrs": 0.0,
    "emi_bounce_30d": 0,
    "branch_code": "BR-133",
    "card_colour": "gold"
  },
  "actual_current_month_churn": 1
}
```

#### Model 1 Output

```json
{
  "churn_probability": 3.74,
  "raw_churn_probability": 4.61,
  "risk_score": 11.21,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "card_spend_change_30d",
      "value": -30.0339
    },
    {
      "factor": "salary_missing_days",
      "value": 4.0
    },
    {
      "factor": "branch_code",
      "value": "BR-133"
    },
    {
      "factor": "failed_transactions_30d",
      "value": 2
    },
    {
      "factor": "age",
      "value": 67
    }
  ]
}
```

#### Model 1 v2 Input

```json
{
  "customer_id": "C15682",
  "customer_name": "Vasana Talwar",
  "prediction_date": "2026-02-01",
  "target_month": "2026-03-01",
  "profile": {
    "tenure_months": 246,
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
      "balance_change_30d": 1.2488,
      "transaction_change_30d": 17.3519,
      "card_spend_change_30d": 0.749,
      "app_login_change_30d": 15.0264,
      "salary_missing_days": 1.0,
      "external_transfer_change_30d": 6.7736,
      "upi_share_of_spend": 0.4507,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 1,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 19.003,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-02-01",
      "days_since_last_transaction": 0,
      "balance_change_30d": 42.7028,
      "transaction_change_30d": 17.1699,
      "card_spend_change_30d": 14.4187,
      "app_login_change_30d": 37.9743,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": 17.3803,
      "upi_share_of_spend": 0.5619,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 0,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 0.0,
      "emi_bounce_30d": 0
    }
  ],
  "actual_next_month_churn": 1
}
```

#### Model 1 v2 Output

```json
{
  "churn_probability": 2.44,
  "raw_churn_probability": 27.84,
  "probability_mode": "sigmoid",
  "risk_score": 7.33,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "latest_vs_avg_upi_share_of_spend_available_history",
      "value": 0.0555999999999999,
      "message": "This signal increased churn risk.",
      "contribution": 0.16163554787635803
    },
    {
      "factor": "external_transfer_change_30d_trend_6m",
      "value": 10.606699999999991,
      "message": "External transfers have increased.",
      "contribution": 0.05022738501429558
    },
    {
      "factor": "transaction_change_30d_trend_6m",
      "value": -0.1820000000000033,
      "message": "Transaction activity has been falling across recent months.",
      "contribution": 0.04139411449432373
    },
    {
      "factor": "avg_balance_change_30d_3m",
      "value": 21.975800000000003,
      "message": "This signal increased churn risk.",
      "contribution": 0.031014470383524895
    },
    {
      "factor": "card_spend_change_30d_trend_6m",
      "value": 13.669699999999995,
      "message": "This signal increased churn risk.",
      "contribution": 0.02674238756299019
    }
  ]
}
```

### 18. Ekalinga Ram (`C15711`)

#### Model 1 Input

```json
{
  "customer_id": "C15711",
  "customer_name": "Ekalinga Ram",
  "snapshot_date": "2026-06-01",
  "customer": {
    "age": 58,
    "tenure_months": 176,
    "customer_segment": "pension",
    "income_regularity": "regular",
    "products_count": 1,
    "has_credit_card": 0,
    "has_loan": 0,
    "days_since_last_transaction": 0,
    "balance_change_30d": 5.714,
    "transaction_change_30d": 9.8603,
    "card_spend_change_30d": 30.4032,
    "app_login_change_30d": 19.2436,
    "salary_missing_days": 0.0,
    "external_transfer_change_30d": -52.8944,
    "upi_share_of_spend": 0.329,
    "fd_maturing_in_30d": 0,
    "products_dropped_90d": 0,
    "complaints_30d": 0,
    "unresolved_complaints": 0,
    "failed_transactions_30d": 1,
    "avg_resolution_time_hrs": 0.0,
    "emi_bounce_30d": 0,
    "branch_code": "BR-133",
    "card_colour": "blue"
  },
  "actual_current_month_churn": 0
}
```

#### Model 1 Output

```json
{
  "churn_probability": 1.96,
  "raw_churn_probability": 1.57,
  "risk_score": 5.87,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "branch_code",
      "value": "BR-133"
    },
    {
      "factor": "app_login_change_30d",
      "value": 19.2436
    },
    {
      "factor": "products_count",
      "value": 1
    },
    {
      "factor": "card_colour",
      "value": "blue"
    },
    {
      "factor": "customer_segment",
      "value": "pension"
    }
  ]
}
```

#### Model 1 v2 Input

```json
{
  "customer_id": "C15711",
  "customer_name": "Ekalinga Ram",
  "prediction_date": "2026-05-01",
  "target_month": "2026-06-01",
  "profile": {
    "tenure_months": 176,
    "customer_segment": "pension",
    "income_regularity": "regular",
    "products_count": 1,
    "has_credit_card": 0,
    "has_loan": 0
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 7,
      "balance_change_30d": 10.7929,
      "transaction_change_30d": 1.7238,
      "card_spend_change_30d": -11.0081,
      "app_login_change_30d": -0.407,
      "salary_missing_days": 4.0,
      "external_transfer_change_30d": 2.0876,
      "upi_share_of_spend": 0.5175,
      "fd_maturing_in_30d": 1,
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
      "balance_change_30d": -16.5231,
      "transaction_change_30d": -15.5513,
      "card_spend_change_30d": 2.1113,
      "app_login_change_30d": -26.8013,
      "salary_missing_days": 5.0,
      "external_transfer_change_30d": 19.7956,
      "upi_share_of_spend": 0.4823,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 1,
      "complaints_30d": 0,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 2,
      "avg_resolution_time_hrs": 0.0,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-03-01",
      "days_since_last_transaction": 5,
      "balance_change_30d": -32.7991,
      "transaction_change_30d": -31.1882,
      "card_spend_change_30d": -3.1205,
      "app_login_change_30d": -28.0585,
      "salary_missing_days": 4.0,
      "external_transfer_change_30d": 9.513,
      "upi_share_of_spend": 0.511,
      "fd_maturing_in_30d": 1,
      "products_dropped_90d": 1,
      "complaints_30d": 0,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 0.0,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-04-01",
      "days_since_last_transaction": 1,
      "balance_change_30d": -9.2843,
      "transaction_change_30d": -15.2758,
      "card_spend_change_30d": 25.9535,
      "app_login_change_30d": -15.3755,
      "salary_missing_days": 5.0,
      "external_transfer_change_30d": 56.5617,
      "upi_share_of_spend": 0.4028,
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
      "days_since_last_transaction": 6,
      "balance_change_30d": -4.4485,
      "transaction_change_30d": -2.5629,
      "card_spend_change_30d": -21.808,
      "app_login_change_30d": -8.4209,
      "salary_missing_days": 2.0,
      "external_transfer_change_30d": -35.8452,
      "upi_share_of_spend": 0.5024,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 13.9996,
      "emi_bounce_30d": 0
    }
  ],
  "actual_next_month_churn": 0
}
```

#### Model 1 v2 Output

```json
{
  "churn_probability": 2.7,
  "raw_churn_probability": 29.73,
  "probability_mode": "sigmoid",
  "risk_score": 8.1,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "latest_salary_missing_days",
      "value": 2.0,
      "message": "This signal increased churn risk.",
      "contribution": 0.08240928500890732
    },
    {
      "factor": "sum_fd_maturing_in_30d_3m",
      "value": 1.0,
      "message": "Customer has a fixed deposit maturing soon.",
      "contribution": 0.060935474932193756
    },
    {
      "factor": "latest_vs_avg_external_transfer_change_30d_available_history",
      "value": -46.26774,
      "message": "This signal increased churn risk.",
      "contribution": 0.04783423990011215
    },
    {
      "factor": "latest_vs_avg_upi_share_of_spend_available_history",
      "value": 0.0191999999999998,
      "message": "This signal increased churn risk.",
      "contribution": 0.03470278158783913
    },
    {
      "factor": "latest_card_spend_change_30d",
      "value": -21.808,
      "message": "Card spending has been falling across recent months.",
      "contribution": 0.027453741058707237
    }
  ]
}
```

### 19. Neel Wadhwa (`C16175`)

#### Model 1 Input

```json
{
  "customer_id": "C16175",
  "customer_name": "Neel Wadhwa",
  "snapshot_date": "2026-06-01",
  "customer": {
    "age": 50,
    "tenure_months": 111,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 1,
    "has_credit_card": 0,
    "has_loan": 0,
    "days_since_last_transaction": 7,
    "balance_change_30d": 24.6862,
    "transaction_change_30d": -0.4333,
    "card_spend_change_30d": 64.7395,
    "app_login_change_30d": 14.7125,
    "salary_missing_days": 0.0,
    "external_transfer_change_30d": -27.2329,
    "upi_share_of_spend": 0.5567,
    "fd_maturing_in_30d": 0,
    "products_dropped_90d": 0,
    "complaints_30d": 0,
    "unresolved_complaints": 0,
    "failed_transactions_30d": 1,
    "avg_resolution_time_hrs": 0.0,
    "emi_bounce_30d": 0,
    "branch_code": "BR-108",
    "card_colour": "silver"
  },
  "actual_current_month_churn": 0
}
```

#### Model 1 Output

```json
{
  "churn_probability": 1.96,
  "raw_churn_probability": 1.45,
  "risk_score": 5.87,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "branch_code",
      "value": "BR-108"
    },
    {
      "factor": "app_login_change_30d",
      "value": 14.7125
    },
    {
      "factor": "products_count",
      "value": 1
    },
    {
      "factor": "has_loan",
      "value": 0
    },
    {
      "factor": "income_regularity",
      "value": "regular"
    }
  ]
}
```

#### Model 1 v2 Input

```json
{
  "customer_id": "C16175",
  "customer_name": "Neel Wadhwa",
  "prediction_date": "2026-05-01",
  "target_month": "2026-06-01",
  "profile": {
    "tenure_months": 111,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 1,
    "has_credit_card": 0,
    "has_loan": 0
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 6,
      "balance_change_30d": 24.2626,
      "transaction_change_30d": 7.888,
      "card_spend_change_30d": -7.4504,
      "app_login_change_30d": -16.1973,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -18.5394,
      "upi_share_of_spend": 0.5964,
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
      "balance_change_30d": 20.9882,
      "transaction_change_30d": 8.8238,
      "card_spend_change_30d": 1.625,
      "app_login_change_30d": 3.9279,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": 21.4389,
      "upi_share_of_spend": 0.5418,
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
      "balance_change_30d": 1.0052,
      "transaction_change_30d": 10.9499,
      "card_spend_change_30d": 17.9488,
      "app_login_change_30d": -7.0094,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -13.0826,
      "upi_share_of_spend": 0.4683,
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
      "balance_change_30d": 11.6059,
      "transaction_change_30d": 10.361,
      "card_spend_change_30d": 33.5363,
      "app_login_change_30d": 36.8662,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -5.8582,
      "upi_share_of_spend": 0.473,
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
      "balance_change_30d": 41.2832,
      "transaction_change_30d": 41.7049,
      "card_spend_change_30d": 52.0748,
      "app_login_change_30d": 17.3358,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -27.2697,
      "upi_share_of_spend": 0.5979,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 0,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 0.0,
      "emi_bounce_30d": 0
    }
  ],
  "actual_next_month_churn": 0
}
```

#### Model 1 v2 Output

```json
{
  "churn_probability": 1.89,
  "raw_churn_probability": 22.91,
  "probability_mode": "sigmoid",
  "risk_score": 5.66,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "latest_vs_avg_upi_share_of_spend_available_history",
      "value": 0.06242,
      "message": "This signal increased churn risk.",
      "contribution": 0.11717011034488678
    },
    {
      "factor": "avg_transaction_change_30d_3m",
      "value": 21.005266666666667,
      "message": "This signal increased churn risk.",
      "contribution": 0.0521225705742836
    },
    {
      "factor": "latest_vs_avg_card_spend_change_30d_available_history",
      "value": 32.5279,
      "message": "This signal increased churn risk.",
      "contribution": 0.05011071637272835
    },
    {
      "factor": "card_spend_change_30d_trend_6m",
      "value": 15.096170000000004,
      "message": "This signal increased churn risk.",
      "contribution": 0.03589971736073494
    },
    {
      "factor": "latest_upi_share_of_spend",
      "value": 0.5979,
      "message": "This signal increased churn risk.",
      "contribution": 0.03085928037762642
    }
  ]
}
```

### 20. Diya Chandra (`C16671`)

#### Model 1 Input

```json
{
  "customer_id": "C16671",
  "customer_name": "Diya Chandra",
  "snapshot_date": "2026-06-01",
  "customer": {
    "age": 56,
    "tenure_months": 193,
    "customer_segment": "farmer",
    "income_regularity": "seasonal",
    "products_count": 3,
    "has_credit_card": 0,
    "has_loan": 0,
    "days_since_last_transaction": 0,
    "balance_change_30d": 30.0684,
    "transaction_change_30d": 22.552,
    "card_spend_change_30d": 7.0719,
    "app_login_change_30d": 20.0719,
    "salary_missing_days": null,
    "external_transfer_change_30d": -62.5778,
    "upi_share_of_spend": 0.1461,
    "fd_maturing_in_30d": 0,
    "products_dropped_90d": 0,
    "complaints_30d": 1,
    "unresolved_complaints": 0,
    "failed_transactions_30d": 0,
    "avg_resolution_time_hrs": 30.5568,
    "emi_bounce_30d": 0,
    "branch_code": "BR-105",
    "card_colour": "green"
  },
  "actual_current_month_churn": 0
}
```

#### Model 1 Output

```json
{
  "churn_probability": 1.96,
  "raw_churn_probability": 1.88,
  "risk_score": 5.87,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "branch_code",
      "value": "BR-105"
    },
    {
      "factor": "app_login_change_30d",
      "value": 20.0719
    },
    {
      "factor": "upi_share_of_spend",
      "value": 0.1461
    },
    {
      "factor": "card_colour",
      "value": "green"
    },
    {
      "factor": "has_loan",
      "value": 0
    }
  ]
}
```

#### Model 1 v2 Input

```json
{
  "customer_id": "C16671",
  "customer_name": "Diya Chandra",
  "prediction_date": "2026-05-01",
  "target_month": "2026-06-01",
  "profile": {
    "tenure_months": 193,
    "customer_segment": "farmer",
    "income_regularity": "seasonal",
    "products_count": 3,
    "has_credit_card": 0,
    "has_loan": 0
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 0,
      "balance_change_30d": -9.1619,
      "transaction_change_30d": 3.6469,
      "card_spend_change_30d": -21.119,
      "app_login_change_30d": -7.4525,
      "salary_missing_days": null,
      "external_transfer_change_30d": 34.1097,
      "upi_share_of_spend": 0.3859,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 2,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 12.9598,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-02-01",
      "days_since_last_transaction": 7,
      "balance_change_30d": -34.7202,
      "transaction_change_30d": -40.8439,
      "card_spend_change_30d": -33.9368,
      "app_login_change_30d": -27.5104,
      "salary_missing_days": null,
      "external_transfer_change_30d": 25.0874,
      "upi_share_of_spend": 0.4318,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 1,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 44.558,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-03-01",
      "days_since_last_transaction": 0,
      "balance_change_30d": 15.8677,
      "transaction_change_30d": -13.8987,
      "card_spend_change_30d": -15.3007,
      "app_login_change_30d": -14.3069,
      "salary_missing_days": null,
      "external_transfer_change_30d": -16.7725,
      "upi_share_of_spend": 0.417,
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
      "balance_change_30d": 25.8705,
      "transaction_change_30d": 7.5434,
      "card_spend_change_30d": 5.5289,
      "app_login_change_30d": -2.2676,
      "salary_missing_days": null,
      "external_transfer_change_30d": -0.658,
      "upi_share_of_spend": 0.2984,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 2,
      "avg_resolution_time_hrs": 34.5373,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-05-01",
      "days_since_last_transaction": 0,
      "balance_change_30d": 3.243,
      "transaction_change_30d": -4.7799,
      "card_spend_change_30d": 22.8734,
      "app_login_change_30d": 18.0811,
      "salary_missing_days": null,
      "external_transfer_change_30d": 1.3504,
      "upi_share_of_spend": 0.3886,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 0,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 0.0,
      "emi_bounce_30d": 0
    }
  ],
  "actual_next_month_churn": 0
}
```

#### Model 1 v2 Output

```json
{
  "churn_probability": 1.88,
  "raw_churn_probability": 22.87,
  "probability_mode": "sigmoid",
  "risk_score": 5.65,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "card_spend_change_30d_trend_6m",
      "value": 12.74505,
      "message": "This signal increased churn risk.",
      "contribution": 0.025314871221780777
    },
    {
      "factor": "latest_vs_avg_upi_share_of_spend_available_history",
      "value": 0.0042599999999999,
      "message": "This signal increased churn risk.",
      "contribution": 0.007438817992806435
    },
    {
      "factor": "sum_unresolved_complaints_6m",
      "value": 0.0,
      "message": "This signal increased churn risk.",
      "contribution": 0.003251376561820507
    },
    {
      "factor": "avg_app_login_change_30d_available_history",
      "value": -6.69126,
      "message": "App usage has been falling across recent months.",
      "contribution": 0.0029916984494775534
    },
    {
      "factor": "count_unresolved_complaint_month_6m",
      "value": 0,
      "message": "This signal increased churn risk.",
      "contribution": 0.002506077755242586
    }
  ]
}
```

### 21. Elijah Mitra (`C16902`)

#### Model 1 Input

```json
{
  "customer_id": "C16902",
  "customer_name": "Elijah Mitra",
  "snapshot_date": "2026-04-01",
  "customer": {
    "age": 29,
    "tenure_months": 111,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 2,
    "has_credit_card": 0,
    "has_loan": 1,
    "days_since_last_transaction": 21,
    "balance_change_30d": -46.5092,
    "transaction_change_30d": -38.5663,
    "card_spend_change_30d": -47.6546,
    "app_login_change_30d": -16.8827,
    "salary_missing_days": 4.0,
    "external_transfer_change_30d": 21.6044,
    "upi_share_of_spend": 0.4952,
    "fd_maturing_in_30d": 0,
    "products_dropped_90d": 0,
    "complaints_30d": 1,
    "unresolved_complaints": 0,
    "failed_transactions_30d": 1,
    "avg_resolution_time_hrs": 12.2636,
    "emi_bounce_30d": 0,
    "branch_code": "BR-116",
    "card_colour": "green"
  },
  "actual_current_month_churn": 1
}
```

#### Model 1 Output

```json
{
  "churn_probability": 45.95,
  "raw_churn_probability": 46.51,
  "risk_score": 79.73,
  "churn_prediction": "Yes",
  "risk_level": "High",
  "top_risk_factors": [
    {
      "factor": "balance_change_30d",
      "value": -46.5092
    },
    {
      "factor": "card_spend_change_30d",
      "value": -47.6546
    },
    {
      "factor": "days_since_last_transaction",
      "value": 21
    },
    {
      "factor": "salary_missing_days",
      "value": 4.0
    },
    {
      "factor": "customer_segment",
      "value": "salary"
    }
  ]
}
```

#### Model 1 v2 Input

```json
{
  "customer_id": "C16902",
  "customer_name": "Elijah Mitra",
  "prediction_date": "2026-03-01",
  "target_month": "2026-04-01",
  "profile": {
    "tenure_months": 111,
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
      "balance_change_30d": -3.0195,
      "transaction_change_30d": 24.0784,
      "card_spend_change_30d": 13.9065,
      "app_login_change_30d": 36.1711,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": 0.5645,
      "upi_share_of_spend": 0.319,
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
      "balance_change_30d": -8.2425,
      "transaction_change_30d": -2.7193,
      "card_spend_change_30d": 35.355,
      "app_login_change_30d": -12.015,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": 4.269,
      "upi_share_of_spend": 0.4249,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 13.0499,
      "emi_bounce_30d": 1
    },
    {
      "snapshot_date": "2026-03-01",
      "days_since_last_transaction": 20,
      "balance_change_30d": -20.6274,
      "transaction_change_30d": -11.2183,
      "card_spend_change_30d": -12.6679,
      "app_login_change_30d": -30.4917,
      "salary_missing_days": 3.0,
      "external_transfer_change_30d": 60.3833,
      "upi_share_of_spend": 0.457,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 8.9936,
      "emi_bounce_30d": 0
    }
  ],
  "actual_next_month_churn": 1
}
```

#### Model 1 v2 Output

```json
{
  "churn_probability": 31.89,
  "raw_churn_probability": 82.21,
  "probability_mode": "sigmoid",
  "risk_score": 74.46,
  "churn_prediction": "Yes",
  "risk_level": "High",
  "top_risk_factors": [
    {
      "factor": "latest_days_since_last_transaction",
      "value": 20,
      "message": "Customer has gone longer without transacting.",
      "contribution": 0.7085362076759338
    },
    {
      "factor": "latest_salary_missing_days",
      "value": 3.0,
      "message": "This signal increased churn risk.",
      "contribution": 0.2849486768245697
    },
    {
      "factor": "latest_vs_avg_upi_share_of_spend_available_history",
      "value": 0.0566999999999999,
      "message": "This signal increased churn risk.",
      "contribution": 0.20996476709842682
    },
    {
      "factor": "days_since_last_transaction_trend_6m",
      "value": 6.9999999999999964,
      "message": "Customer has gone longer without transacting.",
      "contribution": 0.18296876549720764
    },
    {
      "factor": "latest_balance_change_30d",
      "value": -20.6274,
      "message": "Balance has been falling across recent months.",
      "contribution": 0.15334562957286835
    }
  ]
}
```

### 22. Amara Parikh (`C17639`)

#### Model 1 Input

```json
{
  "customer_id": "C17639",
  "customer_name": "Amara Parikh",
  "snapshot_date": "2026-06-01",
  "customer": {
    "age": 79,
    "tenure_months": 204,
    "customer_segment": "pension",
    "income_regularity": "regular",
    "products_count": 2,
    "has_credit_card": 1,
    "has_loan": 0,
    "days_since_last_transaction": 8,
    "balance_change_30d": -6.2492,
    "transaction_change_30d": 23.6252,
    "card_spend_change_30d": -2.8792,
    "app_login_change_30d": 26.888,
    "salary_missing_days": 0.0,
    "external_transfer_change_30d": 35.4407,
    "upi_share_of_spend": 0.1793,
    "fd_maturing_in_30d": 0,
    "products_dropped_90d": 0,
    "complaints_30d": 2,
    "unresolved_complaints": 0,
    "failed_transactions_30d": 1,
    "avg_resolution_time_hrs": 14.271,
    "emi_bounce_30d": 0,
    "branch_code": "BR-112",
    "card_colour": "black"
  },
  "actual_current_month_churn": 1
}
```

#### Model 1 Output

```json
{
  "churn_probability": 2.25,
  "raw_churn_probability": 2.72,
  "risk_score": 6.74,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "complaints_30d",
      "value": 2
    },
    {
      "factor": "age",
      "value": 79
    },
    {
      "factor": "branch_code",
      "value": "BR-112"
    },
    {
      "factor": "app_login_change_30d",
      "value": 26.888
    },
    {
      "factor": "upi_share_of_spend",
      "value": 0.1793
    }
  ]
}
```

#### Model 1 v2 Input

```json
{
  "customer_id": "C17639",
  "customer_name": "Amara Parikh",
  "prediction_date": "2026-05-01",
  "target_month": "2026-06-01",
  "profile": {
    "tenure_months": 204,
    "customer_segment": "pension",
    "income_regularity": "regular",
    "products_count": 2,
    "has_credit_card": 1,
    "has_loan": 0
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 5,
      "balance_change_30d": -1.8407,
      "transaction_change_30d": -6.48,
      "card_spend_change_30d": 19.4588,
      "app_login_change_30d": 15.5164,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": 42.251,
      "upi_share_of_spend": 0.2589,
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
      "days_since_last_transaction": 12,
      "balance_change_30d": -5.8692,
      "transaction_change_30d": -4.8308,
      "card_spend_change_30d": -25.7912,
      "app_login_change_30d": -7.8675,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": 17.3335,
      "upi_share_of_spend": 0.2894,
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
      "days_since_last_transaction": 10,
      "balance_change_30d": -19.0407,
      "transaction_change_30d": -6.0865,
      "card_spend_change_30d": -7.5246,
      "app_login_change_30d": -30.1533,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": 32.0157,
      "upi_share_of_spend": 0.2819,
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
      "days_since_last_transaction": 6,
      "balance_change_30d": -10.5632,
      "transaction_change_30d": 0.9966,
      "card_spend_change_30d": 2.0407,
      "app_login_change_30d": -5.1065,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -10.4436,
      "upi_share_of_spend": 0.1343,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 3,
      "avg_resolution_time_hrs": 33.4535,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-05-01",
      "days_since_last_transaction": 1,
      "balance_change_30d": 20.4966,
      "transaction_change_30d": 10.9572,
      "card_spend_change_30d": 17.5439,
      "app_login_change_30d": 23.7161,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": 40.891,
      "upi_share_of_spend": 0.1859,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 0,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 0.0,
      "emi_bounce_30d": 0
    }
  ],
  "actual_next_month_churn": 1
}
```

#### Model 1 v2 Output

```json
{
  "churn_probability": 2.47,
  "raw_churn_probability": 28.0,
  "probability_mode": "sigmoid",
  "risk_score": 7.4,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "sum_fd_maturing_in_30d_3m",
      "value": 1.0,
      "message": "Customer has a fixed deposit maturing soon.",
      "contribution": 0.1071714237332344
    },
    {
      "factor": "latest_vs_avg_balance_change_30d_available_history",
      "value": 23.86004,
      "message": "This signal increased churn risk.",
      "contribution": 0.06716857105493546
    },
    {
      "factor": "sum_failed_transactions_30d_3m",
      "value": 4.0,
      "message": "Customer has recent failed transactions.",
      "contribution": 0.03661752864718437
    },
    {
      "factor": "avg_card_spend_change_30d_6m",
      "value": 1.1455200000000003,
      "message": "This signal increased churn risk.",
      "contribution": 0.03075772151350975
    },
    {
      "factor": "max_salary_missing_days_6m",
      "value": 0.0,
      "message": "This signal increased churn risk.",
      "contribution": 0.030200572684407234
    }
  ]
}
```

### 23. Nikita Ganguly (`C17907`)

#### Model 1 Input

```json
{
  "customer_id": "C17907",
  "customer_name": "Nikita Ganguly",
  "snapshot_date": "2026-05-01",
  "customer": {
    "age": 44,
    "tenure_months": 60,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 3,
    "has_credit_card": 0,
    "has_loan": 1,
    "days_since_last_transaction": 6,
    "balance_change_30d": 20.6144,
    "transaction_change_30d": 28.7366,
    "card_spend_change_30d": 58.2696,
    "app_login_change_30d": 17.8517,
    "salary_missing_days": 0.0,
    "external_transfer_change_30d": -40.446,
    "upi_share_of_spend": 0.6221,
    "fd_maturing_in_30d": 0,
    "products_dropped_90d": 0,
    "complaints_30d": 2,
    "unresolved_complaints": 2,
    "failed_transactions_30d": 5,
    "avg_resolution_time_hrs": 103.7772,
    "emi_bounce_30d": 1,
    "branch_code": "BR-134",
    "card_colour": "green"
  },
  "actual_current_month_churn": 1
}
```

#### Model 1 Output

```json
{
  "churn_probability": 16.1,
  "raw_churn_probability": 13.8,
  "risk_score": 54.41,
  "churn_prediction": "Yes",
  "risk_level": "Medium",
  "top_risk_factors": [
    {
      "factor": "avg_resolution_time_hrs",
      "value": 103.7772
    },
    {
      "factor": "failed_transactions_30d",
      "value": 5
    },
    {
      "factor": "complaints_30d",
      "value": 2
    },
    {
      "factor": "unresolved_complaints",
      "value": 2
    },
    {
      "factor": "emi_bounce_30d",
      "value": 1
    }
  ]
}
```

#### Model 1 v2 Input

```json
{
  "customer_id": "C17907",
  "customer_name": "Nikita Ganguly",
  "prediction_date": "2026-04-01",
  "target_month": "2026-05-01",
  "profile": {
    "tenure_months": 60,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 3,
    "has_credit_card": 0,
    "has_loan": 1
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 10,
      "balance_change_30d": 21.8396,
      "transaction_change_30d": 9.1438,
      "card_spend_change_30d": 7.6635,
      "app_login_change_30d": 7.0498,
      "salary_missing_days": 1.0,
      "external_transfer_change_30d": -3.8746,
      "upi_share_of_spend": 0.6797,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 1,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 10.9984,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-02-01",
      "days_since_last_transaction": 9,
      "balance_change_30d": 3.9051,
      "transaction_change_30d": -12.7717,
      "card_spend_change_30d": 25.8366,
      "app_login_change_30d": 55.3557,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": 26.6423,
      "upi_share_of_spend": 0.6574,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 3,
      "unresolved_complaints": 1,
      "failed_transactions_30d": 3,
      "avg_resolution_time_hrs": 50.9968,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-03-01",
      "days_since_last_transaction": 3,
      "balance_change_30d": 24.8374,
      "transaction_change_30d": 16.9779,
      "card_spend_change_30d": 30.1872,
      "app_login_change_30d": 32.0375,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -6.7817,
      "upi_share_of_spend": 0.6439,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 4,
      "unresolved_complaints": 4,
      "failed_transactions_30d": 3,
      "avg_resolution_time_hrs": 88.0314,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-04-01",
      "days_since_last_transaction": 0,
      "balance_change_30d": 44.8814,
      "transaction_change_30d": 50.1447,
      "card_spend_change_30d": 29.8075,
      "app_login_change_30d": 39.4359,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -3.1432,
      "upi_share_of_spend": 0.5824,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 3,
      "unresolved_complaints": 3,
      "failed_transactions_30d": 2,
      "avg_resolution_time_hrs": 90.1903,
      "emi_bounce_30d": 1
    }
  ],
  "actual_next_month_churn": 1
}
```

#### Model 1 v2 Output

```json
{
  "churn_probability": 27.49,
  "raw_churn_probability": 78.28,
  "probability_mode": "sigmoid",
  "risk_score": 72.81,
  "churn_prediction": "Yes",
  "risk_level": "High",
  "top_risk_factors": [
    {
      "factor": "max_avg_resolution_time_hrs_3m",
      "value": 90.1903,
      "message": "This signal increased churn risk.",
      "contribution": 0.6112930774688721
    },
    {
      "factor": "latest_avg_resolution_time_hrs",
      "value": 90.1903,
      "message": "This signal increased churn risk.",
      "contribution": 0.4546065330505371
    },
    {
      "factor": "sum_failed_transactions_30d_3m",
      "value": 8.0,
      "message": "Customer has recent failed transactions.",
      "contribution": 0.43972301483154297
    },
    {
      "factor": "sum_failed_transactions_30d_6m",
      "value": 8.0,
      "message": "Customer has recent failed transactions.",
      "contribution": 0.13824370503425598
    },
    {
      "factor": "sum_complaints_30d_3m",
      "value": 10.0,
      "message": "Customer has recent complaint activity.",
      "contribution": 0.12390425056219101
    }
  ]
}
```

### 24. Sneha Mahajan (`C17950`)

#### Model 1 Input

```json
{
  "customer_id": "C17950",
  "customer_name": "Sneha Mahajan",
  "snapshot_date": "2026-06-01",
  "customer": {
    "age": 24,
    "tenure_months": 25,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 1,
    "has_credit_card": 0,
    "has_loan": 0,
    "days_since_last_transaction": 11,
    "balance_change_30d": -10.6715,
    "transaction_change_30d": -2.6381,
    "card_spend_change_30d": -3.6505,
    "app_login_change_30d": -6.8641,
    "salary_missing_days": 0.0,
    "external_transfer_change_30d": 35.9809,
    "upi_share_of_spend": 0.1974,
    "fd_maturing_in_30d": 0,
    "products_dropped_90d": 0,
    "complaints_30d": 2,
    "unresolved_complaints": 0,
    "failed_transactions_30d": 1,
    "avg_resolution_time_hrs": 24.8936,
    "emi_bounce_30d": 0,
    "branch_code": "BR-113",
    "card_colour": "silver"
  },
  "actual_current_month_churn": 0
}
```

#### Model 1 Output

```json
{
  "churn_probability": 2.39,
  "raw_churn_probability": 2.96,
  "risk_score": 7.18,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "tenure_months",
      "value": 25
    },
    {
      "factor": "complaints_30d",
      "value": 2
    },
    {
      "factor": "age",
      "value": 24
    },
    {
      "factor": "upi_share_of_spend",
      "value": 0.1974
    },
    {
      "factor": "external_transfer_change_30d",
      "value": 35.9809
    }
  ]
}
```

#### Model 1 v2 Input

```json
{
  "customer_id": "C17950",
  "customer_name": "Sneha Mahajan",
  "prediction_date": "2026-05-01",
  "target_month": "2026-06-01",
  "profile": {
    "tenure_months": 25,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 1,
    "has_credit_card": 0,
    "has_loan": 0
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 8,
      "balance_change_30d": -8.3785,
      "transaction_change_30d": -4.7188,
      "card_spend_change_30d": 3.9293,
      "app_login_change_30d": 2.7459,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": 7.2133,
      "upi_share_of_spend": 0.0782,
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
      "balance_change_30d": 9.4992,
      "transaction_change_30d": 0.202,
      "card_spend_change_30d": 10.1512,
      "app_login_change_30d": -8.5022,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": 41.9201,
      "upi_share_of_spend": 0.1254,
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
      "days_since_last_transaction": 14,
      "balance_change_30d": -18.9791,
      "transaction_change_30d": -3.0641,
      "card_spend_change_30d": -28.9797,
      "app_login_change_30d": -9.1407,
      "salary_missing_days": 2.0,
      "external_transfer_change_30d": 2.6085,
      "upi_share_of_spend": 0.2181,
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
      "balance_change_30d": -9.1369,
      "transaction_change_30d": -17.7586,
      "card_spend_change_30d": 9.3821,
      "app_login_change_30d": 2.8693,
      "salary_missing_days": 2.0,
      "external_transfer_change_30d": 28.3408,
      "upi_share_of_spend": 0.112,
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
      "days_since_last_transaction": 14,
      "balance_change_30d": -9.9146,
      "transaction_change_30d": -6.3082,
      "card_spend_change_30d": -1.0753,
      "app_login_change_30d": 21.2897,
      "salary_missing_days": 2.0,
      "external_transfer_change_30d": -8.1255,
      "upi_share_of_spend": 0.2393,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 0,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 0.0,
      "emi_bounce_30d": 0
    }
  ],
  "actual_next_month_churn": 0
}
```

#### Model 1 v2 Output

```json
{
  "churn_probability": 8.65,
  "raw_churn_probability": 52.51,
  "probability_mode": "sigmoid",
  "risk_score": 25.94,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "latest_days_since_last_transaction",
      "value": 14,
      "message": "Customer has gone longer without transacting.",
      "contribution": 0.46793562173843384
    },
    {
      "factor": "latest_vs_avg_upi_share_of_spend_available_history",
      "value": 0.0847,
      "message": "This signal increased churn risk.",
      "contribution": 0.15383969247341156
    },
    {
      "factor": "days_since_last_transaction_trend_6m",
      "value": 1.499999999999999,
      "message": "Customer has gone longer without transacting.",
      "contribution": 0.08701510727405548
    },
    {
      "factor": "count_balance_drop_3m",
      "value": 3,
      "message": "This signal increased churn risk.",
      "contribution": 0.05758494883775711
    },
    {
      "factor": "count_quiet_customer_3m",
      "value": 3,
      "message": "This signal increased churn risk.",
      "contribution": 0.03297402337193489
    }
  ]
}
```

### 25. Thomas Kothari (`C18055`)

#### Model 1 Input

```json
{
  "customer_id": "C18055",
  "customer_name": "Thomas Kothari",
  "snapshot_date": "2026-06-01",
  "customer": {
    "age": 42,
    "tenure_months": 70,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 2,
    "has_credit_card": 0,
    "has_loan": 0,
    "days_since_last_transaction": 3,
    "balance_change_30d": 17.3189,
    "transaction_change_30d": 4.0623,
    "card_spend_change_30d": 16.7142,
    "app_login_change_30d": 18.439,
    "salary_missing_days": 0.0,
    "external_transfer_change_30d": -19.7921,
    "upi_share_of_spend": 0.5137,
    "fd_maturing_in_30d": 0,
    "products_dropped_90d": 0,
    "complaints_30d": 1,
    "unresolved_complaints": 0,
    "failed_transactions_30d": 0,
    "avg_resolution_time_hrs": 26.7178,
    "emi_bounce_30d": 0,
    "branch_code": "BR-105",
    "card_colour": "black"
  },
  "actual_current_month_churn": 0
}
```

#### Model 1 Output

```json
{
  "churn_probability": 1.96,
  "raw_churn_probability": 1.8,
  "risk_score": 5.87,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "branch_code",
      "value": "BR-105"
    },
    {
      "factor": "app_login_change_30d",
      "value": 18.439
    },
    {
      "factor": "customer_segment",
      "value": "salary"
    },
    {
      "factor": "card_colour",
      "value": "black"
    },
    {
      "factor": "income_regularity",
      "value": "regular"
    }
  ]
}
```

#### Model 1 v2 Input

```json
{
  "customer_id": "C18055",
  "customer_name": "Thomas Kothari",
  "prediction_date": "2026-05-01",
  "target_month": "2026-06-01",
  "profile": {
    "tenure_months": 70,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 2,
    "has_credit_card": 0,
    "has_loan": 0
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 5,
      "balance_change_30d": 20.8513,
      "transaction_change_30d": -19.0213,
      "card_spend_change_30d": 20.4339,
      "app_login_change_30d": 22.8584,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": 19.2348,
      "upi_share_of_spend": 0.5415,
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
      "balance_change_30d": -9.165,
      "transaction_change_30d": -0.6025,
      "card_spend_change_30d": 15.6051,
      "app_login_change_30d": 49.7833,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": 3.9797,
      "upi_share_of_spend": 0.5978,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 26.0127,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-03-01",
      "days_since_last_transaction": 9,
      "balance_change_30d": 14.2011,
      "transaction_change_30d": 11.0161,
      "card_spend_change_30d": 1.7369,
      "app_login_change_30d": 6.1761,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -0.1054,
      "upi_share_of_spend": 0.4957,
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
      "balance_change_30d": 3.1611,
      "transaction_change_30d": -1.4084,
      "card_spend_change_30d": -2.9423,
      "app_login_change_30d": 3.573,
      "salary_missing_days": 1.0,
      "external_transfer_change_30d": 19.759,
      "upi_share_of_spend": 0.468,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 2,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 45.6093,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-05-01",
      "days_since_last_transaction": 5,
      "balance_change_30d": 16.3909,
      "transaction_change_30d": 2.7859,
      "card_spend_change_30d": 6.7173,
      "app_login_change_30d": 21.2478,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": 14.5088,
      "upi_share_of_spend": 0.5179,
      "fd_maturing_in_30d": 1,
      "products_dropped_90d": 0,
      "complaints_30d": 0,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 0.0,
      "emi_bounce_30d": 0
    }
  ],
  "actual_next_month_churn": 0
}
```

#### Model 1 v2 Output

```json
{
  "churn_probability": 3.46,
  "raw_churn_probability": 34.45,
  "probability_mode": "sigmoid",
  "risk_score": 10.37,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "latest_fd_maturing_in_30d",
      "value": 1,
      "message": "Customer has a fixed deposit maturing soon.",
      "contribution": 0.21233324706554413
    },
    {
      "factor": "sum_fd_maturing_in_30d_3m",
      "value": 1.0,
      "message": "Customer has a fixed deposit maturing soon.",
      "contribution": 0.0572686493396759
    },
    {
      "factor": "external_transfer_change_30d_trend_6m",
      "value": 0.6327299999999997,
      "message": "External transfers have increased.",
      "contribution": 0.028449980542063713
    },
    {
      "factor": "max_avg_resolution_time_hrs_3m",
      "value": 45.6093,
      "message": "This signal increased churn risk.",
      "contribution": 0.02523370273411274
    },
    {
      "factor": "max_avg_resolution_time_hrs_6m",
      "value": 45.6093,
      "message": "This signal increased churn risk.",
      "contribution": 0.010203332640230656
    }
  ]
}
```

### 26. Warda Kalita (`C18307`)

#### Model 1 Input

```json
{
  "customer_id": "C18307",
  "customer_name": "Warda Kalita",
  "snapshot_date": "2026-06-01",
  "customer": {
    "age": 64,
    "tenure_months": 193,
    "customer_segment": "farmer",
    "income_regularity": "seasonal",
    "products_count": 2,
    "has_credit_card": 0,
    "has_loan": 1,
    "days_since_last_transaction": 10,
    "balance_change_30d": -14.8378,
    "transaction_change_30d": -23.8556,
    "card_spend_change_30d": -37.5713,
    "app_login_change_30d": -53.7337,
    "salary_missing_days": null,
    "external_transfer_change_30d": 7.9588,
    "upi_share_of_spend": 0.7577,
    "fd_maturing_in_30d": 0,
    "products_dropped_90d": 0,
    "complaints_30d": 0,
    "unresolved_complaints": 0,
    "failed_transactions_30d": 0,
    "avg_resolution_time_hrs": 0.0,
    "emi_bounce_30d": 0,
    "branch_code": "BR-112",
    "card_colour": "green"
  },
  "actual_current_month_churn": 0
}
```

#### Model 1 Output

```json
{
  "churn_probability": 2.39,
  "raw_churn_probability": 2.95,
  "risk_score": 7.18,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "card_spend_change_30d",
      "value": -37.5713
    },
    {
      "factor": "branch_code",
      "value": "BR-112"
    },
    {
      "factor": "age",
      "value": 64
    },
    {
      "factor": "external_transfer_change_30d",
      "value": 7.9588
    },
    {
      "factor": "card_colour",
      "value": "green"
    }
  ]
}
```

#### Model 1 v2 Input

```json
{
  "customer_id": "C18307",
  "customer_name": "Warda Kalita",
  "prediction_date": "2026-05-01",
  "target_month": "2026-06-01",
  "profile": {
    "tenure_months": 193,
    "customer_segment": "farmer",
    "income_regularity": "seasonal",
    "products_count": 2,
    "has_credit_card": 0,
    "has_loan": 1
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 18,
      "balance_change_30d": -24.6903,
      "transaction_change_30d": -56.1553,
      "card_spend_change_30d": -30.2173,
      "app_login_change_30d": -22.8919,
      "salary_missing_days": null,
      "external_transfer_change_30d": 108.1782,
      "upi_share_of_spend": 0.895,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 3,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 28.5622,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-02-01",
      "days_since_last_transaction": 12,
      "balance_change_30d": -26.3837,
      "transaction_change_30d": -19.3347,
      "card_spend_change_30d": -14.8353,
      "app_login_change_30d": -11.0528,
      "salary_missing_days": null,
      "external_transfer_change_30d": 65.499,
      "upi_share_of_spend": 0.7363,
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
      "days_since_last_transaction": 12,
      "balance_change_30d": -13.9215,
      "transaction_change_30d": -14.2034,
      "card_spend_change_30d": -38.4625,
      "app_login_change_30d": -13.4952,
      "salary_missing_days": null,
      "external_transfer_change_30d": 38.7148,
      "upi_share_of_spend": 0.8967,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 1,
      "complaints_30d": 2,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 8.0873,
      "emi_bounce_30d": 1
    },
    {
      "snapshot_date": "2026-04-01",
      "days_since_last_transaction": 10,
      "balance_change_30d": -5.0995,
      "transaction_change_30d": -33.2631,
      "card_spend_change_30d": -11.1389,
      "app_login_change_30d": -9.2887,
      "salary_missing_days": null,
      "external_transfer_change_30d": 6.6182,
      "upi_share_of_spend": 0.7969,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 1,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 6.9697,
      "emi_bounce_30d": 1
    },
    {
      "snapshot_date": "2026-05-01",
      "days_since_last_transaction": 12,
      "balance_change_30d": -30.6688,
      "transaction_change_30d": -15.0697,
      "card_spend_change_30d": -5.6148,
      "app_login_change_30d": -23.0904,
      "salary_missing_days": null,
      "external_transfer_change_30d": 51.4948,
      "upi_share_of_spend": 0.8025,
      "fd_maturing_in_30d": 1,
      "products_dropped_90d": 1,
      "complaints_30d": 0,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 3,
      "avg_resolution_time_hrs": 0.0,
      "emi_bounce_30d": 0
    }
  ],
  "actual_next_month_churn": 0
}
```

#### Model 1 v2 Output

```json
{
  "churn_probability": 5.69,
  "raw_churn_probability": 44.14,
  "probability_mode": "sigmoid",
  "risk_score": 17.06,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "latest_balance_change_30d",
      "value": -30.6688,
      "message": "Balance has been falling across recent months.",
      "contribution": 0.15196068584918976
    },
    {
      "factor": "latest_failed_transactions_30d",
      "value": 3,
      "message": "Customer has recent failed transactions.",
      "contribution": 0.11683650314807892
    },
    {
      "factor": "latest_fd_maturing_in_30d",
      "value": 1,
      "message": "Customer has a fixed deposit maturing soon.",
      "contribution": 0.07748418301343918
    },
    {
      "factor": "count_balance_drop_3m",
      "value": 3,
      "message": "This signal increased churn risk.",
      "contribution": 0.0767357349395752
    },
    {
      "factor": "count_balance_drop_6m",
      "value": 5,
      "message": "This signal increased churn risk.",
      "contribution": 0.07094801962375641
    }
  ]
}
```

### 27. Arin Pandya (`C18434`)

#### Model 1 Input

```json
{
  "customer_id": "C18434",
  "customer_name": "Arin Pandya",
  "snapshot_date": "2026-06-01",
  "customer": {
    "age": 47,
    "tenure_months": 66,
    "customer_segment": "business",
    "income_regularity": "irregular",
    "products_count": 2,
    "has_credit_card": 1,
    "has_loan": 0,
    "days_since_last_transaction": 1,
    "balance_change_30d": 27.1777,
    "transaction_change_30d": 36.9948,
    "card_spend_change_30d": 36.8526,
    "app_login_change_30d": 73.002,
    "salary_missing_days": null,
    "external_transfer_change_30d": -30.825,
    "upi_share_of_spend": 0.4722,
    "fd_maturing_in_30d": 0,
    "products_dropped_90d": 0,
    "complaints_30d": 0,
    "unresolved_complaints": 0,
    "failed_transactions_30d": 0,
    "avg_resolution_time_hrs": 0.0,
    "emi_bounce_30d": 0,
    "branch_code": "BR-110",
    "card_colour": "green"
  },
  "actual_current_month_churn": 0
}
```

#### Model 1 Output

```json
{
  "churn_probability": 0.0,
  "raw_churn_probability": 0.92,
  "risk_score": 0.0,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "app_login_change_30d",
      "value": 73.002
    },
    {
      "factor": "income_regularity",
      "value": "irregular"
    },
    {
      "factor": "has_loan",
      "value": 0
    },
    {
      "factor": "has_credit_card",
      "value": 1
    },
    {
      "factor": "card_colour",
      "value": "green"
    }
  ]
}
```

#### Model 1 v2 Input

```json
{
  "customer_id": "C18434",
  "customer_name": "Arin Pandya",
  "prediction_date": "2026-05-01",
  "target_month": "2026-06-01",
  "profile": {
    "tenure_months": 66,
    "customer_segment": "business",
    "income_regularity": "irregular",
    "products_count": 2,
    "has_credit_card": 1,
    "has_loan": 0
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 9,
      "balance_change_30d": 14.3273,
      "transaction_change_30d": -9.132,
      "card_spend_change_30d": -12.5265,
      "app_login_change_30d": -25.1404,
      "salary_missing_days": null,
      "external_transfer_change_30d": 30.7832,
      "upi_share_of_spend": 0.6227,
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
      "days_since_last_transaction": 6,
      "balance_change_30d": 0.9085,
      "transaction_change_30d": 23.0589,
      "card_spend_change_30d": 4.3174,
      "app_login_change_30d": 32.587,
      "salary_missing_days": null,
      "external_transfer_change_30d": 9.3807,
      "upi_share_of_spend": 0.5066,
      "fd_maturing_in_30d": 1,
      "products_dropped_90d": 0,
      "complaints_30d": 2,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 2,
      "avg_resolution_time_hrs": 25.0883,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-03-01",
      "days_since_last_transaction": 7,
      "balance_change_30d": 43.8791,
      "transaction_change_30d": 27.6527,
      "card_spend_change_30d": 24.5938,
      "app_login_change_30d": 30.1497,
      "salary_missing_days": null,
      "external_transfer_change_30d": -9.069,
      "upi_share_of_spend": 0.4177,
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
      "balance_change_30d": 43.9597,
      "transaction_change_30d": 15.2736,
      "card_spend_change_30d": 13.7316,
      "app_login_change_30d": 25.4603,
      "salary_missing_days": null,
      "external_transfer_change_30d": -18.1758,
      "upi_share_of_spend": 0.4152,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 2,
      "avg_resolution_time_hrs": 38.3373,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-05-01",
      "days_since_last_transaction": 3,
      "balance_change_30d": 22.3849,
      "transaction_change_30d": 7.7972,
      "card_spend_change_30d": 16.6805,
      "app_login_change_30d": 42.7602,
      "salary_missing_days": null,
      "external_transfer_change_30d": -37.3581,
      "upi_share_of_spend": 0.505,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 0,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 0.0,
      "emi_bounce_30d": 0
    }
  ],
  "actual_next_month_churn": 0
}
```

#### Model 1 v2 Output

```json
{
  "churn_probability": 1.87,
  "raw_churn_probability": 22.72,
  "probability_mode": "sigmoid",
  "risk_score": 5.6,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "latest_vs_avg_external_transfer_change_30d_available_history",
      "value": -32.4703,
      "message": "This signal increased churn risk.",
      "contribution": 0.07224836945533752
    },
    {
      "factor": "avg_balance_change_30d_3m",
      "value": 36.74123333333333,
      "message": "This signal increased churn risk.",
      "contribution": 0.03880218043923378
    },
    {
      "factor": "card_spend_change_30d_trend_6m",
      "value": 6.78282,
      "message": "This signal increased churn risk.",
      "contribution": 0.03656642138957977
    },
    {
      "factor": "latest_external_transfer_change_30d",
      "value": -37.3581,
      "message": "This signal increased churn risk.",
      "contribution": 0.01691477745771408
    },
    {
      "factor": "latest_vs_avg_card_spend_change_30d_available_history",
      "value": 7.321139999999998,
      "message": "This signal increased churn risk.",
      "contribution": 0.007149143610149622
    }
  ]
}
```

### 28. Anirudh Shukla (`C19179`)

#### Model 1 Input

```json
{
  "customer_id": "C19179",
  "customer_name": "Anirudh Shukla",
  "snapshot_date": "2026-06-01",
  "customer": {
    "age": 41,
    "tenure_months": 42,
    "customer_segment": "business",
    "income_regularity": "irregular",
    "products_count": 2,
    "has_credit_card": 1,
    "has_loan": 0,
    "days_since_last_transaction": 8,
    "balance_change_30d": -4.883,
    "transaction_change_30d": 13.7933,
    "card_spend_change_30d": 15.4634,
    "app_login_change_30d": 20.4761,
    "salary_missing_days": null,
    "external_transfer_change_30d": 62.7997,
    "upi_share_of_spend": 0.3739,
    "fd_maturing_in_30d": 0,
    "products_dropped_90d": 0,
    "complaints_30d": 0,
    "unresolved_complaints": 0,
    "failed_transactions_30d": 0,
    "avg_resolution_time_hrs": 0.0,
    "emi_bounce_30d": 0,
    "branch_code": "BR-124",
    "card_colour": "black"
  },
  "actual_current_month_churn": 0
}
```

#### Model 1 Output

```json
{
  "churn_probability": 1.93,
  "raw_churn_probability": 1.36,
  "risk_score": 5.8,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "tenure_months",
      "value": 42
    },
    {
      "factor": "external_transfer_change_30d",
      "value": 62.7997
    },
    {
      "factor": "app_login_change_30d",
      "value": 20.4761
    },
    {
      "factor": "has_loan",
      "value": 0
    },
    {
      "factor": "income_regularity",
      "value": "irregular"
    }
  ]
}
```

#### Model 1 v2 Input

```json
{
  "customer_id": "C19179",
  "customer_name": "Anirudh Shukla",
  "prediction_date": "2026-05-01",
  "target_month": "2026-06-01",
  "profile": {
    "tenure_months": 42,
    "customer_segment": "business",
    "income_regularity": "irregular",
    "products_count": 2,
    "has_credit_card": 1,
    "has_loan": 0
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 6,
      "balance_change_30d": 14.3716,
      "transaction_change_30d": 32.5617,
      "card_spend_change_30d": 15.232,
      "app_login_change_30d": 11.2163,
      "salary_missing_days": null,
      "external_transfer_change_30d": 20.936,
      "upi_share_of_spend": 0.3782,
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
      "balance_change_30d": -16.7887,
      "transaction_change_30d": -2.6795,
      "card_spend_change_30d": -8.5671,
      "app_login_change_30d": -16.5031,
      "salary_missing_days": null,
      "external_transfer_change_30d": 14.02,
      "upi_share_of_spend": 0.4735,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 2,
      "unresolved_complaints": 1,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 48.9147,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-03-01",
      "days_since_last_transaction": 4,
      "balance_change_30d": 1.7156,
      "transaction_change_30d": -17.986,
      "card_spend_change_30d": -3.1116,
      "app_login_change_30d": -7.6012,
      "salary_missing_days": null,
      "external_transfer_change_30d": -26.6619,
      "upi_share_of_spend": 0.4105,
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
      "days_since_last_transaction": 1,
      "balance_change_30d": 18.5828,
      "transaction_change_30d": 13.3681,
      "card_spend_change_30d": 5.1492,
      "app_login_change_30d": 7.7305,
      "salary_missing_days": null,
      "external_transfer_change_30d": -37.0236,
      "upi_share_of_spend": 0.2744,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 13.8589,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-05-01",
      "days_since_last_transaction": 7,
      "balance_change_30d": -8.8986,
      "transaction_change_30d": 14.3065,
      "card_spend_change_30d": 23.897,
      "app_login_change_30d": -12.7398,
      "salary_missing_days": null,
      "external_transfer_change_30d": 25.1169,
      "upi_share_of_spend": 0.431,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 0,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 2,
      "avg_resolution_time_hrs": 0.0,
      "emi_bounce_30d": 0
    }
  ],
  "actual_next_month_churn": 0
}
```

#### Model 1 v2 Output

```json
{
  "churn_probability": 2.34,
  "raw_churn_probability": 26.98,
  "probability_mode": "sigmoid",
  "risk_score": 7.01,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "latest_vs_avg_upi_share_of_spend_available_history",
      "value": 0.03748,
      "message": "This signal increased churn risk.",
      "contribution": 0.09454689919948578
    },
    {
      "factor": "transaction_change_30d_trend_6m",
      "value": -2.046280000000002,
      "message": "Transaction activity has been falling across recent months.",
      "contribution": 0.018447507172822952
    },
    {
      "factor": "latest_vs_avg_balance_change_30d_available_history",
      "value": -10.69514,
      "message": "Balance has been falling across recent months.",
      "contribution": 0.015767604112625122
    },
    {
      "factor": "max_avg_resolution_time_hrs_6m",
      "value": 48.9147,
      "message": "This signal increased churn risk.",
      "contribution": 0.012296310625970364
    },
    {
      "factor": "sum_complaints_30d_6m",
      "value": 3.0,
      "message": "Customer has recent complaint activity.",
      "contribution": 0.007194933015853167
    }
  ]
}
```

### 29. Ekaraj Gokhale (`C19185`)

#### Model 1 Input

```json
{
  "customer_id": "C19185",
  "customer_name": "Ekaraj Gokhale",
  "snapshot_date": "2026-06-01",
  "customer": {
    "age": 26,
    "tenure_months": 40,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 2,
    "has_credit_card": 0,
    "has_loan": 1,
    "days_since_last_transaction": 8,
    "balance_change_30d": 2.6868,
    "transaction_change_30d": -2.0048,
    "card_spend_change_30d": 24.8201,
    "app_login_change_30d": 16.993,
    "salary_missing_days": 0.0,
    "external_transfer_change_30d": 25.6324,
    "upi_share_of_spend": 0.2835,
    "fd_maturing_in_30d": 0,
    "products_dropped_90d": 0,
    "complaints_30d": 0,
    "unresolved_complaints": 0,
    "failed_transactions_30d": 0,
    "avg_resolution_time_hrs": 0.0,
    "emi_bounce_30d": 0,
    "branch_code": "BR-117",
    "card_colour": "silver"
  },
  "actual_current_month_churn": 0
}
```

#### Model 1 Output

```json
{
  "churn_probability": 1.96,
  "raw_churn_probability": 1.47,
  "risk_score": 5.87,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "tenure_months",
      "value": 40
    },
    {
      "factor": "app_login_change_30d",
      "value": 16.993
    },
    {
      "factor": "age",
      "value": 26
    },
    {
      "factor": "external_transfer_change_30d",
      "value": 25.6324
    },
    {
      "factor": "upi_share_of_spend",
      "value": 0.2835
    }
  ]
}
```

#### Model 1 v2 Input

```json
{
  "customer_id": "C19185",
  "customer_name": "Ekaraj Gokhale",
  "prediction_date": "2026-05-01",
  "target_month": "2026-06-01",
  "profile": {
    "tenure_months": 40,
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
      "balance_change_30d": 1.6141,
      "transaction_change_30d": 7.3986,
      "card_spend_change_30d": 49.8415,
      "app_login_change_30d": -21.1405,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": 20.4937,
      "upi_share_of_spend": 0.2098,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 1,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 3,
      "avg_resolution_time_hrs": 17.2782,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-02-01",
      "days_since_last_transaction": 2,
      "balance_change_30d": 13.0566,
      "transaction_change_30d": 18.2985,
      "card_spend_change_30d": -3.9181,
      "app_login_change_30d": 28.8555,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": 50.9205,
      "upi_share_of_spend": 0.2082,
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
      "days_since_last_transaction": 1,
      "balance_change_30d": 21.1126,
      "transaction_change_30d": -4.7791,
      "card_spend_change_30d": 22.2584,
      "app_login_change_30d": 3.2615,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": 6.5449,
      "upi_share_of_spend": 0.1506,
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
      "days_since_last_transaction": 2,
      "balance_change_30d": 22.9386,
      "transaction_change_30d": -7.649,
      "card_spend_change_30d": 6.0251,
      "app_login_change_30d": 11.0143,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -0.7696,
      "upi_share_of_spend": 0.228,
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
      "days_since_last_transaction": 8,
      "balance_change_30d": 6.6713,
      "transaction_change_30d": 25.9192,
      "card_spend_change_30d": -11.955,
      "app_login_change_30d": 10.3828,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": 17.7301,
      "upi_share_of_spend": 0.2239,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 0,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 0.0,
      "emi_bounce_30d": 0
    }
  ],
  "actual_next_month_churn": 0
}
```

#### Model 1 v2 Output

```json
{
  "churn_probability": 2.46,
  "raw_churn_probability": 27.99,
  "probability_mode": "sigmoid",
  "risk_score": 7.39,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "latest_card_spend_change_30d",
      "value": -11.955,
      "message": "Card spending has been falling across recent months.",
      "contribution": 0.015957217663526535
    },
    {
      "factor": "latest_vs_avg_balance_change_30d_available_history",
      "value": -6.407339999999999,
      "message": "Balance has been falling across recent months.",
      "contribution": 0.013006575405597687
    },
    {
      "factor": "latest_vs_avg_upi_share_of_spend_available_history",
      "value": 0.0197999999999999,
      "message": "This signal increased churn risk.",
      "contribution": 0.012066937983036041
    },
    {
      "factor": "avg_upi_share_of_spend_6m",
      "value": 0.2041,
      "message": "This signal increased churn risk.",
      "contribution": 0.004431761801242828
    },
    {
      "factor": "count_balance_drop_3m",
      "value": 0,
      "message": "This signal increased churn risk.",
      "contribution": 0.004232683684676886
    }
  ]
}
```

### 30. Irya Ramakrishnan (`C19406`)

#### Model 1 Input

```json
{
  "customer_id": "C19406",
  "customer_name": "Irya Ramakrishnan",
  "snapshot_date": "2026-06-01",
  "customer": {
    "age": 72,
    "tenure_months": 137,
    "customer_segment": "pension",
    "income_regularity": "regular",
    "products_count": 2,
    "has_credit_card": 1,
    "has_loan": 0,
    "days_since_last_transaction": 14,
    "balance_change_30d": -28.5806,
    "transaction_change_30d": -27.948,
    "card_spend_change_30d": -44.8442,
    "app_login_change_30d": -11.9748,
    "salary_missing_days": 3.0,
    "external_transfer_change_30d": 50.3216,
    "upi_share_of_spend": 0.4547,
    "fd_maturing_in_30d": 0,
    "products_dropped_90d": 1,
    "complaints_30d": 0,
    "unresolved_complaints": 0,
    "failed_transactions_30d": 0,
    "avg_resolution_time_hrs": 0.0,
    "emi_bounce_30d": 0,
    "branch_code": "BR-118",
    "card_colour": "gold"
  },
  "actual_current_month_churn": 0
}
```

#### Model 1 Output

```json
{
  "churn_probability": 7.29,
  "raw_churn_probability": 6.29,
  "risk_score": 21.86,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "balance_change_30d",
      "value": -28.5806
    },
    {
      "factor": "card_spend_change_30d",
      "value": -44.8442
    },
    {
      "factor": "salary_missing_days",
      "value": 3.0
    },
    {
      "factor": "age",
      "value": 72
    },
    {
      "factor": "customer_segment",
      "value": "pension"
    }
  ]
}
```

#### Model 1 v2 Input

```json
{
  "customer_id": "C19406",
  "customer_name": "Irya Ramakrishnan",
  "prediction_date": "2026-05-01",
  "target_month": "2026-06-01",
  "profile": {
    "tenure_months": 137,
    "customer_segment": "pension",
    "income_regularity": "regular",
    "products_count": 2,
    "has_credit_card": 1,
    "has_loan": 0
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 5,
      "balance_change_30d": -16.4033,
      "transaction_change_30d": -11.7482,
      "card_spend_change_30d": -15.917,
      "app_login_change_30d": 3.1814,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": 42.5095,
      "upi_share_of_spend": 0.3326,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 8.2309,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-02-01",
      "days_since_last_transaction": 6,
      "balance_change_30d": -7.5053,
      "transaction_change_30d": 9.7119,
      "card_spend_change_30d": 30.3043,
      "app_login_change_30d": 25.042,
      "salary_missing_days": 1.0,
      "external_transfer_change_30d": 35.4303,
      "upi_share_of_spend": 0.4098,
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
      "balance_change_30d": -21.227,
      "transaction_change_30d": 3.0694,
      "card_spend_change_30d": 0.1775,
      "app_login_change_30d": 14.767,
      "salary_missing_days": 3.0,
      "external_transfer_change_30d": 14.1767,
      "upi_share_of_spend": 0.4189,
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
      "balance_change_30d": -34.7207,
      "transaction_change_30d": 23.9185,
      "card_spend_change_30d": 4.0577,
      "app_login_change_30d": -12.8537,
      "salary_missing_days": 2.0,
      "external_transfer_change_30d": 12.5509,
      "upi_share_of_spend": 0.5069,
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
      "days_since_last_transaction": 15,
      "balance_change_30d": -3.4317,
      "transaction_change_30d": -1.2554,
      "card_spend_change_30d": -24.8147,
      "app_login_change_30d": -1.5704,
      "salary_missing_days": 2.0,
      "external_transfer_change_30d": 75.9525,
      "upi_share_of_spend": 0.3444,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 0,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 0.0,
      "emi_bounce_30d": 0
    }
  ],
  "actual_next_month_churn": 0
}
```

#### Model 1 v2 Output

```json
{
  "churn_probability": 3.64,
  "raw_churn_probability": 35.46,
  "probability_mode": "sigmoid",
  "risk_score": 10.92,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "latest_days_since_last_transaction",
      "value": 15,
      "message": "Customer has gone longer without transacting.",
      "contribution": 0.45247942209243774
    },
    {
      "factor": "days_since_last_transaction_trend_6m",
      "value": 2.3,
      "message": "Customer has gone longer without transacting.",
      "contribution": 0.11073654145002365
    },
    {
      "factor": "latest_external_transfer_change_30d",
      "value": 75.9525,
      "message": "External transfers have increased.",
      "contribution": 0.10299292951822281
    },
    {
      "factor": "avg_card_spend_change_30d_3m",
      "value": -6.859833333333333,
      "message": "Card spending has been falling across recent months.",
      "contribution": 0.03352419659495354
    },
    {
      "factor": "avg_balance_change_30d_3m",
      "value": -19.793133333333333,
      "message": "Balance has been falling across recent months.",
      "contribution": 0.027250846847891808
    }
  ]
}
```
