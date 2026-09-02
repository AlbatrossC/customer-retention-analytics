import os
import sqlite3
from flask import Flask, render_template, jsonify, request

app = Flask(__name__, template_folder='frontend/templates', static_folder='frontend/static')
app.config['JSON_SORT_KEYS'] = False
try:
    app.json.sort_keys = False
except AttributeError:
    pass
DB_PATH = os.path.join(os.path.dirname(__file__), 'database', 'customer_retention.db')

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

# Comprehensive human-friendly labels for all 69 Model 1 v2 engineered features
FACTOR_DISPLAY = {
    'app_login_change_30d_trend_6m': 'Digital Engagement Trajectory (6M Trend)',
    'avg_app_login_change_30d_3m': 'Avg App Login Delta (3-Month)',
    'avg_app_login_change_30d_6m': 'Avg App Login Delta (6-Month)',
    'avg_balance_change_30d_3m': 'Avg Balance Delta (3-Month)',
    'avg_balance_change_30d_6m': 'Avg Balance Delta (6-Month)',
    'avg_card_spend_change_30d_3m': 'Avg Card Spending Delta (3-Month)',
    'avg_card_spend_change_30d_6m': 'Avg Card Spending Delta (6-Month)',
    'avg_external_transfer_change_30d_3m': 'Avg External Outflow Delta (3-Month)',
    'avg_external_transfer_change_30d_6m': 'Avg External Outflow Delta (6-Month)',
    'avg_transaction_change_30d_3m': 'Avg Transaction Delta (3-Month)',
    'avg_transaction_change_30d_6m': 'Avg Transaction Delta (6-Month)',
    'avg_upi_share_of_spend_3m': 'Avg UPI Spend Share (3-Month)',
    'avg_upi_share_of_spend_6m': 'Avg UPI Spend Share (6-Month)',
    'balance_change_30d_trend_6m': 'Account Balance Trajectory (6M Trend)',
    'card_spend_change_30d_trend_6m': 'Card Spend Trajectory (6M Trend)',
    'complaints_30d_trend_6m': 'Service Complaints Trajectory (6M Trend)',
    'count_app_login_drop_3m': 'Consecutive App Login Drops (3M)',
    'count_app_login_drop_6m': 'Consecutive App Login Drops (6M)',
    'count_balance_drop_3m': 'Consecutive Balance Drops (3M)',
    'count_balance_drop_6m': 'Consecutive Balance Drops (6M)',
    'count_card_spend_drop_3m': 'Consecutive Card Spend Drops (3M)',
    'count_card_spend_drop_6m': 'Consecutive Card Spend Drops (6M)',
    'count_emi_bounce_month_6m': 'Months with EMI Bounce (6M)',
    'count_external_transfer_rise_3m': 'Months with Outflow Surge (3M)',
    'count_external_transfer_rise_6m': 'Months with Outflow Surge (6M)',
    'count_failed_transaction_month_3m': 'Months with Failed Txns (3M)',
    'count_failed_transaction_month_6m': 'Months with Failed Txns (6M)',
    'count_transaction_drop_3m': 'Consecutive Transaction Drops (3M)',
    'count_transaction_drop_6m': 'Consecutive Transaction Drops (6M)',
    'days_since_last_transaction_trend_6m': 'Account Inactivity Trajectory (6M Trend)',
    'external_transfer_change_30d_trend_6m': 'External Outflow Surge (6M Trend)',
    'latest_app_login_change_30d': 'Recent App Login Delta (30D)',
    'latest_avg_resolution_time_hrs': 'Slow Complaint Resolution Time',
    'latest_balance_change_30d': 'Severe Account Balance Drop (30D)',
    'latest_card_spend_change_30d': 'Declining Card Spending (30D)',
    'latest_complaints_30d': 'Recent Service Complaints (30D)',
    'latest_days_since_last_transaction': 'Prolonged Account Inactivity (Days)',
    'latest_external_transfer_change_30d': 'Funds Outflow to External Banks (30D)',
    'latest_failed_transactions_30d': 'Recent Failed Transactions (30D)',
    'latest_fd_maturing_in_30d': 'Fixed Deposit Maturing Soon',
    'latest_products_dropped_90d': 'Banking Products Dropped (90D)',
    'latest_salary_missing_days': 'Delayed Salary / Income Inflow',
    'latest_transaction_change_30d': 'Declining Transaction Frequency (30D)',
    'latest_upi_share_of_spend': 'High UPI Share of Spending',
    'latest_vs_avg_app_login_change_30d_available_history': 'App Logins Lower than Historical Avg',
    'latest_vs_avg_balance_change_30d_available_history': 'Balance Drop Worse than Historical Avg',
    'latest_vs_avg_card_spend_change_30d_available_history': 'Card Spend Lower than Historical Avg',
    'latest_vs_avg_external_transfer_change_30d_available_history': 'External Outflows Higher than Avg',
    'latest_vs_avg_transaction_change_30d_available_history': 'Transactions Lower than Historical Avg',
    'latest_vs_avg_upi_share_of_spend_available_history': 'Shift to 3rd-Party UPI Apps',
    'max_avg_resolution_time_hrs_3m': 'Peak Complaint Resolution Time (3M)',
    'max_avg_resolution_time_hrs_6m': 'Peak Complaint Resolution Time (6M)',
    'max_days_since_last_transaction_3m': 'Peak Inactivity Duration (3M)',
    'max_days_since_last_transaction_6m': 'Peak Inactivity Duration (6M)',
    'max_salary_missing_days_3m': 'Longest Salary Delay (3M)',
    'max_salary_missing_days_6m': 'Longest Salary Delay (6M)',
    'sum_complaints_30d_3m': 'Frequent Service Complaints (3M)',
    'sum_complaints_30d_6m': 'Accumulated Service Complaints (6M)',
    'sum_emi_bounce_30d_3m': 'Total EMI Payment Bounces (3M)',
    'sum_emi_bounce_30d_6m': 'Accumulated EMI Bounces (6M)',
    'sum_failed_transactions_30d_3m': 'Persistent Transaction Failures (3M)',
    'sum_failed_transactions_30d_6m': 'Accumulated Failed Transactions (6M)',
    'sum_fd_maturing_in_30d_3m': 'Maturing Fixed Deposits (3M Window)',
    'sum_fd_maturing_in_30d_6m': 'Maturing Fixed Deposits (6M Window)',
    'sum_products_dropped_90d_3m': 'Total Products Cancelled (3M)',
    'sum_products_dropped_90d_6m': 'Total Products Cancelled (6M)',
    'sum_unresolved_complaints_3m': 'Unresolved Escalated Complaints (3M)',
    'sum_unresolved_complaints_6m': 'Unresolved Escalated Complaints (6M)',
    'transaction_change_30d_trend_6m': 'Transaction Activity Trajectory (6M Trend)',
}

def format_factor_label(fn: str) -> str:
    if not fn:
        return ""
    if fn in FACTOR_DISPLAY:
        return FACTOR_DISPLAY[fn]
    # Smart parsing fallback
    clean_name = fn.replace('latest_vs_avg_', 'Recent vs Avg ')
    clean_name = clean_name.replace('latest_', 'Recent ')
    clean_name = clean_name.replace('avg_', 'Avg ')
    clean_name = clean_name.replace('sum_', 'Total ')
    clean_name = clean_name.replace('count_', 'Count ')
    clean_name = clean_name.replace('_30d', '')
    clean_name = clean_name.replace('_trend_6m', ' (6M Trend)')
    clean_name = clean_name.replace('_6m', ' (6M)')
    clean_name = clean_name.replace('_3m', ' (3M)')
    clean_name = clean_name.replace('_available_history', ' (vs History)')
    clean_name = clean_name.replace('_', ' ').strip()
    return clean_name.title()

# ---------------------------------------------------------------------------
# Page routes
# ---------------------------------------------------------------------------

@app.route('/')
@app.route('/customer-directory')
@app.route('/individual-analysis')
@app.route('/cluster-analysis')
@app.route('/visualizations')
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

    # Top risk factors (portfolio-wide across all customers)
    factor_rows = conn.execute('''
        SELECT factor_name, factor_message, COUNT(*) as frequency,
               AVG(contribution) as avg_contribution, AVG(factor_value) as avg_value
        FROM model1_risk_factors GROUP BY factor_name
        ORDER BY frequency DESC LIMIT 8
    ''').fetchall()
    top_factors = []
    for r in factor_rows:
        fn = r['factor_name']
        top_factors.append({
            'factor_name': fn,
            'display_label': format_factor_label(fn),
            'factor_message': r['factor_message'],
            'frequency': r['frequency'],
            'avg_contribution': round(r['avg_contribution'] or 0, 3),
            'avg_value': round(r['avg_value'] or 0, 2),
        })

    # Primary reasons (Model 2 LLM diagnoses for at-risk customers, ordered descending)
    reason_rows = conn.execute('''
        SELECT primary_reason, COUNT(*) as cnt FROM model2_predictions
        WHERE primary_reason IS NOT NULL GROUP BY primary_reason ORDER BY cnt DESC
    ''').fetchall()
    primary_reasons = {r['primary_reason']: r['cnt'] for r in reason_rows}

    # Recommended actions matrix (Model 2 LLM recommendations by urgency, ordered descending by total)
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
    # Sort actions_totals strictly descending by total count
    actions_totals = dict(sorted(actions_totals.items(), key=lambda item: item[1], reverse=True))

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

    # Monthly trends from real snapshots
    trend_rows = conn.execute('''
        SELECT snapshot_date, AVG(balance_change_30d) as avg_bal,
               AVG(transaction_change_30d) as avg_txn,
               AVG(external_transfer_change_30d) as avg_ext,
               AVG(failed_transactions_30d) as avg_fail
        FROM customer_snapshots GROUP BY snapshot_date ORDER BY snapshot_date
    ''').fetchall()
    monthly_trends = [{
        'month': r['snapshot_date'][:7],
        'balance_delta': round(r['avg_bal'] or 0, 2),
        'txn_delta': round(r['avg_txn'] or 0, 2),
        'outflow_delta': round(r['avg_ext'] or 0, 2),
        'failed_txns': round(r['avg_fail'] or 0, 2)
    } for r in trend_rows]

    # Model 2 AI coverage by risk level
    m2_coverage_rows = conn.execute('''
        SELECT m1.risk_level,
               COUNT(*) as total,
               SUM(CASE WHEN m2.customer_id IS NOT NULL THEN 1 ELSE 0 END) as analyzed
        FROM model1_predictions m1
        LEFT JOIN model2_predictions m2 ON m1.customer_id = m2.customer_id
        GROUP BY m1.risk_level
    ''').fetchall()
    m2_coverage = {}
    total_analyzed = 0
    for r in m2_coverage_rows:
        m2_coverage[r['risk_level']] = {
            'total': r['total'],
            'analyzed': r['analyzed'],
        }
        total_analyzed += r['analyzed']

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
        'monthly_trends': monthly_trends,
        'model2_coverage': m2_coverage,
        'total_analyzed': total_analyzed,
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
        wheres.append("m1.risk_level = ?")
        params.append(risk_level)
    if segment and segment.lower() != 'all':
        wheres.append("c.customer_segment = ?")
        params.append(segment)
    if action and action.lower() != 'all':
        if action == 'MONITOR':
            wheres.append("(m2.recommended_action = ? OR m2.recommended_action IS NULL)")
            params.append(action)
        else:
            wheres.append("m2.recommended_action = ?")
            params.append(action)
    if urgency and urgency.lower() != 'all':
        if urgency == 'LOW':
            wheres.append("(m2.urgency = ? OR m2.urgency IS NULL)")
            params.append(urgency)
        else:
            wheres.append("m2.urgency = ?")
            params.append(urgency)
    if cluster_id and cluster_id != '':
        wheres.append("cc.cluster_id = ?")
        params.append(int(cluster_id))
    if search:
        wheres.append("(c.customer_id LIKE ? OR c.customer_name LIKE ?)")
        params.extend([f"%{search}%", f"%{search}%"])

    where_sql = ("WHERE " + " AND ".join(wheres)) if wheres else ""

    sort_map = {
        'risk_score': 'm1.risk_score',
        'churn_probability': 'm1.churn_probability',
        'customer_yearly_value': 'c.customer_yearly_value',
        'tenure_months': 'c.tenure_months',
        'customer_name': 'c.customer_name',
        'customer_id': 'c.customer_id',
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
        'total_count': total,
        'limit': limit,
        'offset': offset,
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

    complaints = conn.execute('''
        SELECT snapshot_date, complaints_30d, unresolved_complaints, complaint_text
        FROM customer_snapshots
        WHERE customer_id = ? AND complaint_text IS NOT NULL AND TRIM(complaint_text) != ''
        ORDER BY snapshot_date DESC
    ''', (customer_id,)).fetchall()

    conn.close()

    p_dict = dict(profile)
    # Default fallback for healthy accounts without LLM Model 2 records
    if p_dict.get('primary_reason') is None:
        p_dict['primary_reason'] = None
        p_dict['recommended_action'] = p_dict.get('recommended_action') or 'MONITOR'
        p_dict['urgency'] = p_dict.get('urgency') or 'LOW'
        p_dict['reasoning_summary'] = p_dict.get('reasoning_summary') or 'Customer displays stable engagement metrics with low churn probability.'

    factors_list = []
    for r in factors:
        f = dict(r)
        f['display_label'] = format_factor_label(f['factor_name'])
        factors_list.append(f)

    return jsonify({
        'profile': p_dict,
        'risk_factors': factors_list,
        'evidence': [dict(r) for r in evidence],
        'complaints': [dict(r) for r in complaints],
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

    p = dict(profile)
    # Default fallback for healthy accounts without LLM Model 2 records
    if p.get('primary_reason') is None:
        p['primary_reason'] = None
        p['recommended_action'] = p.get('recommended_action') or 'MONITOR'
        p['urgency'] = p.get('urgency') or 'LOW'
        p['reasoning_summary'] = p.get('reasoning_summary') or 'Customer displays stable engagement metrics with low churn probability.'

    # Get cluster profile if assigned
    cluster_profile = None
    if p.get('cluster_id') is not None:
        cluster_profile = conn.execute('''
            SELECT * FROM cluster_profiles WHERE cluster_id = ?
        ''', (p['cluster_id'],)).fetchone()
        if cluster_profile:
            cluster_profile = dict(cluster_profile)

    complaints = conn.execute('''
        SELECT snapshot_date, complaints_30d, unresolved_complaints, complaint_text
        FROM customer_snapshots
        WHERE customer_id = ? AND complaint_text IS NOT NULL AND TRIM(complaint_text) != ''
        ORDER BY snapshot_date DESC
    ''', (customer_id,)).fetchall()

    conn.close()

    factors_list = []
    for r in factors:
        f = dict(r)
        f['display_label'] = format_factor_label(f['factor_name'])
        factors_list.append(f)

    return jsonify({
        'profile': p,
        'risk_factors': factors_list,
        'evidence': [dict(r) for r in evidence],
        'history': [dict(r) for r in history],
        'complaints': [dict(r) for r in complaints],
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
        features.append({
            'feature_name': fn,
            'display_label': format_factor_label(fn),
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
