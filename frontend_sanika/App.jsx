import { useState } from "react";
import {
  PieChart,
  Pie,
  Cell,
  Tooltip,
  Legend,
  ResponsiveContainer,
} from "recharts";
import "./App.css";

const API_URL = "http://127.0.0.1:8000";

function App() {
  const [loggedIn, setLoggedIn] = useState(false);
  const [customerId, setCustomerId] = useState("CUST001");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const [result, setResult] = useState(null);

  // --------------------------------------------------
  // DEMO CUSTOMER DATA
  // Replace these values with your actual dataset values
  // --------------------------------------------------

  const customerData = {
    customer_id: customerId,
    customer_name: "Demo Customer",

    profile: {
      customer_segment: "Mass Market",
      income_regularity: "Regular",
      value_tier: "High",
      tenure_months: 48,
      products_count: 3,
      has_credit_card: 1,
      has_loan: 1,
    },

    monthly_history: [
      {
        snapshot_date: "2026-04-01",

        days_since_last_transaction: 3,
        balance_change_30d: -4,
        transaction_change_30d: -3,
        card_spend_change_30d: -2,
        app_login_change_30d: -5,
        salary_missing_days: 0,
        external_transfer_change_30d: 5,
        upi_share_of_spend: 0.45,
        fd_maturing_in_30d: 0,
        products_dropped_90d: 0,
        complaints_30d: 0,
        unresolved_complaints: 0,
        failed_transactions_30d: 0,
        avg_resolution_time_hrs: 12,
        emi_bounce_30d: 0,
      },

      {
        snapshot_date: "2026-05-01",

        days_since_last_transaction: 7,
        balance_change_30d: -8,
        transaction_change_30d: -10,
        card_spend_change_30d: -8,
        app_login_change_30d: -12,
        salary_missing_days: 0,
        external_transfer_change_30d: 10,
        upi_share_of_spend: 0.50,
        fd_maturing_in_30d: 0,
        products_dropped_90d: 0,
        complaints_30d: 1,
        unresolved_complaints: 0,
        failed_transactions_30d: 1,
        avg_resolution_time_hrs: 20,
        emi_bounce_30d: 0,
      },

      {
        snapshot_date: "2026-06-01",

        days_since_last_transaction: 12,
        balance_change_30d: -18,
        transaction_change_30d: -22,
        card_spend_change_30d: -18,
        app_login_change_30d: -28,
        salary_missing_days: 0,
        external_transfer_change_30d: 30,
        upi_share_of_spend: 0.68,
        fd_maturing_in_30d: 1,
        products_dropped_90d: 1,
        complaints_30d: 2,
        unresolved_complaints: 1,
        failed_transactions_30d: 2,
        avg_resolution_time_hrs: 50,
        emi_bounce_30d: 1,
      },
    ],

    extra_context: {
      customer_profile: {
        segment: "Mass Market",
        income_regularity: "Regular",
        value_tier: "High",
        tenure_months: 48,
        products_count: 3,
        has_credit_card: 1,
        has_loan: 1,
      },

      risk_group: "high",

      recent_complaint_text:
        "Customer reported a failed transaction and requested assistance.",

      trend_last_3_months: {
        overall_direction: "declining",
        balance_change_30d: [-4, -8, -18],
        days_since_last_transaction: [3, 7, 12],
        complaints_30d: [0, 1, 2],
        external_transfer_change_30d: [5, 10, 30],
      },
    },
  };

  // --------------------------------------------------
  // CALL BACKEND
  // --------------------------------------------------

  const runPrediction = async () => {
    setLoading(true);
    setError("");

    try {
      const response = await fetch(`${API_URL}/predict/both`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(customerData),
      });

      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.detail || "Prediction failed");
      }

      const data = await response.json();

      console.log("Backend response:", data);

      setResult(data);
    } catch (err) {
      console.error(err);

      setError(
        err.message ||
          "Unable to connect to backend. Make sure FastAPI is running."
      );
    } finally {
      setLoading(false);
    }
  };

  // --------------------------------------------------
  // LOGIN SCREEN
  // --------------------------------------------------

  if (!loggedIn) {
    return (
      <div className="login-page">
        <div className="login-card">
          <h1>Banking Retention Analytics</h1>

          <p>Manager Login</p>

          <input
            type="text"
            placeholder="Manager ID"
            defaultValue="manager001"
          />

          <input
            type="password"
            placeholder="Password"
            defaultValue="123456"
          />

          <button onClick={() => setLoggedIn(true)}>
            Login
          </button>

          <small>Customer Retention Analytics System</small>
        </div>
      </div>
    );
  }

  // --------------------------------------------------
  // EXTRACT BACKEND RESULTS
  // --------------------------------------------------

  const model1 = result?.model1;
  const model2 = result?.model2;

  const churnProbability = model1?.churn_probability ?? 0;
  const riskScore = model1?.risk_score ?? 0;
  const riskLevel = model1?.risk_level ?? "Not analyzed";

  const riskFactors = model1?.top_risk_factors || [];
  const recommendations = model2?.actions || [];

  // --------------------------------------------------
  // CHART DATA
  // --------------------------------------------------

  const riskChartData = model1
    ? [
        {
          name: "Churn Risk",
          value: churnProbability,
        },
        {
          name: "Remaining",
          value: 100 - churnProbability,
        },
      ]
    : [];

  // --------------------------------------------------
  // DASHBOARD
  // --------------------------------------------------

  return (
    <div className="app">

      {/* HEADER */}

      <header className="header">
        <div>
          <h1>Customer Retention Analytics</h1>
          <p>Banking Customer Risk & Retention Dashboard</p>
        </div>

        <button
          className="logout-btn"
          onClick={() => {
            setLoggedIn(false);
            setResult(null);
          }}
        >
          Logout
        </button>
      </header>

      {/* NAVIGATION */}

      <nav className="navbar">
        <button className="active">Dashboard</button>
        <button>Customer Insights</button>
        <button>Visualizations</button>
      </nav>

      {/* MAIN */}

      <main className="main">

        {/* CUSTOMER SEARCH */}

        <section className="customer-section">

          <div>
            <h2>Customer Analysis</h2>
            <p>
              Enter a customer ID and run the retention models.
            </p>
          </div>

          <div className="customer-controls">

            <input
              type="text"
              value={customerId}
              onChange={(e) => setCustomerId(e.target.value)}
              placeholder="Customer ID"
            />

            <button
              onClick={runPrediction}
              disabled={loading}
            >
              {loading ? "Analyzing..." : "Analyze Customer"}
            </button>

          </div>

        </section>

        {/* ERROR */}

        {error && (
          <div className="error-box">
            ⚠️ {error}
          </div>
        )}

        {/* SUMMARY CARDS */}

        <section className="cards">

          <div className="card">
            <h3>Customer</h3>
            <strong>{customerId}</strong>
            <span>Selected Customer</span>
          </div>

          <div className="card">
            <h3>Churn Probability</h3>
            <strong>
              {model1 ? `${churnProbability}%` : "--"}
            </strong>
            <span>Model 1 Prediction</span>
          </div>

          <div className="card">
            <h3>Risk Score</h3>
            <strong>
              {model1 ? riskScore : "--"}
            </strong>
            <span>Score out of 100</span>
          </div>

          <div className="card">
            <h3>Risk Level</h3>

            <strong
              className={
                riskLevel === "High"
                  ? "high"
                  : riskLevel === "Medium"
                  ? "medium"
                  : "low"
              }
            >
              {riskLevel}
            </strong>

            <span>Current Risk Category</span>
          </div>

        </section>

        {/* MODEL RESULTS */}

        <section className="dashboard-grid">

          {/* MODEL 1 */}

          <div className="panel">

            <div className="panel-title">
              <h2>Churn Predictions</h2>
              <span>Model 1 — XGBoost</span>
            </div>

            {!model1 ? (
              <div className="empty">
                Run customer analysis to see prediction.
              </div>
            ) : (
              <>
                <div className="prediction">

                  <div>
                    <span>Prediction</span>

                    <h2>
                      {model1.churn_prediction === "Yes"
                        ? "Likely to Churn"
                        : "Likely to Stay"}
                    </h2>
                  </div>

                  <div className="probability">
                    {churnProbability}%
                  </div>

                </div>

                <h3>Top Risk Factors</h3>

                <div className="risk-list">

                  {riskFactors.length === 0 ? (
                    <p>No major risk factors detected.</p>
                  ) : (
                    riskFactors.map((factor, index) => (
                      <div className="risk-item" key={index}>
                        <span>➜</span>

                        <div>
                          <strong>
                            {factor.message}
                          </strong>

                          <small>
                            Contribution:{" "}
                            {Number(
                              factor.contribution
                            ).toFixed(3)}
                          </small>
                        </div>
                      </div>
                    ))
                  )}

                </div>
              </>
            )}

          </div>

          {/* RISK CHART */}

          <div className="panel">

            <div className="panel-title">
              <h2>Risk Visualization</h2>
              <span>Model 1</span>
            </div>

            {model1 ? (
              <div className="chart-container">

                <ResponsiveContainer
                  width="100%"
                  height={280}
                >
                  <PieChart>

                    <Pie
                      data={riskChartData}
                      dataKey="value"
                      nameKey="name"
                      cx="50%"
                      cy="50%"
                      innerRadius={65}
                      outerRadius={100}
                      paddingAngle={3}
                    >
                      {riskChartData.map(
                        (_, index) => (
                          <Cell key={index} />
                        )
                      )}
                    </Pie>

                    <Tooltip />

                    <Legend />

                  </PieChart>
                </ResponsiveContainer>

                <div className="chart-center">
                  <strong>
                    {churnProbability}%
                  </strong>

                  <span>Churn Risk</span>
                </div>

              </div>
            ) : (
              <div className="empty">
                No prediction available.
              </div>
            )}

          </div>

        </section>

        {/* MODEL 2 */}

        <section className="panel recommendations">

          <div className="panel-title">
            <div>
              <h2>
                Reasons for Risk & Recommendations
              </h2>

              <span>
                Model 2 — AI Retention Assistant
              </span>
            </div>
          </div>

          {!model2 ? (
            <div className="empty">
              Run customer analysis to generate
              personalized recommendations.
            </div>
          ) : (
            <>

              <div className="reason-box">
                <h3>Primary Reason</h3>

                <p>
                  {model2.summary_reason}
                </p>
              </div>

              <h3>Recommended Actions</h3>

              <div className="recommendation-list">

                {recommendations.map(
                  (action, index) => (
                    <div
                      className="recommendation"
                      key={index}
                    >
                      <div className="recommendation-number">
                        {index + 1}
                      </div>

                      <div>
                        <h4>
                          {action.action_label}
                        </h4>

                        <p>
                          {action.reason}
                        </p>

                        <span>
                          Priority:{" "}
                          {action.priority}
                        </span>
                      </div>
                    </div>
                  )
                )}

              </div>

            </>
          )}

        </section>

        {/* MODEL PIPELINE */}

        <section className="pipeline">

          <h2>Analytics Pipeline</h2>

          <div className="pipeline-flow">

            <div>
              <strong>Customer Data</strong>
              <span>Profile + History</span>
            </div>

            <b>→</b>

            <div>
              <strong>Model 1</strong>
              <span>XGBoost Churn Prediction</span>
            </div>

            <b>→</b>

            <div>
              <strong>Risk Analysis</strong>
              <span>Factors + Risk Score</span>
            </div>

            <b>→</b>

            <div>
              <strong>Model 2</strong>
              <span>AI Recommendations</span>
            </div>

          </div>

        </section>

      </main>

      {/* FOOTER */}

      <footer>
        Banking Customer Retention Analytics • AI & Data Science
      </footer>

    </div>
  );
}

export default App;