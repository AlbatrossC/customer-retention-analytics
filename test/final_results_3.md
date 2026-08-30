# Final Results 3

## 1. What This Test Did

This test used random customers from:

```text
model_1/data/customers.csv
```

The script selected 10 customers and sent each latest customer snapshot to:

```text
/predict/both
```

So both models were tested:

- Model 1: XGBoost churn risk model
- Model 2: reason and next action model

API health was good:

```json
{
  "ok": true,
  "model1_loaded": true,
  "model2_loaded": true
}
```

## 2. Compared With Old Result

Old test:

- mostly high-risk customers
- Model 1 predicted all 10 as churn risk
- Model 2 had many bad outputs
- only 7 out of 10 Model 2 outputs passed JSON check after prompt update

New random test:

- includes low-risk and high-risk customers
- Model 1 predicted 8 customers as low risk
- Model 1 predicted 2 customers as high risk
- Model 2 returned valid JSON for all 10 customers

This is a better and more realistic test.

## 3. Overall Ratings

### Model 1 Rating

```text
7.5 / 10
```

Why:

- It gives stable output.
- It correctly identifies many low-risk customers.
- It correctly identifies one churned high-risk customer.
- Top risk factors mostly make sense.

Why not higher:

- It missed one actual churn customer: `C15970`.
- Some low-risk top factors are not very useful, like branch code or card colour.

### Model 2 Rating

```text
6.5 / 10
```

Why:

- JSON format improved a lot.
- All 10 outputs passed the JSON check.
- Most answers are readable.
- Actions are now more normal and less broken.

Why not higher:

- Some explanations are still weak.
- Some actions are too generic.
- For low-risk customers, it sometimes recommends contacting the customer even when no urgent action is needed.
- It sometimes treats small risk signals as more important than they are.

### Full System Rating

```text
7.2 / 10
```

Why:

- API works.
- Both models load.
- Both models return output.
- Model 1 is useful for dashboard analytics.
- Model 2 is improving and usable with validation/fallback logic.

## 4. Customer Wise Results

### 1. Chasmum Atwal (`C10220`)

Input:

- Segment: salary
- Age: 37
- Tenure: 133 months
- Days since last transaction: 8
- Balance change: -2.13%
- Card spend change: +13.38%
- App login change: -23.79%
- Salary missing days: 5
- External transfers change: +70.36%
- Complaints: 0
- Failed transactions: 0
- Actual churn flag: 0

Expected:

- Model 1 should mostly say Low risk / No churn.
- Model 2 should say monitor salary delay and activity, no urgent retention action.

Model 1 output:

- Churn probability: 1.96%
- Risk score: 5.87
- Prediction: No
- Risk level: Low
- Top factors: salary missing days, branch code, app login drop

Model 2 output:

- Why: salary missing days may show account shift
- Action: ask customer about salary shift and branch location

Result:

- Model 1 was correct.
- Model 2 was acceptable, but slightly too active for a low-risk customer.

### 2. Aryan Gola (`C12596`)

Input:

- Segment: salary
- Age: 33
- Tenure: 63 months
- Days since last transaction: 16
- Balance change: -8.97%
- Card spend change: -12.42%
- Salary missing days: 3
- External transfers change: +38.38%
- Complaints: 0
- Failed transactions: 0
- Actual churn flag: 0

Expected:

- Model 1 should say Low risk or Medium watchlist, not high churn.
- Model 2 should suggest light monitoring or customer check-in.

Model 1 output:

- Churn probability: 1.96%
- Risk score: 5.87
- Prediction: No
- Risk level: Low
- Top factors: salary missing days, transaction gap, external transfers

Model 2 output:

- Why: salary missing days may show reduced income stability
- Action: contact customer about decreased payment activity

Result:

- Model 1 was correct.
- Model 2 was okay, but action could be softer.

### 3. Arunima Deol (`C12999`)

Input:

- Segment: salary
- Age: 29
- Tenure: 4 months
- Products count: 1
- Days since last transaction: 1
- Balance change: +12.14%
- Transactions change: +27.87%
- App login change: +23.35%
- Complaints: 1
- Failed transactions: 1
- Products dropped: 1
- Actual churn flag: 0

Expected:

- Model 1 should say Low risk / No churn.
- Model 2 should say customer looks mostly healthy, monitor complaint/product drop.

Model 1 output:

- Churn probability: 1.96%
- Risk score: 5.87
- Prediction: No
- Risk level: Low
- Top factors: low tenure, app login change, products count, product dropped

Model 2 output:

- Why: says high retention-risk signal even though risk score is only 5.87
- Action: contact customer within 24 hours

Result:

- Model 1 was correct.
- Model 2 was weak here because it overreacted to a low-risk customer.

### 4. Vyanjana Mandal (`C14030`)

Input:

- Segment: salary
- Age: 40
- Tenure: 9 months
- Days since last transaction: 16
- Balance change: -5.62%
- Card spend change: -21.49%
- App login change: -14.76%
- Salary missing days: 3
- External transfers change: +31.70%
- Complaints: 0
- Failed transactions: 1
- Actual churn flag: 0

Expected:

- Model 1 should say Low or Medium risk.
- Model 2 should explain reduced engagement and suggest monitoring/check-in.

Model 1 output:

- Churn probability: 7.29%
- Risk score: 21.86
- Prediction: No
- Risk level: Low
- Top factors: low tenure, transaction gap, card spend drop

Model 2 output:

- Why: transaction gap and card spending drop
- Action: contact customer to understand continued poor behavior

Result:

- Model 1 was correct.
- Model 2 was fairly good, but wording could be better.

### 5. Harinakshi Chada (`C14370`)

Input:

- Segment: pension
- Age: 72
- Tenure: 137 months
- Products count: 1
- Days since last transaction: 7
- Balance change: +15.68%
- External transfers change: +25.33%
- Complaints: 0
- Failed transactions: 0
- Actual churn flag: 0

Expected:

- Model 1 should say Low risk / No churn.
- Model 2 should say customer is mostly stable.

Model 1 output:

- Churn probability: 1.96%
- Risk score: 5.87
- Prediction: No
- Risk level: Low
- Top factors: branch code, age, external transfers, products count

Model 2 output:

- Why: branch discrepancy may indicate weaker network engagement
- Action: contact customer to resolve local issue

Result:

- Model 1 was correct.
- Model 2 was weak because branch code is a decoy/noise field and should not be treated as a real reason.

### 6. Arin Tailor (`C15281`)

Input:

- Segment: farmer
- Age: 54
- Tenure: 49 months
- Days since last transaction: 0
- Balance change: +59.16%
- Transactions change: +44.44%
- Card spend change: +42.79%
- App login change: +48.64%
- External transfers change: -100.00%
- Complaints: 0
- Failed transactions: 1
- Actual churn flag: 0

Expected:

- Model 1 should say Low risk / No churn.
- Model 2 should say customer looks healthy and continue monitoring.

Model 1 output:

- Churn probability: 1.65%
- Risk score: 4.96
- Prediction: No
- Risk level: Low
- Top factors: app login change, tenure

Model 2 output:

- Why: mentions app login change and stable pattern
- Action: continue monitoring

Result:

- Model 1 was correct.
- Model 2 was mostly good, but one line says the relationship reduced by 44%, even though activity improved.

### 7. Rishi Barman (`C15970`)

Input:

- Segment: vendor
- Age: 30
- Tenure: 44 months
- Days since last transaction: 12
- Balance change: +0.49%
- Card spend change: -32.65%
- App login change: -20.90%
- Complaints: 1
- Unresolved complaints: 1
- Failed transactions: 3
- Actual churn flag: 1

Expected:

- Since actual churn flag is 1, Model 1 should ideally flag this customer as risk.
- Model 2 should explain service issue and spending drop.

Model 1 output:

- Churn probability: 7.29%
- Risk score: 21.86
- Prediction: No
- Risk level: Low
- Top factors: card spend drop, failed transactions, unresolved complaint

Model 2 output:

- Why: card spend trend dropped
- Action: contact customer about reduced spending and branch issue

Result:

- Model 1 missed this churn customer.
- Model 2 explanation was partly useful.
- This is the weakest Model 1 result in this test.

### 8. Ikbal Jayaraman (`C16651`)

Input:

- Segment: pension
- Age: 68
- Tenure: 136 months
- Days since last transaction: 27
- Balance change: -46.73%
- Transactions change: -48.98%
- Card spend change: -46.85%
- App login change: -47.98%
- Salary missing days: 8
- External transfers change: +100.98%
- Complaints: 0
- Failed transactions: 0
- Actual churn flag: 0

Expected:

- Model 1 should flag high risk because behavior dropped strongly.
- Model 2 should recommend urgent contact.

Model 1 output:

- Churn probability: 48.15%
- Risk score: 80.56
- Prediction: Yes
- Risk level: High
- Top factors: balance drop, transaction gap, salary delay, card spend drop

Model 2 output:

- Why: balance dropped and behavior is trending downward
- Action: contact customer to understand balance decline

Result:

- Model 1 was reasonable.
- Model 2 was good enough, but could recommend a more specific retention action.

### 9. Zaid Borde (`C19126`)

Input:

- Segment: salary
- Age: 46
- Tenure: 2 months
- Days since last transaction: 3
- Balance change: -6.41%
- Salary missing days: 4
- Complaints: 6
- Unresolved complaints: 6
- Failed transactions: 10
- Resolution time: 134.45 hours
- Actual churn flag: 1

Expected:

- Model 1 should say High risk / Churn.
- Model 2 should recommend complaint escalation and urgent contact.

Model 1 output:

- Churn probability: 48.15%
- Risk score: 80.56
- Prediction: Yes
- Risk level: High
- Top factors: resolution time, failed transactions, low tenure, complaints

Model 2 output:

- Why: failed transactions and high resolution time
- Action: ask customer what bank can help with

Result:

- Model 1 was correct.
- Model 2 explanation was good, but action should be stronger: complaint escalation is expected.

### 10. Charles Setty (`C19830`)

Input:

- Segment: pension
- Age: 60
- Tenure: 127 months
- Products count: 1
- Days since last transaction: 1
- Balance change: +24.58%
- Card spend change: +22.40%
- Salary missing days: 2
- External transfers change: -43.20%
- Complaints: 0
- Failed transactions: 2
- Actual churn flag: 0

Expected:

- Model 1 should say Low risk / No churn.
- Model 2 should say continue monitoring or no urgent action.

Model 1 output:

- Churn probability: 1.96%
- Risk score: 5.87
- Prediction: No
- Risk level: Low
- Top factors: failed transactions, salary missing days, products count

Model 2 output:

- Why: failed transactions, fewer products, stable monthly pattern
- Action: continue monitoring

Result:

- Model 1 was correct.
- Model 2 was mostly good, but the phrase "composes" is not polished.

## 5. Final Summary

Model 1:

- Correct for 9 out of 10 customers when compared with `churn_flag`.
- Missed customer `C15970`, who actually churned.
- Correctly flagged customer `C19126`, who actually churned.
- Also flagged `C16651` as high risk even though churn flag was 0, but that customer had very risky behavior.

Model 2:

- Returned valid JSON for all 10 customers.
- Improved compared with old results.
- Still needs better business action quality.
- Should avoid using weak/noisy fields like branch code as reasons.
- Should recommend stronger actions for service-risk cases.

## 6. Final Verdict

The new random-customer result is better and more realistic than the old result.

Model 1 is strong enough for the dashboard.

Model 2 is now technically usable, but still needs cleanup before final presentation.

Best dashboard approach:

- use Model 1 result directly
- validate Model 2 JSON
- show Model 2 only if output is valid and useful
- use fallback action rules when Model 2 output is weak

Final simple rating:

```text
Model 1: 7.5 / 10
Model 2: 6.5 / 10
Overall: 7.2 / 10
```
