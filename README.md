# Customer Retention through Analytics

> **Problem Statement:** Utilizing AI/ML to analyze customer data and develop strategies to improve member retention rates in banking services.

---

## What This Project Does

Banks lose customers every day — some leave quietly, others storm out after a bad experience. By the time the bank notices, it's too late. This project fixes that.

We built a **two-model AI pipeline** that:
1. **Detects** which customers are about to leave (30 days in advance)
2. **Explains** exactly *why* each customer is unhappy
3. **Recommends** the best retention action for each case
4. **Displays** everything in a real-time dashboard for bank managers

```
 ╔═══════════════════════════════════════════════════════════════════════════╗
 ║     Detect  ──►  Explain  ──►  Prioritize  ──►  Act  ──►  Measure      ║
 ╚═══════════════════════════════════════════════════════════════════════════╝

 ┌───────────────┐    ┌──────────────────────┐    ┌──────────────────────┐    ┌────────────────┐
 │   Bank Data   │───►│   Model 1 (XGBoost)  │───►│  Model 2 (Fine-     │───►│   Dashboard    │───► Better
 │  10k Customers│    │  "Will they leave?"   │    │  Tuned LLM)         │    │  (Flask App)   │     Retention
 │  6-Month      │    │                      │    │  "Why? What to do?" │    │                │
 │  History      │    │  Output:             │    │                      │    │  • KPI Cards   │
 │               │    │  • Churn Probability  │    │  Output:             │    │  • Charts      │
 │  31 Columns   │    │  • Risk Level         │    │  • Root Cause        │    │  • Customer    │
 │  per Month    │    │  • Top 5 Risk Factors │    │  • Urgency           │    │    360° View   │
 │               │    │  (via SHAP)           │    │  • Recommended Action│    │  • Action      │
 │               │    │                      │    │  • Evidence           │    │    Worklists   │
 └───────────────┘    └──────────────────────┘    └──────────────────────┘    └────────────────┘
```

### How a Customer Case Flows Through the System

**Example: Priya Sharma (Customer C10042)**

```
Step 1 — Bank Data:
  35 transactions/month → dropped to 10
  2 unresolved complaints (3+ months old)
  Balance dropping, external transfers rising

Step 2 — Model 1 says:
  Churn Probability: 82%
  Risk Level: HIGH
  Top Factors: (1) transactions down, (2) unresolved complaints, (3) external transfers up

Step 3 — Model 2 says:
  Why: "Customer activity dropped for 3 months and complaints remain unresolved."
  Action: COMPLAINT_ESCALATION
  Urgency: HIGH

Step 4 — Dashboard shows:
  → RM gets a call task
  → Complaint gets escalated to senior manager
  → Fee waiver offered if suitable
```

---

## Quickstart — Running the Frontend Dashboard

The web dashboard is built with **Flask** and is powered by a pre-populated SQLite database (`database/customer_retention.db`). No model inference needed — all predictions are precomputed.

> **We recommend using [`uv`](https://github.com/astral-sh/uv)** — an extremely fast Python package and environment manager (10-100x faster than pip).

### Step 1: Install `uv`

**Windows (PowerShell):**
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

**macOS / Linux:**
```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

*(Alternatively: `pip install uv`)*

### Step 2: Create & Activate Virtual Environment

```powershell
# Navigate to the repo root
cd customer-retention-analytics

# Create a virtual environment
uv venv

# Activate it (Windows PowerShell)
.venv\Scripts\activate

# Or on Linux / macOS
# source .venv/bin/activate
```

### Step 3: Install Dependencies

For running the **Dashboard / Web App & Vercel deployment** (lightweight):
```powershell
uv pip install -r requirements.txt
```

For **full ML pipeline & model training** (includes XGBoost, SHAP, LightGBM, FastAPI):
```powershell
uv pip install -r requirements-ml.txt
```

### Step 4: Launch the Dashboard

```powershell
python app.py
```

Open your browser at: **http://127.0.0.1:5000**

The dashboard has 5 sections:
- **Overview** — KPI cards, risk distribution charts, revenue at risk
- **Customer Directory** — Searchable table of all 10,000 customers with filters
- **Individual Analysis** — Deep 360° view of any single customer
- **Cluster Analysis** — Customers grouped by churn reason patterns
- **Visualizations** — Monthly behavioral trends, segment comparisons, risk factor analysis

---

## Deploying to Vercel

The project includes `vercel.json` and `.vercelignore` to deploy the Flask dashboard & precomputed SQLite database as a serverless web app on Vercel:

1. Push the repository to GitHub.
2. In the [Vercel Dashboard](https://vercel.com), click **Add New...** $\rightarrow$ **Project** and import your repository.
3. Keep default settings (`Other` framework preset, root `./`) and click **Deploy**.
4. Vercel will install `requirements.txt` and serve the dashboard globally.

---

## Key Numbers at a Glance

| Metric | Value |
|---|---|
| Total Customers | **10,000** |
| High Risk (likely to churn) | **2,142** (21.4%) |
| Medium Risk (early warnings) | **973** (9.7%) |
| Low Risk (healthy) | **6,885** (68.9%) |
| Customers analyzed by Model 2 (AI reasoning) | **3,803** |
| Churn reasons detected | **9 categories** (e.g., Service Dissatisfaction, Financial Stress, Digital Friction) |
| Retention actions recommended | **10 types** (e.g., Complaint Escalation, RM Callback, Fee Waiver) |
| Most common churn reason | **Service Dissatisfaction** (2,127 customers / 55.9%) |
| Most recommended action | **Complaint Escalation** (1,623 customers / 42.7%) |
| Cases needing immediate intervention (HIGH urgency) | **1,109 customers** |

---

## Tech Stack

| Component | Technology | Purpose |
|---|---|---|
| **Frontend** | Flask + Jinja2 + Vanilla JS + Chart.js | Interactive retention dashboard |
| **Database** | SQLite (`customer_retention.db`, ~23 MB) | Stores all customers, predictions, and evidence |
| **Model 1** | XGBoost (3-seed ensemble) + SHAP | Churn probability & explainable risk factors |
| **Model 2** | Qwen2.5-3B-Instruct + LoRA fine-tuning | Root cause analysis & action recommendation |
| **Model Serving** | FastAPI + Ollama (local) / Google Colab (GPU) | Real-time and batch inference APIs |
| **Preprocessing** | Python + pandas | Feature engineering & batch pipeline orchestration |

---

## Documentation

All detailed technical documentation lives in the [`docs/`](docs/) folder:

| Document | What It Covers |
|---|---|
| 📊 [**Dataset**](docs/dataset.md) | All 31 columns explained, customer segments, 6-month longitudinal structure, synthetic data generation method |
| 🌲 [**Model 1 — Churn Prediction**](docs/model_1.md) | XGBoost architecture, 69 engineered features, SHAP explainability, sigmoid calibration, evaluation metrics (ROC-AUC, PR-AUC, recall) |
| 🤖 [**Model 2 — Reason & Action**](docs/model_2.md) | Fine-tuned LLM details, V1 → V2 training history, approved reason/action taxonomies, input/output schemas, evaluation benchmarks |
| ⚙️ [**Backend & Model Serving**](docs/backend.md) | FastAPI servers, Ollama GGUF integration, Google Colab GPU notebook, exact system prompt and decision rules used by Model 2 |
| 🔄 [**Preprocessing & Outputs**](docs/pre_processing.md) | Batch pipeline scripts, all 4 output JSON files with exact counts, risk breakdowns, and processing times |
| 🗄️ [**Database Schema**](docs/database.md) | All 6 tables with column-level documentation, schema.sql DDL, entity-relationship diagram, example SQL queries |

---

## Repository Structure

```
customer-retention-analytics/
│
├── app.py                        # Flask web server (dashboard entry point)
├── requirements.txt              # Python dependencies
├── Modelfile                     # Ollama model config for local LLM serving
│
├── docs/                         # 📖 Technical documentation
│   ├── dataset.md                #    Dataset feature dictionary & generation methodology
│   ├── model_1.md                #    Model 1 (XGBoost) architecture & metrics
│   ├── model_2.md                #    Model 2 (LLM) fine-tuning & evaluation
│   ├── backend.md                #    Backend API servers & Model 2 prompts
│   ├── pre_processing.md         #    Batch processing pipeline & output breakdowns
│   └── database.md               #    SQLite schema, ERD & SQL recipes
│
├── frontend/                     # 🖥️ Dashboard UI layer
│   ├── templates/
│   │   └── index.html            #    Single-page app template (~42 KB)
│   └── static/
│       ├── css/style.css         #    Dashboard styling (~59 KB)
│       └── js/dashboard.js       #    Client-side logic & charts (~90 KB)
│
├── database/                     # 🗄️ SQLite persistence
│   ├── customer_retention.db     #    Pre-populated database (~23 MB)
│   ├── schema.sql                #    Table DDL definitions
│   ├── build_db.py               #    Rebuild DB from JSON outputs
│   ├── insert_low_risk_model2.py #    Add borderline low-risk Model 2 results
│   └── check_db.py               #    Diagnostic row counts & integrity checks
│
├── model_1_v2/                   # 🌲 Model 1 — Churn prediction (XGBoost)
│   ├── data/                     #    Source CSVs: customers.csv, complaints, responsiveness
│   └── training_scripts/
│       └── xgboost_model1_v2/
│           ├── build_features.py #    69-feature engineering pipeline
│           ├── train_xgboost_v2.py#   Training with 3-seed ensemble
│           └── artifacts/        #    Saved models, calibrators, metrics JSON
│
├── devangs_fine_tuned/           # 🤖 Model 2 — Reason & Action (Fine-tuned LLM)
│   ├── src/                      #    Inference engine, schema validators, config
│   ├── evaluation/RESULTS.md     #    Official evaluation benchmarks
│   ├── examples/                 #    Sample input/output JSON files
│   ├── notebooks/                #    LoRA refinement Jupyter notebook
│   └── model2_v2_finetuned (1)/  #    V2 LoRA adapter weights
│
├── backend/                      # ⚙️ Model serving APIs
│   ├── retention_api_server.py   #    Integrated Model 1 + Model 2 FastAPI (port 8000)
│   ├── devang_api_server.py      #    Dedicated Model 2 FastAPI via Ollama (port 8001)
│   ├── colab_api.ipynb           #    Google Colab GPU inference notebook
│   └── model1_batch_outputs.py   #    Batch scoring utility
│
└── pre_processing/               # 🔄 Batch pipeline orchestration
    ├── run_model_1_v2.py         #    Score all 10k customers through Model 1
    ├── run_devang_pipeline.py    #    Run Model 2 on High/Medium risk customers
    ├── run_top_low_risk_pipeline.py # Run Model 2 on borderline Low risk
    └── outputs/                  #    Precomputed JSON results (4 files, ~183 MB total)
```
