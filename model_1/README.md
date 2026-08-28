# Model 1

Model 1 predicts whether a bank customer is likely to churn.

In simple terms: it reads customer activity, product, and service signals, then returns a churn probability, risk score, risk level, and top risk factors.

## Dataset

The dataset is:

```text
model_1\data\customers.csv
```

It is synthetic bank data, not real customer data.

Quick facts:

- 10,000 customers
- 53,040 monthly customer rows
- 31 columns
- about 6% churn rate
- `churn_flag = 1` means the customer churned
- `churn_flag = 0` means the customer stayed

More dataset details are in:

```text
model_1\data\README.md
```

The hidden simulator data is:

```text
model_1\data\responsiveness.csv
```

Do not use `responsiveness.csv` for churn model training. It is only for retention action simulation.

## Available Models

There are two trained churn models in this folder.

### XGBoost

Main model:

```text
model_1\training_scripts\xgboost_model1\
```

Artifacts:

```text
model_1\training_scripts\xgboost_model1\artifacts\
```

Test results:

- Accuracy: 91.82%
- Precision: 38.43%
- Recall: 59.54%
- ROC-AUC: 83.32%
- PR-AUC: 44.73%

Docs:

```text
model_1\docs\xgboost.md
```

### LightGBM Model 2

Comparison model:

```text
model_1\training_scripts\lightgbm_model2\
```

Artifacts:

```text
model_1\training_scripts\lightgbm_model2\artifacts\
```

Test results:

- Accuracy: 92.43%
- Precision: 41.02%
- Recall: 58.91%
- ROC-AUC: 83.01%
- PR-AUC: 44.26%

Docs:

```text
model_1\docs\lightbgm_model_2.md
```

Overall comparison:

```text
model_1\docs\results.md
```

## Install Dependencies

From the repository root:

```powershell
cd D:\customer-retention-analytics
uv venv
.venv\Scripts\activate
uv pip install -r requirements.txt
```

## Run Model 1

Run the XGBoost sample prediction:

```powershell
python model_1\training_scripts\xgboost_model1\test_prediction.py
```

Run the LightGBM sample prediction:

```powershell
python model_1\training_scripts\lightgbm_model2\test_prediction.py
```

Both commands print JSON like this:

```json
{
  "churn_probability": 100.0,
  "risk_score": 100.0,
  "churn_prediction": "Yes",
  "risk_level": "High",
  "top_risk_factors": []
}
```

## Retrain The Models

Run XGBoost training:

```powershell
python model_1\training_scripts\xgboost_model1\train_xgboost.py
```

Run LightGBM training:

```powershell
python model_1\training_scripts\lightgbm_model2\train_lightgbm.py
```

Training reads:

```text
model_1\data\customers.csv
```

and writes updated artifacts into each model's `artifacts` folder.

## Regenerate The Dataset

From the repository root:

```powershell
python model_1\dataset_scripts\generate.py
python model_1\dataset_scripts\scripts\check_dataset.py
python -m pytest model_1\dataset_scripts\tests -q
```

The dataset generator uses seed `42`, so it should produce the same dataset each time.

