# Final Model Result

## 1. What We Tested

We tested the complete Colab API flow:

```text
Customer data -> Model 1 -> Model 2 -> API output
```

The API was tested using:

```text
model_1/data/customers.csv
```

We selected 10 customers and sent them to:

```text
/predict/both
```

That means both models were used:

- Model 1: XGBoost churn risk model
- Model 2: reason and next action model

## 2. What Was Expected

### Model 1 Expected Output

Model 1 should return:

- churn probability
- risk score
- churn prediction
- risk level
- top risk factors

Example:

```text
Churn Probability: 82%
Prediction: Yes
Risk Level: High
Top Risk Factors:
- transactions down
- unresolved complaints
- external transfers up
```

### Model 2 Expected Output

Model 2 should return:

- why the customer is at risk
- next recommended actions

Expected action types:

- RM call
- complaint escalation
- fee waiver
- rate offer
- do nothing if healthy

Example:

```text
Why:
- Customer activity dropped recently.
- Complaints are unresolved.
- Money is moving to other banks.

Next Actions:
- RM call
- Complaint escalation
```

## 3. Model 1 Official Performance

From `model_1/docs/results.md`, XGBoost has these test results:

| Metric | Result |
|---|---:|
| Accuracy | 91.82% |
| Precision | 38.43% |
| Recall | 59.54% |
| ROC-AUC | 83.32% |
| PR-AUC | 44.73% |

Simple meaning:

- Accuracy is high, but churn is rare, so accuracy alone is not enough.
- ROC-AUC is good.
- PR-AUC is useful because churn customers are a small group.
- Recall is decent because the model finds many churn-risk customers.
- Precision is not very high, but that is common in churn problems.

## 4. Model 1 Live API Result

In the Colab API test, all 10 customers were predicted as churn risk.

Risk probabilities were:

```text
70.37% to 100%
```

All 10 customers were marked:

```text
Prediction: Yes
Risk Level: High
```

The top risk factors looked meaningful.

Common risk factors were:

- balance going down
- card spend going down
- many days since last transaction
- high complaint resolution time
- failed transactions
- complaints
- salary delay
- FD maturity

Simple result:

Model 1 worked well in the API test.

It gave clear and useful churn-risk outputs.

## 5. Model 2 Live API Result

Model 2 loaded successfully and returned output for all 10 customers.

That means the API connection worked.

But the quality of Model 2 output was not good enough yet.

Problems seen:

- Some outputs had no next action.
- Some outputs had strange action names.
- Some outputs contained raw numbers without explanation.
- Some outputs copied raw dictionaries instead of explaining them.
- Some outputs looked broken or incomplete.
- Some outputs gave actions that are not bank-ready.

Examples of weak output:

```text
Next actions: None
```

```text
141.0369
```

```text
600000000.0
```

```text
report_the_issue()
```

```text
request_3rd_communication()
```

Simple result:

Model 2 is running, but the response quality needs improvement.

It should not be shown directly to judges in this form.

## 6. Honest Rating

### Model 1 Rating

```text
8 / 10
```

Why:

- It has proper test metrics.
- It has healthy train/validation/test behavior.
- It gives useful dashboard outputs.
- It correctly identifies high-risk customers.
- Its top risk factors mostly make sense.

Why not 10:

- Precision is only 38.43%.
- Some low-risk top factors can still look odd.
- It is trained on synthetic data, not real bank data.

Overall:

Model 1 is strong enough for the project dashboard.

### Model 2 Rating

```text
4 / 10
```

Why:

- It loads successfully.
- It returns responses through the API.
- Some explanations are partly useful.

Why low:

- Output format is inconsistent.
- Some actions are not practical.
- Some outputs are incomplete.
- Some outputs contain strange numbers.
- It does not reliably follow the expected action style.

Overall:

Model 2 proves the idea, but it needs prompt tuning or better fine-tuning before final demo.

## 7. Overall System Rating

```text
6.5 / 10
```

Why:

- The full pipeline works technically.
- Model 1 is good.
- The API integration works.
- Model 2 is the weak part right now.

If Model 2 output is cleaned up, the full system can become:

```text
8 / 10 or higher
```

## 8. Final Conclusion

Model 1 is ready for the dashboard.

Model 2 is not fully ready yet.

The best next step is to improve Model 2 output control.

Model 2 should always return:

```json
{
  "why": [
    "short clear reason 1",
    "short clear reason 2"
  ],
  "next_actions": [
    "rm_call: call the customer and understand the issue",
    "complaint_escalation: resolve the open complaint quickly"
  ]
}
```

Allowed action prefixes should be:

- `rm_call`
- `complaint_escalation`
- `fee_waiver`
- `rate_offer`
- `do_nothing`

Simple final statement:

```text
Model 1 detects churn risk well.
Model 2 can explain and recommend actions, but it needs cleanup before final presentation.
```
