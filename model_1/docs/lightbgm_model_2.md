# LightGBM Model 2

This file explains LightGBM model 2 in simple points.

## 1. What It Predicts

- It predicts customer churn.
- Churn means the customer may stop actively using the bank.
- It uses the same dataset and same input columns as XGBoost.

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
model_1/training_scripts/lightgbm_model2/train_lightgbm.py
```

Run from project root:

```powershell
python model_1\training_scripts\lightgbm_model2\train_lightgbm.py
```

Training steps:

1. Read the dataset.
2. Remove columns that should not be model inputs.
3. Split customers into train, validation, and test.
4. Try 6 LightGBM parameter sets.
5. Pick the one with best validation PR-AUC.
6. Save model files into `model_1/training_scripts/lightgbm_model2/artifacts/`.
7. Test the model on unseen test data.

## 4. Input Columns

The model uses these 24 input fields:

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

## 5. Example Input

```json
{
  "age": 42,
  "tenure_months": 126,
  "customer_segment": "salary",
  "income_regularity": "regular",
  "products_count": 4,
  "has_credit_card": 1,
  "has_loan": 1,
  "days_since_last_transaction": 2,
  "balance_change_30d": 18,
  "transaction_change_30d": 12,
  "card_spend_change_30d": 16,
  "app_login_change_30d": 10,
  "salary_missing_days": 0,
  "external_transfer_change_30d": -12,
  "upi_share_of_spend": 0.35,
  "fd_maturing_in_30d": 0,
  "products_dropped_90d": 0,
  "complaints_30d": 0,
  "unresolved_complaints": 0,
  "failed_transactions_30d": 0,
  "avg_resolution_time_hrs": 0.0,
  "emi_bounce_30d": 0,
  "branch_code": "BR-118",
  "card_colour": "blue"
}
```

## 6. Example Output

```json
{
  "churn_probability": 0.0,
  "risk_score": 0.0,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    { "factor": "income_regularity", "value": "regular" }
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

## 9. Best Model Parameters

LightGBM model 2 tested 6 parameter sets. The best one was candidate 4.

```python
LGBMClassifier(
    objective="binary",
    metric="average_precision",
    n_estimators=3000,
    random_state=42,
    n_jobs=-1,
    verbose=-1,
    subsample_freq=1,
    learning_rate=0.025,
    num_leaves=12,
    max_depth=3,
    min_child_samples=60,
    subsample=0.95,
    colsample_bytree=0.85,
    reg_alpha=0.0,
    reg_lambda=3.0
)
```

Simple explanation:

| Parameter | Meaning |
|---|---|
| `objective` | two-class prediction: churn or not churn |
| `metric` | score used while training |
| `n_estimators` | maximum number of trees |
| `random_state` | makes results repeatable |
| `n_jobs` | uses CPU cores |
| `verbose` | hides extra training logs |
| `subsample_freq` | tells LightGBM to use row sampling |
| `learning_rate` | how slowly the model learns |
| `num_leaves` | controls tree complexity |
| `max_depth` | maximum tree depth |
| `min_child_samples` | avoids tiny weak branches |
| `subsample` | uses part of rows per tree |
| `colsample_bytree` | uses part of columns per tree |
| `reg_alpha` | simplicity penalty |
| `reg_lambda` | simplicity penalty |

## 10. Accuracy And Metrics

Test results:

| Metric | Value | Simple Meaning |
|---|---:|---|
| Accuracy | 92.43% | total correct predictions |
| Precision | 41.02% | risky predictions that were truly churn |
| Recall | 58.91% | real churners found by the model |
| ROC-AUC | 83.01% | ranking quality |
| PR-AUC | 44.26% | useful rare-churn score |

Note:

Accuracy is high because most customers do not churn. Precision, recall, ROC-AUC, and PR-AUC are more useful here.

## 11. How To Test Prediction

Run:

```powershell
python model_1\training_scripts\lightgbm_model2\test_prediction.py
```

## 12. Simple Summary

- LightGBM model 2 is the backup/comparison model.
- It uses the same 24 input fields as XGBoost.
- It has slightly higher precision and accuracy on the test set.
- It also returns `risk_score` for the dashboard.
- It is useful for comparing whether XGBoost predictions look reasonable.
