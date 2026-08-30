# Model 1 vs Model 1 v2 Report

- Created at: `2026-08-30T18:37:47`
- Customers tested: `100`

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
| 1 | Ayushman Chander (`C10003`) | 7.29% | 4.39% | 1 | 1 |
| 2 | Yashica Issac (`C10040`) | 2.39% | 3.18% | 0 | 0 |
| 3 | Baghyawati Kade (`C10098`) | 3.74% | 31.4% | 1 | 1 |
| 4 | Ayaan D’Alia (`C10122`) | 1.65% | 2.34% | 0 | 0 |
| 5 | Azad Chander (`C10736`) | 1.65% | 2.62% | 0 | 0 |
| 6 | Theodore Bahri (`C11005`) | 100.0% | 46.78% | 1 | 1 |
| 7 | Aadi Narula (`C11006`) | 1.96% | 1.85% | 0 | 0 |
| 8 | Matthew Chatterjee (`C11056`) | 1.93% | 1.89% | 0 | 0 |
| 9 | Vrishti Parmer (`C11153`) | 18.06% | 9.56% | 1 | 1 |
| 10 | Nakul Pathak (`C11345`) | 18.06% | 18.3% | 0 | 0 |
| 11 | Edhitha Palan (`C11532`) | 100.0% | 34.32% | 1 | 1 |
| 12 | Max Om (`C11635`) | 2.39% | 4.6% | 0 | 0 |
| 13 | Prisha Ravel (`C11661`) | 18.06% | 7.88% | 1 | 1 |
| 14 | Oliver Kade (`C11837`) | 1.96% | 8.94% | 1 | 1 |
| 15 | Gagan Vala (`C12027`) | 36.3% | 39.61% | 0 | 0 |
| 16 | Naveen Tella (`C12090`) | 48.15% | 47.78% | 0 | 0 |
| 17 | Qasim Sarraf (`C12096`) | 36.3% | 5.65% | 1 | 1 |
| 18 | Bahadurjit Mahal (`C12211`) | 1.96% | 3.08% | 0 | 0 |
| 19 | Girish Bhargava (`C12247`) | 3.74% | 3.87% | 0 | 0 |
| 20 | Mugdha Sunder (`C12336`) | 1.96% | 2.02% | 0 | 0 |
| 21 | Amrita Sahni (`C12339`) | 18.06% | 2.8% | 0 | 0 |
| 22 | Madhavi Date (`C12391`) | 81.4% | 46.14% | 1 | 1 |
| 23 | Netra Ravi (`C12607`) | 1.96% | 2.77% | 0 | 0 |
| 24 | Lohit Jayaraman (`C12715`) | 16.1% | 21.95% | 1 | 1 |
| 25 | Shivansh Kar (`C12820`) | 1.96% | 2.64% | 0 | 0 |
| 26 | Shaurya Kamdar (`C12831`) | 1.96% | 1.38% | 0 | 0 |
| 27 | Qasim Ravi (`C12850`) | 1.96% | 5.25% | 0 | 0 |
| 28 | Madhavi Rattan (`C12991`) | 1.96% | 1.84% | 0 | 0 |
| 29 | Tara Sangha (`C13175`) | 1.96% | 19.52% | 0 | 0 |
| 30 | Chanchal Anne (`C13220`) | 1.96% | 1.26% | 0 | 0 |
| 31 | Dhriti Thakur (`C13379`) | 70.37% | 46.44% | 1 | 1 |
| 32 | Hredhaan Shetty (`C13411`) | 1.96% | 1.88% | 0 | 0 |
| 33 | Xiti Pandey (`C13447`) | 0.0% | 1.95% | 0 | 0 |
| 34 | Tamanna Murty (`C13555`) | 100.0% | 39.32% | 1 | 1 |
| 35 | Sudiksha Merchant (`C13601`) | 3.74% | 2.36% | 0 | 0 |
| 36 | Advika Nadkarni (`C13635`) | 1.96% | 16.53% | 0 | 0 |
| 37 | Anmol Bail (`C13643`) | 7.29% | 9.7% | 0 | 0 |
| 38 | Jatin Purohit (`C13656`) | 53.49% | 39.93% | 1 | 1 |
| 39 | Viraj Bhargava (`C13678`) | 1.96% | 2.05% | 0 | 0 |
| 40 | Abha Yogi (`C13919`) | 1.96% | 3.12% | 0 | 0 |
| 41 | Anvi Banik (`C13933`) | 1.96% | 3.35% | 0 | 0 |
| 42 | Falak Lad (`C14018`) | 1.96% | 22.24% | 0 | 0 |
| 43 | Ishanvi Bose (`C14204`) | 2.39% | 3.4% | 0 | 0 |
| 44 | Urvi Devi (`C14228`) | 1.96% | 2.4% | 0 | 0 |
| 45 | Sara Dada (`C14252`) | 48.15% | 22.42% | 1 | 1 |
| 46 | Ethan Bahri (`C14321`) | 36.3% | 28.23% | 0 | 0 |
| 47 | Tanay Ramaswamy (`C14341`) | 1.96% | 7.46% | 0 | 0 |
| 48 | Gautami Peri (`C14388`) | 9.94% | 17.12% | 1 | 1 |
| 49 | Viraj Kade (`C14404`) | 1.96% | 4.3% | 0 | 0 |
| 50 | Jatin Borra (`C14412`) | 3.74% | 13.66% | 1 | 1 |
| 51 | Kevin Taneja (`C14491`) | 1.96% | 4.67% | 0 | 0 |
| 52 | Vrinda Mahal (`C14979`) | 48.15% | 36.85% | 0 | 0 |
| 53 | Pooja Atwal (`C14986`) | 1.96% | 2.03% | 0 | 0 |
| 54 | Varenya Rana (`C15055`) | 1.96% | 1.46% | 0 | 0 |
| 55 | Wyatt Modi (`C15182`) | 2.39% | 4.15% | 0 | 0 |
| 56 | Chanchal Khanna (`C15184`) | 95.65% | 30.12% | 1 | 1 |
| 57 | Hemal Wagle (`C15335`) | 36.3% | 4.07% | 1 | 1 |
| 58 | Urvashi Bhasin (`C15360`) | 100.0% | 40.0% | 1 | 1 |
| 59 | Raagini Rai (`C15469`) | 9.94% | 3.7% | 1 | 1 |
| 60 | Krisha Rajagopal (`C15597`) | 7.29% | 7.94% | 0 | 0 |
| 61 | Vasana Talwar (`C15682`) | 3.74% | 2.44% | 1 | 1 |
| 62 | Ekalinga Ram (`C15711`) | 1.96% | 2.7% | 0 | 0 |
| 63 | Karan De (`C15967`) | 95.65% | 35.0% | 1 | 1 |
| 64 | Robert Sidhu (`C16060`) | 36.3% | 18.74% | 1 | 1 |
| 65 | Urvi Kapadia (`C16084`) | 1.96% | 1.74% | 0 | 0 |
| 66 | Aradhana Soni (`C16121`) | 20.69% | 19.83% | 1 | 1 |
| 67 | Neel Wadhwa (`C16175`) | 1.96% | 1.89% | 0 | 0 |
| 68 | Nikita Dugar (`C16218`) | 4.11% | 4.3% | 1 | 1 |
| 69 | Charvi Kata (`C16223`) | 1.96% | 1.68% | 0 | 0 |
| 70 | Devansh Bath (`C16345`) | 36.3% | 41.01% | 1 | 1 |
| 71 | David Bhasin (`C16363`) | 0.0% | 2.29% | 0 | 0 |
| 72 | Benjamin Narayan (`C16421`) | 1.65% | 2.13% | 0 | 0 |
| 73 | Diya Chandra (`C16671`) | 1.96% | 1.88% | 0 | 0 |
| 74 | Elijah Mitra (`C16902`) | 45.95% | 31.89% | 1 | 1 |
| 75 | Unnati Date (`C17033`) | 53.49% | 12.47% | 1 | 1 |
| 76 | Jai Apte (`C17372`) | 1.96% | 5.6% | 0 | 0 |
| 77 | Charles Khanna (`C17462`) | 1.96% | 3.58% | 0 | 0 |
| 78 | Chaman Kalita (`C17484`) | 1.96% | 1.62% | 0 | 0 |
| 79 | Amara Parikh (`C17639`) | 2.25% | 2.47% | 1 | 1 |
| 80 | Hemangini Nazareth (`C17880`) | 1.96% | 2.73% | 0 | 0 |
| 81 | Nikita Ganguly (`C17907`) | 16.1% | 27.49% | 1 | 1 |
| 82 | Sneha Mahajan (`C17950`) | 2.39% | 8.65% | 0 | 0 |
| 83 | Xiti Bath (`C17993`) | 41.38% | 24.14% | 0 | 0 |
| 84 | Ethan Bhasin (`C18023`) | 3.74% | 2.23% | 0 | 0 |
| 85 | Thomas Kothari (`C18055`) | 1.96% | 3.46% | 0 | 0 |
| 86 | Warda Kalita (`C18307`) | 2.39% | 5.69% | 0 | 0 |
| 87 | Arin Pandya (`C18434`) | 0.0% | 1.87% | 0 | 0 |
| 88 | Mugdha Rajagopal (`C18699`) | 70.37% | 42.95% | 1 | 1 |
| 89 | Lavanya Andra (`C18807`) | 1.96% | 7.6% | 0 | 0 |
| 90 | Ojas Borra (`C18976`) | 7.29% | 7.24% | 1 | 1 |
| 91 | Christopher Sarma (`C19096`) | 36.3% | 18.11% | 1 | 1 |
| 92 | Pooja Bawa (`C19159`) | 1.96% | 3.35% | 1 | 1 |
| 93 | Anirudh Shukla (`C19179`) | 1.93% | 2.34% | 0 | 0 |
| 94 | Ekaraj Gokhale (`C19185`) | 1.96% | 2.46% | 0 | 0 |
| 95 | Aadhya Pal (`C19311`) | 1.96% | 1.92% | 0 | 0 |
| 96 | Irya Ramakrishnan (`C19406`) | 7.29% | 3.64% | 0 | 0 |
| 97 | Hredhaan Bakshi (`C19434`) | 70.37% | 28.04% | 1 | 1 |
| 98 | Niharika Oommen (`C19448`) | 100.0% | 41.56% | 1 | 1 |
| 99 | Aarini Dar (`C19761`) | 1.96% | 2.28% | 0 | 0 |
| 100 | Krish Butala (`C19961`) | 1.96% | 2.0% | 0 | 0 |

## Customer Details

### 1. Ayushman Chander (`C10003`)

#### Model 1 Input

```json
{
  "customer_id": "C10003",
  "customer_name": "Ayushman Chander",
  "snapshot_date": "2026-02-01",
  "customer": {
    "age": 25,
    "tenure_months": 39,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 2,
    "has_credit_card": 0,
    "has_loan": 1,
    "days_since_last_transaction": 9,
    "balance_change_30d": -3.2693,
    "transaction_change_30d": -20.1397,
    "card_spend_change_30d": -27.851,
    "app_login_change_30d": -6.6912,
    "salary_missing_days": 2.0,
    "external_transfer_change_30d": -3.9446,
    "upi_share_of_spend": 0.3626,
    "fd_maturing_in_30d": 0,
    "products_dropped_90d": 0,
    "complaints_30d": 1,
    "unresolved_complaints": 0,
    "failed_transactions_30d": 0,
    "avg_resolution_time_hrs": 51.3418,
    "emi_bounce_30d": 0,
    "branch_code": "BR-137",
    "card_colour": "silver"
  },
  "actual_current_month_churn": 1
}
```

#### Model 1 Output

```json
{
  "churn_probability": 7.29,
  "raw_churn_probability": 6.17,
  "risk_score": 21.86,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "card_spend_change_30d",
      "value": -27.851
    },
    {
      "factor": "tenure_months",
      "value": 39
    },
    {
      "factor": "salary_missing_days",
      "value": 2.0
    },
    {
      "factor": "avg_resolution_time_hrs",
      "value": 51.3418
    },
    {
      "factor": "age",
      "value": 25
    }
  ]
}
```

#### Model 1 v2 Input

```json
{
  "customer_id": "C10003",
  "customer_name": "Ayushman Chander",
  "prediction_date": "2026-01-01",
  "target_month": "2026-02-01",
  "profile": {
    "tenure_months": 39,
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
      "balance_change_30d": 15.2295,
      "transaction_change_30d": 7.6981,
      "card_spend_change_30d": -24.0555,
      "app_login_change_30d": 3.9996,
      "salary_missing_days": 1.0,
      "external_transfer_change_30d": 57.912,
      "upi_share_of_spend": 0.3191,
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
  "churn_probability": 4.39,
  "raw_churn_probability": 39.1,
  "probability_mode": "sigmoid",
  "risk_score": 13.18,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "latest_external_transfer_change_30d",
      "value": 57.912,
      "message": "External transfers have increased.",
      "contribution": 0.13768547773361206
    },
    {
      "factor": "avg_card_spend_change_30d_3m",
      "value": -24.0555,
      "message": "Card spending has been falling across recent months.",
      "contribution": 0.034153860062360764
    },
    {
      "factor": "latest_card_spend_change_30d",
      "value": -24.0555,
      "message": "Card spending has been falling across recent months.",
      "contribution": 0.033680882304906845
    },
    {
      "factor": "avg_card_spend_change_30d_6m",
      "value": -24.0555,
      "message": "Card spending has been falling across recent months.",
      "contribution": 0.027816975489258766
    },
    {
      "factor": "max_salary_missing_days_3m",
      "value": 1.0,
      "message": "This signal increased churn risk.",
      "contribution": 0.022527970373630524
    }
  ]
}
```

### 2. Yashica Issac (`C10040`)

#### Model 1 Input

```json
{
  "customer_id": "C10040",
  "customer_name": "Yashica Issac",
  "snapshot_date": "2026-06-01",
  "customer": {
    "age": 35,
    "tenure_months": 142,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 2,
    "has_credit_card": 0,
    "has_loan": 1,
    "days_since_last_transaction": 16,
    "balance_change_30d": 3.4112,
    "transaction_change_30d": -18.4058,
    "card_spend_change_30d": -10.453,
    "app_login_change_30d": -28.2535,
    "salary_missing_days": 2.0,
    "external_transfer_change_30d": 14.2811,
    "upi_share_of_spend": 0.2819,
    "fd_maturing_in_30d": 0,
    "products_dropped_90d": 0,
    "complaints_30d": 2,
    "unresolved_complaints": 0,
    "failed_transactions_30d": 0,
    "avg_resolution_time_hrs": 10.1921,
    "emi_bounce_30d": 0,
    "branch_code": "BR-103",
    "card_colour": "silver"
  },
  "actual_current_month_churn": 0
}
```

#### Model 1 Output

```json
{
  "churn_probability": 2.39,
  "raw_churn_probability": 3.17,
  "risk_score": 7.18,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "complaints_30d",
      "value": 2
    },
    {
      "factor": "days_since_last_transaction",
      "value": 16
    },
    {
      "factor": "salary_missing_days",
      "value": 2.0
    },
    {
      "factor": "external_transfer_change_30d",
      "value": 14.2811
    },
    {
      "factor": "upi_share_of_spend",
      "value": 0.2819
    }
  ]
}
```

#### Model 1 v2 Input

```json
{
  "customer_id": "C10040",
  "customer_name": "Yashica Issac",
  "prediction_date": "2026-05-01",
  "target_month": "2026-06-01",
  "profile": {
    "tenure_months": 142,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 2,
    "has_credit_card": 0,
    "has_loan": 1
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 16,
      "balance_change_30d": -10.6471,
      "transaction_change_30d": 5.5015,
      "card_spend_change_30d": 1.7956,
      "app_login_change_30d": 7.0648,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": 17.1575,
      "upi_share_of_spend": 0.2135,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 1,
      "complaints_30d": 0,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 0.0,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-02-01",
      "days_since_last_transaction": 13,
      "balance_change_30d": 19.0031,
      "transaction_change_30d": 12.2182,
      "card_spend_change_30d": -0.8127,
      "app_login_change_30d": -20.3667,
      "salary_missing_days": 1.0,
      "external_transfer_change_30d": 34.3611,
      "upi_share_of_spend": 0.2697,
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
      "balance_change_30d": -1.8476,
      "transaction_change_30d": -10.2002,
      "card_spend_change_30d": 6.902,
      "app_login_change_30d": -10.1771,
      "salary_missing_days": 1.0,
      "external_transfer_change_30d": 34.8744,
      "upi_share_of_spend": 0.3734,
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
      "days_since_last_transaction": 19,
      "balance_change_30d": -8.144,
      "transaction_change_30d": -23.7416,
      "card_spend_change_30d": -23.1701,
      "app_login_change_30d": -30.8129,
      "salary_missing_days": 2.0,
      "external_transfer_change_30d": 32.4792,
      "upi_share_of_spend": 0.3505,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 2,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 20.0147,
      "emi_bounce_30d": 1
    },
    {
      "snapshot_date": "2026-05-01",
      "days_since_last_transaction": 12,
      "balance_change_30d": -1.1589,
      "transaction_change_30d": 5.9358,
      "card_spend_change_30d": 10.057,
      "app_login_change_30d": -8.719,
      "salary_missing_days": 1.0,
      "external_transfer_change_30d": 30.6872,
      "upi_share_of_spend": 0.346,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 16.0118,
      "emi_bounce_30d": 0
    }
  ],
  "actual_next_month_churn": 0
}
```

#### Model 1 v2 Output

```json
{
  "churn_probability": 3.18,
  "raw_churn_probability": 32.83,
  "probability_mode": "sigmoid",
  "risk_score": 9.53,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "latest_vs_avg_upi_share_of_spend_available_history",
      "value": 0.0353799999999999,
      "message": "This signal increased churn risk.",
      "contribution": 0.06685295701026917
    },
    {
      "factor": "count_quiet_customer_3m",
      "value": 3,
      "message": "This signal increased churn risk.",
      "contribution": 0.04109660163521767
    },
    {
      "factor": "external_transfer_change_30d_trend_6m",
      "value": 2.5177499999999977,
      "message": "External transfers have increased.",
      "contribution": 0.03700347989797592
    },
    {
      "factor": "avg_external_transfer_change_30d_3m",
      "value": 32.68026666666667,
      "message": "External transfers have increased.",
      "contribution": 0.023459650576114655
    },
    {
      "factor": "transaction_change_30d_trend_6m",
      "value": -3.509120000000001,
      "message": "Transaction activity has been falling across recent months.",
      "contribution": 0.017066100612282753
    }
  ]
}
```

### 3. Baghyawati Kade (`C10098`)

#### Model 1 Input

```json
{
  "customer_id": "C10098",
  "customer_name": "Baghyawati Kade",
  "snapshot_date": "2026-04-01",
  "customer": {
    "age": 80,
    "tenure_months": 164,
    "customer_segment": "pension",
    "income_regularity": "regular",
    "products_count": 1,
    "has_credit_card": 0,
    "has_loan": 0,
    "days_since_last_transaction": 6,
    "balance_change_30d": 12.3447,
    "transaction_change_30d": 14.5849,
    "card_spend_change_30d": 4.0286,
    "app_login_change_30d": 14.6959,
    "salary_missing_days": 1.0,
    "external_transfer_change_30d": -8.8499,
    "upi_share_of_spend": 0.4921,
    "fd_maturing_in_30d": 0,
    "products_dropped_90d": 0,
    "complaints_30d": 2,
    "unresolved_complaints": 1,
    "failed_transactions_30d": 2,
    "avg_resolution_time_hrs": 62.1423,
    "emi_bounce_30d": 0,
    "branch_code": "BR-117",
    "card_colour": "silver"
  },
  "actual_current_month_churn": 1
}
```

#### Model 1 Output

```json
{
  "churn_probability": 3.74,
  "raw_churn_probability": 5.25,
  "risk_score": 11.21,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "avg_resolution_time_hrs",
      "value": 62.1423
    },
    {
      "factor": "complaints_30d",
      "value": 2
    },
    {
      "factor": "age",
      "value": 80
    },
    {
      "factor": "unresolved_complaints",
      "value": 1
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
  "customer_id": "C10098",
  "customer_name": "Baghyawati Kade",
  "prediction_date": "2026-03-01",
  "target_month": "2026-04-01",
  "profile": {
    "tenure_months": 164,
    "customer_segment": "pension",
    "income_regularity": "regular",
    "products_count": 1,
    "has_credit_card": 0,
    "has_loan": 0
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 11,
      "balance_change_30d": -4.6367,
      "transaction_change_30d": 0.4296,
      "card_spend_change_30d": -18.8632,
      "app_login_change_30d": -40.1255,
      "salary_missing_days": 2.0,
      "external_transfer_change_30d": 28.7908,
      "upi_share_of_spend": 0.5325,
      "fd_maturing_in_30d": 1,
      "products_dropped_90d": 0,
      "complaints_30d": 0,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 7,
      "avg_resolution_time_hrs": 0.0,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-02-01",
      "days_since_last_transaction": 7,
      "balance_change_30d": -18.0132,
      "transaction_change_30d": 13.2583,
      "card_spend_change_30d": -3.4154,
      "app_login_change_30d": 12.792,
      "salary_missing_days": 1.0,
      "external_transfer_change_30d": 0.1315,
      "upi_share_of_spend": 0.5356,
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
      "balance_change_30d": 9.6721,
      "transaction_change_30d": -3.1833,
      "card_spend_change_30d": 19.2277,
      "app_login_change_30d": 19.3043,
      "salary_missing_days": 1.0,
      "external_transfer_change_30d": 42.4375,
      "upi_share_of_spend": 0.5757,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 6,
      "unresolved_complaints": 3,
      "failed_transactions_30d": 2,
      "avg_resolution_time_hrs": 69.3246,
      "emi_bounce_30d": 0
    }
  ],
  "actual_next_month_churn": 1
}
```

#### Model 1 v2 Output

```json
{
  "churn_probability": 31.4,
  "raw_churn_probability": 81.79,
  "probability_mode": "sigmoid",
  "risk_score": 74.28,
  "churn_prediction": "Yes",
  "risk_level": "High",
  "top_risk_factors": [
    {
      "factor": "max_avg_resolution_time_hrs_3m",
      "value": 69.3246,
      "message": "This signal increased churn risk.",
      "contribution": 0.6612331867218018
    },
    {
      "factor": "latest_avg_resolution_time_hrs",
      "value": 69.3246,
      "message": "This signal increased churn risk.",
      "contribution": 0.5030350685119629
    },
    {
      "factor": "sum_failed_transactions_30d_3m",
      "value": 9.0,
      "message": "Customer has recent failed transactions.",
      "contribution": 0.3734501302242279
    },
    {
      "factor": "sum_complaints_30d_6m",
      "value": 6.0,
      "message": "Customer has recent complaint activity.",
      "contribution": 0.08591601997613907
    },
    {
      "factor": "sum_failed_transactions_30d_6m",
      "value": 9.0,
      "message": "Customer has recent failed transactions.",
      "contribution": 0.08310256898403168
    }
  ]
}
```

### 4. Ayaan D’Alia (`C10122`)

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

### 5. Azad Chander (`C10736`)

#### Model 1 Input

```json
{
  "customer_id": "C10736",
  "customer_name": "Azad Chander",
  "snapshot_date": "2026-06-01",
  "customer": {
    "age": 72,
    "tenure_months": 226,
    "customer_segment": "pension",
    "income_regularity": "regular",
    "products_count": 1,
    "has_credit_card": 0,
    "has_loan": 0,
    "days_since_last_transaction": 7,
    "balance_change_30d": 0.1511,
    "transaction_change_30d": 19.6748,
    "card_spend_change_30d": 9.0656,
    "app_login_change_30d": 25.8499,
    "salary_missing_days": 1.0,
    "external_transfer_change_30d": 14.4852,
    "upi_share_of_spend": 0.8261,
    "fd_maturing_in_30d": 0,
    "products_dropped_90d": 0,
    "complaints_30d": 0,
    "unresolved_complaints": 0,
    "failed_transactions_30d": 0,
    "avg_resolution_time_hrs": 0.0,
    "emi_bounce_30d": 0,
    "branch_code": "BR-119",
    "card_colour": "green"
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
      "factor": "app_login_change_30d",
      "value": 25.8499
    },
    {
      "factor": "age",
      "value": 72
    },
    {
      "factor": "customer_segment",
      "value": "pension"
    },
    {
      "factor": "external_transfer_change_30d",
      "value": 14.4852
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
  "customer_id": "C10736",
  "customer_name": "Azad Chander",
  "prediction_date": "2026-05-01",
  "target_month": "2026-06-01",
  "profile": {
    "tenure_months": 226,
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
      "balance_change_30d": 23.4286,
      "transaction_change_30d": 9.1308,
      "card_spend_change_30d": -10.5415,
      "app_login_change_30d": 13.5164,
      "salary_missing_days": 1.0,
      "external_transfer_change_30d": 10.8802,
      "upi_share_of_spend": 0.8282,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 35.1043,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-02-01",
      "days_since_last_transaction": 9,
      "balance_change_30d": 6.2597,
      "transaction_change_30d": 33.837,
      "card_spend_change_30d": 28.6766,
      "app_login_change_30d": 28.4977,
      "salary_missing_days": 1.0,
      "external_transfer_change_30d": -33.6403,
      "upi_share_of_spend": 0.8464,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 2,
      "unresolved_complaints": 1,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 37.7294,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-03-01",
      "days_since_last_transaction": 7,
      "balance_change_30d": -10.2051,
      "transaction_change_30d": 13.6073,
      "card_spend_change_30d": 26.2225,
      "app_login_change_30d": 27.7977,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": 39.7105,
      "upi_share_of_spend": 0.781,
      "fd_maturing_in_30d": 1,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 32.5718,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-04-01",
      "days_since_last_transaction": 13,
      "balance_change_30d": 35.0893,
      "transaction_change_30d": 16.5555,
      "card_spend_change_30d": 12.9379,
      "app_login_change_30d": 19.2956,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": 16.2465,
      "upi_share_of_spend": 0.763,
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
      "days_since_last_transaction": 9,
      "balance_change_30d": 41.8874,
      "transaction_change_30d": -1.8704,
      "card_spend_change_30d": 8.7873,
      "app_login_change_30d": -14.6753,
      "salary_missing_days": 1.0,
      "external_transfer_change_30d": -25.4468,
      "upi_share_of_spend": 0.9245,
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
  "churn_probability": 2.62,
  "raw_churn_probability": 29.19,
  "probability_mode": "sigmoid",
  "risk_score": 7.87,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "latest_vs_avg_upi_share_of_spend_available_history",
      "value": 0.09588,
      "message": "This signal increased churn risk.",
      "contribution": 0.12889540195465088
    },
    {
      "factor": "sum_fd_maturing_in_30d_3m",
      "value": 1.0,
      "message": "Customer has a fixed deposit maturing soon.",
      "contribution": 0.10457620769739151
    },
    {
      "factor": "latest_upi_share_of_spend",
      "value": 0.9245,
      "message": "This signal increased churn risk.",
      "contribution": 0.06228218972682953
    },
    {
      "factor": "avg_transaction_change_30d_6m",
      "value": 14.25204,
      "message": "This signal increased churn risk.",
      "contribution": 0.03767161816358566
    },
    {
      "factor": "transaction_change_30d_trend_6m",
      "value": -3.928390000000004,
      "message": "Transaction activity has been falling across recent months.",
      "contribution": 0.029124457389116287
    }
  ]
}
```

### 6. Theodore Bahri (`C11005`)

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

### 7. Aadi Narula (`C11006`)

#### Model 1 Input

```json
{
  "customer_id": "C11006",
  "customer_name": "Aadi Narula",
  "snapshot_date": "2026-06-01",
  "customer": {
    "age": 54,
    "tenure_months": 129,
    "customer_segment": "farmer",
    "income_regularity": "seasonal",
    "products_count": 2,
    "has_credit_card": 0,
    "has_loan": 1,
    "days_since_last_transaction": 2,
    "balance_change_30d": -4.1422,
    "transaction_change_30d": 0.8407,
    "card_spend_change_30d": 13.4909,
    "app_login_change_30d": 16.4652,
    "salary_missing_days": null,
    "external_transfer_change_30d": 7.5483,
    "upi_share_of_spend": 0.6292,
    "fd_maturing_in_30d": 1,
    "products_dropped_90d": 0,
    "complaints_30d": 0,
    "unresolved_complaints": 0,
    "failed_transactions_30d": 0,
    "avg_resolution_time_hrs": 0.0,
    "emi_bounce_30d": 0,
    "branch_code": "BR-138",
    "card_colour": "gold"
  },
  "actual_current_month_churn": 0
}
```

#### Model 1 Output

```json
{
  "churn_probability": 1.96,
  "raw_churn_probability": 1.98,
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
      "value": "BR-138"
    },
    {
      "factor": "external_transfer_change_30d",
      "value": 7.5483
    },
    {
      "factor": "app_login_change_30d",
      "value": 16.4652
    },
    {
      "factor": "transaction_change_30d",
      "value": 0.8407
    }
  ]
}
```

#### Model 1 v2 Input

```json
{
  "customer_id": "C11006",
  "customer_name": "Aadi Narula",
  "prediction_date": "2026-05-01",
  "target_month": "2026-06-01",
  "profile": {
    "tenure_months": 129,
    "customer_segment": "farmer",
    "income_regularity": "seasonal",
    "products_count": 2,
    "has_credit_card": 0,
    "has_loan": 1
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 3,
      "balance_change_30d": 3.258,
      "transaction_change_30d": 1.2609,
      "card_spend_change_30d": -18.6395,
      "app_login_change_30d": -22.7541,
      "salary_missing_days": null,
      "external_transfer_change_30d": 41.1218,
      "upi_share_of_spend": 0.6506,
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
      "days_since_last_transaction": 14,
      "balance_change_30d": -32.863,
      "transaction_change_30d": -5.0872,
      "card_spend_change_30d": -30.3962,
      "app_login_change_30d": -10.7296,
      "salary_missing_days": null,
      "external_transfer_change_30d": 57.8361,
      "upi_share_of_spend": 0.7751,
      "fd_maturing_in_30d": 1,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 20.9593,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-03-01",
      "days_since_last_transaction": 9,
      "balance_change_30d": 14.9785,
      "transaction_change_30d": -15.5136,
      "card_spend_change_30d": -26.176,
      "app_login_change_30d": 12.2695,
      "salary_missing_days": null,
      "external_transfer_change_30d": 44.3739,
      "upi_share_of_spend": 0.7429,
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
      "balance_change_30d": -21.4549,
      "transaction_change_30d": -13.642,
      "card_spend_change_30d": -10.1912,
      "app_login_change_30d": 5.4808,
      "salary_missing_days": null,
      "external_transfer_change_30d": 23.3546,
      "upi_share_of_spend": 0.767,
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
      "balance_change_30d": -14.9152,
      "transaction_change_30d": -3.8991,
      "card_spend_change_30d": -6.5804,
      "app_login_change_30d": -5.3433,
      "salary_missing_days": null,
      "external_transfer_change_30d": 39.3493,
      "upi_share_of_spend": 0.6876,
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
  "churn_probability": 1.85,
  "raw_churn_probability": 22.5,
  "probability_mode": "sigmoid",
  "risk_score": 5.54,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "latest_balance_change_30d",
      "value": -14.9152,
      "message": "Balance has been falling across recent months.",
      "contribution": 0.03590558096766472
    },
    {
      "factor": "avg_card_spend_change_30d_6m",
      "value": -18.39666,
      "message": "Card spending has been falling across recent months.",
      "contribution": 0.023511193692684174
    },
    {
      "factor": "avg_upi_share_of_spend_6m",
      "value": 0.72464,
      "message": "This signal increased churn risk.",
      "contribution": 0.022467073053121567
    },
    {
      "factor": "avg_card_spend_change_30d_3m",
      "value": -14.315866666666665,
      "message": "Card spending has been falling across recent months.",
      "contribution": 0.020375605672597885
    },
    {
      "factor": "avg_external_transfer_change_30d_3m",
      "value": 35.6926,
      "message": "External transfers have increased.",
      "contribution": 0.01890287548303604
    }
  ]
}
```

### 8. Matthew Chatterjee (`C11056`)

#### Model 1 Input

```json
{
  "customer_id": "C11056",
  "customer_name": "Matthew Chatterjee",
  "snapshot_date": "2026-06-01",
  "customer": {
    "age": 60,
    "tenure_months": 165,
    "customer_segment": "pension",
    "income_regularity": "regular",
    "products_count": 3,
    "has_credit_card": 1,
    "has_loan": 0,
    "days_since_last_transaction": 9,
    "balance_change_30d": 3.4667,
    "transaction_change_30d": -0.5229,
    "card_spend_change_30d": 21.5568,
    "app_login_change_30d": 28.203,
    "salary_missing_days": 0.0,
    "external_transfer_change_30d": -9.6126,
    "upi_share_of_spend": 0.2918,
    "fd_maturing_in_30d": 0,
    "products_dropped_90d": 0,
    "complaints_30d": 0,
    "unresolved_complaints": 0,
    "failed_transactions_30d": 0,
    "avg_resolution_time_hrs": 0.0,
    "emi_bounce_30d": 0,
    "branch_code": "BR-103",
    "card_colour": "gold"
  },
  "actual_current_month_churn": 0
}
```

#### Model 1 Output

```json
{
  "churn_probability": 1.93,
  "raw_churn_probability": 1.44,
  "risk_score": 5.8,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "app_login_change_30d",
      "value": 28.203
    },
    {
      "factor": "customer_segment",
      "value": "pension"
    },
    {
      "factor": "upi_share_of_spend",
      "value": 0.2918
    },
    {
      "factor": "income_regularity",
      "value": "regular"
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
  "customer_id": "C11056",
  "customer_name": "Matthew Chatterjee",
  "prediction_date": "2026-05-01",
  "target_month": "2026-06-01",
  "profile": {
    "tenure_months": 165,
    "customer_segment": "pension",
    "income_regularity": "regular",
    "products_count": 3,
    "has_credit_card": 1,
    "has_loan": 0
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 10,
      "balance_change_30d": 0.8043,
      "transaction_change_30d": -18.3984,
      "card_spend_change_30d": 15.2698,
      "app_login_change_30d": -0.4739,
      "salary_missing_days": 1.0,
      "external_transfer_change_30d": 20.0711,
      "upi_share_of_spend": 0.3262,
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
      "days_since_last_transaction": 9,
      "balance_change_30d": -6.4846,
      "transaction_change_30d": -1.2492,
      "card_spend_change_30d": 29.4573,
      "app_login_change_30d": 10.9421,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -33.0259,
      "upi_share_of_spend": 0.2646,
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
      "days_since_last_transaction": 17,
      "balance_change_30d": 4.1935,
      "transaction_change_30d": 4.5946,
      "card_spend_change_30d": 19.2121,
      "app_login_change_30d": -16.0068,
      "salary_missing_days": 2.0,
      "external_transfer_change_30d": 25.2064,
      "upi_share_of_spend": 0.3832,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 2,
      "avg_resolution_time_hrs": 7.6961,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-04-01",
      "days_since_last_transaction": 7,
      "balance_change_30d": 8.8584,
      "transaction_change_30d": -1.3115,
      "card_spend_change_30d": 10.9209,
      "app_login_change_30d": 20.7993,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": 23.1193,
      "upi_share_of_spend": 0.2519,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 12.4989,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-05-01",
      "days_since_last_transaction": 12,
      "balance_change_30d": 23.2366,
      "transaction_change_30d": 30.9777,
      "card_spend_change_30d": 7.7173,
      "app_login_change_30d": -2.6434,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -33.2308,
      "upi_share_of_spend": 0.216,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 2,
      "avg_resolution_time_hrs": 6.1062,
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
  "raw_churn_probability": 22.97,
  "probability_mode": "sigmoid",
  "risk_score": 5.67,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "latest_vs_avg_external_transfer_change_30d_available_history",
      "value": -33.65882,
      "message": "This signal increased churn risk.",
      "contribution": 0.06794237345457077
    },
    {
      "factor": "max_days_since_last_transaction_3m",
      "value": 17.0,
      "message": "Customer has gone longer without transacting.",
      "contribution": 0.03016400709748268
    },
    {
      "factor": "count_quiet_customer_3m",
      "value": 2,
      "message": "This signal increased churn risk.",
      "contribution": 0.02550780214369297
    },
    {
      "factor": "avg_app_login_change_30d_6m",
      "value": 2.52346,
      "message": "This signal increased churn risk.",
      "contribution": 0.009277744218707085
    },
    {
      "factor": "latest_vs_avg_app_login_change_30d_available_history",
      "value": -5.16686,
      "message": "App usage has been falling across recent months.",
      "contribution": 0.00879844930022955
    }
  ]
}
```

### 9. Vrishti Parmer (`C11153`)

#### Model 1 Input

```json
{
  "customer_id": "C11153",
  "customer_name": "Vrishti Parmer",
  "snapshot_date": "2026-04-01",
  "customer": {
    "age": 49,
    "tenure_months": 53,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 2,
    "has_credit_card": 0,
    "has_loan": 1,
    "days_since_last_transaction": 16,
    "balance_change_30d": -31.6716,
    "transaction_change_30d": -20.7974,
    "card_spend_change_30d": -26.6134,
    "app_login_change_30d": -25.9857,
    "salary_missing_days": 4.0,
    "external_transfer_change_30d": 1.7815,
    "upi_share_of_spend": 0.7299,
    "fd_maturing_in_30d": 0,
    "products_dropped_90d": 0,
    "complaints_30d": 2,
    "unresolved_complaints": 0,
    "failed_transactions_30d": 0,
    "avg_resolution_time_hrs": 25.5883,
    "emi_bounce_30d": 0,
    "branch_code": "BR-131",
    "card_colour": "green"
  },
  "actual_current_month_churn": 1
}
```

#### Model 1 Output

```json
{
  "churn_probability": 18.06,
  "raw_churn_probability": 17.93,
  "risk_score": 62.22,
  "churn_prediction": "Yes",
  "risk_level": "Medium",
  "top_risk_factors": [
    {
      "factor": "balance_change_30d",
      "value": -31.6716
    },
    {
      "factor": "salary_missing_days",
      "value": 4.0
    },
    {
      "factor": "complaints_30d",
      "value": 2
    },
    {
      "factor": "card_spend_change_30d",
      "value": -26.6134
    },
    {
      "factor": "days_since_last_transaction",
      "value": 16
    }
  ]
}
```

#### Model 1 v2 Input

```json
{
  "customer_id": "C11153",
  "customer_name": "Vrishti Parmer",
  "prediction_date": "2026-03-01",
  "target_month": "2026-04-01",
  "profile": {
    "tenure_months": 53,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 2,
    "has_credit_card": 0,
    "has_loan": 1
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 10,
      "balance_change_30d": -14.0462,
      "transaction_change_30d": 9.6398,
      "card_spend_change_30d": -24.485,
      "app_login_change_30d": 23.4043,
      "salary_missing_days": 1.0,
      "external_transfer_change_30d": 33.531,
      "upi_share_of_spend": 0.6387,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 1,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 34.8744,
      "emi_bounce_30d": 1
    },
    {
      "snapshot_date": "2026-02-01",
      "days_since_last_transaction": 15,
      "balance_change_30d": -9.2735,
      "transaction_change_30d": -17.4645,
      "card_spend_change_30d": -4.8145,
      "app_login_change_30d": -14.9794,
      "salary_missing_days": 1.0,
      "external_transfer_change_30d": 37.5956,
      "upi_share_of_spend": 0.7322,
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
      "days_since_last_transaction": 9,
      "balance_change_30d": 13.5115,
      "transaction_change_30d": 1.4178,
      "card_spend_change_30d": -8.8501,
      "app_login_change_30d": 5.4145,
      "salary_missing_days": 2.0,
      "external_transfer_change_30d": 24.9285,
      "upi_share_of_spend": 0.7371,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 1,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 49.5283,
      "emi_bounce_30d": 0
    }
  ],
  "actual_next_month_churn": 1
}
```

#### Model 1 v2 Output

```json
{
  "churn_probability": 9.56,
  "raw_churn_probability": 54.57,
  "probability_mode": "sigmoid",
  "risk_score": 28.68,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "latest_avg_resolution_time_hrs",
      "value": 49.5283,
      "message": "This signal increased churn risk.",
      "contribution": 0.4267439842224121
    },
    {
      "factor": "latest_vs_avg_upi_share_of_spend_available_history",
      "value": 0.0344333333333333,
      "message": "This signal increased churn risk.",
      "contribution": 0.08708921819925308
    },
    {
      "factor": "latest_salary_missing_days",
      "value": 2.0,
      "message": "This signal increased churn risk.",
      "contribution": 0.08156057447195053
    },
    {
      "factor": "max_avg_resolution_time_hrs_3m",
      "value": 49.5283,
      "message": "This signal increased churn risk.",
      "contribution": 0.07206718623638153
    },
    {
      "factor": "avg_upi_share_of_spend_6m",
      "value": 0.7026666666666667,
      "message": "This signal increased churn risk.",
      "contribution": 0.03916563093662262
    }
  ]
}
```

### 10. Nakul Pathak (`C11345`)

#### Model 1 Input

```json
{
  "customer_id": "C11345",
  "customer_name": "Nakul Pathak",
  "snapshot_date": "2026-06-01",
  "customer": {
    "age": 36,
    "tenure_months": 138,
    "customer_segment": "farmer",
    "income_regularity": "seasonal",
    "products_count": 2,
    "has_credit_card": 0,
    "has_loan": 1,
    "days_since_last_transaction": 20,
    "balance_change_30d": -39.2848,
    "transaction_change_30d": -31.2044,
    "card_spend_change_30d": -33.372,
    "app_login_change_30d": -21.93,
    "salary_missing_days": null,
    "external_transfer_change_30d": 54.4956,
    "upi_share_of_spend": 0.6219,
    "fd_maturing_in_30d": 0,
    "products_dropped_90d": 0,
    "complaints_30d": 0,
    "unresolved_complaints": 0,
    "failed_transactions_30d": 2,
    "avg_resolution_time_hrs": 0.0,
    "emi_bounce_30d": 0,
    "branch_code": "BR-134",
    "card_colour": "gold"
  },
  "actual_current_month_churn": 0
}
```

#### Model 1 Output

```json
{
  "churn_probability": 18.06,
  "raw_churn_probability": 20.93,
  "risk_score": 62.22,
  "churn_prediction": "Yes",
  "risk_level": "Medium",
  "top_risk_factors": [
    {
      "factor": "balance_change_30d",
      "value": -39.2848
    },
    {
      "factor": "days_since_last_transaction",
      "value": 20
    },
    {
      "factor": "card_spend_change_30d",
      "value": -33.372
    },
    {
      "factor": "failed_transactions_30d",
      "value": 2
    },
    {
      "factor": "branch_code",
      "value": "BR-134"
    }
  ]
}
```

#### Model 1 v2 Input

```json
{
  "customer_id": "C11345",
  "customer_name": "Nakul Pathak",
  "prediction_date": "2026-05-01",
  "target_month": "2026-06-01",
  "profile": {
    "tenure_months": 138,
    "customer_segment": "farmer",
    "income_regularity": "seasonal",
    "products_count": 2,
    "has_credit_card": 0,
    "has_loan": 1
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 15,
      "balance_change_30d": -2.7387,
      "transaction_change_30d": -11.4408,
      "card_spend_change_30d": -0.2507,
      "app_login_change_30d": -22.8951,
      "salary_missing_days": null,
      "external_transfer_change_30d": -18.2421,
      "upi_share_of_spend": 0.6098,
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
      "balance_change_30d": -18.4316,
      "transaction_change_30d": -32.7684,
      "card_spend_change_30d": -1.517,
      "app_login_change_30d": -14.1428,
      "salary_missing_days": null,
      "external_transfer_change_30d": 27.8871,
      "upi_share_of_spend": 0.5682,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 33.1074,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-03-01",
      "days_since_last_transaction": 9,
      "balance_change_30d": 9.7732,
      "transaction_change_30d": -19.4251,
      "card_spend_change_30d": 12.705,
      "app_login_change_30d": 29.7292,
      "salary_missing_days": null,
      "external_transfer_change_30d": 0.7274,
      "upi_share_of_spend": 0.4836,
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
      "days_since_last_transaction": 11,
      "balance_change_30d": -9.7913,
      "transaction_change_30d": -6.8327,
      "card_spend_change_30d": 24.8785,
      "app_login_change_30d": 10.3806,
      "salary_missing_days": null,
      "external_transfer_change_30d": 5.2936,
      "upi_share_of_spend": 0.5399,
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
      "balance_change_30d": -17.0964,
      "transaction_change_30d": -23.8049,
      "card_spend_change_30d": -11.1335,
      "app_login_change_30d": -11.0478,
      "salary_missing_days": null,
      "external_transfer_change_30d": 62.6145,
      "upi_share_of_spend": 0.5963,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 2,
      "unresolved_complaints": 1,
      "failed_transactions_30d": 2,
      "avg_resolution_time_hrs": 43.9323,
      "emi_bounce_30d": 0
    }
  ],
  "actual_next_month_churn": 0
}
```

#### Model 1 v2 Output

```json
{
  "churn_probability": 18.3,
  "raw_churn_probability": 68.51,
  "probability_mode": "sigmoid",
  "risk_score": 63.19,
  "churn_prediction": "Yes",
  "risk_level": "Medium",
  "top_risk_factors": [
    {
      "factor": "latest_days_since_last_transaction",
      "value": 17,
      "message": "Customer has gone longer without transacting.",
      "contribution": 0.5099367499351501
    },
    {
      "factor": "latest_avg_resolution_time_hrs",
      "value": 43.9323,
      "message": "This signal increased churn risk.",
      "contribution": 0.2855015695095062
    },
    {
      "factor": "latest_transaction_change_30d",
      "value": -23.8049,
      "message": "Transaction activity has been falling across recent months.",
      "contribution": 0.17107465863227844
    },
    {
      "factor": "latest_external_transfer_change_30d",
      "value": 62.6145,
      "message": "External transfers have increased.",
      "contribution": 0.13524433970451355
    },
    {
      "factor": "sum_fd_maturing_in_30d_3m",
      "value": 1.0,
      "message": "Customer has a fixed deposit maturing soon.",
      "contribution": 0.07759766280651093
    }
  ]
}
```

### 11. Edhitha Palan (`C11532`)

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

### 12. Max Om (`C11635`)

#### Model 1 Input

```json
{
  "customer_id": "C11635",
  "customer_name": "Max Om",
  "snapshot_date": "2026-06-01",
  "customer": {
    "age": 35,
    "tenure_months": 129,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 4,
    "has_credit_card": 1,
    "has_loan": 0,
    "days_since_last_transaction": 7,
    "balance_change_30d": -2.0868,
    "transaction_change_30d": -10.4845,
    "card_spend_change_30d": -12.5904,
    "app_login_change_30d": 26.043,
    "salary_missing_days": 0.0,
    "external_transfer_change_30d": 49.0996,
    "upi_share_of_spend": 0.5294,
    "fd_maturing_in_30d": 0,
    "products_dropped_90d": 0,
    "complaints_30d": 2,
    "unresolved_complaints": 0,
    "failed_transactions_30d": 2,
    "avg_resolution_time_hrs": 30.3923,
    "emi_bounce_30d": 0,
    "branch_code": "BR-106",
    "card_colour": "black"
  },
  "actual_current_month_churn": 0
}
```

#### Model 1 Output

```json
{
  "churn_probability": 2.39,
  "raw_churn_probability": 3.5,
  "risk_score": 7.18,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "branch_code",
      "value": "BR-106"
    },
    {
      "factor": "complaints_30d",
      "value": 2
    },
    {
      "factor": "failed_transactions_30d",
      "value": 2
    },
    {
      "factor": "app_login_change_30d",
      "value": 26.043
    },
    {
      "factor": "external_transfer_change_30d",
      "value": 49.0996
    }
  ]
}
```

#### Model 1 v2 Input

```json
{
  "customer_id": "C11635",
  "customer_name": "Max Om",
  "prediction_date": "2026-05-01",
  "target_month": "2026-06-01",
  "profile": {
    "tenure_months": 129,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 4,
    "has_credit_card": 1,
    "has_loan": 0
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 11,
      "balance_change_30d": 17.7503,
      "transaction_change_30d": 15.4165,
      "card_spend_change_30d": 25.06,
      "app_login_change_30d": -13.098,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -13.5798,
      "upi_share_of_spend": 0.5417,
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
      "balance_change_30d": 28.5977,
      "transaction_change_30d": 24.8283,
      "card_spend_change_30d": 37.8757,
      "app_login_change_30d": -14.0047,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": 26.9574,
      "upi_share_of_spend": 0.4467,
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
      "balance_change_30d": -16.9513,
      "transaction_change_30d": -7.8883,
      "card_spend_change_30d": -23.7052,
      "app_login_change_30d": -23.7083,
      "salary_missing_days": 1.0,
      "external_transfer_change_30d": 35.0832,
      "upi_share_of_spend": 0.4892,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 2,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 19.8584,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-04-01",
      "days_since_last_transaction": 12,
      "balance_change_30d": -20.4055,
      "transaction_change_30d": -9.7008,
      "card_spend_change_30d": 8.2741,
      "app_login_change_30d": -37.8803,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -0.9952,
      "upi_share_of_spend": 0.4839,
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
      "days_since_last_transaction": 12,
      "balance_change_30d": 2.2946,
      "transaction_change_30d": 12.0228,
      "card_spend_change_30d": 20.7422,
      "app_login_change_30d": -4.216,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -10.2206,
      "upi_share_of_spend": 0.6378,
      "fd_maturing_in_30d": 1,
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
  "churn_probability": 4.6,
  "raw_churn_probability": 40.0,
  "probability_mode": "sigmoid",
  "risk_score": 13.81,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "latest_vs_avg_upi_share_of_spend_available_history",
      "value": 0.11794,
      "message": "This signal increased churn risk.",
      "contribution": 0.14137022197246552
    },
    {
      "factor": "sum_fd_maturing_in_30d_3m",
      "value": 1.0,
      "message": "Customer has a fixed deposit maturing soon.",
      "contribution": 0.09229433536529541
    },
    {
      "factor": "latest_fd_maturing_in_30d",
      "value": 1,
      "message": "Customer has a fixed deposit maturing soon.",
      "contribution": 0.09124034643173218
    },
    {
      "factor": "balance_change_30d_trend_6m",
      "value": -7.991460000000002,
      "message": "Balance has been falling across recent months.",
      "contribution": 0.07422832399606705
    },
    {
      "factor": "days_since_last_transaction_trend_6m",
      "value": 0.9999999999999996,
      "message": "Customer has gone longer without transacting.",
      "contribution": 0.03524317592382431
    }
  ]
}
```

### 13. Prisha Ravel (`C11661`)

#### Model 1 Input

```json
{
  "customer_id": "C11661",
  "customer_name": "Prisha Ravel",
  "snapshot_date": "2026-03-01",
  "customer": {
    "age": 47,
    "tenure_months": 122,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 1,
    "has_credit_card": 0,
    "has_loan": 0,
    "days_since_last_transaction": 8,
    "balance_change_30d": 4.577,
    "transaction_change_30d": -2.9184,
    "card_spend_change_30d": 17.9397,
    "app_login_change_30d": 6.09,
    "salary_missing_days": 1.0,
    "external_transfer_change_30d": 31.1581,
    "upi_share_of_spend": 0.2248,
    "fd_maturing_in_30d": 1,
    "products_dropped_90d": 0,
    "complaints_30d": 4,
    "unresolved_complaints": 2,
    "failed_transactions_30d": 3,
    "avg_resolution_time_hrs": 72.1492,
    "emi_bounce_30d": 0,
    "branch_code": "BR-109",
    "card_colour": "gold"
  },
  "actual_current_month_churn": 1
}
```

#### Model 1 Output

```json
{
  "churn_probability": 18.06,
  "raw_churn_probability": 21.29,
  "risk_score": 62.22,
  "churn_prediction": "Yes",
  "risk_level": "Medium",
  "top_risk_factors": [
    {
      "factor": "avg_resolution_time_hrs",
      "value": 72.1492
    },
    {
      "factor": "fd_maturing_in_30d",
      "value": 1
    },
    {
      "factor": "complaints_30d",
      "value": 4
    },
    {
      "factor": "failed_transactions_30d",
      "value": 3
    },
    {
      "factor": "unresolved_complaints",
      "value": 2
    }
  ]
}
```

#### Model 1 v2 Input

```json
{
  "customer_id": "C11661",
  "customer_name": "Prisha Ravel",
  "prediction_date": "2026-02-01",
  "target_month": "2026-03-01",
  "profile": {
    "tenure_months": 122,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 1,
    "has_credit_card": 0,
    "has_loan": 0
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 12,
      "balance_change_30d": 6.6141,
      "transaction_change_30d": -18.7548,
      "card_spend_change_30d": 2.5367,
      "app_login_change_30d": 11.3555,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": 11.46,
      "upi_share_of_spend": 0.2938,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 2,
      "unresolved_complaints": 1,
      "failed_transactions_30d": 3,
      "avg_resolution_time_hrs": 45.614,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-02-01",
      "days_since_last_transaction": 4,
      "balance_change_30d": 15.6652,
      "transaction_change_30d": 27.0014,
      "card_spend_change_30d": 22.3025,
      "app_login_change_30d": -18.0031,
      "salary_missing_days": 1.0,
      "external_transfer_change_30d": 60.3143,
      "upi_share_of_spend": 0.1728,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 4,
      "avg_resolution_time_hrs": 24.4742,
      "emi_bounce_30d": 0
    }
  ],
  "actual_next_month_churn": 1
}
```

#### Model 1 v2 Output

```json
{
  "churn_probability": 7.88,
  "raw_churn_probability": 50.64,
  "probability_mode": "sigmoid",
  "risk_score": 23.64,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "sum_failed_transactions_30d_3m",
      "value": 7.0,
      "message": "Customer has recent failed transactions.",
      "contribution": 0.460086464881897
    },
    {
      "factor": "latest_failed_transactions_30d",
      "value": 4,
      "message": "Customer has recent failed transactions.",
      "contribution": 0.17333762347698212
    },
    {
      "factor": "latest_external_transfer_change_30d",
      "value": 60.3143,
      "message": "External transfers have increased.",
      "contribution": 0.1255442351102829
    },
    {
      "factor": "external_transfer_change_30d_trend_6m",
      "value": 48.85429999999999,
      "message": "External transfers have increased.",
      "contribution": 0.10722237825393677
    },
    {
      "factor": "max_avg_resolution_time_hrs_3m",
      "value": 45.614,
      "message": "This signal increased churn risk.",
      "contribution": 0.054905638098716736
    }
  ]
}
```

### 14. Oliver Kade (`C11837`)

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

### 15. Gagan Vala (`C12027`)

#### Model 1 Input

```json
{
  "customer_id": "C12027",
  "customer_name": "Gagan Vala",
  "snapshot_date": "2026-06-01",
  "customer": {
    "age": 35,
    "tenure_months": 90,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 1,
    "has_credit_card": 0,
    "has_loan": 0,
    "days_since_last_transaction": 18,
    "balance_change_30d": -28.079,
    "transaction_change_30d": -17.3952,
    "card_spend_change_30d": -50.0256,
    "app_login_change_30d": -39.5201,
    "salary_missing_days": 5.0,
    "external_transfer_change_30d": 61.6849,
    "upi_share_of_spend": 0.562,
    "fd_maturing_in_30d": 0,
    "products_dropped_90d": 1,
    "complaints_30d": 2,
    "unresolved_complaints": 1,
    "failed_transactions_30d": 4,
    "avg_resolution_time_hrs": 52.7983,
    "emi_bounce_30d": 0,
    "branch_code": "BR-112",
    "card_colour": "silver"
  },
  "actual_current_month_churn": 0
}
```

#### Model 1 Output

```json
{
  "churn_probability": 36.3,
  "raw_churn_probability": 38.35,
  "risk_score": 76.11,
  "churn_prediction": "Yes",
  "risk_level": "High",
  "top_risk_factors": [
    {
      "factor": "card_spend_change_30d",
      "value": -50.0256
    },
    {
      "factor": "days_since_last_transaction",
      "value": 18
    },
    {
      "factor": "salary_missing_days",
      "value": 5.0
    },
    {
      "factor": "failed_transactions_30d",
      "value": 4
    },
    {
      "factor": "balance_change_30d",
      "value": -28.079
    }
  ]
}
```

#### Model 1 v2 Input

```json
{
  "customer_id": "C12027",
  "customer_name": "Gagan Vala",
  "prediction_date": "2026-05-01",
  "target_month": "2026-06-01",
  "profile": {
    "tenure_months": 90,
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
      "balance_change_30d": -7.5581,
      "transaction_change_30d": -9.1147,
      "card_spend_change_30d": 18.2996,
      "app_login_change_30d": -23.3953,
      "salary_missing_days": 1.0,
      "external_transfer_change_30d": 56.5725,
      "upi_share_of_spend": 0.4416,
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
      "balance_change_30d": 0.9273,
      "transaction_change_30d": -4.0911,
      "card_spend_change_30d": -16.803,
      "app_login_change_30d": 11.3977,
      "salary_missing_days": 4.0,
      "external_transfer_change_30d": 33.7123,
      "upi_share_of_spend": 0.4317,
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
      "days_since_last_transaction": 13,
      "balance_change_30d": -10.2785,
      "transaction_change_30d": -52.2656,
      "card_spend_change_30d": -49.68,
      "app_login_change_30d": -14.4104,
      "salary_missing_days": 2.0,
      "external_transfer_change_30d": 22.8915,
      "upi_share_of_spend": 0.5327,
      "fd_maturing_in_30d": 1,
      "products_dropped_90d": 0,
      "complaints_30d": 3,
      "unresolved_complaints": 1,
      "failed_transactions_30d": 3,
      "avg_resolution_time_hrs": 30.9871,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-04-01",
      "days_since_last_transaction": 13,
      "balance_change_30d": -36.926,
      "transaction_change_30d": -6.3772,
      "card_spend_change_30d": 4.6277,
      "app_login_change_30d": -28.6473,
      "salary_missing_days": 3.0,
      "external_transfer_change_30d": 18.7926,
      "upi_share_of_spend": 0.4604,
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
      "balance_change_30d": -21.5167,
      "transaction_change_30d": -21.516,
      "card_spend_change_30d": -36.6355,
      "app_login_change_30d": -30.5611,
      "salary_missing_days": 4.0,
      "external_transfer_change_30d": 38.0535,
      "upi_share_of_spend": 0.5289,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 1,
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
  "churn_probability": 39.61,
  "raw_churn_probability": 88.47,
  "probability_mode": "sigmoid",
  "risk_score": 77.35,
  "churn_prediction": "Yes",
  "risk_level": "High",
  "top_risk_factors": [
    {
      "factor": "latest_days_since_last_transaction",
      "value": 14,
      "message": "Customer has gone longer without transacting.",
      "contribution": 0.5043866038322449
    },
    {
      "factor": "latest_salary_missing_days",
      "value": 4.0,
      "message": "This signal increased churn risk.",
      "contribution": 0.26618579030036926
    },
    {
      "factor": "latest_vs_avg_upi_share_of_spend_available_history",
      "value": 0.0498400000000001,
      "message": "This signal increased churn risk.",
      "contribution": 0.215730682015419
    },
    {
      "factor": "latest_balance_change_30d",
      "value": -21.5167,
      "message": "Balance has been falling across recent months.",
      "contribution": 0.17652148008346558
    },
    {
      "factor": "days_since_last_transaction_trend_6m",
      "value": 2.0999999999999988,
      "message": "Customer has gone longer without transacting.",
      "contribution": 0.1585390269756317
    }
  ]
}
```

### 16. Naveen Tella (`C12090`)

#### Model 1 Input

```json
{
  "customer_id": "C12090",
  "customer_name": "Naveen Tella",
  "snapshot_date": "2026-06-01",
  "customer": {
    "age": 41,
    "tenure_months": 35,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 1,
    "has_credit_card": 0,
    "has_loan": 0,
    "days_since_last_transaction": 16,
    "balance_change_30d": -37.7748,
    "transaction_change_30d": -49.7912,
    "card_spend_change_30d": -55.3749,
    "app_login_change_30d": -50.2914,
    "salary_missing_days": 6.0,
    "external_transfer_change_30d": 102.4911,
    "upi_share_of_spend": 0.6425,
    "fd_maturing_in_30d": 0,
    "products_dropped_90d": 3,
    "complaints_30d": 1,
    "unresolved_complaints": 0,
    "failed_transactions_30d": 2,
    "avg_resolution_time_hrs": 14.6935,
    "emi_bounce_30d": 0,
    "branch_code": "BR-125",
    "card_colour": "black"
  },
  "actual_current_month_churn": 0
}
```

#### Model 1 Output

```json
{
  "churn_probability": 48.15,
  "raw_churn_probability": 53.26,
  "risk_score": 80.56,
  "churn_prediction": "Yes",
  "risk_level": "High",
  "top_risk_factors": [
    {
      "factor": "balance_change_30d",
      "value": -37.7748
    },
    {
      "factor": "card_spend_change_30d",
      "value": -55.3749
    },
    {
      "factor": "salary_missing_days",
      "value": 6.0
    },
    {
      "factor": "tenure_months",
      "value": 35
    },
    {
      "factor": "days_since_last_transaction",
      "value": 16
    }
  ]
}
```

#### Model 1 v2 Input

```json
{
  "customer_id": "C12090",
  "customer_name": "Naveen Tella",
  "prediction_date": "2026-05-01",
  "target_month": "2026-06-01",
  "profile": {
    "tenure_months": 35,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 1,
    "has_credit_card": 0,
    "has_loan": 0
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 5,
      "balance_change_30d": 18.4361,
      "transaction_change_30d": 18.4717,
      "card_spend_change_30d": 18.2255,
      "app_login_change_30d": 29.0909,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -0.8304,
      "upi_share_of_spend": 0.3633,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 3,
      "avg_resolution_time_hrs": 1.0,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-02-01",
      "days_since_last_transaction": 4,
      "balance_change_30d": 5.6419,
      "transaction_change_30d": 28.7183,
      "card_spend_change_30d": -3.0275,
      "app_login_change_30d": 23.6453,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": 18.5944,
      "upi_share_of_spend": 0.4128,
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
      "balance_change_30d": 5.5455,
      "transaction_change_30d": -10.5556,
      "card_spend_change_30d": 13.1415,
      "app_login_change_30d": -23.2475,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": 3.4708,
      "upi_share_of_spend": 0.5206,
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
      "balance_change_30d": -27.5558,
      "transaction_change_30d": -33.4207,
      "card_spend_change_30d": -19.4304,
      "app_login_change_30d": 2.7368,
      "salary_missing_days": 4.0,
      "external_transfer_change_30d": 31.1697,
      "upi_share_of_spend": 0.5172,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 1,
      "complaints_30d": 2,
      "unresolved_complaints": 2,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 46.6352,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-05-01",
      "days_since_last_transaction": 22,
      "balance_change_30d": -48.976,
      "transaction_change_30d": -48.1033,
      "card_spend_change_30d": -30.8633,
      "app_login_change_30d": -59.4922,
      "salary_missing_days": 7.0,
      "external_transfer_change_30d": 97.5553,
      "upi_share_of_spend": 0.6923,
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
  "churn_probability": 47.78,
  "raw_churn_probability": 94.65,
  "probability_mode": "sigmoid",
  "risk_score": 80.42,
  "churn_prediction": "Yes",
  "risk_level": "High",
  "top_risk_factors": [
    {
      "factor": "latest_days_since_last_transaction",
      "value": 22,
      "message": "Customer has gone longer without transacting.",
      "contribution": 0.6416680812835693
    },
    {
      "factor": "latest_transaction_change_30d",
      "value": -48.1033,
      "message": "Transaction activity has been falling across recent months.",
      "contribution": 0.39285027980804443
    },
    {
      "factor": "latest_salary_missing_days",
      "value": 7.0,
      "message": "This signal increased churn risk.",
      "contribution": 0.386263906955719
    },
    {
      "factor": "latest_balance_change_30d",
      "value": -48.976,
      "message": "Balance has been falling across recent months.",
      "contribution": 0.2249099761247635
    },
    {
      "factor": "latest_vs_avg_upi_share_of_spend_available_history",
      "value": 0.1910600000000001,
      "message": "This signal increased churn risk.",
      "contribution": 0.2143438756465912
    }
  ]
}
```

### 17. Qasim Sarraf (`C12096`)

#### Model 1 Input

```json
{
  "customer_id": "C12096",
  "customer_name": "Qasim Sarraf",
  "snapshot_date": "2026-02-01",
  "customer": {
    "age": 58,
    "tenure_months": 169,
    "customer_segment": "pension",
    "income_regularity": "regular",
    "products_count": 1,
    "has_credit_card": 0,
    "has_loan": 0,
    "days_since_last_transaction": 3,
    "balance_change_30d": -13.0865,
    "transaction_change_30d": -7.1228,
    "card_spend_change_30d": 16.0898,
    "app_login_change_30d": 20.1985,
    "salary_missing_days": 1.0,
    "external_transfer_change_30d": 6.1703,
    "upi_share_of_spend": 0.5021,
    "fd_maturing_in_30d": 1,
    "products_dropped_90d": 0,
    "complaints_30d": 4,
    "unresolved_complaints": 3,
    "failed_transactions_30d": 4,
    "avg_resolution_time_hrs": 97.8229,
    "emi_bounce_30d": 0,
    "branch_code": "BR-103",
    "card_colour": "black"
  },
  "actual_current_month_churn": 1
}
```

#### Model 1 Output

```json
{
  "churn_probability": 36.3,
  "raw_churn_probability": 30.79,
  "risk_score": 76.11,
  "churn_prediction": "Yes",
  "risk_level": "High",
  "top_risk_factors": [
    {
      "factor": "avg_resolution_time_hrs",
      "value": 97.8229
    },
    {
      "factor": "fd_maturing_in_30d",
      "value": 1
    },
    {
      "factor": "complaints_30d",
      "value": 4
    },
    {
      "factor": "failed_transactions_30d",
      "value": 4
    },
    {
      "factor": "unresolved_complaints",
      "value": 3
    }
  ]
}
```

#### Model 1 v2 Input

```json
{
  "customer_id": "C12096",
  "customer_name": "Qasim Sarraf",
  "prediction_date": "2026-01-01",
  "target_month": "2026-02-01",
  "profile": {
    "tenure_months": 169,
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
      "balance_change_30d": -12.6141,
      "transaction_change_30d": 4.1325,
      "card_spend_change_30d": 14.5846,
      "app_login_change_30d": -19.8097,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -10.5943,
      "upi_share_of_spend": 0.4984,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 1,
      "complaints_30d": 2,
      "unresolved_complaints": 1,
      "failed_transactions_30d": 3,
      "avg_resolution_time_hrs": 38.3385,
      "emi_bounce_30d": 0
    }
  ],
  "actual_next_month_churn": 1
}
```

#### Model 1 v2 Output

```json
{
  "churn_probability": 5.65,
  "raw_churn_probability": 44.03,
  "probability_mode": "sigmoid",
  "risk_score": 16.96,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "latest_avg_resolution_time_hrs",
      "value": 38.3385,
      "message": "This signal increased churn risk.",
      "contribution": 0.2622227072715759
    },
    {
      "factor": "latest_failed_transactions_30d",
      "value": 3,
      "message": "Customer has recent failed transactions.",
      "contribution": 0.13243967294692993
    },
    {
      "factor": "latest_days_since_last_transaction",
      "value": 12,
      "message": "Customer has gone longer without transacting.",
      "contribution": 0.03523215651512146
    },
    {
      "factor": "external_transfer_change_30d_trend_6m",
      "value": 0.0,
      "message": "This signal increased churn risk.",
      "contribution": 0.03498905524611473
    },
    {
      "factor": "transaction_change_30d_trend_6m",
      "value": 0.0,
      "message": "This signal increased churn risk.",
      "contribution": 0.024751679971814156
    }
  ]
}
```

### 18. Bahadurjit Mahal (`C12211`)

#### Model 1 Input

```json
{
  "customer_id": "C12211",
  "customer_name": "Bahadurjit Mahal",
  "snapshot_date": "2026-06-01",
  "customer": {
    "age": 42,
    "tenure_months": 77,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 1,
    "has_credit_card": 0,
    "has_loan": 0,
    "days_since_last_transaction": 5,
    "balance_change_30d": 0.5307,
    "transaction_change_30d": 8.319,
    "card_spend_change_30d": 18.745,
    "app_login_change_30d": 5.4284,
    "salary_missing_days": 0.0,
    "external_transfer_change_30d": 7.8163,
    "upi_share_of_spend": 0.1555,
    "fd_maturing_in_30d": 0,
    "products_dropped_90d": 0,
    "complaints_30d": 0,
    "unresolved_complaints": 0,
    "failed_transactions_30d": 0,
    "avg_resolution_time_hrs": 0.0,
    "emi_bounce_30d": 0,
    "branch_code": "BR-112",
    "card_colour": "black"
  },
  "actual_current_month_churn": 0
}
```

#### Model 1 Output

```json
{
  "churn_probability": 1.96,
  "raw_churn_probability": 1.7,
  "risk_score": 5.87,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "branch_code",
      "value": "BR-112"
    },
    {
      "factor": "upi_share_of_spend",
      "value": 0.1555
    },
    {
      "factor": "external_transfer_change_30d",
      "value": 7.8163
    },
    {
      "factor": "products_count",
      "value": 1
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
  "customer_id": "C12211",
  "customer_name": "Bahadurjit Mahal",
  "prediction_date": "2026-05-01",
  "target_month": "2026-06-01",
  "profile": {
    "tenure_months": 77,
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
      "balance_change_30d": 25.5193,
      "transaction_change_30d": 5.3848,
      "card_spend_change_30d": 1.5519,
      "app_login_change_30d": -4.947,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -46.48,
      "upi_share_of_spend": 0.1357,
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
      "balance_change_30d": 15.9855,
      "transaction_change_30d": 8.3178,
      "card_spend_change_30d": 11.8574,
      "app_login_change_30d": 18.2588,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": 16.7303,
      "upi_share_of_spend": 0.2497,
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
      "days_since_last_transaction": 13,
      "balance_change_30d": 0.7836,
      "transaction_change_30d": 9.8646,
      "card_spend_change_30d": 0.2279,
      "app_login_change_30d": -0.084,
      "salary_missing_days": 5.0,
      "external_transfer_change_30d": 18.6139,
      "upi_share_of_spend": 0.1901,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 16.3322,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-04-01",
      "days_since_last_transaction": 14,
      "balance_change_30d": -24.1045,
      "transaction_change_30d": -3.1026,
      "card_spend_change_30d": 8.1744,
      "app_login_change_30d": -18.1491,
      "salary_missing_days": 1.0,
      "external_transfer_change_30d": 13.0243,
      "upi_share_of_spend": 0.1293,
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
      "balance_change_30d": 16.8987,
      "transaction_change_30d": 18.8949,
      "card_spend_change_30d": 44.2477,
      "app_login_change_30d": 16.9153,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -43.159,
      "upi_share_of_spend": 0.1325,
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
  "churn_probability": 3.08,
  "raw_churn_probability": 32.25,
  "probability_mode": "sigmoid",
  "risk_score": 9.24,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "latest_fd_maturing_in_30d",
      "value": 1,
      "message": "Customer has a fixed deposit maturing soon.",
      "contribution": 0.21764664351940155
    },
    {
      "factor": "sum_fd_maturing_in_30d_3m",
      "value": 1.0,
      "message": "Customer has a fixed deposit maturing soon.",
      "contribution": 0.08995722979307175
    },
    {
      "factor": "latest_external_transfer_change_30d",
      "value": -43.159,
      "message": "This signal increased churn risk.",
      "contribution": 0.07368414103984833
    },
    {
      "factor": "balance_change_30d_trend_6m",
      "value": -5.733120000000005,
      "message": "Balance has been falling across recent months.",
      "contribution": 0.038398899137973785
    },
    {
      "factor": "latest_vs_avg_external_transfer_change_30d_available_history",
      "value": -34.9049,
      "message": "This signal increased churn risk.",
      "contribution": 0.03812900558114052
    }
  ]
}
```

### 19. Girish Bhargava (`C12247`)

#### Model 1 Input

```json
{
  "customer_id": "C12247",
  "customer_name": "Girish Bhargava",
  "snapshot_date": "2026-06-01",
  "customer": {
    "age": 63,
    "tenure_months": 160,
    "customer_segment": "pension",
    "income_regularity": "regular",
    "products_count": 1,
    "has_credit_card": 0,
    "has_loan": 0,
    "days_since_last_transaction": 13,
    "balance_change_30d": 2.5097,
    "transaction_change_30d": 17.4389,
    "card_spend_change_30d": 3.1463,
    "app_login_change_30d": 15.5659,
    "salary_missing_days": 0.0,
    "external_transfer_change_30d": -28.9988,
    "upi_share_of_spend": 0.1994,
    "fd_maturing_in_30d": 0,
    "products_dropped_90d": 0,
    "complaints_30d": 3,
    "unresolved_complaints": 0,
    "failed_transactions_30d": 1,
    "avg_resolution_time_hrs": 57.7989,
    "emi_bounce_30d": 0,
    "branch_code": "BR-115",
    "card_colour": "silver"
  },
  "actual_current_month_churn": 0
}
```

#### Model 1 Output

```json
{
  "churn_probability": 3.74,
  "raw_churn_probability": 4.64,
  "risk_score": 11.21,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "avg_resolution_time_hrs",
      "value": 57.7989
    },
    {
      "factor": "complaints_30d",
      "value": 3
    },
    {
      "factor": "days_since_last_transaction",
      "value": 13
    },
    {
      "factor": "app_login_change_30d",
      "value": 15.5659
    },
    {
      "factor": "age",
      "value": 63
    }
  ]
}
```

#### Model 1 v2 Input

```json
{
  "customer_id": "C12247",
  "customer_name": "Girish Bhargava",
  "prediction_date": "2026-05-01",
  "target_month": "2026-06-01",
  "profile": {
    "tenure_months": 160,
    "customer_segment": "pension",
    "income_regularity": "regular",
    "products_count": 1,
    "has_credit_card": 0,
    "has_loan": 0
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 2,
      "balance_change_30d": 2.1403,
      "transaction_change_30d": -8.0953,
      "card_spend_change_30d": 18.1087,
      "app_login_change_30d": 7.6995,
      "salary_missing_days": 1.0,
      "external_transfer_change_30d": 15.84,
      "upi_share_of_spend": 0.1048,
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
      "days_since_last_transaction": 3,
      "balance_change_30d": 0.0887,
      "transaction_change_30d": 4.8129,
      "card_spend_change_30d": 10.0087,
      "app_login_change_30d": 5.4667,
      "salary_missing_days": 2.0,
      "external_transfer_change_30d": -8.0217,
      "upi_share_of_spend": 0.0285,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 3,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 17.5833,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-03-01",
      "days_since_last_transaction": 2,
      "balance_change_30d": 11.3999,
      "transaction_change_30d": 20.5081,
      "card_spend_change_30d": 15.5547,
      "app_login_change_30d": 24.6092,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -32.3503,
      "upi_share_of_spend": 0.0562,
      "fd_maturing_in_30d": 1,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 29.6204,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-04-01",
      "days_since_last_transaction": 0,
      "balance_change_30d": 17.377,
      "transaction_change_30d": 11.7707,
      "card_spend_change_30d": 46.1911,
      "app_login_change_30d": 15.8025,
      "salary_missing_days": 1.0,
      "external_transfer_change_30d": 32.1701,
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
      "days_since_last_transaction": 10,
      "balance_change_30d": 24.0464,
      "transaction_change_30d": -11.3456,
      "card_spend_change_30d": -22.6556,
      "app_login_change_30d": 8.6376,
      "salary_missing_days": 3.0,
      "external_transfer_change_30d": 23.2218,
      "upi_share_of_spend": 0.2234,
      "fd_maturing_in_30d": 1,
      "products_dropped_90d": 0,
      "complaints_30d": 2,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 2,
      "avg_resolution_time_hrs": 4.5136,
      "emi_bounce_30d": 0
    }
  ],
  "actual_next_month_churn": 0
}
```

#### Model 1 v2 Output

```json
{
  "churn_probability": 3.87,
  "raw_churn_probability": 36.66,
  "probability_mode": "sigmoid",
  "risk_score": 11.62,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "latest_vs_avg_upi_share_of_spend_available_history",
      "value": 0.14082,
      "message": "This signal increased churn risk.",
      "contribution": 0.16311605274677277
    },
    {
      "factor": "latest_salary_missing_days",
      "value": 3.0,
      "message": "This signal increased churn risk.",
      "contribution": 0.14445973932743073
    },
    {
      "factor": "latest_fd_maturing_in_30d",
      "value": 1,
      "message": "Customer has a fixed deposit maturing soon.",
      "contribution": 0.13868799805641174
    },
    {
      "factor": "days_since_last_transaction_trend_6m",
      "value": 1.2999999999999998,
      "message": "Customer has gone longer without transacting.",
      "contribution": 0.0941445529460907
    },
    {
      "factor": "sum_fd_maturing_in_30d_3m",
      "value": 2.0,
      "message": "Customer has a fixed deposit maturing soon.",
      "contribution": 0.09370903670787811
    }
  ]
}
```

### 20. Mugdha Sunder (`C12336`)

#### Model 1 Input

```json
{
  "customer_id": "C12336",
  "customer_name": "Mugdha Sunder",
  "snapshot_date": "2026-06-01",
  "customer": {
    "age": 58,
    "tenure_months": 40,
    "customer_segment": "business",
    "income_regularity": "irregular",
    "products_count": 2,
    "has_credit_card": 0,
    "has_loan": 1,
    "days_since_last_transaction": 9,
    "balance_change_30d": -5.2719,
    "transaction_change_30d": 12.0045,
    "card_spend_change_30d": -13.8446,
    "app_login_change_30d": -8.0263,
    "salary_missing_days": null,
    "external_transfer_change_30d": 45.4855,
    "upi_share_of_spend": 0.5039,
    "fd_maturing_in_30d": 0,
    "products_dropped_90d": 0,
    "complaints_30d": 0,
    "unresolved_complaints": 0,
    "failed_transactions_30d": 1,
    "avg_resolution_time_hrs": 0.0,
    "emi_bounce_30d": 0,
    "branch_code": "BR-129",
    "card_colour": "green"
  },
  "actual_current_month_churn": 0
}
```

#### Model 1 Output

```json
{
  "churn_probability": 1.96,
  "raw_churn_probability": 1.9,
  "risk_score": 5.87,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "tenure_months",
      "value": 40
    },
    {
      "factor": "branch_code",
      "value": "BR-129"
    },
    {
      "factor": "external_transfer_change_30d",
      "value": 45.4855
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
  "customer_id": "C12336",
  "customer_name": "Mugdha Sunder",
  "prediction_date": "2026-05-01",
  "target_month": "2026-06-01",
  "profile": {
    "tenure_months": 40,
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
      "balance_change_30d": 3.6448,
      "transaction_change_30d": -5.0699,
      "card_spend_change_30d": -0.8586,
      "app_login_change_30d": -14.2766,
      "salary_missing_days": null,
      "external_transfer_change_30d": 0.1175,
      "upi_share_of_spend": 0.523,
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
      "balance_change_30d": -14.1824,
      "transaction_change_30d": -5.3544,
      "card_spend_change_30d": -19.9842,
      "app_login_change_30d": -21.4501,
      "salary_missing_days": null,
      "external_transfer_change_30d": 7.0642,
      "upi_share_of_spend": 0.554,
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
      "balance_change_30d": -25.1146,
      "transaction_change_30d": -20.7553,
      "card_spend_change_30d": -21.9753,
      "app_login_change_30d": -22.3834,
      "salary_missing_days": null,
      "external_transfer_change_30d": 1.363,
      "upi_share_of_spend": 0.5435,
      "fd_maturing_in_30d": 1,
      "products_dropped_90d": 2,
      "complaints_30d": 0,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 0.0,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-04-01",
      "days_since_last_transaction": 4,
      "balance_change_30d": 6.4768,
      "transaction_change_30d": -15.6433,
      "card_spend_change_30d": -9.8094,
      "app_login_change_30d": -2.227,
      "salary_missing_days": null,
      "external_transfer_change_30d": 6.625,
      "upi_share_of_spend": 0.4402,
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
      "balance_change_30d": 8.2752,
      "transaction_change_30d": 20.6408,
      "card_spend_change_30d": -8.3694,
      "app_login_change_30d": 10.0579,
      "salary_missing_days": null,
      "external_transfer_change_30d": -3.3096,
      "upi_share_of_spend": 0.3871,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 1,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 26.0001,
      "emi_bounce_30d": 0
    }
  ],
  "actual_next_month_churn": 0
}
```

#### Model 1 v2 Output

```json
{
  "churn_probability": 2.02,
  "raw_churn_probability": 24.23,
  "probability_mode": "sigmoid",
  "risk_score": 6.07,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "sum_fd_maturing_in_30d_3m",
      "value": 1.0,
      "message": "Customer has a fixed deposit maturing soon.",
      "contribution": 0.11870409548282623
    },
    {
      "factor": "max_days_since_last_transaction_3m",
      "value": 12.0,
      "message": "Customer has gone longer without transacting.",
      "contribution": 0.017499752342700958
    },
    {
      "factor": "latest_vs_avg_card_spend_change_30d_available_history",
      "value": 3.829979999999999,
      "message": "This signal increased churn risk.",
      "contribution": 0.016174867749214172
    },
    {
      "factor": "sum_fd_maturing_in_30d_6m",
      "value": 1.0,
      "message": "Customer has a fixed deposit maturing soon.",
      "contribution": 0.01474044844508171
    },
    {
      "factor": "avg_app_login_change_30d_3m",
      "value": -4.850833333333334,
      "message": "App usage has been falling across recent months.",
      "contribution": 0.0057327598333358765
    }
  ]
}
```

### 21. Amrita Sahni (`C12339`)

#### Model 1 Input

```json
{
  "customer_id": "C12339",
  "customer_name": "Amrita Sahni",
  "snapshot_date": "2026-06-01",
  "customer": {
    "age": 53,
    "tenure_months": 1,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 3,
    "has_credit_card": 1,
    "has_loan": 1,
    "days_since_last_transaction": 16,
    "balance_change_30d": 12.6984,
    "transaction_change_30d": -10.9263,
    "card_spend_change_30d": -0.9029,
    "app_login_change_30d": -1.0008,
    "salary_missing_days": 4.0,
    "external_transfer_change_30d": 2.6245,
    "upi_share_of_spend": 0.3835,
    "fd_maturing_in_30d": 1,
    "products_dropped_90d": 1,
    "complaints_30d": 2,
    "unresolved_complaints": 2,
    "failed_transactions_30d": 4,
    "avg_resolution_time_hrs": 31.2713,
    "emi_bounce_30d": 0,
    "branch_code": "BR-111",
    "card_colour": "green"
  },
  "actual_current_month_churn": 0
}
```

#### Model 1 Output

```json
{
  "churn_probability": 18.06,
  "raw_churn_probability": 24.69,
  "risk_score": 62.22,
  "churn_prediction": "Yes",
  "risk_level": "Medium",
  "top_risk_factors": [
    {
      "factor": "fd_maturing_in_30d",
      "value": 1
    },
    {
      "factor": "tenure_months",
      "value": 1
    },
    {
      "factor": "failed_transactions_30d",
      "value": 4
    },
    {
      "factor": "salary_missing_days",
      "value": 4.0
    },
    {
      "factor": "complaints_30d",
      "value": 2
    }
  ]
}
```

#### Model 1 v2 Input

```json
{
  "customer_id": "C12339",
  "customer_name": "Amrita Sahni",
  "prediction_date": "2026-05-01",
  "target_month": "2026-06-01",
  "profile": {
    "tenure_months": 1,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 3,
    "has_credit_card": 1,
    "has_loan": 1
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 7,
      "balance_change_30d": 28.2643,
      "transaction_change_30d": 12.3991,
      "card_spend_change_30d": 8.9932,
      "app_login_change_30d": 19.8066,
      "salary_missing_days": 3.0,
      "external_transfer_change_30d": 0.7476,
      "upi_share_of_spend": 0.335,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 7.1319,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-02-01",
      "days_since_last_transaction": 2,
      "balance_change_30d": 29.4972,
      "transaction_change_30d": 13.4865,
      "card_spend_change_30d": 39.4906,
      "app_login_change_30d": -0.1408,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -18.8592,
      "upi_share_of_spend": 0.2884,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 3,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 3,
      "avg_resolution_time_hrs": 7.0362,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-03-01",
      "days_since_last_transaction": 6,
      "balance_change_30d": 39.7642,
      "transaction_change_30d": 10.3504,
      "card_spend_change_30d": -20.7674,
      "app_login_change_30d": -5.2581,
      "salary_missing_days": 1.0,
      "external_transfer_change_30d": -41.0579,
      "upi_share_of_spend": 0.2944,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 3.6144,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-04-01",
      "days_since_last_transaction": 7,
      "balance_change_30d": 7.1192,
      "transaction_change_30d": 3.5563,
      "card_spend_change_30d": 21.2858,
      "app_login_change_30d": 13.6604,
      "salary_missing_days": 2.0,
      "external_transfer_change_30d": -25.1342,
      "upi_share_of_spend": 0.3215,
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
      "days_since_last_transaction": 9,
      "balance_change_30d": 11.3848,
      "transaction_change_30d": 51.8456,
      "card_spend_change_30d": -2.5745,
      "app_login_change_30d": 1.4124,
      "salary_missing_days": 1.0,
      "external_transfer_change_30d": -11.8416,
      "upi_share_of_spend": 0.4045,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 8.3906,
      "emi_bounce_30d": 0
    }
  ],
  "actual_next_month_churn": 0
}
```

#### Model 1 v2 Output

```json
{
  "churn_probability": 2.8,
  "raw_churn_probability": 30.4,
  "probability_mode": "sigmoid",
  "risk_score": 8.39,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "latest_vs_avg_upi_share_of_spend_available_history",
      "value": 0.0757399999999999,
      "message": "This signal increased churn risk.",
      "contribution": 0.14142955839633942
    },
    {
      "factor": "sum_complaints_30d_6m",
      "value": 6.0,
      "message": "Customer has recent complaint activity.",
      "contribution": 0.05481298267841339
    },
    {
      "factor": "avg_transaction_change_30d_6m",
      "value": 18.32758,
      "message": "This signal increased churn risk.",
      "contribution": 0.04470724239945412
    },
    {
      "factor": "balance_change_30d_trend_6m",
      "value": -5.613700000000003,
      "message": "Balance has been falling across recent months.",
      "contribution": 0.04358555004000664
    },
    {
      "factor": "sum_complaints_30d_available_history",
      "value": 6.0,
      "message": "Customer has recent complaint activity.",
      "contribution": 0.03606070950627327
    }
  ]
}
```

### 22. Madhavi Date (`C12391`)

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

### 23. Netra Ravi (`C12607`)

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

### 24. Lohit Jayaraman (`C12715`)

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

### 25. Shivansh Kar (`C12820`)

#### Model 1 Input

```json
{
  "customer_id": "C12820",
  "customer_name": "Shivansh Kar",
  "snapshot_date": "2026-06-01",
  "customer": {
    "age": 42,
    "tenure_months": 76,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 2,
    "has_credit_card": 1,
    "has_loan": 0,
    "days_since_last_transaction": 13,
    "balance_change_30d": -13.8443,
    "transaction_change_30d": 9.1767,
    "card_spend_change_30d": -6.6338,
    "app_login_change_30d": 34.6991,
    "salary_missing_days": 0.0,
    "external_transfer_change_30d": -20.973,
    "upi_share_of_spend": 0.235,
    "fd_maturing_in_30d": 0,
    "products_dropped_90d": 0,
    "complaints_30d": 2,
    "unresolved_complaints": 0,
    "failed_transactions_30d": 1,
    "avg_resolution_time_hrs": 25.935,
    "emi_bounce_30d": 0,
    "branch_code": "BR-130",
    "card_colour": "gold"
  },
  "actual_current_month_churn": 0
}
```

#### Model 1 Output

```json
{
  "churn_probability": 1.96,
  "raw_churn_probability": 2.44,
  "risk_score": 5.87,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "complaints_30d",
      "value": 2
    },
    {
      "factor": "app_login_change_30d",
      "value": 34.6991
    },
    {
      "factor": "days_since_last_transaction",
      "value": 13
    },
    {
      "factor": "upi_share_of_spend",
      "value": 0.235
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
  "customer_id": "C12820",
  "customer_name": "Shivansh Kar",
  "prediction_date": "2026-05-01",
  "target_month": "2026-06-01",
  "profile": {
    "tenure_months": 76,
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
      "balance_change_30d": 22.2905,
      "transaction_change_30d": 4.0397,
      "card_spend_change_30d": -11.0847,
      "app_login_change_30d": 17.3422,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -33.1068,
      "upi_share_of_spend": 0.2202,
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
      "balance_change_30d": 26.675,
      "transaction_change_30d": 25.4417,
      "card_spend_change_30d": -10.7772,
      "app_login_change_30d": 47.7101,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -53.7429,
      "upi_share_of_spend": 0.1349,
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
      "days_since_last_transaction": 0,
      "balance_change_30d": 14.316,
      "transaction_change_30d": -2.755,
      "card_spend_change_30d": 12.3957,
      "app_login_change_30d": -11.1105,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": 2.031,
      "upi_share_of_spend": 0.238,
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
      "balance_change_30d": 29.1551,
      "transaction_change_30d": 9.9087,
      "card_spend_change_30d": -8.4583,
      "app_login_change_30d": 14.5862,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -22.8724,
      "upi_share_of_spend": 0.1402,
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
      "balance_change_30d": -11.1686,
      "transaction_change_30d": 4.5377,
      "card_spend_change_30d": -22.522,
      "app_login_change_30d": -3.2003,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": 10.7085,
      "upi_share_of_spend": 0.2128,
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
  "churn_probability": 2.64,
  "raw_churn_probability": 29.28,
  "probability_mode": "sigmoid",
  "risk_score": 7.91,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "balance_change_30d_trend_6m",
      "value": -6.4438100000000045,
      "message": "Balance has been falling across recent months.",
      "contribution": 0.043914906680583954
    },
    {
      "factor": "external_transfer_change_30d_trend_6m",
      "value": 11.850110000000004,
      "message": "External transfers have increased.",
      "contribution": 0.03942312300205231
    },
    {
      "factor": "transaction_change_30d_trend_6m",
      "value": -1.453700000000001,
      "message": "Transaction activity has been falling across recent months.",
      "contribution": 0.027720356360077858
    },
    {
      "factor": "latest_vs_avg_upi_share_of_spend_available_history",
      "value": 0.0235799999999999,
      "message": "This signal increased churn risk.",
      "contribution": 0.024891456589102745
    },
    {
      "factor": "latest_card_spend_change_30d",
      "value": -22.522,
      "message": "Card spending has been falling across recent months.",
      "contribution": 0.024803586304187775
    }
  ]
}
```

### 26. Shaurya Kamdar (`C12831`)

#### Model 1 Input

```json
{
  "customer_id": "C12831",
  "customer_name": "Shaurya Kamdar",
  "snapshot_date": "2026-06-01",
  "customer": {
    "age": 40,
    "tenure_months": 88,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 1,
    "has_credit_card": 0,
    "has_loan": 0,
    "days_since_last_transaction": 0,
    "balance_change_30d": 43.6327,
    "transaction_change_30d": 41.9903,
    "card_spend_change_30d": 15.3056,
    "app_login_change_30d": 34.2218,
    "salary_missing_days": 0.0,
    "external_transfer_change_30d": -60.482,
    "upi_share_of_spend": 0.0,
    "fd_maturing_in_30d": 0,
    "products_dropped_90d": 0,
    "complaints_30d": 0,
    "unresolved_complaints": 0,
    "failed_transactions_30d": 1,
    "avg_resolution_time_hrs": 0.0,
    "emi_bounce_30d": 0,
    "branch_code": "BR-112",
    "card_colour": "blue"
  },
  "actual_current_month_churn": 0
}
```

#### Model 1 Output

```json
{
  "churn_probability": 1.96,
  "raw_churn_probability": 1.74,
  "risk_score": 5.87,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "branch_code",
      "value": "BR-112"
    },
    {
      "factor": "upi_share_of_spend",
      "value": 0.0
    },
    {
      "factor": "app_login_change_30d",
      "value": 34.2218
    },
    {
      "factor": "products_count",
      "value": 1
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
  "customer_id": "C12831",
  "customer_name": "Shaurya Kamdar",
  "prediction_date": "2026-05-01",
  "target_month": "2026-06-01",
  "profile": {
    "tenure_months": 88,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 1,
    "has_credit_card": 0,
    "has_loan": 0
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 12,
      "balance_change_30d": -4.783,
      "transaction_change_30d": -20.1544,
      "card_spend_change_30d": -13.8233,
      "app_login_change_30d": 3.5366,
      "salary_missing_days": 4.0,
      "external_transfer_change_30d": 19.401,
      "upi_share_of_spend": 0.2338,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 19.8302,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-02-01",
      "days_since_last_transaction": 0,
      "balance_change_30d": -16.9535,
      "transaction_change_30d": 1.463,
      "card_spend_change_30d": 8.0114,
      "app_login_change_30d": -12.7132,
      "salary_missing_days": 2.0,
      "external_transfer_change_30d": -13.7928,
      "upi_share_of_spend": 0.102,
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
      "balance_change_30d": -6.6618,
      "transaction_change_30d": -3.5228,
      "card_spend_change_30d": 11.0208,
      "app_login_change_30d": 3.3513,
      "salary_missing_days": 3.0,
      "external_transfer_change_30d": 25.5234,
      "upi_share_of_spend": 0.0876,
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
      "balance_change_30d": 26.0039,
      "transaction_change_30d": 23.7094,
      "card_spend_change_30d": 27.7043,
      "app_login_change_30d": 30.2033,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": 0.5998,
      "upi_share_of_spend": 0.0985,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 1,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 6.8804,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-05-01",
      "days_since_last_transaction": 0,
      "balance_change_30d": 24.0994,
      "transaction_change_30d": 19.3316,
      "card_spend_change_30d": 40.181,
      "app_login_change_30d": 24.9196,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -2.8092,
      "upi_share_of_spend": 0.0888,
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
  "churn_probability": 1.38,
  "raw_churn_probability": 17.0,
  "probability_mode": "sigmoid",
  "risk_score": 4.14,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "card_spend_change_30d_trend_6m",
      "value": 12.77015,
      "message": "This signal increased churn risk.",
      "contribution": 0.03367763012647629
    },
    {
      "factor": "avg_upi_share_of_spend_available_history",
      "value": 0.12214,
      "message": "This signal increased churn risk.",
      "contribution": 0.009652705863118172
    },
    {
      "factor": "avg_upi_share_of_spend_6m",
      "value": 0.12214,
      "message": "This signal increased churn risk.",
      "contribution": 0.008168664760887623
    },
    {
      "factor": "latest_vs_avg_transaction_change_30d_available_history",
      "value": 15.166240000000002,
      "message": "This signal increased churn risk.",
      "contribution": 0.0041139558888971806
    },
    {
      "factor": "count_balance_drop_3m",
      "value": 1,
      "message": "This signal increased churn risk.",
      "contribution": 0.0038415761664509773
    }
  ]
}
```

### 27. Qasim Ravi (`C12850`)

#### Model 1 Input

```json
{
  "customer_id": "C12850",
  "customer_name": "Qasim Ravi",
  "snapshot_date": "2026-06-01",
  "customer": {
    "age": 34,
    "tenure_months": 68,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 3,
    "has_credit_card": 1,
    "has_loan": 0,
    "days_since_last_transaction": 12,
    "balance_change_30d": 23.3868,
    "transaction_change_30d": -5.3584,
    "card_spend_change_30d": 5.3778,
    "app_login_change_30d": -1.4328,
    "salary_missing_days": 0.0,
    "external_transfer_change_30d": 32.8477,
    "upi_share_of_spend": 0.6323,
    "fd_maturing_in_30d": 0,
    "products_dropped_90d": 0,
    "complaints_30d": 0,
    "unresolved_complaints": 0,
    "failed_transactions_30d": 1,
    "avg_resolution_time_hrs": 0.0,
    "emi_bounce_30d": 0,
    "branch_code": "BR-101",
    "card_colour": "blue"
  },
  "actual_current_month_churn": 0
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
      "factor": "branch_code",
      "value": "BR-101"
    },
    {
      "factor": "card_colour",
      "value": "blue"
    },
    {
      "factor": "external_transfer_change_30d",
      "value": 32.8477
    },
    {
      "factor": "has_loan",
      "value": 0
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
  "customer_id": "C12850",
  "customer_name": "Qasim Ravi",
  "prediction_date": "2026-05-01",
  "target_month": "2026-06-01",
  "profile": {
    "tenure_months": 68,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 3,
    "has_credit_card": 1,
    "has_loan": 0
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 9,
      "balance_change_30d": -12.2011,
      "transaction_change_30d": -9.4962,
      "card_spend_change_30d": -13.878,
      "app_login_change_30d": -1.28,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": 13.5503,
      "upi_share_of_spend": 0.6735,
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
      "days_since_last_transaction": 19,
      "balance_change_30d": -13.3724,
      "transaction_change_30d": -9.9892,
      "card_spend_change_30d": -7.1345,
      "app_login_change_30d": -3.7552,
      "salary_missing_days": 3.0,
      "external_transfer_change_30d": 42.9687,
      "upi_share_of_spend": 0.773,
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
      "balance_change_30d": -6.8391,
      "transaction_change_30d": -5.8798,
      "card_spend_change_30d": -4.0028,
      "app_login_change_30d": 25.2085,
      "salary_missing_days": 1.0,
      "external_transfer_change_30d": -12.7917,
      "upi_share_of_spend": 0.6534,
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
      "balance_change_30d": 15.2703,
      "transaction_change_30d": 26.9963,
      "card_spend_change_30d": 2.8657,
      "app_login_change_30d": 32.5484,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": 6.7091,
      "upi_share_of_spend": 0.6017,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 2,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 12.2397,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-05-01",
      "days_since_last_transaction": 14,
      "balance_change_30d": -18.088,
      "transaction_change_30d": 19.4428,
      "card_spend_change_30d": 17.4959,
      "app_login_change_30d": -3.7324,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -0.9687,
      "upi_share_of_spend": 0.662,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 1.0,
      "emi_bounce_30d": 0
    }
  ],
  "actual_next_month_churn": 0
}
```

#### Model 1 v2 Output

```json
{
  "churn_probability": 5.25,
  "raw_churn_probability": 42.56,
  "probability_mode": "sigmoid",
  "risk_score": 15.74,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "latest_days_since_last_transaction",
      "value": 14,
      "message": "Customer has gone longer without transacting.",
      "contribution": 0.5307373404502869
    },
    {
      "factor": "count_balance_drop_6m",
      "value": 4,
      "message": "This signal increased churn risk.",
      "contribution": 0.07274015247821808
    },
    {
      "factor": "latest_balance_change_30d",
      "value": -18.088,
      "message": "Balance has been falling across recent months.",
      "contribution": 0.062075335532426834
    },
    {
      "factor": "count_quiet_customer_3m",
      "value": 2,
      "message": "This signal increased churn risk.",
      "contribution": 0.058752454817295074
    },
    {
      "factor": "card_spend_change_30d_trend_6m",
      "value": 7.274800000000001,
      "message": "This signal increased churn risk.",
      "contribution": 0.026442058384418488
    }
  ]
}
```

### 28. Madhavi Rattan (`C12991`)

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

### 29. Tara Sangha (`C13175`)

#### Model 1 Input

```json
{
  "customer_id": "C13175",
  "customer_name": "Tara Sangha",
  "snapshot_date": "2026-06-01",
  "customer": {
    "age": 30,
    "tenure_months": 67,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 1,
    "has_credit_card": 0,
    "has_loan": 0,
    "days_since_last_transaction": 10,
    "balance_change_30d": -6.0917,
    "transaction_change_30d": 19.5522,
    "card_spend_change_30d": 1.3409,
    "app_login_change_30d": -33.3181,
    "salary_missing_days": 3.0,
    "external_transfer_change_30d": -17.9729,
    "upi_share_of_spend": 0.6939,
    "fd_maturing_in_30d": 0,
    "products_dropped_90d": 0,
    "complaints_30d": 0,
    "unresolved_complaints": 0,
    "failed_transactions_30d": 0,
    "avg_resolution_time_hrs": 0.0,
    "emi_bounce_30d": 0,
    "branch_code": "BR-129",
    "card_colour": "green"
  },
  "actual_current_month_churn": 0
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
      "factor": "salary_missing_days",
      "value": 3.0
    },
    {
      "factor": "branch_code",
      "value": "BR-129"
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
  "customer_id": "C13175",
  "customer_name": "Tara Sangha",
  "prediction_date": "2026-05-01",
  "target_month": "2026-06-01",
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
      "days_since_last_transaction": 5,
      "balance_change_30d": 18.4757,
      "transaction_change_30d": 17.2829,
      "card_spend_change_30d": 1.8621,
      "app_login_change_30d": 11.3724,
      "salary_missing_days": 1.0,
      "external_transfer_change_30d": 17.1406,
      "upi_share_of_spend": 0.5466,
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
      "balance_change_30d": -22.1609,
      "transaction_change_30d": -6.3892,
      "card_spend_change_30d": -26.4177,
      "app_login_change_30d": -1.7993,
      "salary_missing_days": 3.0,
      "external_transfer_change_30d": 18.1208,
      "upi_share_of_spend": 0.5987,
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
      "balance_change_30d": -23.5419,
      "transaction_change_30d": 10.7528,
      "card_spend_change_30d": 13.5378,
      "app_login_change_30d": -1.4278,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -17.5707,
      "upi_share_of_spend": 0.6248,
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
      "days_since_last_transaction": 13,
      "balance_change_30d": -6.5437,
      "transaction_change_30d": -17.2244,
      "card_spend_change_30d": 4.7225,
      "app_login_change_30d": 0.8163,
      "salary_missing_days": 1.0,
      "external_transfer_change_30d": -3.5242,
      "upi_share_of_spend": 0.6784,
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
      "days_since_last_transaction": 16,
      "balance_change_30d": -12.7232,
      "transaction_change_30d": -16.4256,
      "card_spend_change_30d": -27.073,
      "app_login_change_30d": -34.1518,
      "salary_missing_days": 3.0,
      "external_transfer_change_30d": 16.8791,
      "upi_share_of_spend": 0.6716,
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
  "churn_probability": 19.52,
  "raw_churn_probability": 69.99,
  "probability_mode": "sigmoid",
  "risk_score": 68.09,
  "churn_prediction": "Yes",
  "risk_level": "Medium",
  "top_risk_factors": [
    {
      "factor": "latest_days_since_last_transaction",
      "value": 16,
      "message": "Customer has gone longer without transacting.",
      "contribution": 0.43233394622802734
    },
    {
      "factor": "latest_salary_missing_days",
      "value": 3.0,
      "message": "This signal increased churn risk.",
      "contribution": 0.31707674264907837
    },
    {
      "factor": "days_since_last_transaction_trend_6m",
      "value": 2.8,
      "message": "Customer has gone longer without transacting.",
      "contribution": 0.1561855524778366
    },
    {
      "factor": "latest_vs_avg_upi_share_of_spend_available_history",
      "value": 0.0475799999999999,
      "message": "This signal increased churn risk.",
      "contribution": 0.09119242429733276
    },
    {
      "factor": "latest_app_login_change_30d",
      "value": -34.1518,
      "message": "App usage has been falling across recent months.",
      "contribution": 0.06794475764036179
    }
  ]
}
```

### 30. Chanchal Anne (`C13220`)

#### Model 1 Input

```json
{
  "customer_id": "C13220",
  "customer_name": "Chanchal Anne",
  "snapshot_date": "2026-06-01",
  "customer": {
    "age": 28,
    "tenure_months": 92,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 2,
    "has_credit_card": 1,
    "has_loan": 0,
    "days_since_last_transaction": 2,
    "balance_change_30d": 34.7873,
    "transaction_change_30d": 26.6859,
    "card_spend_change_30d": 24.2787,
    "app_login_change_30d": 4.3977,
    "salary_missing_days": 0.0,
    "external_transfer_change_30d": -46.4044,
    "upi_share_of_spend": 0.5343,
    "fd_maturing_in_30d": 0,
    "products_dropped_90d": 0,
    "complaints_30d": 0,
    "unresolved_complaints": 0,
    "failed_transactions_30d": 2,
    "avg_resolution_time_hrs": 0.0,
    "emi_bounce_30d": 0,
    "branch_code": "BR-121",
    "card_colour": "green"
  },
  "actual_current_month_churn": 0
}
```

#### Model 1 Output

```json
{
  "churn_probability": 1.96,
  "raw_churn_probability": 1.84,
  "risk_score": 5.87,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "branch_code",
      "value": "BR-121"
    },
    {
      "factor": "failed_transactions_30d",
      "value": 2
    },
    {
      "factor": "age",
      "value": 28
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
  "customer_id": "C13220",
  "customer_name": "Chanchal Anne",
  "prediction_date": "2026-05-01",
  "target_month": "2026-06-01",
  "profile": {
    "tenure_months": 92,
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
      "balance_change_30d": 22.3442,
      "transaction_change_30d": -2.406,
      "card_spend_change_30d": 9.6957,
      "app_login_change_30d": -32.0284,
      "salary_missing_days": 1.0,
      "external_transfer_change_30d": -38.4653,
      "upi_share_of_spend": 0.5502,
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
      "balance_change_30d": 6.8678,
      "transaction_change_30d": -0.7064,
      "card_spend_change_30d": 12.7753,
      "app_login_change_30d": 0.9397,
      "salary_missing_days": 1.0,
      "external_transfer_change_30d": 28.5068,
      "upi_share_of_spend": 0.6547,
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
      "balance_change_30d": 41.9651,
      "transaction_change_30d": 16.6207,
      "card_spend_change_30d": 34.6031,
      "app_login_change_30d": 27.1988,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -35.293,
      "upi_share_of_spend": 0.6378,
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
      "balance_change_30d": 47.6685,
      "transaction_change_30d": 42.9315,
      "card_spend_change_30d": 56.6771,
      "app_login_change_30d": 39.9934,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -34.0891,
      "upi_share_of_spend": 0.4788,
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
      "balance_change_30d": 39.9489,
      "transaction_change_30d": 44.828,
      "card_spend_change_30d": 38.7508,
      "app_login_change_30d": 33.7548,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -71.6996,
      "upi_share_of_spend": 0.4659,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 1,
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
  "churn_probability": 1.26,
  "raw_churn_probability": 15.31,
  "probability_mode": "sigmoid",
  "risk_score": 3.78,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "avg_balance_change_30d_6m",
      "value": 31.7589,
      "message": "This signal increased churn risk.",
      "contribution": 0.06990790367126465
    },
    {
      "factor": "latest_external_transfer_change_30d",
      "value": -71.6996,
      "message": "This signal increased churn risk.",
      "contribution": 0.061316974461078644
    },
    {
      "factor": "latest_vs_avg_external_transfer_change_30d_available_history",
      "value": -41.49156000000001,
      "message": "This signal increased churn risk.",
      "contribution": 0.04352891072630882
    },
    {
      "factor": "card_spend_change_30d_trend_6m",
      "value": 10.2012,
      "message": "This signal increased churn risk.",
      "contribution": 0.032399989664554596
    },
    {
      "factor": "avg_balance_change_30d_3m",
      "value": 43.19416666666667,
      "message": "This signal increased churn risk.",
      "contribution": 0.023178819566965103
    }
  ]
}
```

### 31. Dhriti Thakur (`C13379`)

#### Model 1 Input

```json
{
  "customer_id": "C13379",
  "customer_name": "Dhriti Thakur",
  "snapshot_date": "2026-06-01",
  "customer": {
    "age": 61,
    "tenure_months": 210,
    "customer_segment": "pension",
    "income_regularity": "regular",
    "products_count": 3,
    "has_credit_card": 0,
    "has_loan": 0,
    "days_since_last_transaction": 22,
    "balance_change_30d": -63.2104,
    "transaction_change_30d": -41.2159,
    "card_spend_change_30d": -58.6476,
    "app_login_change_30d": -51.6621,
    "salary_missing_days": 8.0,
    "external_transfer_change_30d": 80.3617,
    "upi_share_of_spend": 0.7439,
    "fd_maturing_in_30d": 0,
    "products_dropped_90d": 0,
    "complaints_30d": 0,
    "unresolved_complaints": 0,
    "failed_transactions_30d": 2,
    "avg_resolution_time_hrs": 0.0,
    "emi_bounce_30d": 0,
    "branch_code": "BR-102",
    "card_colour": "blue"
  },
  "actual_current_month_churn": 1
}
```

#### Model 1 Output

```json
{
  "churn_probability": 70.37,
  "raw_churn_probability": 66.86,
  "risk_score": 88.89,
  "churn_prediction": "Yes",
  "risk_level": "High",
  "top_risk_factors": [
    {
      "factor": "balance_change_30d",
      "value": -63.2104
    },
    {
      "factor": "card_spend_change_30d",
      "value": -58.6476
    },
    {
      "factor": "days_since_last_transaction",
      "value": 22
    },
    {
      "factor": "salary_missing_days",
      "value": 8.0
    },
    {
      "factor": "branch_code",
      "value": "BR-102"
    }
  ]
}
```

#### Model 1 v2 Input

```json
{
  "customer_id": "C13379",
  "customer_name": "Dhriti Thakur",
  "prediction_date": "2026-05-01",
  "target_month": "2026-06-01",
  "profile": {
    "tenure_months": 210,
    "customer_segment": "pension",
    "income_regularity": "regular",
    "products_count": 3,
    "has_credit_card": 0,
    "has_loan": 0
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 8,
      "balance_change_30d": 1.4631,
      "transaction_change_30d": 10.2926,
      "card_spend_change_30d": 4.9592,
      "app_login_change_30d": 4.7384,
      "salary_missing_days": 1.0,
      "external_transfer_change_30d": 11.6939,
      "upi_share_of_spend": 0.5548,
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
      "balance_change_30d": 13.0315,
      "transaction_change_30d": 4.7544,
      "card_spend_change_30d": 22.3046,
      "app_login_change_30d": 11.0447,
      "salary_missing_days": 2.0,
      "external_transfer_change_30d": -54.8894,
      "upi_share_of_spend": 0.4403,
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
      "balance_change_30d": -12.6913,
      "transaction_change_30d": -18.057,
      "card_spend_change_30d": -5.9702,
      "app_login_change_30d": -8.8898,
      "salary_missing_days": 4.0,
      "external_transfer_change_30d": 67.1082,
      "upi_share_of_spend": 0.4461,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 1,
      "complaints_30d": 0,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 0.0,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-04-01",
      "days_since_last_transaction": 18,
      "balance_change_30d": -48.1193,
      "transaction_change_30d": -21.2882,
      "card_spend_change_30d": -58.6931,
      "app_login_change_30d": -24.6332,
      "salary_missing_days": 5.0,
      "external_transfer_change_30d": 31.979,
      "upi_share_of_spend": 0.7238,
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
      "days_since_last_transaction": 20,
      "balance_change_30d": -56.6283,
      "transaction_change_30d": -54.3925,
      "card_spend_change_30d": -55.1619,
      "app_login_change_30d": -34.0444,
      "salary_missing_days": 6.0,
      "external_transfer_change_30d": 42.9745,
      "upi_share_of_spend": 0.7969,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 5,
      "avg_resolution_time_hrs": 15.9424,
      "emi_bounce_30d": 0
    }
  ],
  "actual_next_month_churn": 1
}
```

#### Model 1 v2 Output

```json
{
  "churn_probability": 46.44,
  "raw_churn_probability": 93.65,
  "probability_mode": "sigmoid",
  "risk_score": 79.91,
  "churn_prediction": "Yes",
  "risk_level": "High",
  "top_risk_factors": [
    {
      "factor": "latest_days_since_last_transaction",
      "value": 20,
      "message": "Customer has gone longer without transacting.",
      "contribution": 0.6472587585449219
    },
    {
      "factor": "latest_transaction_change_30d",
      "value": -54.3925,
      "message": "Transaction activity has been falling across recent months.",
      "contribution": 0.4769414961338043
    },
    {
      "factor": "latest_salary_missing_days",
      "value": 6.0,
      "message": "This signal increased churn risk.",
      "contribution": 0.2856617867946625
    },
    {
      "factor": "latest_vs_avg_upi_share_of_spend_available_history",
      "value": 0.20452,
      "message": "This signal increased churn risk.",
      "contribution": 0.23116502165794373
    },
    {
      "factor": "latest_balance_change_30d",
      "value": -56.6283,
      "message": "Balance has been falling across recent months.",
      "contribution": 0.21351607143878937
    }
  ]
}
```

### 32. Hredhaan Shetty (`C13411`)

#### Model 1 Input

```json
{
  "customer_id": "C13411",
  "customer_name": "Hredhaan Shetty",
  "snapshot_date": "2026-06-01",
  "customer": {
    "age": 25,
    "tenure_months": 82,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 2,
    "has_credit_card": 0,
    "has_loan": 0,
    "days_since_last_transaction": 7,
    "balance_change_30d": 16.3418,
    "transaction_change_30d": 27.7175,
    "card_spend_change_30d": 23.5275,
    "app_login_change_30d": 5.4241,
    "salary_missing_days": 0.0,
    "external_transfer_change_30d": -36.3995,
    "upi_share_of_spend": 0.2843,
    "fd_maturing_in_30d": 0,
    "products_dropped_90d": 0,
    "complaints_30d": 0,
    "unresolved_complaints": 0,
    "failed_transactions_30d": 0,
    "avg_resolution_time_hrs": 0.0,
    "emi_bounce_30d": 0,
    "branch_code": "BR-111",
    "card_colour": "silver"
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
      "value": "BR-111"
    },
    {
      "factor": "age",
      "value": 25
    },
    {
      "factor": "upi_share_of_spend",
      "value": 0.2843
    },
    {
      "factor": "products_count",
      "value": 2
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
  "customer_id": "C13411",
  "customer_name": "Hredhaan Shetty",
  "prediction_date": "2026-05-01",
  "target_month": "2026-06-01",
  "profile": {
    "tenure_months": 82,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 2,
    "has_credit_card": 0,
    "has_loan": 0
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 10,
      "balance_change_30d": -13.6171,
      "transaction_change_30d": 2.7301,
      "card_spend_change_30d": 19.0165,
      "app_login_change_30d": 24.792,
      "salary_missing_days": 1.0,
      "external_transfer_change_30d": 12.2926,
      "upi_share_of_spend": 0.3637,
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
      "days_since_last_transaction": 12,
      "balance_change_30d": 15.5443,
      "transaction_change_30d": 6.9416,
      "card_spend_change_30d": 20.5361,
      "app_login_change_30d": 1.1292,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": 11.9535,
      "upi_share_of_spend": 0.2799,
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
      "days_since_last_transaction": 7,
      "balance_change_30d": 6.6707,
      "transaction_change_30d": 15.6465,
      "card_spend_change_30d": 25.0316,
      "app_login_change_30d": 10.0804,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": 33.0032,
      "upi_share_of_spend": 0.3322,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 33.9521,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-04-01",
      "days_since_last_transaction": 8,
      "balance_change_30d": 21.5299,
      "transaction_change_30d": 42.8039,
      "card_spend_change_30d": 5.9428,
      "app_login_change_30d": 10.2583,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -19.1781,
      "upi_share_of_spend": 0.2698,
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
      "days_since_last_transaction": 6,
      "balance_change_30d": 4.9728,
      "transaction_change_30d": 15.2569,
      "card_spend_change_30d": -1.8741,
      "app_login_change_30d": 2.5255,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -22.3756,
      "upi_share_of_spend": 0.3028,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 16.0288,
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
      "factor": "latest_vs_avg_external_transfer_change_30d_available_history",
      "value": -25.51472,
      "message": "This signal increased churn risk.",
      "contribution": 0.038761578500270844
    },
    {
      "factor": "avg_transaction_change_30d_6m",
      "value": 16.675800000000002,
      "message": "This signal increased churn risk.",
      "contribution": 0.020990924909710884
    },
    {
      "factor": "max_days_since_last_transaction_3m",
      "value": 8.0,
      "message": "Customer has gone longer without transacting.",
      "contribution": 0.005069625563919544
    },
    {
      "factor": "count_balance_drop_3m",
      "value": 0,
      "message": "This signal increased churn risk.",
      "contribution": 0.0049749272875487804
    },
    {
      "factor": "count_unresolved_complaint_month_6m",
      "value": 0,
      "message": "This signal increased churn risk.",
      "contribution": 0.0038039213977754116
    }
  ]
}
```

### 33. Xiti Pandey (`C13447`)

#### Model 1 Input

```json
{
  "customer_id": "C13447",
  "customer_name": "Xiti Pandey",
  "snapshot_date": "2026-06-01",
  "customer": {
    "age": 47,
    "tenure_months": 74,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 2,
    "has_credit_card": 1,
    "has_loan": 0,
    "days_since_last_transaction": 0,
    "balance_change_30d": 26.6111,
    "transaction_change_30d": 5.0526,
    "card_spend_change_30d": 8.1328,
    "app_login_change_30d": 36.3612,
    "salary_missing_days": 0.0,
    "external_transfer_change_30d": 22.8478,
    "upi_share_of_spend": 0.3207,
    "fd_maturing_in_30d": 0,
    "products_dropped_90d": 0,
    "complaints_30d": 0,
    "unresolved_complaints": 0,
    "failed_transactions_30d": 1,
    "avg_resolution_time_hrs": 0.0,
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
  "churn_probability": 0.0,
  "raw_churn_probability": 0.99,
  "risk_score": 0.0,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "app_login_change_30d",
      "value": 36.3612
    },
    {
      "factor": "card_colour",
      "value": "blue"
    },
    {
      "factor": "external_transfer_change_30d",
      "value": 22.8478
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
  "customer_id": "C13447",
  "customer_name": "Xiti Pandey",
  "prediction_date": "2026-05-01",
  "target_month": "2026-06-01",
  "profile": {
    "tenure_months": 74,
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
      "balance_change_30d": 1.841,
      "transaction_change_30d": -5.0342,
      "card_spend_change_30d": 5.4588,
      "app_login_change_30d": -9.8099,
      "salary_missing_days": 1.0,
      "external_transfer_change_30d": -5.7804,
      "upi_share_of_spend": 0.5087,
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
      "balance_change_30d": 14.5521,
      "transaction_change_30d": 3.5083,
      "card_spend_change_30d": 3.302,
      "app_login_change_30d": 23.5876,
      "salary_missing_days": 1.0,
      "external_transfer_change_30d": 4.4992,
      "upi_share_of_spend": 0.4987,
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
      "balance_change_30d": -4.0034,
      "transaction_change_30d": -10.5468,
      "card_spend_change_30d": 22.7421,
      "app_login_change_30d": 3.8083,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": 29.352,
      "upi_share_of_spend": 0.3678,
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
      "balance_change_30d": 26.0878,
      "transaction_change_30d": 3.4968,
      "card_spend_change_30d": 19.5576,
      "app_login_change_30d": -5.6593,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -17.9317,
      "upi_share_of_spend": 0.3807,
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
      "days_since_last_transaction": 0,
      "balance_change_30d": 13.8994,
      "transaction_change_30d": 23.5708,
      "card_spend_change_30d": -2.783,
      "app_login_change_30d": -12.1286,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -24.725,
      "upi_share_of_spend": 0.4458,
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
  "churn_probability": 1.95,
  "raw_churn_probability": 23.5,
  "probability_mode": "sigmoid",
  "risk_score": 5.84,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "sum_fd_maturing_in_30d_3m",
      "value": 1.0,
      "message": "Customer has a fixed deposit maturing soon.",
      "contribution": 0.09862249344587326
    },
    {
      "factor": "sum_fd_maturing_in_30d_6m",
      "value": 1.0,
      "message": "Customer has a fixed deposit maturing soon.",
      "contribution": 0.008566565811634064
    },
    {
      "factor": "latest_vs_avg_card_spend_change_30d_available_history",
      "value": -12.4385,
      "message": "Card spending has been falling across recent months.",
      "contribution": 0.005477046128362417
    },
    {
      "factor": "avg_app_login_change_30d_3m",
      "value": -4.659866666666667,
      "message": "App usage has been falling across recent months.",
      "contribution": 0.004959335550665855
    },
    {
      "factor": "latest_vs_avg_upi_share_of_spend_available_history",
      "value": 0.00546,
      "message": "This signal increased churn risk.",
      "contribution": 0.004616644233465195
    }
  ]
}
```

### 34. Tamanna Murty (`C13555`)

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

### 35. Sudiksha Merchant (`C13601`)

#### Model 1 Input

```json
{
  "customer_id": "C13601",
  "customer_name": "Sudiksha Merchant",
  "snapshot_date": "2026-06-01",
  "customer": {
    "age": 41,
    "tenure_months": 87,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 2,
    "has_credit_card": 0,
    "has_loan": 1,
    "days_since_last_transaction": 11,
    "balance_change_30d": -13.4832,
    "transaction_change_30d": -21.9776,
    "card_spend_change_30d": -19.7703,
    "app_login_change_30d": 9.6041,
    "salary_missing_days": 2.0,
    "external_transfer_change_30d": 28.1994,
    "upi_share_of_spend": 0.6726,
    "fd_maturing_in_30d": 1,
    "products_dropped_90d": 0,
    "complaints_30d": 1,
    "unresolved_complaints": 0,
    "failed_transactions_30d": 0,
    "avg_resolution_time_hrs": 26.0668,
    "emi_bounce_30d": 0,
    "branch_code": "BR-117",
    "card_colour": "green"
  },
  "actual_current_month_churn": 0
}
```

#### Model 1 Output

```json
{
  "churn_probability": 3.74,
  "raw_churn_probability": 4.78,
  "risk_score": 11.21,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "fd_maturing_in_30d",
      "value": 1
    },
    {
      "factor": "card_spend_change_30d",
      "value": -19.7703
    },
    {
      "factor": "salary_missing_days",
      "value": 2.0
    },
    {
      "factor": "external_transfer_change_30d",
      "value": 28.1994
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
  "customer_id": "C13601",
  "customer_name": "Sudiksha Merchant",
  "prediction_date": "2026-05-01",
  "target_month": "2026-06-01",
  "profile": {
    "tenure_months": 87,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 2,
    "has_credit_card": 0,
    "has_loan": 1
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 0,
      "balance_change_30d": -4.2675,
      "transaction_change_30d": 4.5765,
      "card_spend_change_30d": -6.4793,
      "app_login_change_30d": -12.5714,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": 22.866,
      "upi_share_of_spend": 0.6791,
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
      "balance_change_30d": -4.3635,
      "transaction_change_30d": 0.3411,
      "card_spend_change_30d": 8.7423,
      "app_login_change_30d": 19.1203,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -53.8724,
      "upi_share_of_spend": 0.57,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 24.7567,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-03-01",
      "days_since_last_transaction": 8,
      "balance_change_30d": 16.2587,
      "transaction_change_30d": 31.5155,
      "card_spend_change_30d": -1.0037,
      "app_login_change_30d": 29.9935,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": 1.8399,
      "upi_share_of_spend": 0.6118,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 2,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 21.7507,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-04-01",
      "days_since_last_transaction": 3,
      "balance_change_30d": 13.0828,
      "transaction_change_30d": 3.5247,
      "card_spend_change_30d": 9.0063,
      "app_login_change_30d": 27.0733,
      "salary_missing_days": 1.0,
      "external_transfer_change_30d": 36.1131,
      "upi_share_of_spend": 0.6249,
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
      "balance_change_30d": -2.9286,
      "transaction_change_30d": 1.2782,
      "card_spend_change_30d": 33.8996,
      "app_login_change_30d": -2.1953,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -19.626,
      "upi_share_of_spend": 0.5895,
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
  "churn_probability": 2.36,
  "raw_churn_probability": 27.18,
  "probability_mode": "sigmoid",
  "risk_score": 7.08,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "days_since_last_transaction_trend_6m",
      "value": 1.5000000000000002,
      "message": "Customer has gone longer without transacting.",
      "contribution": 0.10901843011379242
    },
    {
      "factor": "transaction_change_30d_trend_6m",
      "value": -0.3413000000000002,
      "message": "Transaction activity has been falling across recent months.",
      "contribution": 0.0189652182161808
    },
    {
      "factor": "card_spend_change_30d_trend_6m",
      "value": 8.10218,
      "message": "This signal increased churn risk.",
      "contribution": 0.017549417912960052
    },
    {
      "factor": "latest_upi_share_of_spend",
      "value": 0.5895,
      "message": "This signal increased churn risk.",
      "contribution": 0.016776081174612045
    },
    {
      "factor": "external_transfer_change_30d_trend_6m",
      "value": 0.5001499999999965,
      "message": "External transfers have increased.",
      "contribution": 0.013479680754244328
    }
  ]
}
```

### 36. Advika Nadkarni (`C13635`)

#### Model 1 Input

```json
{
  "customer_id": "C13635",
  "customer_name": "Advika Nadkarni",
  "snapshot_date": "2026-06-01",
  "customer": {
    "age": 52,
    "tenure_months": 144,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 2,
    "has_credit_card": 0,
    "has_loan": 0,
    "days_since_last_transaction": 6,
    "balance_change_30d": 13.9662,
    "transaction_change_30d": -6.7571,
    "card_spend_change_30d": 34.6464,
    "app_login_change_30d": 38.3122,
    "salary_missing_days": 0.0,
    "external_transfer_change_30d": 21.1262,
    "upi_share_of_spend": 0.4972,
    "fd_maturing_in_30d": 1,
    "products_dropped_90d": 1,
    "complaints_30d": 0,
    "unresolved_complaints": 0,
    "failed_transactions_30d": 1,
    "avg_resolution_time_hrs": 0.0,
    "emi_bounce_30d": 0,
    "branch_code": "BR-104",
    "card_colour": "green"
  },
  "actual_current_month_churn": 0
}
```

#### Model 1 Output

```json
{
  "churn_probability": 1.96,
  "raw_churn_probability": 1.63,
  "risk_score": 5.87,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "fd_maturing_in_30d",
      "value": 1
    },
    {
      "factor": "app_login_change_30d",
      "value": 38.3122
    },
    {
      "factor": "external_transfer_change_30d",
      "value": 21.1262
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
  "customer_id": "C13635",
  "customer_name": "Advika Nadkarni",
  "prediction_date": "2026-05-01",
  "target_month": "2026-06-01",
  "profile": {
    "tenure_months": 144,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 2,
    "has_credit_card": 0,
    "has_loan": 0
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 8,
      "balance_change_30d": 53.058,
      "transaction_change_30d": 16.0239,
      "card_spend_change_30d": 17.485,
      "app_login_change_30d": 38.7324,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -2.0662,
      "upi_share_of_spend": 0.4803,
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
      "balance_change_30d": 25.1548,
      "transaction_change_30d": 22.7445,
      "card_spend_change_30d": 35.5676,
      "app_login_change_30d": 10.3476,
      "salary_missing_days": 1.0,
      "external_transfer_change_30d": 9.3085,
      "upi_share_of_spend": 0.4741,
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
      "days_since_last_transaction": 12,
      "balance_change_30d": 6.4233,
      "transaction_change_30d": -14.1414,
      "card_spend_change_30d": -1.719,
      "app_login_change_30d": 1.9857,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": 4.9248,
      "upi_share_of_spend": 0.5298,
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
      "days_since_last_transaction": 13,
      "balance_change_30d": 6.0375,
      "transaction_change_30d": -14.9226,
      "card_spend_change_30d": 5.5694,
      "app_login_change_30d": 0.195,
      "salary_missing_days": 2.0,
      "external_transfer_change_30d": 79.6819,
      "upi_share_of_spend": 0.5242,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 2,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 14.338,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-05-01",
      "days_since_last_transaction": 11,
      "balance_change_30d": 3.1367,
      "transaction_change_30d": -19.9855,
      "card_spend_change_30d": -29.6774,
      "app_login_change_30d": -26.6185,
      "salary_missing_days": 3.0,
      "external_transfer_change_30d": 8.2099,
      "upi_share_of_spend": 0.5964,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 25.062,
      "emi_bounce_30d": 0
    }
  ],
  "actual_next_month_churn": 0
}
```

#### Model 1 v2 Output

```json
{
  "churn_probability": 16.53,
  "raw_churn_probability": 66.22,
  "probability_mode": "sigmoid",
  "risk_score": 56.1,
  "churn_prediction": "Yes",
  "risk_level": "Medium",
  "top_risk_factors": [
    {
      "factor": "latest_salary_missing_days",
      "value": 3.0,
      "message": "This signal increased churn risk.",
      "contribution": 0.2818012833595276
    },
    {
      "factor": "latest_vs_avg_upi_share_of_spend_available_history",
      "value": 0.07544,
      "message": "This signal increased churn risk.",
      "contribution": 0.18083325028419495
    },
    {
      "factor": "days_since_last_transaction_trend_6m",
      "value": 1.3999999999999986,
      "message": "Customer has gone longer without transacting.",
      "contribution": 0.17763841152191162
    },
    {
      "factor": "latest_transaction_change_30d",
      "value": -19.9855,
      "message": "Transaction activity has been falling across recent months.",
      "contribution": 0.1532660722732544
    },
    {
      "factor": "transaction_change_30d_trend_6m",
      "value": -10.96859,
      "message": "Transaction activity has been falling across recent months.",
      "contribution": 0.07789719104766846
    }
  ]
}
```

### 37. Anmol Bail (`C13643`)

#### Model 1 Input

```json
{
  "customer_id": "C13643",
  "customer_name": "Anmol Bail",
  "snapshot_date": "2026-06-01",
  "customer": {
    "age": 44,
    "tenure_months": 77,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 2,
    "has_credit_card": 1,
    "has_loan": 0,
    "days_since_last_transaction": 15,
    "balance_change_30d": -11.5854,
    "transaction_change_30d": -40.5355,
    "card_spend_change_30d": -44.1442,
    "app_login_change_30d": 6.8534,
    "salary_missing_days": 3.0,
    "external_transfer_change_30d": 23.2802,
    "upi_share_of_spend": 0.4492,
    "fd_maturing_in_30d": 0,
    "products_dropped_90d": 0,
    "complaints_30d": 0,
    "unresolved_complaints": 0,
    "failed_transactions_30d": 2,
    "avg_resolution_time_hrs": 0.0,
    "emi_bounce_30d": 0,
    "branch_code": "BR-103",
    "card_colour": "blue"
  },
  "actual_current_month_churn": 0
}
```

#### Model 1 Output

```json
{
  "churn_probability": 7.29,
  "raw_churn_probability": 6.59,
  "risk_score": 21.86,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "card_spend_change_30d",
      "value": -44.1442
    },
    {
      "factor": "days_since_last_transaction",
      "value": 15
    },
    {
      "factor": "salary_missing_days",
      "value": 3.0
    },
    {
      "factor": "failed_transactions_30d",
      "value": 2
    },
    {
      "factor": "external_transfer_change_30d",
      "value": 23.2802
    }
  ]
}
```

#### Model 1 v2 Input

```json
{
  "customer_id": "C13643",
  "customer_name": "Anmol Bail",
  "prediction_date": "2026-05-01",
  "target_month": "2026-06-01",
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
      "days_since_last_transaction": 4,
      "balance_change_30d": 14.9703,
      "transaction_change_30d": 14.7278,
      "card_spend_change_30d": 12.6773,
      "app_login_change_30d": 12.4996,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -48.7748,
      "upi_share_of_spend": 0.5003,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 25.9852,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-02-01",
      "days_since_last_transaction": 9,
      "balance_change_30d": 0.703,
      "transaction_change_30d": -17.9337,
      "card_spend_change_30d": -24.3571,
      "app_login_change_30d": 9.9367,
      "salary_missing_days": 4.0,
      "external_transfer_change_30d": 10.6587,
      "upi_share_of_spend": 0.4546,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 3,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 2,
      "avg_resolution_time_hrs": 19.845,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-03-01",
      "days_since_last_transaction": 9,
      "balance_change_30d": -2.7882,
      "transaction_change_30d": 18.1638,
      "card_spend_change_30d": 10.5349,
      "app_login_change_30d": 10.996,
      "salary_missing_days": 1.0,
      "external_transfer_change_30d": 25.8173,
      "upi_share_of_spend": 0.422,
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
      "balance_change_30d": 22.0852,
      "transaction_change_30d": -4.1339,
      "card_spend_change_30d": 3.1886,
      "app_login_change_30d": 4.5652,
      "salary_missing_days": 3.0,
      "external_transfer_change_30d": -11.59,
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
      "snapshot_date": "2026-05-01",
      "days_since_last_transaction": 10,
      "balance_change_30d": -27.0365,
      "transaction_change_30d": -9.9787,
      "card_spend_change_30d": 1.3576,
      "app_login_change_30d": 9.2486,
      "salary_missing_days": 4.0,
      "external_transfer_change_30d": 3.9139,
      "upi_share_of_spend": 0.5112,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 38.8653,
      "emi_bounce_30d": 0
    }
  ],
  "actual_next_month_churn": 0
}
```

#### Model 1 v2 Output

```json
{
  "churn_probability": 9.7,
  "raw_churn_probability": 54.86,
  "probability_mode": "sigmoid",
  "risk_score": 29.1,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "latest_salary_missing_days",
      "value": 4.0,
      "message": "This signal increased churn risk.",
      "contribution": 0.311309814453125
    },
    {
      "factor": "latest_avg_resolution_time_hrs",
      "value": 38.8653,
      "message": "This signal increased churn risk.",
      "contribution": 0.22168771922588348
    },
    {
      "factor": "latest_vs_avg_upi_share_of_spend_available_history",
      "value": 0.0579399999999999,
      "message": "This signal increased churn risk.",
      "contribution": 0.179183229804039
    },
    {
      "factor": "latest_balance_change_30d",
      "value": -27.0365,
      "message": "Balance has been falling across recent months.",
      "contribution": 0.13743551075458527
    },
    {
      "factor": "external_transfer_change_30d_trend_6m",
      "value": 8.31287,
      "message": "External transfers have increased.",
      "contribution": 0.02439855970442295
    }
  ]
}
```

### 38. Jatin Purohit (`C13656`)

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

### 39. Viraj Bhargava (`C13678`)

#### Model 1 Input

```json
{
  "customer_id": "C13678",
  "customer_name": "Viraj Bhargava",
  "snapshot_date": "2026-06-01",
  "customer": {
    "age": 34,
    "tenure_months": 172,
    "customer_segment": "farmer",
    "income_regularity": "seasonal",
    "products_count": 1,
    "has_credit_card": 0,
    "has_loan": 0,
    "days_since_last_transaction": 8,
    "balance_change_30d": 2.3249,
    "transaction_change_30d": 14.1289,
    "card_spend_change_30d": -17.8053,
    "app_login_change_30d": 14.359,
    "salary_missing_days": null,
    "external_transfer_change_30d": -24.1479,
    "upi_share_of_spend": 0.4696,
    "fd_maturing_in_30d": 0,
    "products_dropped_90d": 0,
    "complaints_30d": 0,
    "unresolved_complaints": 0,
    "failed_transactions_30d": 0,
    "avg_resolution_time_hrs": 0.0,
    "emi_bounce_30d": 0,
    "branch_code": "BR-102",
    "card_colour": "black"
  },
  "actual_current_month_churn": 0
}
```

#### Model 1 Output

```json
{
  "churn_probability": 1.96,
  "raw_churn_probability": 2.06,
  "risk_score": 5.87,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "branch_code",
      "value": "BR-102"
    },
    {
      "factor": "card_spend_change_30d",
      "value": -17.8053
    },
    {
      "factor": "app_login_change_30d",
      "value": 14.359
    },
    {
      "factor": "products_count",
      "value": 1
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
  "customer_id": "C13678",
  "customer_name": "Viraj Bhargava",
  "prediction_date": "2026-05-01",
  "target_month": "2026-06-01",
  "profile": {
    "tenure_months": 172,
    "customer_segment": "farmer",
    "income_regularity": "seasonal",
    "products_count": 1,
    "has_credit_card": 0,
    "has_loan": 0
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 9,
      "balance_change_30d": -2.6227,
      "transaction_change_30d": -4.2546,
      "card_spend_change_30d": -7.9519,
      "app_login_change_30d": -10.0776,
      "salary_missing_days": null,
      "external_transfer_change_30d": 17.2258,
      "upi_share_of_spend": 0.4617,
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
      "balance_change_30d": 1.2052,
      "transaction_change_30d": -11.688,
      "card_spend_change_30d": 9.3088,
      "app_login_change_30d": 5.617,
      "salary_missing_days": null,
      "external_transfer_change_30d": 5.0553,
      "upi_share_of_spend": 0.3706,
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
      "balance_change_30d": 16.3103,
      "transaction_change_30d": -12.6351,
      "card_spend_change_30d": -5.212,
      "app_login_change_30d": 16.2736,
      "salary_missing_days": null,
      "external_transfer_change_30d": -10.1443,
      "upi_share_of_spend": 0.3548,
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
      "balance_change_30d": -17.8457,
      "transaction_change_30d": -10.5626,
      "card_spend_change_30d": 9.9052,
      "app_login_change_30d": 14.1562,
      "salary_missing_days": null,
      "external_transfer_change_30d": -10.0609,
      "upi_share_of_spend": 0.5045,
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
      "balance_change_30d": 2.1932,
      "transaction_change_30d": 4.7811,
      "card_spend_change_30d": 16.4429,
      "app_login_change_30d": 31.1307,
      "salary_missing_days": null,
      "external_transfer_change_30d": -3.9943,
      "upi_share_of_spend": 0.3934,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 2,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 3.9418,
      "emi_bounce_30d": 0
    }
  ],
  "actual_next_month_churn": 0
}
```

#### Model 1 v2 Output

```json
{
  "churn_probability": 2.05,
  "raw_churn_probability": 24.49,
  "probability_mode": "sigmoid",
  "risk_score": 6.15,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "count_quiet_customer_3m",
      "value": 2,
      "message": "This signal increased churn risk.",
      "contribution": 0.019037790596485138
    },
    {
      "factor": "card_spend_change_30d_trend_6m",
      "value": 4.938600000000002,
      "message": "This signal increased churn risk.",
      "contribution": 0.015604554675519466
    },
    {
      "factor": "count_unresolved_complaint_month_6m",
      "value": 0,
      "message": "This signal increased churn risk.",
      "contribution": 0.0038039213977754116
    },
    {
      "factor": "count_external_transfer_rise_6m",
      "value": 0,
      "message": "This signal increased churn risk.",
      "contribution": 0.002879970008507371
    },
    {
      "factor": "sum_unresolved_complaints_6m",
      "value": 0.0,
      "message": "This signal increased churn risk.",
      "contribution": 0.0028714186046272516
    }
  ]
}
```

### 40. Abha Yogi (`C13919`)

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

### 41. Anvi Banik (`C13933`)

#### Model 1 Input

```json
{
  "customer_id": "C13933",
  "customer_name": "Anvi Banik",
  "snapshot_date": "2026-06-01",
  "customer": {
    "age": 59,
    "tenure_months": 173,
    "customer_segment": "pension",
    "income_regularity": "regular",
    "products_count": 1,
    "has_credit_card": 0,
    "has_loan": 0,
    "days_since_last_transaction": 4,
    "balance_change_30d": 18.0337,
    "transaction_change_30d": 7.1382,
    "card_spend_change_30d": -2.3846,
    "app_login_change_30d": -2.6799,
    "salary_missing_days": 0.0,
    "external_transfer_change_30d": -4.7785,
    "upi_share_of_spend": 0.6396,
    "fd_maturing_in_30d": 0,
    "products_dropped_90d": 0,
    "complaints_30d": 2,
    "unresolved_complaints": 0,
    "failed_transactions_30d": 1,
    "avg_resolution_time_hrs": 39.7324,
    "emi_bounce_30d": 0,
    "branch_code": "BR-136",
    "card_colour": "silver"
  },
  "actual_current_month_churn": 0
}
```

#### Model 1 Output

```json
{
  "churn_probability": 1.96,
  "raw_churn_probability": 1.56,
  "risk_score": 5.87,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "complaints_30d",
      "value": 2
    },
    {
      "factor": "customer_segment",
      "value": "pension"
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
  "customer_id": "C13933",
  "customer_name": "Anvi Banik",
  "prediction_date": "2026-05-01",
  "target_month": "2026-06-01",
  "profile": {
    "tenure_months": 173,
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
      "balance_change_30d": 24.0337,
      "transaction_change_30d": -5.8259,
      "card_spend_change_30d": -3.0072,
      "app_login_change_30d": 27.4658,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": 0.47,
      "upi_share_of_spend": 0.5976,
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
      "balance_change_30d": 23.3979,
      "transaction_change_30d": 24.0572,
      "card_spend_change_30d": 34.9977,
      "app_login_change_30d": 18.3365,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -8.6546,
      "upi_share_of_spend": 0.5723,
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
      "balance_change_30d": 0.5344,
      "transaction_change_30d": 2.3914,
      "card_spend_change_30d": 1.5587,
      "app_login_change_30d": -0.1135,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -3.7997,
      "upi_share_of_spend": 0.6272,
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
      "balance_change_30d": 4.4693,
      "transaction_change_30d": 0.2776,
      "card_spend_change_30d": 3.7253,
      "app_login_change_30d": -19.1222,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": 14.6792,
      "upi_share_of_spend": 0.6696,
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
      "balance_change_30d": 31.3441,
      "transaction_change_30d": -6.5639,
      "card_spend_change_30d": 15.5611,
      "app_login_change_30d": 6.0359,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": 4.6725,
      "upi_share_of_spend": 0.7506,
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
  "churn_probability": 3.35,
  "raw_churn_probability": 33.88,
  "probability_mode": "sigmoid",
  "risk_score": 10.06,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "latest_vs_avg_upi_share_of_spend_available_history",
      "value": 0.10714,
      "message": "This signal increased churn risk.",
      "contribution": 0.15304839611053467
    },
    {
      "factor": "days_since_last_transaction_trend_6m",
      "value": 1.2999999999999994,
      "message": "Customer has gone longer without transacting.",
      "contribution": 0.11410029977560043
    },
    {
      "factor": "latest_upi_share_of_spend",
      "value": 0.7506,
      "message": "This signal increased churn risk.",
      "contribution": 0.06450791656970978
    },
    {
      "factor": "external_transfer_change_30d_trend_6m",
      "value": 3.17388,
      "message": "External transfers have increased.",
      "contribution": 0.03303554654121399
    },
    {
      "factor": "latest_vs_avg_card_spend_change_30d_available_history",
      "value": 4.9939800000000005,
      "message": "This signal increased churn risk.",
      "contribution": 0.016101155430078506
    }
  ]
}
```

### 42. Falak Lad (`C14018`)

#### Model 1 Input

```json
{
  "customer_id": "C14018",
  "customer_name": "Falak Lad",
  "snapshot_date": "2026-06-01",
  "customer": {
    "age": 25,
    "tenure_months": 61,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 3,
    "has_credit_card": 1,
    "has_loan": 1,
    "days_since_last_transaction": 4,
    "balance_change_30d": -5.3613,
    "transaction_change_30d": -5.9583,
    "card_spend_change_30d": -1.584,
    "app_login_change_30d": -16.0642,
    "salary_missing_days": 2.0,
    "external_transfer_change_30d": -0.8654,
    "upi_share_of_spend": 0.1119,
    "fd_maturing_in_30d": 0,
    "products_dropped_90d": 1,
    "complaints_30d": 0,
    "unresolved_complaints": 0,
    "failed_transactions_30d": 0,
    "avg_resolution_time_hrs": 0.0,
    "emi_bounce_30d": 0,
    "branch_code": "BR-140",
    "card_colour": "blue"
  },
  "actual_current_month_churn": 0
}
```

#### Model 1 Output

```json
{
  "churn_probability": 1.96,
  "raw_churn_probability": 2.13,
  "risk_score": 5.87,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "branch_code",
      "value": "BR-140"
    },
    {
      "factor": "salary_missing_days",
      "value": 2.0
    },
    {
      "factor": "age",
      "value": 25
    },
    {
      "factor": "tenure_months",
      "value": 61
    },
    {
      "factor": "upi_share_of_spend",
      "value": 0.1119
    }
  ]
}
```

#### Model 1 v2 Input

```json
{
  "customer_id": "C14018",
  "customer_name": "Falak Lad",
  "prediction_date": "2026-05-01",
  "target_month": "2026-06-01",
  "profile": {
    "tenure_months": 61,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 3,
    "has_credit_card": 1,
    "has_loan": 1
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 2,
      "balance_change_30d": 21.1504,
      "transaction_change_30d": 42.7642,
      "card_spend_change_30d": 14.835,
      "app_login_change_30d": 16.8814,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -22.1099,
      "upi_share_of_spend": 0.0605,
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
      "balance_change_30d": 3.3952,
      "transaction_change_30d": 17.0421,
      "card_spend_change_30d": 12.4495,
      "app_login_change_30d": -1.6192,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": 12.7816,
      "upi_share_of_spend": 0.0604,
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
      "balance_change_30d": 11.9346,
      "transaction_change_30d": 12.7481,
      "card_spend_change_30d": -14.7713,
      "app_login_change_30d": 11.6852,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": 24.492,
      "upi_share_of_spend": 0.0747,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 2,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 2.2471,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-04-01",
      "days_since_last_transaction": 11,
      "balance_change_30d": -12.6722,
      "transaction_change_30d": -4.8655,
      "card_spend_change_30d": -28.1487,
      "app_login_change_30d": -13.6292,
      "salary_missing_days": 1.0,
      "external_transfer_change_30d": 22.7343,
      "upi_share_of_spend": 0.2853,
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
      "balance_change_30d": -12.5087,
      "transaction_change_30d": -25.5044,
      "card_spend_change_30d": -32.7405,
      "app_login_change_30d": -46.1612,
      "salary_missing_days": 2.0,
      "external_transfer_change_30d": 26.7948,
      "upi_share_of_spend": 0.2065,
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
  "churn_probability": 22.24,
  "raw_churn_probability": 73.06,
  "probability_mode": "sigmoid",
  "risk_score": 70.84,
  "churn_prediction": "Yes",
  "risk_level": "Medium",
  "top_risk_factors": [
    {
      "factor": "latest_transaction_change_30d",
      "value": -25.5044,
      "message": "Transaction activity has been falling across recent months.",
      "contribution": 0.26768529415130615
    },
    {
      "factor": "latest_vs_avg_upi_share_of_spend_available_history",
      "value": 0.06902,
      "message": "This signal increased churn risk.",
      "contribution": 0.16711118817329407
    },
    {
      "factor": "days_since_last_transaction_trend_6m",
      "value": 2.9000000000000004,
      "message": "Customer has gone longer without transacting.",
      "contribution": 0.16681431233882904
    },
    {
      "factor": "transaction_change_30d_trend_6m",
      "value": -15.844480000000004,
      "message": "Transaction activity has been falling across recent months.",
      "contribution": 0.1266697198152542
    },
    {
      "factor": "balance_change_30d_trend_6m",
      "value": -8.338560000000001,
      "message": "Balance has been falling across recent months.",
      "contribution": 0.07952609658241272
    }
  ]
}
```

### 43. Ishanvi Bose (`C14204`)

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

### 44. Urvi Devi (`C14228`)

#### Model 1 Input

```json
{
  "customer_id": "C14228",
  "customer_name": "Urvi Devi",
  "snapshot_date": "2026-06-01",
  "customer": {
    "age": 27,
    "tenure_months": 108,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 3,
    "has_credit_card": 1,
    "has_loan": 1,
    "days_since_last_transaction": 4,
    "balance_change_30d": -22.6114,
    "transaction_change_30d": -12.6579,
    "card_spend_change_30d": -8.6338,
    "app_login_change_30d": 5.1381,
    "salary_missing_days": 0.0,
    "external_transfer_change_30d": 2.6042,
    "upi_share_of_spend": 0.4377,
    "fd_maturing_in_30d": 0,
    "products_dropped_90d": 1,
    "complaints_30d": 0,
    "unresolved_complaints": 0,
    "failed_transactions_30d": 0,
    "avg_resolution_time_hrs": 0.0,
    "emi_bounce_30d": 0,
    "branch_code": "BR-125",
    "card_colour": "silver"
  },
  "actual_current_month_churn": 0
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
      "factor": "balance_change_30d",
      "value": -22.6114
    },
    {
      "factor": "age",
      "value": 27
    },
    {
      "factor": "branch_code",
      "value": "BR-125"
    },
    {
      "factor": "external_transfer_change_30d",
      "value": 2.6042
    },
    {
      "factor": "upi_share_of_spend",
      "value": 0.4377
    }
  ]
}
```

#### Model 1 v2 Input

```json
{
  "customer_id": "C14228",
  "customer_name": "Urvi Devi",
  "prediction_date": "2026-05-01",
  "target_month": "2026-06-01",
  "profile": {
    "tenure_months": 108,
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
      "balance_change_30d": 7.3145,
      "transaction_change_30d": 11.1215,
      "card_spend_change_30d": -11.6315,
      "app_login_change_30d": -15.0629,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": 0.8814,
      "upi_share_of_spend": 0.3271,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 1,
      "complaints_30d": 1,
      "unresolved_complaints": 1,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 29.7788,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-02-01",
      "days_since_last_transaction": 0,
      "balance_change_30d": -17.7003,
      "transaction_change_30d": -10.0061,
      "card_spend_change_30d": 39.5948,
      "app_login_change_30d": 15.7072,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": 14.4983,
      "upi_share_of_spend": 0.3637,
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
      "balance_change_30d": 3.4394,
      "transaction_change_30d": -4.8619,
      "card_spend_change_30d": -16.2057,
      "app_login_change_30d": 5.785,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -7.9245,
      "upi_share_of_spend": 0.3648,
      "fd_maturing_in_30d": 1,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 1.0,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-04-01",
      "days_since_last_transaction": 3,
      "balance_change_30d": 6.7832,
      "transaction_change_30d": -27.9383,
      "card_spend_change_30d": -7.0171,
      "app_login_change_30d": -5.3076,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": 11.7715,
      "upi_share_of_spend": 0.3709,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 26.2081,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-05-01",
      "days_since_last_transaction": 0,
      "balance_change_30d": 6.951,
      "transaction_change_30d": 7.6078,
      "card_spend_change_30d": 9.4511,
      "app_login_change_30d": 14.7933,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": 47.3466,
      "upi_share_of_spend": 0.3294,
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
  "churn_probability": 2.4,
  "raw_churn_probability": 27.45,
  "probability_mode": "sigmoid",
  "risk_score": 7.19,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "sum_fd_maturing_in_30d_3m",
      "value": 1.0,
      "message": "Customer has a fixed deposit maturing soon.",
      "contribution": 0.060460980981588364
    },
    {
      "factor": "external_transfer_change_30d_trend_6m",
      "value": 9.02036,
      "message": "External transfers have increased.",
      "contribution": 0.035649243742227554
    },
    {
      "factor": "transaction_change_30d_trend_6m",
      "value": -2.495960000000001,
      "message": "Transaction activity has been falling across recent months.",
      "contribution": 0.02785881794989109
    },
    {
      "factor": "latest_vs_avg_card_spend_change_30d_available_history",
      "value": 6.612780000000001,
      "message": "This signal increased churn risk.",
      "contribution": 0.014874734915792942
    },
    {
      "factor": "max_salary_missing_days_6m",
      "value": 0.0,
      "message": "This signal increased churn risk.",
      "contribution": 0.009915442205965519
    }
  ]
}
```

### 45. Sara Dada (`C14252`)

#### Model 1 Input

```json
{
  "customer_id": "C14252",
  "customer_name": "Sara Dada",
  "snapshot_date": "2026-04-01",
  "customer": {
    "age": 60,
    "tenure_months": 134,
    "customer_segment": "pension",
    "income_regularity": "regular",
    "products_count": 2,
    "has_credit_card": 0,
    "has_loan": 0,
    "days_since_last_transaction": 11,
    "balance_change_30d": -44.3259,
    "transaction_change_30d": -37.157,
    "card_spend_change_30d": -63.3992,
    "app_login_change_30d": -23.65,
    "salary_missing_days": 5.0,
    "external_transfer_change_30d": 49.1605,
    "upi_share_of_spend": 0.391,
    "fd_maturing_in_30d": 1,
    "products_dropped_90d": 0,
    "complaints_30d": 2,
    "unresolved_complaints": 1,
    "failed_transactions_30d": 1,
    "avg_resolution_time_hrs": 39.4239,
    "emi_bounce_30d": 0,
    "branch_code": "BR-115",
    "card_colour": "gold"
  },
  "actual_current_month_churn": 1
}
```

#### Model 1 Output

```json
{
  "churn_probability": 48.15,
  "raw_churn_probability": 53.88,
  "risk_score": 80.56,
  "churn_prediction": "Yes",
  "risk_level": "High",
  "top_risk_factors": [
    {
      "factor": "balance_change_30d",
      "value": -44.3259
    },
    {
      "factor": "card_spend_change_30d",
      "value": -63.3992
    },
    {
      "factor": "salary_missing_days",
      "value": 5.0
    },
    {
      "factor": "fd_maturing_in_30d",
      "value": 1
    },
    {
      "factor": "complaints_30d",
      "value": 2
    }
  ]
}
```

#### Model 1 v2 Input

```json
{
  "customer_id": "C14252",
  "customer_name": "Sara Dada",
  "prediction_date": "2026-03-01",
  "target_month": "2026-04-01",
  "profile": {
    "tenure_months": 134,
    "customer_segment": "pension",
    "income_regularity": "regular",
    "products_count": 2,
    "has_credit_card": 0,
    "has_loan": 0
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 3,
      "balance_change_30d": 5.6593,
      "transaction_change_30d": 17.5487,
      "card_spend_change_30d": 28.6844,
      "app_login_change_30d": -29.5341,
      "salary_missing_days": 1.0,
      "external_transfer_change_30d": 65.9046,
      "upi_share_of_spend": 0.2134,
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
      "days_since_last_transaction": 3,
      "balance_change_30d": -8.2684,
      "transaction_change_30d": 7.7788,
      "card_spend_change_30d": 16.6942,
      "app_login_change_30d": 15.1851,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": 5.7527,
      "upi_share_of_spend": 0.2295,
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
      "days_since_last_transaction": 10,
      "balance_change_30d": -37.2213,
      "transaction_change_30d": -24.327,
      "card_spend_change_30d": -12.9997,
      "app_login_change_30d": -12.2409,
      "salary_missing_days": 4.0,
      "external_transfer_change_30d": 26.114,
      "upi_share_of_spend": 0.3508,
      "fd_maturing_in_30d": 1,
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
  "churn_probability": 22.42,
  "raw_churn_probability": 73.25,
  "probability_mode": "sigmoid",
  "risk_score": 70.91,
  "churn_prediction": "Yes",
  "risk_level": "Medium",
  "top_risk_factors": [
    {
      "factor": "latest_salary_missing_days",
      "value": 4.0,
      "message": "This signal increased churn risk.",
      "contribution": 0.34189462661743164
    },
    {
      "factor": "latest_balance_change_30d",
      "value": -37.2213,
      "message": "Balance has been falling across recent months.",
      "contribution": 0.2909736931324005
    },
    {
      "factor": "days_since_last_transaction_trend_6m",
      "value": 3.4999999999999987,
      "message": "Customer has gone longer without transacting.",
      "contribution": 0.20924387872219086
    },
    {
      "factor": "latest_transaction_change_30d",
      "value": -24.327,
      "message": "Transaction activity has been falling across recent months.",
      "contribution": 0.17981547117233276
    },
    {
      "factor": "latest_vs_avg_upi_share_of_spend_available_history",
      "value": 0.0862333333333333,
      "message": "This signal increased churn risk.",
      "contribution": 0.1706794649362564
    }
  ]
}
```

### 46. Ethan Bahri (`C14321`)

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

### 47. Tanay Ramaswamy (`C14341`)

#### Model 1 Input

```json
{
  "customer_id": "C14341",
  "customer_name": "Tanay Ramaswamy",
  "snapshot_date": "2026-06-01",
  "customer": {
    "age": 29,
    "tenure_months": 24,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 3,
    "has_credit_card": 1,
    "has_loan": 1,
    "days_since_last_transaction": 8,
    "balance_change_30d": 31.1086,
    "transaction_change_30d": 26.1588,
    "card_spend_change_30d": 2.5195,
    "app_login_change_30d": -1.451,
    "salary_missing_days": 0.0,
    "external_transfer_change_30d": -15.6649,
    "upi_share_of_spend": 0.4695,
    "fd_maturing_in_30d": 0,
    "products_dropped_90d": 0,
    "complaints_30d": 0,
    "unresolved_complaints": 0,
    "failed_transactions_30d": 1,
    "avg_resolution_time_hrs": 0.0,
    "emi_bounce_30d": 0,
    "branch_code": "BR-103",
    "card_colour": "blue"
  },
  "actual_current_month_churn": 0
}
```

#### Model 1 Output

```json
{
  "churn_probability": 1.96,
  "raw_churn_probability": 1.89,
  "risk_score": 5.87,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "tenure_months",
      "value": 24
    },
    {
      "factor": "card_colour",
      "value": "blue"
    },
    {
      "factor": "has_credit_card",
      "value": 1
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
  "customer_id": "C14341",
  "customer_name": "Tanay Ramaswamy",
  "prediction_date": "2026-05-01",
  "target_month": "2026-06-01",
  "profile": {
    "tenure_months": 24,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 3,
    "has_credit_card": 1,
    "has_loan": 1
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 14,
      "balance_change_30d": 33.7171,
      "transaction_change_30d": -8.8341,
      "card_spend_change_30d": 50.7427,
      "app_login_change_30d": 41.7937,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -6.4669,
      "upi_share_of_spend": 0.4354,
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
      "days_since_last_transaction": 12,
      "balance_change_30d": -5.0425,
      "transaction_change_30d": 2.0005,
      "card_spend_change_30d": -1.7858,
      "app_login_change_30d": -21.4805,
      "salary_missing_days": 2.0,
      "external_transfer_change_30d": 24.4215,
      "upi_share_of_spend": 0.5884,
      "fd_maturing_in_30d": 1,
      "products_dropped_90d": 0,
      "complaints_30d": 2,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 24.2842,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-03-01",
      "days_since_last_transaction": 11,
      "balance_change_30d": 12.7737,
      "transaction_change_30d": -4.0089,
      "card_spend_change_30d": 10.0572,
      "app_login_change_30d": 13.4523,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -16.4944,
      "upi_share_of_spend": 0.5658,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 28.506,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-04-01",
      "days_since_last_transaction": 16,
      "balance_change_30d": -7.2023,
      "transaction_change_30d": 1.8452,
      "card_spend_change_30d": -11.6897,
      "app_login_change_30d": -3.4082,
      "salary_missing_days": 2.0,
      "external_transfer_change_30d": 76.9683,
      "upi_share_of_spend": 0.5923,
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
      "balance_change_30d": -6.3788,
      "transaction_change_30d": 7.8076,
      "card_spend_change_30d": -14.7534,
      "app_login_change_30d": 10.4431,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": 16.5436,
      "upi_share_of_spend": 0.5744,
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
  "churn_probability": 7.46,
  "raw_churn_probability": 49.54,
  "probability_mode": "sigmoid",
  "risk_score": 22.38,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "latest_days_since_last_transaction",
      "value": 13,
      "message": "Customer has gone longer without transacting.",
      "contribution": 0.36730849742889404
    },
    {
      "factor": "external_transfer_change_30d_trend_6m",
      "value": 9.856780000000004,
      "message": "External transfers have increased.",
      "contribution": 0.040780775249004364
    },
    {
      "factor": "sum_failed_transactions_30d_3m",
      "value": 4.0,
      "message": "Customer has recent failed transactions.",
      "contribution": 0.03495946153998375
    },
    {
      "factor": "balance_change_30d_trend_6m",
      "value": -8.235160000000004,
      "message": "Balance has been falling across recent months.",
      "contribution": 0.031543467193841934
    },
    {
      "factor": "count_quiet_customer_3m",
      "value": 3,
      "message": "This signal increased churn risk.",
      "contribution": 0.02254015952348709
    }
  ]
}
```

### 48. Gautami Peri (`C14388`)

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

### 49. Viraj Kade (`C14404`)

#### Model 1 Input

```json
{
  "customer_id": "C14404",
  "customer_name": "Viraj Kade",
  "snapshot_date": "2026-06-01",
  "customer": {
    "age": 36,
    "tenure_months": 121,
    "customer_segment": "business",
    "income_regularity": "irregular",
    "products_count": 2,
    "has_credit_card": 0,
    "has_loan": 1,
    "days_since_last_transaction": 8,
    "balance_change_30d": 6.9438,
    "transaction_change_30d": -6.8733,
    "card_spend_change_30d": 45.3892,
    "app_login_change_30d": 20.1642,
    "salary_missing_days": null,
    "external_transfer_change_30d": -3.5571,
    "upi_share_of_spend": 0.5337,
    "fd_maturing_in_30d": 0,
    "products_dropped_90d": 0,
    "complaints_30d": 0,
    "unresolved_complaints": 0,
    "failed_transactions_30d": 1,
    "avg_resolution_time_hrs": 0.0,
    "emi_bounce_30d": 0,
    "branch_code": "BR-107",
    "card_colour": "gold"
  },
  "actual_current_month_churn": 0
}
```

#### Model 1 Output

```json
{
  "churn_probability": 1.96,
  "raw_churn_probability": 1.63,
  "risk_score": 5.87,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "branch_code",
      "value": "BR-107"
    },
    {
      "factor": "app_login_change_30d",
      "value": 20.1642
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
  "customer_id": "C14404",
  "customer_name": "Viraj Kade",
  "prediction_date": "2026-05-01",
  "target_month": "2026-06-01",
  "profile": {
    "tenure_months": 121,
    "customer_segment": "business",
    "income_regularity": "irregular",
    "products_count": 2,
    "has_credit_card": 0,
    "has_loan": 1
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 13,
      "balance_change_30d": -4.0661,
      "transaction_change_30d": -1.0983,
      "card_spend_change_30d": -7.8271,
      "app_login_change_30d": 18.2179,
      "salary_missing_days": null,
      "external_transfer_change_30d": 38.8425,
      "upi_share_of_spend": 0.409,
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
      "balance_change_30d": -13.2196,
      "transaction_change_30d": 11.3643,
      "card_spend_change_30d": 5.8512,
      "app_login_change_30d": 4.7298,
      "salary_missing_days": null,
      "external_transfer_change_30d": 13.7281,
      "upi_share_of_spend": 0.4626,
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
      "balance_change_30d": -16.435,
      "transaction_change_30d": -0.5467,
      "card_spend_change_30d": -27.8545,
      "app_login_change_30d": -12.6733,
      "salary_missing_days": null,
      "external_transfer_change_30d": -28.1597,
      "upi_share_of_spend": 0.4162,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 1,
      "complaints_30d": 0,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 2,
      "avg_resolution_time_hrs": 0.0,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-04-01",
      "days_since_last_transaction": 8,
      "balance_change_30d": 3.8341,
      "transaction_change_30d": 13.6289,
      "card_spend_change_30d": 12.6665,
      "app_login_change_30d": 4.6727,
      "salary_missing_days": null,
      "external_transfer_change_30d": -4.4956,
      "upi_share_of_spend": 0.49,
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
      "balance_change_30d": -14.5853,
      "transaction_change_30d": 10.5457,
      "card_spend_change_30d": -9.9306,
      "app_login_change_30d": 33.8563,
      "salary_missing_days": null,
      "external_transfer_change_30d": 16.2472,
      "upi_share_of_spend": 0.4976,
      "fd_maturing_in_30d": 1,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 2,
      "avg_resolution_time_hrs": 29.9749,
      "emi_bounce_30d": 0
    }
  ],
  "actual_next_month_churn": 0
}
```

#### Model 1 v2 Output

```json
{
  "churn_probability": 4.3,
  "raw_churn_probability": 38.68,
  "probability_mode": "sigmoid",
  "risk_score": 12.9,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "latest_fd_maturing_in_30d",
      "value": 1,
      "message": "Customer has a fixed deposit maturing soon.",
      "contribution": 0.2022916078567505
    },
    {
      "factor": "latest_avg_resolution_time_hrs",
      "value": 29.9749,
      "message": "This signal increased churn risk.",
      "contribution": 0.1456885039806366
    },
    {
      "factor": "sum_fd_maturing_in_30d_3m",
      "value": 1.0,
      "message": "Customer has a fixed deposit maturing soon.",
      "contribution": 0.13898247480392456
    },
    {
      "factor": "latest_vs_avg_upi_share_of_spend_available_history",
      "value": 0.04252,
      "message": "This signal increased churn risk.",
      "contribution": 0.0829584077000618
    },
    {
      "factor": "sum_failed_transactions_30d_3m",
      "value": 5.0,
      "message": "Customer has recent failed transactions.",
      "contribution": 0.02586277388036251
    }
  ]
}
```

### 50. Jatin Borra (`C14412`)

#### Model 1 Input

```json
{
  "customer_id": "C14412",
  "customer_name": "Jatin Borra",
  "snapshot_date": "2026-04-01",
  "customer": {
    "age": 77,
    "tenure_months": 10,
    "customer_segment": "pension",
    "income_regularity": "regular",
    "products_count": 1,
    "has_credit_card": 0,
    "has_loan": 0,
    "days_since_last_transaction": 10,
    "balance_change_30d": -13.3155,
    "transaction_change_30d": -4.9216,
    "card_spend_change_30d": 4.7567,
    "app_login_change_30d": 8.2226,
    "salary_missing_days": 0.0,
    "external_transfer_change_30d": 20.9466,
    "upi_share_of_spend": 0.7667,
    "fd_maturing_in_30d": 1,
    "products_dropped_90d": 0,
    "complaints_30d": 0,
    "unresolved_complaints": 0,
    "failed_transactions_30d": 1,
    "avg_resolution_time_hrs": 0.0,
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
  "churn_probability": 3.74,
  "raw_churn_probability": 4.11,
  "risk_score": 11.21,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "tenure_months",
      "value": 10
    },
    {
      "factor": "fd_maturing_in_30d",
      "value": 1
    },
    {
      "factor": "branch_code",
      "value": "BR-112"
    },
    {
      "factor": "age",
      "value": 77
    },
    {
      "factor": "external_transfer_change_30d",
      "value": 20.9466
    }
  ]
}
```

#### Model 1 v2 Input

```json
{
  "customer_id": "C14412",
  "customer_name": "Jatin Borra",
  "prediction_date": "2026-03-01",
  "target_month": "2026-04-01",
  "profile": {
    "tenure_months": 10,
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
      "balance_change_30d": -2.1054,
      "transaction_change_30d": 31.233,
      "card_spend_change_30d": 3.257,
      "app_login_change_30d": -2.4599,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": 0.5727,
      "upi_share_of_spend": 0.7796,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 2,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 17.683,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-02-01",
      "days_since_last_transaction": 6,
      "balance_change_30d": 7.1079,
      "transaction_change_30d": -7.5666,
      "card_spend_change_30d": -16.2297,
      "app_login_change_30d": -13.0338,
      "salary_missing_days": 2.0,
      "external_transfer_change_30d": 4.0352,
      "upi_share_of_spend": 0.7984,
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
      "days_since_last_transaction": 14,
      "balance_change_30d": -6.6164,
      "transaction_change_30d": -2.1477,
      "card_spend_change_30d": 25.3395,
      "app_login_change_30d": -2.9247,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -18.2985,
      "upi_share_of_spend": 0.809,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 43.9839,
      "emi_bounce_30d": 0
    }
  ],
  "actual_next_month_churn": 1
}
```

#### Model 1 v2 Output

```json
{
  "churn_probability": 13.66,
  "raw_churn_probability": 62.06,
  "probability_mode": "sigmoid",
  "risk_score": 44.64,
  "churn_prediction": "Yes",
  "risk_level": "Medium",
  "top_risk_factors": [
    {
      "factor": "latest_days_since_last_transaction",
      "value": 14,
      "message": "Customer has gone longer without transacting.",
      "contribution": 0.4797784686088562
    },
    {
      "factor": "latest_avg_resolution_time_hrs",
      "value": 43.9839,
      "message": "This signal increased churn risk.",
      "contribution": 0.22776764631271362
    },
    {
      "factor": "transaction_change_30d_trend_6m",
      "value": -16.690350000000002,
      "message": "Transaction activity has been falling across recent months.",
      "contribution": 0.10500390082597733
    },
    {
      "factor": "days_since_last_transaction_trend_6m",
      "value": 2.9999999999999982,
      "message": "Customer has gone longer without transacting.",
      "contribution": 0.08450861275196075
    },
    {
      "factor": "latest_upi_share_of_spend",
      "value": 0.809,
      "message": "This signal increased churn risk.",
      "contribution": 0.052117519080638885
    }
  ]
}
```

### 51. Kevin Taneja (`C14491`)

#### Model 1 Input

```json
{
  "customer_id": "C14491",
  "customer_name": "Kevin Taneja",
  "snapshot_date": "2026-06-01",
  "customer": {
    "age": 29,
    "tenure_months": 35,
    "customer_segment": "vendor",
    "income_regularity": "irregular",
    "products_count": 2,
    "has_credit_card": 0,
    "has_loan": 1,
    "days_since_last_transaction": 6,
    "balance_change_30d": 39.651,
    "transaction_change_30d": 4.8862,
    "card_spend_change_30d": -8.3275,
    "app_login_change_30d": 39.1623,
    "salary_missing_days": null,
    "external_transfer_change_30d": -39.7436,
    "upi_share_of_spend": 0.5139,
    "fd_maturing_in_30d": 0,
    "products_dropped_90d": 0,
    "complaints_30d": 0,
    "unresolved_complaints": 0,
    "failed_transactions_30d": 0,
    "avg_resolution_time_hrs": 0.0,
    "emi_bounce_30d": 0,
    "branch_code": "BR-120",
    "card_colour": "silver"
  },
  "actual_current_month_churn": 0
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
      "value": 35
    },
    {
      "factor": "app_login_change_30d",
      "value": 39.1623
    },
    {
      "factor": "branch_code",
      "value": "BR-120"
    },
    {
      "factor": "customer_segment",
      "value": "vendor"
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
  "customer_id": "C14491",
  "customer_name": "Kevin Taneja",
  "prediction_date": "2026-05-01",
  "target_month": "2026-06-01",
  "profile": {
    "tenure_months": 35,
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
      "balance_change_30d": 0.037,
      "transaction_change_30d": -16.5452,
      "card_spend_change_30d": 22.7644,
      "app_login_change_30d": -28.234,
      "salary_missing_days": null,
      "external_transfer_change_30d": -18.4388,
      "upi_share_of_spend": 0.7028,
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
      "balance_change_30d": 8.3375,
      "transaction_change_30d": -17.0689,
      "card_spend_change_30d": -22.2611,
      "app_login_change_30d": -12.8383,
      "salary_missing_days": null,
      "external_transfer_change_30d": 31.5859,
      "upi_share_of_spend": 0.7864,
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
      "days_since_last_transaction": 5,
      "balance_change_30d": 23.7738,
      "transaction_change_30d": 14.7211,
      "card_spend_change_30d": 12.6991,
      "app_login_change_30d": -13.1261,
      "salary_missing_days": null,
      "external_transfer_change_30d": 0.6466,
      "upi_share_of_spend": 0.756,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 11.3287,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-04-01",
      "days_since_last_transaction": 4,
      "balance_change_30d": 41.1675,
      "transaction_change_30d": 6.0756,
      "card_spend_change_30d": 31.8877,
      "app_login_change_30d": 13.0209,
      "salary_missing_days": null,
      "external_transfer_change_30d": -18.4636,
      "upi_share_of_spend": 0.6474,
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
      "days_since_last_transaction": 9,
      "balance_change_30d": -18.2478,
      "transaction_change_30d": -15.7894,
      "card_spend_change_30d": -33.1002,
      "app_login_change_30d": 19.0392,
      "salary_missing_days": null,
      "external_transfer_change_30d": 33.681,
      "upi_share_of_spend": 0.7436,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 1,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 43.481,
      "emi_bounce_30d": 0
    }
  ],
  "actual_next_month_churn": 0
}
```

#### Model 1 v2 Output

```json
{
  "churn_probability": 4.67,
  "raw_churn_probability": 40.28,
  "probability_mode": "sigmoid",
  "risk_score": 14.0,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "latest_avg_resolution_time_hrs",
      "value": 43.481,
      "message": "This signal increased churn risk.",
      "contribution": 0.3421066403388977
    },
    {
      "factor": "latest_card_spend_change_30d",
      "value": -33.1002,
      "message": "Card spending has been falling across recent months.",
      "contribution": 0.06269463151693344
    },
    {
      "factor": "external_transfer_change_30d_trend_6m",
      "value": 5.419010000000002,
      "message": "External transfers have increased.",
      "contribution": 0.04785650223493576
    },
    {
      "factor": "max_avg_resolution_time_hrs_3m",
      "value": 43.481,
      "message": "This signal increased churn risk.",
      "contribution": 0.021450607106089592
    },
    {
      "factor": "latest_upi_share_of_spend",
      "value": 0.7436,
      "message": "This signal increased churn risk.",
      "contribution": 0.020837316289544106
    }
  ]
}
```

### 52. Vrinda Mahal (`C14979`)

#### Model 1 Input

```json
{
  "customer_id": "C14979",
  "customer_name": "Vrinda Mahal",
  "snapshot_date": "2026-06-01",
  "customer": {
    "age": 49,
    "tenure_months": 100,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 1,
    "has_credit_card": 0,
    "has_loan": 0,
    "days_since_last_transaction": 2,
    "balance_change_30d": -12.1067,
    "transaction_change_30d": -18.4976,
    "card_spend_change_30d": -3.1035,
    "app_login_change_30d": 6.8745,
    "salary_missing_days": 0.0,
    "external_transfer_change_30d": 26.4441,
    "upi_share_of_spend": 0.724,
    "fd_maturing_in_30d": 1,
    "products_dropped_90d": 0,
    "complaints_30d": 6,
    "unresolved_complaints": 6,
    "failed_transactions_30d": 10,
    "avg_resolution_time_hrs": 131.9768,
    "emi_bounce_30d": 0,
    "branch_code": "BR-119",
    "card_colour": "gold"
  },
  "actual_current_month_churn": 0
}
```

#### Model 1 Output

```json
{
  "churn_probability": 48.15,
  "raw_churn_probability": 56.4,
  "risk_score": 80.56,
  "churn_prediction": "Yes",
  "risk_level": "High",
  "top_risk_factors": [
    {
      "factor": "avg_resolution_time_hrs",
      "value": 131.9768
    },
    {
      "factor": "failed_transactions_30d",
      "value": 10
    },
    {
      "factor": "fd_maturing_in_30d",
      "value": 1
    },
    {
      "factor": "complaints_30d",
      "value": 6
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
  "customer_id": "C14979",
  "customer_name": "Vrinda Mahal",
  "prediction_date": "2026-05-01",
  "target_month": "2026-06-01",
  "profile": {
    "tenure_months": 100,
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
      "balance_change_30d": -2.5951,
      "transaction_change_30d": 5.2803,
      "card_spend_change_30d": -11.4005,
      "app_login_change_30d": -15.2209,
      "salary_missing_days": 2.0,
      "external_transfer_change_30d": -11.9745,
      "upi_share_of_spend": 0.7127,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 3,
      "unresolved_complaints": 2,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 63.435,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-02-01",
      "days_since_last_transaction": 0,
      "balance_change_30d": 27.7696,
      "transaction_change_30d": 32.2826,
      "card_spend_change_30d": 24.34,
      "app_login_change_30d": 24.2603,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": 9.1215,
      "upi_share_of_spend": 0.5342,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 2,
      "unresolved_complaints": 1,
      "failed_transactions_30d": 3,
      "avg_resolution_time_hrs": 50.7512,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-03-01",
      "days_since_last_transaction": 6,
      "balance_change_30d": -13.772,
      "transaction_change_30d": -3.698,
      "card_spend_change_30d": -27.8532,
      "app_login_change_30d": -5.8521,
      "salary_missing_days": 1.0,
      "external_transfer_change_30d": -12.6838,
      "upi_share_of_spend": 0.5834,
      "fd_maturing_in_30d": 1,
      "products_dropped_90d": 0,
      "complaints_30d": 6,
      "unresolved_complaints": 4,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 95.8305,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-04-01",
      "days_since_last_transaction": 3,
      "balance_change_30d": -3.4769,
      "transaction_change_30d": -4.5253,
      "card_spend_change_30d": 12.8861,
      "app_login_change_30d": 11.4546,
      "salary_missing_days": 1.0,
      "external_transfer_change_30d": 18.9586,
      "upi_share_of_spend": 0.7596,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 6,
      "unresolved_complaints": 4,
      "failed_transactions_30d": 4,
      "avg_resolution_time_hrs": 93.1215,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-05-01",
      "days_since_last_transaction": 10,
      "balance_change_30d": 3.3703,
      "transaction_change_30d": -3.0049,
      "card_spend_change_30d": -7.9384,
      "app_login_change_30d": 3.4452,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": 26.561,
      "upi_share_of_spend": 0.7092,
      "fd_maturing_in_30d": 1,
      "products_dropped_90d": 0,
      "complaints_30d": 4,
      "unresolved_complaints": 2,
      "failed_transactions_30d": 3,
      "avg_resolution_time_hrs": 41.834,
      "emi_bounce_30d": 0
    }
  ],
  "actual_next_month_churn": 0
}
```

#### Model 1 v2 Output

```json
{
  "churn_probability": 36.85,
  "raw_churn_probability": 86.29,
  "probability_mode": "sigmoid",
  "risk_score": 76.32,
  "churn_prediction": "Yes",
  "risk_level": "High",
  "top_risk_factors": [
    {
      "factor": "max_avg_resolution_time_hrs_3m",
      "value": 95.8305,
      "message": "This signal increased churn risk.",
      "contribution": 0.5834065079689026
    },
    {
      "factor": "latest_avg_resolution_time_hrs",
      "value": 41.834,
      "message": "This signal increased churn risk.",
      "contribution": 0.4121509790420532
    },
    {
      "factor": "sum_failed_transactions_30d_3m",
      "value": 8.0,
      "message": "Customer has recent failed transactions.",
      "contribution": 0.3584021031856537
    },
    {
      "factor": "latest_vs_avg_upi_share_of_spend_available_history",
      "value": 0.0493799999999999,
      "message": "This signal increased churn risk.",
      "contribution": 0.1681366264820099
    },
    {
      "factor": "sum_failed_transactions_30d_6m",
      "value": 12.0,
      "message": "Customer has recent failed transactions.",
      "contribution": 0.1032535508275032
    }
  ]
}
```

### 53. Pooja Atwal (`C14986`)

#### Model 1 Input

```json
{
  "customer_id": "C14986",
  "customer_name": "Pooja Atwal",
  "snapshot_date": "2026-06-01",
  "customer": {
    "age": 37,
    "tenure_months": 147,
    "customer_segment": "farmer",
    "income_regularity": "seasonal",
    "products_count": 2,
    "has_credit_card": 0,
    "has_loan": 0,
    "days_since_last_transaction": 4,
    "balance_change_30d": -7.9448,
    "transaction_change_30d": -14.4918,
    "card_spend_change_30d": 3.1699,
    "app_login_change_30d": -4.6297,
    "salary_missing_days": null,
    "external_transfer_change_30d": 1.5751,
    "upi_share_of_spend": 0.7829,
    "fd_maturing_in_30d": 0,
    "products_dropped_90d": 1,
    "complaints_30d": 0,
    "unresolved_complaints": 0,
    "failed_transactions_30d": 0,
    "avg_resolution_time_hrs": 0.0,
    "emi_bounce_30d": 0,
    "branch_code": "BR-111",
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
      "value": "BR-111"
    },
    {
      "factor": "external_transfer_change_30d",
      "value": 1.5751
    },
    {
      "factor": "products_dropped_90d",
      "value": 1
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
  "customer_id": "C14986",
  "customer_name": "Pooja Atwal",
  "prediction_date": "2026-05-01",
  "target_month": "2026-06-01",
  "profile": {
    "tenure_months": 147,
    "customer_segment": "farmer",
    "income_regularity": "seasonal",
    "products_count": 2,
    "has_credit_card": 0,
    "has_loan": 0
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 1,
      "balance_change_30d": 8.4833,
      "transaction_change_30d": -4.8834,
      "card_spend_change_30d": -11.5412,
      "app_login_change_30d": -18.6379,
      "salary_missing_days": null,
      "external_transfer_change_30d": 53.6854,
      "upi_share_of_spend": 0.6883,
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
      "balance_change_30d": -29.1498,
      "transaction_change_30d": -26.0471,
      "card_spend_change_30d": -45.3916,
      "app_login_change_30d": -30.9422,
      "salary_missing_days": null,
      "external_transfer_change_30d": 54.0986,
      "upi_share_of_spend": 0.8592,
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
      "balance_change_30d": 12.1205,
      "transaction_change_30d": 0.6089,
      "card_spend_change_30d": 8.6369,
      "app_login_change_30d": -0.4024,
      "salary_missing_days": null,
      "external_transfer_change_30d": 22.8104,
      "upi_share_of_spend": 0.6,
      "fd_maturing_in_30d": 1,
      "products_dropped_90d": 1,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 38.6639,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-04-01",
      "days_since_last_transaction": 0,
      "balance_change_30d": 18.4727,
      "transaction_change_30d": 15.1391,
      "card_spend_change_30d": 27.4491,
      "app_login_change_30d": 7.7726,
      "salary_missing_days": null,
      "external_transfer_change_30d": 25.4243,
      "upi_share_of_spend": 0.6455,
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
      "balance_change_30d": -37.4316,
      "transaction_change_30d": -11.7788,
      "card_spend_change_30d": 0.0115,
      "app_login_change_30d": -19.8579,
      "salary_missing_days": null,
      "external_transfer_change_30d": 31.5223,
      "upi_share_of_spend": 0.6853,
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
  "churn_probability": 2.03,
  "raw_churn_probability": 24.28,
  "probability_mode": "sigmoid",
  "risk_score": 6.08,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "latest_balance_change_30d",
      "value": -37.4316,
      "message": "Balance has been falling across recent months.",
      "contribution": 0.1697123944759369
    },
    {
      "factor": "sum_fd_maturing_in_30d_3m",
      "value": 1.0,
      "message": "Customer has a fixed deposit maturing soon.",
      "contribution": 0.0844864770770073
    },
    {
      "factor": "latest_upi_share_of_spend",
      "value": 0.6853,
      "message": "This signal increased churn risk.",
      "contribution": 0.023038379848003387
    },
    {
      "factor": "card_spend_change_30d_trend_6m",
      "value": 9.594610000000008,
      "message": "This signal increased churn risk.",
      "contribution": 0.02036401443183422
    },
    {
      "factor": "latest_vs_avg_card_spend_change_30d_available_history",
      "value": 4.17856,
      "message": "This signal increased churn risk.",
      "contribution": 0.015085880644619465
    }
  ]
}
```

### 54. Varenya Rana (`C15055`)

#### Model 1 Input

```json
{
  "customer_id": "C15055",
  "customer_name": "Varenya Rana",
  "snapshot_date": "2026-06-01",
  "customer": {
    "age": 42,
    "tenure_months": 211,
    "customer_segment": "farmer",
    "income_regularity": "seasonal",
    "products_count": 4,
    "has_credit_card": 0,
    "has_loan": 1,
    "days_since_last_transaction": 0,
    "balance_change_30d": 29.5707,
    "transaction_change_30d": 35.8007,
    "card_spend_change_30d": 30.57,
    "app_login_change_30d": 25.1137,
    "salary_missing_days": null,
    "external_transfer_change_30d": -22.2795,
    "upi_share_of_spend": 0.4104,
    "fd_maturing_in_30d": 1,
    "products_dropped_90d": 0,
    "complaints_30d": 0,
    "unresolved_complaints": 0,
    "failed_transactions_30d": 1,
    "avg_resolution_time_hrs": 0.0,
    "emi_bounce_30d": 0,
    "branch_code": "BR-102",
    "card_colour": "gold"
  },
  "actual_current_month_churn": 0
}
```

#### Model 1 Output

```json
{
  "churn_probability": 1.96,
  "raw_churn_probability": 1.68,
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
      "value": "BR-102"
    },
    {
      "factor": "app_login_change_30d",
      "value": 25.1137
    },
    {
      "factor": "has_loan",
      "value": 1
    }
  ]
}
```

#### Model 1 v2 Input

```json
{
  "customer_id": "C15055",
  "customer_name": "Varenya Rana",
  "prediction_date": "2026-05-01",
  "target_month": "2026-06-01",
  "profile": {
    "tenure_months": 211,
    "customer_segment": "farmer",
    "income_regularity": "seasonal",
    "products_count": 4,
    "has_credit_card": 0,
    "has_loan": 1
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 8,
      "balance_change_30d": -5.2209,
      "transaction_change_30d": -4.2348,
      "card_spend_change_30d": 3.1187,
      "app_login_change_30d": 1.3651,
      "salary_missing_days": null,
      "external_transfer_change_30d": 17.9955,
      "upi_share_of_spend": 0.5408,
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
      "balance_change_30d": 8.8021,
      "transaction_change_30d": -21.6213,
      "card_spend_change_30d": 11.8809,
      "app_login_change_30d": 15.6098,
      "salary_missing_days": null,
      "external_transfer_change_30d": 12.3963,
      "upi_share_of_spend": 0.4993,
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
      "days_since_last_transaction": 1,
      "balance_change_30d": 6.9535,
      "transaction_change_30d": 3.6638,
      "card_spend_change_30d": 3.5964,
      "app_login_change_30d": 10.6444,
      "salary_missing_days": null,
      "external_transfer_change_30d": -25.0625,
      "upi_share_of_spend": 0.5056,
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
      "balance_change_30d": 51.3749,
      "transaction_change_30d": 16.9878,
      "card_spend_change_30d": 4.6819,
      "app_login_change_30d": -10.7974,
      "salary_missing_days": null,
      "external_transfer_change_30d": -0.8684,
      "upi_share_of_spend": 0.435,
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
      "balance_change_30d": 27.8226,
      "transaction_change_30d": 24.1829,
      "card_spend_change_30d": 22.4503,
      "app_login_change_30d": -17.4075,
      "salary_missing_days": null,
      "external_transfer_change_30d": -1.7451,
      "upi_share_of_spend": 0.4626,
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
  "churn_probability": 1.46,
  "raw_churn_probability": 18.04,
  "probability_mode": "sigmoid",
  "risk_score": 4.37,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "avg_balance_change_30d_3m",
      "value": 28.717,
      "message": "This signal increased churn risk.",
      "contribution": 0.019225291907787323
    },
    {
      "factor": "avg_app_login_change_30d_6m",
      "value": -0.1171200000000006,
      "message": "App usage has been falling across recent months.",
      "contribution": 0.007027223706245422
    },
    {
      "factor": "count_balance_drop_3m",
      "value": 0,
      "message": "This signal increased churn risk.",
      "contribution": 0.0026914579793810844
    },
    {
      "factor": "count_external_transfer_rise_6m",
      "value": 0,
      "message": "This signal increased churn risk.",
      "contribution": 0.002688427222892642
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

### 55. Wyatt Modi (`C15182`)

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

### 56. Chanchal Khanna (`C15184`)

#### Model 1 Input

```json
{
  "customer_id": "C15184",
  "customer_name": "Chanchal Khanna",
  "snapshot_date": "2026-05-01",
  "customer": {
    "age": 45,
    "tenure_months": 122,
    "customer_segment": "business",
    "income_regularity": "irregular",
    "products_count": 3,
    "has_credit_card": 1,
    "has_loan": 1,
    "days_since_last_transaction": 31,
    "balance_change_30d": -79.4454,
    "transaction_change_30d": -70.181,
    "card_spend_change_30d": -70.7809,
    "app_login_change_30d": -57.381,
    "salary_missing_days": null,
    "external_transfer_change_30d": 109.285,
    "upi_share_of_spend": 0.996,
    "fd_maturing_in_30d": 0,
    "products_dropped_90d": 3,
    "complaints_30d": 0,
    "unresolved_complaints": 0,
    "failed_transactions_30d": 5,
    "avg_resolution_time_hrs": 0.0,
    "emi_bounce_30d": 1,
    "branch_code": "BR-138",
    "card_colour": "silver"
  },
  "actual_current_month_churn": 1
}
```

#### Model 1 Output

```json
{
  "churn_probability": 95.65,
  "raw_churn_probability": 83.24,
  "risk_score": 98.37,
  "churn_prediction": "Yes",
  "risk_level": "High",
  "top_risk_factors": [
    {
      "factor": "balance_change_30d",
      "value": -79.4454
    },
    {
      "factor": "days_since_last_transaction",
      "value": 31
    },
    {
      "factor": "card_spend_change_30d",
      "value": -70.7809
    },
    {
      "factor": "transaction_change_30d",
      "value": -70.181
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
  "customer_id": "C15184",
  "customer_name": "Chanchal Khanna",
  "prediction_date": "2026-04-01",
  "target_month": "2026-05-01",
  "profile": {
    "tenure_months": 122,
    "customer_segment": "business",
    "income_regularity": "irregular",
    "products_count": 3,
    "has_credit_card": 1,
    "has_loan": 1
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 10,
      "balance_change_30d": 5.612,
      "transaction_change_30d": 26.5129,
      "card_spend_change_30d": 20.0444,
      "app_login_change_30d": -7.2051,
      "salary_missing_days": null,
      "external_transfer_change_30d": -13.6105,
      "upi_share_of_spend": 0.6197,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 5.3479,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-02-01",
      "days_since_last_transaction": 16,
      "balance_change_30d": -1.443,
      "transaction_change_30d": 3.2271,
      "card_spend_change_30d": 10.3347,
      "app_login_change_30d": -22.7243,
      "salary_missing_days": null,
      "external_transfer_change_30d": 27.1187,
      "upi_share_of_spend": 0.6692,
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
      "days_since_last_transaction": 15,
      "balance_change_30d": -30.9373,
      "transaction_change_30d": -10.0252,
      "card_spend_change_30d": -4.744,
      "app_login_change_30d": -20.5306,
      "salary_missing_days": null,
      "external_transfer_change_30d": 33.4294,
      "upi_share_of_spend": 0.7973,
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
      "days_since_last_transaction": 14,
      "balance_change_30d": -32.9477,
      "transaction_change_30d": -16.7412,
      "card_spend_change_30d": -46.0339,
      "app_login_change_30d": -27.9831,
      "salary_missing_days": null,
      "external_transfer_change_30d": 38.4946,
      "upi_share_of_spend": 0.6877,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 0,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 5,
      "avg_resolution_time_hrs": 0.0,
      "emi_bounce_30d": 1
    }
  ],
  "actual_next_month_churn": 1
}
```

#### Model 1 v2 Output

```json
{
  "churn_probability": 30.12,
  "raw_churn_probability": 80.67,
  "probability_mode": "sigmoid",
  "risk_score": 73.8,
  "churn_prediction": "Yes",
  "risk_level": "High",
  "top_risk_factors": [
    {
      "factor": "latest_days_since_last_transaction",
      "value": 14,
      "message": "Customer has gone longer without transacting.",
      "contribution": 0.4759744703769684
    },
    {
      "factor": "sum_failed_transactions_30d_3m",
      "value": 7.0,
      "message": "Customer has recent failed transactions.",
      "contribution": 0.2881186604499817
    },
    {
      "factor": "latest_balance_change_30d",
      "value": -32.9477,
      "message": "Balance has been falling across recent months.",
      "contribution": 0.20228052139282227
    },
    {
      "factor": "latest_card_spend_change_30d",
      "value": -46.0339,
      "message": "Card spending has been falling across recent months.",
      "contribution": 0.20207470655441284
    },
    {
      "factor": "days_since_last_transaction_trend_6m",
      "value": 1.1000000000000003,
      "message": "Customer has gone longer without transacting.",
      "contribution": 0.11450693011283875
    }
  ]
}
```

### 57. Hemal Wagle (`C15335`)

#### Model 1 Input

```json
{
  "customer_id": "C15335",
  "customer_name": "Hemal Wagle",
  "snapshot_date": "2026-05-01",
  "customer": {
    "age": 50,
    "tenure_months": 221,
    "customer_segment": "farmer",
    "income_regularity": "seasonal",
    "products_count": 1,
    "has_credit_card": 0,
    "has_loan": 0,
    "days_since_last_transaction": 18,
    "balance_change_30d": -55.349,
    "transaction_change_30d": 5.9032,
    "card_spend_change_30d": -38.0502,
    "app_login_change_30d": -9.2858,
    "salary_missing_days": null,
    "external_transfer_change_30d": 38.5428,
    "upi_share_of_spend": 0.8145,
    "fd_maturing_in_30d": 0,
    "products_dropped_90d": 0,
    "complaints_30d": 2,
    "unresolved_complaints": 1,
    "failed_transactions_30d": 3,
    "avg_resolution_time_hrs": 36.2894,
    "emi_bounce_30d": 0,
    "branch_code": "BR-114",
    "card_colour": "black"
  },
  "actual_current_month_churn": 1
}
```

#### Model 1 Output

```json
{
  "churn_probability": 36.3,
  "raw_churn_probability": 41.37,
  "risk_score": 76.11,
  "churn_prediction": "Yes",
  "risk_level": "High",
  "top_risk_factors": [
    {
      "factor": "balance_change_30d",
      "value": -55.349
    },
    {
      "factor": "card_spend_change_30d",
      "value": -38.0502
    },
    {
      "factor": "days_since_last_transaction",
      "value": 18
    },
    {
      "factor": "failed_transactions_30d",
      "value": 3
    },
    {
      "factor": "complaints_30d",
      "value": 2
    }
  ]
}
```

#### Model 1 v2 Input

```json
{
  "customer_id": "C15335",
  "customer_name": "Hemal Wagle",
  "prediction_date": "2026-04-01",
  "target_month": "2026-05-01",
  "profile": {
    "tenure_months": 221,
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
      "balance_change_30d": -25.7493,
      "transaction_change_30d": -19.7073,
      "card_spend_change_30d": -38.6379,
      "app_login_change_30d": -32.4897,
      "salary_missing_days": null,
      "external_transfer_change_30d": 22.5084,
      "upi_share_of_spend": 0.7862,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 23.9063,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-02-01",
      "days_since_last_transaction": 17,
      "balance_change_30d": -24.5562,
      "transaction_change_30d": -14.0207,
      "card_spend_change_30d": -3.3417,
      "app_login_change_30d": -3.2117,
      "salary_missing_days": null,
      "external_transfer_change_30d": 75.5818,
      "upi_share_of_spend": 0.7783,
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
      "balance_change_30d": -43.0431,
      "transaction_change_30d": -26.4035,
      "card_spend_change_30d": 4.2139,
      "app_login_change_30d": -4.306,
      "salary_missing_days": null,
      "external_transfer_change_30d": 41.4968,
      "upi_share_of_spend": 0.85,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 1,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 3,
      "avg_resolution_time_hrs": 38.2104,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-04-01",
      "days_since_last_transaction": 10,
      "balance_change_30d": -10.3187,
      "transaction_change_30d": -20.119,
      "card_spend_change_30d": -34.8954,
      "app_login_change_30d": -16.4425,
      "salary_missing_days": null,
      "external_transfer_change_30d": 4.1474,
      "upi_share_of_spend": 0.7777,
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
  "churn_probability": 4.07,
  "raw_churn_probability": 37.61,
  "probability_mode": "sigmoid",
  "risk_score": 12.2,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "latest_transaction_change_30d",
      "value": -20.119,
      "message": "Transaction activity has been falling across recent months.",
      "contribution": 0.14789995551109314
    },
    {
      "factor": "latest_vs_avg_external_transfer_change_30d_available_history",
      "value": -31.786200000000004,
      "message": "This signal increased churn risk.",
      "contribution": 0.12890073657035828
    },
    {
      "factor": "latest_card_spend_change_30d",
      "value": -34.8954,
      "message": "Card spending has been falling across recent months.",
      "contribution": 0.0984719842672348
    },
    {
      "factor": "count_quiet_customer_3m",
      "value": 2,
      "message": "This signal increased churn risk.",
      "contribution": 0.05941136181354523
    },
    {
      "factor": "count_balance_drop_3m",
      "value": 3,
      "message": "This signal increased churn risk.",
      "contribution": 0.056010790169239044
    }
  ]
}
```

### 58. Urvashi Bhasin (`C15360`)

#### Model 1 Input

```json
{
  "customer_id": "C15360",
  "customer_name": "Urvashi Bhasin",
  "snapshot_date": "2026-06-01",
  "customer": {
    "age": 30,
    "tenure_months": 60,
    "customer_segment": "vendor",
    "income_regularity": "irregular",
    "products_count": 2,
    "has_credit_card": 0,
    "has_loan": 0,
    "days_since_last_transaction": 25,
    "balance_change_30d": -58.2982,
    "transaction_change_30d": -43.5092,
    "card_spend_change_30d": -66.9059,
    "app_login_change_30d": -71.0304,
    "salary_missing_days": null,
    "external_transfer_change_30d": 107.4829,
    "upi_share_of_spend": 0.6764,
    "fd_maturing_in_30d": 0,
    "products_dropped_90d": 0,
    "complaints_30d": 3,
    "unresolved_complaints": 2,
    "failed_transactions_30d": 4,
    "avg_resolution_time_hrs": 61.7847,
    "emi_bounce_30d": 0,
    "branch_code": "BR-110",
    "card_colour": "silver"
  },
  "actual_current_month_churn": 1
}
```

#### Model 1 Output

```json
{
  "churn_probability": 100.0,
  "raw_churn_probability": 87.56,
  "risk_score": 100.0,
  "churn_prediction": "Yes",
  "risk_level": "High",
  "top_risk_factors": [
    {
      "factor": "balance_change_30d",
      "value": -58.2982
    },
    {
      "factor": "days_since_last_transaction",
      "value": 25
    },
    {
      "factor": "card_spend_change_30d",
      "value": -66.9059
    },
    {
      "factor": "failed_transactions_30d",
      "value": 4
    },
    {
      "factor": "complaints_30d",
      "value": 3
    }
  ]
}
```

#### Model 1 v2 Input

```json
{
  "customer_id": "C15360",
  "customer_name": "Urvashi Bhasin",
  "prediction_date": "2026-05-01",
  "target_month": "2026-06-01",
  "profile": {
    "tenure_months": 60,
    "customer_segment": "vendor",
    "income_regularity": "irregular",
    "products_count": 2,
    "has_credit_card": 0,
    "has_loan": 0
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 3,
      "balance_change_30d": 24.3184,
      "transaction_change_30d": 19.4102,
      "card_spend_change_30d": 27.8684,
      "app_login_change_30d": 32.0458,
      "salary_missing_days": null,
      "external_transfer_change_30d": -69.872,
      "upi_share_of_spend": 0.4334,
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
      "days_since_last_transaction": 11,
      "balance_change_30d": -1.7301,
      "transaction_change_30d": -19.6776,
      "card_spend_change_30d": -5.0284,
      "app_login_change_30d": 19.8961,
      "salary_missing_days": null,
      "external_transfer_change_30d": -5.7079,
      "upi_share_of_spend": 0.4859,
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
      "balance_change_30d": 10.9151,
      "transaction_change_30d": -3.0898,
      "card_spend_change_30d": -26.3984,
      "app_login_change_30d": -24.145,
      "salary_missing_days": null,
      "external_transfer_change_30d": 10.6031,
      "upi_share_of_spend": 0.486,
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
      "days_since_last_transaction": 19,
      "balance_change_30d": -24.2428,
      "transaction_change_30d": -42.2718,
      "card_spend_change_30d": -7.3214,
      "app_login_change_30d": -30.7583,
      "salary_missing_days": null,
      "external_transfer_change_30d": 3.0601,
      "upi_share_of_spend": 0.4533,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 1,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 53.8138,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-05-01",
      "days_since_last_transaction": 16,
      "balance_change_30d": -37.4282,
      "transaction_change_30d": -31.73,
      "card_spend_change_30d": -37.7143,
      "app_login_change_30d": -37.1633,
      "salary_missing_days": null,
      "external_transfer_change_30d": 17.4848,
      "upi_share_of_spend": 0.6061,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 18.8848,
      "emi_bounce_30d": 0
    }
  ],
  "actual_next_month_churn": 1
}
```

#### Model 1 v2 Output

```json
{
  "churn_probability": 40.0,
  "raw_churn_probability": 88.77,
  "probability_mode": "sigmoid",
  "risk_score": 77.5,
  "churn_prediction": "Yes",
  "risk_level": "High",
  "top_risk_factors": [
    {
      "factor": "latest_days_since_last_transaction",
      "value": 16,
      "message": "Customer has gone longer without transacting.",
      "contribution": 0.4677756130695343
    },
    {
      "factor": "latest_transaction_change_30d",
      "value": -31.73,
      "message": "Transaction activity has been falling across recent months.",
      "contribution": 0.262341171503067
    },
    {
      "factor": "latest_vs_avg_upi_share_of_spend_available_history",
      "value": 0.1131599999999999,
      "message": "This signal increased churn risk.",
      "contribution": 0.24741818010807037
    },
    {
      "factor": "latest_balance_change_30d",
      "value": -37.4282,
      "message": "Balance has been falling across recent months.",
      "contribution": 0.23680326342582703
    },
    {
      "factor": "max_avg_resolution_time_hrs_3m",
      "value": 53.8138,
      "message": "This signal increased churn risk.",
      "contribution": 0.1822301298379898
    }
  ]
}
```

### 59. Raagini Rai (`C15469`)

#### Model 1 Input

```json
{
  "customer_id": "C15469",
  "customer_name": "Raagini Rai",
  "snapshot_date": "2026-04-01",
  "customer": {
    "age": 43,
    "tenure_months": 58,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 2,
    "has_credit_card": 0,
    "has_loan": 0,
    "days_since_last_transaction": 22,
    "balance_change_30d": -11.0384,
    "transaction_change_30d": -24.3072,
    "card_spend_change_30d": -23.3186,
    "app_login_change_30d": -16.3508,
    "salary_missing_days": 4.0,
    "external_transfer_change_30d": 38.9204,
    "upi_share_of_spend": 0.4862,
    "fd_maturing_in_30d": 0,
    "products_dropped_90d": 0,
    "complaints_30d": 0,
    "unresolved_complaints": 0,
    "failed_transactions_30d": 3,
    "avg_resolution_time_hrs": 0.0,
    "emi_bounce_30d": 0,
    "branch_code": "BR-115",
    "card_colour": "blue"
  },
  "actual_current_month_churn": 1
}
```

#### Model 1 Output

```json
{
  "churn_probability": 9.94,
  "raw_churn_probability": 10.47,
  "risk_score": 29.81,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "days_since_last_transaction",
      "value": 22
    },
    {
      "factor": "salary_missing_days",
      "value": 4.0
    },
    {
      "factor": "failed_transactions_30d",
      "value": 3
    },
    {
      "factor": "card_spend_change_30d",
      "value": -23.3186
    },
    {
      "factor": "tenure_months",
      "value": 58
    }
  ]
}
```

#### Model 1 v2 Input

```json
{
  "customer_id": "C15469",
  "customer_name": "Raagini Rai",
  "prediction_date": "2026-03-01",
  "target_month": "2026-04-01",
  "profile": {
    "tenure_months": 58,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 2,
    "has_credit_card": 0,
    "has_loan": 0
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 13,
      "balance_change_30d": -26.6316,
      "transaction_change_30d": -2.5603,
      "card_spend_change_30d": 0.9206,
      "app_login_change_30d": -6.9277,
      "salary_missing_days": 1.0,
      "external_transfer_change_30d": 36.1028,
      "upi_share_of_spend": 0.3547,
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
      "balance_change_30d": 10.4002,
      "transaction_change_30d": -3.5712,
      "card_spend_change_30d": 6.5305,
      "app_login_change_30d": 12.0053,
      "salary_missing_days": 2.0,
      "external_transfer_change_30d": 50.0677,
      "upi_share_of_spend": 0.4073,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 2,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 25.3538,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-03-01",
      "days_since_last_transaction": 16,
      "balance_change_30d": -1.1408,
      "transaction_change_30d": -8.929,
      "card_spend_change_30d": 10.8841,
      "app_login_change_30d": 43.4899,
      "salary_missing_days": 1.0,
      "external_transfer_change_30d": -12.3701,
      "upi_share_of_spend": 0.39,
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
  "churn_probability": 3.7,
  "raw_churn_probability": 35.79,
  "probability_mode": "sigmoid",
  "risk_score": 11.11,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "latest_days_since_last_transaction",
      "value": 16,
      "message": "Customer has gone longer without transacting.",
      "contribution": 0.4474121630191803
    },
    {
      "factor": "days_since_last_transaction_trend_6m",
      "value": 1.4999999999999984,
      "message": "Customer has gone longer without transacting.",
      "contribution": 0.08147028088569641
    },
    {
      "factor": "latest_vs_avg_external_transfer_change_30d_available_history",
      "value": -36.97023333333333,
      "message": "This signal increased churn risk.",
      "contribution": 0.03805823624134064
    },
    {
      "factor": "count_quiet_customer_3m",
      "value": 3,
      "message": "This signal increased churn risk.",
      "contribution": 0.025528190657496452
    },
    {
      "factor": "transaction_change_30d_trend_6m",
      "value": -3.18435,
      "message": "Transaction activity has been falling across recent months.",
      "contribution": 0.01893628016114235
    }
  ]
}
```

### 60. Krisha Rajagopal (`C15597`)

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

### 61. Vasana Talwar (`C15682`)

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

### 62. Ekalinga Ram (`C15711`)

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

### 63. Karan De (`C15967`)

#### Model 1 Input

```json
{
  "customer_id": "C15967",
  "customer_name": "Karan De",
  "snapshot_date": "2026-02-01",
  "customer": {
    "age": 28,
    "tenure_months": 1,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 2,
    "has_credit_card": 1,
    "has_loan": 0,
    "days_since_last_transaction": 15,
    "balance_change_30d": -7.5547,
    "transaction_change_30d": -34.7327,
    "card_spend_change_30d": -37.2042,
    "app_login_change_30d": -17.4249,
    "salary_missing_days": 3.0,
    "external_transfer_change_30d": 20.6294,
    "upi_share_of_spend": 0.5821,
    "fd_maturing_in_30d": 1,
    "products_dropped_90d": 0,
    "complaints_30d": 5,
    "unresolved_complaints": 4,
    "failed_transactions_30d": 4,
    "avg_resolution_time_hrs": 101.8931,
    "emi_bounce_30d": 0,
    "branch_code": "BR-122",
    "card_colour": "black"
  },
  "actual_current_month_churn": 1
}
```

#### Model 1 Output

```json
{
  "churn_probability": 95.65,
  "raw_churn_probability": 85.55,
  "risk_score": 98.37,
  "churn_prediction": "Yes",
  "risk_level": "High",
  "top_risk_factors": [
    {
      "factor": "avg_resolution_time_hrs",
      "value": 101.8931
    },
    {
      "factor": "fd_maturing_in_30d",
      "value": 1
    },
    {
      "factor": "card_spend_change_30d",
      "value": -37.2042
    },
    {
      "factor": "tenure_months",
      "value": 1
    },
    {
      "factor": "failed_transactions_30d",
      "value": 4
    }
  ]
}
```

#### Model 1 v2 Input

```json
{
  "customer_id": "C15967",
  "customer_name": "Karan De",
  "prediction_date": "2026-01-01",
  "target_month": "2026-02-01",
  "profile": {
    "tenure_months": 1,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 2,
    "has_credit_card": 1,
    "has_loan": 0
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 17,
      "balance_change_30d": 5.2731,
      "transaction_change_30d": -1.1242,
      "card_spend_change_30d": 0.6629,
      "app_login_change_30d": 15.004,
      "salary_missing_days": 3.0,
      "external_transfer_change_30d": -0.536,
      "upi_share_of_spend": 0.61,
      "fd_maturing_in_30d": 1,
      "products_dropped_90d": 0,
      "complaints_30d": 6,
      "unresolved_complaints": 3,
      "failed_transactions_30d": 3,
      "avg_resolution_time_hrs": 70.5756,
      "emi_bounce_30d": 0
    }
  ],
  "actual_next_month_churn": 1
}
```

#### Model 1 v2 Output

```json
{
  "churn_probability": 35.0,
  "raw_churn_probability": 84.8,
  "probability_mode": "sigmoid",
  "risk_score": 75.63,
  "churn_prediction": "Yes",
  "risk_level": "High",
  "top_risk_factors": [
    {
      "factor": "max_avg_resolution_time_hrs_3m",
      "value": 70.5756,
      "message": "This signal increased churn risk.",
      "contribution": 0.3820260763168335
    },
    {
      "factor": "latest_avg_resolution_time_hrs",
      "value": 70.5756,
      "message": "This signal increased churn risk.",
      "contribution": 0.34796226024627686
    },
    {
      "factor": "latest_days_since_last_transaction",
      "value": 17,
      "message": "Customer has gone longer without transacting.",
      "contribution": 0.23612761497497559
    },
    {
      "factor": "latest_salary_missing_days",
      "value": 3.0,
      "message": "This signal increased churn risk.",
      "contribution": 0.20353451371192932
    },
    {
      "factor": "latest_failed_transactions_30d",
      "value": 3,
      "message": "Customer has recent failed transactions.",
      "contribution": 0.11054258048534393
    }
  ]
}
```

### 64. Robert Sidhu (`C16060`)

#### Model 1 Input

```json
{
  "customer_id": "C16060",
  "customer_name": "Robert Sidhu",
  "snapshot_date": "2026-03-01",
  "customer": {
    "age": 46,
    "tenure_months": 24,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 3,
    "has_credit_card": 0,
    "has_loan": 0,
    "days_since_last_transaction": 7,
    "balance_change_30d": -39.6159,
    "transaction_change_30d": -43.9265,
    "card_spend_change_30d": -38.3602,
    "app_login_change_30d": -17.2799,
    "salary_missing_days": 4.0,
    "external_transfer_change_30d": 94.6045,
    "upi_share_of_spend": 0.3878,
    "fd_maturing_in_30d": 1,
    "products_dropped_90d": 0,
    "complaints_30d": 0,
    "unresolved_complaints": 0,
    "failed_transactions_30d": 1,
    "avg_resolution_time_hrs": 0.0,
    "emi_bounce_30d": 0,
    "branch_code": "BR-115",
    "card_colour": "gold"
  },
  "actual_current_month_churn": 1
}
```

#### Model 1 Output

```json
{
  "churn_probability": 36.3,
  "raw_churn_probability": 38.49,
  "risk_score": 76.11,
  "churn_prediction": "Yes",
  "risk_level": "High",
  "top_risk_factors": [
    {
      "factor": "balance_change_30d",
      "value": -39.6159
    },
    {
      "factor": "card_spend_change_30d",
      "value": -38.3602
    },
    {
      "factor": "tenure_months",
      "value": 24
    },
    {
      "factor": "salary_missing_days",
      "value": 4.0
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
  "customer_id": "C16060",
  "customer_name": "Robert Sidhu",
  "prediction_date": "2026-02-01",
  "target_month": "2026-03-01",
  "profile": {
    "tenure_months": 24,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 3,
    "has_credit_card": 0,
    "has_loan": 0
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 3,
      "balance_change_30d": 0.2485,
      "transaction_change_30d": -18.2111,
      "card_spend_change_30d": -28.2989,
      "app_login_change_30d": -13.6687,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": 30.5717,
      "upi_share_of_spend": 0.1194,
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
      "balance_change_30d": -37.4784,
      "transaction_change_30d": -17.0302,
      "card_spend_change_30d": -11.3501,
      "app_login_change_30d": -33.2492,
      "salary_missing_days": 3.0,
      "external_transfer_change_30d": 66.0381,
      "upi_share_of_spend": 0.2325,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 3,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 2,
      "avg_resolution_time_hrs": 22.1637,
      "emi_bounce_30d": 0
    }
  ],
  "actual_next_month_churn": 1
}
```

#### Model 1 v2 Output

```json
{
  "churn_probability": 18.74,
  "raw_churn_probability": 69.06,
  "probability_mode": "sigmoid",
  "risk_score": 64.97,
  "churn_prediction": "Yes",
  "risk_level": "Medium",
  "top_risk_factors": [
    {
      "factor": "latest_vs_avg_upi_share_of_spend_available_history",
      "value": 0.05655,
      "message": "This signal increased churn risk.",
      "contribution": 0.21545115113258362
    },
    {
      "factor": "latest_balance_change_30d",
      "value": -37.4784,
      "message": "Balance has been falling across recent months.",
      "contribution": 0.21288222074508667
    },
    {
      "factor": "latest_salary_missing_days",
      "value": 3.0,
      "message": "This signal increased churn risk.",
      "contribution": 0.20553579926490784
    },
    {
      "factor": "days_since_last_transaction_trend_6m",
      "value": 7.999999999999998,
      "message": "Customer has gone longer without transacting.",
      "contribution": 0.18898233771324158
    },
    {
      "factor": "latest_transaction_change_30d",
      "value": -17.0302,
      "message": "Transaction activity has been falling across recent months.",
      "contribution": 0.16116780042648315
    }
  ]
}
```

### 65. Urvi Kapadia (`C16084`)

#### Model 1 Input

```json
{
  "customer_id": "C16084",
  "customer_name": "Urvi Kapadia",
  "snapshot_date": "2026-06-01",
  "customer": {
    "age": 46,
    "tenure_months": 137,
    "customer_segment": "farmer",
    "income_regularity": "seasonal",
    "products_count": 1,
    "has_credit_card": 0,
    "has_loan": 0,
    "days_since_last_transaction": 0,
    "balance_change_30d": 44.8976,
    "transaction_change_30d": 50.8078,
    "card_spend_change_30d": 46.4943,
    "app_login_change_30d": 62.4612,
    "salary_missing_days": null,
    "external_transfer_change_30d": -100.0,
    "upi_share_of_spend": 0.0726,
    "fd_maturing_in_30d": 0,
    "products_dropped_90d": 0,
    "complaints_30d": 0,
    "unresolved_complaints": 0,
    "failed_transactions_30d": 1,
    "avg_resolution_time_hrs": 0.0,
    "emi_bounce_30d": 0,
    "branch_code": "BR-101",
    "card_colour": "blue"
  },
  "actual_current_month_churn": 0
}
```

#### Model 1 Output

```json
{
  "churn_probability": 1.96,
  "raw_churn_probability": 1.72,
  "risk_score": 5.87,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "branch_code",
      "value": "BR-101"
    },
    {
      "factor": "app_login_change_30d",
      "value": 62.4612
    },
    {
      "factor": "upi_share_of_spend",
      "value": 0.0726
    },
    {
      "factor": "card_colour",
      "value": "blue"
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
  "customer_id": "C16084",
  "customer_name": "Urvi Kapadia",
  "prediction_date": "2026-05-01",
  "target_month": "2026-06-01",
  "profile": {
    "tenure_months": 137,
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
      "balance_change_30d": 7.5985,
      "transaction_change_30d": -15.4382,
      "card_spend_change_30d": 31.1733,
      "app_login_change_30d": -9.1533,
      "salary_missing_days": null,
      "external_transfer_change_30d": -8.4631,
      "upi_share_of_spend": 0.1898,
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
      "balance_change_30d": 8.7079,
      "transaction_change_30d": 23.7268,
      "card_spend_change_30d": 32.6055,
      "app_login_change_30d": 8.2802,
      "salary_missing_days": null,
      "external_transfer_change_30d": -12.506,
      "upi_share_of_spend": 0.2664,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 27.6048,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-03-01",
      "days_since_last_transaction": 6,
      "balance_change_30d": 43.459,
      "transaction_change_30d": 12.9773,
      "card_spend_change_30d": 4.9074,
      "app_login_change_30d": 30.1094,
      "salary_missing_days": null,
      "external_transfer_change_30d": -4.5716,
      "upi_share_of_spend": 0.1433,
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
      "balance_change_30d": 19.0883,
      "transaction_change_30d": 16.7292,
      "card_spend_change_30d": 32.902,
      "app_login_change_30d": 34.4956,
      "salary_missing_days": null,
      "external_transfer_change_30d": -29.0868,
      "upi_share_of_spend": 0.2093,
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
      "balance_change_30d": 50.1747,
      "transaction_change_30d": 33.4132,
      "card_spend_change_30d": 46.1171,
      "app_login_change_30d": 18.1534,
      "salary_missing_days": null,
      "external_transfer_change_30d": -72.0235,
      "upi_share_of_spend": 0.177,
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
  "churn_probability": 1.74,
  "raw_churn_probability": 21.34,
  "probability_mode": "sigmoid",
  "risk_score": 5.21,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "latest_vs_avg_balance_change_30d_available_history",
      "value": 24.36902,
      "message": "This signal increased churn risk.",
      "contribution": 0.05225330591201782
    },
    {
      "factor": "latest_vs_avg_external_transfer_change_30d_available_history",
      "value": -46.6933,
      "message": "This signal increased churn risk.",
      "contribution": 0.04948611930012703
    },
    {
      "factor": "latest_external_transfer_change_30d",
      "value": -72.0235,
      "message": "This signal increased churn risk.",
      "contribution": 0.04057292267680168
    },
    {
      "factor": "avg_balance_change_30d_3m",
      "value": 37.574000000000005,
      "message": "This signal increased churn risk.",
      "contribution": 0.014775191433727741
    },
    {
      "factor": "avg_external_transfer_change_30d_6m",
      "value": -25.3302,
      "message": "This signal increased churn risk.",
      "contribution": 0.013742024078965187
    }
  ]
}
```

### 66. Aradhana Soni (`C16121`)

#### Model 1 Input

```json
{
  "customer_id": "C16121",
  "customer_name": "Aradhana Soni",
  "snapshot_date": "2026-05-01",
  "customer": {
    "age": 62,
    "tenure_months": 131,
    "customer_segment": "farmer",
    "income_regularity": "seasonal",
    "products_count": 1,
    "has_credit_card": 0,
    "has_loan": 0,
    "days_since_last_transaction": 18,
    "balance_change_30d": -45.0499,
    "transaction_change_30d": -27.7593,
    "card_spend_change_30d": -37.4718,
    "app_login_change_30d": -32.9263,
    "salary_missing_days": null,
    "external_transfer_change_30d": 28.9638,
    "upi_share_of_spend": 0.6222,
    "fd_maturing_in_30d": 0,
    "products_dropped_90d": 2,
    "complaints_30d": 1,
    "unresolved_complaints": 1,
    "failed_transactions_30d": 0,
    "avg_resolution_time_hrs": 55.5874,
    "emi_bounce_30d": 0,
    "branch_code": "BR-134",
    "card_colour": "gold"
  },
  "actual_current_month_churn": 1
}
```

#### Model 1 Output

```json
{
  "churn_probability": 20.69,
  "raw_churn_probability": 25.74,
  "risk_score": 70.26,
  "churn_prediction": "Yes",
  "risk_level": "High",
  "top_risk_factors": [
    {
      "factor": "balance_change_30d",
      "value": -45.0499
    },
    {
      "factor": "days_since_last_transaction",
      "value": 18
    },
    {
      "factor": "card_spend_change_30d",
      "value": -37.4718
    },
    {
      "factor": "avg_resolution_time_hrs",
      "value": 55.5874
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
  "customer_id": "C16121",
  "customer_name": "Aradhana Soni",
  "prediction_date": "2026-04-01",
  "target_month": "2026-05-01",
  "profile": {
    "tenure_months": 131,
    "customer_segment": "farmer",
    "income_regularity": "seasonal",
    "products_count": 1,
    "has_credit_card": 0,
    "has_loan": 0
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 3,
      "balance_change_30d": -11.2862,
      "transaction_change_30d": 8.4372,
      "card_spend_change_30d": -11.4197,
      "app_login_change_30d": 8.6257,
      "salary_missing_days": null,
      "external_transfer_change_30d": -21.5046,
      "upi_share_of_spend": 0.5532,
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
      "days_since_last_transaction": 4,
      "balance_change_30d": 21.7431,
      "transaction_change_30d": 14.6797,
      "card_spend_change_30d": 13.6392,
      "app_login_change_30d": -7.8225,
      "salary_missing_days": null,
      "external_transfer_change_30d": -12.4336,
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
      "snapshot_date": "2026-03-01",
      "days_since_last_transaction": 1,
      "balance_change_30d": -12.0974,
      "transaction_change_30d": -20.3396,
      "card_spend_change_30d": 16.9495,
      "app_login_change_30d": -26.1842,
      "salary_missing_days": null,
      "external_transfer_change_30d": 18.4515,
      "upi_share_of_spend": 0.5647,
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
      "balance_change_30d": -24.3239,
      "transaction_change_30d": -48.0504,
      "card_spend_change_30d": -23.0036,
      "app_login_change_30d": -20.901,
      "salary_missing_days": null,
      "external_transfer_change_30d": 40.7871,
      "upi_share_of_spend": 0.6151,
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
  "churn_probability": 19.83,
  "raw_churn_probability": 70.35,
  "probability_mode": "sigmoid",
  "risk_score": 69.31,
  "churn_prediction": "Yes",
  "risk_level": "Medium",
  "top_risk_factors": [
    {
      "factor": "latest_transaction_change_30d",
      "value": -48.0504,
      "message": "Transaction activity has been falling across recent months.",
      "contribution": 0.5003253221511841
    },
    {
      "factor": "days_since_last_transaction_trend_6m",
      "value": 2.1,
      "message": "Customer has gone longer without transacting.",
      "contribution": 0.21772664785385132
    },
    {
      "factor": "latest_balance_change_30d",
      "value": -24.3239,
      "message": "Balance has been falling across recent months.",
      "contribution": 0.20266219973564148
    },
    {
      "factor": "latest_vs_avg_upi_share_of_spend_available_history",
      "value": 0.0407999999999999,
      "message": "This signal increased churn risk.",
      "contribution": 0.1325322836637497
    },
    {
      "factor": "transaction_change_30d_trend_6m",
      "value": -20.44821,
      "message": "Transaction activity has been falling across recent months.",
      "contribution": 0.12839366495609283
    }
  ]
}
```

### 67. Neel Wadhwa (`C16175`)

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

### 68. Nikita Dugar (`C16218`)

#### Model 1 Input

```json
{
  "customer_id": "C16218",
  "customer_name": "Nikita Dugar",
  "snapshot_date": "2026-02-01",
  "customer": {
    "age": 29,
    "tenure_months": 77,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 2,
    "has_credit_card": 1,
    "has_loan": 0,
    "days_since_last_transaction": 12,
    "balance_change_30d": -14.484,
    "transaction_change_30d": -38.4535,
    "card_spend_change_30d": -43.0233,
    "app_login_change_30d": -56.5552,
    "salary_missing_days": 3.0,
    "external_transfer_change_30d": 43.7913,
    "upi_share_of_spend": 0.7793,
    "fd_maturing_in_30d": 0,
    "products_dropped_90d": 1,
    "complaints_30d": 1,
    "unresolved_complaints": 0,
    "failed_transactions_30d": 0,
    "avg_resolution_time_hrs": 23.4442,
    "emi_bounce_30d": 0,
    "branch_code": "BR-134",
    "card_colour": "blue"
  },
  "actual_current_month_churn": 1
}
```

#### Model 1 Output

```json
{
  "churn_probability": 4.11,
  "raw_churn_probability": 5.63,
  "risk_score": 12.33,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "card_spend_change_30d",
      "value": -43.0233
    },
    {
      "factor": "salary_missing_days",
      "value": 3.0
    },
    {
      "factor": "external_transfer_change_30d",
      "value": 43.7913
    },
    {
      "factor": "card_colour",
      "value": "blue"
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
  "customer_id": "C16218",
  "customer_name": "Nikita Dugar",
  "prediction_date": "2026-01-01",
  "target_month": "2026-02-01",
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
      "days_since_last_transaction": 7,
      "balance_change_30d": -10.1467,
      "transaction_change_30d": -11.5521,
      "card_spend_change_30d": -4.7657,
      "app_login_change_30d": 4.0831,
      "salary_missing_days": 4.0,
      "external_transfer_change_30d": 13.7415,
      "upi_share_of_spend": 0.6983,
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
  "churn_probability": 4.3,
  "raw_churn_probability": 38.7,
  "probability_mode": "sigmoid",
  "risk_score": 12.91,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "latest_salary_missing_days",
      "value": 4.0,
      "message": "This signal increased churn risk.",
      "contribution": 0.35023465752601624
    },
    {
      "factor": "avg_card_spend_change_30d_3m",
      "value": -4.7657,
      "message": "Card spending has been falling across recent months.",
      "contribution": 0.03272753581404686
    },
    {
      "factor": "avg_upi_share_of_spend_6m",
      "value": 0.6983,
      "message": "This signal increased churn risk.",
      "contribution": 0.026568034663796425
    },
    {
      "factor": "external_transfer_change_30d_trend_6m",
      "value": 0.0,
      "message": "This signal increased churn risk.",
      "contribution": 0.026006722822785378
    },
    {
      "factor": "latest_upi_share_of_spend",
      "value": 0.6983,
      "message": "This signal increased churn risk.",
      "contribution": 0.019665006548166275
    }
  ]
}
```

### 69. Charvi Kata (`C16223`)

#### Model 1 Input

```json
{
  "customer_id": "C16223",
  "customer_name": "Charvi Kata",
  "snapshot_date": "2026-06-01",
  "customer": {
    "age": 45,
    "tenure_months": 86,
    "customer_segment": "business",
    "income_regularity": "irregular",
    "products_count": 4,
    "has_credit_card": 1,
    "has_loan": 0,
    "days_since_last_transaction": 2,
    "balance_change_30d": 1.3854,
    "transaction_change_30d": -1.4419,
    "card_spend_change_30d": 15.1194,
    "app_login_change_30d": 16.3664,
    "salary_missing_days": null,
    "external_transfer_change_30d": -28.7954,
    "upi_share_of_spend": 0.5359,
    "fd_maturing_in_30d": 1,
    "products_dropped_90d": 0,
    "complaints_30d": 1,
    "unresolved_complaints": 0,
    "failed_transactions_30d": 0,
    "avg_resolution_time_hrs": 18.3626,
    "emi_bounce_30d": 0,
    "branch_code": "BR-104",
    "card_colour": "green"
  },
  "actual_current_month_churn": 0
}
```

#### Model 1 Output

```json
{
  "churn_probability": 1.96,
  "raw_churn_probability": 1.64,
  "risk_score": 5.87,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "fd_maturing_in_30d",
      "value": 1
    },
    {
      "factor": "app_login_change_30d",
      "value": 16.3664
    },
    {
      "factor": "transaction_change_30d",
      "value": -1.4419
    },
    {
      "factor": "card_colour",
      "value": "green"
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
  "customer_id": "C16223",
  "customer_name": "Charvi Kata",
  "prediction_date": "2026-05-01",
  "target_month": "2026-06-01",
  "profile": {
    "tenure_months": 86,
    "customer_segment": "business",
    "income_regularity": "irregular",
    "products_count": 4,
    "has_credit_card": 1,
    "has_loan": 0
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 2,
      "balance_change_30d": -4.8943,
      "transaction_change_30d": -9.6885,
      "card_spend_change_30d": -12.9263,
      "app_login_change_30d": -8.724,
      "salary_missing_days": null,
      "external_transfer_change_30d": -11.0215,
      "upi_share_of_spend": 0.5632,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 1,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 33.1588,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-02-01",
      "days_since_last_transaction": 10,
      "balance_change_30d": 5.5694,
      "transaction_change_30d": -10.4486,
      "card_spend_change_30d": -10.3316,
      "app_login_change_30d": 21.6823,
      "salary_missing_days": null,
      "external_transfer_change_30d": 17.1304,
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
      "snapshot_date": "2026-03-01",
      "days_since_last_transaction": 4,
      "balance_change_30d": -2.3657,
      "transaction_change_30d": 23.6819,
      "card_spend_change_30d": 23.653,
      "app_login_change_30d": 4.7835,
      "salary_missing_days": null,
      "external_transfer_change_30d": 33.2393,
      "upi_share_of_spend": 0.533,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 43.9194,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-04-01",
      "days_since_last_transaction": 4,
      "balance_change_30d": 15.6426,
      "transaction_change_30d": 12.4212,
      "card_spend_change_30d": 24.0123,
      "app_login_change_30d": 20.2381,
      "salary_missing_days": null,
      "external_transfer_change_30d": -48.1615,
      "upi_share_of_spend": 0.5466,
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
      "balance_change_30d": 23.0672,
      "transaction_change_30d": 44.6108,
      "card_spend_change_30d": 25.244,
      "app_login_change_30d": 13.6006,
      "salary_missing_days": null,
      "external_transfer_change_30d": -34.227,
      "upi_share_of_spend": 0.5504,
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
  "churn_probability": 1.68,
  "raw_churn_probability": 20.69,
  "probability_mode": "sigmoid",
  "risk_score": 5.03,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "card_spend_change_30d_trend_6m",
      "value": 11.068450000000002,
      "message": "This signal increased churn risk.",
      "contribution": 0.029302749782800674
    },
    {
      "factor": "latest_upi_share_of_spend",
      "value": 0.5504,
      "message": "This signal increased churn risk.",
      "contribution": 0.023654498159885406
    },
    {
      "factor": "latest_vs_avg_external_transfer_change_30d_available_history",
      "value": -25.61894,
      "message": "This signal increased churn risk.",
      "contribution": 0.021717462688684464
    },
    {
      "factor": "max_avg_resolution_time_hrs_3m",
      "value": 43.9194,
      "message": "This signal increased churn risk.",
      "contribution": 0.018576176837086678
    },
    {
      "factor": "count_balance_drop_3m",
      "value": 0,
      "message": "This signal increased churn risk.",
      "contribution": 0.004429497756063938
    }
  ]
}
```

### 70. Devansh Bath (`C16345`)

#### Model 1 Input

```json
{
  "customer_id": "C16345",
  "customer_name": "Devansh Bath",
  "snapshot_date": "2026-05-01",
  "customer": {
    "age": 41,
    "tenure_months": 115,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 2,
    "has_credit_card": 1,
    "has_loan": 0,
    "days_since_last_transaction": 18,
    "balance_change_30d": -49.2454,
    "transaction_change_30d": -44.4485,
    "card_spend_change_30d": -31.8466,
    "app_login_change_30d": -28.0616,
    "salary_missing_days": 5.0,
    "external_transfer_change_30d": 63.4591,
    "upi_share_of_spend": 0.3427,
    "fd_maturing_in_30d": 0,
    "products_dropped_90d": 0,
    "complaints_30d": 0,
    "unresolved_complaints": 0,
    "failed_transactions_30d": 2,
    "avg_resolution_time_hrs": 0.0,
    "emi_bounce_30d": 0,
    "branch_code": "BR-123",
    "card_colour": "silver"
  },
  "actual_current_month_churn": 1
}
```

#### Model 1 Output

```json
{
  "churn_probability": 36.3,
  "raw_churn_probability": 38.78,
  "risk_score": 76.11,
  "churn_prediction": "Yes",
  "risk_level": "High",
  "top_risk_factors": [
    {
      "factor": "balance_change_30d",
      "value": -49.2454
    },
    {
      "factor": "days_since_last_transaction",
      "value": 18
    },
    {
      "factor": "salary_missing_days",
      "value": 5.0
    },
    {
      "factor": "card_spend_change_30d",
      "value": -31.8466
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
  "customer_id": "C16345",
  "customer_name": "Devansh Bath",
  "prediction_date": "2026-04-01",
  "target_month": "2026-05-01",
  "profile": {
    "tenure_months": 115,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 2,
    "has_credit_card": 1,
    "has_loan": 0
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 11,
      "balance_change_30d": 3.3747,
      "transaction_change_30d": 17.5237,
      "card_spend_change_30d": -17.0649,
      "app_login_change_30d": 35.7148,
      "salary_missing_days": 1.0,
      "external_transfer_change_30d": -19.6174,
      "upi_share_of_spend": 0.315,
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
      "days_since_last_transaction": 13,
      "balance_change_30d": 1.0818,
      "transaction_change_30d": -12.0146,
      "card_spend_change_30d": -39.0569,
      "app_login_change_30d": 5.1994,
      "salary_missing_days": 1.0,
      "external_transfer_change_30d": 40.3142,
      "upi_share_of_spend": 0.226,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 6,
      "unresolved_complaints": 4,
      "failed_transactions_30d": 2,
      "avg_resolution_time_hrs": 73.4587,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-03-01",
      "days_since_last_transaction": 16,
      "balance_change_30d": -23.074,
      "transaction_change_30d": -34.1395,
      "card_spend_change_30d": -20.6652,
      "app_login_change_30d": -19.2145,
      "salary_missing_days": 3.0,
      "external_transfer_change_30d": 74.0366,
      "upi_share_of_spend": 0.3954,
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
      "days_since_last_transaction": 20,
      "balance_change_30d": -21.2711,
      "transaction_change_30d": -18.1223,
      "card_spend_change_30d": -7.014,
      "app_login_change_30d": -10.3226,
      "salary_missing_days": 3.0,
      "external_transfer_change_30d": 71.1199,
      "upi_share_of_spend": 0.4036,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 1,
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
  "churn_probability": 41.01,
  "raw_churn_probability": 89.54,
  "probability_mode": "sigmoid",
  "risk_score": 77.88,
  "churn_prediction": "Yes",
  "risk_level": "High",
  "top_risk_factors": [
    {
      "factor": "latest_days_since_last_transaction",
      "value": 20,
      "message": "Customer has gone longer without transacting.",
      "contribution": 0.5064125657081604
    },
    {
      "factor": "latest_vs_avg_upi_share_of_spend_available_history",
      "value": 0.0686,
      "message": "This signal increased churn risk.",
      "contribution": 0.27253830432891846
    },
    {
      "factor": "max_avg_resolution_time_hrs_3m",
      "value": 73.4587,
      "message": "This signal increased churn risk.",
      "contribution": 0.2481403648853302
    },
    {
      "factor": "latest_salary_missing_days",
      "value": 3.0,
      "message": "This signal increased churn risk.",
      "contribution": 0.23566311597824097
    },
    {
      "factor": "days_since_last_transaction_trend_6m",
      "value": 3.000000000000001,
      "message": "Customer has gone longer without transacting.",
      "contribution": 0.15973055362701416
    }
  ]
}
```

### 71. David Bhasin (`C16363`)

#### Model 1 Input

```json
{
  "customer_id": "C16363",
  "customer_name": "David Bhasin",
  "snapshot_date": "2026-06-01",
  "customer": {
    "age": 34,
    "tenure_months": 159,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 3,
    "has_credit_card": 1,
    "has_loan": 0,
    "days_since_last_transaction": 1,
    "balance_change_30d": -8.0304,
    "transaction_change_30d": -2.0877,
    "card_spend_change_30d": 25.7686,
    "app_login_change_30d": 6.6584,
    "salary_missing_days": 0.0,
    "external_transfer_change_30d": -30.026,
    "upi_share_of_spend": 0.4038,
    "fd_maturing_in_30d": 0,
    "products_dropped_90d": 0,
    "complaints_30d": 0,
    "unresolved_complaints": 0,
    "failed_transactions_30d": 0,
    "avg_resolution_time_hrs": 0.0,
    "emi_bounce_30d": 0,
    "branch_code": "BR-135",
    "card_colour": "gold"
  },
  "actual_current_month_churn": 0
}
```

#### Model 1 Output

```json
{
  "churn_probability": 0.0,
  "raw_churn_probability": 0.88,
  "risk_score": 0.0,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "app_login_change_30d",
      "value": 6.6584
    },
    {
      "factor": "customer_segment",
      "value": "salary"
    },
    {
      "factor": "income_regularity",
      "value": "regular"
    },
    {
      "factor": "has_loan",
      "value": 0
    },
    {
      "factor": "upi_share_of_spend",
      "value": 0.4038
    }
  ]
}
```

#### Model 1 v2 Input

```json
{
  "customer_id": "C16363",
  "customer_name": "David Bhasin",
  "prediction_date": "2026-05-01",
  "target_month": "2026-06-01",
  "profile": {
    "tenure_months": 159,
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
      "balance_change_30d": -0.9669,
      "transaction_change_30d": 9.0093,
      "card_spend_change_30d": -3.495,
      "app_login_change_30d": 26.9039,
      "salary_missing_days": 1.0,
      "external_transfer_change_30d": -7.8509,
      "upi_share_of_spend": 0.4963,
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
      "days_since_last_transaction": 0,
      "balance_change_30d": 18.4728,
      "transaction_change_30d": 17.8999,
      "card_spend_change_30d": 38.2918,
      "app_login_change_30d": 33.2961,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -22.911,
      "upi_share_of_spend": 0.38,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 5.56,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-03-01",
      "days_since_last_transaction": 0,
      "balance_change_30d": 44.2625,
      "transaction_change_30d": 31.7474,
      "card_spend_change_30d": 29.7485,
      "app_login_change_30d": 6.2436,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -25.1837,
      "upi_share_of_spend": 0.327,
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
      "balance_change_30d": 5.6483,
      "transaction_change_30d": 12.474,
      "card_spend_change_30d": 9.9359,
      "app_login_change_30d": 14.3,
      "salary_missing_days": 1.0,
      "external_transfer_change_30d": -13.2903,
      "upi_share_of_spend": 0.4294,
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
      "days_since_last_transaction": 2,
      "balance_change_30d": 0.1996,
      "transaction_change_30d": 9.5622,
      "card_spend_change_30d": 17.6812,
      "app_login_change_30d": 2.2276,
      "salary_missing_days": 1.0,
      "external_transfer_change_30d": -15.0999,
      "upi_share_of_spend": 0.4943,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 3,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 23.98,
      "emi_bounce_30d": 0
    }
  ],
  "actual_next_month_churn": 0
}
```

#### Model 1 v2 Output

```json
{
  "churn_probability": 2.29,
  "raw_churn_probability": 26.58,
  "probability_mode": "sigmoid",
  "risk_score": 6.87,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "latest_vs_avg_upi_share_of_spend_available_history",
      "value": 0.0688999999999999,
      "message": "This signal increased churn risk.",
      "contribution": 0.15811993181705475
    },
    {
      "factor": "avg_transaction_change_30d_6m",
      "value": 16.138560000000002,
      "message": "This signal increased churn risk.",
      "contribution": 0.028921732679009438
    },
    {
      "factor": "transaction_change_30d_trend_6m",
      "value": -0.4320099999999999,
      "message": "Transaction activity has been falling across recent months.",
      "contribution": 0.025660166516900063
    },
    {
      "factor": "avg_transaction_change_30d_3m",
      "value": 17.92786666666667,
      "message": "This signal increased churn risk.",
      "contribution": 0.010127306915819645
    },
    {
      "factor": "sum_complaints_30d_3m",
      "value": 3.0,
      "message": "Customer has recent complaint activity.",
      "contribution": 0.010053676553070545
    }
  ]
}
```

### 72. Benjamin Narayan (`C16421`)

#### Model 1 Input

```json
{
  "customer_id": "C16421",
  "customer_name": "Benjamin Narayan",
  "snapshot_date": "2026-06-01",
  "customer": {
    "age": 30,
    "tenure_months": 66,
    "customer_segment": "business",
    "income_regularity": "irregular",
    "products_count": 3,
    "has_credit_card": 1,
    "has_loan": 1,
    "days_since_last_transaction": 0,
    "balance_change_30d": 53.2678,
    "transaction_change_30d": 40.6251,
    "card_spend_change_30d": 48.3155,
    "app_login_change_30d": 42.5393,
    "salary_missing_days": null,
    "external_transfer_change_30d": -35.453,
    "upi_share_of_spend": 0.1581,
    "fd_maturing_in_30d": 0,
    "products_dropped_90d": 0,
    "complaints_30d": 0,
    "unresolved_complaints": 0,
    "failed_transactions_30d": 1,
    "avg_resolution_time_hrs": 0.0,
    "emi_bounce_30d": 0,
    "branch_code": "BR-130",
    "card_colour": "green"
  },
  "actual_current_month_churn": 0
}
```

#### Model 1 Output

```json
{
  "churn_probability": 1.65,
  "raw_churn_probability": 1.25,
  "risk_score": 4.96,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "app_login_change_30d",
      "value": 42.5393
    },
    {
      "factor": "upi_share_of_spend",
      "value": 0.1581
    },
    {
      "factor": "card_colour",
      "value": "green"
    },
    {
      "factor": "income_regularity",
      "value": "irregular"
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
  "customer_id": "C16421",
  "customer_name": "Benjamin Narayan",
  "prediction_date": "2026-05-01",
  "target_month": "2026-06-01",
  "profile": {
    "tenure_months": 66,
    "customer_segment": "business",
    "income_regularity": "irregular",
    "products_count": 3,
    "has_credit_card": 1,
    "has_loan": 1
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 4,
      "balance_change_30d": 26.8409,
      "transaction_change_30d": 2.297,
      "card_spend_change_30d": -6.9597,
      "app_login_change_30d": 9.3472,
      "salary_missing_days": null,
      "external_transfer_change_30d": 18.5133,
      "upi_share_of_spend": 0.2229,
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
      "days_since_last_transaction": 4,
      "balance_change_30d": 8.2614,
      "transaction_change_30d": 18.8563,
      "card_spend_change_30d": 60.5657,
      "app_login_change_30d": 3.2746,
      "salary_missing_days": null,
      "external_transfer_change_30d": 20.5797,
      "upi_share_of_spend": 0.1986,
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
      "days_since_last_transaction": 1,
      "balance_change_30d": 23.6385,
      "transaction_change_30d": 25.8937,
      "card_spend_change_30d": 36.4776,
      "app_login_change_30d": 11.6314,
      "salary_missing_days": null,
      "external_transfer_change_30d": -3.6926,
      "upi_share_of_spend": 0.224,
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
      "balance_change_30d": 22.9684,
      "transaction_change_30d": 11.888,
      "card_spend_change_30d": 14.2627,
      "app_login_change_30d": 27.3559,
      "salary_missing_days": null,
      "external_transfer_change_30d": -23.8192,
      "upi_share_of_spend": 0.279,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 2.256,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-05-01",
      "days_since_last_transaction": 0,
      "balance_change_30d": 59.9423,
      "transaction_change_30d": 19.0138,
      "card_spend_change_30d": 53.0118,
      "app_login_change_30d": 13.6692,
      "salary_missing_days": null,
      "external_transfer_change_30d": -40.9135,
      "upi_share_of_spend": 0.2131,
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
  "churn_probability": 2.13,
  "raw_churn_probability": 25.19,
  "probability_mode": "sigmoid",
  "risk_score": 6.38,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "avg_balance_change_30d_6m",
      "value": 28.3303,
      "message": "This signal increased churn risk.",
      "contribution": 0.1372753530740738
    },
    {
      "factor": "avg_balance_change_30d_available_history",
      "value": 28.3303,
      "message": "This signal increased churn risk.",
      "contribution": 0.04471127316355705
    },
    {
      "factor": "latest_vs_avg_external_transfer_change_30d_available_history",
      "value": -35.04704,
      "message": "This signal increased churn risk.",
      "contribution": 0.039982330054044724
    },
    {
      "factor": "avg_balance_change_30d_3m",
      "value": 35.5164,
      "message": "This signal increased churn risk.",
      "contribution": 0.0385977104306221
    },
    {
      "factor": "latest_external_transfer_change_30d",
      "value": -40.9135,
      "message": "This signal increased churn risk.",
      "contribution": 0.03430734947323799
    }
  ]
}
```

### 73. Diya Chandra (`C16671`)

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

### 74. Elijah Mitra (`C16902`)

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

### 75. Unnati Date (`C17033`)

#### Model 1 Input

```json
{
  "customer_id": "C17033",
  "customer_name": "Unnati Date",
  "snapshot_date": "2026-03-01",
  "customer": {
    "age": 25,
    "tenure_months": 74,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 2,
    "has_credit_card": 1,
    "has_loan": 0,
    "days_since_last_transaction": 17,
    "balance_change_30d": -44.0002,
    "transaction_change_30d": -4.3932,
    "card_spend_change_30d": -40.3444,
    "app_login_change_30d": -34.3758,
    "salary_missing_days": 2.0,
    "external_transfer_change_30d": 33.7608,
    "upi_share_of_spend": 0.4383,
    "fd_maturing_in_30d": 1,
    "products_dropped_90d": 0,
    "complaints_30d": 2,
    "unresolved_complaints": 1,
    "failed_transactions_30d": 0,
    "avg_resolution_time_hrs": 53.0411,
    "emi_bounce_30d": 0,
    "branch_code": "BR-123",
    "card_colour": "green"
  },
  "actual_current_month_churn": 1
}
```

#### Model 1 Output

```json
{
  "churn_probability": 53.49,
  "raw_churn_probability": 61.13,
  "risk_score": 82.56,
  "churn_prediction": "Yes",
  "risk_level": "High",
  "top_risk_factors": [
    {
      "factor": "balance_change_30d",
      "value": -44.0002
    },
    {
      "factor": "fd_maturing_in_30d",
      "value": 1
    },
    {
      "factor": "card_spend_change_30d",
      "value": -40.3444
    },
    {
      "factor": "days_since_last_transaction",
      "value": 17
    },
    {
      "factor": "complaints_30d",
      "value": 2
    }
  ]
}
```

#### Model 1 v2 Input

```json
{
  "customer_id": "C17033",
  "customer_name": "Unnati Date",
  "prediction_date": "2026-02-01",
  "target_month": "2026-03-01",
  "profile": {
    "tenure_months": 74,
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
      "balance_change_30d": 6.2886,
      "transaction_change_30d": 8.9346,
      "card_spend_change_30d": -11.4061,
      "app_login_change_30d": -2.1553,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -7.2668,
      "upi_share_of_spend": 0.3186,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 4,
      "unresolved_complaints": 3,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 79.4238,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-02-01",
      "days_since_last_transaction": 14,
      "balance_change_30d": 11.0663,
      "transaction_change_30d": 12.1568,
      "card_spend_change_30d": -4.567,
      "app_login_change_30d": -28.2535,
      "salary_missing_days": 2.0,
      "external_transfer_change_30d": -3.3556,
      "upi_share_of_spend": 0.3983,
      "fd_maturing_in_30d": 1,
      "products_dropped_90d": 0,
      "complaints_30d": 2,
      "unresolved_complaints": 1,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 29.0488,
      "emi_bounce_30d": 0
    }
  ],
  "actual_next_month_churn": 1
}
```

#### Model 1 v2 Output

```json
{
  "churn_probability": 12.47,
  "raw_churn_probability": 60.11,
  "probability_mode": "sigmoid",
  "risk_score": 39.88,
  "churn_prediction": "Yes",
  "risk_level": "Medium",
  "top_risk_factors": [
    {
      "factor": "max_avg_resolution_time_hrs_3m",
      "value": 79.4238,
      "message": "This signal increased churn risk.",
      "contribution": 0.2968759536743164
    },
    {
      "factor": "latest_days_since_last_transaction",
      "value": 14,
      "message": "Customer has gone longer without transacting.",
      "contribution": 0.23402659595012665
    },
    {
      "factor": "latest_avg_resolution_time_hrs",
      "value": 29.0488,
      "message": "This signal increased churn risk.",
      "contribution": 0.108514703810215
    },
    {
      "factor": "latest_fd_maturing_in_30d",
      "value": 1,
      "message": "Customer has a fixed deposit maturing soon.",
      "contribution": 0.09972787648439407
    },
    {
      "factor": "sum_fd_maturing_in_30d_3m",
      "value": 1.0,
      "message": "Customer has a fixed deposit maturing soon.",
      "contribution": 0.09380017966032028
    }
  ]
}
```

### 76. Jai Apte (`C17372`)

#### Model 1 Input

```json
{
  "customer_id": "C17372",
  "customer_name": "Jai Apte",
  "snapshot_date": "2026-06-01",
  "customer": {
    "age": 33,
    "tenure_months": 12,
    "customer_segment": "vendor",
    "income_regularity": "irregular",
    "products_count": 3,
    "has_credit_card": 1,
    "has_loan": 1,
    "days_since_last_transaction": 2,
    "balance_change_30d": 14.8583,
    "transaction_change_30d": 29.0158,
    "card_spend_change_30d": 1.1383,
    "app_login_change_30d": 33.5581,
    "salary_missing_days": null,
    "external_transfer_change_30d": 0.1355,
    "upi_share_of_spend": 0.3432,
    "fd_maturing_in_30d": 0,
    "products_dropped_90d": 0,
    "complaints_30d": 0,
    "unresolved_complaints": 0,
    "failed_transactions_30d": 2,
    "avg_resolution_time_hrs": 0.0,
    "emi_bounce_30d": 0,
    "branch_code": "BR-117",
    "card_colour": "blue"
  },
  "actual_current_month_churn": 0
}
```

#### Model 1 Output

```json
{
  "churn_probability": 1.96,
  "raw_churn_probability": 2.34,
  "risk_score": 5.87,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "tenure_months",
      "value": 12
    },
    {
      "factor": "failed_transactions_30d",
      "value": 2
    },
    {
      "factor": "app_login_change_30d",
      "value": 33.5581
    },
    {
      "factor": "card_colour",
      "value": "blue"
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
  "customer_id": "C17372",
  "customer_name": "Jai Apte",
  "prediction_date": "2026-05-01",
  "target_month": "2026-06-01",
  "profile": {
    "tenure_months": 12,
    "customer_segment": "vendor",
    "income_regularity": "irregular",
    "products_count": 3,
    "has_credit_card": 1,
    "has_loan": 1
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 1,
      "balance_change_30d": 36.4493,
      "transaction_change_30d": 22.2324,
      "card_spend_change_30d": 2.5779,
      "app_login_change_30d": 31.4805,
      "salary_missing_days": null,
      "external_transfer_change_30d": -25.8982,
      "upi_share_of_spend": 0.3567,
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
      "days_since_last_transaction": 1,
      "balance_change_30d": 38.1769,
      "transaction_change_30d": 16.3936,
      "card_spend_change_30d": -1.6728,
      "app_login_change_30d": 10.44,
      "salary_missing_days": null,
      "external_transfer_change_30d": -16.7599,
      "upi_share_of_spend": 0.3354,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 24.0086,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-03-01",
      "days_since_last_transaction": 0,
      "balance_change_30d": 17.3321,
      "transaction_change_30d": 7.9112,
      "card_spend_change_30d": 1.0266,
      "app_login_change_30d": 10.2991,
      "salary_missing_days": null,
      "external_transfer_change_30d": 30.7733,
      "upi_share_of_spend": 0.3119,
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
      "days_since_last_transaction": 6,
      "balance_change_30d": 17.7127,
      "transaction_change_30d": -5.4948,
      "card_spend_change_30d": 7.7213,
      "app_login_change_30d": 28.5223,
      "salary_missing_days": null,
      "external_transfer_change_30d": -27.7085,
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
      "snapshot_date": "2026-05-01",
      "days_since_last_transaction": 7,
      "balance_change_30d": 9.836,
      "transaction_change_30d": -16.9041,
      "card_spend_change_30d": -10.0176,
      "app_login_change_30d": 5.1919,
      "salary_missing_days": null,
      "external_transfer_change_30d": 5.9423,
      "upi_share_of_spend": 0.3816,
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
  "churn_probability": 5.6,
  "raw_churn_probability": 43.82,
  "probability_mode": "sigmoid",
  "risk_score": 16.79,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "latest_transaction_change_30d",
      "value": -16.9041,
      "message": "Transaction activity has been falling across recent months.",
      "contribution": 0.2035433053970337
    },
    {
      "factor": "days_since_last_transaction_trend_6m",
      "value": 1.7000000000000002,
      "message": "Customer has gone longer without transacting.",
      "contribution": 0.13720577955245972
    },
    {
      "factor": "transaction_change_30d_trend_6m",
      "value": -10.016140000000004,
      "message": "Transaction activity has been falling across recent months.",
      "contribution": 0.06145353987812996
    },
    {
      "factor": "external_transfer_change_30d_trend_6m",
      "value": 5.273240000000001,
      "message": "External transfers have increased.",
      "contribution": 0.050637319684028625
    },
    {
      "factor": "balance_change_30d_trend_6m",
      "value": -7.3690800000000065,
      "message": "Balance has been falling across recent months.",
      "contribution": 0.0461476594209671
    }
  ]
}
```

### 77. Charles Khanna (`C17462`)

#### Model 1 Input

```json
{
  "customer_id": "C17462",
  "customer_name": "Charles Khanna",
  "snapshot_date": "2026-06-01",
  "customer": {
    "age": 37,
    "tenure_months": 1,
    "customer_segment": "vendor",
    "income_regularity": "irregular",
    "products_count": 1,
    "has_credit_card": 0,
    "has_loan": 0,
    "days_since_last_transaction": 2,
    "balance_change_30d": 11.7375,
    "transaction_change_30d": 25.9362,
    "card_spend_change_30d": 14.6378,
    "app_login_change_30d": 5.439,
    "salary_missing_days": null,
    "external_transfer_change_30d": -28.6276,
    "upi_share_of_spend": 0.6378,
    "fd_maturing_in_30d": 0,
    "products_dropped_90d": 0,
    "complaints_30d": 1,
    "unresolved_complaints": 0,
    "failed_transactions_30d": 2,
    "avg_resolution_time_hrs": 13.162,
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
  "churn_probability": 1.96,
  "raw_churn_probability": 2.5,
  "risk_score": 5.87,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "tenure_months",
      "value": 1
    },
    {
      "factor": "failed_transactions_30d",
      "value": 2
    },
    {
      "factor": "products_count",
      "value": 1
    },
    {
      "factor": "customer_segment",
      "value": "vendor"
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
  "customer_id": "C17462",
  "customer_name": "Charles Khanna",
  "prediction_date": "2026-05-01",
  "target_month": "2026-06-01",
  "profile": {
    "tenure_months": 1,
    "customer_segment": "vendor",
    "income_regularity": "irregular",
    "products_count": 1,
    "has_credit_card": 0,
    "has_loan": 0
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 0,
      "balance_change_30d": -6.4047,
      "transaction_change_30d": 17.0513,
      "card_spend_change_30d": 8.6805,
      "app_login_change_30d": 4.6117,
      "salary_missing_days": null,
      "external_transfer_change_30d": -10.6242,
      "upi_share_of_spend": 0.539,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 15.3742,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-02-01",
      "days_since_last_transaction": 1,
      "balance_change_30d": 3.4261,
      "transaction_change_30d": -4.85,
      "card_spend_change_30d": -4.7579,
      "app_login_change_30d": -14.7873,
      "salary_missing_days": null,
      "external_transfer_change_30d": 21.1626,
      "upi_share_of_spend": 0.6394,
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
      "balance_change_30d": 29.0519,
      "transaction_change_30d": -13.7256,
      "card_spend_change_30d": -1.3909,
      "app_login_change_30d": 18.2741,
      "salary_missing_days": null,
      "external_transfer_change_30d": -35.2147,
      "upi_share_of_spend": 0.5981,
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
      "balance_change_30d": 29.5507,
      "transaction_change_30d": -1.7664,
      "card_spend_change_30d": 28.9021,
      "app_login_change_30d": 17.0369,
      "salary_missing_days": null,
      "external_transfer_change_30d": -34.3673,
      "upi_share_of_spend": 0.6097,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 3,
      "avg_resolution_time_hrs": 23.9154,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-05-01",
      "days_since_last_transaction": 2,
      "balance_change_30d": -7.608,
      "transaction_change_30d": 5.3494,
      "card_spend_change_30d": 27.9083,
      "app_login_change_30d": -3.4378,
      "salary_missing_days": null,
      "external_transfer_change_30d": 41.8846,
      "upi_share_of_spend": 0.711,
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
  "churn_probability": 3.58,
  "raw_churn_probability": 35.14,
  "probability_mode": "sigmoid",
  "risk_score": 10.74,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "latest_vs_avg_upi_share_of_spend_available_history",
      "value": 0.0915599999999999,
      "message": "This signal increased churn risk.",
      "contribution": 0.21277906000614166
    },
    {
      "factor": "external_transfer_change_30d_trend_6m",
      "value": 4.948770000000001,
      "message": "External transfers have increased.",
      "contribution": 0.03671436011791229
    },
    {
      "factor": "transaction_change_30d_trend_6m",
      "value": -2.032020000000001,
      "message": "Transaction activity has been falling across recent months.",
      "contribution": 0.027896398678421974
    },
    {
      "factor": "latest_upi_share_of_spend",
      "value": 0.711,
      "message": "This signal increased churn risk.",
      "contribution": 0.02694968320429325
    },
    {
      "factor": "app_login_change_30d_trend_6m",
      "value": 1.57252,
      "message": "This signal increased churn risk.",
      "contribution": 0.0204249769449234
    }
  ]
}
```

### 78. Chaman Kalita (`C17484`)

#### Model 1 Input

```json
{
  "customer_id": "C17484",
  "customer_name": "Chaman Kalita",
  "snapshot_date": "2026-06-01",
  "customer": {
    "age": 80,
    "tenure_months": 80,
    "customer_segment": "pension",
    "income_regularity": "regular",
    "products_count": 2,
    "has_credit_card": 0,
    "has_loan": 0,
    "days_since_last_transaction": 7,
    "balance_change_30d": 2.3104,
    "transaction_change_30d": 3.3775,
    "card_spend_change_30d": -7.735,
    "app_login_change_30d": 11.9638,
    "salary_missing_days": 1.0,
    "external_transfer_change_30d": -13.57,
    "upi_share_of_spend": 0.505,
    "fd_maturing_in_30d": 0,
    "products_dropped_90d": 0,
    "complaints_30d": 0,
    "unresolved_complaints": 0,
    "failed_transactions_30d": 0,
    "avg_resolution_time_hrs": 0.0,
    "emi_bounce_30d": 0,
    "branch_code": "BR-114",
    "card_colour": "silver"
  },
  "actual_current_month_churn": 0
}
```

#### Model 1 Output

```json
{
  "churn_probability": 1.96,
  "raw_churn_probability": 1.66,
  "risk_score": 5.87,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "age",
      "value": 80
    },
    {
      "factor": "branch_code",
      "value": "BR-114"
    },
    {
      "factor": "customer_segment",
      "value": "pension"
    },
    {
      "factor": "app_login_change_30d",
      "value": 11.9638
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
  "customer_id": "C17484",
  "customer_name": "Chaman Kalita",
  "prediction_date": "2026-05-01",
  "target_month": "2026-06-01",
  "profile": {
    "tenure_months": 80,
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
      "balance_change_30d": -11.9819,
      "transaction_change_30d": 5.7484,
      "card_spend_change_30d": 24.6023,
      "app_login_change_30d": 46.805,
      "salary_missing_days": 1.0,
      "external_transfer_change_30d": 18.7861,
      "upi_share_of_spend": 0.591,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 2,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 32.5404,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-02-01",
      "days_since_last_transaction": 2,
      "balance_change_30d": 9.3678,
      "transaction_change_30d": 29.1576,
      "card_spend_change_30d": 15.4774,
      "app_login_change_30d": 23.078,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -11.7228,
      "upi_share_of_spend": 0.5341,
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
      "balance_change_30d": 33.511,
      "transaction_change_30d": 24.3238,
      "card_spend_change_30d": 42.6829,
      "app_login_change_30d": 50.7267,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -27.3262,
      "upi_share_of_spend": 0.4668,
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
      "balance_change_30d": 21.9041,
      "transaction_change_30d": 19.6354,
      "card_spend_change_30d": 44.1563,
      "app_login_change_30d": 20.1615,
      "salary_missing_days": 1.0,
      "external_transfer_change_30d": 43.153,
      "upi_share_of_spend": 0.5082,
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
      "balance_change_30d": 18.1826,
      "transaction_change_30d": 14.2129,
      "card_spend_change_30d": 3.001,
      "app_login_change_30d": -4.6418,
      "salary_missing_days": 2.0,
      "external_transfer_change_30d": 26.8166,
      "upi_share_of_spend": 0.4579,
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
  "churn_probability": 1.62,
  "raw_churn_probability": 20.06,
  "probability_mode": "sigmoid",
  "risk_score": 4.87,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "external_transfer_change_30d_trend_6m",
      "value": 7.093679999999999,
      "message": "External transfers have increased.",
      "contribution": 0.049074672162532806
    },
    {
      "factor": "latest_salary_missing_days",
      "value": 2.0,
      "message": "This signal increased churn risk.",
      "contribution": 0.029598083347082138
    },
    {
      "factor": "avg_transaction_change_30d_6m",
      "value": 18.61562,
      "message": "This signal increased churn risk.",
      "contribution": 0.02238905057311058
    },
    {
      "factor": "avg_transaction_change_30d_3m",
      "value": 19.3907,
      "message": "This signal increased churn risk.",
      "contribution": 0.018913673236966133
    },
    {
      "factor": "avg_balance_change_30d_3m",
      "value": 24.532566666666668,
      "message": "This signal increased churn risk.",
      "contribution": 0.0171146672219038
    }
  ]
}
```

### 79. Amara Parikh (`C17639`)

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

### 80. Hemangini Nazareth (`C17880`)

#### Model 1 Input

```json
{
  "customer_id": "C17880",
  "customer_name": "Hemangini Nazareth",
  "snapshot_date": "2026-06-01",
  "customer": {
    "age": 40,
    "tenure_months": 13,
    "customer_segment": "vendor",
    "income_regularity": "irregular",
    "products_count": 1,
    "has_credit_card": 0,
    "has_loan": 0,
    "days_since_last_transaction": 0,
    "balance_change_30d": 34.3573,
    "transaction_change_30d": 15.6209,
    "card_spend_change_30d": 25.3396,
    "app_login_change_30d": 37.447,
    "salary_missing_days": null,
    "external_transfer_change_30d": 18.4022,
    "upi_share_of_spend": 0.0103,
    "fd_maturing_in_30d": 0,
    "products_dropped_90d": 1,
    "complaints_30d": 0,
    "unresolved_complaints": 0,
    "failed_transactions_30d": 2,
    "avg_resolution_time_hrs": 0.0,
    "emi_bounce_30d": 0,
    "branch_code": "BR-132",
    "card_colour": "silver"
  },
  "actual_current_month_churn": 0
}
```

#### Model 1 Output

```json
{
  "churn_probability": 1.96,
  "raw_churn_probability": 1.91,
  "risk_score": 5.87,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "tenure_months",
      "value": 13
    },
    {
      "factor": "failed_transactions_30d",
      "value": 2
    },
    {
      "factor": "app_login_change_30d",
      "value": 37.447
    },
    {
      "factor": "upi_share_of_spend",
      "value": 0.0103
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
  "customer_id": "C17880",
  "customer_name": "Hemangini Nazareth",
  "prediction_date": "2026-05-01",
  "target_month": "2026-06-01",
  "profile": {
    "tenure_months": 13,
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
      "balance_change_30d": 8.668,
      "transaction_change_30d": -8.0018,
      "card_spend_change_30d": -6.0415,
      "app_login_change_30d": 5.2293,
      "salary_missing_days": null,
      "external_transfer_change_30d": 16.6038,
      "upi_share_of_spend": 0.1636,
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
      "days_since_last_transaction": 2,
      "balance_change_30d": 13.0552,
      "transaction_change_30d": 2.0113,
      "card_spend_change_30d": 16.6,
      "app_login_change_30d": -10.287,
      "salary_missing_days": null,
      "external_transfer_change_30d": 8.0233,
      "upi_share_of_spend": 0.1256,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 1,
      "failed_transactions_30d": 2,
      "avg_resolution_time_hrs": 34.2074,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-03-01",
      "days_since_last_transaction": 0,
      "balance_change_30d": 6.4893,
      "transaction_change_30d": -0.781,
      "card_spend_change_30d": 6.0482,
      "app_login_change_30d": 20.6774,
      "salary_missing_days": null,
      "external_transfer_change_30d": 20.0937,
      "upi_share_of_spend": 0.0759,
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
      "balance_change_30d": 20.3496,
      "transaction_change_30d": 29.6954,
      "card_spend_change_30d": 11.7634,
      "app_login_change_30d": 8.7006,
      "salary_missing_days": null,
      "external_transfer_change_30d": -58.7669,
      "upi_share_of_spend": 0.0102,
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
      "balance_change_30d": 21.8956,
      "transaction_change_30d": 20.3563,
      "card_spend_change_30d": 18.9128,
      "app_login_change_30d": 15.171,
      "salary_missing_days": null,
      "external_transfer_change_30d": -23.7631,
      "upi_share_of_spend": 0.0,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 1,
      "failed_transactions_30d": 4,
      "avg_resolution_time_hrs": 23.3464,
      "emi_bounce_30d": 0
    }
  ],
  "actual_next_month_churn": 0
}
```

#### Model 1 v2 Output

```json
{
  "churn_probability": 2.73,
  "raw_churn_probability": 29.96,
  "probability_mode": "sigmoid",
  "risk_score": 8.2,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "latest_failed_transactions_30d",
      "value": 4,
      "message": "Customer has recent failed transactions.",
      "contribution": 0.15143318474292755
    },
    {
      "factor": "sum_failed_transactions_30d_3m",
      "value": 6.0,
      "message": "Customer has recent failed transactions.",
      "contribution": 0.14531917870044708
    },
    {
      "factor": "sum_failed_transactions_30d_6m",
      "value": 9.0,
      "message": "Customer has recent failed transactions.",
      "contribution": 0.1287573128938675
    },
    {
      "factor": "latest_upi_share_of_spend",
      "value": 0.0,
      "message": "This signal increased churn risk.",
      "contribution": 0.0910203754901886
    },
    {
      "factor": "latest_salary_missing_days",
      "value": null,
      "message": "This signal increased churn risk.",
      "contribution": 0.02836022898554802
    }
  ]
}
```

### 81. Nikita Ganguly (`C17907`)

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

### 82. Sneha Mahajan (`C17950`)

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

### 83. Xiti Bath (`C17993`)

#### Model 1 Input

```json
{
  "customer_id": "C17993",
  "customer_name": "Xiti Bath",
  "snapshot_date": "2026-06-01",
  "customer": {
    "age": 35,
    "tenure_months": 81,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 1,
    "has_credit_card": 0,
    "has_loan": 0,
    "days_since_last_transaction": 22,
    "balance_change_30d": -37.7409,
    "transaction_change_30d": -23.1055,
    "card_spend_change_30d": -50.6185,
    "app_login_change_30d": -53.4192,
    "salary_missing_days": 8.0,
    "external_transfer_change_30d": 97.4584,
    "upi_share_of_spend": 0.656,
    "fd_maturing_in_30d": 0,
    "products_dropped_90d": 1,
    "complaints_30d": 0,
    "unresolved_complaints": 0,
    "failed_transactions_30d": 2,
    "avg_resolution_time_hrs": 0.0,
    "emi_bounce_30d": 0,
    "branch_code": "BR-113",
    "card_colour": "gold"
  },
  "actual_current_month_churn": 0
}
```

#### Model 1 Output

```json
{
  "churn_probability": 41.38,
  "raw_churn_probability": 44.2,
  "risk_score": 78.02,
  "churn_prediction": "Yes",
  "risk_level": "High",
  "top_risk_factors": [
    {
      "factor": "balance_change_30d",
      "value": -37.7409
    },
    {
      "factor": "salary_missing_days",
      "value": 8.0
    },
    {
      "factor": "days_since_last_transaction",
      "value": 22
    },
    {
      "factor": "card_spend_change_30d",
      "value": -50.6185
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
  "customer_id": "C17993",
  "customer_name": "Xiti Bath",
  "prediction_date": "2026-05-01",
  "target_month": "2026-06-01",
  "profile": {
    "tenure_months": 81,
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
      "balance_change_30d": -2.5382,
      "transaction_change_30d": 9.337,
      "card_spend_change_30d": -1.5598,
      "app_login_change_30d": -24.9866,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": 9.0543,
      "upi_share_of_spend": 0.5171,
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
      "balance_change_30d": -14.5101,
      "transaction_change_30d": 2.7756,
      "card_spend_change_30d": -9.8731,
      "app_login_change_30d": 0.2103,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": 37.6083,
      "upi_share_of_spend": 0.4248,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 19.2758,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-03-01",
      "days_since_last_transaction": 7,
      "balance_change_30d": 2.7871,
      "transaction_change_30d": 32.3536,
      "card_spend_change_30d": -2.3649,
      "app_login_change_30d": -5.6554,
      "salary_missing_days": 1.0,
      "external_transfer_change_30d": 25.7977,
      "upi_share_of_spend": 0.4347,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 1,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 32.6627,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-04-01",
      "days_since_last_transaction": 13,
      "balance_change_30d": -13.4758,
      "transaction_change_30d": -34.041,
      "card_spend_change_30d": -8.9691,
      "app_login_change_30d": -8.3585,
      "salary_missing_days": 2.0,
      "external_transfer_change_30d": 28.154,
      "upi_share_of_spend": 0.496,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 2,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 25.0321,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-05-01",
      "days_since_last_transaction": 10,
      "balance_change_30d": -46.9603,
      "transaction_change_30d": -34.0477,
      "card_spend_change_30d": -44.0942,
      "app_login_change_30d": -10.3249,
      "salary_missing_days": 5.0,
      "external_transfer_change_30d": 55.7071,
      "upi_share_of_spend": 0.6419,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 2,
      "unresolved_complaints": 1,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 23.2113,
      "emi_bounce_30d": 0
    }
  ],
  "actual_next_month_churn": 0
}
```

#### Model 1 v2 Output

```json
{
  "churn_probability": 24.14,
  "raw_churn_probability": 75.04,
  "probability_mode": "sigmoid",
  "risk_score": 71.55,
  "churn_prediction": "Yes",
  "risk_level": "Medium",
  "top_risk_factors": [
    {
      "factor": "latest_salary_missing_days",
      "value": 5.0,
      "message": "This signal increased churn risk.",
      "contribution": 0.2894395589828491
    },
    {
      "factor": "latest_transaction_change_30d",
      "value": -34.0477,
      "message": "Transaction activity has been falling across recent months.",
      "contribution": 0.23712344467639923
    },
    {
      "factor": "latest_balance_change_30d",
      "value": -46.9603,
      "message": "Balance has been falling across recent months.",
      "contribution": 0.22443479299545288
    },
    {
      "factor": "latest_vs_avg_upi_share_of_spend_available_history",
      "value": 0.139,
      "message": "This signal increased churn risk.",
      "contribution": 0.20907561480998993
    },
    {
      "factor": "latest_card_spend_change_30d",
      "value": -44.0942,
      "message": "Card spending has been falling across recent months.",
      "contribution": 0.15033087134361267
    }
  ]
}
```

### 84. Ethan Bhasin (`C18023`)

#### Model 1 Input

```json
{
  "customer_id": "C18023",
  "customer_name": "Ethan Bhasin",
  "snapshot_date": "2026-06-01",
  "customer": {
    "age": 61,
    "tenure_months": 1,
    "customer_segment": "pension",
    "income_regularity": "regular",
    "products_count": 1,
    "has_credit_card": 0,
    "has_loan": 0,
    "days_since_last_transaction": 8,
    "balance_change_30d": -28.2312,
    "transaction_change_30d": 4.2131,
    "card_spend_change_30d": 28.39,
    "app_login_change_30d": -20.4279,
    "salary_missing_days": 1.0,
    "external_transfer_change_30d": 2.2949,
    "upi_share_of_spend": 0.4322,
    "fd_maturing_in_30d": 0,
    "products_dropped_90d": 0,
    "complaints_30d": 0,
    "unresolved_complaints": 0,
    "failed_transactions_30d": 0,
    "avg_resolution_time_hrs": 0.0,
    "emi_bounce_30d": 0,
    "branch_code": "BR-102",
    "card_colour": "green"
  },
  "actual_current_month_churn": 0
}
```

#### Model 1 Output

```json
{
  "churn_probability": 3.74,
  "raw_churn_probability": 4.27,
  "risk_score": 11.21,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "tenure_months",
      "value": 1
    },
    {
      "factor": "balance_change_30d",
      "value": -28.2312
    },
    {
      "factor": "branch_code",
      "value": "BR-102"
    },
    {
      "factor": "external_transfer_change_30d",
      "value": 2.2949
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
  "customer_id": "C18023",
  "customer_name": "Ethan Bhasin",
  "prediction_date": "2026-05-01",
  "target_month": "2026-06-01",
  "profile": {
    "tenure_months": 1,
    "customer_segment": "pension",
    "income_regularity": "regular",
    "products_count": 1,
    "has_credit_card": 0,
    "has_loan": 0
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 4,
      "balance_change_30d": 3.7836,
      "transaction_change_30d": -14.7301,
      "card_spend_change_30d": -6.5188,
      "app_login_change_30d": -2.9234,
      "salary_missing_days": 2.0,
      "external_transfer_change_30d": -10.0621,
      "upi_share_of_spend": 0.3067,
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
      "balance_change_30d": 1.8509,
      "transaction_change_30d": 2.7927,
      "card_spend_change_30d": -9.2301,
      "app_login_change_30d": 29.5288,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -0.0664,
      "upi_share_of_spend": 0.3987,
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
      "balance_change_30d": -4.3271,
      "transaction_change_30d": 39.2585,
      "card_spend_change_30d": -17.8059,
      "app_login_change_30d": 19.5334,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": 23.8898,
      "upi_share_of_spend": 0.3582,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 1,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 39.8289,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-04-01",
      "days_since_last_transaction": 5,
      "balance_change_30d": 1.8838,
      "transaction_change_30d": 8.4165,
      "card_spend_change_30d": 11.8018,
      "app_login_change_30d": 13.1132,
      "salary_missing_days": 1.0,
      "external_transfer_change_30d": -1.4455,
      "upi_share_of_spend": 0.358,
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
      "balance_change_30d": 44.1675,
      "transaction_change_30d": 14.6169,
      "card_spend_change_30d": 49.6778,
      "app_login_change_30d": 21.6432,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -30.5288,
      "upi_share_of_spend": 0.3461,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 41.5371,
      "emi_bounce_30d": 0
    }
  ],
  "actual_next_month_churn": 0
}
```

#### Model 1 v2 Output

```json
{
  "churn_probability": 2.23,
  "raw_churn_probability": 26.06,
  "probability_mode": "sigmoid",
  "risk_score": 6.68,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "latest_avg_resolution_time_hrs",
      "value": 41.5371,
      "message": "This signal increased churn risk.",
      "contribution": 0.2977200746536255
    },
    {
      "factor": "avg_transaction_change_30d_3m",
      "value": 20.763966666666665,
      "message": "This signal increased churn risk.",
      "contribution": 0.037424035370349884
    },
    {
      "factor": "card_spend_change_30d_trend_6m",
      "value": 13.34251,
      "message": "This signal increased churn risk.",
      "contribution": 0.034588176757097244
    },
    {
      "factor": "latest_card_spend_change_30d",
      "value": 49.6778,
      "message": "This signal increased churn risk.",
      "contribution": 0.022914772853255272
    },
    {
      "factor": "latest_vs_avg_external_transfer_change_30d_available_history",
      "value": -26.8862,
      "message": "This signal increased churn risk.",
      "contribution": 0.02016851119697094
    }
  ]
}
```

### 85. Thomas Kothari (`C18055`)

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

### 86. Warda Kalita (`C18307`)

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

### 87. Arin Pandya (`C18434`)

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

### 88. Mugdha Rajagopal (`C18699`)

#### Model 1 Input

```json
{
  "customer_id": "C18699",
  "customer_name": "Mugdha Rajagopal",
  "snapshot_date": "2026-04-01",
  "customer": {
    "age": 60,
    "tenure_months": 105,
    "customer_segment": "pension",
    "income_regularity": "regular",
    "products_count": 1,
    "has_credit_card": 0,
    "has_loan": 0,
    "days_since_last_transaction": 23,
    "balance_change_30d": -47.494,
    "transaction_change_30d": -40.0565,
    "card_spend_change_30d": -50.1712,
    "app_login_change_30d": -21.734,
    "salary_missing_days": 6.0,
    "external_transfer_change_30d": 79.9438,
    "upi_share_of_spend": 0.6836,
    "fd_maturing_in_30d": 0,
    "products_dropped_90d": 0,
    "complaints_30d": 0,
    "unresolved_complaints": 0,
    "failed_transactions_30d": 3,
    "avg_resolution_time_hrs": 0.0,
    "emi_bounce_30d": 0,
    "branch_code": "BR-108",
    "card_colour": "green"
  },
  "actual_current_month_churn": 1
}
```

#### Model 1 Output

```json
{
  "churn_probability": 70.37,
  "raw_churn_probability": 66.29,
  "risk_score": 88.89,
  "churn_prediction": "Yes",
  "risk_level": "High",
  "top_risk_factors": [
    {
      "factor": "balance_change_30d",
      "value": -47.494
    },
    {
      "factor": "days_since_last_transaction",
      "value": 23
    },
    {
      "factor": "card_spend_change_30d",
      "value": -50.1712
    },
    {
      "factor": "salary_missing_days",
      "value": 6.0
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
  "customer_id": "C18699",
  "customer_name": "Mugdha Rajagopal",
  "prediction_date": "2026-03-01",
  "target_month": "2026-04-01",
  "profile": {
    "tenure_months": 105,
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
      "balance_change_30d": 0.4734,
      "transaction_change_30d": 27.5139,
      "card_spend_change_30d": -4.2764,
      "app_login_change_30d": 33.5641,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -10.807,
      "upi_share_of_spend": 0.4038,
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
      "days_since_last_transaction": 14,
      "balance_change_30d": -11.3496,
      "transaction_change_30d": -23.5205,
      "card_spend_change_30d": -7.6311,
      "app_login_change_30d": 10.2424,
      "salary_missing_days": 3.0,
      "external_transfer_change_30d": 29.7805,
      "upi_share_of_spend": 0.5353,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 2,
      "unresolved_complaints": 1,
      "failed_transactions_30d": 3,
      "avg_resolution_time_hrs": 29.6867,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-03-01",
      "days_since_last_transaction": 18,
      "balance_change_30d": -40.6452,
      "transaction_change_30d": -36.2818,
      "card_spend_change_30d": -55.6391,
      "app_login_change_30d": -18.9845,
      "salary_missing_days": 4.0,
      "external_transfer_change_30d": 49.4598,
      "upi_share_of_spend": 0.596,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 1,
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
  "churn_probability": 42.95,
  "raw_churn_probability": 91.03,
  "probability_mode": "sigmoid",
  "risk_score": 78.61,
  "churn_prediction": "Yes",
  "risk_level": "High",
  "top_risk_factors": [
    {
      "factor": "latest_days_since_last_transaction",
      "value": 18,
      "message": "Customer has gone longer without transacting.",
      "contribution": 0.6629189252853394
    },
    {
      "factor": "latest_transaction_change_30d",
      "value": -36.2818,
      "message": "Transaction activity has been falling across recent months.",
      "contribution": 0.4420900344848633
    },
    {
      "factor": "latest_salary_missing_days",
      "value": 4.0,
      "message": "This signal increased churn risk.",
      "contribution": 0.2928442358970642
    },
    {
      "factor": "latest_vs_avg_upi_share_of_spend_available_history",
      "value": 0.0843,
      "message": "This signal increased churn risk.",
      "contribution": 0.24954111874103546
    },
    {
      "factor": "days_since_last_transaction_trend_6m",
      "value": 5.500000000000001,
      "message": "Customer has gone longer without transacting.",
      "contribution": 0.17531301081180573
    }
  ]
}
```

### 89. Lavanya Andra (`C18807`)

#### Model 1 Input

```json
{
  "customer_id": "C18807",
  "customer_name": "Lavanya Andra",
  "snapshot_date": "2026-06-01",
  "customer": {
    "age": 80,
    "tenure_months": 136,
    "customer_segment": "pension",
    "income_regularity": "regular",
    "products_count": 2,
    "has_credit_card": 0,
    "has_loan": 0,
    "days_since_last_transaction": 6,
    "balance_change_30d": -10.1996,
    "transaction_change_30d": -12.8359,
    "card_spend_change_30d": -7.001,
    "app_login_change_30d": 5.2197,
    "salary_missing_days": 0.0,
    "external_transfer_change_30d": 41.4559,
    "upi_share_of_spend": 0.5557,
    "fd_maturing_in_30d": 0,
    "products_dropped_90d": 0,
    "complaints_30d": 0,
    "unresolved_complaints": 0,
    "failed_transactions_30d": 1,
    "avg_resolution_time_hrs": 0.0,
    "emi_bounce_30d": 0,
    "branch_code": "BR-125",
    "card_colour": "black"
  },
  "actual_current_month_churn": 0
}
```

#### Model 1 Output

```json
{
  "churn_probability": 1.96,
  "raw_churn_probability": 1.64,
  "risk_score": 5.87,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "age",
      "value": 80
    },
    {
      "factor": "branch_code",
      "value": "BR-125"
    },
    {
      "factor": "customer_segment",
      "value": "pension"
    },
    {
      "factor": "external_transfer_change_30d",
      "value": 41.4559
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
  "customer_id": "C18807",
  "customer_name": "Lavanya Andra",
  "prediction_date": "2026-05-01",
  "target_month": "2026-06-01",
  "profile": {
    "tenure_months": 136,
    "customer_segment": "pension",
    "income_regularity": "regular",
    "products_count": 2,
    "has_credit_card": 0,
    "has_loan": 0
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 0,
      "balance_change_30d": 15.1477,
      "transaction_change_30d": 7.7258,
      "card_spend_change_30d": 5.6145,
      "app_login_change_30d": 17.0182,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": 12.5749,
      "upi_share_of_spend": 0.5117,
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
      "balance_change_30d": -23.7253,
      "transaction_change_30d": -13.0694,
      "card_spend_change_30d": -24.2045,
      "app_login_change_30d": -20.6785,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": 40.3136,
      "upi_share_of_spend": 0.54,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 2,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 29.9761,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-03-01",
      "days_since_last_transaction": 4,
      "balance_change_30d": -19.0542,
      "transaction_change_30d": -21.8989,
      "card_spend_change_30d": -41.5941,
      "app_login_change_30d": -8.3317,
      "salary_missing_days": 2.0,
      "external_transfer_change_30d": 2.74,
      "upi_share_of_spend": 0.5984,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 31.0953,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-04-01",
      "days_since_last_transaction": 2,
      "balance_change_30d": -9.1308,
      "transaction_change_30d": -26.9137,
      "card_spend_change_30d": -12.6467,
      "app_login_change_30d": -34.7191,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": 12.1607,
      "upi_share_of_spend": 0.6082,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 1,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 64.4142,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-05-01",
      "days_since_last_transaction": 1,
      "balance_change_30d": 3.2932,
      "transaction_change_30d": 2.0729,
      "card_spend_change_30d": -12.9859,
      "app_login_change_30d": -10.2035,
      "salary_missing_days": 1.0,
      "external_transfer_change_30d": 35.5523,
      "upi_share_of_spend": 0.6808,
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
  "churn_probability": 7.6,
  "raw_churn_probability": 49.9,
  "probability_mode": "sigmoid",
  "risk_score": 22.79,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "max_avg_resolution_time_hrs_3m",
      "value": 64.4142,
      "message": "This signal increased churn risk.",
      "contribution": 0.4513840079307556
    },
    {
      "factor": "latest_vs_avg_upi_share_of_spend_available_history",
      "value": 0.0929799999999999,
      "message": "This signal increased churn risk.",
      "contribution": 0.24129119515419006
    },
    {
      "factor": "avg_card_spend_change_30d_3m",
      "value": -22.4089,
      "message": "Card spending has been falling across recent months.",
      "contribution": 0.05347030609846115
    },
    {
      "factor": "external_transfer_change_30d_trend_6m",
      "value": 1.7801899999999982,
      "message": "External transfers have increased.",
      "contribution": 0.044247809797525406
    },
    {
      "factor": "transaction_change_30d_trend_6m",
      "value": -2.5150100000000006,
      "message": "Transaction activity has been falling across recent months.",
      "contribution": 0.039291150867938995
    }
  ]
}
```

### 90. Ojas Borra (`C18976`)

#### Model 1 Input

```json
{
  "customer_id": "C18976",
  "customer_name": "Ojas Borra",
  "snapshot_date": "2026-03-01",
  "customer": {
    "age": 54,
    "tenure_months": 33,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 4,
    "has_credit_card": 0,
    "has_loan": 0,
    "days_since_last_transaction": 7,
    "balance_change_30d": -11.2912,
    "transaction_change_30d": -32.3099,
    "card_spend_change_30d": -8.1505,
    "app_login_change_30d": -12.0685,
    "salary_missing_days": 5.0,
    "external_transfer_change_30d": 12.1471,
    "upi_share_of_spend": 0.3007,
    "fd_maturing_in_30d": 1,
    "products_dropped_90d": 0,
    "complaints_30d": 1,
    "unresolved_complaints": 0,
    "failed_transactions_30d": 1,
    "avg_resolution_time_hrs": 15.9015,
    "emi_bounce_30d": 0,
    "branch_code": "BR-130",
    "card_colour": "green"
  },
  "actual_current_month_churn": 1
}
```

#### Model 1 Output

```json
{
  "churn_probability": 7.29,
  "raw_churn_probability": 6.07,
  "risk_score": 21.86,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "salary_missing_days",
      "value": 5.0
    },
    {
      "factor": "fd_maturing_in_30d",
      "value": 1
    },
    {
      "factor": "tenure_months",
      "value": 33
    },
    {
      "factor": "external_transfer_change_30d",
      "value": 12.1471
    },
    {
      "factor": "transaction_change_30d",
      "value": -32.3099
    }
  ]
}
```

#### Model 1 v2 Input

```json
{
  "customer_id": "C18976",
  "customer_name": "Ojas Borra",
  "prediction_date": "2026-02-01",
  "target_month": "2026-03-01",
  "profile": {
    "tenure_months": 33,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 4,
    "has_credit_card": 0,
    "has_loan": 0
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 9,
      "balance_change_30d": 10.1791,
      "transaction_change_30d": 10.982,
      "card_spend_change_30d": 37.9596,
      "app_login_change_30d": 17.8625,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -5.3139,
      "upi_share_of_spend": 0.2657,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 16.8015,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-02-01",
      "days_since_last_transaction": 12,
      "balance_change_30d": -4.0843,
      "transaction_change_30d": -13.6685,
      "card_spend_change_30d": 12.2123,
      "app_login_change_30d": 0.179,
      "salary_missing_days": 2.0,
      "external_transfer_change_30d": 29.6508,
      "upi_share_of_spend": 0.3748,
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
  "churn_probability": 7.24,
  "raw_churn_probability": 48.94,
  "probability_mode": "sigmoid",
  "risk_score": 21.72,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "latest_vs_avg_upi_share_of_spend_available_history",
      "value": 0.0545499999999999,
      "message": "This signal increased churn risk.",
      "contribution": 0.18969859182834625
    },
    {
      "factor": "transaction_change_30d_trend_6m",
      "value": -24.6505,
      "message": "Transaction activity has been falling across recent months.",
      "contribution": 0.1465737670660019
    },
    {
      "factor": "days_since_last_transaction_trend_6m",
      "value": 2.9999999999999987,
      "message": "Customer has gone longer without transacting.",
      "contribution": 0.10554484277963638
    },
    {
      "factor": "external_transfer_change_30d_trend_6m",
      "value": 34.96469999999999,
      "message": "External transfers have increased.",
      "contribution": 0.09458829462528229
    },
    {
      "factor": "latest_salary_missing_days",
      "value": 2.0,
      "message": "This signal increased churn risk.",
      "contribution": 0.06788713485002518
    }
  ]
}
```

### 91. Christopher Sarma (`C19096`)

#### Model 1 Input

```json
{
  "customer_id": "C19096",
  "customer_name": "Christopher Sarma",
  "snapshot_date": "2026-03-01",
  "customer": {
    "age": 41,
    "tenure_months": 1,
    "customer_segment": "vendor",
    "income_regularity": "irregular",
    "products_count": 2,
    "has_credit_card": 0,
    "has_loan": 1,
    "days_since_last_transaction": 16,
    "balance_change_30d": -35.7034,
    "transaction_change_30d": -23.5037,
    "card_spend_change_30d": -75.4,
    "app_login_change_30d": -9.2952,
    "salary_missing_days": null,
    "external_transfer_change_30d": 70.2937,
    "upi_share_of_spend": 0.2705,
    "fd_maturing_in_30d": 0,
    "products_dropped_90d": 0,
    "complaints_30d": 0,
    "unresolved_complaints": 0,
    "failed_transactions_30d": 1,
    "avg_resolution_time_hrs": 0.0,
    "emi_bounce_30d": 0,
    "branch_code": "BR-102",
    "card_colour": "silver"
  },
  "actual_current_month_churn": 1
}
```

#### Model 1 Output

```json
{
  "churn_probability": 36.3,
  "raw_churn_probability": 39.77,
  "risk_score": 76.11,
  "churn_prediction": "Yes",
  "risk_level": "High",
  "top_risk_factors": [
    {
      "factor": "balance_change_30d",
      "value": -35.7034
    },
    {
      "factor": "card_spend_change_30d",
      "value": -75.4
    },
    {
      "factor": "tenure_months",
      "value": 1
    },
    {
      "factor": "days_since_last_transaction",
      "value": 16
    },
    {
      "factor": "branch_code",
      "value": "BR-102"
    }
  ]
}
```

#### Model 1 v2 Input

```json
{
  "customer_id": "C19096",
  "customer_name": "Christopher Sarma",
  "prediction_date": "2026-02-01",
  "target_month": "2026-03-01",
  "profile": {
    "tenure_months": 1,
    "customer_segment": "vendor",
    "income_regularity": "irregular",
    "products_count": 2,
    "has_credit_card": 0,
    "has_loan": 1
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 11,
      "balance_change_30d": 22.577,
      "transaction_change_30d": 30.8539,
      "card_spend_change_30d": 10.085,
      "app_login_change_30d": 3.9374,
      "salary_missing_days": null,
      "external_transfer_change_30d": 15.5163,
      "upi_share_of_spend": 0.1937,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 2,
      "avg_resolution_time_hrs": 12.4826,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-02-01",
      "days_since_last_transaction": 15,
      "balance_change_30d": -12.2949,
      "transaction_change_30d": -8.1176,
      "card_spend_change_30d": -19.8748,
      "app_login_change_30d": -4.5752,
      "salary_missing_days": null,
      "external_transfer_change_30d": 62.0398,
      "upi_share_of_spend": 0.2635,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 2,
      "avg_resolution_time_hrs": 5.8089,
      "emi_bounce_30d": 0
    }
  ],
  "actual_next_month_churn": 1
}
```

#### Model 1 v2 Output

```json
{
  "churn_probability": 18.11,
  "raw_churn_probability": 68.27,
  "probability_mode": "sigmoid",
  "risk_score": 62.43,
  "churn_prediction": "Yes",
  "risk_level": "Medium",
  "top_risk_factors": [
    {
      "factor": "latest_days_since_last_transaction",
      "value": 15,
      "message": "Customer has gone longer without transacting.",
      "contribution": 0.4985378682613373
    },
    {
      "factor": "days_since_last_transaction_trend_6m",
      "value": 3.999999999999998,
      "message": "Customer has gone longer without transacting.",
      "contribution": 0.13030992448329926
    },
    {
      "factor": "transaction_change_30d_trend_6m",
      "value": -38.97149999999999,
      "message": "Transaction activity has been falling across recent months.",
      "contribution": 0.10697359591722488
    },
    {
      "factor": "latest_external_transfer_change_30d",
      "value": 62.0398,
      "message": "External transfers have increased.",
      "contribution": 0.0858369842171669
    },
    {
      "factor": "external_transfer_change_30d_trend_6m",
      "value": 46.523499999999984,
      "message": "External transfers have increased.",
      "contribution": 0.07214082032442093
    }
  ]
}
```

### 92. Pooja Bawa (`C19159`)

#### Model 1 Input

```json
{
  "customer_id": "C19159",
  "customer_name": "Pooja Bawa",
  "snapshot_date": "2026-02-01",
  "customer": {
    "age": 51,
    "tenure_months": 163,
    "customer_segment": "business",
    "income_regularity": "irregular",
    "products_count": 4,
    "has_credit_card": 1,
    "has_loan": 1,
    "days_since_last_transaction": 2,
    "balance_change_30d": 10.7333,
    "transaction_change_30d": -8.6068,
    "card_spend_change_30d": 10.9393,
    "app_login_change_30d": -3.3598,
    "salary_missing_days": null,
    "external_transfer_change_30d": 11.7534,
    "upi_share_of_spend": 0.5147,
    "fd_maturing_in_30d": 0,
    "products_dropped_90d": 0,
    "complaints_30d": 1,
    "unresolved_complaints": 1,
    "failed_transactions_30d": 0,
    "avg_resolution_time_hrs": 1.8607,
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
  "churn_probability": 1.96,
  "raw_churn_probability": 1.77,
  "risk_score": 5.87,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "branch_code",
      "value": "BR-109"
    },
    {
      "factor": "unresolved_complaints",
      "value": 1
    },
    {
      "factor": "external_transfer_change_30d",
      "value": 11.7534
    },
    {
      "factor": "card_colour",
      "value": "black"
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
  "customer_id": "C19159",
  "customer_name": "Pooja Bawa",
  "prediction_date": "2026-01-01",
  "target_month": "2026-02-01",
  "profile": {
    "tenure_months": 163,
    "customer_segment": "business",
    "income_regularity": "irregular",
    "products_count": 4,
    "has_credit_card": 1,
    "has_loan": 1
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 6,
      "balance_change_30d": -13.2381,
      "transaction_change_30d": -24.1358,
      "card_spend_change_30d": -38.579,
      "app_login_change_30d": 11.8106,
      "salary_missing_days": null,
      "external_transfer_change_30d": -34.053,
      "upi_share_of_spend": 0.4296,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 23.272,
      "emi_bounce_30d": 0
    }
  ],
  "actual_next_month_churn": 1
}
```

#### Model 1 v2 Output

```json
{
  "churn_probability": 3.35,
  "raw_churn_probability": 33.88,
  "probability_mode": "sigmoid",
  "risk_score": 10.06,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "latest_transaction_change_30d",
      "value": -24.1358,
      "message": "Transaction activity has been falling across recent months.",
      "contribution": 0.18717359006404877
    },
    {
      "factor": "latest_card_spend_change_30d",
      "value": -38.579,
      "message": "Card spending has been falling across recent months.",
      "contribution": 0.12967932224273682
    },
    {
      "factor": "avg_card_spend_change_30d_6m",
      "value": -38.579,
      "message": "Card spending has been falling across recent months.",
      "contribution": 0.059722065925598145
    },
    {
      "factor": "avg_card_spend_change_30d_3m",
      "value": -38.579,
      "message": "Card spending has been falling across recent months.",
      "contribution": 0.04673703759908676
    },
    {
      "factor": "avg_transaction_change_30d_3m",
      "value": -24.1358,
      "message": "Transaction activity has been falling across recent months.",
      "contribution": 0.01798371598124504
    }
  ]
}
```

### 93. Anirudh Shukla (`C19179`)

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

### 94. Ekaraj Gokhale (`C19185`)

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

### 95. Aadhya Pal (`C19311`)

#### Model 1 Input

```json
{
  "customer_id": "C19311",
  "customer_name": "Aadhya Pal",
  "snapshot_date": "2026-06-01",
  "customer": {
    "age": 52,
    "tenure_months": 3,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 3,
    "has_credit_card": 0,
    "has_loan": 1,
    "days_since_last_transaction": 0,
    "balance_change_30d": 40.2391,
    "transaction_change_30d": -11.7343,
    "card_spend_change_30d": 47.1212,
    "app_login_change_30d": 51.499,
    "salary_missing_days": 0.0,
    "external_transfer_change_30d": -18.7712,
    "upi_share_of_spend": 0.328,
    "fd_maturing_in_30d": 0,
    "products_dropped_90d": 0,
    "complaints_30d": 1,
    "unresolved_complaints": 0,
    "failed_transactions_30d": 1,
    "avg_resolution_time_hrs": 18.7373,
    "emi_bounce_30d": 0,
    "branch_code": "BR-130",
    "card_colour": "black"
  },
  "actual_current_month_churn": 0
}
```

#### Model 1 Output

```json
{
  "churn_probability": 1.96,
  "raw_churn_probability": 1.73,
  "risk_score": 5.87,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "tenure_months",
      "value": 3
    },
    {
      "factor": "app_login_change_30d",
      "value": 51.499
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
  "customer_id": "C19311",
  "customer_name": "Aadhya Pal",
  "prediction_date": "2026-05-01",
  "target_month": "2026-06-01",
  "profile": {
    "tenure_months": 3,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 3,
    "has_credit_card": 0,
    "has_loan": 1
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 6,
      "balance_change_30d": 1.0401,
      "transaction_change_30d": -5.8913,
      "card_spend_change_30d": -5.3957,
      "app_login_change_30d": -3.4834,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": 12.2005,
      "upi_share_of_spend": 0.5252,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 1,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 32.2956,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-02-01",
      "days_since_last_transaction": 2,
      "balance_change_30d": 12.3514,
      "transaction_change_30d": -5.1099,
      "card_spend_change_30d": 10.0721,
      "app_login_change_30d": 30.8181,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": 2.708,
      "upi_share_of_spend": 0.4396,
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
      "balance_change_30d": 9.0132,
      "transaction_change_30d": 4.6761,
      "card_spend_change_30d": 61.1748,
      "app_login_change_30d": 13.0162,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -63.1947,
      "upi_share_of_spend": 0.4599,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 2,
      "avg_resolution_time_hrs": 29.1821,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-04-01",
      "days_since_last_transaction": 0,
      "balance_change_30d": 20.9907,
      "transaction_change_30d": 17.4589,
      "card_spend_change_30d": 5.0836,
      "app_login_change_30d": 4.8544,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -7.0784,
      "upi_share_of_spend": 0.4269,
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
      "days_since_last_transaction": 2,
      "balance_change_30d": 21.3861,
      "transaction_change_30d": 2.4818,
      "card_spend_change_30d": 29.1702,
      "app_login_change_30d": 22.3284,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -43.6231,
      "upi_share_of_spend": 0.4002,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 11.5807,
      "emi_bounce_30d": 0
    }
  ],
  "actual_next_month_churn": 0
}
```

#### Model 1 v2 Output

```json
{
  "churn_probability": 1.92,
  "raw_churn_probability": 23.23,
  "probability_mode": "sigmoid",
  "risk_score": 5.75,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "latest_external_transfer_change_30d",
      "value": -43.6231,
      "message": "This signal increased churn risk.",
      "contribution": 0.06360804289579391
    },
    {
      "factor": "sum_fd_maturing_in_30d_3m",
      "value": 1.0,
      "message": "Customer has a fixed deposit maturing soon.",
      "contribution": 0.06131623312830925
    },
    {
      "factor": "max_salary_missing_days_6m",
      "value": 0.0,
      "message": "This signal increased churn risk.",
      "contribution": 0.01941727288067341
    },
    {
      "factor": "card_spend_change_30d_trend_6m",
      "value": 6.41433,
      "message": "This signal increased churn risk.",
      "contribution": 0.017588265240192413
    },
    {
      "factor": "latest_vs_avg_app_login_change_30d_available_history",
      "value": 8.82166,
      "message": "This signal increased churn risk.",
      "contribution": 0.009556610137224197
    }
  ]
}
```

### 96. Irya Ramakrishnan (`C19406`)

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

### 97. Hredhaan Bakshi (`C19434`)

#### Model 1 Input

```json
{
  "customer_id": "C19434",
  "customer_name": "Hredhaan Bakshi",
  "snapshot_date": "2026-05-01",
  "customer": {
    "age": 60,
    "tenure_months": 106,
    "customer_segment": "pension",
    "income_regularity": "regular",
    "products_count": 2,
    "has_credit_card": 0,
    "has_loan": 0,
    "days_since_last_transaction": 17,
    "balance_change_30d": -44.666,
    "transaction_change_30d": -37.5146,
    "card_spend_change_30d": -28.3064,
    "app_login_change_30d": -25.4409,
    "salary_missing_days": 4.0,
    "external_transfer_change_30d": 52.645,
    "upi_share_of_spend": 0.4163,
    "fd_maturing_in_30d": 0,
    "products_dropped_90d": 0,
    "complaints_30d": 2,
    "unresolved_complaints": 0,
    "failed_transactions_30d": 7,
    "avg_resolution_time_hrs": 22.2128,
    "emi_bounce_30d": 0,
    "branch_code": "BR-122",
    "card_colour": "green"
  },
  "actual_current_month_churn": 1
}
```

#### Model 1 Output

```json
{
  "churn_probability": 70.37,
  "raw_churn_probability": 68.32,
  "risk_score": 88.89,
  "churn_prediction": "Yes",
  "risk_level": "High",
  "top_risk_factors": [
    {
      "factor": "balance_change_30d",
      "value": -44.666
    },
    {
      "factor": "failed_transactions_30d",
      "value": 7
    },
    {
      "factor": "days_since_last_transaction",
      "value": 17
    },
    {
      "factor": "salary_missing_days",
      "value": 4.0
    },
    {
      "factor": "card_spend_change_30d",
      "value": -28.3064
    }
  ]
}
```

#### Model 1 v2 Input

```json
{
  "customer_id": "C19434",
  "customer_name": "Hredhaan Bakshi",
  "prediction_date": "2026-04-01",
  "target_month": "2026-05-01",
  "profile": {
    "tenure_months": 106,
    "customer_segment": "pension",
    "income_regularity": "regular",
    "products_count": 2,
    "has_credit_card": 0,
    "has_loan": 0
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 3,
      "balance_change_30d": 8.7038,
      "transaction_change_30d": 30.7118,
      "card_spend_change_30d": 9.3486,
      "app_login_change_30d": 28.5446,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -1.7578,
      "upi_share_of_spend": 0.3011,
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
      "balance_change_30d": -37.0628,
      "transaction_change_30d": -11.6803,
      "card_spend_change_30d": -18.111,
      "app_login_change_30d": -25.1381,
      "salary_missing_days": 3.0,
      "external_transfer_change_30d": 57.6432,
      "upi_share_of_spend": 0.317,
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
      "balance_change_30d": -18.9526,
      "transaction_change_30d": -20.8132,
      "card_spend_change_30d": -17.1229,
      "app_login_change_30d": -16.6043,
      "salary_missing_days": 3.0,
      "external_transfer_change_30d": 51.8739,
      "upi_share_of_spend": 0.4114,
      "fd_maturing_in_30d": 1,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 1.0,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-04-01",
      "days_since_last_transaction": 15,
      "balance_change_30d": -9.3726,
      "transaction_change_30d": 1.4161,
      "card_spend_change_30d": -69.9076,
      "app_login_change_30d": -42.1416,
      "salary_missing_days": 5.0,
      "external_transfer_change_30d": 22.2118,
      "upi_share_of_spend": 0.393,
      "fd_maturing_in_30d": 1,
      "products_dropped_90d": 1,
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
  "churn_probability": 28.04,
  "raw_churn_probability": 78.8,
  "probability_mode": "sigmoid",
  "risk_score": 73.02,
  "churn_prediction": "Yes",
  "risk_level": "High",
  "top_risk_factors": [
    {
      "factor": "latest_days_since_last_transaction",
      "value": 15,
      "message": "Customer has gone longer without transacting.",
      "contribution": 0.4795878827571869
    },
    {
      "factor": "latest_salary_missing_days",
      "value": 5.0,
      "message": "This signal increased churn risk.",
      "contribution": 0.3957844376564026
    },
    {
      "factor": "latest_card_spend_change_30d",
      "value": -69.9076,
      "message": "Card spending has been falling across recent months.",
      "contribution": 0.18139785528182983
    },
    {
      "factor": "days_since_last_transaction_trend_6m",
      "value": 3.5,
      "message": "Customer has gone longer without transacting.",
      "contribution": 0.156596377491951
    },
    {
      "factor": "latest_app_login_change_30d",
      "value": -42.1416,
      "message": "App usage has been falling across recent months.",
      "contribution": 0.09509458392858505
    }
  ]
}
```

### 98. Niharika Oommen (`C19448`)

#### Model 1 Input

```json
{
  "customer_id": "C19448",
  "customer_name": "Niharika Oommen",
  "snapshot_date": "2026-06-01",
  "customer": {
    "age": 45,
    "tenure_months": 42,
    "customer_segment": "vendor",
    "income_regularity": "irregular",
    "products_count": 3,
    "has_credit_card": 0,
    "has_loan": 1,
    "days_since_last_transaction": 35,
    "balance_change_30d": -73.7412,
    "transaction_change_30d": -63.8751,
    "card_spend_change_30d": -77.2658,
    "app_login_change_30d": -50.7696,
    "salary_missing_days": null,
    "external_transfer_change_30d": 112.3171,
    "upi_share_of_spend": 0.4323,
    "fd_maturing_in_30d": 0,
    "products_dropped_90d": 0,
    "complaints_30d": 3,
    "unresolved_complaints": 0,
    "failed_transactions_30d": 5,
    "avg_resolution_time_hrs": 32.9494,
    "emi_bounce_30d": 0,
    "branch_code": "BR-125",
    "card_colour": "silver"
  },
  "actual_current_month_churn": 1
}
```

#### Model 1 Output

```json
{
  "churn_probability": 100.0,
  "raw_churn_probability": 90.68,
  "risk_score": 100.0,
  "churn_prediction": "Yes",
  "risk_level": "High",
  "top_risk_factors": [
    {
      "factor": "balance_change_30d",
      "value": -73.7412
    },
    {
      "factor": "card_spend_change_30d",
      "value": -77.2658
    },
    {
      "factor": "days_since_last_transaction",
      "value": 35
    },
    {
      "factor": "failed_transactions_30d",
      "value": 5
    },
    {
      "factor": "complaints_30d",
      "value": 3
    }
  ]
}
```

#### Model 1 v2 Input

```json
{
  "customer_id": "C19448",
  "customer_name": "Niharika Oommen",
  "prediction_date": "2026-05-01",
  "target_month": "2026-06-01",
  "profile": {
    "tenure_months": 42,
    "customer_segment": "vendor",
    "income_regularity": "irregular",
    "products_count": 3,
    "has_credit_card": 0,
    "has_loan": 1
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 15,
      "balance_change_30d": -0.9487,
      "transaction_change_30d": -12.8381,
      "card_spend_change_30d": -1.9867,
      "app_login_change_30d": 16.2729,
      "salary_missing_days": null,
      "external_transfer_change_30d": 1.9689,
      "upi_share_of_spend": 0.1706,
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
      "days_since_last_transaction": 21,
      "balance_change_30d": 4.0517,
      "transaction_change_30d": -29.9444,
      "card_spend_change_30d": 4.8327,
      "app_login_change_30d": -20.8158,
      "salary_missing_days": null,
      "external_transfer_change_30d": -22.8239,
      "upi_share_of_spend": 0.1634,
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
      "days_since_last_transaction": 25,
      "balance_change_30d": -30.9863,
      "transaction_change_30d": -17.3933,
      "card_spend_change_30d": -8.7187,
      "app_login_change_30d": -4.6155,
      "salary_missing_days": null,
      "external_transfer_change_30d": 60.1984,
      "upi_share_of_spend": 0.3189,
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
      "days_since_last_transaction": 31,
      "balance_change_30d": -50.5143,
      "transaction_change_30d": -59.4472,
      "card_spend_change_30d": -26.4921,
      "app_login_change_30d": -43.1689,
      "salary_missing_days": null,
      "external_transfer_change_30d": 44.2648,
      "upi_share_of_spend": 0.3492,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 36.6892,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-05-01",
      "days_since_last_transaction": 31,
      "balance_change_30d": -71.1168,
      "transaction_change_30d": -48.4555,
      "card_spend_change_30d": -63.3862,
      "app_login_change_30d": -59.7868,
      "salary_missing_days": null,
      "external_transfer_change_30d": 66.8547,
      "upi_share_of_spend": 0.2136,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 4,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 4,
      "avg_resolution_time_hrs": 24.3275,
      "emi_bounce_30d": 0
    }
  ],
  "actual_next_month_churn": 1
}
```

#### Model 1 v2 Output

```json
{
  "churn_probability": 41.56,
  "raw_churn_probability": 89.97,
  "probability_mode": "sigmoid",
  "risk_score": 78.09,
  "churn_prediction": "Yes",
  "risk_level": "High",
  "top_risk_factors": [
    {
      "factor": "latest_days_since_last_transaction",
      "value": 31,
      "message": "Customer has gone longer without transacting.",
      "contribution": 0.6775386929512024
    },
    {
      "factor": "latest_transaction_change_30d",
      "value": -48.4555,
      "message": "Transaction activity has been falling across recent months.",
      "contribution": 0.42317330837249756
    },
    {
      "factor": "latest_balance_change_30d",
      "value": -71.1168,
      "message": "Balance has been falling across recent months.",
      "contribution": 0.20619361102581024
    },
    {
      "factor": "latest_card_spend_change_30d",
      "value": -63.3862,
      "message": "Card spending has been falling across recent months.",
      "contribution": 0.17434142529964447
    },
    {
      "factor": "days_since_last_transaction_trend_6m",
      "value": 4.199999999999998,
      "message": "Customer has gone longer without transacting.",
      "contribution": 0.14759519696235657
    }
  ]
}
```

### 99. Aarini Dar (`C19761`)

#### Model 1 Input

```json
{
  "customer_id": "C19761",
  "customer_name": "Aarini Dar",
  "snapshot_date": "2026-06-01",
  "customer": {
    "age": 60,
    "tenure_months": 1,
    "customer_segment": "business",
    "income_regularity": "irregular",
    "products_count": 4,
    "has_credit_card": 1,
    "has_loan": 1,
    "days_since_last_transaction": 2,
    "balance_change_30d": 19.9724,
    "transaction_change_30d": 19.983,
    "card_spend_change_30d": -26.6868,
    "app_login_change_30d": -10.6279,
    "salary_missing_days": null,
    "external_transfer_change_30d": 5.1055,
    "upi_share_of_spend": 0.376,
    "fd_maturing_in_30d": 0,
    "products_dropped_90d": 1,
    "complaints_30d": 0,
    "unresolved_complaints": 0,
    "failed_transactions_30d": 0,
    "avg_resolution_time_hrs": 0.0,
    "emi_bounce_30d": 0,
    "branch_code": "BR-107",
    "card_colour": "green"
  },
  "actual_current_month_churn": 0
}
```

#### Model 1 Output

```json
{
  "churn_probability": 1.96,
  "raw_churn_probability": 2.64,
  "risk_score": 5.87,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "tenure_months",
      "value": 1
    },
    {
      "factor": "card_spend_change_30d",
      "value": -26.6868
    },
    {
      "factor": "external_transfer_change_30d",
      "value": 5.1055
    },
    {
      "factor": "upi_share_of_spend",
      "value": 0.376
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
  "customer_id": "C19761",
  "customer_name": "Aarini Dar",
  "prediction_date": "2026-05-01",
  "target_month": "2026-06-01",
  "profile": {
    "tenure_months": 1,
    "customer_segment": "business",
    "income_regularity": "irregular",
    "products_count": 4,
    "has_credit_card": 1,
    "has_loan": 1
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 0,
      "balance_change_30d": -6.2336,
      "transaction_change_30d": 3.6216,
      "card_spend_change_30d": 7.7975,
      "app_login_change_30d": 0.3102,
      "salary_missing_days": null,
      "external_transfer_change_30d": -4.51,
      "upi_share_of_spend": 0.3448,
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
      "balance_change_30d": 17.2367,
      "transaction_change_30d": 35.2473,
      "card_spend_change_30d": 24.3266,
      "app_login_change_30d": -21.6694,
      "salary_missing_days": null,
      "external_transfer_change_30d": -8.6453,
      "upi_share_of_spend": 0.3065,
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
      "balance_change_30d": -14.4336,
      "transaction_change_30d": -6.3845,
      "card_spend_change_30d": -19.0807,
      "app_login_change_30d": 11.5011,
      "salary_missing_days": null,
      "external_transfer_change_30d": -19.7332,
      "upi_share_of_spend": 0.2481,
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
      "balance_change_30d": -2.4829,
      "transaction_change_30d": 2.2622,
      "card_spend_change_30d": 14.3882,
      "app_login_change_30d": 10.4217,
      "salary_missing_days": null,
      "external_transfer_change_30d": 0.6631,
      "upi_share_of_spend": 0.2877,
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
      "balance_change_30d": 1.3419,
      "transaction_change_30d": 25.9512,
      "card_spend_change_30d": 5.1931,
      "app_login_change_30d": 21.1561,
      "salary_missing_days": null,
      "external_transfer_change_30d": -66.4893,
      "upi_share_of_spend": 0.1677,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 0,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 2,
      "avg_resolution_time_hrs": 0.0,
      "emi_bounce_30d": 1
    }
  ],
  "actual_next_month_churn": 0
}
```

#### Model 1 v2 Output

```json
{
  "churn_probability": 2.28,
  "raw_churn_probability": 26.54,
  "probability_mode": "sigmoid",
  "risk_score": 6.85,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "latest_vs_avg_external_transfer_change_30d_available_history",
      "value": -46.74636,
      "message": "This signal increased churn risk.",
      "contribution": 0.03698715195059776
    },
    {
      "factor": "avg_card_spend_change_30d_3m",
      "value": 0.1668666666666665,
      "message": "This signal increased churn risk.",
      "contribution": 0.015989938750863075
    },
    {
      "factor": "avg_balance_change_30d_6m",
      "value": -0.9143,
      "message": "Balance has been falling across recent months.",
      "contribution": 0.014620761387050152
    },
    {
      "factor": "avg_upi_share_of_spend_6m",
      "value": 0.27096,
      "message": "This signal increased churn risk.",
      "contribution": 0.014197573065757751
    },
    {
      "factor": "latest_external_transfer_change_30d",
      "value": -66.4893,
      "message": "This signal increased churn risk.",
      "contribution": 0.008164238184690475
    }
  ]
}
```

### 100. Krish Butala (`C19961`)

#### Model 1 Input

```json
{
  "customer_id": "C19961",
  "customer_name": "Krish Butala",
  "snapshot_date": "2026-06-01",
  "customer": {
    "age": 32,
    "tenure_months": 70,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 1,
    "has_credit_card": 0,
    "has_loan": 0,
    "days_since_last_transaction": 11,
    "balance_change_30d": 35.9897,
    "transaction_change_30d": 10.9215,
    "card_spend_change_30d": 14.9228,
    "app_login_change_30d": 21.9684,
    "salary_missing_days": 0.0,
    "external_transfer_change_30d": -38.8791,
    "upi_share_of_spend": 0.337,
    "fd_maturing_in_30d": 0,
    "products_dropped_90d": 0,
    "complaints_30d": 0,
    "unresolved_complaints": 0,
    "failed_transactions_30d": 0,
    "avg_resolution_time_hrs": 0.0,
    "emi_bounce_30d": 0,
    "branch_code": "BR-107",
    "card_colour": "green"
  },
  "actual_current_month_churn": 0
}
```

#### Model 1 Output

```json
{
  "churn_probability": 1.96,
  "raw_churn_probability": 1.53,
  "risk_score": 5.87,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "branch_code",
      "value": "BR-107"
    },
    {
      "factor": "app_login_change_30d",
      "value": 21.9684
    },
    {
      "factor": "upi_share_of_spend",
      "value": 0.337
    },
    {
      "factor": "products_count",
      "value": 1
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
  "customer_id": "C19961",
  "customer_name": "Krish Butala",
  "prediction_date": "2026-05-01",
  "target_month": "2026-06-01",
  "profile": {
    "tenure_months": 70,
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
      "balance_change_30d": -18.9975,
      "transaction_change_30d": -9.809,
      "card_spend_change_30d": -6.6532,
      "app_login_change_30d": -34.0615,
      "salary_missing_days": 4.0,
      "external_transfer_change_30d": 24.0809,
      "upi_share_of_spend": 0.3722,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 1,
      "avg_resolution_time_hrs": 40.8779,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-02-01",
      "days_since_last_transaction": 14,
      "balance_change_30d": 2.5757,
      "transaction_change_30d": -18.1871,
      "card_spend_change_30d": -28.652,
      "app_login_change_30d": 2.2449,
      "salary_missing_days": 3.0,
      "external_transfer_change_30d": 12.1199,
      "upi_share_of_spend": 0.4173,
      "fd_maturing_in_30d": 0,
      "products_dropped_90d": 0,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0,
      "avg_resolution_time_hrs": 19.3999,
      "emi_bounce_30d": 0
    },
    {
      "snapshot_date": "2026-03-01",
      "days_since_last_transaction": 11,
      "balance_change_30d": 31.6644,
      "transaction_change_30d": 26.6107,
      "card_spend_change_30d": -6.5504,
      "app_login_change_30d": 18.7546,
      "salary_missing_days": 0.0,
      "external_transfer_change_30d": -21.5317,
      "upi_share_of_spend": 0.3355,
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
      "balance_change_30d": 24.6289,
      "transaction_change_30d": 9.4006,
      "card_spend_change_30d": -7.9885,
      "app_login_change_30d": 14.6301,
      "salary_missing_days": 1.0,
      "external_transfer_change_30d": 23.1924,
      "upi_share_of_spend": 0.3953,
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
      "days_since_last_transaction": 9,
      "balance_change_30d": -10.8739,
      "transaction_change_30d": 12.9037,
      "card_spend_change_30d": -5.7966,
      "app_login_change_30d": -6.3595,
      "salary_missing_days": 1.0,
      "external_transfer_change_30d": -0.7655,
      "upi_share_of_spend": 0.4065,
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
  "churn_probability": 2.0,
  "raw_churn_probability": 24.05,
  "probability_mode": "sigmoid",
  "risk_score": 6.01,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "latest_vs_avg_upi_share_of_spend_available_history",
      "value": 0.0211399999999999,
      "message": "This signal increased churn risk.",
      "contribution": 0.025518672540783882
    },
    {
      "factor": "max_days_since_last_transaction_3m",
      "value": 11.0,
      "message": "Customer has gone longer without transacting.",
      "contribution": 0.018512729555368423
    },
    {
      "factor": "latest_vs_avg_card_spend_change_30d_available_history",
      "value": 5.331539999999999,
      "message": "This signal increased churn risk.",
      "contribution": 0.013651357032358646
    },
    {
      "factor": "avg_card_spend_change_30d_3m",
      "value": -6.7785,
      "message": "Card spending has been falling across recent months.",
      "contribution": 0.011121201328933239
    },
    {
      "factor": "latest_vs_avg_balance_change_30d_available_history",
      "value": -16.67342,
      "message": "Balance has been falling across recent months.",
      "contribution": 0.010664164088666439
    }
  ]
}
```
