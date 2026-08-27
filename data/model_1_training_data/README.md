# Model 1 Training Data

Fake (synthetic) bank data for the churn model. No real customer data is used here.

- Spec: [`dataset/model_1_plan.md`](../../dataset/model_1_plan.md)
- Code that makes this data: [`dataset-scripts/model_1_data/`](../../dataset-scripts/model_1_data/)

---

## 1. What is in this folder

| File | Size | What it is |
|---|---|---|
| `customers.csv` | 53,040 rows × 31 columns | **The training data.** |
| `responsiveness.csv` | 10,000 rows × 8 columns | **Hidden.** For the retention simulator only. Never used to train. |
| `complaint_texts.json` | 360 texts | Pool of complaint messages. This is an **input**, not an output. |
| `README.md` | — | This file. |

---

## 2. Quick numbers

| Thing | Value |
|---|---|
| Customers | 10,000 |
| Customer IDs | `C10000` to `C19999` |
| Total rows | **53,040** |
| Columns | 31 |
| Dates | 6 monthly, `2026-01-01` to `2026-06-01` |
| Rows per customer | 1 to 6 |
| Churn rate | **6.00%** |
| Rows where `churn_flag = 1` | 3,183 |

---

## 3. What one row means

- **One row = one customer on one date.**
- A customer can appear up to 6 times (once per month).
- Example: customer `C10020` has 6 rows, one for each month.

### Why not exactly 60,000 rows?

- 10,000 customers × 6 months would be 60,000 rows.
- But **once a customer churns, we stop recording them.**
- Churn means "gone quiet". A customer who is quiet in April cannot be shown as active in May.
- So their rows stop at the churn month.

| Rows a customer has | How many customers |
|---|---|
| 6 rows (never churned) | 7,406 |
| 5 rows | 673 |
| 4 rows | 615 |
| 3 rows | 517 |
| 2 rows | 439 |
| 1 row | 350 |

Rules that are always true:

- Every customer has **at least 1** and **at most 6** rows.
- A customer has **at most one** row with `churn_flag = 1`.
- That churn row is **always their last row**.

---

## 4. Who the customers are

| Segment | Share | Age range | Income type |
|---|---|---|---|
| `salary` | 35% | 24–55 | regular |
| `pension` | 20% | 58–80 | regular |
| `farmer` | 20% | 30–65 | seasonal |
| `vendor` | 15% | 25–55 | irregular |
| `business` | 10% | 30–60 | irregular |

---

## 5. All 31 columns

### Who they are (3 columns) — never given to the model

| # | Column | Type | Meaning |
|---|---|---|---|
| 1 | `customer_id` | text | `C10000` to `C19999` |
| 2 | `customer_name` | text | Fake Indian name. Duplicates are fine. |
| 3 | `snapshot_date` | date | Which month this row is for |

### About the person (6 columns) — same in all their rows

| # | Column | Type | Meaning |
|---|---|---|---|
| 4 | `age` | number | 24 to 80 |
| 5 | `tenure_months` | number | How long they have banked with us |
| 6 | `customer_segment` | text | salary / pension / farmer / vendor / business |
| 7 | `income_regularity` | text | regular / seasonal / irregular |
| 8 | `customer_yearly_value` | number | What they are worth per year. **Not a model input** (used for ranking risk). |
| 9 | `loyalty` | number | **Hidden.** Secretly used to create the label. **Not a model input.** |

### Products (3 columns) — same in all their rows

| # | Column | Type | Meaning |
|---|---|---|---|
| 10 | `products_count` | number | How many products they hold (1 to 7) |
| 11 | `has_credit_card` | 0 or 1 | |
| 12 | `has_loan` | 0 or 1 | |

### Behaviour (10 columns) — changes every month

| # | Column | Type | Meaning |
|---|---|---|---|
| 13 | `days_since_last_transaction` | number | 0 to 37. Usually the biggest warning sign. |
| 14 | `balance_change_30d` | % | Balance up or down. `-31` means balance fell 31%. |
| 15 | `transaction_change_30d` | % | Number of transactions up or down |
| 16 | `card_spend_change_30d` | % | Card spending up or down |
| 17 | `app_login_change_30d` | % | App logins up or down |
| 18 | `salary_missing_days` | number | Days their salary/pension is late. **Blank for farmer, vendor, business** (they have no fixed salary). |
| 19 | `external_transfer_change_30d` | % | Money moving out to other banks. Going **up** is bad. |
| 20 | `upi_share_of_spend` | 0 to 1 | How much they use UPI. High = drifting to fintech apps. |
| 21 | `fd_maturing_in_30d` | 0 or 1 | Fixed deposit about to mature. A classic moment to leave. |
| 22 | `products_dropped_90d` | number | Products closed recently (0 to 3) |

> All five `%` columns are limited to **−100 to +300**.
> Reason: a balance going ₹500 → ₹1,500 is +200%, but ₹50,000 → ₹40,000 is only −20%. Without a limit, tiny accounts would dominate the model.

### Service and complaints (6 columns) — changes every month

| # | Column | Type | Meaning |
|---|---|---|---|
| 23 | `complaints_30d` | number | Complaints raised this month (0 to 6) |
| 24 | `unresolved_complaints` | number | Still not fixed. Never more than `complaints_30d`. |
| 25 | `failed_transactions_30d` | number | Failed payments (0 to 15) |
| 26 | `avg_resolution_time_hrs` | number | Hours to fix a complaint. `0` when there were no complaints. |
| 27 | `emi_bounce_30d` | 0 or 1 | Loan EMI bounced. Only ever `1` if `has_loan = 1`. |
| 28 | `complaint_text` | text | The actual complaint. Empty when there were no complaints. |

### Decoys (2 columns) — pure noise on purpose

| # | Column | Type | Meaning |
|---|---|---|---|
| 29 | `branch_code` | text | `BR-101` to `BR-140` |
| 30 | `card_colour` | text | blue / green / silver / gold / black |

- These are **deliberately meaningless**.
- They exist so we can prove the model correctly ignores them.
- Checked: churn is statistically unrelated to both.
- **If either shows up as important in the model, something is broken.**

### The answer (1 column)

| # | Column | Type | Meaning |
|---|---|---|---|
| 31 | `churn_flag` | 0 or 1 | `1` = customer went quiet. This is what we predict. |

### Columns the model must NEVER see

```
customer_id, customer_name, snapshot_date,
loyalty, customer_yearly_value, complaint_text, churn_flag
```

- That leaves **24 columns** the model can use.
- If `customer_id` gets in, the model just memorises which customers churn. The score looks great but means nothing.

---

## 6. Example 1 — a customer who CHURNED

**C10015 — Chakradev Kari**

| Field | Value |
|---|---|
| Age | 26 |
| Segment | salary (regular income) |
| Tenure | 61 months (about 5 years) |
| Products | 3 (has a loan, no credit card) |
| Yearly value | ₹31,008 |
| Branch / card | BR-135 / green |

**His 5 months:**

| Month | Days since last txn | Balance % | Card spend % | Money out to other banks % | Salary late (days) | Complaints | Failed txns | **Churn** |
|---|---|---|---|---|---|---|---|---|
| Jan | 10 | **+35** | **+34** | −22 | 1 | 1 | 0 | 0 |
| Feb | 9 | −12 | +12 | +5 | 1 | 0 | 0 | 0 |
| Mar | 16 | −10 | −25 | +25 | 3 | 2 | 2 | 0 |
| Apr | 18 | −13 | −36 | +67 | 5 | 0 | 2 | 0 |
| May | 19 | −35 | −34 | **+44** | 4 | 0 | 1 | **1** |

**What the story is, in plain words:**

- In January he was **fine** — balance up 35%, spending up 34%.
- From February onwards things **slowly got worse every single month**, not suddenly.
- The gap between transactions grew: **10 → 9 → 16 → 18 → 19 days**.
- His balance kept falling and his card spending kept falling.
- Money leaving for **other banks kept rising**: −22% → +67% → +44%.
- His salary started arriving **late**: 1 → 3 → 5 days.
- In May he went quiet. `churn_flag = 1`.
- **His rows stop at May.** There is no June row, because he already left.

His complaints along the way:
> *"Your ATM printed slip saying transaction cancelled but money went out."*
> *"Please confirm my final EMI, the app and passbook show different amounts."*

---

## 7. Example 2 — a customer who did NOT churn

**C10020 — Ekbal Garg**

| Field | Value |
|---|---|
| Age | 44 |
| Segment | salary (regular income) |
| Tenure | 129 months (about 11 years) |
| Products | 3 (has credit card and loan) |
| Yearly value | ₹49,712 |
| Branch / card | BR-121 / gold |

**His 6 months:**

| Month | Days since last txn | Balance % | Card spend % | Money out to other banks % | Salary late (days) | Complaints | Failed txns | **Churn** |
|---|---|---|---|---|---|---|---|---|
| Jan | 5 | +14 | +10 | +10 | 0 | 1 | 0 | 0 |
| Feb | 7 | +2 | +40 | −17 | 0 | 0 | 2 | 0 |
| Mar | 9 | −3 | +30 | +10 | 1 | 0 | 0 | 0 |
| Apr | 15 | +8 | −10 | −12 | 0 | 0 | 0 | 0 |
| May | 2 | +21 | −6 | +3 | 0 | 0 | 2 | 0 |
| Jun | 0 | +16 | +46 | −19 | 0 | 0 | 0 | 0 |

**What the story is, in plain words:**

- His numbers **wobble up and down**, but there is **no downward trend**.
- Transaction gap stays small and even improves: 5 → 15 → 2 → **0 days**.
- Balance is **mostly positive** every month.
- Salary arrives **on time** almost always.
- He did complain once in January, but it got sorted.
- He never churned, so he keeps **all 6 rows**.

He also complained once:
> *"Kindly reissue my card, the chip has stopped reading at merchants."*

### The two side by side

| | C10015 (churned) | C10020 (stayed) |
|---|---|---|
| Rows | 5 (stops early) | 6 (full) |
| Trend | Gets worse every month | Wobbles, no trend |
| Days since last txn | 10 → 19 (rising) | 5 → 0 (fine) |
| Balance | Falls to −35% | Stays positive |
| Money out to other banks | Rises to +67% | Flat |
| Salary late | 1 → 5 days | 0 days |
| Result | **Churned in May** | Still with us |

---

## 8. How the label was decided (important)

**We never used simple rules like "if salary is 7+ days late then churn = 1".**

Why that matters:

- With rules, the model would score 99% and just repeat the rules back to us.
- The whole system would become an expensive `if` statement.
- Anyone who asks how the data was made would see it immediately.

**What we did instead:**

1. Add up a risk **score** from many signals (balance drop, days quiet, complaints, salary late, FD maturing, tenure).
2. Turn that score into a **probability** (0 to 1).
3. **Flip a weighted coin** using that probability.

So:

- A very risky customer might **still stay**.
- A safe-looking customer might **still leave**.
- That is realistic, and it is the whole point.

We also flip an extra **1.5%** of stayers to "churned" at random — real people leave for reasons a bank cannot see. That is about 23% of all churns.

### Behaviour follows a trend, not random noise

Every customer is secretly given one of three states:

| State | Share | What their numbers do |
|---|---|---|
| stable | 70% | Wobble around their normal |
| declining | 20% | Get **worse every month** |
| improving | 10% | Get gradually better |

- **97.7%** of declining customers measurably get worse across their months.
- Farmers also dip during their lean season.
- This is why C10015 above trends down instead of having one random bad month.

### Two different ways to become a risk

Complaints **cause** churn, not the other way round. So there are two separate routes:

| Group | Customers | Churn rate | What their problem is |
|---|---|---|---|
| Behaviour problem | 1,779 | 16.0% | Balance falling, going quiet |
| Service problem | 804 | 18.4% | Complaints, slow fixes, FD maturing |
| **Both at once** | 184 | **32.1%** | Everything wrong |
| Neither | 7,233 | 2.6% | Healthy |

This matters because Model 2 needs to tell **different stories** for different customers, not the same story every time.

---

## 9. The hidden file: `responsiveness.csv`

- One row per customer (10,000 rows).
- **Never joined into training data.**
- It answers: *"if the bank does X, will this customer respond?"*

| Column | Who it works best on |
|---|---|
| `fee_waiver` | Low-value customers, people who complained about fees |
| `rm_call` | Long-tenure customers |
| `complaint_escalation` | People with unresolved complaints |
| `rate_offer` | Pension customers, deposit holders |
| `do_nothing` | Everyone, about 15% |
| `drift_state` | Hidden. stable / declining / improving. |
| `service_shock` | Hidden. Marks the "service problem" group. |

Used through:

```python
simulate_intervention("C10015", "rm_call")  ->  True or False
```

- It flips a weighted coin, so two identical calls can give different answers.
- That is correct for a simulator.

---

## 10. How to split the data for training

**Split by customer, never by row.**

- If you split by row, C10015's January row goes to training and his May row goes to testing.
- The model then just memorises the customer instead of learning the pattern.

| Split | Customers | Churn rate |
|---|---|---|
| Train | 7,000 | 5.96% |
| Validation | 1,500 | 6.06% |
| Test | 1,500 | 6.11% |

---

## 11. How to regenerate this data

Run all three from the **repository root**:

```
pip install -r requirements.txt
python dataset-scripts/model_1_data/generate.py
python dataset-scripts/model_1_data/scripts/check_dataset.py
python -m pytest dataset-scripts/model_1_data/tests -q
```

| Command | What it does |
|---|---|
| `generate.py` | Writes `customers.csv` and `responsiveness.csv` into this folder |
| `check_dataset.py` | Runs all 10 quality checks, prints PASS or FAIL for each |
| `pytest` | Runs 27 tests on the generator |

**The seed is 42.** Running it again gives a **byte-for-byte identical file**.

- All settings live in `dataset-scripts/model_1_data/config.yaml`.
- There are no hard-coded numbers in the Python.
- File paths in that config are relative to the repository root.
- `data/` is in `.gitignore` — do not commit a 53,000 row CSV.

---

## 12. Quality checks — all 10 pass

| # | Check | Result |
|---|---|---|
| 1 | 1–6 rows per customer, one churn row, always last | PASS |
| 2 | Churn rate 4%–8% in every split | PASS — 6.00% |
| 3 | Nobody opened an account before age 18 | PASS — 0 violations |
| 4 | Salary column blank for exactly the right segments | PASS |
| 5 | All % columns inside −100 to +300 | PASS |
| 6 | Decoy columns are truly meaningless | PASS — p = 0.54 and 0.88 |
| 7 | No single value gives 0% or 100% churn | PASS |
| 8 | Declining customers really do trend down | PASS — 97.7% |
| 9 | No customer appears in two splits | PASS |
| 10 | A quick model scores between 0.70 and 0.95 | PASS — **0.8142** |

### How good is the model on this data?

| Metric | Score | Meaning |
|---|---|---|
| ROC-AUC | 0.8142 | Good, and realistic. Not suspiciously perfect. |
| PR-AUC | 0.4489 | The main metric when churn is rare |

**Never report accuracy.** Only 6% of customers churn, so a model that says "nobody will churn" gets **94% accuracy** and is completely useless.
