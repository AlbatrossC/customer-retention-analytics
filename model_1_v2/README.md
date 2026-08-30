# Model 1 v2

XGBoost churn model for next-month customer retention risk.

Model 1 v2 answers:

```text
Is this customer likely to churn next month?
```

It uses customer history from the local v2 data file:

```text
model_1_v2/data/customers.csv
```

and builds a new v2 training table:

```text
model_1_v2/data/customers_model_1_v2.csv
```

## Run

From the repository root:

```powershell
python model_1_v2\training_scripts\xgboost_model1_v2\build_features.py
python model_1_v2\training_scripts\xgboost_model1_v2\train_xgboost_v2.py
python model_1_v2\training_scripts\xgboost_model1_v2\diagnose_probabilities_v2.py
python model_1_v2\training_scripts\xgboost_model1_v2\test_prediction_v2.py
```

Build customer-linked complaint data:

```powershell
python model_1_v2\data\build_complaints_with_customer_id.py
```

## Important Rules

- Predict next-month churn, not current-month churn.
- Build labels from the following month's `churn_flag`.
- Do not use `age`, `branch_code`, or `card_colour`.
- Do not use `complaint_text` for Model 1 training.
- Split by customer, not by row.
- Compare raw, sigmoid calibrated, and isotonic calibrated probabilities.
