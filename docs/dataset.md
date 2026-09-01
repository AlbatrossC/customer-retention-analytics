# Customer Banking Dataset

## What Is This Dataset?

This is a **synthetic (fake but realistic)** dataset of 10,000 retail banking customers tracked over 6 months (January–June 2026). It simulates the kind of data a real Indian bank would have — monthly transaction patterns, complaint tickets, salary deposits, app usage, and more.

No real customer data was used anywhere.

### Quick Facts

| Fact | Value |
|---|---|
| Total customers | **10,000** (IDs: `C10000` to `C19999`) |
| Total monthly snapshot rows | **53,040** |
| Columns per row | **31** |
| Time window | **6 months** (Jan 2026 – Jun 2026) |
| Overall churn rate | **~6%** (3,183 churn events) |
| Source file | `model_1_v2/data/customers.csv` (~10 MB) |

---

## How to Read the Data

Each row in `customers.csv` = **one customer on one specific month**.

A customer can have anywhere from 1 to 6 rows:
- If they **never churned**, they have **6 rows** (one per month).
- If they **churned in March**, they have **3 rows** (Jan, Feb, Mar) — and their March row has `churn_flag = 1`. No rows after that, because they already left.

| Rows per Customer | Count | What Happened |
|---|---|---|
| 6 rows | 7,406 | Never churned — stayed all 6 months |
| 5 rows | 673 | Churned in month 5 |
| 4 rows | 615 | Churned in month 4 |
| 3 rows | 517 | Churned in month 3 |
| 2 rows | 439 | Churned in month 2 |
| 1 row | 350 | Churned in month 1 |

**Rules that always hold:**
- Every customer has **at least 1** and **at most 6** rows.
- A customer has **at most one** row with `churn_flag = 1`.
- That churn row is **always their last row** — rows stop after churn.

---

## Customer Segments

The 10,000 customers belong to five occupational segments, each with different banking behaviors:

| Segment | Share | Age Range | Income Pattern | Typical Banking Behavior |
|---|---|---|---|---|
| `salary` | 35% | 24–55 | Regular monthly paycheck | Active digital banking, credit cards, personal loans |
| `pension` | 20% | 58–80 | Regular monthly pension | Branch-heavy, conservative, fixed deposits |
| `farmer` | 20% | 30–65 | Seasonal (harvest cycles) | Seasonal balance swings, crop loans |
| `vendor` | 15% | 25–55 | Irregular (daily sales) | High-frequency UPI, small ticket transactions |
| `business` | 10% | 30–60 | Irregular (commercial) | Larger balances, business credit lines |

---

## All 31 Columns Explained

### Group 1: Identifiers (3 columns) — NOT used by models

| Column | Type | What It Means |
|---|---|---|
| `customer_id` | Text | Unique ID like `C10015` |
| `customer_name` | Text | Fake Indian name |
| `snapshot_date` | Date | Which month this row is for (e.g., `2026-03-01`) |

### Group 2: Customer Profile (6 columns) — Same across all their rows

| Column | Type | What It Means | Used by Model? |
|---|---|---|---|
| `age` | Integer | Customer's age (24–80) | ❌ Blocked (fairness) |
| `tenure_months` | Integer | How many months they've been with the bank | ✅ Yes |
| `customer_segment` | Text | salary / pension / farmer / vendor / business | ✅ Yes |
| `income_regularity` | Text | regular / irregular / seasonal | ✅ Yes |
| `customer_yearly_value` | Float | Annual revenue they generate for the bank (₹) | ❌ Blocked (used for prioritization only) |
| `loyalty` | Float | Hidden score used to generate the churn label | ❌ Blocked (would be cheating) |

### Group 3: Products Held (3 columns)

| Column | Type | What It Means |
|---|---|---|
| `products_count` | Integer | Number of banking products held (1–7) |
| `has_credit_card` | 0 or 1 | Has a credit card? |
| `has_loan` | 0 or 1 | Has a loan? |

### Group 4: Monthly Behavioral Signals (10 columns) — Changes every month

| Column | Type | What It Means | Why It Matters for Churn |
|---|---|---|---|
| `days_since_last_transaction` | Integer (0–37) | Days since they last did anything | High = going quiet, biggest warning sign |
| `balance_change_30d` | % (-100 to +300) | Account balance up or down | Sustained drops = leaving |
| `transaction_change_30d` | % | Number of transactions up or down | Fewer transactions = disengaging |
| `card_spend_change_30d` | % | Card spending up or down | Dropping card use = migrating elsewhere |
| `app_login_change_30d` | % | Mobile app logins up or down | Less app usage = losing interest |
| `salary_missing_days` | Integer or Null | Days salary/pension is late | Late salary = financial stress. Null for non-salaried. |
| `external_transfer_change_30d` | % | Money sent OUT to other banks | Going UP = sending money to competitors |
| `upi_share_of_spend` | 0.0 – 1.0 | Fraction of spend via UPI | High = drifting to fintech apps like PhonePe/GPay |
| `fd_maturing_in_30d` | 0 or 1 | FD about to mature? | Classic moment customers consider leaving |
| `products_dropped_90d` | Integer (0–3) | Products closed recently | Closing products = one foot out the door |

### Group 5: Service & Complaints (6 columns)

| Column | Type | What It Means |
|---|---|---|
| `complaints_30d` | Integer (0–6) | How many complaints filed this month |
| `unresolved_complaints` | Integer | How many complaints are STILL not resolved |
| `failed_transactions_30d` | Integer (0–15) | How many transactions failed (ATM, POS, online) |
| `avg_resolution_time_hrs` | Float | Average hours taken to resolve complaints (0 = no complaints) |
| `emi_bounce_30d` | 0 or 1 | Did a loan EMI payment bounce? (only if `has_loan = 1`) |
| `complaint_text` | Text or Null | Actual complaint text filed by the customer. Null if none. |

### Group 6: Decoys & Target (3 columns)

| Column | Type | Role |
|---|---|---|
| `branch_code` | Text | **Deliberate noise** (`BR-101` to `BR-140`). Statistically unrelated to churn. Exists to test if models correctly ignore it. |
| `card_colour` | Text | **Deliberate noise** (blue/green/silver/gold/black). If this shows up as important, the model is broken. |
| `churn_flag` | 0 or 1 | **The target label.** `1` = customer churned (went quiet). This is what we predict. |

---

## Concrete Example: A Customer Who Churned

**C10015 — Chakradev Kari** (salary segment, age 26, 5-year tenure, 3 products)

| Month | Days Quiet | Balance % | Card Spend % | Money OUT % | Salary Late | Complaints | Churn |
|---|---|---|---|---|---|---|---|
| Jan | 10 | **+35%** | **+34%** | −22% | 1 day | 1 | 0 |
| Feb | 9 | −12% | +12% | +5% | 1 day | 0 | 0 |
| Mar | 16 | −10% | −25% | +25% | 3 days | 2 | 0 |
| Apr | 18 | −13% | −36% | +67% | 5 days | 0 | 0 |
| **May** | **19** | **−35%** | **−34%** | **+44%** | **4 days** | **0** | **1** ✗ |

**The story in plain words:**
- January: Fine — balance up, spending up.
- February onwards: **Every single metric gets worse, every single month.** Not a sudden crash, a slow decline.
- Inactivity gap grows: 10 → 9 → 16 → 18 → **19 days** between transactions.
- Balance keeps falling. Card spending keeps falling.
- Money flowing OUT to other banks: −22% → +67% → +44% (competitor migration).
- Salary arriving **later and later**: 1 → 3 → 5 days.
- May: Goes quiet. `churn_flag = 1`. **No June row** — he's gone.

---

## How the Churn Label Was Generated

We did **NOT** use simple rules like "if salary is 7+ days late → churn = 1". That would make the model just memorize the rules and score 99% (useless).

Instead:
1. We compute a **risk score** from many signals (balance drop, inactivity, complaints, salary delays, FD maturity, tenure).
2. We convert it to a **probability** between 0 and 1.
3. We **flip a weighted coin** — high-risk customers are more likely to churn, but it's not guaranteed. Safe-looking customers can also leave.
4. An extra **1.5% of retained customers** are randomly flipped to churned (people leave for reasons banks can't observe).

Each customer also has a hidden behavioral trajectory:
- **70% Stable** — numbers wobble around normal
- **20% Declining** — gets worse every month (like C10015 above)
- **10% Improving** — getting gradually better

---

## Other Files in the Data Folder

| File | Size | What It Is |
|---|---|---|
| `customers.csv` | ~10 MB | **The main dataset** (53,040 rows × 31 columns) |
| `customers_model_1_v2.csv` | ~25.6 MB | Expanded dataset with 69 engineered features (generated by `build_features.py`) |
| `complaint_texts.json` | ~74 KB | Pool of 360 complaint message templates |
| `complaint_texts_with_customer_id.json` | ~5.4 MB | Complaint texts linked to specific customer IDs (used by Model 2) |
| `responsiveness.csv` | ~1.1 MB | Hidden simulator data (10,000 rows). **Never used for training.** Used to simulate "if bank does X action, will customer respond?" |

### Data Splitting Rules

> ⚠️ **Always split by customer ID, never by row.** If you split by row, the same customer's January row goes to training and their May row goes to testing — the model just memorizes the customer instead of learning patterns.

| Split | Customers | Rows | Churn Rate |
|---|---|---|---|
| Training | 6,755 (70%) | 30,120 | ~6.58% |
| Fit Validation | 723 (7.5%) | 3,245 | ~6.53% |
| Calibration | 724 (7.5%) | 3,258 | ~6.54% |
| Test | 1,448 (15%) | 6,417 | ~6.62% |
