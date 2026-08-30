# Model 1 vs Model 1 v2 Report

- Created at: `2026-08-30T19:27:22`
- Customers tested: `100`

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
| 1 | Ayushman Chander (`C10003`) | 2026-01-01 | 1.96% | 4.62% | 1 |
| 2 | Yashica Issac (`C10040`) | 2026-05-01 | 1.96% | 4.04% | 0 |
| 3 | Baghyawati Kade (`C10098`) | 2026-03-01 | 7.29% | 26.93% | 1 |
| 4 | Ayaan D’Alia (`C10122`) | 2026-05-01 | 3.74% | 2.97% | 0 |
| 5 | Azad Chander (`C10736`) | 2026-05-01 | 1.16% | 3.14% | 0 |
| 6 | Theodore Bahri (`C11005`) | 2026-05-01 | 25.0% | 40.91% | 1 |
| 7 | Aadi Narula (`C11006`) | 2026-05-01 | 1.96% | 2.36% | 0 |
| 8 | Matthew Chatterjee (`C11056`) | 2026-05-01 | 1.96% | 2.35% | 0 |
| 9 | Vrishti Parmer (`C11153`) | 2026-03-01 | 2.39% | 10.57% | 1 |
| 10 | Nakul Pathak (`C11345`) | 2026-05-01 | 7.29% | 21.39% | 0 |
| 11 | Edhitha Palan (`C11532`) | 2026-05-01 | 18.06% | 29.7% | 1 |
| 12 | Max Om (`C11635`) | 2026-05-01 | 2.39% | 5.06% | 0 |
| 13 | Prisha Ravel (`C11661`) | 2026-02-01 | 1.96% | 11.01% | 1 |
| 14 | Oliver Kade (`C11837`) | 2026-05-01 | 1.96% | 9.32% | 1 |
| 15 | Gagan Vala (`C12027`) | 2026-05-01 | 7.29% | 35.12% | 0 |
| 16 | Naveen Tella (`C12090`) | 2026-05-01 | 45.95% | 42.47% | 0 |
| 17 | Qasim Sarraf (`C12096`) | 2026-01-01 | 2.39% | 6.36% | 1 |
| 18 | Bahadurjit Mahal (`C12211`) | 2026-05-01 | 1.96% | 3.86% | 0 |
| 19 | Girish Bhargava (`C12247`) | 2026-05-01 | 8.16% | 4.37% | 0 |
| 20 | Mugdha Sunder (`C12336`) | 2026-05-01 | 1.96% | 2.63% | 0 |
| 21 | Amrita Sahni (`C12339`) | 2026-05-01 | 1.96% | 2.69% | 0 |
| 22 | Madhavi Date (`C12391`) | 2026-04-01 | 16.1% | 41.21% | 1 |
| 23 | Netra Ravi (`C12607`) | 2026-05-01 | 1.96% | 2.84% | 0 |
| 24 | Lohit Jayaraman (`C12715`) | 2026-02-01 | 9.94% | 20.52% | 1 |
| 25 | Shivansh Kar (`C12820`) | 2026-05-01 | 1.96% | 3.04% | 0 |
| 26 | Shaurya Kamdar (`C12831`) | 2026-05-01 | 1.96% | 1.7% | 0 |
| 27 | Qasim Ravi (`C12850`) | 2026-05-01 | 1.96% | 4.65% | 0 |
| 28 | Madhavi Rattan (`C12991`) | 2026-05-01 | 1.96% | 2.38% | 0 |
| 29 | Tara Sangha (`C13175`) | 2026-05-01 | 2.39% | 18.53% | 0 |
| 30 | Chanchal Anne (`C13220`) | 2026-05-01 | 1.96% | 1.61% | 0 |
| 31 | Dhriti Thakur (`C13379`) | 2026-05-01 | 53.85% | 41.36% | 1 |
| 32 | Hredhaan Shetty (`C13411`) | 2026-05-01 | 1.96% | 2.31% | 0 |
| 33 | Xiti Pandey (`C13447`) | 2026-05-01 | 0.0% | 2.33% | 0 |
| 34 | Tamanna Murty (`C13555`) | 2026-04-01 | 20.69% | 34.91% | 1 |
| 35 | Sudiksha Merchant (`C13601`) | 2026-05-01 | 1.93% | 2.76% | 0 |
| 36 | Advika Nadkarni (`C13635`) | 2026-05-01 | 2.39% | 15.94% | 0 |
| 37 | Anmol Bail (`C13643`) | 2026-05-01 | 7.29% | 9.23% | 0 |
| 38 | Jatin Purohit (`C13656`) | 2026-03-01 | 10.0% | 35.84% | 1 |
| 39 | Viraj Bhargava (`C13678`) | 2026-05-01 | 1.96% | 2.24% | 0 |
| 40 | Abha Yogi (`C13919`) | 2026-05-01 | 7.29% | 3.28% | 0 |
| 41 | Anvi Banik (`C13933`) | 2026-05-01 | 1.16% | 3.41% | 0 |
| 42 | Falak Lad (`C14018`) | 2026-05-01 | 7.29% | 20.47% | 0 |
| 43 | Ishanvi Bose (`C14204`) | 2026-05-01 | 1.96% | 3.62% | 0 |
| 44 | Urvi Devi (`C14228`) | 2026-05-01 | 1.96% | 2.36% | 0 |
| 45 | Sara Dada (`C14252`) | 2026-03-01 | 18.06% | 21.19% | 1 |
| 46 | Ethan Bahri (`C14321`) | 2026-05-01 | 9.94% | 25.51% | 0 |
| 47 | Tanay Ramaswamy (`C14341`) | 2026-05-01 | 2.39% | 7.35% | 0 |
| 48 | Gautami Peri (`C14388`) | 2026-03-01 | 3.74% | 16.77% | 1 |
| 49 | Viraj Kade (`C14404`) | 2026-05-01 | 3.74% | 4.67% | 0 |
| 50 | Jatin Borra (`C14412`) | 2026-03-01 | 3.74% | 15.22% | 1 |
| 51 | Kevin Taneja (`C14491`) | 2026-05-01 | 7.29% | 6.0% | 0 |
| 52 | Vrinda Mahal (`C14979`) | 2026-05-01 | 7.29% | 33.53% | 0 |
| 53 | Pooja Atwal (`C14986`) | 2026-05-01 | 2.39% | 2.81% | 0 |
| 54 | Varenya Rana (`C15055`) | 2026-05-01 | 1.65% | 1.71% | 0 |
| 55 | Wyatt Modi (`C15182`) | 2026-05-01 | 1.96% | 4.14% | 0 |
| 56 | Chanchal Khanna (`C15184`) | 2026-04-01 | 10.0% | 28.03% | 1 |
| 57 | Hemal Wagle (`C15335`) | 2026-04-01 | 1.96% | 5.82% | 1 |
| 58 | Urvashi Bhasin (`C15360`) | 2026-05-01 | 16.1% | 35.55% | 1 |
| 59 | Raagini Rai (`C15469`) | 2026-03-01 | 1.96% | 3.83% | 1 |
| 60 | Krisha Rajagopal (`C15597`) | 2026-05-01 | 1.96% | 7.9% | 0 |
| 61 | Vasana Talwar (`C15682`) | 2026-02-01 | 1.96% | 3.94% | 1 |
| 62 | Ekalinga Ram (`C15711`) | 2026-05-01 | 2.39% | 3.19% | 0 |
| 63 | Karan De (`C15967`) | 2026-01-01 | 45.95% | 30.69% | 1 |
| 64 | Robert Sidhu (`C16060`) | 2026-02-01 | 16.1% | 23.66% | 1 |
| 65 | Urvi Kapadia (`C16084`) | 2026-05-01 | 1.96% | 2.2% | 0 |
| 66 | Aradhana Soni (`C16121`) | 2026-04-01 | 2.39% | 19.42% | 1 |
| 67 | Neel Wadhwa (`C16175`) | 2026-05-01 | 1.93% | 2.88% | 0 |
| 68 | Nikita Dugar (`C16218`) | 2026-01-01 | 1.96% | 5.44% | 1 |
| 69 | Charvi Kata (`C16223`) | 2026-05-01 | 1.65% | 2.01% | 0 |
| 70 | Devansh Bath (`C16345`) | 2026-04-01 | 3.74% | 35.68% | 1 |
| 71 | David Bhasin (`C16363`) | 2026-05-01 | 1.96% | 2.76% | 0 |
| 72 | Benjamin Narayan (`C16421`) | 2026-05-01 | 1.65% | 2.55% | 0 |
| 73 | Diya Chandra (`C16671`) | 2026-05-01 | 1.96% | 2.09% | 0 |
| 74 | Elijah Mitra (`C16902`) | 2026-03-01 | 3.74% | 28.75% | 1 |
| 75 | Unnati Date (`C17033`) | 2026-02-01 | 7.29% | 16.76% | 1 |
| 76 | Jai Apte (`C17372`) | 2026-05-01 | 1.96% | 5.64% | 0 |
| 77 | Charles Khanna (`C17462`) | 2026-05-01 | 1.96% | 4.09% | 0 |
| 78 | Chaman Kalita (`C17484`) | 2026-05-01 | 1.96% | 2.04% | 0 |
| 79 | Amara Parikh (`C17639`) | 2026-05-01 | 1.96% | 3.0% | 1 |
| 80 | Hemangini Nazareth (`C17880`) | 2026-05-01 | 2.39% | 2.68% | 0 |
| 81 | Nikita Ganguly (`C17907`) | 2026-04-01 | 7.41% | 26.6% | 1 |
| 82 | Sneha Mahajan (`C17950`) | 2026-05-01 | 2.25% | 8.86% | 0 |
| 83 | Xiti Bath (`C17993`) | 2026-05-01 | 36.3% | 23.37% | 0 |
| 84 | Ethan Bhasin (`C18023`) | 2026-05-01 | 1.96% | 2.81% | 0 |
| 85 | Thomas Kothari (`C18055`) | 2026-05-01 | 1.96% | 3.71% | 0 |
| 86 | Warda Kalita (`C18307`) | 2026-05-01 | 9.94% | 5.97% | 0 |
| 87 | Arin Pandya (`C18434`) | 2026-05-01 | 0.0% | 2.58% | 0 |
| 88 | Mugdha Rajagopal (`C18699`) | 2026-03-01 | 45.95% | 36.27% | 1 |
| 89 | Lavanya Andra (`C18807`) | 2026-05-01 | 1.93% | 5.45% | 0 |
| 90 | Ojas Borra (`C18976`) | 2026-02-01 | 1.96% | 7.39% | 1 |
| 91 | Christopher Sarma (`C19096`) | 2026-02-01 | 7.29% | 17.54% | 1 |
| 92 | Pooja Bawa (`C19159`) | 2026-01-01 | 2.39% | 4.3% | 1 |
| 93 | Anirudh Shukla (`C19179`) | 2026-05-01 | 1.96% | 2.77% | 0 |
| 94 | Ekaraj Gokhale (`C19185`) | 2026-05-01 | 1.96% | 2.6% | 0 |
| 95 | Aadhya Pal (`C19311`) | 2026-05-01 | 1.96% | 2.09% | 0 |
| 96 | Irya Ramakrishnan (`C19406`) | 2026-05-01 | 1.96% | 3.85% | 0 |
| 97 | Hredhaan Bakshi (`C19434`) | 2026-04-01 | 18.06% | 27.34% | 1 |
| 98 | Niharika Oommen (`C19448`) | 2026-05-01 | 95.65% | 37.79% | 1 |
| 99 | Aarini Dar (`C19761`) | 2026-05-01 | 1.96% | 2.88% | 0 |
| 100 | Krish Butala (`C19961`) | 2026-05-01 | 1.96% | 2.36% | 0 |

## Customer Details

### 1. Ayushman Chander (`C10003`)

#### Model 1 Input

```json
{
  "customer_id": "C10003",
  "customer_name": "Ayushman Chander",
  "snapshot_date": "2026-01-01",
  "customer": {
    "age": 25,
    "tenure_months": 39,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 2,
    "has_credit_card": 0,
    "has_loan": 1,
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
    "emi_bounce_30d": 0,
    "branch_code": "BR-137",
    "card_colour": "silver"
  },
  "actual_next_month_churn": 1
}
```

#### Model 1 Output

```json
{
  "churn_probability": 1.96,
  "raw_churn_probability": 2.14,
  "risk_score": 5.87,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "tenure_months",
      "value": 39
    },
    {
      "factor": "card_spend_change_30d",
      "value": -24.0555
    },
    {
      "factor": "age",
      "value": 25
    },
    {
      "factor": "external_transfer_change_30d",
      "value": 57.912
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
  "churn_probability": 4.62,
  "raw_churn_probability": 36.98,
  "probability_mode": "sigmoid",
  "risk_score": 13.85,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "latest_external_transfer_change_30d",
      "value": 57.912,
      "message": "External transfers have increased.",
      "contribution": 0.1152321994304657
    },
    {
      "factor": "avg_card_spend_change_30d_3m",
      "value": -24.0555,
      "message": "Card spending has been falling across recent months.",
      "contribution": 0.04462185874581337
    },
    {
      "factor": "avg_external_transfer_change_30d_3m",
      "value": 57.912,
      "message": "External transfers have increased.",
      "contribution": 0.034331176429986954
    },
    {
      "factor": "avg_card_spend_change_30d_6m",
      "value": -24.0555,
      "message": "Card spending has been falling across recent months.",
      "contribution": 0.033895839005708694
    },
    {
      "factor": "avg_external_transfer_change_30d_6m",
      "value": 57.912,
      "message": "External transfers have increased.",
      "contribution": 0.027452170848846436
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
  "snapshot_date": "2026-05-01",
  "customer": {
    "age": 35,
    "tenure_months": 142,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 2,
    "has_credit_card": 0,
    "has_loan": 1,
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
    "emi_bounce_30d": 0,
    "branch_code": "BR-103",
    "card_colour": "silver"
  },
  "actual_next_month_churn": 0
}
```

#### Model 1 Output

```json
{
  "churn_probability": 1.96,
  "raw_churn_probability": 1.85,
  "risk_score": 5.87,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "upi_share_of_spend",
      "value": 0.346
    },
    {
      "factor": "external_transfer_change_30d",
      "value": 30.6872
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
  "churn_probability": 4.04,
  "raw_churn_probability": 33.97,
  "probability_mode": "sigmoid",
  "risk_score": 12.11,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "latest_vs_avg_upi_share_of_spend_available_history",
      "value": 0.0353799999999999,
      "message": "This signal increased churn risk.",
      "contribution": 0.07607629895210266
    },
    {
      "factor": "count_quiet_customer_3m",
      "value": 3,
      "message": "This signal increased churn risk.",
      "contribution": 0.05046837404370308
    },
    {
      "factor": "max_days_since_last_transaction_3m",
      "value": 19.0,
      "message": "Customer has gone longer without transacting.",
      "contribution": 0.03322892263531685
    },
    {
      "factor": "external_transfer_change_30d_trend_6m",
      "value": 2.5177499999999977,
      "message": "External transfers have increased.",
      "contribution": 0.024330055341124535
    },
    {
      "factor": "count_quiet_customer_6m",
      "value": 5,
      "message": "This signal increased churn risk.",
      "contribution": 0.02084338106215
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
  "snapshot_date": "2026-03-01",
  "customer": {
    "age": 80,
    "tenure_months": 164,
    "customer_segment": "pension",
    "income_regularity": "regular",
    "products_count": 1,
    "has_credit_card": 0,
    "has_loan": 0,
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
    "emi_bounce_30d": 0,
    "branch_code": "BR-117",
    "card_colour": "silver"
  },
  "actual_next_month_churn": 1
}
```

#### Model 1 Output

```json
{
  "churn_probability": 7.29,
  "raw_churn_probability": 7.88,
  "risk_score": 21.86,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "avg_resolution_time_hrs",
      "value": 69.3246
    },
    {
      "factor": "complaints_30d",
      "value": 6
    },
    {
      "factor": "unresolved_complaints",
      "value": 3
    },
    {
      "factor": "age",
      "value": 80
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
  "churn_probability": 26.93,
  "raw_churn_probability": 80.58,
  "probability_mode": "sigmoid",
  "risk_score": 72.6,
  "churn_prediction": "Yes",
  "risk_level": "High",
  "top_risk_factors": [
    {
      "factor": "max_avg_resolution_time_hrs_3m",
      "value": 69.3246,
      "message": "This signal increased churn risk.",
      "contribution": 0.6523938179016113
    },
    {
      "factor": "latest_avg_resolution_time_hrs",
      "value": 69.3246,
      "message": "This signal increased churn risk.",
      "contribution": 0.47629889845848083
    },
    {
      "factor": "sum_failed_transactions_30d_3m",
      "value": 9.0,
      "message": "Customer has recent failed transactions.",
      "contribution": 0.36161792278289795
    },
    {
      "factor": "sum_failed_transactions_30d_6m",
      "value": 9.0,
      "message": "Customer has recent failed transactions.",
      "contribution": 0.12564130127429962
    },
    {
      "factor": "sum_complaints_30d_3m",
      "value": 6.0,
      "message": "Customer has recent complaint activity.",
      "contribution": 0.09594690054655075
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

### 5. Azad Chander (`C10736`)

#### Model 1 Input

```json
{
  "customer_id": "C10736",
  "customer_name": "Azad Chander",
  "snapshot_date": "2026-05-01",
  "customer": {
    "age": 72,
    "tenure_months": 226,
    "customer_segment": "pension",
    "income_regularity": "regular",
    "products_count": 1,
    "has_credit_card": 0,
    "has_loan": 0,
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
    "emi_bounce_30d": 0,
    "branch_code": "BR-119",
    "card_colour": "green"
  },
  "actual_next_month_churn": 0
}
```

#### Model 1 Output

```json
{
  "churn_probability": 1.16,
  "raw_churn_probability": 1.12,
  "risk_score": 3.49,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "age",
      "value": 72
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
      "factor": "upi_share_of_spend",
      "value": 0.9245
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
  "churn_probability": 3.14,
  "raw_churn_probability": 28.35,
  "probability_mode": "sigmoid",
  "risk_score": 9.41,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "latest_vs_avg_upi_share_of_spend_available_history",
      "value": 0.09588,
      "message": "This signal increased churn risk.",
      "contribution": 0.17058898508548737
    },
    {
      "factor": "sum_fd_maturing_in_30d_3m",
      "value": 1.0,
      "message": "Customer has a fixed deposit maturing soon.",
      "contribution": 0.06880325824022293
    },
    {
      "factor": "latest_upi_share_of_spend",
      "value": 0.9245,
      "message": "This signal increased churn risk.",
      "contribution": 0.04927142336964607
    },
    {
      "factor": "latest_vs_avg_external_transfer_change_30d_available_history",
      "value": -26.99682,
      "message": "This signal increased churn risk.",
      "contribution": 0.04881404712796211
    },
    {
      "factor": "latest_vs_avg_balance_change_30d_available_history",
      "value": 22.59542,
      "message": "This signal increased churn risk.",
      "contribution": 0.03905041143298149
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

### 7. Aadi Narula (`C11006`)

#### Model 1 Input

```json
{
  "customer_id": "C11006",
  "customer_name": "Aadi Narula",
  "snapshot_date": "2026-05-01",
  "customer": {
    "age": 54,
    "tenure_months": 129,
    "customer_segment": "farmer",
    "income_regularity": "seasonal",
    "products_count": 2,
    "has_credit_card": 0,
    "has_loan": 1,
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
    "emi_bounce_30d": 0,
    "branch_code": "BR-138",
    "card_colour": "gold"
  },
  "actual_next_month_churn": 0
}
```

#### Model 1 Output

```json
{
  "churn_probability": 1.96,
  "raw_churn_probability": 2.16,
  "risk_score": 5.87,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "branch_code",
      "value": "BR-138"
    },
    {
      "factor": "failed_transactions_30d",
      "value": 2
    },
    {
      "factor": "external_transfer_change_30d",
      "value": 39.3493
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
  "churn_probability": 2.36,
  "raw_churn_probability": 22.11,
  "probability_mode": "sigmoid",
  "risk_score": 7.09,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "avg_card_spend_change_30d_6m",
      "value": -18.39666,
      "message": "Card spending has been falling across recent months.",
      "contribution": 0.03493345156311989
    },
    {
      "factor": "avg_card_spend_change_30d_3m",
      "value": -14.315866666666665,
      "message": "Card spending has been falling across recent months.",
      "contribution": 0.034015920013189316
    },
    {
      "factor": "avg_upi_share_of_spend_3m",
      "value": 0.7324999999999999,
      "message": "This signal increased churn risk.",
      "contribution": 0.02725871093571186
    },
    {
      "factor": "latest_upi_share_of_spend",
      "value": 0.6876,
      "message": "This signal increased churn risk.",
      "contribution": 0.025592269375920296
    },
    {
      "factor": "avg_upi_share_of_spend_6m",
      "value": 0.72464,
      "message": "This signal increased churn risk.",
      "contribution": 0.019852755591273308
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
  "snapshot_date": "2026-05-01",
  "customer": {
    "age": 60,
    "tenure_months": 165,
    "customer_segment": "pension",
    "income_regularity": "regular",
    "products_count": 3,
    "has_credit_card": 1,
    "has_loan": 0,
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
    "emi_bounce_30d": 0,
    "branch_code": "BR-103",
    "card_colour": "gold"
  },
  "actual_next_month_churn": 0
}
```

#### Model 1 Output

```json
{
  "churn_probability": 1.96,
  "raw_churn_probability": 2.09,
  "risk_score": 5.87,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "failed_transactions_30d",
      "value": 2
    },
    {
      "factor": "upi_share_of_spend",
      "value": 0.216
    },
    {
      "factor": "customer_segment",
      "value": "pension"
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
  "churn_probability": 2.35,
  "raw_churn_probability": 21.99,
  "probability_mode": "sigmoid",
  "risk_score": 7.06,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "latest_vs_avg_external_transfer_change_30d_available_history",
      "value": -33.65882,
      "message": "This signal increased churn risk.",
      "contribution": 0.0797099694609642
    },
    {
      "factor": "count_quiet_customer_3m",
      "value": 2,
      "message": "This signal increased churn risk.",
      "contribution": 0.04016046226024628
    },
    {
      "factor": "max_days_since_last_transaction_3m",
      "value": 17.0,
      "message": "Customer has gone longer without transacting.",
      "contribution": 0.037259869277477264
    },
    {
      "factor": "avg_upi_share_of_spend_6m",
      "value": 0.2883799999999999,
      "message": "This signal increased churn risk.",
      "contribution": 0.018756410107016563
    },
    {
      "factor": "sum_failed_transactions_30d_6m",
      "value": 5.0,
      "message": "Customer has recent failed transactions.",
      "contribution": 0.010174417868256569
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
  "snapshot_date": "2026-03-01",
  "customer": {
    "age": 49,
    "tenure_months": 53,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 2,
    "has_credit_card": 0,
    "has_loan": 1,
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
    "emi_bounce_30d": 0,
    "branch_code": "BR-131",
    "card_colour": "green"
  },
  "actual_next_month_churn": 1
}
```

#### Model 1 Output

```json
{
  "churn_probability": 2.39,
  "raw_churn_probability": 3.09,
  "risk_score": 7.18,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "unresolved_complaints",
      "value": 1
    },
    {
      "factor": "tenure_months",
      "value": 53
    },
    {
      "factor": "salary_missing_days",
      "value": 2.0
    },
    {
      "factor": "branch_code",
      "value": "BR-131"
    },
    {
      "factor": "avg_resolution_time_hrs",
      "value": 49.5283
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
  "churn_probability": 10.57,
  "raw_churn_probability": 56.15,
  "probability_mode": "sigmoid",
  "risk_score": 32.27,
  "churn_prediction": "Yes",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "latest_avg_resolution_time_hrs",
      "value": 49.5283,
      "message": "This signal increased churn risk.",
      "contribution": 0.4239612817764282
    },
    {
      "factor": "latest_vs_avg_upi_share_of_spend_available_history",
      "value": 0.0344333333333333,
      "message": "This signal increased churn risk.",
      "contribution": 0.08508741110563278
    },
    {
      "factor": "latest_salary_missing_days",
      "value": 2.0,
      "message": "This signal increased churn risk.",
      "contribution": 0.07870952039957047
    },
    {
      "factor": "max_avg_resolution_time_hrs_3m",
      "value": 49.5283,
      "message": "This signal increased churn risk.",
      "contribution": 0.06960994750261307
    },
    {
      "factor": "count_quiet_customer_3m",
      "value": 2,
      "message": "This signal increased churn risk.",
      "contribution": 0.04554307460784912
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
  "snapshot_date": "2026-05-01",
  "customer": {
    "age": 36,
    "tenure_months": 138,
    "customer_segment": "farmer",
    "income_regularity": "seasonal",
    "products_count": 2,
    "has_credit_card": 0,
    "has_loan": 1,
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
    "emi_bounce_30d": 0,
    "branch_code": "BR-134",
    "card_colour": "gold"
  },
  "actual_next_month_churn": 0
}
```

#### Model 1 Output

```json
{
  "churn_probability": 7.29,
  "raw_churn_probability": 6.86,
  "risk_score": 21.86,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "days_since_last_transaction",
      "value": 17
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
      "factor": "unresolved_complaints",
      "value": 1
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
  "churn_probability": 21.39,
  "raw_churn_probability": 74.07,
  "probability_mode": "sigmoid",
  "risk_score": 70.52,
  "churn_prediction": "Yes",
  "risk_level": "Medium",
  "top_risk_factors": [
    {
      "factor": "latest_days_since_last_transaction",
      "value": 17,
      "message": "Customer has gone longer without transacting.",
      "contribution": 0.6167489886283875
    },
    {
      "factor": "latest_avg_resolution_time_hrs",
      "value": 43.9323,
      "message": "This signal increased churn risk.",
      "contribution": 0.3015771806240082
    },
    {
      "factor": "latest_transaction_change_30d",
      "value": -23.8049,
      "message": "Transaction activity has been falling across recent months.",
      "contribution": 0.1391603648662567
    },
    {
      "factor": "latest_external_transfer_change_30d",
      "value": 62.6145,
      "message": "External transfers have increased.",
      "contribution": 0.12248808890581131
    },
    {
      "factor": "sum_fd_maturing_in_30d_3m",
      "value": 1.0,
      "message": "Customer has a fixed deposit maturing soon.",
      "contribution": 0.08080471307039261
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

### 12. Max Om (`C11635`)

#### Model 1 Input

```json
{
  "customer_id": "C11635",
  "customer_name": "Max Om",
  "snapshot_date": "2026-05-01",
  "customer": {
    "age": 35,
    "tenure_months": 129,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 4,
    "has_credit_card": 1,
    "has_loan": 0,
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
    "emi_bounce_30d": 0,
    "branch_code": "BR-106",
    "card_colour": "black"
  },
  "actual_next_month_churn": 0
}
```

#### Model 1 Output

```json
{
  "churn_probability": 2.39,
  "raw_churn_probability": 3.76,
  "risk_score": 7.18,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "branch_code",
      "value": "BR-106"
    },
    {
      "factor": "fd_maturing_in_30d",
      "value": 1
    },
    {
      "factor": "failed_transactions_30d",
      "value": 2
    },
    {
      "factor": "transaction_change_30d",
      "value": 12.0228
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
  "churn_probability": 5.06,
  "raw_churn_probability": 39.03,
  "probability_mode": "sigmoid",
  "risk_score": 15.17,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "latest_vs_avg_upi_share_of_spend_available_history",
      "value": 0.11794,
      "message": "This signal increased churn risk.",
      "contribution": 0.1551114171743393
    },
    {
      "factor": "latest_fd_maturing_in_30d",
      "value": 1,
      "message": "Customer has a fixed deposit maturing soon.",
      "contribution": 0.11341489106416702
    },
    {
      "factor": "sum_fd_maturing_in_30d_3m",
      "value": 1.0,
      "message": "Customer has a fixed deposit maturing soon.",
      "contribution": 0.079158715903759
    },
    {
      "factor": "days_since_last_transaction_trend_6m",
      "value": 0.9999999999999996,
      "message": "Customer has gone longer without transacting.",
      "contribution": 0.05521949753165245
    },
    {
      "factor": "balance_change_30d_trend_6m",
      "value": -7.991460000000002,
      "message": "Balance has been falling across recent months.",
      "contribution": 0.03871840238571167
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
  "snapshot_date": "2026-02-01",
  "customer": {
    "age": 47,
    "tenure_months": 122,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 1,
    "has_credit_card": 0,
    "has_loan": 0,
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
    "emi_bounce_30d": 0,
    "branch_code": "BR-109",
    "card_colour": "gold"
  },
  "actual_next_month_churn": 1
}
```

#### Model 1 Output

```json
{
  "churn_probability": 1.96,
  "raw_churn_probability": 2.41,
  "risk_score": 5.87,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "failed_transactions_30d",
      "value": 4
    },
    {
      "factor": "branch_code",
      "value": "BR-109"
    },
    {
      "factor": "upi_share_of_spend",
      "value": 0.1728
    },
    {
      "factor": "external_transfer_change_30d",
      "value": 60.3143
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
  "churn_probability": 11.01,
  "raw_churn_probability": 57.15,
  "probability_mode": "sigmoid",
  "risk_score": 34.05,
  "churn_prediction": "Yes",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "sum_failed_transactions_30d_3m",
      "value": 7.0,
      "message": "Customer has recent failed transactions.",
      "contribution": 0.3748191297054291
    },
    {
      "factor": "latest_failed_transactions_30d",
      "value": 4,
      "message": "Customer has recent failed transactions.",
      "contribution": 0.2386663407087326
    },
    {
      "factor": "external_transfer_change_30d_trend_6m",
      "value": 48.85429999999999,
      "message": "External transfers have increased.",
      "contribution": 0.13773711025714874
    },
    {
      "factor": "latest_external_transfer_change_30d",
      "value": 60.3143,
      "message": "External transfers have increased.",
      "contribution": 0.13249154388904572
    },
    {
      "factor": "max_avg_resolution_time_hrs_3m",
      "value": 45.614,
      "message": "This signal increased churn risk.",
      "contribution": 0.08271753787994385
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

### 15. Gagan Vala (`C12027`)

#### Model 1 Input

```json
{
  "customer_id": "C12027",
  "customer_name": "Gagan Vala",
  "snapshot_date": "2026-05-01",
  "customer": {
    "age": 35,
    "tenure_months": 90,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 1,
    "has_credit_card": 0,
    "has_loan": 0,
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
    "emi_bounce_30d": 0,
    "branch_code": "BR-112",
    "card_colour": "silver"
  },
  "actual_next_month_churn": 0
}
```

#### Model 1 Output

```json
{
  "churn_probability": 7.29,
  "raw_churn_probability": 8.75,
  "risk_score": 21.86,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "card_spend_change_30d",
      "value": -36.6355
    },
    {
      "factor": "salary_missing_days",
      "value": 4.0
    },
    {
      "factor": "balance_change_30d",
      "value": -21.5167
    },
    {
      "factor": "days_since_last_transaction",
      "value": 14
    },
    {
      "factor": "branch_code",
      "value": "BR-112"
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
  "churn_probability": 35.12,
  "raw_churn_probability": 88.84,
  "probability_mode": "sigmoid",
  "risk_score": 75.67,
  "churn_prediction": "Yes",
  "risk_level": "High",
  "top_risk_factors": [
    {
      "factor": "latest_days_since_last_transaction",
      "value": 14,
      "message": "Customer has gone longer without transacting.",
      "contribution": 0.4730629026889801
    },
    {
      "factor": "latest_vs_avg_upi_share_of_spend_available_history",
      "value": 0.0498400000000001,
      "message": "This signal increased churn risk.",
      "contribution": 0.23521780967712402
    },
    {
      "factor": "latest_salary_missing_days",
      "value": 4.0,
      "message": "This signal increased churn risk.",
      "contribution": 0.2116551548242569
    },
    {
      "factor": "days_since_last_transaction_trend_6m",
      "value": 2.0999999999999988,
      "message": "Customer has gone longer without transacting.",
      "contribution": 0.2051222324371338
    },
    {
      "factor": "latest_balance_change_30d",
      "value": -21.5167,
      "message": "Balance has been falling across recent months.",
      "contribution": 0.1384003609418869
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
  "snapshot_date": "2026-05-01",
  "customer": {
    "age": 41,
    "tenure_months": 35,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 1,
    "has_credit_card": 0,
    "has_loan": 0,
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
    "emi_bounce_30d": 0,
    "branch_code": "BR-125",
    "card_colour": "black"
  },
  "actual_next_month_churn": 0
}
```

#### Model 1 Output

```json
{
  "churn_probability": 45.95,
  "raw_churn_probability": 52.46,
  "risk_score": 79.73,
  "churn_prediction": "Yes",
  "risk_level": "High",
  "top_risk_factors": [
    {
      "factor": "balance_change_30d",
      "value": -48.976
    },
    {
      "factor": "days_since_last_transaction",
      "value": 22
    },
    {
      "factor": "salary_missing_days",
      "value": 7.0
    },
    {
      "factor": "tenure_months",
      "value": 35
    },
    {
      "factor": "card_spend_change_30d",
      "value": -30.8633
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
  "churn_probability": 42.47,
  "raw_churn_probability": 95.5,
  "probability_mode": "sigmoid",
  "risk_score": 78.43,
  "churn_prediction": "Yes",
  "risk_level": "High",
  "top_risk_factors": [
    {
      "factor": "latest_days_since_last_transaction",
      "value": 22,
      "message": "Customer has gone longer without transacting.",
      "contribution": 0.6401055455207825
    },
    {
      "factor": "latest_transaction_change_30d",
      "value": -48.1033,
      "message": "Transaction activity has been falling across recent months.",
      "contribution": 0.38283148407936096
    },
    {
      "factor": "latest_salary_missing_days",
      "value": 7.0,
      "message": "This signal increased churn risk.",
      "contribution": 0.2999474108219147
    },
    {
      "factor": "days_since_last_transaction_trend_6m",
      "value": 4.0,
      "message": "Customer has gone longer without transacting.",
      "contribution": 0.21994216740131378
    },
    {
      "factor": "max_salary_missing_days_3m",
      "value": 7.0,
      "message": "This signal increased churn risk.",
      "contribution": 0.21805495023727417
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
  "snapshot_date": "2026-01-01",
  "customer": {
    "age": 58,
    "tenure_months": 169,
    "customer_segment": "pension",
    "income_regularity": "regular",
    "products_count": 1,
    "has_credit_card": 0,
    "has_loan": 0,
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
    "emi_bounce_30d": 0,
    "branch_code": "BR-103",
    "card_colour": "black"
  },
  "actual_next_month_churn": 1
}
```

#### Model 1 Output

```json
{
  "churn_probability": 2.39,
  "raw_churn_probability": 3.45,
  "risk_score": 7.18,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "failed_transactions_30d",
      "value": 3
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
      "factor": "customer_segment",
      "value": "pension"
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
  "churn_probability": 6.36,
  "raw_churn_probability": 44.27,
  "probability_mode": "sigmoid",
  "risk_score": 19.09,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "latest_avg_resolution_time_hrs",
      "value": 38.3385,
      "message": "This signal increased churn risk.",
      "contribution": 0.275077223777771
    },
    {
      "factor": "latest_failed_transactions_30d",
      "value": 3,
      "message": "Customer has recent failed transactions.",
      "contribution": 0.14174233376979828
    },
    {
      "factor": "external_transfer_change_30d_trend_6m",
      "value": 0.0,
      "message": "This signal increased churn risk.",
      "contribution": 0.03028945066034794
    },
    {
      "factor": "latest_vs_avg_card_spend_change_30d_available_history",
      "value": 0.0,
      "message": "This signal increased churn risk.",
      "contribution": 0.019505193457007408
    },
    {
      "factor": "transaction_change_30d_trend_6m",
      "value": 0.0,
      "message": "This signal increased churn risk.",
      "contribution": 0.017507461830973625
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
  "snapshot_date": "2026-05-01",
  "customer": {
    "age": 42,
    "tenure_months": 77,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 1,
    "has_credit_card": 0,
    "has_loan": 0,
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
    "emi_bounce_30d": 0,
    "branch_code": "BR-112",
    "card_colour": "black"
  },
  "actual_next_month_churn": 0
}
```

#### Model 1 Output

```json
{
  "churn_probability": 1.96,
  "raw_churn_probability": 1.67,
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
      "value": "BR-112"
    },
    {
      "factor": "upi_share_of_spend",
      "value": 0.1325
    },
    {
      "factor": "app_login_change_30d",
      "value": 16.9153
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
  "churn_probability": 3.86,
  "raw_churn_probability": 32.97,
  "probability_mode": "sigmoid",
  "risk_score": 11.58,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "latest_fd_maturing_in_30d",
      "value": 1,
      "message": "Customer has a fixed deposit maturing soon.",
      "contribution": 0.20731548964977264
    },
    {
      "factor": "sum_fd_maturing_in_30d_3m",
      "value": 1.0,
      "message": "Customer has a fixed deposit maturing soon.",
      "contribution": 0.0859856829047203
    },
    {
      "factor": "latest_vs_avg_external_transfer_change_30d_available_history",
      "value": -34.9049,
      "message": "This signal increased churn risk.",
      "contribution": 0.0785028412938118
    },
    {
      "factor": "latest_external_transfer_change_30d",
      "value": -43.159,
      "message": "This signal increased churn risk.",
      "contribution": 0.045260291546583176
    },
    {
      "factor": "latest_vs_avg_card_spend_change_30d_available_history",
      "value": 31.03584,
      "message": "This signal increased churn risk.",
      "contribution": 0.043678104877471924
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
  "snapshot_date": "2026-05-01",
  "customer": {
    "age": 63,
    "tenure_months": 160,
    "customer_segment": "pension",
    "income_regularity": "regular",
    "products_count": 1,
    "has_credit_card": 0,
    "has_loan": 0,
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
    "emi_bounce_30d": 0,
    "branch_code": "BR-115",
    "card_colour": "silver"
  },
  "actual_next_month_churn": 0
}
```

#### Model 1 Output

```json
{
  "churn_probability": 8.16,
  "raw_churn_probability": 10.01,
  "risk_score": 24.49,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "fd_maturing_in_30d",
      "value": 1
    },
    {
      "factor": "complaints_30d",
      "value": 2
    },
    {
      "factor": "salary_missing_days",
      "value": 3.0
    },
    {
      "factor": "card_spend_change_30d",
      "value": -22.6556
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
  "churn_probability": 4.37,
  "raw_churn_probability": 35.74,
  "probability_mode": "sigmoid",
  "risk_score": 13.11,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "latest_vs_avg_upi_share_of_spend_available_history",
      "value": 0.14082,
      "message": "This signal increased churn risk.",
      "contribution": 0.17341507971286774
    },
    {
      "factor": "latest_fd_maturing_in_30d",
      "value": 1,
      "message": "Customer has a fixed deposit maturing soon.",
      "contribution": 0.1481606811285019
    },
    {
      "factor": "latest_salary_missing_days",
      "value": 3.0,
      "message": "This signal increased churn risk.",
      "contribution": 0.1454518586397171
    },
    {
      "factor": "days_since_last_transaction_trend_6m",
      "value": 1.2999999999999998,
      "message": "Customer has gone longer without transacting.",
      "contribution": 0.11002194881439209
    },
    {
      "factor": "sum_fd_maturing_in_30d_3m",
      "value": 2.0,
      "message": "Customer has a fixed deposit maturing soon.",
      "contribution": 0.08622314780950546
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
  "snapshot_date": "2026-05-01",
  "customer": {
    "age": 58,
    "tenure_months": 40,
    "customer_segment": "business",
    "income_regularity": "irregular",
    "products_count": 2,
    "has_credit_card": 0,
    "has_loan": 1,
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
    "emi_bounce_30d": 0,
    "branch_code": "BR-129",
    "card_colour": "green"
  },
  "actual_next_month_churn": 0
}
```

#### Model 1 Output

```json
{
  "churn_probability": 1.96,
  "raw_churn_probability": 2.48,
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
      "value": 40
    },
    {
      "factor": "unresolved_complaints",
      "value": 1
    },
    {
      "factor": "app_login_change_30d",
      "value": 10.0579
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
  "churn_probability": 2.63,
  "raw_churn_probability": 24.47,
  "probability_mode": "sigmoid",
  "risk_score": 7.9,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "sum_fd_maturing_in_30d_3m",
      "value": 1.0,
      "message": "Customer has a fixed deposit maturing soon.",
      "contribution": 0.09560070186853409
    },
    {
      "factor": "max_days_since_last_transaction_3m",
      "value": 12.0,
      "message": "Customer has gone longer without transacting.",
      "contribution": 0.02862040512263775
    },
    {
      "factor": "avg_card_spend_change_30d_3m",
      "value": -13.3847,
      "message": "Card spending has been falling across recent months.",
      "contribution": 0.013966298662126064
    },
    {
      "factor": "latest_vs_avg_card_spend_change_30d_available_history",
      "value": 3.829979999999999,
      "message": "This signal increased churn risk.",
      "contribution": 0.012958653271198273
    },
    {
      "factor": "count_external_transfer_rise_6m",
      "value": 0,
      "message": "This signal increased churn risk.",
      "contribution": 0.009755546227097511
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
  "snapshot_date": "2026-05-01",
  "customer": {
    "age": 53,
    "tenure_months": 1,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 3,
    "has_credit_card": 1,
    "has_loan": 1,
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
    "emi_bounce_30d": 0,
    "branch_code": "BR-111",
    "card_colour": "green"
  },
  "actual_next_month_churn": 0
}
```

#### Model 1 Output

```json
{
  "churn_probability": 1.96,
  "raw_churn_probability": 2.6,
  "risk_score": 5.87,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "tenure_months",
      "value": 1
    },
    {
      "factor": "branch_code",
      "value": "BR-111"
    },
    {
      "factor": "customer_segment",
      "value": "salary"
    },
    {
      "factor": "card_colour",
      "value": "green"
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
  "churn_probability": 2.69,
  "raw_churn_probability": 24.94,
  "probability_mode": "sigmoid",
  "risk_score": 8.07,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "latest_vs_avg_upi_share_of_spend_available_history",
      "value": 0.0757399999999999,
      "message": "This signal increased churn risk.",
      "contribution": 0.17937572300434113
    },
    {
      "factor": "sum_complaints_30d_6m",
      "value": 6.0,
      "message": "Customer has recent complaint activity.",
      "contribution": 0.09394565969705582
    },
    {
      "factor": "avg_transaction_change_30d_6m",
      "value": 18.32758,
      "message": "This signal increased churn risk.",
      "contribution": 0.0475764274597168
    },
    {
      "factor": "balance_change_30d_trend_6m",
      "value": -5.613700000000003,
      "message": "Balance has been falling across recent months.",
      "contribution": 0.0281006321310997
    },
    {
      "factor": "latest_vs_avg_balance_change_30d_available_history",
      "value": -11.821140000000002,
      "message": "Balance has been falling across recent months.",
      "contribution": 0.023379305377602577
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

### 23. Netra Ravi (`C12607`)

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

### 24. Lohit Jayaraman (`C12715`)

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

### 25. Shivansh Kar (`C12820`)

#### Model 1 Input

```json
{
  "customer_id": "C12820",
  "customer_name": "Shivansh Kar",
  "snapshot_date": "2026-05-01",
  "customer": {
    "age": 42,
    "tenure_months": 76,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 2,
    "has_credit_card": 1,
    "has_loan": 0,
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
    "emi_bounce_30d": 0,
    "branch_code": "BR-130",
    "card_colour": "gold"
  },
  "actual_next_month_churn": 0
}
```

#### Model 1 Output

```json
{
  "churn_probability": 1.96,
  "raw_churn_probability": 1.85,
  "risk_score": 5.87,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "card_spend_change_30d",
      "value": -22.522
    },
    {
      "factor": "upi_share_of_spend",
      "value": 0.2128
    },
    {
      "factor": "external_transfer_change_30d",
      "value": 10.7085
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
  "churn_probability": 3.04,
  "raw_churn_probability": 27.69,
  "probability_mode": "sigmoid",
  "risk_score": 9.13,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "external_transfer_change_30d_trend_6m",
      "value": 11.850110000000004,
      "message": "External transfers have increased.",
      "contribution": 0.045390862971544266
    },
    {
      "factor": "balance_change_30d_trend_6m",
      "value": -6.4438100000000045,
      "message": "Balance has been falling across recent months.",
      "contribution": 0.02802552469074726
    },
    {
      "factor": "latest_vs_avg_upi_share_of_spend_available_history",
      "value": 0.0235799999999999,
      "message": "This signal increased churn risk.",
      "contribution": 0.026694586500525475
    },
    {
      "factor": "transaction_change_30d_trend_6m",
      "value": -1.453700000000001,
      "message": "Transaction activity has been falling across recent months.",
      "contribution": 0.023308351635932922
    },
    {
      "factor": "avg_upi_share_of_spend_6m",
      "value": 0.18922,
      "message": "This signal increased churn risk.",
      "contribution": 0.019581051543354988
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
  "snapshot_date": "2026-05-01",
  "customer": {
    "age": 40,
    "tenure_months": 88,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 1,
    "has_credit_card": 0,
    "has_loan": 0,
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
    "emi_bounce_30d": 0,
    "branch_code": "BR-112",
    "card_colour": "blue"
  },
  "actual_next_month_churn": 0
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
      "factor": "branch_code",
      "value": "BR-112"
    },
    {
      "factor": "failed_transactions_30d",
      "value": 2
    },
    {
      "factor": "upi_share_of_spend",
      "value": 0.0888
    },
    {
      "factor": "app_login_change_30d",
      "value": 24.9196
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
  "churn_probability": 1.7,
  "raw_churn_probability": 14.94,
  "probability_mode": "sigmoid",
  "risk_score": 5.11,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "card_spend_change_30d_trend_6m",
      "value": 12.77015,
      "message": "This signal increased churn risk.",
      "contribution": 0.03326667472720146
    },
    {
      "factor": "avg_upi_share_of_spend_6m",
      "value": 0.12214,
      "message": "This signal increased churn risk.",
      "contribution": 0.024917634204030037
    },
    {
      "factor": "count_balance_drop_3m",
      "value": 1,
      "message": "This signal increased churn risk.",
      "contribution": 0.007323273923248053
    },
    {
      "factor": "latest_vs_avg_transaction_change_30d_available_history",
      "value": 15.166240000000002,
      "message": "This signal increased churn risk.",
      "contribution": 0.00598517432808876
    },
    {
      "factor": "latest_vs_avg_external_transfer_change_30d_available_history",
      "value": -8.593639999999999,
      "message": "This signal increased churn risk.",
      "contribution": 0.003581043565645814
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
  "snapshot_date": "2026-05-01",
  "customer": {
    "age": 34,
    "tenure_months": 68,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 3,
    "has_credit_card": 1,
    "has_loan": 0,
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
    "emi_bounce_30d": 0,
    "branch_code": "BR-101",
    "card_colour": "blue"
  },
  "actual_next_month_churn": 0
}
```

#### Model 1 Output

```json
{
  "churn_probability": 1.96,
  "raw_churn_probability": 2.41,
  "risk_score": 5.87,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "branch_code",
      "value": "BR-101"
    },
    {
      "factor": "days_since_last_transaction",
      "value": 14
    },
    {
      "factor": "card_colour",
      "value": "blue"
    },
    {
      "factor": "customer_segment",
      "value": "salary"
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
  "churn_probability": 4.65,
  "raw_churn_probability": 37.16,
  "probability_mode": "sigmoid",
  "risk_score": 13.96,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "latest_days_since_last_transaction",
      "value": 14,
      "message": "Customer has gone longer without transacting.",
      "contribution": 0.5215210914611816
    },
    {
      "factor": "count_quiet_customer_3m",
      "value": 2,
      "message": "This signal increased churn risk.",
      "contribution": 0.06398528069257736
    },
    {
      "factor": "count_balance_drop_6m",
      "value": 4,
      "message": "This signal increased churn risk.",
      "contribution": 0.04125675931572914
    },
    {
      "factor": "card_spend_change_30d_trend_6m",
      "value": 7.274800000000001,
      "message": "This signal increased churn risk.",
      "contribution": 0.03836657851934433
    },
    {
      "factor": "latest_upi_share_of_spend",
      "value": 0.662,
      "message": "This signal increased churn risk.",
      "contribution": 0.03469259664416313
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

### 29. Tara Sangha (`C13175`)

#### Model 1 Input

```json
{
  "customer_id": "C13175",
  "customer_name": "Tara Sangha",
  "snapshot_date": "2026-05-01",
  "customer": {
    "age": 30,
    "tenure_months": 67,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 1,
    "has_credit_card": 0,
    "has_loan": 0,
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
    "emi_bounce_30d": 0,
    "branch_code": "BR-129",
    "card_colour": "green"
  },
  "actual_next_month_churn": 0
}
```

#### Model 1 Output

```json
{
  "churn_probability": 2.39,
  "raw_churn_probability": 3.35,
  "risk_score": 7.18,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "days_since_last_transaction",
      "value": 16
    },
    {
      "factor": "card_spend_change_30d",
      "value": -27.073
    },
    {
      "factor": "salary_missing_days",
      "value": 3.0
    },
    {
      "factor": "external_transfer_change_30d",
      "value": 16.8791
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
  "churn_probability": 18.53,
  "raw_churn_probability": 70.21,
  "probability_mode": "sigmoid",
  "risk_score": 64.1,
  "churn_prediction": "Yes",
  "risk_level": "Medium",
  "top_risk_factors": [
    {
      "factor": "latest_days_since_last_transaction",
      "value": 16,
      "message": "Customer has gone longer without transacting.",
      "contribution": 0.49040699005126953
    },
    {
      "factor": "latest_salary_missing_days",
      "value": 3.0,
      "message": "This signal increased churn risk.",
      "contribution": 0.2477962225675583
    },
    {
      "factor": "days_since_last_transaction_trend_6m",
      "value": 2.8,
      "message": "Customer has gone longer without transacting.",
      "contribution": 0.17365407943725586
    },
    {
      "factor": "latest_vs_avg_upi_share_of_spend_available_history",
      "value": 0.0475799999999999,
      "message": "This signal increased churn risk.",
      "contribution": 0.09531023353338242
    },
    {
      "factor": "latest_app_login_change_30d",
      "value": -34.1518,
      "message": "App usage has been falling across recent months.",
      "contribution": 0.09505008906126022
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
  "snapshot_date": "2026-05-01",
  "customer": {
    "age": 28,
    "tenure_months": 92,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 2,
    "has_credit_card": 1,
    "has_loan": 0,
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
    "emi_bounce_30d": 0,
    "branch_code": "BR-121",
    "card_colour": "green"
  },
  "actual_next_month_churn": 0
}
```

#### Model 1 Output

```json
{
  "churn_probability": 1.96,
  "raw_churn_probability": 1.61,
  "risk_score": 5.87,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "branch_code",
      "value": "BR-121"
    },
    {
      "factor": "app_login_change_30d",
      "value": 33.7548
    },
    {
      "factor": "age",
      "value": 28
    },
    {
      "factor": "products_dropped_90d",
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
  "churn_probability": 1.61,
  "raw_churn_probability": 13.63,
  "probability_mode": "sigmoid",
  "risk_score": 4.82,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "avg_balance_change_30d_6m",
      "value": 31.7589,
      "message": "This signal increased churn risk.",
      "contribution": 0.1033778116106987
    },
    {
      "factor": "latest_vs_avg_external_transfer_change_30d_available_history",
      "value": -41.49156000000001,
      "message": "This signal increased churn risk.",
      "contribution": 0.08516564965248108
    },
    {
      "factor": "card_spend_change_30d_trend_6m",
      "value": 10.2012,
      "message": "This signal increased churn risk.",
      "contribution": 0.05435176193714142
    },
    {
      "factor": "latest_vs_avg_app_login_change_30d_available_history",
      "value": 19.783140000000003,
      "message": "This signal increased churn risk.",
      "contribution": 0.03465104475617409
    },
    {
      "factor": "latest_upi_share_of_spend",
      "value": 0.4659,
      "message": "This signal increased churn risk.",
      "contribution": 0.03260818496346474
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
  "snapshot_date": "2026-05-01",
  "customer": {
    "age": 61,
    "tenure_months": 210,
    "customer_segment": "pension",
    "income_regularity": "regular",
    "products_count": 3,
    "has_credit_card": 0,
    "has_loan": 0,
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
    "emi_bounce_30d": 0,
    "branch_code": "BR-102",
    "card_colour": "blue"
  },
  "actual_next_month_churn": 1
}
```

#### Model 1 Output

```json
{
  "churn_probability": 53.85,
  "raw_churn_probability": 65.42,
  "risk_score": 82.69,
  "churn_prediction": "Yes",
  "risk_level": "High",
  "top_risk_factors": [
    {
      "factor": "balance_change_30d",
      "value": -56.6283
    },
    {
      "factor": "card_spend_change_30d",
      "value": -55.1619
    },
    {
      "factor": "days_since_last_transaction",
      "value": 20
    },
    {
      "factor": "salary_missing_days",
      "value": 6.0
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
  "churn_probability": 41.36,
  "raw_churn_probability": 94.52,
  "probability_mode": "sigmoid",
  "risk_score": 78.01,
  "churn_prediction": "Yes",
  "risk_level": "High",
  "top_risk_factors": [
    {
      "factor": "latest_days_since_last_transaction",
      "value": 20,
      "message": "Customer has gone longer without transacting.",
      "contribution": 0.6088116765022278
    },
    {
      "factor": "latest_transaction_change_30d",
      "value": -54.3925,
      "message": "Transaction activity has been falling across recent months.",
      "contribution": 0.45333972573280334
    },
    {
      "factor": "latest_salary_missing_days",
      "value": 6.0,
      "message": "This signal increased churn risk.",
      "contribution": 0.2567542791366577
    },
    {
      "factor": "latest_vs_avg_upi_share_of_spend_available_history",
      "value": 0.20452,
      "message": "This signal increased churn risk.",
      "contribution": 0.2536928355693817
    },
    {
      "factor": "latest_card_spend_change_30d",
      "value": -55.1619,
      "message": "Card spending has been falling across recent months.",
      "contribution": 0.2085566371679306
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
  "snapshot_date": "2026-05-01",
  "customer": {
    "age": 25,
    "tenure_months": 82,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 2,
    "has_credit_card": 0,
    "has_loan": 0,
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
    "emi_bounce_30d": 0,
    "branch_code": "BR-111",
    "card_colour": "silver"
  },
  "actual_next_month_churn": 0
}
```

#### Model 1 Output

```json
{
  "churn_probability": 1.96,
  "raw_churn_probability": 2.0,
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
      "factor": "products_count",
      "value": 2
    },
    {
      "factor": "customer_segment",
      "value": "salary"
    },
    {
      "factor": "upi_share_of_spend",
      "value": 0.3028
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
  "churn_probability": 2.31,
  "raw_churn_probability": 21.57,
  "probability_mode": "sigmoid",
  "risk_score": 6.92,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "avg_transaction_change_30d_6m",
      "value": 16.675800000000002,
      "message": "This signal increased churn risk.",
      "contribution": 0.023096978664398193
    },
    {
      "factor": "latest_vs_avg_external_transfer_change_30d_available_history",
      "value": -25.51472,
      "message": "This signal increased churn risk.",
      "contribution": 0.0221616942435503
    },
    {
      "factor": "max_days_since_last_transaction_3m",
      "value": 8.0,
      "message": "Customer has gone longer without transacting.",
      "contribution": 0.019972413778305054
    },
    {
      "factor": "max_salary_missing_days_6m",
      "value": 1.0,
      "message": "This signal increased churn risk.",
      "contribution": 0.011131723411381245
    },
    {
      "factor": "sum_products_dropped_90d_6m",
      "value": 2.0,
      "message": "This signal increased churn risk.",
      "contribution": 0.007810878101736307
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
  "snapshot_date": "2026-05-01",
  "customer": {
    "age": 47,
    "tenure_months": 74,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 2,
    "has_credit_card": 1,
    "has_loan": 0,
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
  "churn_probability": 0.0,
  "raw_churn_probability": 0.93,
  "risk_score": 0.0,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "card_colour",
      "value": "blue"
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
      "factor": "has_credit_card",
      "value": 1
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
  "churn_probability": 2.33,
  "raw_churn_probability": 21.79,
  "probability_mode": "sigmoid",
  "risk_score": 6.99,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "sum_fd_maturing_in_30d_3m",
      "value": 1.0,
      "message": "Customer has a fixed deposit maturing soon.",
      "contribution": 0.10836882144212723
    },
    {
      "factor": "avg_app_login_change_30d_6m",
      "value": -0.0403800000000003,
      "message": "App usage has been falling across recent months.",
      "contribution": 0.01649622619152069
    },
    {
      "factor": "avg_app_login_change_30d_3m",
      "value": -4.659866666666667,
      "message": "App usage has been falling across recent months.",
      "contribution": 0.01423698291182518
    },
    {
      "factor": "card_spend_change_30d_trend_6m",
      "value": -0.0227999999999999,
      "message": "Card spending has been falling across recent months.",
      "contribution": 0.009418151341378689
    },
    {
      "factor": "max_salary_missing_days_6m",
      "value": 1.0,
      "message": "This signal increased churn risk.",
      "contribution": 0.00932850781828165
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

### 35. Sudiksha Merchant (`C13601`)

#### Model 1 Input

```json
{
  "customer_id": "C13601",
  "customer_name": "Sudiksha Merchant",
  "snapshot_date": "2026-05-01",
  "customer": {
    "age": 41,
    "tenure_months": 87,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 2,
    "has_credit_card": 0,
    "has_loan": 1,
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
    "emi_bounce_30d": 0,
    "branch_code": "BR-117",
    "card_colour": "green"
  },
  "actual_next_month_churn": 0
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
  "churn_probability": 2.76,
  "raw_churn_probability": 25.55,
  "probability_mode": "sigmoid",
  "risk_score": 8.29,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "days_since_last_transaction_trend_6m",
      "value": 1.5000000000000002,
      "message": "Customer has gone longer without transacting.",
      "contribution": 0.11780404299497604
    },
    {
      "factor": "latest_upi_share_of_spend",
      "value": 0.5895,
      "message": "This signal increased churn risk.",
      "contribution": 0.04162773862481117
    },
    {
      "factor": "card_spend_change_30d_trend_6m",
      "value": 8.10218,
      "message": "This signal increased churn risk.",
      "contribution": 0.03871029242873192
    },
    {
      "factor": "external_transfer_change_30d_trend_6m",
      "value": 0.5001499999999965,
      "message": "External transfers have increased.",
      "contribution": 0.025633418932557106
    },
    {
      "factor": "latest_vs_avg_balance_change_30d_available_history",
      "value": -6.48498,
      "message": "Balance has been falling across recent months.",
      "contribution": 0.009123445488512516
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
  "snapshot_date": "2026-05-01",
  "customer": {
    "age": 52,
    "tenure_months": 144,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 2,
    "has_credit_card": 0,
    "has_loan": 0,
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
    "emi_bounce_30d": 0,
    "branch_code": "BR-104",
    "card_colour": "green"
  },
  "actual_next_month_churn": 0
}
```

#### Model 1 Output

```json
{
  "churn_probability": 2.39,
  "raw_churn_probability": 3.63,
  "risk_score": 7.18,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "card_spend_change_30d",
      "value": -29.6774
    },
    {
      "factor": "salary_missing_days",
      "value": 3.0
    },
    {
      "factor": "external_transfer_change_30d",
      "value": 8.2099
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
  "churn_probability": 15.94,
  "raw_churn_probability": 66.3,
  "probability_mode": "sigmoid",
  "risk_score": 53.74,
  "churn_prediction": "Yes",
  "risk_level": "Medium",
  "top_risk_factors": [
    {
      "factor": "latest_salary_missing_days",
      "value": 3.0,
      "message": "This signal increased churn risk.",
      "contribution": 0.2524355351924896
    },
    {
      "factor": "latest_vs_avg_upi_share_of_spend_available_history",
      "value": 0.07544,
      "message": "This signal increased churn risk.",
      "contribution": 0.1974029392004013
    },
    {
      "factor": "days_since_last_transaction_trend_6m",
      "value": 1.3999999999999986,
      "message": "Customer has gone longer without transacting.",
      "contribution": 0.175797700881958
    },
    {
      "factor": "latest_transaction_change_30d",
      "value": -19.9855,
      "message": "Transaction activity has been falling across recent months.",
      "contribution": 0.1246231272816658
    },
    {
      "factor": "transaction_change_30d_trend_6m",
      "value": -10.96859,
      "message": "Transaction activity has been falling across recent months.",
      "contribution": 0.09040725231170654
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
  "snapshot_date": "2026-05-01",
  "customer": {
    "age": 44,
    "tenure_months": 77,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 2,
    "has_credit_card": 1,
    "has_loan": 0,
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
    "emi_bounce_30d": 0,
    "branch_code": "BR-103",
    "card_colour": "blue"
  },
  "actual_next_month_churn": 0
}
```

#### Model 1 Output

```json
{
  "churn_probability": 7.29,
  "raw_churn_probability": 5.79,
  "risk_score": 21.86,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "salary_missing_days",
      "value": 4.0
    },
    {
      "factor": "balance_change_30d",
      "value": -27.0365
    },
    {
      "factor": "external_transfer_change_30d",
      "value": 3.9139
    },
    {
      "factor": "app_login_change_30d",
      "value": 9.2486
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
  "churn_probability": 9.23,
  "raw_churn_probability": 52.93,
  "probability_mode": "sigmoid",
  "risk_score": 27.69,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "latest_salary_missing_days",
      "value": 4.0,
      "message": "This signal increased churn risk.",
      "contribution": 0.2839606702327728
    },
    {
      "factor": "latest_avg_resolution_time_hrs",
      "value": 38.8653,
      "message": "This signal increased churn risk.",
      "contribution": 0.23475493490695953
    },
    {
      "factor": "latest_vs_avg_upi_share_of_spend_available_history",
      "value": 0.0579399999999999,
      "message": "This signal increased churn risk.",
      "contribution": 0.1838693469762802
    },
    {
      "factor": "latest_balance_change_30d",
      "value": -27.0365,
      "message": "Balance has been falling across recent months.",
      "contribution": 0.11057157069444656
    },
    {
      "factor": "external_transfer_change_30d_trend_6m",
      "value": 8.31287,
      "message": "External transfers have increased.",
      "contribution": 0.0219553392380476
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

### 39. Viraj Bhargava (`C13678`)

#### Model 1 Input

```json
{
  "customer_id": "C13678",
  "customer_name": "Viraj Bhargava",
  "snapshot_date": "2026-05-01",
  "customer": {
    "age": 34,
    "tenure_months": 172,
    "customer_segment": "farmer",
    "income_regularity": "seasonal",
    "products_count": 1,
    "has_credit_card": 0,
    "has_loan": 0,
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
    "emi_bounce_30d": 0,
    "branch_code": "BR-102",
    "card_colour": "black"
  },
  "actual_next_month_churn": 0
}
```

#### Model 1 Output

```json
{
  "churn_probability": 1.96,
  "raw_churn_probability": 2.67,
  "risk_score": 5.87,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "complaints_30d",
      "value": 2
    },
    {
      "factor": "branch_code",
      "value": "BR-102"
    },
    {
      "factor": "app_login_change_30d",
      "value": 31.1307
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
  "churn_probability": 2.24,
  "raw_churn_probability": 20.96,
  "probability_mode": "sigmoid",
  "risk_score": 6.73,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "count_quiet_customer_3m",
      "value": 2,
      "message": "This signal increased churn risk.",
      "contribution": 0.033674661070108414
    },
    {
      "factor": "card_spend_change_30d_trend_6m",
      "value": 4.938600000000002,
      "message": "This signal increased churn risk.",
      "contribution": 0.02744707465171814
    },
    {
      "factor": "count_external_transfer_rise_6m",
      "value": 0,
      "message": "This signal increased churn risk.",
      "contribution": 0.019301673397421837
    },
    {
      "factor": "sum_failed_transactions_30d_6m",
      "value": 5.0,
      "message": "Customer has recent failed transactions.",
      "contribution": 0.012634855695068836
    },
    {
      "factor": "latest_vs_avg_transaction_change_30d_available_history",
      "value": 11.65294,
      "message": "This signal increased churn risk.",
      "contribution": 0.010735691525042057
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

### 41. Anvi Banik (`C13933`)

#### Model 1 Input

```json
{
  "customer_id": "C13933",
  "customer_name": "Anvi Banik",
  "snapshot_date": "2026-05-01",
  "customer": {
    "age": 59,
    "tenure_months": 173,
    "customer_segment": "pension",
    "income_regularity": "regular",
    "products_count": 1,
    "has_credit_card": 0,
    "has_loan": 0,
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
    "emi_bounce_30d": 0,
    "branch_code": "BR-136",
    "card_colour": "silver"
  },
  "actual_next_month_churn": 0
}
```

#### Model 1 Output

```json
{
  "churn_probability": 1.16,
  "raw_churn_probability": 1.14,
  "risk_score": 3.49,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "external_transfer_change_30d",
      "value": 4.6725
    },
    {
      "factor": "products_count",
      "value": 1
    },
    {
      "factor": "customer_segment",
      "value": "pension"
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
  "churn_probability": 3.41,
  "raw_churn_probability": 30.22,
  "probability_mode": "sigmoid",
  "risk_score": 10.24,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "latest_vs_avg_upi_share_of_spend_available_history",
      "value": 0.10714,
      "message": "This signal increased churn risk.",
      "contribution": 0.17280597984790802
    },
    {
      "factor": "days_since_last_transaction_trend_6m",
      "value": 1.2999999999999994,
      "message": "Customer has gone longer without transacting.",
      "contribution": 0.11989424377679825
    },
    {
      "factor": "latest_upi_share_of_spend",
      "value": 0.7506,
      "message": "This signal increased churn risk.",
      "contribution": 0.030390769243240356
    },
    {
      "factor": "external_transfer_change_30d_trend_6m",
      "value": 3.17388,
      "message": "External transfers have increased.",
      "contribution": 0.026749489828944206
    },
    {
      "factor": "avg_app_login_change_30d_3m",
      "value": -4.399933333333332,
      "message": "App usage has been falling across recent months.",
      "contribution": 0.024654565379023552
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
  "snapshot_date": "2026-05-01",
  "customer": {
    "age": 25,
    "tenure_months": 61,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 3,
    "has_credit_card": 1,
    "has_loan": 1,
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
    "emi_bounce_30d": 0,
    "branch_code": "BR-140",
    "card_colour": "blue"
  },
  "actual_next_month_churn": 0
}
```

#### Model 1 Output

```json
{
  "churn_probability": 7.29,
  "raw_churn_probability": 7.22,
  "risk_score": 21.86,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "card_spend_change_30d",
      "value": -32.7405
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
      "factor": "age",
      "value": 25
    },
    {
      "factor": "branch_code",
      "value": "BR-140"
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
  "churn_probability": 20.47,
  "raw_churn_probability": 72.87,
  "probability_mode": "sigmoid",
  "risk_score": 70.18,
  "churn_prediction": "Yes",
  "risk_level": "Medium",
  "top_risk_factors": [
    {
      "factor": "latest_transaction_change_30d",
      "value": -25.5044,
      "message": "Transaction activity has been falling across recent months.",
      "contribution": 0.2262910008430481
    },
    {
      "factor": "days_since_last_transaction_trend_6m",
      "value": 2.9000000000000004,
      "message": "Customer has gone longer without transacting.",
      "contribution": 0.19526326656341553
    },
    {
      "factor": "latest_vs_avg_upi_share_of_spend_available_history",
      "value": 0.06902,
      "message": "This signal increased churn risk.",
      "contribution": 0.1827458292245865
    },
    {
      "factor": "transaction_change_30d_trend_6m",
      "value": -15.844480000000004,
      "message": "Transaction activity has been falling across recent months.",
      "contribution": 0.14246265590190887
    },
    {
      "factor": "latest_failed_transactions_30d",
      "value": 3,
      "message": "Customer has recent failed transactions.",
      "contribution": 0.08875423669815063
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

### 44. Urvi Devi (`C14228`)

#### Model 1 Input

```json
{
  "customer_id": "C14228",
  "customer_name": "Urvi Devi",
  "snapshot_date": "2026-05-01",
  "customer": {
    "age": 27,
    "tenure_months": 108,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 3,
    "has_credit_card": 1,
    "has_loan": 1,
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
    "emi_bounce_30d": 0,
    "branch_code": "BR-125",
    "card_colour": "silver"
  },
  "actual_next_month_churn": 0
}
```

#### Model 1 Output

```json
{
  "churn_probability": 1.96,
  "raw_churn_probability": 1.5,
  "risk_score": 5.87,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "branch_code",
      "value": "BR-125"
    },
    {
      "factor": "age",
      "value": 27
    },
    {
      "factor": "app_login_change_30d",
      "value": 14.7933
    },
    {
      "factor": "external_transfer_change_30d",
      "value": 47.3466
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
  "churn_probability": 2.36,
  "raw_churn_probability": 22.04,
  "probability_mode": "sigmoid",
  "risk_score": 7.07,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "sum_fd_maturing_in_30d_3m",
      "value": 1.0,
      "message": "Customer has a fixed deposit maturing soon.",
      "contribution": 0.05768587067723274
    },
    {
      "factor": "external_transfer_change_30d_trend_6m",
      "value": 9.02036,
      "message": "External transfers have increased.",
      "contribution": 0.030869191512465477
    },
    {
      "factor": "transaction_change_30d_trend_6m",
      "value": -2.495960000000001,
      "message": "Transaction activity has been falling across recent months.",
      "contribution": 0.01844465546309948
    },
    {
      "factor": "latest_vs_avg_card_spend_change_30d_available_history",
      "value": 6.612780000000001,
      "message": "This signal increased churn risk.",
      "contribution": 0.010901394300162792
    },
    {
      "factor": "sum_products_dropped_90d_6m",
      "value": 1.0,
      "message": "This signal increased churn risk.",
      "contribution": 0.0053376308642327785
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
  "snapshot_date": "2026-03-01",
  "customer": {
    "age": 60,
    "tenure_months": 134,
    "customer_segment": "pension",
    "income_regularity": "regular",
    "products_count": 2,
    "has_credit_card": 0,
    "has_loan": 0,
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
    "emi_bounce_30d": 0,
    "branch_code": "BR-115",
    "card_colour": "gold"
  },
  "actual_next_month_churn": 1
}
```

#### Model 1 Output

```json
{
  "churn_probability": 18.06,
  "raw_churn_probability": 20.28,
  "risk_score": 62.22,
  "churn_prediction": "Yes",
  "risk_level": "Medium",
  "top_risk_factors": [
    {
      "factor": "balance_change_30d",
      "value": -37.2213
    },
    {
      "factor": "fd_maturing_in_30d",
      "value": 1
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
      "factor": "customer_segment",
      "value": "pension"
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
  "churn_probability": 21.19,
  "raw_churn_probability": 73.81,
  "probability_mode": "sigmoid",
  "risk_score": 70.45,
  "churn_prediction": "Yes",
  "risk_level": "Medium",
  "top_risk_factors": [
    {
      "factor": "latest_salary_missing_days",
      "value": 4.0,
      "message": "This signal increased churn risk.",
      "contribution": 0.31699755787849426
    },
    {
      "factor": "latest_balance_change_30d",
      "value": -37.2213,
      "message": "Balance has been falling across recent months.",
      "contribution": 0.29161307215690613
    },
    {
      "factor": "days_since_last_transaction_trend_6m",
      "value": 3.4999999999999987,
      "message": "Customer has gone longer without transacting.",
      "contribution": 0.2264360934495926
    },
    {
      "factor": "latest_vs_avg_upi_share_of_spend_available_history",
      "value": 0.0862333333333333,
      "message": "This signal increased churn risk.",
      "contribution": 0.173005148768425
    },
    {
      "factor": "latest_transaction_change_30d",
      "value": -24.327,
      "message": "Transaction activity has been falling across recent months.",
      "contribution": 0.14965565502643585
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

### 47. Tanay Ramaswamy (`C14341`)

#### Model 1 Input

```json
{
  "customer_id": "C14341",
  "customer_name": "Tanay Ramaswamy",
  "snapshot_date": "2026-05-01",
  "customer": {
    "age": 29,
    "tenure_months": 24,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 3,
    "has_credit_card": 1,
    "has_loan": 1,
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
    "emi_bounce_30d": 0,
    "branch_code": "BR-103",
    "card_colour": "blue"
  },
  "actual_next_month_churn": 0
}
```

#### Model 1 Output

```json
{
  "churn_probability": 2.39,
  "raw_churn_probability": 3.23,
  "risk_score": 7.18,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "tenure_months",
      "value": 24
    },
    {
      "factor": "failed_transactions_30d",
      "value": 2
    },
    {
      "factor": "days_since_last_transaction",
      "value": 13
    },
    {
      "factor": "app_login_change_30d",
      "value": 10.4431
    },
    {
      "factor": "external_transfer_change_30d",
      "value": 16.5436
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
  "churn_probability": 7.35,
  "raw_churn_probability": 47.58,
  "probability_mode": "sigmoid",
  "risk_score": 22.04,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "latest_days_since_last_transaction",
      "value": 13,
      "message": "Customer has gone longer without transacting.",
      "contribution": 0.3354056775569916
    },
    {
      "factor": "count_quiet_customer_3m",
      "value": 3,
      "message": "This signal increased churn risk.",
      "contribution": 0.062102507799863815
    },
    {
      "factor": "external_transfer_change_30d_trend_6m",
      "value": 9.856780000000004,
      "message": "External transfers have increased.",
      "contribution": 0.03733833506703377
    },
    {
      "factor": "sum_failed_transactions_30d_3m",
      "value": 4.0,
      "message": "Customer has recent failed transactions.",
      "contribution": 0.036387111991643906
    },
    {
      "factor": "latest_vs_avg_balance_change_30d_available_history",
      "value": -11.95224,
      "message": "Balance has been falling across recent months.",
      "contribution": 0.030779793858528137
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

### 49. Viraj Kade (`C14404`)

#### Model 1 Input

```json
{
  "customer_id": "C14404",
  "customer_name": "Viraj Kade",
  "snapshot_date": "2026-05-01",
  "customer": {
    "age": 36,
    "tenure_months": 121,
    "customer_segment": "business",
    "income_regularity": "irregular",
    "products_count": 2,
    "has_credit_card": 0,
    "has_loan": 1,
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
    "emi_bounce_30d": 0,
    "branch_code": "BR-107",
    "card_colour": "gold"
  },
  "actual_next_month_churn": 0
}
```

#### Model 1 Output

```json
{
  "churn_probability": 3.74,
  "raw_churn_probability": 4.33,
  "risk_score": 11.21,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "fd_maturing_in_30d",
      "value": 1
    },
    {
      "factor": "failed_transactions_30d",
      "value": 2
    },
    {
      "factor": "branch_code",
      "value": "BR-107"
    },
    {
      "factor": "app_login_change_30d",
      "value": 33.8563
    },
    {
      "factor": "external_transfer_change_30d",
      "value": 16.2472
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
  "churn_probability": 4.67,
  "raw_churn_probability": 37.23,
  "probability_mode": "sigmoid",
  "risk_score": 14.0,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "latest_fd_maturing_in_30d",
      "value": 1,
      "message": "Customer has a fixed deposit maturing soon.",
      "contribution": 0.20898796617984772
    },
    {
      "factor": "latest_avg_resolution_time_hrs",
      "value": 29.9749,
      "message": "This signal increased churn risk.",
      "contribution": 0.15190808475017548
    },
    {
      "factor": "sum_fd_maturing_in_30d_3m",
      "value": 1.0,
      "message": "Customer has a fixed deposit maturing soon.",
      "contribution": 0.129082590341568
    },
    {
      "factor": "latest_vs_avg_upi_share_of_spend_available_history",
      "value": 0.04252,
      "message": "This signal increased churn risk.",
      "contribution": 0.08697360008955002
    },
    {
      "factor": "sum_failed_transactions_30d_3m",
      "value": 5.0,
      "message": "Customer has recent failed transactions.",
      "contribution": 0.030812421813607216
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
  "snapshot_date": "2026-03-01",
  "customer": {
    "age": 77,
    "tenure_months": 10,
    "customer_segment": "pension",
    "income_regularity": "regular",
    "products_count": 1,
    "has_credit_card": 0,
    "has_loan": 0,
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
  "churn_probability": 3.74,
  "raw_churn_probability": 4.24,
  "risk_score": 11.21,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "tenure_months",
      "value": 10
    },
    {
      "factor": "branch_code",
      "value": "BR-112"
    },
    {
      "factor": "days_since_last_transaction",
      "value": 14
    },
    {
      "factor": "age",
      "value": 77
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
  "churn_probability": 15.22,
  "raw_churn_probability": 65.13,
  "probability_mode": "sigmoid",
  "risk_score": 50.87,
  "churn_prediction": "Yes",
  "risk_level": "Medium",
  "top_risk_factors": [
    {
      "factor": "latest_days_since_last_transaction",
      "value": 14,
      "message": "Customer has gone longer without transacting.",
      "contribution": 0.44682130217552185
    },
    {
      "factor": "latest_avg_resolution_time_hrs",
      "value": 43.9839,
      "message": "This signal increased churn risk.",
      "contribution": 0.24838727712631226
    },
    {
      "factor": "transaction_change_30d_trend_6m",
      "value": -16.690350000000002,
      "message": "Transaction activity has been falling across recent months.",
      "contribution": 0.1343468874692917
    },
    {
      "factor": "days_since_last_transaction_trend_6m",
      "value": 2.9999999999999982,
      "message": "Customer has gone longer without transacting.",
      "contribution": 0.10742185264825821
    },
    {
      "factor": "max_avg_resolution_time_hrs_3m",
      "value": 43.9839,
      "message": "This signal increased churn risk.",
      "contribution": 0.05844960734248161
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
  "snapshot_date": "2026-05-01",
  "customer": {
    "age": 29,
    "tenure_months": 35,
    "customer_segment": "vendor",
    "income_regularity": "irregular",
    "products_count": 2,
    "has_credit_card": 0,
    "has_loan": 1,
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
    "emi_bounce_30d": 0,
    "branch_code": "BR-120",
    "card_colour": "silver"
  },
  "actual_next_month_churn": 0
}
```

#### Model 1 Output

```json
{
  "churn_probability": 7.29,
  "raw_churn_probability": 6.79,
  "risk_score": 21.86,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "card_spend_change_30d",
      "value": -33.1002
    },
    {
      "factor": "tenure_months",
      "value": 35
    },
    {
      "factor": "unresolved_complaints",
      "value": 1
    },
    {
      "factor": "avg_resolution_time_hrs",
      "value": 43.481
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
  "churn_probability": 6.0,
  "raw_churn_probability": 42.92,
  "probability_mode": "sigmoid",
  "risk_score": 18.0,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "latest_avg_resolution_time_hrs",
      "value": 43.481,
      "message": "This signal increased churn risk.",
      "contribution": 0.36555972695350647
    },
    {
      "factor": "external_transfer_change_30d_trend_6m",
      "value": 5.419010000000002,
      "message": "External transfers have increased.",
      "contribution": 0.042930085211992264
    },
    {
      "factor": "latest_upi_share_of_spend",
      "value": 0.7436,
      "message": "This signal increased churn risk.",
      "contribution": 0.04171092435717583
    },
    {
      "factor": "latest_card_spend_change_30d",
      "value": -33.1002,
      "message": "Card spending has been falling across recent months.",
      "contribution": 0.041340965777635574
    },
    {
      "factor": "max_avg_resolution_time_hrs_3m",
      "value": 43.481,
      "message": "This signal increased churn risk.",
      "contribution": 0.035134460777044296
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
  "snapshot_date": "2026-05-01",
  "customer": {
    "age": 49,
    "tenure_months": 100,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 1,
    "has_credit_card": 0,
    "has_loan": 0,
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
    "emi_bounce_30d": 0,
    "branch_code": "BR-119",
    "card_colour": "gold"
  },
  "actual_next_month_churn": 0
}
```

#### Model 1 Output

```json
{
  "churn_probability": 7.29,
  "raw_churn_probability": 8.58,
  "risk_score": 21.86,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
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
    },
    {
      "factor": "branch_code",
      "value": "BR-119"
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
  "churn_probability": 33.53,
  "raw_churn_probability": 87.32,
  "probability_mode": "sigmoid",
  "risk_score": 75.07,
  "churn_prediction": "Yes",
  "risk_level": "High",
  "top_risk_factors": [
    {
      "factor": "max_avg_resolution_time_hrs_3m",
      "value": 95.8305,
      "message": "This signal increased churn risk.",
      "contribution": 0.5756898522377014
    },
    {
      "factor": "latest_avg_resolution_time_hrs",
      "value": 41.834,
      "message": "This signal increased churn risk.",
      "contribution": 0.41567668318748474
    },
    {
      "factor": "sum_failed_transactions_30d_3m",
      "value": 8.0,
      "message": "Customer has recent failed transactions.",
      "contribution": 0.3379349410533905
    },
    {
      "factor": "latest_vs_avg_upi_share_of_spend_available_history",
      "value": 0.0493799999999999,
      "message": "This signal increased churn risk.",
      "contribution": 0.1685720533132553
    },
    {
      "factor": "sum_failed_transactions_30d_6m",
      "value": 12.0,
      "message": "Customer has recent failed transactions.",
      "contribution": 0.13757896423339844
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
  "snapshot_date": "2026-05-01",
  "customer": {
    "age": 37,
    "tenure_months": 147,
    "customer_segment": "farmer",
    "income_regularity": "seasonal",
    "products_count": 2,
    "has_credit_card": 0,
    "has_loan": 0,
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
    "emi_bounce_30d": 0,
    "branch_code": "BR-111",
    "card_colour": "gold"
  },
  "actual_next_month_churn": 0
}
```

#### Model 1 Output

```json
{
  "churn_probability": 2.39,
  "raw_churn_probability": 3.62,
  "risk_score": 7.18,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "balance_change_30d",
      "value": -37.4316
    },
    {
      "factor": "branch_code",
      "value": "BR-111"
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
  "churn_probability": 2.81,
  "raw_churn_probability": 25.89,
  "probability_mode": "sigmoid",
  "risk_score": 8.42,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "latest_balance_change_30d",
      "value": -37.4316,
      "message": "Balance has been falling across recent months.",
      "contribution": 0.22231249511241913
    },
    {
      "factor": "sum_fd_maturing_in_30d_3m",
      "value": 1.0,
      "message": "Customer has a fixed deposit maturing soon.",
      "contribution": 0.07899791747331619
    },
    {
      "factor": "latest_upi_share_of_spend",
      "value": 0.6853,
      "message": "This signal increased churn risk.",
      "contribution": 0.03755500540137291
    },
    {
      "factor": "card_spend_change_30d_trend_6m",
      "value": 9.594610000000008,
      "message": "This signal increased churn risk.",
      "contribution": 0.02755696140229702
    },
    {
      "factor": "avg_app_login_change_30d_3m",
      "value": -4.162566666666667,
      "message": "App usage has been falling across recent months.",
      "contribution": 0.021993229165673256
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
  "snapshot_date": "2026-05-01",
  "customer": {
    "age": 42,
    "tenure_months": 211,
    "customer_segment": "farmer",
    "income_regularity": "seasonal",
    "products_count": 4,
    "has_credit_card": 0,
    "has_loan": 1,
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
    "emi_bounce_30d": 0,
    "branch_code": "BR-102",
    "card_colour": "gold"
  },
  "actual_next_month_churn": 0
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
      "factor": "branch_code",
      "value": "BR-102"
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
  "churn_probability": 1.71,
  "raw_churn_probability": 15.02,
  "probability_mode": "sigmoid",
  "risk_score": 5.13,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "latest_upi_share_of_spend",
      "value": 0.4626,
      "message": "This signal increased churn risk.",
      "contribution": 0.03046652115881443
    },
    {
      "factor": "count_external_transfer_rise_6m",
      "value": 0,
      "message": "This signal increased churn risk.",
      "contribution": 0.014673036523163319
    },
    {
      "factor": "avg_app_login_change_30d_3m",
      "value": -5.8535,
      "message": "App usage has been falling across recent months.",
      "contribution": 0.010176117531955242
    },
    {
      "factor": "sum_products_dropped_90d_6m",
      "value": 1.0,
      "message": "This signal increased churn risk.",
      "contribution": 0.0075331092812120914
    },
    {
      "factor": "count_balance_drop_3m",
      "value": 0,
      "message": "This signal increased churn risk.",
      "contribution": 0.004414701368659735
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

### 56. Chanchal Khanna (`C15184`)

#### Model 1 Input

```json
{
  "customer_id": "C15184",
  "customer_name": "Chanchal Khanna",
  "snapshot_date": "2026-04-01",
  "customer": {
    "age": 45,
    "tenure_months": 122,
    "customer_segment": "business",
    "income_regularity": "irregular",
    "products_count": 3,
    "has_credit_card": 1,
    "has_loan": 1,
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
    "emi_bounce_30d": 1,
    "branch_code": "BR-138",
    "card_colour": "silver"
  },
  "actual_next_month_churn": 1
}
```

#### Model 1 Output

```json
{
  "churn_probability": 10.0,
  "raw_churn_probability": 13.07,
  "risk_score": 30.0,
  "churn_prediction": "Yes",
  "risk_level": "Medium",
  "top_risk_factors": [
    {
      "factor": "balance_change_30d",
      "value": -32.9477
    },
    {
      "factor": "card_spend_change_30d",
      "value": -46.0339
    },
    {
      "factor": "failed_transactions_30d",
      "value": 5
    },
    {
      "factor": "emi_bounce_30d",
      "value": 1
    },
    {
      "factor": "branch_code",
      "value": "BR-138"
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
  "churn_probability": 28.03,
  "raw_churn_probability": 81.77,
  "probability_mode": "sigmoid",
  "risk_score": 73.01,
  "churn_prediction": "Yes",
  "risk_level": "High",
  "top_risk_factors": [
    {
      "factor": "latest_days_since_last_transaction",
      "value": 14,
      "message": "Customer has gone longer without transacting.",
      "contribution": 0.43285417556762695
    },
    {
      "factor": "sum_failed_transactions_30d_3m",
      "value": 7.0,
      "message": "Customer has recent failed transactions.",
      "contribution": 0.2467239946126938
    },
    {
      "factor": "latest_card_spend_change_30d",
      "value": -46.0339,
      "message": "Card spending has been falling across recent months.",
      "contribution": 0.18671424686908722
    },
    {
      "factor": "latest_balance_change_30d",
      "value": -32.9477,
      "message": "Balance has been falling across recent months.",
      "contribution": 0.1829364150762558
    },
    {
      "factor": "days_since_last_transaction_trend_6m",
      "value": 1.1000000000000003,
      "message": "Customer has gone longer without transacting.",
      "contribution": 0.1609785407781601
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
  "snapshot_date": "2026-04-01",
  "customer": {
    "age": 50,
    "tenure_months": 221,
    "customer_segment": "farmer",
    "income_regularity": "seasonal",
    "products_count": 1,
    "has_credit_card": 0,
    "has_loan": 0,
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
    "emi_bounce_30d": 0,
    "branch_code": "BR-114",
    "card_colour": "black"
  },
  "actual_next_month_churn": 1
}
```

#### Model 1 Output

```json
{
  "churn_probability": 1.96,
  "raw_churn_probability": 2.55,
  "risk_score": 5.87,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "card_spend_change_30d",
      "value": -34.8954
    },
    {
      "factor": "branch_code",
      "value": "BR-114"
    },
    {
      "factor": "card_colour",
      "value": "black"
    },
    {
      "factor": "upi_share_of_spend",
      "value": 0.7777
    },
    {
      "factor": "external_transfer_change_30d",
      "value": 4.1474
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
  "churn_probability": 5.82,
  "raw_churn_probability": 42.25,
  "probability_mode": "sigmoid",
  "risk_score": 17.47,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "latest_vs_avg_external_transfer_change_30d_available_history",
      "value": -31.786200000000004,
      "message": "This signal increased churn risk.",
      "contribution": 0.17174583673477173
    },
    {
      "factor": "latest_transaction_change_30d",
      "value": -20.119,
      "message": "Transaction activity has been falling across recent months.",
      "contribution": 0.12405835837125778
    },
    {
      "factor": "count_balance_drop_3m",
      "value": 3,
      "message": "This signal increased churn risk.",
      "contribution": 0.07009764760732651
    },
    {
      "factor": "count_quiet_customer_3m",
      "value": 2,
      "message": "This signal increased churn risk.",
      "contribution": 0.06410031020641327
    },
    {
      "factor": "count_balance_drop_6m",
      "value": 4,
      "message": "This signal increased churn risk.",
      "contribution": 0.062349408864974976
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
  "snapshot_date": "2026-05-01",
  "customer": {
    "age": 30,
    "tenure_months": 60,
    "customer_segment": "vendor",
    "income_regularity": "irregular",
    "products_count": 2,
    "has_credit_card": 0,
    "has_loan": 0,
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
    "emi_bounce_30d": 0,
    "branch_code": "BR-110",
    "card_colour": "silver"
  },
  "actual_next_month_churn": 1
}
```

#### Model 1 Output

```json
{
  "churn_probability": 16.1,
  "raw_churn_probability": 15.99,
  "risk_score": 54.41,
  "churn_prediction": "Yes",
  "risk_level": "Medium",
  "top_risk_factors": [
    {
      "factor": "balance_change_30d",
      "value": -37.4282
    },
    {
      "factor": "card_spend_change_30d",
      "value": -37.7143
    },
    {
      "factor": "days_since_last_transaction",
      "value": 16
    },
    {
      "factor": "tenure_months",
      "value": 60
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
  "churn_probability": 35.55,
  "raw_churn_probability": 89.24,
  "probability_mode": "sigmoid",
  "risk_score": 75.83,
  "churn_prediction": "Yes",
  "risk_level": "High",
  "top_risk_factors": [
    {
      "factor": "latest_days_since_last_transaction",
      "value": 16,
      "message": "Customer has gone longer without transacting.",
      "contribution": 0.49141451716423035
    },
    {
      "factor": "latest_transaction_change_30d",
      "value": -31.73,
      "message": "Transaction activity has been falling across recent months.",
      "contribution": 0.23249077796936035
    },
    {
      "factor": "latest_vs_avg_upi_share_of_spend_available_history",
      "value": 0.1131599999999999,
      "message": "This signal increased churn risk.",
      "contribution": 0.21538054943084717
    },
    {
      "factor": "latest_balance_change_30d",
      "value": -37.4282,
      "message": "Balance has been falling across recent months.",
      "contribution": 0.21341848373413086
    },
    {
      "factor": "days_since_last_transaction_trend_6m",
      "value": 3.3999999999999995,
      "message": "Customer has gone longer without transacting.",
      "contribution": 0.212307408452034
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
  "snapshot_date": "2026-03-01",
  "customer": {
    "age": 43,
    "tenure_months": 58,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 2,
    "has_credit_card": 0,
    "has_loan": 0,
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
    "emi_bounce_30d": 0,
    "branch_code": "BR-115",
    "card_colour": "blue"
  },
  "actual_next_month_churn": 1
}
```

#### Model 1 Output

```json
{
  "churn_probability": 1.96,
  "raw_churn_probability": 2.11,
  "risk_score": 5.87,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "days_since_last_transaction",
      "value": 16
    },
    {
      "factor": "tenure_months",
      "value": 58
    },
    {
      "factor": "app_login_change_30d",
      "value": 43.4899
    },
    {
      "factor": "card_colour",
      "value": "blue"
    },
    {
      "factor": "upi_share_of_spend",
      "value": 0.39
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
  "churn_probability": 3.83,
  "raw_churn_probability": 32.79,
  "probability_mode": "sigmoid",
  "risk_score": 11.49,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "latest_days_since_last_transaction",
      "value": 16,
      "message": "Customer has gone longer without transacting.",
      "contribution": 0.44749531149864197
    },
    {
      "factor": "days_since_last_transaction_trend_6m",
      "value": 1.4999999999999984,
      "message": "Customer has gone longer without transacting.",
      "contribution": 0.07783112674951553
    },
    {
      "factor": "count_quiet_customer_3m",
      "value": 3,
      "message": "This signal increased churn risk.",
      "contribution": 0.04648369178175926
    },
    {
      "factor": "latest_vs_avg_external_transfer_change_30d_available_history",
      "value": -36.97023333333333,
      "message": "This signal increased churn risk.",
      "contribution": 0.045846059918403625
    },
    {
      "factor": "transaction_change_30d_trend_6m",
      "value": -3.18435,
      "message": "Transaction activity has been falling across recent months.",
      "contribution": 0.04052073881030083
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

### 61. Vasana Talwar (`C15682`)

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

### 62. Ekalinga Ram (`C15711`)

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

### 63. Karan De (`C15967`)

#### Model 1 Input

```json
{
  "customer_id": "C15967",
  "customer_name": "Karan De",
  "snapshot_date": "2026-01-01",
  "customer": {
    "age": 28,
    "tenure_months": 1,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 2,
    "has_credit_card": 1,
    "has_loan": 0,
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
    "emi_bounce_30d": 0,
    "branch_code": "BR-122",
    "card_colour": "black"
  },
  "actual_next_month_churn": 1
}
```

#### Model 1 Output

```json
{
  "churn_probability": 45.95,
  "raw_churn_probability": 52.32,
  "risk_score": 79.73,
  "churn_prediction": "Yes",
  "risk_level": "High",
  "top_risk_factors": [
    {
      "factor": "avg_resolution_time_hrs",
      "value": 70.5756
    },
    {
      "factor": "fd_maturing_in_30d",
      "value": 1
    },
    {
      "factor": "tenure_months",
      "value": 1
    },
    {
      "factor": "complaints_30d",
      "value": 6
    },
    {
      "factor": "days_since_last_transaction",
      "value": 17
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
  "churn_probability": 30.69,
  "raw_churn_probability": 84.52,
  "probability_mode": "sigmoid",
  "risk_score": 74.01,
  "churn_prediction": "Yes",
  "risk_level": "High",
  "top_risk_factors": [
    {
      "factor": "latest_avg_resolution_time_hrs",
      "value": 70.5756,
      "message": "This signal increased churn risk.",
      "contribution": 0.40570780634880066
    },
    {
      "factor": "max_avg_resolution_time_hrs_3m",
      "value": 70.5756,
      "message": "This signal increased churn risk.",
      "contribution": 0.3765343427658081
    },
    {
      "factor": "latest_days_since_last_transaction",
      "value": 17,
      "message": "Customer has gone longer without transacting.",
      "contribution": 0.19698010385036469
    },
    {
      "factor": "latest_salary_missing_days",
      "value": 3.0,
      "message": "This signal increased churn risk.",
      "contribution": 0.16922323405742645
    },
    {
      "factor": "latest_failed_transactions_30d",
      "value": 3,
      "message": "Customer has recent failed transactions.",
      "contribution": 0.13286028802394867
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
  "snapshot_date": "2026-02-01",
  "customer": {
    "age": 46,
    "tenure_months": 24,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 3,
    "has_credit_card": 0,
    "has_loan": 0,
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
    "emi_bounce_30d": 0,
    "branch_code": "BR-115",
    "card_colour": "gold"
  },
  "actual_next_month_churn": 1
}
```

#### Model 1 Output

```json
{
  "churn_probability": 16.1,
  "raw_churn_probability": 14.81,
  "risk_score": 54.41,
  "churn_prediction": "Yes",
  "risk_level": "Medium",
  "top_risk_factors": [
    {
      "factor": "balance_change_30d",
      "value": -37.4784
    },
    {
      "factor": "complaints_30d",
      "value": 3
    },
    {
      "factor": "tenure_months",
      "value": 24
    },
    {
      "factor": "salary_missing_days",
      "value": 3.0
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
  "churn_probability": 23.66,
  "raw_churn_probability": 76.86,
  "probability_mode": "sigmoid",
  "risk_score": 71.37,
  "churn_prediction": "Yes",
  "risk_level": "Medium",
  "top_risk_factors": [
    {
      "factor": "latest_salary_missing_days",
      "value": 3.0,
      "message": "This signal increased churn risk.",
      "contribution": 0.24166125059127808
    },
    {
      "factor": "latest_balance_change_30d",
      "value": -37.4784,
      "message": "Balance has been falling across recent months.",
      "contribution": 0.21977412700653076
    },
    {
      "factor": "latest_vs_avg_upi_share_of_spend_available_history",
      "value": 0.05655,
      "message": "This signal increased churn risk.",
      "contribution": 0.20794667303562164
    },
    {
      "factor": "days_since_last_transaction_trend_6m",
      "value": 7.999999999999998,
      "message": "Customer has gone longer without transacting.",
      "contribution": 0.18145646154880524
    },
    {
      "factor": "latest_transaction_change_30d",
      "value": -17.0302,
      "message": "Transaction activity has been falling across recent months.",
      "contribution": 0.17087209224700928
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
  "snapshot_date": "2026-05-01",
  "customer": {
    "age": 46,
    "tenure_months": 137,
    "customer_segment": "farmer",
    "income_regularity": "seasonal",
    "products_count": 1,
    "has_credit_card": 0,
    "has_loan": 0,
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
    "emi_bounce_30d": 0,
    "branch_code": "BR-101",
    "card_colour": "blue"
  },
  "actual_next_month_churn": 0
}
```

#### Model 1 Output

```json
{
  "churn_probability": 1.96,
  "raw_churn_probability": 1.55,
  "risk_score": 5.87,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "branch_code",
      "value": "BR-101"
    },
    {
      "factor": "upi_share_of_spend",
      "value": 0.177
    },
    {
      "factor": "app_login_change_30d",
      "value": 18.1534
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
  "churn_probability": 2.2,
  "raw_churn_probability": 20.55,
  "probability_mode": "sigmoid",
  "risk_score": 6.61,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "latest_vs_avg_balance_change_30d_available_history",
      "value": 24.36902,
      "message": "This signal increased churn risk.",
      "contribution": 0.0863020122051239
    },
    {
      "factor": "latest_vs_avg_external_transfer_change_30d_available_history",
      "value": -46.6933,
      "message": "This signal increased churn risk.",
      "contribution": 0.08621009439229965
    },
    {
      "factor": "avg_transaction_change_30d_6m",
      "value": 14.28166,
      "message": "This signal increased churn risk.",
      "contribution": 0.021021218970417976
    },
    {
      "factor": "avg_external_transfer_change_30d_6m",
      "value": -25.3302,
      "message": "This signal increased churn risk.",
      "contribution": 0.019087525084614754
    },
    {
      "factor": "count_external_transfer_rise_6m",
      "value": 0,
      "message": "This signal increased churn risk.",
      "contribution": 0.016077831387519836
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
  "snapshot_date": "2026-04-01",
  "customer": {
    "age": 62,
    "tenure_months": 131,
    "customer_segment": "farmer",
    "income_regularity": "seasonal",
    "products_count": 1,
    "has_credit_card": 0,
    "has_loan": 0,
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
    "emi_bounce_30d": 0,
    "branch_code": "BR-134",
    "card_colour": "gold"
  },
  "actual_next_month_churn": 1
}
```

#### Model 1 Output

```json
{
  "churn_probability": 2.39,
  "raw_churn_probability": 3.32,
  "risk_score": 7.18,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "balance_change_30d",
      "value": -24.3239
    },
    {
      "factor": "card_spend_change_30d",
      "value": -23.0036
    },
    {
      "factor": "branch_code",
      "value": "BR-134"
    },
    {
      "factor": "age",
      "value": 62
    },
    {
      "factor": "external_transfer_change_30d",
      "value": 40.7871
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
  "churn_probability": 19.42,
  "raw_churn_probability": 71.46,
  "probability_mode": "sigmoid",
  "risk_score": 67.7,
  "churn_prediction": "Yes",
  "risk_level": "Medium",
  "top_risk_factors": [
    {
      "factor": "latest_transaction_change_30d",
      "value": -48.0504,
      "message": "Transaction activity has been falling across recent months.",
      "contribution": 0.4851604402065277
    },
    {
      "factor": "days_since_last_transaction_trend_6m",
      "value": 2.1,
      "message": "Customer has gone longer without transacting.",
      "contribution": 0.2527863383293152
    },
    {
      "factor": "latest_balance_change_30d",
      "value": -24.3239,
      "message": "Balance has been falling across recent months.",
      "contribution": 0.19833378493785858
    },
    {
      "factor": "transaction_change_30d_trend_6m",
      "value": -20.44821,
      "message": "Transaction activity has been falling across recent months.",
      "contribution": 0.14821405708789825
    },
    {
      "factor": "latest_vs_avg_upi_share_of_spend_available_history",
      "value": 0.0407999999999999,
      "message": "This signal increased churn risk.",
      "contribution": 0.13397656381130219
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

### 68. Nikita Dugar (`C16218`)

#### Model 1 Input

```json
{
  "customer_id": "C16218",
  "customer_name": "Nikita Dugar",
  "snapshot_date": "2026-01-01",
  "customer": {
    "age": 29,
    "tenure_months": 77,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 2,
    "has_credit_card": 1,
    "has_loan": 0,
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
    "emi_bounce_30d": 0,
    "branch_code": "BR-134",
    "card_colour": "blue"
  },
  "actual_next_month_churn": 1
}
```

#### Model 1 Output

```json
{
  "churn_probability": 1.96,
  "raw_churn_probability": 2.46,
  "risk_score": 5.87,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "salary_missing_days",
      "value": 4.0
    },
    {
      "factor": "external_transfer_change_30d",
      "value": 13.7415
    },
    {
      "factor": "card_colour",
      "value": "blue"
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
  "churn_probability": 5.44,
  "raw_churn_probability": 40.69,
  "probability_mode": "sigmoid",
  "risk_score": 16.32,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "latest_salary_missing_days",
      "value": 4.0,
      "message": "This signal increased churn risk.",
      "contribution": 0.31890788674354553
    },
    {
      "factor": "latest_upi_share_of_spend",
      "value": 0.6983,
      "message": "This signal increased churn risk.",
      "contribution": 0.04117776080965996
    },
    {
      "factor": "avg_upi_share_of_spend_6m",
      "value": 0.6983,
      "message": "This signal increased churn risk.",
      "contribution": 0.038157302886247635
    },
    {
      "factor": "avg_upi_share_of_spend_3m",
      "value": 0.6983,
      "message": "This signal increased churn risk.",
      "contribution": 0.029062995687127113
    },
    {
      "factor": "external_transfer_change_30d_trend_6m",
      "value": 0.0,
      "message": "This signal increased churn risk.",
      "contribution": 0.026733217760920525
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
  "snapshot_date": "2026-05-01",
  "customer": {
    "age": 45,
    "tenure_months": 86,
    "customer_segment": "business",
    "income_regularity": "irregular",
    "products_count": 4,
    "has_credit_card": 1,
    "has_loan": 0,
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
    "emi_bounce_30d": 0,
    "branch_code": "BR-104",
    "card_colour": "green"
  },
  "actual_next_month_churn": 0
}
```

#### Model 1 Output

```json
{
  "churn_probability": 1.65,
  "raw_churn_probability": 1.24,
  "risk_score": 4.96,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "app_login_change_30d",
      "value": 13.6006
    },
    {
      "factor": "has_loan",
      "value": 0
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
  "churn_probability": 2.01,
  "raw_churn_probability": 18.58,
  "probability_mode": "sigmoid",
  "risk_score": 6.04,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "card_spend_change_30d_trend_6m",
      "value": 11.068450000000002,
      "message": "This signal increased churn risk.",
      "contribution": 0.05037986859679222
    },
    {
      "factor": "latest_upi_share_of_spend",
      "value": 0.5504,
      "message": "This signal increased churn risk.",
      "contribution": 0.048681262880563736
    },
    {
      "factor": "latest_vs_avg_external_transfer_change_30d_available_history",
      "value": -25.61894,
      "message": "This signal increased churn risk.",
      "contribution": 0.02582966350018978
    },
    {
      "factor": "avg_transaction_change_30d_6m",
      "value": 12.11536,
      "message": "This signal increased churn risk.",
      "contribution": 0.020729217678308487
    },
    {
      "factor": "max_avg_resolution_time_hrs_3m",
      "value": 43.9194,
      "message": "This signal increased churn risk.",
      "contribution": 0.01899307779967785
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
  "snapshot_date": "2026-04-01",
  "customer": {
    "age": 41,
    "tenure_months": 115,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 2,
    "has_credit_card": 1,
    "has_loan": 0,
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
    "emi_bounce_30d": 0,
    "branch_code": "BR-123",
    "card_colour": "silver"
  },
  "actual_next_month_churn": 1
}
```

#### Model 1 Output

```json
{
  "churn_probability": 3.74,
  "raw_churn_probability": 4.81,
  "risk_score": 11.21,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "days_since_last_transaction",
      "value": 20
    },
    {
      "factor": "balance_change_30d",
      "value": -21.2711
    },
    {
      "factor": "salary_missing_days",
      "value": 3.0
    },
    {
      "factor": "customer_segment",
      "value": "salary"
    },
    {
      "factor": "app_login_change_30d",
      "value": -10.3226
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
  "churn_probability": 35.68,
  "raw_churn_probability": 89.36,
  "probability_mode": "sigmoid",
  "risk_score": 75.88,
  "churn_prediction": "Yes",
  "risk_level": "High",
  "top_risk_factors": [
    {
      "factor": "latest_days_since_last_transaction",
      "value": 20,
      "message": "Customer has gone longer without transacting.",
      "contribution": 0.4781237542629242
    },
    {
      "factor": "latest_vs_avg_upi_share_of_spend_available_history",
      "value": 0.0686,
      "message": "This signal increased churn risk.",
      "contribution": 0.26214659214019775
    },
    {
      "factor": "max_avg_resolution_time_hrs_3m",
      "value": 73.4587,
      "message": "This signal increased churn risk.",
      "contribution": 0.2503737211227417
    },
    {
      "factor": "days_since_last_transaction_trend_6m",
      "value": 3.000000000000001,
      "message": "Customer has gone longer without transacting.",
      "contribution": 0.21252785623073578
    },
    {
      "factor": "latest_salary_missing_days",
      "value": 3.0,
      "message": "This signal increased churn risk.",
      "contribution": 0.19045709073543549
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
  "snapshot_date": "2026-05-01",
  "customer": {
    "age": 34,
    "tenure_months": 159,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 3,
    "has_credit_card": 1,
    "has_loan": 0,
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
    "emi_bounce_30d": 0,
    "branch_code": "BR-135",
    "card_colour": "gold"
  },
  "actual_next_month_churn": 0
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
      "factor": "complaints_30d",
      "value": 3
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
      "factor": "has_credit_card",
      "value": 1
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
  "churn_probability": 2.76,
  "raw_churn_probability": 25.54,
  "probability_mode": "sigmoid",
  "risk_score": 8.29,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "latest_vs_avg_upi_share_of_spend_available_history",
      "value": 0.0688999999999999,
      "message": "This signal increased churn risk.",
      "contribution": 0.16132231056690216
    },
    {
      "factor": "avg_transaction_change_30d_6m",
      "value": 16.138560000000002,
      "message": "This signal increased churn risk.",
      "contribution": 0.027743464335799217
    },
    {
      "factor": "latest_complaints_30d",
      "value": 3,
      "message": "Customer has recent complaint activity.",
      "contribution": 0.023838922381401062
    },
    {
      "factor": "count_external_transfer_rise_6m",
      "value": 0,
      "message": "This signal increased churn risk.",
      "contribution": 0.015646833926439285
    },
    {
      "factor": "sum_complaints_30d_3m",
      "value": 3.0,
      "message": "Customer has recent complaint activity.",
      "contribution": 0.015526440925896168
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
  "snapshot_date": "2026-05-01",
  "customer": {
    "age": 30,
    "tenure_months": 66,
    "customer_segment": "business",
    "income_regularity": "irregular",
    "products_count": 3,
    "has_credit_card": 1,
    "has_loan": 1,
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
    "emi_bounce_30d": 0,
    "branch_code": "BR-130",
    "card_colour": "green"
  },
  "actual_next_month_churn": 0
}
```

#### Model 1 Output

```json
{
  "churn_probability": 1.65,
  "raw_churn_probability": 1.21,
  "risk_score": 4.96,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "app_login_change_30d",
      "value": 13.6692
    },
    {
      "factor": "upi_share_of_spend",
      "value": 0.2131
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
  "churn_probability": 2.55,
  "raw_churn_probability": 23.8,
  "probability_mode": "sigmoid",
  "risk_score": 7.66,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "avg_balance_change_30d_6m",
      "value": 28.3303,
      "message": "This signal increased churn risk.",
      "contribution": 0.20032663643360138
    },
    {
      "factor": "avg_balance_change_30d_3m",
      "value": 35.5164,
      "message": "This signal increased churn risk.",
      "contribution": 0.07092425227165222
    },
    {
      "factor": "latest_vs_avg_external_transfer_change_30d_available_history",
      "value": -35.04704,
      "message": "This signal increased churn risk.",
      "contribution": 0.06399033963680267
    },
    {
      "factor": "card_spend_change_30d_trend_6m",
      "value": 7.364,
      "message": "This signal increased churn risk.",
      "contribution": 0.0627608373761177
    },
    {
      "factor": "avg_transaction_change_30d_6m",
      "value": 15.589759999999998,
      "message": "This signal increased churn risk.",
      "contribution": 0.04173754155635834
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

### 74. Elijah Mitra (`C16902`)

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

### 75. Unnati Date (`C17033`)

#### Model 1 Input

```json
{
  "customer_id": "C17033",
  "customer_name": "Unnati Date",
  "snapshot_date": "2026-02-01",
  "customer": {
    "age": 25,
    "tenure_months": 74,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 2,
    "has_credit_card": 1,
    "has_loan": 0,
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
    "emi_bounce_30d": 0,
    "branch_code": "BR-123",
    "card_colour": "green"
  },
  "actual_next_month_churn": 1
}
```

#### Model 1 Output

```json
{
  "churn_probability": 7.29,
  "raw_churn_probability": 6.03,
  "risk_score": 21.86,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "fd_maturing_in_30d",
      "value": 1
    },
    {
      "factor": "complaints_30d",
      "value": 2
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
      "factor": "days_since_last_transaction",
      "value": 14
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
  "churn_probability": 16.76,
  "raw_churn_probability": 67.6,
  "probability_mode": "sigmoid",
  "risk_score": 57.06,
  "churn_prediction": "Yes",
  "risk_level": "Medium",
  "top_risk_factors": [
    {
      "factor": "max_avg_resolution_time_hrs_3m",
      "value": 79.4238,
      "message": "This signal increased churn risk.",
      "contribution": 0.2935968041419983
    },
    {
      "factor": "latest_days_since_last_transaction",
      "value": 14,
      "message": "Customer has gone longer without transacting.",
      "contribution": 0.20679736137390137
    },
    {
      "factor": "latest_avg_resolution_time_hrs",
      "value": 29.0488,
      "message": "This signal increased churn risk.",
      "contribution": 0.12753863632678986
    },
    {
      "factor": "days_since_last_transaction_trend_6m",
      "value": 6.999999999999997,
      "message": "Customer has gone longer without transacting.",
      "contribution": 0.11225074529647827
    },
    {
      "factor": "latest_fd_maturing_in_30d",
      "value": 1,
      "message": "Customer has a fixed deposit maturing soon.",
      "contribution": 0.10022059828042984
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
  "snapshot_date": "2026-05-01",
  "customer": {
    "age": 33,
    "tenure_months": 12,
    "customer_segment": "vendor",
    "income_regularity": "irregular",
    "products_count": 3,
    "has_credit_card": 1,
    "has_loan": 1,
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
    "emi_bounce_30d": 0,
    "branch_code": "BR-117",
    "card_colour": "blue"
  },
  "actual_next_month_churn": 0
}
```

#### Model 1 Output

```json
{
  "churn_probability": 1.96,
  "raw_churn_probability": 2.62,
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
      "factor": "card_colour",
      "value": "blue"
    },
    {
      "factor": "external_transfer_change_30d",
      "value": 5.9423
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
  "churn_probability": 5.64,
  "raw_churn_probability": 41.5,
  "probability_mode": "sigmoid",
  "risk_score": 16.91,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "latest_transaction_change_30d",
      "value": -16.9041,
      "message": "Transaction activity has been falling across recent months.",
      "contribution": 0.17736510932445526
    },
    {
      "factor": "days_since_last_transaction_trend_6m",
      "value": 1.7000000000000002,
      "message": "Customer has gone longer without transacting.",
      "contribution": 0.1474694013595581
    },
    {
      "factor": "transaction_change_30d_trend_6m",
      "value": -10.016140000000004,
      "message": "Transaction activity has been falling across recent months.",
      "contribution": 0.08120033890008926
    },
    {
      "factor": "external_transfer_change_30d_trend_6m",
      "value": 5.273240000000001,
      "message": "External transfers have increased.",
      "contribution": 0.049585241824388504
    },
    {
      "factor": "balance_change_30d_trend_6m",
      "value": -7.3690800000000065,
      "message": "Balance has been falling across recent months.",
      "contribution": 0.03524574264883995
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
  "snapshot_date": "2026-05-01",
  "customer": {
    "age": 37,
    "tenure_months": 1,
    "customer_segment": "vendor",
    "income_regularity": "irregular",
    "products_count": 1,
    "has_credit_card": 0,
    "has_loan": 0,
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
  "churn_probability": 1.96,
  "raw_churn_probability": 2.09,
  "risk_score": 5.87,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "tenure_months",
      "value": 1
    },
    {
      "factor": "branch_code",
      "value": "BR-114"
    },
    {
      "factor": "external_transfer_change_30d",
      "value": 41.8846
    },
    {
      "factor": "products_count",
      "value": 1
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
  "churn_probability": 4.09,
  "raw_churn_probability": 34.24,
  "probability_mode": "sigmoid",
  "risk_score": 12.26,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "latest_vs_avg_upi_share_of_spend_available_history",
      "value": 0.0915599999999999,
      "message": "This signal increased churn risk.",
      "contribution": 0.18843378126621246
    },
    {
      "factor": "latest_upi_share_of_spend",
      "value": 0.711,
      "message": "This signal increased churn risk.",
      "contribution": 0.059897392988204956
    },
    {
      "factor": "external_transfer_change_30d_trend_6m",
      "value": 4.948770000000001,
      "message": "External transfers have increased.",
      "contribution": 0.031950946897268295
    },
    {
      "factor": "latest_vs_avg_balance_change_30d_available_history",
      "value": -17.211199999999998,
      "message": "Balance has been falling across recent months.",
      "contribution": 0.027851127088069916
    },
    {
      "factor": "transaction_change_30d_trend_6m",
      "value": -2.032020000000001,
      "message": "Transaction activity has been falling across recent months.",
      "contribution": 0.01903083175420761
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
  "snapshot_date": "2026-05-01",
  "customer": {
    "age": 80,
    "tenure_months": 80,
    "customer_segment": "pension",
    "income_regularity": "regular",
    "products_count": 2,
    "has_credit_card": 0,
    "has_loan": 0,
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
    "emi_bounce_30d": 0,
    "branch_code": "BR-114",
    "card_colour": "silver"
  },
  "actual_next_month_churn": 0
}
```

#### Model 1 Output

```json
{
  "churn_probability": 1.96,
  "raw_churn_probability": 2.11,
  "risk_score": 5.87,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "age",
      "value": 80
    },
    {
      "factor": "salary_missing_days",
      "value": 2.0
    },
    {
      "factor": "branch_code",
      "value": "BR-114"
    },
    {
      "factor": "failed_transactions_30d",
      "value": 2
    },
    {
      "factor": "external_transfer_change_30d",
      "value": 26.8166
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
  "churn_probability": 2.04,
  "raw_churn_probability": 18.89,
  "probability_mode": "sigmoid",
  "risk_score": 6.13,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "latest_salary_missing_days",
      "value": 2.0,
      "message": "This signal increased churn risk.",
      "contribution": 0.0397488959133625
    },
    {
      "factor": "avg_transaction_change_30d_6m",
      "value": 18.61562,
      "message": "This signal increased churn risk.",
      "contribution": 0.03962134197354317
    },
    {
      "factor": "external_transfer_change_30d_trend_6m",
      "value": 7.093679999999999,
      "message": "External transfers have increased.",
      "contribution": 0.0391262024641037
    },
    {
      "factor": "latest_upi_share_of_spend",
      "value": 0.4579,
      "message": "This signal increased churn risk.",
      "contribution": 0.025286803022027016
    },
    {
      "factor": "max_salary_missing_days_3m",
      "value": 2.0,
      "message": "This signal increased churn risk.",
      "contribution": 0.010864357464015484
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

### 80. Hemangini Nazareth (`C17880`)

#### Model 1 Input

```json
{
  "customer_id": "C17880",
  "customer_name": "Hemangini Nazareth",
  "snapshot_date": "2026-05-01",
  "customer": {
    "age": 40,
    "tenure_months": 13,
    "customer_segment": "vendor",
    "income_regularity": "irregular",
    "products_count": 1,
    "has_credit_card": 0,
    "has_loan": 0,
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
    "emi_bounce_30d": 0,
    "branch_code": "BR-132",
    "card_colour": "silver"
  },
  "actual_next_month_churn": 0
}
```

#### Model 1 Output

```json
{
  "churn_probability": 2.39,
  "raw_churn_probability": 3.4,
  "risk_score": 7.18,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "failed_transactions_30d",
      "value": 4
    },
    {
      "factor": "tenure_months",
      "value": 13
    },
    {
      "factor": "unresolved_complaints",
      "value": 1
    },
    {
      "factor": "upi_share_of_spend",
      "value": 0.0
    },
    {
      "factor": "app_login_change_30d",
      "value": 15.171
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
  "churn_probability": 2.68,
  "raw_churn_probability": 24.84,
  "probability_mode": "sigmoid",
  "risk_score": 8.03,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "latest_failed_transactions_30d",
      "value": 4,
      "message": "Customer has recent failed transactions.",
      "contribution": 0.1831824630498886
    },
    {
      "factor": "sum_failed_transactions_30d_6m",
      "value": 9.0,
      "message": "Customer has recent failed transactions.",
      "contribution": 0.1389920711517334
    },
    {
      "factor": "sum_failed_transactions_30d_3m",
      "value": 6.0,
      "message": "Customer has recent failed transactions.",
      "contribution": 0.11242606490850449
    },
    {
      "factor": "latest_upi_share_of_spend",
      "value": 0.0,
      "message": "This signal increased churn risk.",
      "contribution": 0.11097428947687149
    },
    {
      "factor": "avg_upi_share_of_spend_6m",
      "value": 0.0750599999999999,
      "message": "This signal increased churn risk.",
      "contribution": 0.017780421301722527
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

### 82. Sneha Mahajan (`C17950`)

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

### 83. Xiti Bath (`C17993`)

#### Model 1 Input

```json
{
  "customer_id": "C17993",
  "customer_name": "Xiti Bath",
  "snapshot_date": "2026-05-01",
  "customer": {
    "age": 35,
    "tenure_months": 81,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 1,
    "has_credit_card": 0,
    "has_loan": 0,
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
    "emi_bounce_30d": 0,
    "branch_code": "BR-113",
    "card_colour": "gold"
  },
  "actual_next_month_churn": 0
}
```

#### Model 1 Output

```json
{
  "churn_probability": 36.3,
  "raw_churn_probability": 36.27,
  "risk_score": 76.11,
  "churn_prediction": "Yes",
  "risk_level": "High",
  "top_risk_factors": [
    {
      "factor": "balance_change_30d",
      "value": -46.9603
    },
    {
      "factor": "salary_missing_days",
      "value": 5.0
    },
    {
      "factor": "card_spend_change_30d",
      "value": -44.0942
    },
    {
      "factor": "complaints_30d",
      "value": 2
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
  "churn_probability": 23.37,
  "raw_churn_probability": 76.51,
  "probability_mode": "sigmoid",
  "risk_score": 71.26,
  "churn_prediction": "Yes",
  "risk_level": "Medium",
  "top_risk_factors": [
    {
      "factor": "latest_salary_missing_days",
      "value": 5.0,
      "message": "This signal increased churn risk.",
      "contribution": 0.2893126308917999
    },
    {
      "factor": "latest_balance_change_30d",
      "value": -46.9603,
      "message": "Balance has been falling across recent months.",
      "contribution": 0.24829614162445068
    },
    {
      "factor": "latest_transaction_change_30d",
      "value": -34.0477,
      "message": "Transaction activity has been falling across recent months.",
      "contribution": 0.22423036396503448
    },
    {
      "factor": "latest_vs_avg_upi_share_of_spend_available_history",
      "value": 0.139,
      "message": "This signal increased churn risk.",
      "contribution": 0.19830544292926788
    },
    {
      "factor": "latest_card_spend_change_30d",
      "value": -44.0942,
      "message": "Card spending has been falling across recent months.",
      "contribution": 0.17719316482543945
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
  "snapshot_date": "2026-05-01",
  "customer": {
    "age": 61,
    "tenure_months": 1,
    "customer_segment": "pension",
    "income_regularity": "regular",
    "products_count": 1,
    "has_credit_card": 0,
    "has_loan": 0,
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
    "emi_bounce_30d": 0,
    "branch_code": "BR-102",
    "card_colour": "green"
  },
  "actual_next_month_churn": 0
}
```

#### Model 1 Output

```json
{
  "churn_probability": 1.96,
  "raw_churn_probability": 2.2,
  "risk_score": 5.87,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "tenure_months",
      "value": 1
    },
    {
      "factor": "branch_code",
      "value": "BR-102"
    },
    {
      "factor": "app_login_change_30d",
      "value": 21.6432
    },
    {
      "factor": "customer_segment",
      "value": "pension"
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
  "churn_probability": 2.81,
  "raw_churn_probability": 25.88,
  "probability_mode": "sigmoid",
  "risk_score": 8.42,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "latest_avg_resolution_time_hrs",
      "value": 41.5371,
      "message": "This signal increased churn risk.",
      "contribution": 0.27196863293647766
    },
    {
      "factor": "card_spend_change_30d_trend_6m",
      "value": 13.34251,
      "message": "This signal increased churn risk.",
      "contribution": 0.054232221096754074
    },
    {
      "factor": "latest_vs_avg_card_spend_change_30d_available_history",
      "value": 44.09284,
      "message": "This signal increased churn risk.",
      "contribution": 0.04288605973124504
    },
    {
      "factor": "latest_card_spend_change_30d",
      "value": 49.6778,
      "message": "This signal increased churn risk.",
      "contribution": 0.04120771959424019
    },
    {
      "factor": "latest_vs_avg_external_transfer_change_30d_available_history",
      "value": -26.8862,
      "message": "This signal increased churn risk.",
      "contribution": 0.0311286523938179
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

### 86. Warda Kalita (`C18307`)

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

### 87. Arin Pandya (`C18434`)

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

### 88. Mugdha Rajagopal (`C18699`)

#### Model 1 Input

```json
{
  "customer_id": "C18699",
  "customer_name": "Mugdha Rajagopal",
  "snapshot_date": "2026-03-01",
  "customer": {
    "age": 60,
    "tenure_months": 105,
    "customer_segment": "pension",
    "income_regularity": "regular",
    "products_count": 1,
    "has_credit_card": 0,
    "has_loan": 0,
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
    "emi_bounce_30d": 0,
    "branch_code": "BR-108",
    "card_colour": "green"
  },
  "actual_next_month_churn": 1
}
```

#### Model 1 Output

```json
{
  "churn_probability": 45.95,
  "raw_churn_probability": 48.21,
  "risk_score": 79.73,
  "churn_prediction": "Yes",
  "risk_level": "High",
  "top_risk_factors": [
    {
      "factor": "balance_change_30d",
      "value": -40.6452
    },
    {
      "factor": "card_spend_change_30d",
      "value": -55.6391
    },
    {
      "factor": "days_since_last_transaction",
      "value": 18
    },
    {
      "factor": "salary_missing_days",
      "value": 4.0
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
  "churn_probability": 36.27,
  "raw_churn_probability": 89.91,
  "probability_mode": "sigmoid",
  "risk_score": 76.1,
  "churn_prediction": "Yes",
  "risk_level": "High",
  "top_risk_factors": [
    {
      "factor": "latest_days_since_last_transaction",
      "value": 18,
      "message": "Customer has gone longer without transacting.",
      "contribution": 0.6196742653846741
    },
    {
      "factor": "latest_transaction_change_30d",
      "value": -36.2818,
      "message": "Transaction activity has been falling across recent months.",
      "contribution": 0.42009326815605164
    },
    {
      "factor": "latest_salary_missing_days",
      "value": 4.0,
      "message": "This signal increased churn risk.",
      "contribution": 0.26187029480934143
    },
    {
      "factor": "latest_vs_avg_upi_share_of_spend_available_history",
      "value": 0.0843,
      "message": "This signal increased churn risk.",
      "contribution": 0.24828247725963593
    },
    {
      "factor": "days_since_last_transaction_trend_6m",
      "value": 5.500000000000001,
      "message": "Customer has gone longer without transacting.",
      "contribution": 0.2137395739555359
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
  "snapshot_date": "2026-05-01",
  "customer": {
    "age": 80,
    "tenure_months": 136,
    "customer_segment": "pension",
    "income_regularity": "regular",
    "products_count": 2,
    "has_credit_card": 0,
    "has_loan": 0,
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
    "emi_bounce_30d": 0,
    "branch_code": "BR-125",
    "card_colour": "black"
  },
  "actual_next_month_churn": 0
}
```

#### Model 1 Output

```json
{
  "churn_probability": 1.93,
  "raw_churn_probability": 1.42,
  "risk_score": 5.8,
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
      "value": 35.5523
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
  "churn_probability": 5.45,
  "raw_churn_probability": 40.74,
  "probability_mode": "sigmoid",
  "risk_score": 16.35,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "max_avg_resolution_time_hrs_3m",
      "value": 64.4142,
      "message": "This signal increased churn risk.",
      "contribution": 0.3752117156982422
    },
    {
      "factor": "latest_vs_avg_upi_share_of_spend_available_history",
      "value": 0.0929799999999999,
      "message": "This signal increased churn risk.",
      "contribution": 0.23820579051971436
    },
    {
      "factor": "avg_card_spend_change_30d_3m",
      "value": -22.4089,
      "message": "Card spending has been falling across recent months.",
      "contribution": 0.06347939372062683
    },
    {
      "factor": "latest_upi_share_of_spend",
      "value": 0.6808,
      "message": "This signal increased churn risk.",
      "contribution": 0.04542364552617073
    },
    {
      "factor": "avg_card_spend_change_30d_6m",
      "value": -17.163339999999998,
      "message": "Card spending has been falling across recent months.",
      "contribution": 0.029804537072777748
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
  "snapshot_date": "2026-02-01",
  "customer": {
    "age": 54,
    "tenure_months": 33,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 4,
    "has_credit_card": 0,
    "has_loan": 0,
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
    "emi_bounce_30d": 0,
    "branch_code": "BR-130",
    "card_colour": "green"
  },
  "actual_next_month_churn": 1
}
```

#### Model 1 Output

```json
{
  "churn_probability": 1.96,
  "raw_churn_probability": 2.38,
  "risk_score": 5.87,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "tenure_months",
      "value": 33
    },
    {
      "factor": "salary_missing_days",
      "value": 2.0
    },
    {
      "factor": "external_transfer_change_30d",
      "value": 29.6508
    },
    {
      "factor": "upi_share_of_spend",
      "value": 0.3748
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
  "churn_probability": 7.39,
  "raw_churn_probability": 47.71,
  "probability_mode": "sigmoid",
  "risk_score": 22.16,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "latest_vs_avg_upi_share_of_spend_available_history",
      "value": 0.0545499999999999,
      "message": "This signal increased churn risk.",
      "contribution": 0.18946021795272827
    },
    {
      "factor": "transaction_change_30d_trend_6m",
      "value": -24.6505,
      "message": "Transaction activity has been falling across recent months.",
      "contribution": 0.1755145937204361
    },
    {
      "factor": "days_since_last_transaction_trend_6m",
      "value": 2.9999999999999987,
      "message": "Customer has gone longer without transacting.",
      "contribution": 0.11417274922132492
    },
    {
      "factor": "external_transfer_change_30d_trend_6m",
      "value": 34.96469999999999,
      "message": "External transfers have increased.",
      "contribution": 0.10375294834375381
    },
    {
      "factor": "latest_salary_missing_days",
      "value": 2.0,
      "message": "This signal increased churn risk.",
      "contribution": 0.05291576310992241
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
  "snapshot_date": "2026-02-01",
  "customer": {
    "age": 41,
    "tenure_months": 1,
    "customer_segment": "vendor",
    "income_regularity": "irregular",
    "products_count": 2,
    "has_credit_card": 0,
    "has_loan": 1,
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
    "emi_bounce_30d": 0,
    "branch_code": "BR-102",
    "card_colour": "silver"
  },
  "actual_next_month_churn": 1
}
```

#### Model 1 Output

```json
{
  "churn_probability": 7.29,
  "raw_churn_probability": 7.58,
  "risk_score": 21.86,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "tenure_months",
      "value": 1
    },
    {
      "factor": "days_since_last_transaction",
      "value": 15
    },
    {
      "factor": "branch_code",
      "value": "BR-102"
    },
    {
      "factor": "card_spend_change_30d",
      "value": -19.8748
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
  "churn_probability": 17.54,
  "raw_churn_probability": 68.77,
  "probability_mode": "sigmoid",
  "risk_score": 60.15,
  "churn_prediction": "Yes",
  "risk_level": "Medium",
  "top_risk_factors": [
    {
      "factor": "latest_days_since_last_transaction",
      "value": 15,
      "message": "Customer has gone longer without transacting.",
      "contribution": 0.48577797412872314
    },
    {
      "factor": "days_since_last_transaction_trend_6m",
      "value": 3.999999999999998,
      "message": "Customer has gone longer without transacting.",
      "contribution": 0.14029048383235931
    },
    {
      "factor": "transaction_change_30d_trend_6m",
      "value": -38.97149999999999,
      "message": "Transaction activity has been falling across recent months.",
      "contribution": 0.11890789866447449
    },
    {
      "factor": "external_transfer_change_30d_trend_6m",
      "value": 46.523499999999984,
      "message": "External transfers have increased.",
      "contribution": 0.07658470422029495
    },
    {
      "factor": "latest_vs_avg_balance_change_30d_available_history",
      "value": -17.435950000000002,
      "message": "Balance has been falling across recent months.",
      "contribution": 0.05901643633842468
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
  "snapshot_date": "2026-01-01",
  "customer": {
    "age": 51,
    "tenure_months": 163,
    "customer_segment": "business",
    "income_regularity": "irregular",
    "products_count": 4,
    "has_credit_card": 1,
    "has_loan": 1,
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
  "churn_probability": 2.39,
  "raw_churn_probability": 3.18,
  "risk_score": 7.18,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "card_spend_change_30d",
      "value": -38.579
    },
    {
      "factor": "branch_code",
      "value": "BR-109"
    },
    {
      "factor": "app_login_change_30d",
      "value": 11.8106
    },
    {
      "factor": "customer_segment",
      "value": "business"
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
  "churn_probability": 4.3,
  "raw_churn_probability": 35.38,
  "probability_mode": "sigmoid",
  "risk_score": 12.9,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "latest_transaction_change_30d",
      "value": -24.1358,
      "message": "Transaction activity has been falling across recent months.",
      "contribution": 0.17952857911586761
    },
    {
      "factor": "latest_card_spend_change_30d",
      "value": -38.579,
      "message": "Card spending has been falling across recent months.",
      "contribution": 0.09101048111915588
    },
    {
      "factor": "avg_card_spend_change_30d_6m",
      "value": -38.579,
      "message": "Card spending has been falling across recent months.",
      "contribution": 0.07028314471244812
    },
    {
      "factor": "avg_card_spend_change_30d_3m",
      "value": -38.579,
      "message": "Card spending has been falling across recent months.",
      "contribution": 0.06869029998779297
    },
    {
      "factor": "external_transfer_change_30d_trend_6m",
      "value": 0.0,
      "message": "This signal increased churn risk.",
      "contribution": 0.03576795384287834
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

### 94. Ekaraj Gokhale (`C19185`)

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

### 95. Aadhya Pal (`C19311`)

#### Model 1 Input

```json
{
  "customer_id": "C19311",
  "customer_name": "Aadhya Pal",
  "snapshot_date": "2026-05-01",
  "customer": {
    "age": 52,
    "tenure_months": 3,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 3,
    "has_credit_card": 0,
    "has_loan": 1,
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
    "emi_bounce_30d": 0,
    "branch_code": "BR-130",
    "card_colour": "black"
  },
  "actual_next_month_churn": 0
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
      "value": 22.3284
    },
    {
      "factor": "card_colour",
      "value": "black"
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
  "churn_probability": 2.09,
  "raw_churn_probability": 19.41,
  "probability_mode": "sigmoid",
  "risk_score": 6.27,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "sum_fd_maturing_in_30d_3m",
      "value": 1.0,
      "message": "Customer has a fixed deposit maturing soon.",
      "contribution": 0.07265264540910721
    },
    {
      "factor": "latest_external_transfer_change_30d",
      "value": -43.6231,
      "message": "This signal increased churn risk.",
      "contribution": 0.06406257301568985
    },
    {
      "factor": "card_spend_change_30d_trend_6m",
      "value": 6.41433,
      "message": "This signal increased churn risk.",
      "contribution": 0.041547346860170364
    },
    {
      "factor": "max_salary_missing_days_6m",
      "value": 0.0,
      "message": "This signal increased churn risk.",
      "contribution": 0.039660241454839706
    },
    {
      "factor": "latest_vs_avg_app_login_change_30d_available_history",
      "value": 8.82166,
      "message": "This signal increased churn risk.",
      "contribution": 0.020134305581450462
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

### 97. Hredhaan Bakshi (`C19434`)

#### Model 1 Input

```json
{
  "customer_id": "C19434",
  "customer_name": "Hredhaan Bakshi",
  "snapshot_date": "2026-04-01",
  "customer": {
    "age": 60,
    "tenure_months": 106,
    "customer_segment": "pension",
    "income_regularity": "regular",
    "products_count": 2,
    "has_credit_card": 0,
    "has_loan": 0,
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
    "emi_bounce_30d": 0,
    "branch_code": "BR-122",
    "card_colour": "green"
  },
  "actual_next_month_churn": 1
}
```

#### Model 1 Output

```json
{
  "churn_probability": 18.06,
  "raw_churn_probability": 22.19,
  "risk_score": 62.22,
  "churn_prediction": "Yes",
  "risk_level": "Medium",
  "top_risk_factors": [
    {
      "factor": "card_spend_change_30d",
      "value": -69.9076
    },
    {
      "factor": "fd_maturing_in_30d",
      "value": 1
    },
    {
      "factor": "salary_missing_days",
      "value": 5.0
    },
    {
      "factor": "branch_code",
      "value": "BR-122"
    },
    {
      "factor": "days_since_last_transaction",
      "value": 15
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
  "churn_probability": 27.34,
  "raw_churn_probability": 81.02,
  "probability_mode": "sigmoid",
  "risk_score": 72.75,
  "churn_prediction": "Yes",
  "risk_level": "High",
  "top_risk_factors": [
    {
      "factor": "latest_days_since_last_transaction",
      "value": 15,
      "message": "Customer has gone longer without transacting.",
      "contribution": 0.4762691557407379
    },
    {
      "factor": "latest_salary_missing_days",
      "value": 5.0,
      "message": "This signal increased churn risk.",
      "contribution": 0.37432149052619934
    },
    {
      "factor": "latest_card_spend_change_30d",
      "value": -69.9076,
      "message": "Card spending has been falling across recent months.",
      "contribution": 0.22100798785686493
    },
    {
      "factor": "days_since_last_transaction_trend_6m",
      "value": 3.5,
      "message": "Customer has gone longer without transacting.",
      "contribution": 0.1796194314956665
    },
    {
      "factor": "latest_app_login_change_30d",
      "value": -42.1416,
      "message": "App usage has been falling across recent months.",
      "contribution": 0.09559303522109985
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
  "snapshot_date": "2026-05-01",
  "customer": {
    "age": 45,
    "tenure_months": 42,
    "customer_segment": "vendor",
    "income_regularity": "irregular",
    "products_count": 3,
    "has_credit_card": 0,
    "has_loan": 1,
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
    "emi_bounce_30d": 0,
    "branch_code": "BR-125",
    "card_colour": "silver"
  },
  "actual_next_month_churn": 1
}
```

#### Model 1 Output

```json
{
  "churn_probability": 95.65,
  "raw_churn_probability": 86.84,
  "risk_score": 98.37,
  "churn_prediction": "Yes",
  "risk_level": "High",
  "top_risk_factors": [
    {
      "factor": "balance_change_30d",
      "value": -71.1168
    },
    {
      "factor": "days_since_last_transaction",
      "value": 31
    },
    {
      "factor": "card_spend_change_30d",
      "value": -63.3862
    },
    {
      "factor": "failed_transactions_30d",
      "value": 4
    },
    {
      "factor": "complaints_30d",
      "value": 4
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
  "churn_probability": 37.79,
  "raw_churn_probability": 91.31,
  "probability_mode": "sigmoid",
  "risk_score": 76.67,
  "churn_prediction": "Yes",
  "risk_level": "High",
  "top_risk_factors": [
    {
      "factor": "latest_days_since_last_transaction",
      "value": 31,
      "message": "Customer has gone longer without transacting.",
      "contribution": 0.674877941608429
    },
    {
      "factor": "latest_transaction_change_30d",
      "value": -48.4555,
      "message": "Transaction activity has been falling across recent months.",
      "contribution": 0.43102338910102844
    },
    {
      "factor": "latest_balance_change_30d",
      "value": -71.1168,
      "message": "Balance has been falling across recent months.",
      "contribution": 0.2090490609407425
    },
    {
      "factor": "latest_card_spend_change_30d",
      "value": -63.3862,
      "message": "Card spending has been falling across recent months.",
      "contribution": 0.19028949737548828
    },
    {
      "factor": "days_since_last_transaction_trend_6m",
      "value": 4.199999999999998,
      "message": "Customer has gone longer without transacting.",
      "contribution": 0.17050057649612427
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
  "snapshot_date": "2026-05-01",
  "customer": {
    "age": 60,
    "tenure_months": 1,
    "customer_segment": "business",
    "income_regularity": "irregular",
    "products_count": 4,
    "has_credit_card": 1,
    "has_loan": 1,
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
    "emi_bounce_30d": 1,
    "branch_code": "BR-107",
    "card_colour": "green"
  },
  "actual_next_month_churn": 0
}
```

#### Model 1 Output

```json
{
  "churn_probability": 1.96,
  "raw_churn_probability": 2.63,
  "risk_score": 5.87,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "tenure_months",
      "value": 1
    },
    {
      "factor": "emi_bounce_30d",
      "value": 1
    },
    {
      "factor": "failed_transactions_30d",
      "value": 2
    },
    {
      "factor": "app_login_change_30d",
      "value": 21.1561
    },
    {
      "factor": "upi_share_of_spend",
      "value": 0.1677
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
  "churn_probability": 2.88,
  "raw_churn_probability": 26.47,
  "probability_mode": "sigmoid",
  "risk_score": 8.65,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "avg_upi_share_of_spend_6m",
      "value": 0.27096,
      "message": "This signal increased churn risk.",
      "contribution": 0.045292239636182785
    },
    {
      "factor": "latest_external_transfer_change_30d",
      "value": -66.4893,
      "message": "This signal increased churn risk.",
      "contribution": 0.040651097893714905
    },
    {
      "factor": "latest_vs_avg_external_transfer_change_30d_available_history",
      "value": -46.74636,
      "message": "This signal increased churn risk.",
      "contribution": 0.032833531498909
    },
    {
      "factor": "count_external_transfer_rise_6m",
      "value": 0,
      "message": "This signal increased churn risk.",
      "contribution": 0.02110993303358555
    },
    {
      "factor": "latest_vs_avg_app_login_change_30d_available_history",
      "value": 16.81216,
      "message": "This signal increased churn risk.",
      "contribution": 0.014569259248673916
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
  "snapshot_date": "2026-05-01",
  "customer": {
    "age": 32,
    "tenure_months": 70,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 1,
    "has_credit_card": 0,
    "has_loan": 0,
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
    "emi_bounce_30d": 0,
    "branch_code": "BR-107",
    "card_colour": "green"
  },
  "actual_next_month_churn": 0
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
      "factor": "branch_code",
      "value": "BR-107"
    },
    {
      "factor": "products_count",
      "value": 1
    },
    {
      "factor": "upi_share_of_spend",
      "value": 0.4065
    },
    {
      "factor": "card_colour",
      "value": "green"
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
  "churn_probability": 2.36,
  "raw_churn_probability": 22.03,
  "probability_mode": "sigmoid",
  "risk_score": 7.07,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    {
      "factor": "latest_vs_avg_balance_change_30d_available_history",
      "value": -16.67342,
      "message": "Balance has been falling across recent months.",
      "contribution": 0.025081222876906395
    },
    {
      "factor": "latest_vs_avg_upi_share_of_spend_available_history",
      "value": 0.0211399999999999,
      "message": "This signal increased churn risk.",
      "contribution": 0.023951062932610512
    },
    {
      "factor": "max_days_since_last_transaction_3m",
      "value": 11.0,
      "message": "Customer has gone longer without transacting.",
      "contribution": 0.018974555656313896
    },
    {
      "factor": "avg_app_login_change_30d_6m",
      "value": -0.95828,
      "message": "App usage has been falling across recent months.",
      "contribution": 0.014090784825384617
    },
    {
      "factor": "latest_vs_avg_card_spend_change_30d_available_history",
      "value": 5.331539999999999,
      "message": "This signal increased churn risk.",
      "contribution": 0.01381944864988327
    }
  ]
}
```
