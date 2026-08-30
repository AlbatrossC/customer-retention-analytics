# Colab API Test Results

- API URL: `https://encryption-shall-foster-overall.trycloudflare.com`
- Created at: `2026-08-29T15:57:18`
- Customers tested: `10`
- Health: `{"ok": true, "model1_loaded": true, "model2_loaded": true}`

## Summary

| # | Customer | Risk | Prediction | Model 2 Status | JSON |
|---:|---|---:|---|---|---|
| 1 | Chasmum Atwal (`C10220`) | 1.96% | No | OK | Valid |
| 2 | Aryan Gola (`C12596`) | 1.96% | No | OK | Valid |
| 3 | Arunima Deol (`C12999`) | 1.96% | No | OK | Valid |
| 4 | Vyanjana Mandal (`C14030`) | 7.29% | No | OK | Valid |
| 5 | Harinakshi Chada (`C14370`) | 1.96% | No | OK | Valid |
| 6 | Arin Tailor (`C15281`) | 1.65% | No | OK | Valid |
| 7 | Rishi Barman (`C15970`) | 7.29% | No | OK | Valid |
| 8 | Ikbal Jayaraman (`C16651`) | 48.15% | Yes | OK | Valid |
| 9 | Zaid Borde (`C19126`) | 48.15% | Yes | OK | Valid |
| 10 | Charles Setty (`C19830`) | 1.96% | No | OK | Valid |

## Customer Details

### 1. Chasmum Atwal (`C10220`)

- Snapshot date: `2026-06-01`
- Status: `OK`

**Model 1 Output**

- Churn probability: `1.96`
- Risk score: `5.87`
- Churn prediction: `No`
- Risk level: `Low`

Top risk factors:

- salary_missing_days: 5.0<br>- branch_code: BR-101<br>- app_login_change_30d: -23.7924<br>- customer_segment: salary<br>- income_regularity: regular

**Model 2 Output**

Why:

- The customer has 5 missing salary day(s), suggesting funds may be moving through the bank.

Next actions:

- Ask the customer why the preferred bank account has shifted by 5 days.<br>- Verify if the branch code is correct and nearby for the customer's current location.

### 2. Aryan Gola (`C12596`)

- Snapshot date: `2026-06-01`
- Status: `OK`

**Model 1 Output**

- Churn probability: `1.96`
- Risk score: `5.87`
- Churn prediction: `No`
- Risk level: `Low`

Top risk factors:

- salary_missing_days: 3.0<br>- days_since_last_transaction: 16<br>- external_transfer_change_30d: 38.3777<br>- card_colour: blue<br>- customer_segment: salary

**Model 2 Output**

Why:

- The customer has 3 missing salary day(s), which could indicate reduced income stability.

Next actions:

- Contact the customer to understand the specific reason behind the decreased payment activity and confirm the same.

### 3. Arunima Deol (`C12999`)

- Snapshot date: `2026-06-01`
- Status: `OK`

**Model 1 Output**

- Churn probability: `1.96`
- Risk score: `5.87`
- Churn prediction: `No`
- Risk level: `Low`

Top risk factors:

- tenure_months: 4<br>- app_login_change_30d: 23.3539<br>- products_count: 1<br>- customer_segment: salary<br>- products_dropped_90d: 1

**Model 2 Output**

Why:

- The customer has a high retention-risk signal indicated by a high churn probability and a risk score of 5.87.

Next actions:

- Contact the customer within 24 hours to discuss the recent behavior and what would help improve friction.

### 4. Vyanjana Mandal (`C14030`)

- Snapshot date: `2026-06-01`
- Status: `OK`

**Model 1 Output**

- Churn probability: `7.29`
- Risk score: `21.86`
- Churn prediction: `No`
- Risk level: `Low`

Top risk factors:

- tenure_months: 9<br>- days_since_last_transaction: 16<br>- card_spend_change_30d: -21.4877<br>- salary_missing_days: 3.0<br>- branch_code: BR-121

**Model 2 Output**

Why:

- The customer has a 16-day gap since the last transaction, indicating weaker recent engagement.<br>- A -21.5% change in card spending suggests the customer is using the bank less for regular purchases.<br>- The recent monthly pattern is stable, which reduces urgency but does not remove the need to monitor for emerging trends.

Next actions:

- Contact the customer to understand the reason for the continued poor behavior and what would help improve things.

### 5. Harinakshi Chada (`C14370`)

- Snapshot date: `2026-06-01`
- Status: `OK`

**Model 1 Output**

- Churn probability: `1.96`
- Risk score: `5.87`
- Churn prediction: `No`
- Risk level: `Low`

Top risk factors:

- branch_code: BR-108<br>- age: 72<br>- external_transfer_change_30d: 25.3302<br>- products_count: 1<br>- customer_segment: pension

**Model 2 Output**

Why:

- Branch code BR-108 is showing a relevant branch discrepancy that could indicate weaker network engagement.

Next actions:

- Contact the customer to see if the issue is local and resolve it quickly.

### 6. Arin Tailor (`C15281`)

- Snapshot date: `2026-06-01`
- Status: `OK`

**Model 1 Output**

- Churn probability: `1.65`
- Risk score: `4.96`
- Churn prediction: `No`
- Risk level: `Low`

Top risk factors:

- app_login_change_30d: 48.644<br>- tenure_months: 49

**Model 2 Output**

Why:

- The customer has a 48% change in their app login activity over the last 30 days.<br>- The customer has reduced their relationship with the bank by 44% over the last 30 days.<br>- The recent monthly pattern is stable, so no immediate risk signal is pointing to a change in behavior.

Next actions:

- Continue monitoring the latest trend and recent complaint activity.

### 7. Rishi Barman (`C15970`)

- Snapshot date: `2026-05-01`
- Status: `OK`

**Model 1 Output**

- Churn probability: `7.29`
- Risk score: `21.86`
- Churn prediction: `No`
- Risk level: `Low`

Top risk factors:

- card_spend_change_30d: -32.6523<br>- failed_transactions_30d: 3<br>- tenure_months: 44<br>- unresolved_complaints: 1<br>- external_transfer_change_30d: 7.2381

**Model 2 Output**

Why:

- The customer has -32% in a spend trend change over the last 30 days, suggesting funds may be moving towards the bank.

Next actions:

- Contact the customer to understand the full reason behind the reduced spending and confirm if the issue is still occurring at the same or nearby branches.

### 8. Ikbal Jayaraman (`C16651`)

- Snapshot date: `2026-06-01`
- Status: `OK`

**Model 1 Output**

- Churn probability: `48.15`
- Risk score: `80.56`
- Churn prediction: `Yes`
- Risk level: `High`

Top risk factors:

- balance_change_30d: -46.7293<br>- days_since_last_transaction: 27<br>- salary_missing_days: 8.0<br>- card_spend_change_30d: -46.8531<br>- age: 68

**Model 2 Output**

Why:

- The customer recorded a -47% change in their overall balance over the last 30 days.<br>- The recent behavior is trending downward, making early intervention more useful.

Next actions:

- Contact the customer to understand the specific reason behind the -46.73% change in balance and what it means for the customer's financial situation.

### 9. Zaid Borde (`C19126`)

- Snapshot date: `2026-01-01`
- Status: `OK`

**Model 1 Output**

- Churn probability: `48.15`
- Risk score: `80.56`
- Churn prediction: `Yes`
- Risk level: `High`

Top risk factors:

- avg_resolution_time_hrs: 134.4477<br>- failed_transactions_30d: 10<br>- tenure_months: 2<br>- complaints_30d: 6<br>- salary_missing_days: 4.0

**Model 2 Output**

Why:

- The customer has 6 failed transaction(s) in the last 30 days, which can discourage continued usage.<br>- The customer has a high risk signal indicated by a high resolution time average (134 hours).

Next actions:

- Ask the customer why the latest behavior is causing concern and what they would like the bank to help with.

### 10. Charles Setty (`C19830`)

- Snapshot date: `2026-06-01`
- Status: `OK`

**Model 1 Output**

- Churn probability: `1.96`
- Risk score: `5.87`
- Churn prediction: `No`
- Risk level: `Low`

Top risk factors:

- failed_transactions_30d: 2<br>- salary_missing_days: 2.0<br>- products_count: 1<br>- customer_segment: pension<br>- has_loan: 0

**Model 2 Output**

Why:

- The customer has 2 failed transaction(s) in the last 30 days.<br>- The pension segment has fewer products than other segments, which can reduce flexibility.<br>- The recent monthly pattern is stable, so no sudden change warrants intervention.

Next actions:

- Continue monitoring the recent behavior and composes. For now, keep the relationship strong rather than weakening it.
