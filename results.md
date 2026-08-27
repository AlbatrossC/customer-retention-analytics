# Model Results

The dataset was not changed.

Tested four models:

- XGBoost old
- XGBoost calibrated
- LightGBM model 1
- LightGBM model 2

## Simple Answer

The old XGBoost model is not good for probability display. It is too confident.

The three calibrated models are healthier.

Best practical choices:

1. XGBoost calibrated
2. LightGBM model 2

## Fit Check

| Model | Status | Why | Train ROC | Val ROC | Test ROC | Train PR | Val PR | Test PR |
|---|---|---|---:|---:|---:|---:|---:|---:|
| XGBoost old | Healthy | Train and test are close enough. | 0.8611 | 0.8305 | 0.8379 | 0.5043 | 0.4911 | 0.4633 |
| XGBoost calibrated | Healthy | Train and test are close enough. | 0.8593 | 0.8370 | 0.8332 | 0.5134 | 0.4885 | 0.4473 |
| LightGBM model 1 | Healthy | Train and test are close enough. | 0.8681 | 0.8380 | 0.8289 | 0.5361 | 0.4880 | 0.4426 |
| LightGBM model 2 | Healthy | Train and test are close enough. | 0.8540 | 0.8398 | 0.8301 | 0.5134 | 0.4887 | 0.4426 |

## Test Set Results

| Model | Precision | Recall | Flagged Rows | Mean Probability | Confusion Matrix |
|---|---:|---:|---:|---:|---|
| XGBoost old | 0.3398 | 0.6205 | 871 | 0.3229 | [[6869, 575], [181, 296]] |
| XGBoost calibrated | 0.3843 | 0.5954 | 739 | 0.0570 | [[6989, 455], [193, 284]] |
| LightGBM model 1 | 0.3961 | 0.5996 | 722 | 0.0571 | [[7008, 436], [191, 286]] |
| LightGBM model 2 | 0.4102 | 0.5891 | 685 | 0.0571 | [[7040, 404], [196, 281]] |

## Example Tests

| Example | Expected | XGBoost old | XGBoost calibrated | LightGBM 1 | LightGBM 2 |
|---|---|---:|---:|---:|---:|
| Healthy salary customer | Very low risk | 14.31% | 1.96% | 1.89% | 1.91% |
| Salary customer going quiet | Medium risk | 83.81% | 18.06% | 16.67% | 21.97% |
| Complaint-heavy customer | Medium to high risk | 85.51% | 20.69% | 19.13% | 21.97% |
| Everything going wrong | Highest risk | 99.13% | 100.00% | 100.00% | 100.00% |
| Farmer with no salary field | Should not crash; NaN salary is valid | 43.57% | 4.11% | 4.23% | 3.58% |
| Pension FD maturity | Moderate risk | 27.86% | 2.39% | 1.98% | 1.91% |
| Vendor with failed payments | Service risk | 62.81% | 8.16% | 9.15% | 8.26% |
| Improving after complaint | Low risk | 16.51% | 1.96% | 1.89% | 1.91% |

## Example Predictions

| Example | XGBoost old | XGBoost calibrated | LightGBM 1 | LightGBM 2 |
|---|---|---|---|---|
| Healthy salary customer | No / Medium | No / Low | No / Low | No / Low |
| Salary customer going quiet | Yes / High | Yes / Medium | Yes / Medium | Yes / High |
| Complaint-heavy customer | Yes / High | Yes / High | Yes / Medium | Yes / High |
| Everything going wrong | Yes / High | Yes / High | Yes / High | Yes / High |
| Farmer with no salary field | No / High | No / Low | No / Low | No / Low |
| Pension FD maturity | No / High | No / Low | No / Low | No / Low |
| Vendor with failed payments | No / High | No / Low | No / Low | No / Low |
| Improving after complaint | No / Medium | No / Low | No / Low | No / Low |

## Plain Meaning

Overfitting means train score is much higher than test score.

Underfitting means both train and test scores are weak.

Healthy means train, validation, and test are close, and test ROC/PR are in the expected range.

In these results, the calibrated models look healthy. The old XGBoost model ranks customers fairly well, but its probabilities are too high.

## Best Model Runtime Contract

Use **XGBoost calibrated** from `training_scripts/xgboost_model1/artifacts_candidate`.

Prediction rule:

- `churn_prediction = "Yes"` when `churn_probability >= 10%`
- `risk_level = "Low"` below 10%
- `risk_level = "Medium"` from 10% to below 20%
- `risk_level = "High"` from 20% and above

Do not send leakage fields at prediction time: `customer_id`, `customer_name`, `snapshot_date`, `loyalty`, `customer_yearly_value`, `complaint_text`, `churn_flag`.

### JSON Input Schema

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "CustomerChurnPredictionInput",
  "type": "object",
  "additionalProperties": false,
  "required": [
    "age",
    "tenure_months",
    "customer_segment",
    "income_regularity",
    "products_count",
    "has_credit_card",
    "has_loan",
    "days_since_last_transaction",
    "balance_change_30d",
    "transaction_change_30d",
    "card_spend_change_30d",
    "app_login_change_30d",
    "salary_missing_days",
    "external_transfer_change_30d",
    "upi_share_of_spend",
    "fd_maturing_in_30d",
    "products_dropped_90d",
    "complaints_30d",
    "unresolved_complaints",
    "failed_transactions_30d",
    "avg_resolution_time_hrs",
    "emi_bounce_30d",
    "branch_code",
    "card_colour"
  ],
  "properties": {
    "age": { "type": "integer" },
    "tenure_months": { "type": "integer" },
    "customer_segment": { "type": "string", "enum": ["salary", "pension", "farmer", "vendor", "business"] },
    "income_regularity": { "type": "string", "enum": ["regular", "irregular", "seasonal"] },
    "products_count": { "type": "integer" },
    "has_credit_card": { "type": "integer", "enum": [0, 1] },
    "has_loan": { "type": "integer", "enum": [0, 1] },
    "days_since_last_transaction": { "type": "integer" },
    "balance_change_30d": { "type": "number" },
    "transaction_change_30d": { "type": "number" },
    "card_spend_change_30d": { "type": "number" },
    "app_login_change_30d": { "type": "number" },
    "salary_missing_days": { "type": ["number", "null"] },
    "external_transfer_change_30d": { "type": "number" },
    "upi_share_of_spend": { "type": "number", "minimum": 0, "maximum": 1 },
    "fd_maturing_in_30d": { "type": "integer", "enum": [0, 1] },
    "products_dropped_90d": { "type": "integer" },
    "complaints_30d": { "type": "integer" },
    "unresolved_complaints": { "type": "integer" },
    "failed_transactions_30d": { "type": "integer" },
    "avg_resolution_time_hrs": { "type": "number" },
    "emi_bounce_30d": { "type": "integer" },
    "branch_code": { "type": "string", "pattern": "^BR-[0-9]{3}$" },
    "card_colour": { "type": "string", "enum": ["blue", "green", "silver", "gold", "black"] }
  }
}
```

### JSON Output Schema

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "CustomerChurnPredictionOutput",
  "type": "object",
  "additionalProperties": false,
  "required": ["churn_probability", "churn_prediction", "risk_level", "top_risk_factors"],
  "properties": {
    "churn_probability": { "type": "number", "minimum": 0, "maximum": 100 },
    "churn_prediction": { "type": "string", "enum": ["Yes", "No"] },
    "risk_level": { "type": "string", "enum": ["Low", "Medium", "High"] },
    "top_risk_factors": {
      "type": "array",
      "items": {
        "type": "object",
        "additionalProperties": false,
        "required": ["factor", "value"],
        "properties": {
          "factor": { "type": "string" },
          "value": { "type": ["string", "number", "integer", "boolean", "null"] }
        }
      }
    }
  }
}
```

### Sample Input

```json
{
  "age": 38,
  "tenure_months": 96,
  "customer_segment": "salary",
  "income_regularity": "regular",
  "products_count": 3,
  "has_credit_card": 1,
  "has_loan": 1,
  "days_since_last_transaction": 20,
  "balance_change_30d": -34,
  "transaction_change_30d": -38,
  "card_spend_change_30d": -35,
  "app_login_change_30d": -42,
  "salary_missing_days": 3,
  "external_transfer_change_30d": 70,
  "upi_share_of_spend": 0.68,
  "fd_maturing_in_30d": 0,
  "products_dropped_90d": 0,
  "complaints_30d": 0,
  "unresolved_complaints": 0,
  "failed_transactions_30d": 0,
  "avg_resolution_time_hrs": 0,
  "emi_bounce_30d": 0,
  "branch_code": "BR-121",
  "card_colour": "gold"
}
```

### Sample Output

```json
{
  "churn_probability": 18.06,
  "churn_prediction": "Yes",
  "risk_level": "Medium",
  "top_risk_factors": [
    { "factor": "balance_change_30d", "value": -34 },
    { "factor": "days_since_last_transaction", "value": 20 },
    { "factor": "card_spend_change_30d", "value": -35 },
    { "factor": "salary_missing_days", "value": 3 },
    { "factor": "branch_code", "value": "BR-121" }
  ]
}
```

### Real Input

Source row: `data/model_1_training_data/customers.csv`, row index `0`, customer `C10000`, snapshot `2026-01-01`, actual `churn_flag = 0`.

```json
{
  "age": 32,
  "tenure_months": 6,
  "customer_segment": "business",
  "income_regularity": "irregular",
  "products_count": 2,
  "has_credit_card": 0,
  "has_loan": 1,
  "days_since_last_transaction": 12,
  "balance_change_30d": 14.3603,
  "transaction_change_30d": 12.3591,
  "card_spend_change_30d": 29.2178,
  "app_login_change_30d": -17.2005,
  "salary_missing_days": null,
  "external_transfer_change_30d": -5.5963,
  "upi_share_of_spend": 0.2942,
  "fd_maturing_in_30d": 0,
  "products_dropped_90d": 1,
  "complaints_30d": 0,
  "unresolved_complaints": 0,
  "failed_transactions_30d": 0,
  "avg_resolution_time_hrs": 0.0,
  "emi_bounce_30d": 0,
  "branch_code": "BR-106",
  "card_colour": "blue"
}
```

### Real Output

```json
{
  "churn_probability": 2.39,
  "churn_prediction": "No",
  "risk_level": "Low",
  "top_risk_factors": [
    { "factor": "tenure_months", "value": 6 },
    { "factor": "branch_code", "value": "BR-106" },
    { "factor": "upi_share_of_spend", "value": 0.2942 },
    { "factor": "card_colour", "value": "blue" },
    { "factor": "products_dropped_90d", "value": 1 }
  ]
}
```
