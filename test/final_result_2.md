# Final Model Result 2

## 1. What Changed

We updated the Model 2 system prompt.

The new prompt tells Model 2 to:

- return only JSON
- use exactly two keys: `why` and `next_actions`
- keep both values as arrays of short strings
- put explanations only in `why`
- put recommendations only in `next_actions`

Then we tested the Colab API again using:

```text
test/colab_api_test.py
```

The latest result file is:

```text
test/colab_api_test_results.md
```

## 2. API Result

The API worked.

Health check:

```json
{
  "ok": true,
  "model1_loaded": true,
  "model2_loaded": true
}
```

This means:

- Model 1 loaded successfully.
- Model 2 loaded successfully.
- The Colab API was reachable.
- `/predict/both` worked for all 10 customers.

## 3. Model 1 Result

Model 1 performed the same as before.

All 10 tested customers were predicted as high churn risk.

Risk range:

```text
70.37% to 100%
```

All 10 customers had:

```text
Prediction: Yes
Risk Level: High
```

The top risk factors were meaningful.

Common Model 1 risk factors:

- balance going down
- card spend going down
- many days since last transaction
- failed transactions
- high complaint resolution time
- complaints
- salary delay
- FD maturity

Simple result:

Model 1 is working well.

It is ready to use for the dashboard.

## 4. Model 2 Old Result

Before the prompt change, Model 2 had many output problems.

Old problems:

- strange action names
- missing next actions
- raw numbers without explanation
- broken JSON-like text
- copied raw dictionaries
- actions that were not useful for bank staff

Examples from old result:

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

Old Model 2 rating:

```text
4 / 10
```

## 5. Model 2 New Result

After the prompt change, Model 2 improved.

In the new test:

- 10 out of 10 requests completed.
- 7 out of 10 outputs passed the strict JSON structure check.
- 3 out of 10 outputs were still marked invalid.

Valid JSON count:

```text
7 / 10
```

Invalid JSON count:

```text
3 / 10
```

The new answers are more readable than before.

Better examples:

```text
The customer has a -64% change in their balance over the last 30 days,
which may indicate funds being shifted out of the account.
```

```text
Contact the customer within 24 hours.
Ask about the loss of confidence and what would help improve loyalty.
```

```text
Contact the customer to understand the specific reason behind the balance decline
and agree on a next course of action.
```

This is better than the old function-like outputs.

## 6. Remaining Model 2 Problems

Model 2 is better, but still not perfect.

Remaining problems:

- 3 outputs still failed the strict JSON check.
- Some explanations still include raw numbers without enough meaning.
- One output was still incomplete/truncated.
- Some explanations are vague.
- Some actions are useful, but not always specific enough.

Examples:

```text
139.9209
```

```text
141.0369
```

```text
The risk group is both broad (both
```

Simple meaning:

Model 2 improved, but still needs one more cleanup step before final judging.

## 7. Updated Ratings

### Model 1 Rating

```text
8 / 10
```

Reason:

- Good official test metrics.
- Stable API output.
- Good high-risk detection.
- Useful top risk factors.
- Good enough for dashboard analytics.

Model 1 is ready.

### Model 2 Old Rating

```text
4 / 10
```

Reason:

- It ran, but outputs were messy.
- Too many strange actions and malformed responses.

### Model 2 New Rating

```text
6 / 10
```

Reason:

- Output quality improved.
- Most results are now readable.
- 7 out of 10 outputs passed the JSON structure check.
- Actions are more practical than before.

Why not higher:

- 3 out of 10 outputs still failed JSON validation.
- Some outputs are still incomplete or vague.
- It still does not reliably follow the exact required format.

### Overall System Rating

```text
7 / 10
```

Reason:

- Full API pipeline works.
- Model 1 is strong.
- Model 2 improved after prompt change.
- The system now shows the main idea clearly:

```text
Detect -> Explain -> Recommend Action
```

But Model 2 still needs better output control.

## 8. Final Verdict

The new result is better than the old result.

Model 1 is ready for the dashboard.

Model 2 is usable for demo after filtering/cleaning, but not perfect yet.

For final dashboard, we should:

- use Model 1 outputs directly
- use Model 2 outputs only after validation
- show fallback actions if Model 2 output is invalid

Suggested fallback:

```text
If complaints are unresolved -> complaint_escalation
If balance/spend/activity dropped -> rm_call
If FD is maturing -> rate_offer
If service issue is small -> fee_waiver
If customer is low risk -> do_nothing
```

Simple final statement:

```text
Model 1 detects risk well.
Model 2 improved after prompt tuning, but still needs validation or fallback logic.
```
