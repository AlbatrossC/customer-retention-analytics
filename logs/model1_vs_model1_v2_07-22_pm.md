# Model 1 vs Model 1 v2 Report

- Created at: `2026-08-30T19:22:10`
- Customers tested: `30`

## Important Note

Churn is absorbing in this dataset: a churned customer's panel stops at the month
they leave, so `churn_flag = 1` is always their final row. Model 1's original task -
"is this customer churning in this snapshot?" - therefore scores it on a row whose
features already show the collapse. That is detection after the fact, not prediction,
and it leaves no time to run a retention action.

The first two metric blocks below put both models on the same footing: same rows,
same month of input, same next-month label. The third block is Model 1's original
task, kept for reference only. Its higher numbers come from the easier question,
not from a better model - do not compare them across blocks.

## Metrics

### model_1_same_task_next_month

- Question: Is this customer likely to churn next month? (Model 1, same rows and label as v2)
- Accuracy: `0.9132`
- Precision: `0.3254`
- Recall: `0.2894`
- ROC-AUC: `0.7556`
- PR-AUC: `0.2240`
- Flagged rows: `378`
- Rows evaluated: `6417`
- Positive rows: `425`
- Confusion matrix: `[[5737, 255], [302, 123]]`
- Unique rounded probability values: `43`
- Most common probabilities: `[{'probability_percent': 1.9600000381469727, 'count': 3148}, {'probability_percent': 2.390000104904175, 'count': 691}, {'probability_percent': 3.740000009536743, 'count': 453}, {'probability_percent': 1.649999976158142, 'count': 354}, {'probability_percent': 7.289999961853027, 'count': 322}]`
- Probability percentiles: `[0.0, 1.65, 1.96, 1.96, 2.39, 7.29, 16.1, 36.3, 95.65]`

### model_1_v2_next_month

- Question: Is this customer likely to churn next month?
- Accuracy: `0.8998`
- Precision: `0.3094`
- Recall: `0.4165`
- ROC-AUC: `0.7802`
- PR-AUC: `0.2929`
- Flagged rows: `572`
- Rows evaluated: `6417`
- Positive rows: `425`
- Confusion matrix: `[[5597, 395], [248, 177]]`
- Unique rounded probability values: `1617`
- Most common probabilities: `[{'probability_percent': 2.17, 'count': 34}, {'probability_percent': 2.2, 'count': 31}, {'probability_percent': 2.62, 'count': 30}, {'probability_percent': 2.69, 'count': 30}, {'probability_percent': 3.24, 'count': 28}]`
- Probability percentiles: `[1.18, 2.08, 2.56, 3.39, 6.0, 16.46, 25.222, 37.8968, 44.22]`

### model_1_own_task_current_month

- Question: Is this customer churning in this snapshot? (Model 1's original task, NOT comparable)
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

## 30 Customer Test

Both models score the same month and are graded on the same label: did this
customer churn in the following month?

| # | Customer | Prediction Month | Model 1 Risk | Model 1 v2 Risk | Actual Next Month |
|---:|---|---|---:|---:|---:|
| 1 | Ayaan D’Alia (`C10122`) | 2026-05-01 | 3.74% | 2.97% | 0 |
| 2 | Theodore Bahri (`C11005`) | 2026-05-01 | 25.0% | 40.91% | 1 |
| 3 | Edhitha Palan (`C11532`) | 2026-05-01 | 18.06% | 29.7% | 1 |
| 4 | Oliver Kade (`C11837`) | 2026-05-01 | 1.96% | 9.32% | 1 |
| 5 | Madhavi Date (`C12391`) | 2026-04-01 | 16.1% | 41.21% | 1 |
| 6 | Netra Ravi (`C12607`) | 2026-05-01 | 1.96% | 2.84% | 0 |
| 7 | Lohit Jayaraman (`C12715`) | 2026-02-01 | 9.94% | 20.52% | 1 |
| 8 | Madhavi Rattan (`C12991`) | 2026-05-01 | 1.96% | 2.38% | 0 |
| 9 | Tamanna Murty (`C13555`) | 2026-04-01 | 20.69% | 34.91% | 1 |
| 10 | Jatin Purohit (`C13656`) | 2026-03-01 | 10.0% | 35.84% | 1 |
| 11 | Abha Yogi (`C13919`) | 2026-05-01 | 7.29% | 3.28% | 0 |
| 12 | Ishanvi Bose (`C14204`) | 2026-05-01 | 1.96% | 3.62% | 0 |
| 13 | Ethan Bahri (`C14321`) | 2026-05-01 | 9.94% | 25.51% | 0 |
| 14 | Gautami Peri (`C14388`) | 2026-03-01 | 3.74% | 16.77% | 1 |
| 15 | Wyatt Modi (`C15182`) | 2026-05-01 | 1.96% | 4.14% | 0 |
| 16 | Krisha Rajagopal (`C15597`) | 2026-05-01 | 1.96% | 7.9% | 0 |
| 17 | Vasana Talwar (`C15682`) | 2026-02-01 | 1.96% | 3.94% | 1 |
| 18 | Ekalinga Ram (`C15711`) | 2026-05-01 | 2.39% | 3.19% | 0 |
| 19 | Neel Wadhwa (`C16175`) | 2026-05-01 | 1.93% | 2.88% | 0 |
| 20 | Diya Chandra (`C16671`) | 2026-05-01 | 1.96% | 2.09% | 0 |
| 21 | Elijah Mitra (`C16902`) | 2026-03-01 | 3.74% | 28.75% | 1 |
| 22 | Amara Parikh (`C17639`) | 2026-05-01 | 1.96% | 3.0% | 1 |
| 23 | Nikita Ganguly (`C17907`) | 2026-04-01 | 7.41% | 26.6% | 1 |
| 24 | Sneha Mahajan (`C17950`) | 2026-05-01 | 2.25% | 8.86% | 0 |
| 25 | Thomas Kothari (`C18055`) | 2026-05-01 | 1.96% | 3.71% | 0 |
| 26 | Warda Kalita (`C18307`) | 2026-05-01 | 9.94% | 5.97% | 0 |
| 27 | Arin Pandya (`C18434`) | 2026-05-01 | 0.0% | 2.58% | 0 |
| 28 | Anirudh Shukla (`C19179`) | 2026-05-01 | 1.96% | 2.77% | 0 |
| 29 | Ekaraj Gokhale (`C19185`) | 2026-05-01 | 1.96% | 2.6% | 0 |
| 30 | Irya Ramakrishnan (`C19406`) | 2026-05-01 | 1.96% | 3.85% | 0 |

## Customer Details

### 1. Ayaan D’Alia (`C10122`)

#### Model 1 Input

```json
{
  "customer_id": "C10122",
  "customer_name": "Ayaan D’Alia",
  "snapshot_date": "2026-05-01",
  "customer": {
    "age": 65,
    "tenure_months": 62,
    "customer_segment": "farmer",
    "income_regularity": "seasonal",
    "products_count": 1,
    "has_credit_card": 0,
    "has_loan": 0,
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
    "emi_bounce_30d": 0,
    "branch_code": "BR-110",
    "card_colour": "black"
  },
  "actual_next_month_churn": 0
}
```

#### Model 1 Output

```json
{
  "churn_probability": 3.74,
  "raw_churn_probability": 4.41,
  "risk_score": 11.21,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "card_spend_change_30d",
      "value": -31.6215
    },
    {
      "factor": "balance_change_30d",
      "value": -24.8127
    },
    {
      "factor": "tenure_months",
      "value": 62
    },
    {
      "factor": "age",
      "value": 65
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
  "churn_probability": 2.97,
  "raw_churn_probability": 27.14,
  "probability_mode": "sigmoid",
  "risk_score": 8.91,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "latest_balance_change_30d",
      "value": -24.8127,
      "message": "Balance has been falling across recent months.",
      "contribution": 0.15311937034130096
    },
    {
      "factor": "avg_card_spend_change_30d_3m",
      "value": -21.351066666666668,
      "message": "Card spending has been falling across recent months.",
      "contribution": 0.059115439653396606
    },
    {
      "factor": "latest_card_spend_change_30d",
      "value": -31.6215,
      "message": "Card spending has been falling across recent months.",
      "contribution": 0.04643790423870087
    },
    {
      "factor": "avg_card_spend_change_30d_6m",
      "value": -23.03612,
      "message": "Card spending has been falling across recent months.",
      "contribution": 0.04077627882361412
    },
    {
      "factor": "latest_app_login_change_30d",
      "value": -54.9605,
      "message": "App usage has been falling across recent months.",
      "contribution": 0.03200814127922058
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
  "snapshot_date": "2026-05-01",
  "customer": {
    "age": 54,
    "tenure_months": 107,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 3,
    "has_credit_card": 1,
    "has_loan": 1,
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
    "emi_bounce_30d": 0,
    "branch_code": "BR-101",
    "card_colour": "gold"
  },
  "actual_next_month_churn": 1
}
```

#### Model 1 Output

```json
{
  "churn_probability": 25.0,
  "raw_churn_probability": 28.05,
  "risk_score": 71.88,
  "churn_prediction": "Yes",
  "risk_level": "High",
  "top_risk_factors": [
    {
      "factor": "balance_change_30d",
      "value": -36.8811
    },
    {
      "factor": "salary_missing_days",
      "value": 7.0
    },
    {
      "factor": "card_spend_change_30d",
      "value": -31.1808
    },
    {
      "factor": "branch_code",
      "value": "BR-101"
    },
    {
      "factor": "failed_transactions_30d",
      "value": 2
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
  "churn_probability": 40.91,
  "raw_churn_probability": 94.12,
  "probability_mode": "sigmoid",
  "risk_score": 77.84,
  "churn_prediction": "Yes",
  "risk_level": "High",
  "top_risk_factors": [
    {
      "factor": "latest_days_since_last_transaction",
      "value": 14,
      "message": "Customer has gone longer without transacting.",
      "contribution": 0.47557100653648376
    },
    {
      "factor": "latest_salary_missing_days",
      "value": 7.0,
      "message": "This signal increased churn risk.",
      "contribution": 0.3064092993736267
    },
    {
      "factor": "max_salary_missing_days_3m",
      "value": 8.0,
      "message": "This signal increased churn risk.",
      "contribution": 0.28381168842315674
    },
    {
      "factor": "latest_vs_avg_upi_share_of_spend_available_history",
      "value": 0.05996,
      "message": "This signal increased churn risk.",
      "contribution": 0.25875455141067505
    },
    {
      "factor": "latest_balance_change_30d",
      "value": -36.8811,
      "message": "Balance has been falling across recent months.",
      "contribution": 0.21674835681915283
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
  "snapshot_date": "2026-05-01",
  "customer": {
    "age": 40,
    "tenure_months": 61,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 3,
    "has_credit_card": 1,
    "has_loan": 0,
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
    "emi_bounce_30d": 0,
    "branch_code": "BR-110",
    "card_colour": "blue"
  },
  "actual_next_month_churn": 1
}
```

#### Model 1 Output

```json
{
  "churn_probability": 18.06,
  "raw_churn_probability": 23.65,
  "risk_score": 62.22,
  "churn_prediction": "Yes",
  "risk_level": "Medium",
  "top_risk_factors": [
    {
      "factor": "card_spend_change_30d",
      "value": -48.4717
    },
    {
      "factor": "complaints_30d",
      "value": 3
    },
    {
      "factor": "balance_change_30d",
      "value": -25.8761
    },
    {
      "factor": "failed_transactions_30d",
      "value": 3
    },
    {
      "factor": "salary_missing_days",
      "value": 3.0
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
  "churn_probability": 29.7,
  "raw_churn_probability": 83.52,
  "probability_mode": "sigmoid",
  "risk_score": 73.64,
  "churn_prediction": "Yes",
  "risk_level": "High",
  "top_risk_factors": [
    {
      "factor": "latest_days_since_last_transaction",
      "value": 13,
      "message": "Customer has gone longer without transacting.",
      "contribution": 0.32638314366340637
    },
    {
      "factor": "latest_card_spend_change_30d",
      "value": -48.4717,
      "message": "Card spending has been falling across recent months.",
      "contribution": 0.18294228613376617
    },
    {
      "factor": "latest_salary_missing_days",
      "value": 3.0,
      "message": "This signal increased churn risk.",
      "contribution": 0.17253847420215607
    },
    {
      "factor": "latest_balance_change_30d",
      "value": -25.8761,
      "message": "Balance has been falling across recent months.",
      "contribution": 0.17177516222000122
    },
    {
      "factor": "days_since_last_transaction_trend_6m",
      "value": 1.7999999999999987,
      "message": "Customer has gone longer without transacting.",
      "contribution": 0.17051024734973907
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
  "snapshot_date": "2026-05-01",
  "customer": {
    "age": 47,
    "tenure_months": 53,
    "customer_segment": "vendor",
    "income_regularity": "irregular",
    "products_count": 2,
    "has_credit_card": 0,
    "has_loan": 1,
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
    "emi_bounce_30d": 0,
    "branch_code": "BR-129",
    "card_colour": "black"
  },
  "actual_next_month_churn": 1
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
      "factor": "branch_code",
      "value": "BR-129"
    },
    {
      "factor": "tenure_months",
      "value": 53
    },
    {
      "factor": "unresolved_complaints",
      "value": 1
    },
    {
      "factor": "external_transfer_change_30d",
      "value": 79.4736
    },
    {
      "factor": "customer_segment",
      "value": "vendor"
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
  "churn_probability": 9.32,
  "raw_churn_probability": 53.17,
  "probability_mode": "sigmoid",
  "risk_score": 27.97,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "latest_avg_resolution_time_hrs",
      "value": 40.909,
      "message": "This signal increased churn risk.",
      "contribution": 0.425851434469223
    },
    {
      "factor": "latest_external_transfer_change_30d",
      "value": 79.4736,
      "message": "External transfers have increased.",
      "contribution": 0.20929604768753052
    },
    {
      "factor": "count_balance_drop_6m",
      "value": 4,
      "message": "This signal increased churn risk.",
      "contribution": 0.06814339756965637
    },
    {
      "factor": "external_transfer_change_30d_trend_6m",
      "value": 18.276440000000004,
      "message": "External transfers have increased.",
      "contribution": 0.06701716780662537
    },
    {
      "factor": "latest_upi_share_of_spend",
      "value": 0.6192,
      "message": "This signal increased churn risk.",
      "contribution": 0.04334016144275665
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
  "snapshot_date": "2026-04-01",
  "customer": {
    "age": 54,
    "tenure_months": 82,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 1,
    "has_credit_card": 0,
    "has_loan": 0,
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
    "emi_bounce_30d": 0,
    "branch_code": "BR-109",
    "card_colour": "black"
  },
  "actual_next_month_churn": 1
}
```

#### Model 1 Output

```json
{
  "churn_probability": 16.1,
  "raw_churn_probability": 16.77,
  "risk_score": 54.41,
  "churn_prediction": "Yes",
  "risk_level": "Medium",
  "top_risk_factors": [
    {
      "factor": "card_spend_change_30d",
      "value": -42.1893
    },
    {
      "factor": "salary_missing_days",
      "value": 5.0
    },
    {
      "factor": "balance_change_30d",
      "value": -27.2062
    },
    {
      "factor": "failed_transactions_30d",
      "value": 3
    },
    {
      "factor": "days_since_last_transaction",
      "value": 14
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
  "churn_probability": 41.21,
  "raw_churn_probability": 94.39,
  "probability_mode": "sigmoid",
  "risk_score": 77.95,
  "churn_prediction": "Yes",
  "risk_level": "High",
  "top_risk_factors": [
    {
      "factor": "latest_days_since_last_transaction",
      "value": 14,
      "message": "Customer has gone longer without transacting.",
      "contribution": 0.454880952835083
    },
    {
      "factor": "latest_transaction_change_30d",
      "value": -46.3738,
      "message": "Transaction activity has been falling across recent months.",
      "contribution": 0.43597865104675293
    },
    {
      "factor": "latest_salary_missing_days",
      "value": 5.0,
      "message": "This signal increased churn risk.",
      "contribution": 0.2622058391571045
    },
    {
      "factor": "latest_vs_avg_upi_share_of_spend_available_history",
      "value": 0.1022499999999999,
      "message": "This signal increased churn risk.",
      "contribution": 0.24466447532176971
    },
    {
      "factor": "days_since_last_transaction_trend_6m",
      "value": 3.8000000000000007,
      "message": "Customer has gone longer without transacting.",
      "contribution": 0.22183264791965485
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
  "snapshot_date": "2026-05-01",
  "customer": {
    "age": 49,
    "tenure_months": 21,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 2,
    "has_credit_card": 0,
    "has_loan": 1,
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
    "emi_bounce_30d": 0,
    "branch_code": "BR-116",
    "card_colour": "silver"
  },
  "actual_next_month_churn": 0
}
```

#### Model 1 Output

```json
{
  "churn_probability": 1.96,
  "raw_churn_probability": 1.82,
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
      "value": 12.4461
    },
    {
      "factor": "upi_share_of_spend",
      "value": 0.2795
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
  "churn_probability": 2.84,
  "raw_churn_probability": 26.14,
  "probability_mode": "sigmoid",
  "risk_score": 8.52,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "days_since_last_transaction_trend_6m",
      "value": 1.499999999999999,
      "message": "Customer has gone longer without transacting.",
      "contribution": 0.10662141442298889
    },
    {
      "factor": "latest_vs_avg_external_transfer_change_30d_available_history",
      "value": -35.43164,
      "message": "This signal increased churn risk.",
      "contribution": 0.06865046173334122
    },
    {
      "factor": "sum_failed_transactions_30d_3m",
      "value": 4.0,
      "message": "Customer has recent failed transactions.",
      "contribution": 0.023496313020586967
    },
    {
      "factor": "avg_upi_share_of_spend_6m",
      "value": 0.26798,
      "message": "This signal increased churn risk.",
      "contribution": 0.01764862611889839
    },
    {
      "factor": "count_external_transfer_rise_6m",
      "value": 0,
      "message": "This signal increased churn risk.",
      "contribution": 0.01604391820728779
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
  "snapshot_date": "2026-02-01",
  "customer": {
    "age": 51,
    "tenure_months": 50,
    "customer_segment": "business",
    "income_regularity": "irregular",
    "products_count": 3,
    "has_credit_card": 1,
    "has_loan": 1,
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
    "emi_bounce_30d": 1,
    "branch_code": "BR-139",
    "card_colour": "silver"
  },
  "actual_next_month_churn": 1
}
```

#### Model 1 Output

```json
{
  "churn_probability": 9.94,
  "raw_churn_probability": 12.22,
  "risk_score": 29.81,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "avg_resolution_time_hrs",
      "value": 56.5525
    },
    {
      "factor": "complaints_30d",
      "value": 3
    },
    {
      "factor": "failed_transactions_30d",
      "value": 4
    },
    {
      "factor": "branch_code",
      "value": "BR-139"
    },
    {
      "factor": "tenure_months",
      "value": 50
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
  "churn_probability": 20.52,
  "raw_churn_probability": 72.94,
  "probability_mode": "sigmoid",
  "risk_score": 70.2,
  "churn_prediction": "Yes",
  "risk_level": "Medium",
  "top_risk_factors": [
    {
      "factor": "max_avg_resolution_time_hrs_3m",
      "value": 56.5525,
      "message": "This signal increased churn risk.",
      "contribution": 0.5337674617767334
    },
    {
      "factor": "latest_avg_resolution_time_hrs",
      "value": 56.5525,
      "message": "This signal increased churn risk.",
      "contribution": 0.30361446738243103
    },
    {
      "factor": "sum_failed_transactions_30d_3m",
      "value": 6.0,
      "message": "Customer has recent failed transactions.",
      "contribution": 0.1983717530965805
    },
    {
      "factor": "latest_failed_transactions_30d",
      "value": 4,
      "message": "Customer has recent failed transactions.",
      "contribution": 0.1507859081029892
    },
    {
      "factor": "latest_vs_avg_upi_share_of_spend_available_history",
      "value": 0.0484,
      "message": "This signal increased churn risk.",
      "contribution": 0.14834849536418915
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
  "snapshot_date": "2026-05-01",
  "customer": {
    "age": 78,
    "tenure_months": 214,
    "customer_segment": "pension",
    "income_regularity": "regular",
    "products_count": 1,
    "has_credit_card": 0,
    "has_loan": 0,
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
    "emi_bounce_30d": 0,
    "branch_code": "BR-133",
    "card_colour": "gold"
  },
  "actual_next_month_churn": 0
}
```

#### Model 1 Output

```json
{
  "churn_probability": 1.96,
  "raw_churn_probability": 2.08,
  "risk_score": 5.87,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "failed_transactions_30d",
      "value": 3
    },
    {
      "factor": "branch_code",
      "value": "BR-133"
    },
    {
      "factor": "app_login_change_30d",
      "value": 21.1746
    },
    {
      "factor": "age",
      "value": 78
    },
    {
      "factor": "upi_share_of_spend",
      "value": 0.0
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
  "churn_probability": 2.38,
  "raw_churn_probability": 22.29,
  "probability_mode": "sigmoid",
  "risk_score": 7.15,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "latest_upi_share_of_spend",
      "value": 0.0,
      "message": "This signal increased churn risk.",
      "contribution": 0.1428268998861313
    },
    {
      "factor": "latest_failed_transactions_30d",
      "value": 3,
      "message": "Customer has recent failed transactions.",
      "contribution": 0.0633123591542244
    },
    {
      "factor": "external_transfer_change_30d_trend_6m",
      "value": 2.71016,
      "message": "External transfers have increased.",
      "contribution": 0.03754734992980957
    },
    {
      "factor": "avg_upi_share_of_spend_6m",
      "value": 0.08954,
      "message": "This signal increased churn risk.",
      "contribution": 0.026309674605727196
    },
    {
      "factor": "sum_failed_transactions_30d_3m",
      "value": 4.0,
      "message": "Customer has recent failed transactions.",
      "contribution": 0.018789123743772507
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
  "snapshot_date": "2026-04-01",
  "customer": {
    "age": 66,
    "tenure_months": 125,
    "customer_segment": "pension",
    "income_regularity": "regular",
    "products_count": 3,
    "has_credit_card": 0,
    "has_loan": 1,
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
    "emi_bounce_30d": 0,
    "branch_code": "BR-120",
    "card_colour": "silver"
  },
  "actual_next_month_churn": 1
}
```

#### Model 1 Output

```json
{
  "churn_probability": 20.69,
  "raw_churn_probability": 26.36,
  "risk_score": 70.26,
  "churn_prediction": "Yes",
  "risk_level": "High",
  "top_risk_factors": [
    {
      "factor": "balance_change_30d",
      "value": -39.49
    },
    {
      "factor": "failed_transactions_30d",
      "value": 6
    },
    {
      "factor": "salary_missing_days",
      "value": 4.0
    },
    {
      "factor": "complaints_30d",
      "value": 3
    },
    {
      "factor": "card_spend_change_30d",
      "value": -25.0329
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
  "churn_probability": 34.91,
  "raw_churn_probability": 88.64,
  "probability_mode": "sigmoid",
  "risk_score": 75.59,
  "churn_prediction": "Yes",
  "risk_level": "High",
  "top_risk_factors": [
    {
      "factor": "max_avg_resolution_time_hrs_3m",
      "value": 65.7882,
      "message": "This signal increased churn risk.",
      "contribution": 0.3434170186519623
    },
    {
      "factor": "sum_failed_transactions_30d_3m",
      "value": 9.0,
      "message": "Customer has recent failed transactions.",
      "contribution": 0.28306111693382263
    },
    {
      "factor": "latest_salary_missing_days",
      "value": 4.0,
      "message": "This signal increased churn risk.",
      "contribution": 0.22338277101516724
    },
    {
      "factor": "latest_avg_resolution_time_hrs",
      "value": 39.8896,
      "message": "This signal increased churn risk.",
      "contribution": 0.20978176593780518
    },
    {
      "factor": "latest_balance_change_30d",
      "value": -39.49,
      "message": "Balance has been falling across recent months.",
      "contribution": 0.1590433567762375
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
  "snapshot_date": "2026-03-01",
  "customer": {
    "age": 42,
    "tenure_months": 41,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 2,
    "has_credit_card": 1,
    "has_loan": 0,
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
    "emi_bounce_30d": 0,
    "branch_code": "BR-133",
    "card_colour": "blue"
  },
  "actual_next_month_churn": 1
}
```

#### Model 1 Output

```json
{
  "churn_probability": 10.0,
  "raw_churn_probability": 13.2,
  "risk_score": 30.0,
  "churn_prediction": "Yes",
  "risk_level": "Medium",
  "top_risk_factors": [
    {
      "factor": "days_since_last_transaction",
      "value": 18
    },
    {
      "factor": "complaints_30d",
      "value": 2
    },
    {
      "factor": "failed_transactions_30d",
      "value": 3
    },
    {
      "factor": "branch_code",
      "value": "BR-133"
    },
    {
      "factor": "tenure_months",
      "value": 41
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
  "churn_probability": 35.84,
  "raw_churn_probability": 89.51,
  "probability_mode": "sigmoid",
  "risk_score": 75.94,
  "churn_prediction": "Yes",
  "risk_level": "High",
  "top_risk_factors": [
    {
      "factor": "latest_days_since_last_transaction",
      "value": 18,
      "message": "Customer has gone longer without transacting.",
      "contribution": 0.5735109448432922
    },
    {
      "factor": "latest_transaction_change_30d",
      "value": -25.4873,
      "message": "Transaction activity has been falling across recent months.",
      "contribution": 0.23606204986572266
    },
    {
      "factor": "latest_salary_missing_days",
      "value": 3.0,
      "message": "This signal increased churn risk.",
      "contribution": 0.2212715893983841
    },
    {
      "factor": "days_since_last_transaction_trend_6m",
      "value": 5.499999999999999,
      "message": "Customer has gone longer without transacting.",
      "contribution": 0.18350958824157715
    },
    {
      "factor": "latest_vs_avg_upi_share_of_spend_available_history",
      "value": 0.0703999999999999,
      "message": "This signal increased churn risk.",
      "contribution": 0.16546879708766937
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
  "snapshot_date": "2026-05-01",
  "customer": {
    "age": 40,
    "tenure_months": 45,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 2,
    "has_credit_card": 1,
    "has_loan": 0,
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
    "emi_bounce_30d": 0,
    "branch_code": "BR-105",
    "card_colour": "black"
  },
  "actual_next_month_churn": 0
}
```

#### Model 1 Output

```json
{
  "churn_probability": 7.29,
  "raw_churn_probability": 6.45,
  "risk_score": 21.86,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "fd_maturing_in_30d",
      "value": 1
    },
    {
      "factor": "failed_transactions_30d",
      "value": 3
    },
    {
      "factor": "tenure_months",
      "value": 45
    },
    {
      "factor": "branch_code",
      "value": "BR-105"
    },
    {
      "factor": "external_transfer_change_30d",
      "value": 2.2055
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
  "churn_probability": 3.28,
  "raw_churn_probability": 29.33,
  "probability_mode": "sigmoid",
  "risk_score": 9.83,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "latest_fd_maturing_in_30d",
      "value": 1,
      "message": "Customer has a fixed deposit maturing soon.",
      "contribution": 0.18135516345500946
    },
    {
      "factor": "sum_fd_maturing_in_30d_3m",
      "value": 1.0,
      "message": "Customer has a fixed deposit maturing soon.",
      "contribution": 0.09343000501394272
    },
    {
      "factor": "latest_failed_transactions_30d",
      "value": 3,
      "message": "Customer has recent failed transactions.",
      "contribution": 0.0925949439406395
    },
    {
      "factor": "latest_card_spend_change_30d",
      "value": -13.9221,
      "message": "Card spending has been falling across recent months.",
      "contribution": 0.020729830488562584
    },
    {
      "factor": "avg_upi_share_of_spend_6m",
      "value": 0.29434,
      "message": "This signal increased churn risk.",
      "contribution": 0.017041988670825958
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
  "snapshot_date": "2026-05-01",
  "customer": {
    "age": 36,
    "tenure_months": 51,
    "customer_segment": "business",
    "income_regularity": "irregular",
    "products_count": 1,
    "has_credit_card": 0,
    "has_loan": 0,
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
    "emi_bounce_30d": 0,
    "branch_code": "BR-124",
    "card_colour": "gold"
  },
  "actual_next_month_churn": 0
}
```

#### Model 1 Output

```json
{
  "churn_probability": 1.96,
  "raw_churn_probability": 2.39,
  "risk_score": 5.87,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "complaints_30d",
      "value": 2
    },
    {
      "factor": "tenure_months",
      "value": 51
    },
    {
      "factor": "upi_share_of_spend",
      "value": 0.209
    },
    {
      "factor": "external_transfer_change_30d",
      "value": 21.2957
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
  "churn_probability": 3.62,
  "raw_churn_probability": 31.51,
  "probability_mode": "sigmoid",
  "risk_score": 10.85,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "latest_avg_resolution_time_hrs",
      "value": 29.6081,
      "message": "This signal increased churn risk.",
      "contribution": 0.13767468929290771
    },
    {
      "factor": "external_transfer_change_30d_trend_6m",
      "value": 8.606550000000002,
      "message": "External transfers have increased.",
      "contribution": 0.04258709028363228
    },
    {
      "factor": "latest_card_spend_change_30d",
      "value": -12.5405,
      "message": "Card spending has been falling across recent months.",
      "contribution": 0.026713795959949493
    },
    {
      "factor": "avg_transaction_change_30d_6m",
      "value": 12.90454,
      "message": "This signal increased churn risk.",
      "contribution": 0.019563574343919754
    },
    {
      "factor": "latest_vs_avg_balance_change_30d_available_history",
      "value": -7.402260000000001,
      "message": "Balance has been falling across recent months.",
      "contribution": 0.01689467765390873
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
  "snapshot_date": "2026-05-01",
  "customer": {
    "age": 72,
    "tenure_months": 6,
    "customer_segment": "pension",
    "income_regularity": "regular",
    "products_count": 2,
    "has_credit_card": 1,
    "has_loan": 0,
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
    "emi_bounce_30d": 0,
    "branch_code": "BR-114",
    "card_colour": "black"
  },
  "actual_next_month_churn": 0
}
```

#### Model 1 Output

```json
{
  "churn_probability": 9.94,
  "raw_churn_probability": 12.93,
  "risk_score": 29.81,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "balance_change_30d",
      "value": -30.2961
    },
    {
      "factor": "tenure_months",
      "value": 6
    },
    {
      "factor": "avg_resolution_time_hrs",
      "value": 55.5174
    },
    {
      "factor": "fd_maturing_in_30d",
      "value": 1
    },
    {
      "factor": "unresolved_complaints",
      "value": 1
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
  "churn_probability": 25.51,
  "raw_churn_probability": 79.0,
  "probability_mode": "sigmoid",
  "risk_score": 72.07,
  "churn_prediction": "Yes",
  "risk_level": "High",
  "top_risk_factors": [
    {
      "factor": "max_avg_resolution_time_hrs_3m",
      "value": 126.7058,
      "message": "This signal increased churn risk.",
      "contribution": 0.5174546241760254
    },
    {
      "factor": "latest_avg_resolution_time_hrs",
      "value": 55.5174,
      "message": "This signal increased churn risk.",
      "contribution": 0.32501572370529175
    },
    {
      "factor": "sum_failed_transactions_30d_3m",
      "value": 8.0,
      "message": "Customer has recent failed transactions.",
      "contribution": 0.2845830023288727
    },
    {
      "factor": "latest_fd_maturing_in_30d",
      "value": 1,
      "message": "Customer has a fixed deposit maturing soon.",
      "contribution": 0.11224591732025146
    },
    {
      "factor": "sum_failed_transactions_30d_6m",
      "value": 12.0,
      "message": "Customer has recent failed transactions.",
      "contribution": 0.10969728976488113
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
  "snapshot_date": "2026-03-01",
  "customer": {
    "age": 39,
    "tenure_months": 26,
    "customer_segment": "vendor",
    "income_regularity": "irregular",
    "products_count": 2,
    "has_credit_card": 0,
    "has_loan": 1,
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
    "emi_bounce_30d": 0,
    "branch_code": "BR-140",
    "card_colour": "silver"
  },
  "actual_next_month_churn": 1
}
```

#### Model 1 Output

```json
{
  "churn_probability": 3.74,
  "raw_churn_probability": 4.96,
  "risk_score": 11.21,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "tenure_months",
      "value": 26
    },
    {
      "factor": "failed_transactions_30d",
      "value": 5
    },
    {
      "factor": "days_since_last_transaction",
      "value": 15
    },
    {
      "factor": "branch_code",
      "value": "BR-140"
    },
    {
      "factor": "customer_segment",
      "value": "vendor"
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
  "churn_probability": 16.77,
  "raw_churn_probability": 67.62,
  "probability_mode": "sigmoid",
  "risk_score": 57.09,
  "churn_prediction": "Yes",
  "risk_level": "Medium",
  "top_risk_factors": [
    {
      "factor": "latest_days_since_last_transaction",
      "value": 15,
      "message": "Customer has gone longer without transacting.",
      "contribution": 0.5256009697914124
    },
    {
      "factor": "sum_failed_transactions_30d_3m",
      "value": 7.0,
      "message": "Customer has recent failed transactions.",
      "contribution": 0.2498501092195511
    },
    {
      "factor": "days_since_last_transaction_trend_6m",
      "value": 3.999999999999999,
      "message": "Customer has gone longer without transacting.",
      "contribution": 0.12394356727600098
    },
    {
      "factor": "latest_failed_transactions_30d",
      "value": 5,
      "message": "Customer has recent failed transactions.",
      "contribution": 0.11997435241937637
    },
    {
      "factor": "transaction_change_30d_trend_6m",
      "value": -12.652050000000004,
      "message": "Transaction activity has been falling across recent months.",
      "contribution": 0.10796799510717392
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
  "snapshot_date": "2026-05-01",
  "customer": {
    "age": 43,
    "tenure_months": 28,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 1,
    "has_credit_card": 0,
    "has_loan": 0,
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
    "emi_bounce_30d": 0,
    "branch_code": "BR-110",
    "card_colour": "blue"
  },
  "actual_next_month_churn": 0
}
```

#### Model 1 Output

```json
{
  "churn_probability": 1.96,
  "raw_churn_probability": 2.5,
  "risk_score": 5.87,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "tenure_months",
      "value": 28
    },
    {
      "factor": "complaints_30d",
      "value": 2
    },
    {
      "factor": "unresolved_complaints",
      "value": 1
    },
    {
      "factor": "external_transfer_change_30d",
      "value": 7.6118
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
  "churn_probability": 4.14,
  "raw_churn_probability": 34.51,
  "probability_mode": "sigmoid",
  "risk_score": 12.41,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "latest_avg_resolution_time_hrs",
      "value": 40.5862,
      "message": "This signal increased churn risk.",
      "contribution": 0.33962664008140564
    },
    {
      "factor": "latest_upi_share_of_spend",
      "value": 0.5528,
      "message": "This signal increased churn risk.",
      "contribution": 0.035683631896972656
    },
    {
      "factor": "latest_card_spend_change_30d",
      "value": -11.9554,
      "message": "Card spending has been falling across recent months.",
      "contribution": 0.02153998427093029
    },
    {
      "factor": "transaction_change_30d_trend_6m",
      "value": -0.6916799999999997,
      "message": "Transaction activity has been falling across recent months.",
      "contribution": 0.01655220240354538
    },
    {
      "factor": "latest_complaints_30d",
      "value": 2,
      "message": "Customer has recent complaint activity.",
      "contribution": 0.014781713485717773
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
  "snapshot_date": "2026-05-01",
  "customer": {
    "age": 58,
    "tenure_months": 132,
    "customer_segment": "pension",
    "income_regularity": "regular",
    "products_count": 2,
    "has_credit_card": 1,
    "has_loan": 0,
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
    "emi_bounce_30d": 0,
    "branch_code": "BR-127",
    "card_colour": "black"
  },
  "actual_next_month_churn": 0
}
```

#### Model 1 Output

```json
{
  "churn_probability": 1.96,
  "raw_churn_probability": 2.5,
  "risk_score": 5.87,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "failed_transactions_30d",
      "value": 2
    },
    {
      "factor": "branch_code",
      "value": "BR-127"
    },
    {
      "factor": "external_transfer_change_30d",
      "value": 19.159
    },
    {
      "factor": "customer_segment",
      "value": "pension"
    },
    {
      "factor": "upi_share_of_spend",
      "value": 0.1062
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
  "churn_probability": 7.9,
  "raw_churn_probability": 49.28,
  "probability_mode": "sigmoid",
  "risk_score": 23.71,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "latest_avg_resolution_time_hrs",
      "value": 47.2211,
      "message": "This signal increased churn risk.",
      "contribution": 0.38921085000038147
    },
    {
      "factor": "latest_transaction_change_30d",
      "value": -22.3872,
      "message": "Transaction activity has been falling across recent months.",
      "contribution": 0.07185053825378418
    },
    {
      "factor": "max_avg_resolution_time_hrs_3m",
      "value": 47.2211,
      "message": "This signal increased churn risk.",
      "contribution": 0.05618193373084068
    },
    {
      "factor": "count_quiet_customer_3m",
      "value": 3,
      "message": "This signal increased churn risk.",
      "contribution": 0.04597211256623268
    },
    {
      "factor": "transaction_change_30d_trend_6m",
      "value": -8.235030000000002,
      "message": "Transaction activity has been falling across recent months.",
      "contribution": 0.044030483812093735
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
  "snapshot_date": "2026-02-01",
  "customer": {
    "age": 67,
    "tenure_months": 246,
    "customer_segment": "pension",
    "income_regularity": "regular",
    "products_count": 1,
    "has_credit_card": 0,
    "has_loan": 0,
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
    "emi_bounce_30d": 0,
    "branch_code": "BR-133",
    "card_colour": "gold"
  },
  "actual_next_month_churn": 1
}
```

#### Model 1 Output

```json
{
  "churn_probability": 1.96,
  "raw_churn_probability": 1.49,
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
      "value": 37.9743
    },
    {
      "factor": "age",
      "value": 67
    },
    {
      "factor": "products_count",
      "value": 1
    },
    {
      "factor": "external_transfer_change_30d",
      "value": 17.3803
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
  "churn_probability": 3.94,
  "raw_churn_probability": 33.43,
  "probability_mode": "sigmoid",
  "risk_score": 11.82,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "latest_vs_avg_upi_share_of_spend_available_history",
      "value": 0.0555999999999999,
      "message": "This signal increased churn risk.",
      "contribution": 0.18026947975158691
    },
    {
      "factor": "balance_change_30d_trend_6m",
      "value": 41.45399999999999,
      "message": "This signal increased churn risk.",
      "contribution": 0.1468019038438797
    },
    {
      "factor": "card_spend_change_30d_trend_6m",
      "value": 13.669699999999995,
      "message": "This signal increased churn risk.",
      "contribution": 0.06006110832095146
    },
    {
      "factor": "external_transfer_change_30d_trend_6m",
      "value": 10.606699999999991,
      "message": "External transfers have increased.",
      "contribution": 0.05246195197105408
    },
    {
      "factor": "transaction_change_30d_trend_6m",
      "value": -0.1820000000000033,
      "message": "Transaction activity has been falling across recent months.",
      "contribution": 0.0517866276204586
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
  "snapshot_date": "2026-05-01",
  "customer": {
    "age": 58,
    "tenure_months": 176,
    "customer_segment": "pension",
    "income_regularity": "regular",
    "products_count": 1,
    "has_credit_card": 0,
    "has_loan": 0,
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
    "emi_bounce_30d": 0,
    "branch_code": "BR-133",
    "card_colour": "blue"
  },
  "actual_next_month_churn": 0
}
```

#### Model 1 Output

```json
{
  "churn_probability": 2.39,
  "raw_churn_probability": 3.0,
  "risk_score": 7.18,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "branch_code",
      "value": "BR-133"
    },
    {
      "factor": "card_spend_change_30d",
      "value": -21.808
    },
    {
      "factor": "salary_missing_days",
      "value": 2.0
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
  "churn_probability": 3.19,
  "raw_churn_probability": 28.75,
  "probability_mode": "sigmoid",
  "risk_score": 9.58,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "sum_fd_maturing_in_30d_3m",
      "value": 1.0,
      "message": "Customer has a fixed deposit maturing soon.",
      "contribution": 0.07703860849142075
    },
    {
      "factor": "latest_salary_missing_days",
      "value": 2.0,
      "message": "This signal increased churn risk.",
      "contribution": 0.06958091259002686
    },
    {
      "factor": "latest_vs_avg_external_transfer_change_30d_available_history",
      "value": -46.26774,
      "message": "This signal increased churn risk.",
      "contribution": 0.06107153370976448
    },
    {
      "factor": "latest_vs_avg_upi_share_of_spend_available_history",
      "value": 0.0191999999999998,
      "message": "This signal increased churn risk.",
      "contribution": 0.03041810728609562
    },
    {
      "factor": "transaction_change_30d_trend_6m",
      "value": -0.8297899999999988,
      "message": "Transaction activity has been falling across recent months.",
      "contribution": 0.026684822514653206
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
  "snapshot_date": "2026-05-01",
  "customer": {
    "age": 50,
    "tenure_months": 111,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 1,
    "has_credit_card": 0,
    "has_loan": 0,
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
    "emi_bounce_30d": 0,
    "branch_code": "BR-108",
    "card_colour": "silver"
  },
  "actual_next_month_churn": 0
}
```

#### Model 1 Output

```json
{
  "churn_probability": 1.93,
  "raw_churn_probability": 1.34,
  "risk_score": 5.8,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "branch_code",
      "value": "BR-108"
    },
    {
      "factor": "app_login_change_30d",
      "value": 17.3358
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
  "churn_probability": 2.88,
  "raw_churn_probability": 26.49,
  "probability_mode": "sigmoid",
  "risk_score": 8.65,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "latest_vs_avg_upi_share_of_spend_available_history",
      "value": 0.06242,
      "message": "This signal increased churn risk.",
      "contribution": 0.12457484751939774
    },
    {
      "factor": "latest_vs_avg_card_spend_change_30d_available_history",
      "value": 32.5279,
      "message": "This signal increased churn risk.",
      "contribution": 0.11432057619094849
    },
    {
      "factor": "card_spend_change_30d_trend_6m",
      "value": 15.096170000000004,
      "message": "This signal increased churn risk.",
      "contribution": 0.07246963679790497
    },
    {
      "factor": "latest_upi_share_of_spend",
      "value": 0.5979,
      "message": "This signal increased churn risk.",
      "contribution": 0.06102463975548744
    },
    {
      "factor": "latest_card_spend_change_30d",
      "value": 52.0748,
      "message": "This signal increased churn risk.",
      "contribution": 0.04107455536723137
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
  "snapshot_date": "2026-05-01",
  "customer": {
    "age": 56,
    "tenure_months": 193,
    "customer_segment": "farmer",
    "income_regularity": "seasonal",
    "products_count": 3,
    "has_credit_card": 0,
    "has_loan": 0,
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
    "emi_bounce_30d": 0,
    "branch_code": "BR-105",
    "card_colour": "green"
  },
  "actual_next_month_churn": 0
}
```

#### Model 1 Output

```json
{
  "churn_probability": 1.96,
  "raw_churn_probability": 1.49,
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
      "value": 18.0811
    },
    {
      "factor": "external_transfer_change_30d",
      "value": 1.3504
    },
    {
      "factor": "card_colour",
      "value": "green"
    },
    {
      "factor": "upi_share_of_spend",
      "value": 0.3886
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
  "churn_probability": 2.09,
  "raw_churn_probability": 19.4,
  "probability_mode": "sigmoid",
  "risk_score": 6.27,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "latest_vs_avg_card_spend_change_30d_available_history",
      "value": 31.26424,
      "message": "This signal increased churn risk.",
      "contribution": 0.04996977373957634
    },
    {
      "factor": "card_spend_change_30d_trend_6m",
      "value": 12.74505,
      "message": "This signal increased churn risk.",
      "contribution": 0.03705377131700516
    },
    {
      "factor": "latest_vs_avg_upi_share_of_spend_available_history",
      "value": 0.0042599999999999,
      "message": "This signal increased churn risk.",
      "contribution": 0.02150551974773407
    },
    {
      "factor": "count_product_drop_month_6m",
      "value": 1,
      "message": "This signal increased churn risk.",
      "contribution": 0.004735826049000025
    },
    {
      "factor": "sum_products_dropped_90d_6m",
      "value": 1.0,
      "message": "This signal increased churn risk.",
      "contribution": 0.004124809522181749
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
  "snapshot_date": "2026-03-01",
  "customer": {
    "age": 29,
    "tenure_months": 111,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 2,
    "has_credit_card": 0,
    "has_loan": 1,
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
    "emi_bounce_30d": 0,
    "branch_code": "BR-116",
    "card_colour": "green"
  },
  "actual_next_month_churn": 1
}
```

#### Model 1 Output

```json
{
  "churn_probability": 3.74,
  "raw_churn_probability": 5.32,
  "risk_score": 11.21,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "days_since_last_transaction",
      "value": 20
    },
    {
      "factor": "salary_missing_days",
      "value": 3.0
    },
    {
      "factor": "external_transfer_change_30d",
      "value": 60.3833
    },
    {
      "factor": "balance_change_30d",
      "value": -20.6274
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
  "churn_probability": 28.75,
  "raw_churn_probability": 82.53,
  "probability_mode": "sigmoid",
  "risk_score": 73.28,
  "churn_prediction": "Yes",
  "risk_level": "High",
  "top_risk_factors": [
    {
      "factor": "latest_days_since_last_transaction",
      "value": 20,
      "message": "Customer has gone longer without transacting.",
      "contribution": 0.6554021239280701
    },
    {
      "factor": "latest_salary_missing_days",
      "value": 3.0,
      "message": "This signal increased churn risk.",
      "contribution": 0.24392713606357574
    },
    {
      "factor": "days_since_last_transaction_trend_6m",
      "value": 6.9999999999999964,
      "message": "Customer has gone longer without transacting.",
      "contribution": 0.21786455810070038
    },
    {
      "factor": "latest_vs_avg_upi_share_of_spend_available_history",
      "value": 0.0566999999999999,
      "message": "This signal increased churn risk.",
      "contribution": 0.21705107390880585
    },
    {
      "factor": "transaction_change_30d_trend_6m",
      "value": -17.64835,
      "message": "Transaction activity has been falling across recent months.",
      "contribution": 0.13982868194580078
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
  "snapshot_date": "2026-05-01",
  "customer": {
    "age": 79,
    "tenure_months": 204,
    "customer_segment": "pension",
    "income_regularity": "regular",
    "products_count": 2,
    "has_credit_card": 1,
    "has_loan": 0,
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
    "emi_bounce_30d": 0,
    "branch_code": "BR-112",
    "card_colour": "black"
  },
  "actual_next_month_churn": 1
}
```

#### Model 1 Output

```json
{
  "churn_probability": 1.96,
  "raw_churn_probability": 1.71,
  "risk_score": 5.87,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
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
      "value": 23.7161
    },
    {
      "factor": "upi_share_of_spend",
      "value": 0.1859
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
  "churn_probability": 3.0,
  "raw_churn_probability": 27.33,
  "probability_mode": "sigmoid",
  "risk_score": 8.99,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "latest_vs_avg_balance_change_30d_available_history",
      "value": 23.86004,
      "message": "This signal increased churn risk.",
      "contribution": 0.09281963855028152
    },
    {
      "factor": "sum_fd_maturing_in_30d_3m",
      "value": 1.0,
      "message": "Customer has a fixed deposit maturing soon.",
      "contribution": 0.0669441893696785
    },
    {
      "factor": "max_salary_missing_days_6m",
      "value": 0.0,
      "message": "This signal increased churn risk.",
      "contribution": 0.046195078641176224
    },
    {
      "factor": "avg_app_login_change_30d_6m",
      "value": -0.77896,
      "message": "App usage has been falling across recent months.",
      "contribution": 0.03269102796912193
    },
    {
      "factor": "avg_app_login_change_30d_3m",
      "value": -3.847899999999999,
      "message": "App usage has been falling across recent months.",
      "contribution": 0.032441530376672745
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
  "snapshot_date": "2026-04-01",
  "customer": {
    "age": 44,
    "tenure_months": 60,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 3,
    "has_credit_card": 0,
    "has_loan": 1,
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
    "emi_bounce_30d": 1,
    "branch_code": "BR-134",
    "card_colour": "green"
  },
  "actual_next_month_churn": 1
}
```

#### Model 1 Output

```json
{
  "churn_probability": 7.41,
  "raw_churn_probability": 9.29,
  "risk_score": 22.22,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "avg_resolution_time_hrs",
      "value": 90.1903
    },
    {
      "factor": "complaints_30d",
      "value": 3
    },
    {
      "factor": "unresolved_complaints",
      "value": 3
    },
    {
      "factor": "emi_bounce_30d",
      "value": 1
    },
    {
      "factor": "app_login_change_30d",
      "value": 39.4359
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
  "churn_probability": 26.6,
  "raw_churn_probability": 80.22,
  "probability_mode": "sigmoid",
  "risk_score": 72.47,
  "churn_prediction": "Yes",
  "risk_level": "High",
  "top_risk_factors": [
    {
      "factor": "max_avg_resolution_time_hrs_3m",
      "value": 90.1903,
      "message": "This signal increased churn risk.",
      "contribution": 0.592974841594696
    },
    {
      "factor": "latest_avg_resolution_time_hrs",
      "value": 90.1903,
      "message": "This signal increased churn risk.",
      "contribution": 0.44119343161582947
    },
    {
      "factor": "sum_failed_transactions_30d_3m",
      "value": 8.0,
      "message": "Customer has recent failed transactions.",
      "contribution": 0.4025602340698242
    },
    {
      "factor": "sum_failed_transactions_30d_6m",
      "value": 8.0,
      "message": "Customer has recent failed transactions.",
      "contribution": 0.171050027012825
    },
    {
      "factor": "sum_complaints_30d_6m",
      "value": 11.0,
      "message": "Customer has recent complaint activity.",
      "contribution": 0.13503865897655487
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
  "snapshot_date": "2026-05-01",
  "customer": {
    "age": 24,
    "tenure_months": 25,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 1,
    "has_credit_card": 0,
    "has_loan": 0,
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
    "emi_bounce_30d": 0,
    "branch_code": "BR-113",
    "card_colour": "silver"
  },
  "actual_next_month_churn": 0
}
```

#### Model 1 Output

```json
{
  "churn_probability": 2.25,
  "raw_churn_probability": 2.69,
  "risk_score": 6.74,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "tenure_months",
      "value": 25
    },
    {
      "factor": "age",
      "value": 24
    },
    {
      "factor": "days_since_last_transaction",
      "value": 14
    },
    {
      "factor": "salary_missing_days",
      "value": 2.0
    },
    {
      "factor": "app_login_change_30d",
      "value": 21.2897
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
  "churn_probability": 8.86,
  "raw_churn_probability": 51.95,
  "probability_mode": "sigmoid",
  "risk_score": 26.58,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "latest_days_since_last_transaction",
      "value": 14,
      "message": "Customer has gone longer without transacting.",
      "contribution": 0.4569288492202759
    },
    {
      "factor": "latest_vs_avg_upi_share_of_spend_available_history",
      "value": 0.0847,
      "message": "This signal increased churn risk.",
      "contribution": 0.14435051381587982
    },
    {
      "factor": "days_since_last_transaction_trend_6m",
      "value": 1.499999999999999,
      "message": "Customer has gone longer without transacting.",
      "contribution": 0.10242065042257309
    },
    {
      "factor": "count_balance_drop_3m",
      "value": 3,
      "message": "This signal increased churn risk.",
      "contribution": 0.0618261992931366
    },
    {
      "factor": "count_quiet_customer_3m",
      "value": 3,
      "message": "This signal increased churn risk.",
      "contribution": 0.04218319430947304
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
  "snapshot_date": "2026-05-01",
  "customer": {
    "age": 42,
    "tenure_months": 70,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 2,
    "has_credit_card": 0,
    "has_loan": 0,
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
    "emi_bounce_30d": 0,
    "branch_code": "BR-105",
    "card_colour": "black"
  },
  "actual_next_month_churn": 0
}
```

#### Model 1 Output

```json
{
  "churn_probability": 1.96,
  "raw_churn_probability": 1.99,
  "risk_score": 5.87,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "fd_maturing_in_30d",
      "value": 1
    },
    {
      "factor": "branch_code",
      "value": "BR-105"
    },
    {
      "factor": "external_transfer_change_30d",
      "value": 14.5088
    },
    {
      "factor": "app_login_change_30d",
      "value": 21.2478
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
  "churn_probability": 3.71,
  "raw_churn_probability": 32.11,
  "probability_mode": "sigmoid",
  "risk_score": 11.14,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "latest_fd_maturing_in_30d",
      "value": 1,
      "message": "Customer has a fixed deposit maturing soon.",
      "contribution": 0.19435255229473114
    },
    {
      "factor": "sum_fd_maturing_in_30d_3m",
      "value": 1.0,
      "message": "Customer has a fixed deposit maturing soon.",
      "contribution": 0.06045542657375336
    },
    {
      "factor": "external_transfer_change_30d_trend_6m",
      "value": 0.6327299999999997,
      "message": "External transfers have increased.",
      "contribution": 0.0340721569955349
    },
    {
      "factor": "max_avg_resolution_time_hrs_3m",
      "value": 45.6093,
      "message": "This signal increased churn risk.",
      "contribution": 0.031836654990911484
    },
    {
      "factor": "count_external_transfer_rise_6m",
      "value": 0,
      "message": "This signal increased churn risk.",
      "contribution": 0.014462434686720371
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
  "snapshot_date": "2026-05-01",
  "customer": {
    "age": 64,
    "tenure_months": 193,
    "customer_segment": "farmer",
    "income_regularity": "seasonal",
    "products_count": 2,
    "has_credit_card": 0,
    "has_loan": 1,
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
    "emi_bounce_30d": 0,
    "branch_code": "BR-112",
    "card_colour": "green"
  },
  "actual_next_month_churn": 0
}
```

#### Model 1 Output

```json
{
  "churn_probability": 9.94,
  "raw_churn_probability": 10.78,
  "risk_score": 29.81,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "balance_change_30d",
      "value": -30.6688
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
      "factor": "branch_code",
      "value": "BR-112"
    },
    {
      "factor": "age",
      "value": 64
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
  "churn_probability": 5.97,
  "raw_churn_probability": 42.79,
  "probability_mode": "sigmoid",
  "risk_score": 17.9,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "latest_balance_change_30d",
      "value": -30.6688,
      "message": "Balance has been falling across recent months.",
      "contribution": 0.1575489193201065
    },
    {
      "factor": "count_balance_drop_3m",
      "value": 3,
      "message": "This signal increased churn risk.",
      "contribution": 0.10127264261245728
    },
    {
      "factor": "latest_fd_maturing_in_30d",
      "value": 1,
      "message": "Customer has a fixed deposit maturing soon.",
      "contribution": 0.09451526403427124
    },
    {
      "factor": "count_balance_drop_6m",
      "value": 5,
      "message": "This signal increased churn risk.",
      "contribution": 0.08114857226610184
    },
    {
      "factor": "sum_fd_maturing_in_30d_3m",
      "value": 1.0,
      "message": "Customer has a fixed deposit maturing soon.",
      "contribution": 0.07523081451654434
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
  "snapshot_date": "2026-05-01",
  "customer": {
    "age": 47,
    "tenure_months": 66,
    "customer_segment": "business",
    "income_regularity": "irregular",
    "products_count": 2,
    "has_credit_card": 1,
    "has_loan": 0,
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
    "emi_bounce_30d": 0,
    "branch_code": "BR-110",
    "card_colour": "green"
  },
  "actual_next_month_churn": 0
}
```

#### Model 1 Output

```json
{
  "churn_probability": 0.0,
  "raw_churn_probability": 0.93,
  "risk_score": 0.0,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "app_login_change_30d",
      "value": 42.7602
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
      "factor": "card_colour",
      "value": "green"
    },
    {
      "factor": "has_credit_card",
      "value": 1
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
  "churn_probability": 2.58,
  "raw_churn_probability": 24.03,
  "probability_mode": "sigmoid",
  "risk_score": 7.74,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "latest_vs_avg_external_transfer_change_30d_available_history",
      "value": -32.4703,
      "message": "This signal increased churn risk.",
      "contribution": 0.09162018448114395
    },
    {
      "factor": "avg_balance_change_30d_3m",
      "value": 36.74123333333333,
      "message": "This signal increased churn risk.",
      "contribution": 0.06509826332330704
    },
    {
      "factor": "card_spend_change_30d_trend_6m",
      "value": 6.78282,
      "message": "This signal increased churn risk.",
      "contribution": 0.04742797836661339
    },
    {
      "factor": "avg_transaction_change_30d_6m",
      "value": 12.93008,
      "message": "This signal increased churn risk.",
      "contribution": 0.019034581258893013
    },
    {
      "factor": "latest_upi_share_of_spend",
      "value": 0.505,
      "message": "This signal increased churn risk.",
      "contribution": 0.016867712140083313
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
  "snapshot_date": "2026-05-01",
  "customer": {
    "age": 41,
    "tenure_months": 42,
    "customer_segment": "business",
    "income_regularity": "irregular",
    "products_count": 2,
    "has_credit_card": 1,
    "has_loan": 0,
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
    "emi_bounce_30d": 0,
    "branch_code": "BR-124",
    "card_colour": "black"
  },
  "actual_next_month_churn": 0
}
```

#### Model 1 Output

```json
{
  "churn_probability": 1.96,
  "raw_churn_probability": 1.86,
  "risk_score": 5.87,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "tenure_months",
      "value": 42
    },
    {
      "factor": "failed_transactions_30d",
      "value": 2
    },
    {
      "factor": "external_transfer_change_30d",
      "value": 25.1169
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
  "churn_probability": 2.77,
  "raw_churn_probability": 25.61,
  "probability_mode": "sigmoid",
  "risk_score": 8.31,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "latest_vs_avg_upi_share_of_spend_available_history",
      "value": 0.03748,
      "message": "This signal increased churn risk.",
      "contribution": 0.09259944409132004
    },
    {
      "factor": "latest_vs_avg_balance_change_30d_available_history",
      "value": -10.69514,
      "message": "Balance has been falling across recent months.",
      "contribution": 0.018045654520392418
    },
    {
      "factor": "transaction_change_30d_trend_6m",
      "value": -2.046280000000002,
      "message": "Transaction activity has been falling across recent months.",
      "contribution": 0.01569320075213909
    },
    {
      "factor": "avg_app_login_change_30d_6m",
      "value": -3.57946,
      "message": "App usage has been falling across recent months.",
      "contribution": 0.014115337282419205
    },
    {
      "factor": "avg_app_login_change_30d_3m",
      "value": -4.203500000000001,
      "message": "App usage has been falling across recent months.",
      "contribution": 0.00999471265822649
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
  "snapshot_date": "2026-05-01",
  "customer": {
    "age": 26,
    "tenure_months": 40,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 2,
    "has_credit_card": 0,
    "has_loan": 1,
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
    "emi_bounce_30d": 0,
    "branch_code": "BR-117",
    "card_colour": "silver"
  },
  "actual_next_month_churn": 0
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
      "factor": "tenure_months",
      "value": 40
    },
    {
      "factor": "age",
      "value": 26
    },
    {
      "factor": "upi_share_of_spend",
      "value": 0.2239
    },
    {
      "factor": "app_login_change_30d",
      "value": 10.3828
    },
    {
      "factor": "external_transfer_change_30d",
      "value": 17.7301
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
  "churn_probability": 2.6,
  "raw_churn_probability": 24.23,
  "probability_mode": "sigmoid",
  "risk_score": 7.81,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "latest_card_spend_change_30d",
      "value": -11.955,
      "message": "Card spending has been falling across recent months.",
      "contribution": 0.020617855712771416
    },
    {
      "factor": "latest_vs_avg_balance_change_30d_available_history",
      "value": -6.407339999999999,
      "message": "Balance has been falling across recent months.",
      "contribution": 0.017026590183377266
    },
    {
      "factor": "latest_vs_avg_upi_share_of_spend_available_history",
      "value": 0.0197999999999999,
      "message": "This signal increased churn risk.",
      "contribution": 0.013923396356403828
    },
    {
      "factor": "max_salary_missing_days_6m",
      "value": 0.0,
      "message": "This signal increased churn risk.",
      "contribution": 0.010414511896669865
    },
    {
      "factor": "avg_upi_share_of_spend_6m",
      "value": 0.2041,
      "message": "This signal increased churn risk.",
      "contribution": 0.009936697781085968
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
  "snapshot_date": "2026-05-01",
  "customer": {
    "age": 72,
    "tenure_months": 137,
    "customer_segment": "pension",
    "income_regularity": "regular",
    "products_count": 2,
    "has_credit_card": 1,
    "has_loan": 0,
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
    "emi_bounce_30d": 0,
    "branch_code": "BR-118",
    "card_colour": "gold"
  },
  "actual_next_month_churn": 0
}
```

#### Model 1 Output

```json
{
  "churn_probability": 1.96,
  "raw_churn_probability": 2.37,
  "risk_score": 5.87,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "card_spend_change_30d",
      "value": -24.8147
    },
    {
      "factor": "days_since_last_transaction",
      "value": 15
    },
    {
      "factor": "salary_missing_days",
      "value": 2.0
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
  "churn_probability": 3.85,
  "raw_churn_probability": 32.93,
  "probability_mode": "sigmoid",
  "risk_score": 11.56,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "latest_days_since_last_transaction",
      "value": 15,
      "message": "Customer has gone longer without transacting.",
      "contribution": 0.4480477273464203
    },
    {
      "factor": "latest_external_transfer_change_30d",
      "value": 75.9525,
      "message": "External transfers have increased.",
      "contribution": 0.10313663631677628
    },
    {
      "factor": "days_since_last_transaction_trend_6m",
      "value": 2.3,
      "message": "Customer has gone longer without transacting.",
      "contribution": 0.10294529050588608
    },
    {
      "factor": "count_balance_drop_6m",
      "value": 4,
      "message": "This signal increased churn risk.",
      "contribution": 0.03265073895454407
    },
    {
      "factor": "external_transfer_change_30d_trend_6m",
      "value": 4.400659999999993,
      "message": "External transfers have increased.",
      "contribution": 0.020924298092722893
    }
  ]
}
```
