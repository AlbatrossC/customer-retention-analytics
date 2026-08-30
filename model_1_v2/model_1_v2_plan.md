# Model 1 v2 Plan

## Context

We have a customer retention project.

Model 1 predicts customer churn.

For a retention system, Model 1 should answer:

> Is this customer likely to churn next month?

This is important.

There are two possible questions:

```text
A. Is this customer churning now?
B. Is this customer likely to churn next month?
```

For customer retention, we choose **B**.

The business does not only want to know who already left.

The business wants to know:

> Who should the bank intervene with before they leave?

The current Model 1 is an XGBoost model.

The v2 dataset should live inside the v2 folder:

```text
model_1_v2\data\customers.csv
```

The dataset has:

- 10,000 customers
- 53,040 monthly rows
- 31 columns
- 6 monthly snapshots: January 2026 to June 2026
- about 6% churn rate
- one row = one customer in one month

The current label is:

```text
churn_flag
```

Current meaning:

- `churn_flag = 1`: customer churned
- `churn_flag = 0`: customer stayed

For Model 1 v2, we should create a new label:

```text
next_month_churn
```

Meaning:

- `next_month_churn = 1`: customer churns in the next month
- `next_month_churn = 0`: customer does not churn in the next month

Example:

```text
Use January to May history -> predict June churn
Use January to June history -> predict July churn
```

Important:

The current `customers.csv` only has January to June 2026.

So exact July churn is not available yet.

To train a true next-month model, we should either:

- extend the synthetic dataset to include July labels, or
- train using earlier months, for example January to May history -> June churn

Best recommendation:

> Modify or regenerate the v2 dataset so it contains the next-month label clearly.

## Current Problems

### Problem 1: Same Prediction Too Often

In the local API log:

```text
logs\04-48 pm.md
```

many customers received almost the same Model 1 churn probability.

Example from the summary:

```text
1.96
1.65
1.96
1.96
1.96
1.96
1.96
1.96
7.29
36.3
```

This is not good enough.

Model 1 should separate customers better.

In simple terms:

> Healthy customers, slightly risky customers, medium-risk customers, and high-risk customers should not all get nearly the same score.

Possible reasons:

- the model is using only one monthly snapshot
- the model does not see the full customer trend
- isotonic calibration is compressing many low-risk customers into the same probability
- weak features may not explain enough difference between customers
- decoy fields may be adding noise

We checked raw XGBoost probabilities vs calibrated probabilities.

The result:

```text
Raw XGBoost probabilities:
- 1,541 unique rounded probability values on the test split
- scores are more spread out

Calibrated probabilities:
- only 66 unique rounded probability values on the test split
- 1.96% appears 3,757 times
```

Simple conclusion:

> The current isotonic calibration is probably causing the repeated 1.96% problem.

This does not mean calibration is always bad.

It means this calibration method is making the output too step-like for our use case.

For Model 1 v2, we should compare:

```text
raw XGBoost probability
sigmoid calibrated probability
isotonic calibrated probability
```

Then choose the one that is both:

- accurate enough
- not collapsed into repeated values

### Problem 2: Bad Risk Factors

The current Model 1 sometimes returns bad top risk factors like:

```text
age
branch_code
card_colour
```

This is a problem.

`branch_code` and `card_colour` are decoy columns. They are intentionally meaningless.

`age` may describe a customer, but it is not a useful retention action reason.

Hard rule:

> Do not use `age` as a Model 1 v2 training feature.

We should not train Model 1 v2 with `age`, `branch_code`, or `card_colour`.

## Folder Decision

Do not build v2 inside the old `model_1` folder.

Create a new top-level folder:

```text
model_1_v2
```

This folder should contain everything for v2:

- v2 data
- v2 feature building
- v2 training code
- v2 prediction code
- v2 model artifacts
- v2 metrics
- v2 documentation

The old `model_1` folder should stay untouched as the baseline.

## Goal

Create a better XGBoost model called:

```text
model_1_v2
```

The new model should:

- use 6 months of customer history
- predict next-month churn
- create better customer differentiation
- avoid repeated same probabilities like `1.96`
- remove noisy and unfair fields
- output useful risk factors
- keep the same simple API output format
- be easy to compare against the old Model 1

## Snapshot Recommendation

Use a **growing history window up to 6 months** to predict the **next month**.

This means:

> For each prediction, use all history available so far, up to 6 months.

Then predict whether the customer will churn in the next month.

Do not send six raw rows directly into XGBoost.

Instead:

```text
6 months of history -> one feature row -> XGBoost -> next-month churn prediction
```

Training examples should look like this:

```text
Jan -> predict Feb
Jan-Feb -> predict Mar
Jan-Feb-Mar -> predict Apr
Jan-Feb-Mar-Apr -> predict May
Jan-Feb-Mar-Apr-May -> predict Jun
```

If July data exists later:

```text
Jan-Feb-Mar-Apr-May-Jun -> predict Jul
```

For the current dataset, we only have January to June.

So the last usable next-month training example is:

```text
Input: January to May customer history
Output: June churn risk
```

Why 6 months?

- The dataset only has 6 months.
- 1 month is too short.
- 3 months is useful but may miss slow decline.
- 6 months can show whether a customer is getting worse over time.

## What We Will Input

The raw input should be:

```text
customer profile + monthly history
```

Example raw API input:

```json
{
  "customer_id": "C10020",
  "prediction_date": "2026-05-01",
  "target_month": "2026-06-01",
  "profile": {
    "tenure_months": 129,
    "customer_segment": "salary",
    "income_regularity": "regular",
    "products_count": 3,
    "has_credit_card": 1,
    "has_loan": 1
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 5,
      "balance_change_30d": 14,
      "transaction_change_30d": 10,
      "card_spend_change_30d": 10,
      "app_login_change_30d": 4,
      "external_transfer_change_30d": 10,
      "complaints_30d": 1,
      "unresolved_complaints": 0,
      "failed_transactions_30d": 0
    }
  ]
}
```

For training, this raw history will come from:

```text
model_1_v2\data\customers.csv
```

For Model 1 v2, we will copy or transform it into:

```text
model_1_v2\data\customers_model_1_v2.csv
```

## What XGBoost Will Actually See

XGBoost will see one flat row per customer prediction date.

Example:

```text
tenure_months
customer_segment
income_regularity
products_count
has_credit_card
has_loan
latest_days_since_last_transaction
latest_balance_change_30d
avg_balance_change_3m
avg_balance_change_6m
balance_trend_6m
sum_complaints_6m
max_failed_transactions_6m
months_observed
```

So the model input is still simple.

The model does not understand raw time series.

We convert history into numbers first.

For example:

```text
Raw history:
Jan, Feb, Mar, Apr, May

Flat model row:
latest balance change
average balance change across 3 months
average balance change across 5 months
balance trend
total complaints so far
maximum days since transaction so far
```

## Features To Use

Use profile fields that are useful and safe:

```text
tenure_months
customer_segment
income_regularity
products_count
has_credit_card
has_loan
```

Do not include:

```text
age
```

Age must stay out of training features.

Use latest-month behavior:

```text
latest_days_since_last_transaction
latest_balance_change_30d
latest_transaction_change_30d
latest_card_spend_change_30d
latest_app_login_change_30d
latest_salary_missing_days
latest_external_transfer_change_30d
latest_upi_share_of_spend
latest_fd_maturing_in_30d
latest_products_dropped_90d
latest_complaints_30d
latest_unresolved_complaints
latest_failed_transactions_30d
latest_avg_resolution_time_hrs
latest_emi_bounce_30d
```

Use 3-month summaries:

```text
avg_balance_change_3m
avg_transaction_change_3m
avg_card_spend_change_3m
avg_app_login_change_3m
avg_external_transfer_change_3m
max_days_since_last_transaction_3m
sum_complaints_3m
sum_unresolved_complaints_3m
sum_failed_transactions_3m
sum_products_dropped_3m
max_avg_resolution_time_hrs_3m
```

Use 6-month summaries:

```text
avg_balance_change_6m
avg_transaction_change_6m
avg_card_spend_change_6m
avg_app_login_change_6m
avg_external_transfer_change_6m
max_days_since_last_transaction_6m
sum_complaints_6m
sum_unresolved_complaints_6m
sum_failed_transactions_6m
sum_products_dropped_6m
max_avg_resolution_time_hrs_6m
months_observed
```

Because the current next-month examples can have 1 to 5 months of history, also include flexible history features:

```text
avg_balance_change_available_history
avg_transaction_change_available_history
avg_card_spend_change_available_history
avg_app_login_change_available_history
avg_external_transfer_change_available_history
max_days_since_last_transaction_available_history
sum_complaints_available_history
sum_failed_transactions_available_history
months_observed
```

This lets the model learn from:

```text
Jan only
Jan-Feb
Jan-Feb-Mar
Jan-Feb-Mar-Apr
Jan-Feb-Mar-Apr-May
```

Use trend features:

```text
balance_trend_6m
transaction_trend_6m
card_spend_trend_6m
app_login_trend_6m
days_since_transaction_trend_6m
external_transfer_trend_6m
complaints_trend_6m
```

A trend feature means:

```text
Is this value generally going up or down across the months?
```

## Features To Remove

Do not train Model 1 v2 on:

```text
customer_id
customer_name
snapshot_date
age
customer_yearly_value
loyalty
complaint_text
branch_code
card_colour
churn_flag
```

Reasons:

- `customer_id` can cause memorization
- `customer_name` is not useful
- `snapshot_date` may create time leakage
- `age` is not a training feature for Model 1 v2
- `age` is not a good retention reason
- `customer_yearly_value` is for business value ranking, not churn prediction
- `loyalty` is hidden and was used to generate the label
- `complaint_text` should go to Model 2, not Model 1
- `branch_code` is decoy noise
- `card_colour` is decoy noise
- `churn_flag` is the answer, never an input

## What We Will Output

Model 1 v2 should keep the same output shape:

```json
{
  "churn_probability": 72.4,
  "risk_score": 88.1,
  "churn_prediction": "Yes",
  "risk_level": "High",
  "top_risk_factors": [
    {
      "factor": "max_days_since_last_transaction_6m",
      "value": 19
    },
    {
      "factor": "avg_balance_change_6m",
      "value": -18.7
    },
    {
      "factor": "sum_complaints_3m",
      "value": 3
    }
  ]
}
```

Meaning:

- `churn_probability`: estimated chance of churn next month, as a percent
- `risk_score`: 0 to 100 business risk score
- `churn_prediction`: `Yes` or `No` for next-month churn
- `risk_level`: `Low`, `Medium`, or `High`
- `top_risk_factors`: useful reasons behind the score

Top risk factors must never include:

```text
age
branch_code
card_colour
customer_id
customer_name
snapshot_date
loyalty
customer_yearly_value
complaint_text
churn_flag
```

## Better Differentiation Plan

We need to make sure Model 1 v2 does not give the same probability to too many customers.

During evaluation, check:

```text
How many unique probability values are produced?
How many customers get exactly the same probability?
What is the probability range?
What are the probability percentiles?
```

Example checks:

```text
min probability
10th percentile
25th percentile
median
75th percentile
90th percentile
max probability
number of unique probability values
top 10 most repeated probability values
```

Current finding:

```text
Raw probabilities are much more varied.
Calibrated probabilities are step-like.
The repeated 1.96% value is coming from isotonic calibration.
```

Acceptance rule:

> The model should not assign the same low probability, such as 1.96%, to most normal customers.

If this still happens, test these fixes:

- compare raw XGBoost probability vs calibrated probability
- try sigmoid calibration instead of isotonic calibration
- keep raw probability if both calibration methods over-compress scores
- tune XGBoost depth and regularization
- add more trend features
- review whether labels are too weak for low-risk customers
- evaluate customer-level predictions, not only row-level predictions

Recommended v2 decision:

> Do not blindly use isotonic calibration. First compare raw, sigmoid calibrated, and isotonic calibrated probabilities.

## Top Risk Factor Plan

The current API creates `top_risk_factors` using XGBoost contribution values.

In simple terms:

```text
For one prediction, it asks XGBoost:
Which features pushed this score upward?
```

Current problem:

This can return features like:

```text
branch_code
card_colour
age
```

That is not useful.

For Model 1 v2, top risk factors should be generated using only approved business signals.

Approved examples:

```text
latest_days_since_last_transaction
avg_balance_change_6m
balance_trend_6m
avg_transaction_change_6m
transaction_trend_6m
avg_card_spend_change_6m
app_login_trend_6m
avg_external_transfer_change_6m
sum_complaints_6m
sum_unresolved_complaints_6m
sum_failed_transactions_6m
latest_fd_maturing_in_30d
sum_products_dropped_6m
latest_emi_bounce_30d
```

Blocked examples:

```text
age
branch_code
card_colour
customer_id
customer_name
snapshot_date
loyalty
customer_yearly_value
complaint_text
churn_flag
```

Better method:

1. Calculate feature contributions.
2. Keep only positive contributions.
3. Remove blocked fields.
4. Keep only business-actionable fields.
5. Convert technical feature names into simple messages.

Example:

```json
{
  "factor": "balance_trend_6m",
  "value": -6.2,
  "message": "Balance has been trending downward over recent months."
}
```

Important:

> Top risk factors are not just the biggest math values. They must also be useful explanations for a bank team.

## Training Dataset For v2

Create a new folder:

```text
model_1_v2\data
```

Create a new v2 training table:

```text
model_1_v2\data\customers_model_1_v2.csv
```

This file is created from:

```text
model_1_v2\data\customers.csv
```

Each row in the v2 file should mean:

> One customer at one prediction date, with features created from up to 6 months of history, and a label for the next month.

Example:

```text
C10020, prediction date May 2026, history Jan to May, label next_month_churn for June
```

For current data, build labels like this:

```text
Jan row -> next_month_churn = Feb churn_flag
Feb row with Jan-Feb history -> next_month_churn = Mar churn_flag
Mar row with Jan-Feb-Mar history -> next_month_churn = Apr churn_flag
Apr row with Jan-Feb-Mar-Apr history -> next_month_churn = May churn_flag
May row with Jan-Feb-Mar-Apr-May history -> next_month_churn = Jun churn_flag
```

Very important rule:

> The next-month label must come from the following month's `churn_flag`.

Do not create the label from the number of rows a customer has.

Why?

Some customers churn in the first few months.

The model should learn:

```text
What did the customer look like before churn?
```

not:

```text
How many rows does this customer have?
```

If a following month does not exist, do not use that row for next-month training.

Example:

```text
June cannot be used to train next-month churn unless July exists.
```

Future recommended decision:

> If we extend the data to July, then Jan-Jun history can predict July churn.

## Model 2 Data Copy Plan

This is not for Model 1 training.

Model 2 needs customer context and complaint text so it can explain the risk and suggest actions.

Copy the needed data into the Model 2 area:

```text
model_2\data
```

Recommended files:

```text
model_2\data\customers.csv
model_2\data\complaint_texts_with_customer_id.json
```

The complaint text pool should also be copied into v2:

```text
model_1_v2\data\complaint_texts.json
```

That file is a complaint text pool by complaint type.

It does not directly tell us:

```text
which customer had which complaint
```

For Model 2, create a customer-linked complaint file from `customers.csv`.

Recommended format:

```json
[
  {
    "customer_id": "C10020",
    "customer_name": "Ekbal Garg",
    "snapshot_date": "2026-01-01",
    "complaints_30d": 1,
    "unresolved_complaints": 0,
    "complaint_text": "Kindly reissue my card, the chip has stopped reading at merchants."
  }
]
```

Only include rows where `complaint_text` is present.

This file helps Model 2 because we can easily send:

```text
customer_id -> complaint text -> Model 2 explanation
```

Important:

Do not use complaint text in Model 1 v2 training.

Complaint text is for Model 2 only.

## Training Approach

Use XGBoost.

Split by customer:

```text
70% train customers
15% validation customers
15% test customers
```

Important:

Do not split by row.

If we split by row, the same customer can appear in both training and testing.

That makes the score look better than it really is.

## Evaluation

Do not focus on accuracy.

Churn is rare. Accuracy can look good even if the model is bad.

Use:

```text
PR-AUC
ROC-AUC
precision
recall
confusion matrix
threshold sweep
calibration check
probability differentiation check
feature importance check
```

Main metric:

```text
PR-AUC
```

Why:

Only about 6% of rows churn, so PR-AUC is more useful than accuracy.

## Acceptance Checks

Model 1 v2 is acceptable only if:

- `age` is not used
- `branch_code` is not used
- `card_colour` is not used
- no leakage columns enter training
- train, validation, and test are split by customer
- PR-AUC is close to or better than the current model
- repeated identical probabilities are reduced
- raw vs calibrated probability comparison is saved in metrics
- top risk factors are useful business signals
- the model gives better separation between low, medium, and high risk customers
- the API can still return the same output format

## New Folder Structure

Create:

```text
model_1_v2
model_1_v2\data
model_1_v2\training_scripts
model_1_v2\training_scripts\xgboost_model1_v2
model_1_v2\training_scripts\xgboost_model1_v2\artifacts
model_1_v2\docs
```

Recommended files:

```text
model_1_v2\README.md
model_1_v2\model_1_v2_plan.md
model_1_v2\data\customers_model_1_v2.csv
model_1_v2\training_scripts\xgboost_model1_v2\build_features.py
model_1_v2\training_scripts\xgboost_model1_v2\train_xgboost_v2.py
model_1_v2\training_scripts\xgboost_model1_v2\test_prediction_v2.py
model_1_v2\training_scripts\xgboost_model1_v2\diagnose_probabilities_v2.py
model_1_v2\training_scripts\xgboost_model1_v2\artifacts\xgboost_model_v2.json
model_1_v2\training_scripts\xgboost_model1_v2\artifacts\calibrator_v2.joblib
model_1_v2\training_scripts\xgboost_model1_v2\artifacts\model_metadata_v2.json
model_1_v2\training_scripts\xgboost_model1_v2\artifacts\metrics_v2.json
model_1_v2\docs\results_v2.md
```

## API Plan

The API should eventually be able to use Model 1 v2.

It should still return:

```json
{
  "churn_probability": 72.4,
  "risk_score": 88.1,
  "churn_prediction": "Yes",
  "risk_level": "High",
  "top_risk_factors": []
}
```

But the input should support 6-month history for next-month prediction:

```json
{
  "profile": {
    "customer_segment": "salary",
    "income_regularity": "regular",
    "tenure_months": 48,
    "products_count": 3,
    "has_credit_card": 1,
    "has_loan": 1
  },
  "monthly_history": [
    {
      "snapshot_date": "2026-01-01",
      "days_since_last_transaction": 5,
      "balance_change_30d": 14,
      "transaction_change_30d": 10,
      "complaints_30d": 1
    }
  ]
}
```

The API should convert this history into v2 features before prediction.

In production terms:

```text
Input: latest available 6 months
Output: churn risk for the next month
```

If only 3 months are available, the API can still predict.

The feature builder should set:

```text
months_observed = 3
```

and calculate summaries using the available months.

## Simple Summary

We should create a separate folder:

```text
model_1_v2
```

Inside it, we build a new XGBoost churn model.

The new model should use:

```text
6 months of customer history to predict next-month churn
```

But XGBoost should receive:

```text
one flat feature row
```

The conversion is:

```text
6 months of history -> summary features + trend features -> one row -> XGBoost -> next-month churn risk
```

The model should not use:

```text
age
branch_code
card_colour
```

The model should fix the current problem where many customers get almost the same probability, like:

```text
1.96%
```

Also copy Model 2 support data into:

```text
model_2\data
```

and create:

```text
complaint_texts_with_customer_id.json
```

This is for Model 2 context only, not Model 1 training.

Final recommendation:

> Build Model 1 v2 as a separate `model_1_v2` project using XGBoost, 6-month history features, a next-month churn label, no decoy fields, and explicit probability differentiation checks.
