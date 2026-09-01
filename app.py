import os
import sqlite3
from flask import Flask, render_template, jsonify, request

app = Flask(__name__, template_folder='frontend/templates', static_folder='frontend/static')
DB_PATH = os.path.join(os.path.dirname(__file__), 'database', 'sample_customer_retention.db')

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

# Human-friendly labels for Model 1 v2 risk factor names
FACTOR_DISPLAY = {
    'latest_vs_avg_upi_share_of_spend_available_history': 'Shift to 3rd-Party UPI Apps',
    'latest_days_since_last_transaction': 'Prolonged Account Inactivity',
    'latest_transaction_change_30d': 'Declining Transaction Frequency',
    'latest_salary_missing_days': 'Delayed Salary / Pension Credit',
    'latest_upi_share_of_spend': 'High UPI Share of Spend',
    'latest_balance_change_30d': 'Severe Account Balance Drop',
    'latest_external_transfer_change_30d': 'Funds Outflow to External Banks',
    'sum_failed_transactions_30d_3m': 'Persistent Transaction Failures',
    'sum_complaints_30d_3m': 'Frequent Service Complaints',
    'latest_unresolved_complaints': 'Unresolved Escalated Complaints',
    'latest_card_spend_change_30d': 'Declining Card Spending',
    'latest_app_login_change_30d': 'Reduced Digital Engagement',
    'latest_complaints_30d': 'Recent Complaint Activity',
    'latest_failed_transactions_30d': 'Failed Transactions',
    'latest_emi_bounce_30d': 'EMI Payment Bounce',
    'latest_avg_resolution_time_hrs': 'Slow Complaint Resolution',
    'latest_fd_maturing_in_30d': 'FD Maturing Soon',
    'latest_products_dropped_90d': 'Product Cancellations',
    'avg_balance_change_30d_3m': 'Balance Decline (3-Month)',
    'avg_balance_change_30d_6m': 'Balance Decline (6-Month)',
    'avg_transaction_change_30d_3m': 'Transaction Decline (3-Month)',
    'avg_transaction_change_30d_6m': 'Transaction Decline (6-Month)',
    'sum_complaints_30d_6m': 'Complaint History (6-Month)',
    'sum_failed_transactions_30d_6m': 'Failed Transactions (6-Month)',
    'balance_change_30d_trend_6m': 'Balance Downward Trend',
    'transaction_change_30d_trend_6m': 'Transaction Downward Trend',
    'days_since_last_transaction_trend_6m': 'Growing Inactivity Trend',
    'external_transfer_change_30d_trend_6m': 'Rising External Transfers',
    'complaints_30d_trend_6m': 'Rising Complaint Trend',
    'latest_vs_avg_balance_change_30d_available_history': 'Balance Below Historical Average',
}

# ---------------------------------------------------------------------------
# Page routes
# ---------------------------------------------------------------------------

@app.route('/')
def index():
    return render_template('index.html')

# ---------------------------------------------------------------------------
# API: Dashboard Stats
# ---------------------------------------------------------------------------

@app.route('/api/dashboard_stats')
def dashboard_stats():
    conn = get_db()

    # Risk distribution
    rows = conn.execute('''
        SELECT risk_level, COUNT(*) as cnt, AVG(churn_probability) as avg_prob, AVG(risk_score) as avg_score
        FROM model1_predictions GROUP BY risk_level
    ''').fetchall()
    risk_dist = {'High': 0, 'Medium': 0, 'Low': 0}
    avg_probs = {'High': 0, 'Medium': 0, 'Low': 0}
    total = 0
    for r in rows:
        risk_dist[r['risk_level']] = r['cnt']
        avg_probs[r['risk_level']] = round(r['avg_prob'] or 0, 2)
        total += r['cnt']

    # Portfolio value
    total_val = conn.execute('SELECT SUM(customer_yearly_value) as v FROM customers').fetchone()['v'] or 0

    # Revenue by risk
    rev_rows = conn.execute('''
        SELECT m.risk_level, SUM(c.customer_yearly_value) as rev
        FROM customers c JOIN model1_predictions m ON c.customer_id = m.customer_id
        GROUP BY m.risk_level
    ''').fetchall()
    rev_by_risk = {'High': 0, 'Medium': 0, 'Low': 0}
    for r in rev_rows:
        rev_by_risk[r['risk_level']] = r['rev'] or 0
    rev_at_risk = rev_by_risk['High'] + rev_by_risk['Medium']

    # Top risk factors (portfolio-wide)
    factor_rows = conn.execute('''
        SELECT factor_name, factor_message, COUNT(*) as frequency,
               AVG(contribution) as avg_contribution, AVG(factor_value) as avg_value
        FROM model1_risk_factors GROUP BY factor_name
        ORDER BY frequency DESC LIMIT 8
    ''').fetchall()
    top_factors = []
    for r in factor_rows:
        fn = r['factor_name']
        fallback = fn.replace('latest_', '').replace('_30d', '').replace('_', ' ').title()
        top_factors.append({
            'factor_name': fn,
            'display_label': FACTOR_DISPLAY.get(fn, fallback),
            'factor_message': r['factor_message'],
            'frequency': r['frequency'],
            'avg_contribution': round(r['avg_contribution'] or 0, 3),
            'avg_value': round(r['avg_value'] or 0, 2),
        })

    # Primary reasons
    reason_rows = conn.execute('''
        SELECT primary_reason, COUNT(*) as cnt FROM model2_predictions
        WHERE primary_reason IS NOT NULL GROUP BY primary_reason ORDER BY cnt DESC
    ''').fetchall()
    primary_reasons = {r['primary_reason']: r['cnt'] for r in reason_rows}

    # Recommended actions
    action_rows = conn.execute('''
        SELECT recommended_action, urgency, COUNT(*) as cnt FROM model2_predictions
        WHERE recommended_action IS NOT NULL GROUP BY recommended_action, urgency ORDER BY cnt DESC
    ''').fetchall()
    actions_totals = {}
    actions_matrix = {}
    for r in action_rows:
        act, urg, cnt = r['recommended_action'], r['urgency'] or 'MEDIUM', r['cnt']
        if act not in actions_matrix:
            actions_matrix[act] = {'HIGH': 0, 'MEDIUM': 0, 'LOW': 0, 'total': 0}
        actions_matrix[act][urg] = cnt
        actions_matrix[act]['total'] += cnt
        actions_totals[act] = actions_totals.get(act, 0) + cnt

    # Segments
    seg_rows = conn.execute('''
        SELECT c.customer_segment, COUNT(*) as total,
               SUM(CASE WHEN m.risk_level='High' THEN 1 ELSE 0 END) as high_cnt,
               SUM(CASE WHEN m.risk_level='Medium' THEN 1 ELSE 0 END) as med_cnt,
               SUM(CASE WHEN m.risk_level='Low' THEN 1 ELSE 0 END) as low_cnt,
               AVG(m.churn_probability) as avg_cp,
               SUM(c.customer_yearly_value) as total_val,
               SUM(CASE WHEN m.risk_level IN ('High','Medium') THEN c.customer_yearly_value ELSE 0 END) as risk_val
        FROM customers c JOIN model1_predictions m ON c.customer_id = m.customer_id
        GROUP BY c.customer_segment ORDER BY total_val DESC
    ''').fetchall()
    segments = [{
        'segment': r['customer_segment'].title(),
        'total_customers': r['total'],
        'high_risk_count': r['high_cnt'],
        'medium_risk_count': r['med_cnt'],
        'low_risk_count': r['low_cnt'],
        'avg_churn_prob': round(r['avg_cp'] or 0, 2),
        'total_value': round(r['total_val'] or 0, 2),
        'at_risk_value': round(r['risk_val'] or 0, 2),
        'high_risk_pct': round((r['high_cnt'] / r['total']) * 100, 1) if r['total'] else 0,
    } for r in seg_rows]

    # Product depth
    prod_rows = conn.execute('''
        SELECT CASE WHEN products_count=1 THEN '1 Product'
                    WHEN products_count=2 THEN '2 Products'
                    WHEN products_count=3 THEN '3 Products'
                    ELSE '4+ Products' END as bracket,
               COUNT(*) as total,
               SUM(CASE WHEN m.risk_level='High' THEN 1 ELSE 0 END) as high_cnt,
               AVG(m.churn_probability) as avg_cp
        FROM customers c JOIN model1_predictions m ON c.customer_id = m.customer_id
        GROUP BY bracket ORDER BY MIN(products_count)
    ''').fetchall()
    product_depth = [{'bracket': r['bracket'], 'total_customers': r['total'],
                      'high_risk_count': r['high_cnt'], 'avg_churn_prob': round(r['avg_cp'] or 0, 2)} for r in prod_rows]

    # Monthly trends
    trend_rows = conn.execute('''
        SELECT snapshot_date, AVG(balance_change_30d) as avg_bal,
               AVG(transaction_change_30d) as avg_txn,
               AVG(external_transfer_change_30d) as avg_ext,
               AVG(failed_transactions_30d) as avg_fail
        FROM customer_snapshots GROUP BY snapshot_date ORDER BY snapshot_date
    ''').fetchall()
    monthly_trends = [{'month': r['snapshot_date'][:7],
                       'balance_delta': round(r['avg_bal'] or 0, 2),
                       'txn_delta': round(r['avg_txn'] or 0, 2),
                       'outflow_delta': round(r['avg_ext'] or 0, 2),
                       'failed_txns': round(r['avg_fail'] or 0, 2)} for r in trend_rows]

    conn.close()
    return jsonify({
        'total_customers': total,
        'risk_distribution': risk_dist,
        'avg_probs': avg_probs,
        'total_portfolio_value': total_val,
        'revenue_by_risk': rev_by_risk,
        'revenue_at_risk': rev_at_risk,
        'top_risk_factors': top_factors,
        'primary_reasons': primary_reasons,
        'recommended_actions': actions_totals,
        'actions_matrix': actions_matrix,
        'segment_clusters': segments,
        'product_depth_stats': product_depth,
        'monthly_trends': monthly_trends,
    })

# ---------------------------------------------------------------------------
# API: Customer Directory
# ---------------------------------------------------------------------------

@app.route('/api/customers')
def get_customers():
    risk_level = request.args.get('risk_level', '').strip()
    segment = request.args.get('segment', '').strip()
    action = request.args.get('action', '').strip()
    urgency = request.args.get('urgency', '').strip()
    search = request.args.get('search', '').strip()
    cluster_id = request.args.get('cluster_id', '').strip()
    sort_by = request.args.get('sort_by', 'risk_score').strip()
    sort_order = request.args.get('sort_order', 'desc').lower()
    limit = request.args.get('limit', 50, type=int)
    offset = request.args.get('offset', 0, type=int)

    conn = get_db()
    wheres, params = [], []

    if risk_level and risk_level.lower() != 'all':
        wheres.append("m1.risk_level = ?"); params.append(risk_level)
    if segment and segment.lower() != 'all':
        wheres.append("c.customer_segment = ?"); params.append(segment)
    if action and action.lower() != 'all':
        wheres.append("m2.recommended_action = ?"); params.append(action)
    if urgency and urgency.lower() != 'all':
        wheres.append("m2.urgency = ?"); params.append(urgency)
    if cluster_id and cluster_id != '':
        wheres.append("cc.cluster_id = ?"); params.append(int(cluster_id))
    if search:
        wheres.append("(c.customer_id LIKE ? OR c.customer_name LIKE ?)")
        params.extend([f"%{search}%", f"%{search}%"])

    where_sql = ("WHERE " + " AND ".join(wheres)) if wheres else ""

    sort_map = {
        'risk_score': 'm1.risk_score', 'churn_probability': 'm1.churn_probability',
        'customer_yearly_value': 'c.customer_yearly_value', 'tenure_months': 'c.tenure_months',
        'customer_name': 'c.customer_name', 'customer_id': 'c.customer_id',
    }
    col = sort_map.get(sort_by, 'm1.risk_score')
    direction = 'ASC' if sort_order == 'asc' else 'DESC'

    total = conn.execute(f'''
        SELECT COUNT(*) as total FROM customers c
        JOIN model1_predictions m1 ON c.customer_id = m1.customer_id
        LEFT JOIN model2_predictions m2 ON c.customer_id = m2.customer_id
        LEFT JOIN customer_clusters cc ON c.customer_id = cc.customer_id
        {where_sql}
    ''', params).fetchone()['total']

    data = conn.execute(f'''
        SELECT c.customer_id, c.customer_name, c.customer_segment, c.customer_yearly_value,
               c.tenure_months, c.age, c.card_colour, c.products_count, c.has_credit_card, c.has_loan,
               m1.churn_probability, m1.risk_level, m1.risk_score, m1.churn_prediction,
               m2.primary_reason, m2.recommended_action, m2.urgency,
               cc.cluster_id, cc.cluster_label
        FROM customers c
        JOIN model1_predictions m1 ON c.customer_id = m1.customer_id
        LEFT JOIN model2_predictions m2 ON c.customer_id = m2.customer_id
        LEFT JOIN customer_clusters cc ON c.customer_id = cc.customer_id
        {where_sql} ORDER BY {col} {direction} LIMIT ? OFFSET ?
    ''', params + [limit, offset]).fetchall()

    conn.close()
    return jsonify({
        'total_count': total, 'limit': limit, 'offset': offset,
        'customers': [dict(r) for r in data],
    })

# ---------------------------------------------------------------------------
# API: Individual Customer Detail
# ---------------------------------------------------------------------------

@app.route('/api/customer/<customer_id>')
def customer_detail(customer_id):
    conn = get_db()
    profile = conn.execute('''
        SELECT c.*, m1.churn_probability, m1.raw_churn_probability, m1.probability_mode,
               m1.risk_level, m1.risk_score, m1.churn_prediction,
               m2.primary_reason, m2.secondary_reasons, m2.reasoning_summary,
               m2.recommended_action, m2.urgency,
               cc.cluster_id, cc.cluster_label
        FROM customers c
        JOIN model1_predictions m1 ON c.customer_id = m1.customer_id
        LEFT JOIN model2_predictions m2 ON c.customer_id = m2.customer_id
        LEFT JOIN customer_clusters cc ON c.customer_id = cc.customer_id
        WHERE c.customer_id = ?
    ''', (customer_id,)).fetchone()

    if not profile:
        conn.close()
        return jsonify({'error': 'Customer not found'}), 404

    factors = conn.execute('''
        SELECT factor_rank, factor_name, factor_value, factor_message, contribution
        FROM model1_risk_factors WHERE customer_id = ? ORDER BY factor_rank
    ''', (customer_id,)).fetchall()

    evidence = conn.execute('''
        SELECT evidence_rank, evidence_text
        FROM model2_evidence WHERE customer_id = ? ORDER BY evidence_rank
    ''', (customer_id,)).fetchall()

    conn.close()
    return jsonify({
        'profile': dict(profile),
        'risk_factors': [dict(r) for r in factors],
        'evidence': [dict(r) for r in evidence],
    })


@app.route('/api/customer/<customer_id>/history')
def customer_history(customer_id):
    conn = get_db()
    rows = conn.execute('''
        SELECT snapshot_date, days_since_last_transaction, balance_change_30d,
               transaction_change_30d, card_spend_change_30d, app_login_change_30d,
               salary_missing_days, external_transfer_change_30d, upi_share_of_spend,
               complaints_30d, unresolved_complaints, failed_transactions_30d,
               emi_bounce_30d, complaint_text, churn_flag
        FROM customer_snapshots WHERE customer_id = ? ORDER BY snapshot_date
    ''', (customer_id,)).fetchall()
    conn.close()
    return jsonify([dict(r) for r in rows])


@app.route('/api/customer/<customer_id>/retention_analysis')
def customer_retention_analysis(customer_id):
    """Combined retention analysis for individual customer."""
    conn = get_db()

    profile = conn.execute('''
        SELECT c.*, m1.churn_probability, m1.risk_level, m1.risk_score,
               m2.primary_reason, m2.secondary_reasons, m2.reasoning_summary,
               m2.recommended_action, m2.urgency,
               cc.cluster_id, cc.cluster_label
        FROM customers c
        JOIN model1_predictions m1 ON c.customer_id = m1.customer_id
        LEFT JOIN model2_predictions m2 ON c.customer_id = m2.customer_id
        LEFT JOIN customer_clusters cc ON c.customer_id = cc.customer_id
        WHERE c.customer_id = ?
    ''', (customer_id,)).fetchone()

    if not profile:
        conn.close()
        return jsonify({'error': 'Customer not found'}), 404

    factors = conn.execute('''
        SELECT factor_rank, factor_name, factor_value, factor_message, contribution
        FROM model1_risk_factors WHERE customer_id = ? ORDER BY factor_rank
    ''', (customer_id,)).fetchall()

    evidence = conn.execute('''
        SELECT evidence_rank, evidence_text
        FROM model2_evidence WHERE customer_id = ? ORDER BY evidence_rank
    ''', (customer_id,)).fetchall()

    history = conn.execute('''
        SELECT snapshot_date, balance_change_30d, transaction_change_30d,
               app_login_change_30d, complaints_30d, failed_transactions_30d,
               days_since_last_transaction, external_transfer_change_30d
        FROM customer_snapshots WHERE customer_id = ? ORDER BY snapshot_date
    ''', (customer_id,)).fetchall()

    # Get cluster profile if assigned
    cluster_profile = None
    p = dict(profile)
    if p.get('cluster_id') is not None:
        cluster_profile = conn.execute('''
            SELECT * FROM cluster_profiles WHERE cluster_id = ?
        ''', (p['cluster_id'],)).fetchone()
        if cluster_profile:
            cluster_profile = dict(cluster_profile)

    conn.close()
    return jsonify({
        'profile': p,
        'risk_factors': [dict(r) for r in factors],
        'evidence': [dict(r) for r in evidence],
        'history': [dict(r) for r in history],
        'cluster_profile': cluster_profile,
    })

# ---------------------------------------------------------------------------
# API: Cluster Analysis
# ---------------------------------------------------------------------------

@app.route('/api/clusters')
def get_clusters():
    conn = get_db()
    rows = conn.execute('SELECT * FROM cluster_profiles ORDER BY cluster_id').fetchall()
    conn.close()
    return jsonify({'clusters': [dict(r) for r in rows]})


@app.route('/api/cluster/<int:cluster_id>')
def cluster_detail(cluster_id):
    conn = get_db()
    profile = conn.execute('SELECT * FROM cluster_profiles WHERE cluster_id = ?', (cluster_id,)).fetchone()
    if not profile:
        conn.close()
        return jsonify({'error': 'Cluster not found'}), 404

    # Get customers in this cluster with their predictions
    customers = conn.execute('''
        SELECT c.customer_id, c.customer_name, c.customer_segment, c.customer_yearly_value,
               c.tenure_months, m1.churn_probability, m1.risk_level, m1.risk_score,
               m2.primary_reason, m2.recommended_action, m2.urgency
        FROM customer_clusters cc
        JOIN customers c ON cc.customer_id = c.customer_id
        JOIN model1_predictions m1 ON c.customer_id = m1.customer_id
        LEFT JOIN model2_predictions m2 ON c.customer_id = m2.customer_id
        WHERE cc.cluster_id = ?
        ORDER BY m1.risk_score DESC LIMIT 100
    ''', (cluster_id,)).fetchall()

    # Reason distribution within cluster
    reasons = conn.execute('''
        SELECT m2.primary_reason, COUNT(*) as cnt
        FROM customer_clusters cc
        JOIN model2_predictions m2 ON cc.customer_id = m2.customer_id
        WHERE cc.cluster_id = ? AND m2.primary_reason IS NOT NULL
        GROUP BY m2.primary_reason ORDER BY cnt DESC
    ''', (cluster_id,)).fetchall()

    conn.close()
    return jsonify({
        'profile': dict(profile),
        'customers': [dict(r) for r in customers],
        'reason_distribution': {r['primary_reason']: r['cnt'] for r in reasons},
    })


@app.route('/api/cluster/<int:cluster_id>/customers')
def cluster_customers(cluster_id):
    limit = request.args.get('limit', 50, type=int)
    offset = request.args.get('offset', 0, type=int)

    conn = get_db()
    total = conn.execute('''
        SELECT COUNT(*) as cnt FROM customer_clusters WHERE cluster_id = ?
    ''', (cluster_id,)).fetchone()['cnt']

    rows = conn.execute('''
        SELECT c.customer_id, c.customer_name, c.customer_segment, c.customer_yearly_value,
               m1.churn_probability, m1.risk_level, m1.risk_score,
               m2.primary_reason, m2.recommended_action, m2.urgency
        FROM customer_clusters cc
        JOIN customers c ON cc.customer_id = c.customer_id
        JOIN model1_predictions m1 ON c.customer_id = m1.customer_id
        LEFT JOIN model2_predictions m2 ON c.customer_id = m2.customer_id
        WHERE cc.cluster_id = ?
        ORDER BY m1.risk_score DESC LIMIT ? OFFSET ?
    ''', (cluster_id, limit, offset)).fetchall()

    conn.close()
    return jsonify({'total_count': total, 'customers': [dict(r) for r in rows]})

# ---------------------------------------------------------------------------
# API: Feature Importance
# ---------------------------------------------------------------------------

@app.route('/api/feature_importance')
def feature_importance():
    conn = get_db()
    rows = conn.execute('''
        SELECT factor_name, COUNT(*) as frequency,
               AVG(contribution) as avg_contribution,
               AVG(factor_value) as avg_value
        FROM model1_risk_factors
        GROUP BY factor_name
        ORDER BY avg_contribution DESC
        LIMIT 15
    ''').fetchall()
    conn.close()

    features = []
    for r in rows:
        fn = r['factor_name']
        fallback = fn.replace('latest_', '').replace('_30d', '').replace('_', ' ').title()
        features.append({
            'feature_name': fn,
            'display_label': FACTOR_DISPLAY.get(fn, fallback),
            'frequency': r['frequency'],
            'avg_contribution': round(r['avg_contribution'] or 0, 4),
            'avg_value': round(r['avg_value'] or 0, 2),
        })

    return jsonify({'features': features})


# ---------------------------------------------------------------------------
# Run
# ---------------------------------------------------------------------------

if __name__ == '__main__':
    app.run(debug=True, port=5000)
