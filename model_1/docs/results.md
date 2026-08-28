# Model Results

This file compares the two models kept in the project:

- XGBoost
- LightGBM model 2

The dataset was not changed.

## 1. Dataset

Both models use the same dataset:

```text
model_1/data/customers.csv
```

Simple meaning:

- This is synthetic bank customer data.
- It has 10,000 customers.
- It has 53,040 monthly customer rows.
- Churn rate is about 6%.
- `churn_flag = 1` means the customer churned.
- `churn_flag = 0` means the customer stayed.

## 2. Test Results

These results are from the unseen test set.

| Model | Accuracy | Precision | Recall | ROC-AUC | PR-AUC | Flagged Rows |
|---|---:|---:|---:|---:|---:|---:|
| XGBoost | 91.82% | 38.43% | 59.54% | 83.32% | 44.73% | 739 |
| LightGBM model 2 | 92.43% | 41.02% | 58.91% | 83.01% | 44.26% | 685 |

Simple explanation:

| Metric | Simple Meaning |
|---|---|
| Accuracy | How many total rows were predicted correctly. It looks high because most customers do not churn. |
| Precision | Out of customers marked risky, how many actually churned. |
| Recall | Out of real churners, how many the model found. |
| ROC-AUC | How well the model ranks risky customers above safe customers. |
| PR-AUC | A better score for rare churn problems. |
| Flagged Rows | How many rows were marked as churn risk at the 10% threshold. |

## 3. Fit Check

Fit check tells us if the model is learning normally.

| Model | Status | Train ROC | Validation ROC | Test ROC | Train PR | Validation PR | Test PR |
|---|---|---:|---:|---:|---:|---:|---:|
| XGBoost | Healthy | 85.93% | 83.70% | 83.32% | 51.34% | 48.85% | 44.73% |
| LightGBM model 2 | Healthy | 85.40% | 83.98% | 83.01% | 51.34% | 48.87% | 44.26% |

Simple meaning:

- Train, validation, and test scores are close.
- That means the models are not just memorizing the training data.
- Both models are usable.

## 4. Runtime Contract

XGBoost files:

```text
model_1/training_scripts/xgboost_model1/
```

LightGBM model 2 files:

```text
model_1/training_scripts/lightgbm_model2/
```

Both models return:

| Output | Meaning |
|---|---|
| `churn_probability` | Real model probability from 0 to 100 |
| `risk_score` | Dashboard score from 0 to 100 |
| `churn_prediction` | `Yes` or `No` |
| `risk_level` | `Low`, `Medium`, or `High` |
| `top_risk_factors` | Inputs that pushed risk upward |

Prediction rule:

| Churn Probability | Prediction | Risk Level | Risk Score |
|---:|---|---|---:|
| below 10% | No | Low | 0 to below 30 |
| 10% to below 20% | Yes | Medium | 30 to below 70 |
| 20% and above | Yes | High | 70 to 100 |

Important:

`risk_score` is not a probability. It is only a dashboard-friendly score.

## 5. Customer 1: Risky Customer

Expected result:

```text
This customer should be High risk and predicted as churn.
```

Exact input JSON:

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

One-line explanation:

This customer is going quiet, balance is falling, card spend is falling, salary is late, money is moving out, and complaints are unresolved.

### Customer 1 Output

| Expected | XGBoost | LightGBM model 2 |
|---|---|---|
| Churn / High risk | Churn / High risk | Churn / High risk |

XGBoost output:

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

LightGBM model 2 output:

```json
{
  "churn_probability": 100.0,
  "risk_score": 100.0,
  "churn_prediction": "Yes",
  "risk_level": "High",
  "top_risk_factors": [
    { "factor": "balance_change_30d", "value": -48 },
    { "factor": "days_since_last_transaction", "value": 28 },
    { "factor": "card_spend_change_30d", "value": -62 },
    { "factor": "salary_missing_days", "value": 7 },
    { "factor": "complaints_30d", "value": 3 }
  ]
}
```

Simple result:

Both models strongly agree that this customer needs retention action.

## 6. Customer 2: Normal Customer

Expected result:

```text
This customer should be Low risk and predicted as not churn.
```

Exact input JSON:

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

One-line explanation:

This customer is active, balance is growing, spend is growing, salary is on time, and there are no complaints or failed transactions.

### Customer 2 Output

| Expected | XGBoost | LightGBM model 2 |
|---|---|---|
| Not churn / Low risk | Not churn / Low risk | Not churn / Low risk |

XGBoost output:

```json
{
  "churn_probability": 0.0,
  "risk_score": 0.0,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    { "factor": "card_colour", "value": "blue" },
    { "factor": "app_login_change_30d", "value": 10 },
    { "factor": "customer_segment", "value": "salary" },
    { "factor": "income_regularity", "value": "regular" },
    { "factor": "has_credit_card", "value": 1 }
  ]
}
```

LightGBM model 2 output:

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

Simple result:

Both models agree this customer looks healthy.

## 7. Short Conclusion

XGBoost and LightGBM model 2 behave similarly.

LightGBM model 2 has slightly higher precision and accuracy.

XGBoost is still a strong and simple main model for the project.
