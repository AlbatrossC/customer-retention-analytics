# XGBoost

This file explains the XGBoost model in simple points.

## 1. What It Predicts

- It predicts customer churn.
- Churn means the customer may stop actively using the bank.
- The answer column during training is `churn_flag`.

| Value | Meaning |
|---:|---|
| `0` | customer stayed |
| `1` | customer churned |

## 2. Training Dataset

Dataset:

```text
model_1/data/customers.csv
```

Simple dataset facts:

- 10,000 customers
- 53,040 rows
- 31 columns
- about 6% churn rate
- synthetic data, not real customer data

Split:

| Split | Customers | Rows | Churn Rate |
|---|---:|---:|---:|
| Train | 7,000 | 37,132 | 6.00% |
| Validation | 1,500 | 7,987 | 5.98% |
| Test | 1,500 | 7,921 | 6.02% |

## 3. How It Is Trained

Training file:

```text
model_1/training_scripts/xgboost_model1/train_xgboost.py
```

Run from project root:

```powershell
python model_1\training_scripts\xgboost_model1\train_xgboost.py
```

Training steps:

1. Read the dataset.
2. Remove columns that should not be model inputs.
3. Split customers into train, validation, and test.
4. Train XGBoost on train data.
5. Use validation data to stop training at the right time.
6. Save model files into `model_1/training_scripts/xgboost_model1/artifacts/`.
7. Test the model on unseen test data.

## 4. Input Columns

The model uses 24 input fields:

```text
age
tenure_months
customer_segment
income_regularity
products_count
has_credit_card
has_loan
days_since_last_transaction
balance_change_30d
transaction_change_30d
card_spend_change_30d
app_login_change_30d
salary_missing_days
external_transfer_change_30d
upi_share_of_spend
fd_maturing_in_30d
products_dropped_90d
complaints_30d
unresolved_complaints
failed_transactions_30d
avg_resolution_time_hrs
emi_bounce_30d
branch_code
card_colour
```

These columns are not used as inputs:

```text
customer_id
customer_name
snapshot_date
loyalty
customer_yearly_value
complaint_text
churn_flag
```

Simple reason:

- `churn_flag` is the answer.
- ID and name can cause memorization.
- hidden or extra fields can make the score unrealistic.

## 5. Example Input

```json
{
  "age": 34,
  "tenure_months": 48,
  "customer_segment": "salary",
  "income_regularity": "regular",
  "products_count": 3,
  "has_credit_card": 1,
  "has_loan": 1,
  "days_since_last_transaction": 28,
  "balance_change_30d": -48,
  "transaction_change_30d": -55,
  "card_spend_change_30d": -62,
  "app_login_change_30d": -70,
  "salary_missing_days": 7,
  "external_transfer_change_30d": 95,
  "upi_share_of_spend": 0.82,
  "fd_maturing_in_30d": 0,
  "products_dropped_90d": 2,
  "complaints_30d": 3,
  "unresolved_complaints": 2,
  "failed_transactions_30d": 5,
  "avg_resolution_time_hrs": 64.0,
  "emi_bounce_30d": 1,
  "branch_code": "BR-124",
  "card_colour": "gold"
}
```

## 6. Example Output

```json
{
  "churn_probability": 100.0,
  "risk_score": 100.0,
  "churn_prediction": "Yes",
  "risk_level": "High",
  "top_risk_factors": [
    { "factor": "balance_change_30d", "value": -48 },
    { "factor": "card_spend_change_30d", "value": -62 },
    { "factor": "days_since_last_transaction", "value": 28 },
    { "factor": "salary_missing_days", "value": 7 },
    { "factor": "complaints_30d", "value": 3 }
  ]
}
```

## 7. Output Meaning

| Output | Simple Meaning |
|---|---|
| `churn_probability` | real churn chance from the model |
| `risk_score` | dashboard score from 0 to 100 |
| `churn_prediction` | `Yes` if churn probability is at least 10% |
| `risk_level` | Low, Medium, or High |
| `top_risk_factors` | main reasons risk went up |

## 8. Risk Rules

| Churn Probability | Prediction | Risk Level | Risk Score |
|---:|---|---|---:|
| below 10% | No | Low | 0 to below 30 |
| 10% to below 20% | Yes | Medium | 30 to below 70 |
| 20% and above | Yes | High | 70 to 100 |

## 9. Model Parameters

```python
XGBClassifier(
    objective="binary:logistic",
    eval_metric="aucpr",
    enable_categorical=True,
    tree_method="hist",
    n_estimators=900,
    learning_rate=0.03,
    max_depth=3,
    min_child_weight=8,
    subsample=0.85,
    colsample_bytree=0.85,
    reg_alpha=0.2,
    reg_lambda=4.0,
    gamma=0.5,
    random_state=42,
    n_jobs=-1,
    early_stopping_rounds=50
)
```

Simple explanation:

| Parameter | Meaning |
|---|---|
| `objective` | two-class prediction: churn or not churn |
| `eval_metric` | score used while training |
| `enable_categorical` | allows text categories like segment |
| `tree_method` | faster training method |
| `n_estimators` | maximum number of trees |
| `learning_rate` | how slowly the model learns |
| `max_depth` | how deep each tree can be |
| `min_child_weight` | avoids tiny weak branches |
| `subsample` | uses only part of rows per tree |
| `colsample_bytree` | uses only part of columns per tree |
| `reg_alpha` | keeps model simpler |
| `reg_lambda` | keeps model simpler |
| `gamma` | only allows useful splits |
| `random_state` | makes results repeatable |
| `n_jobs` | uses CPU cores |
| `early_stopping_rounds` | stops when validation score stops improving |

## 10. Accuracy And Metrics

Test results:

| Metric | Value | Simple Meaning |
|---|---:|---|
| Accuracy | 91.82% | total correct predictions |
| Precision | 38.43% | risky predictions that were truly churn |
| Recall | 59.54% | real churners found by the model |
| ROC-AUC | 83.32% | ranking quality |
| PR-AUC | 44.73% | useful rare-churn score |

Note:

Accuracy is high because most customers do not churn. Precision, recall, ROC-AUC, and PR-AUC are more useful here.

## 11. How To Test Prediction

Run:

```powershell
python model_1\training_scripts\xgboost_model1\test_prediction.py
```

## 12. Simple Summary

- XGBoost is the main churn model.
- It uses 24 customer behavior fields.
- It predicts churn probability.
- It also returns a dashboard-friendly risk score.
- Falling balance, low activity, late salary, complaints, and failed transactions increase risk.
