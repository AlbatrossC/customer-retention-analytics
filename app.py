import os
import sqlite3
from flask import Flask, render_template, jsonify, request

app = Flask(__name__, template_folder='frontend/templates', static_folder='frontend/static')
DB_PATH = os.path.join(os.path.dirname(__file__), 'database', 'customer_retention.db')

def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/dashboard_stats')
def get_dashboard_stats():
    conn = get_db_connection()
    
    # 1. Total customer counts and averages by risk level
    risk_counts_raw = conn.execute('''
        SELECT risk_level, COUNT(*) as count, AVG(churn_probability) as avg_prob, AVG(risk_score) as avg_score
        FROM model1_predictions 
        GROUP BY risk_level
    ''').fetchall()
    
    risk_distribution = {'High': 0, 'Medium': 0, 'Low': 0}
    avg_probs = {'High': 0, 'Medium': 0, 'Low': 0}
    total_customers = 0
    
    for row in risk_counts_raw:
        r_level = row['risk_level']
        cnt = row['count']
        risk_distribution[r_level] = cnt
        avg_probs[r_level] = round(row['avg_prob'] or 0, 2)
        total_customers += cnt

    # 2. Total portfolio yearly value
    total_portfolio_value = conn.execute('''
        SELECT SUM(customer_yearly_value) as total_val FROM customers
    ''').fetchone()['total_val'] or 0

    # 3. Revenue by risk tier breakdown
    revenue_by_risk_raw = conn.execute('''
        SELECT m1.risk_level, SUM(c.customer_yearly_value) as revenue
        FROM customers c
        JOIN model1_predictions m1 ON c.customer_id = m1.customer_id
        GROUP BY m1.risk_level
    ''').fetchall()
    
    revenue_by_risk = {'High': 0, 'Medium': 0, 'Low': 0}
    for row in revenue_by_risk_raw:
        revenue_by_risk[row['risk_level']] = row['revenue'] or 0

    revenue_at_risk = revenue_by_risk['High'] + revenue_by_risk['Medium']

    # 4. Portfolio-wide Top Risk Factors (Clean executive labeling)
    top_risk_factors_raw = conn.execute('''
        SELECT factor_name, factor_message, COUNT(*) as frequency, 
               AVG(contribution) as avg_contribution, AVG(factor_value) as avg_value
        FROM model1_risk_factors
        GROUP BY factor_name
        ORDER BY frequency DESC
        LIMIT 8
    ''').fetchall()
    
    # Human-friendly executive descriptions for bank managers
    factor_display_names = {
        'latest_vs_avg_upi_share_of_spend_available_history': 'Shift to 3rd-Party UPI Apps',
        'latest_days_since_last_transaction': 'Prolonged Account Inactivity',
        'latest_transaction_change_30d': 'Declining Transaction Frequency',
        'latest_salary_missing_days': 'Delayed Salary / Pension Credit',
        'latest_upi_share_of_spend': 'High UPI Share of Spend',
        'latest_balance_change_30d': 'Severe Account Balance Drop',
        'latest_external_transfer_change_30d': 'Funds Outflow to External Banks',
        'sum_failed_transactions_30d_3m': 'Persistent Transaction Failures',
        'sum_complaints_30d_3m': 'Frequent Service Complaints',
        'latest_unresolved_complaints': 'Unresolved Escalated Complaints'
    }

    top_risk_factors = []
    for row in top_risk_factors_raw:
        f_name = row['factor_name']
        fallback_label = f_name.replace('latest_', '').replace('_30d', '').replace('_', ' ').title()
        display_label = factor_display_names.get(f_name, fallback_label)
        top_risk_factors.append({
            'factor_name': f_name,
            'display_label': display_label,
            'factor_message': row['factor_message'],
            'frequency': row['frequency'],
            'avg_contribution': round(row['avg_contribution'] or 0, 3),
            'avg_value': round(row['avg_value'] or 0, 2)
        })

    # 5. Primary reasons breakdown
    primary_reasons_raw = conn.execute('''
        SELECT primary_reason, COUNT(*) as count
        FROM model2_predictions
        WHERE primary_reason IS NOT NULL
        GROUP BY primary_reason
        ORDER BY count DESC
    ''').fetchall()
    primary_reasons = {row['primary_reason']: row['count'] for row in primary_reasons_raw}

    # 6. Recommended actions breakdown with urgency
    recommended_actions_raw = conn.execute('''
        SELECT recommended_action, urgency, COUNT(*) as count
        FROM model2_predictions
        WHERE recommended_action IS NOT NULL
        GROUP BY recommended_action, urgency
        ORDER BY count DESC
    ''').fetchall()
    
    actions_matrix = {}
    actions_totals = {}
    for row in recommended_actions_raw:
        act = row['recommended_action']
        urg = row['urgency'] or 'MEDIUM'
        cnt = row['count']
        if act not in actions_matrix:
            actions_matrix[act] = {'HIGH': 0, 'MEDIUM': 0, 'LOW': 0, 'total': 0}
        actions_matrix[act][urg] = cnt
        actions_matrix[act]['total'] += cnt
        actions_totals[act] = actions_totals.get(act, 0) + cnt

    # 7. Customer Segment Vulnerability & Revenue Exposure
    segments_raw = conn.execute('''
        SELECT c.customer_segment, 
               COUNT(*) as total_customers,
               SUM(CASE WHEN m1.risk_level = 'High' THEN 1 ELSE 0 END) as high_risk_count,
               SUM(CASE WHEN m1.risk_level = 'Medium' THEN 1 ELSE 0 END) as medium_risk_count,
               SUM(CASE WHEN m1.risk_level = 'Low' THEN 1 ELSE 0 END) as low_risk_count,
               AVG(m1.churn_probability) as avg_churn_prob,
               SUM(c.customer_yearly_value) as total_value,
               SUM(CASE WHEN m1.risk_level IN ('High', 'Medium') THEN c.customer_yearly_value ELSE 0 END) as at_risk_value
        FROM customers c
        JOIN model1_predictions m1 ON c.customer_id = m1.customer_id
        GROUP BY c.customer_segment
        ORDER BY total_value DESC
    ''').fetchall()
    
    segment_clusters = []
    for row in segments_raw:
        segment_clusters.append({
            'segment': row['customer_segment'].title(),
            'total_customers': row['total_customers'],
            'high_risk_count': row['high_risk_count'],
            'medium_risk_count': row['medium_risk_count'],
            'low_risk_count': row['low_risk_count'],
            'avg_churn_prob': round(row['avg_churn_prob'] or 0, 2),
            'total_value': round(row['total_value'] or 0, 2),
            'at_risk_value': round(row['at_risk_value'] or 0, 2),
            'high_risk_pct': round((row['high_risk_count'] / row['total_customers']) * 100, 1) if row['total_customers'] else 0
        })

    # 8. Product Depth vs. Churn Rate (Cross-sell & Account Stickiness)
    products_depth_raw = conn.execute('''
        SELECT 
            CASE 
                WHEN products_count = 1 THEN '1 Product'
                WHEN products_count = 2 THEN '2 Products'
                WHEN products_count = 3 THEN '3 Products'
                ELSE '4+ Products'
            END as product_bracket,
            COUNT(*) as total_customers,
            SUM(CASE WHEN m1.risk_level = 'High' THEN 1 ELSE 0 END) as high_risk_count,
            AVG(m1.churn_probability) as avg_churn_prob
        FROM customers c
        JOIN model1_predictions m1 ON c.customer_id = m1.customer_id
        GROUP BY product_bracket
        ORDER BY MIN(products_count) ASC
    ''').fetchall()
    
    product_depth_stats = []
    for row in products_depth_raw:
        product_depth_stats.append({
            'bracket': row['product_bracket'],
            'total_customers': row['total_customers'],
            'high_risk_count': row['high_risk_count'],
            'avg_churn_prob': round(row['avg_churn_prob'] or 0, 2)
        })

    # 9. Monthly Portfolio Inflow / Outflow Behavioral Trends (6 Months)
    monthly_trends_raw = conn.execute('''
        SELECT snapshot_date, 
               AVG(balance_change_30d) as avg_balance_delta,
               AVG(transaction_change_30d) as avg_txn_delta,
               AVG(external_transfer_change_30d) as avg_outflow_delta,
               AVG(failed_transactions_30d) as avg_failed_txns
        FROM customer_snapshots
        GROUP BY snapshot_date
        ORDER BY snapshot_date ASC
    ''').fetchall()
    
    monthly_trends = []
    for row in monthly_trends_raw:
        monthly_trends.append({
            'month': row['snapshot_date'][:7],
            'balance_delta': round(row['avg_balance_delta'] or 0, 2),
            'txn_delta': round(row['avg_txn_delta'] or 0, 2),
            'outflow_delta': round(row['avg_outflow_delta'] or 0, 2),
            'failed_txns': round(row['avg_failed_txns'] or 0, 2)
        })

    conn.close()

    return jsonify({
        'total_customers': total_customers,
        'risk_distribution': risk_distribution,
        'avg_probs': avg_probs,
        'total_portfolio_value': total_portfolio_value,
        'revenue_by_risk': revenue_by_risk,
        'revenue_at_risk': revenue_at_risk,
        'top_risk_factors': top_risk_factors,
        'primary_reasons': primary_reasons,
        'recommended_actions': actions_totals,
        'actions_matrix': actions_matrix,
        'segment_clusters': segment_clusters,
        'product_depth_stats': product_depth_stats,
        'monthly_trends': monthly_trends
    })

@app.route('/api/customers')
def get_customers():
    risk_level = request.args.get('risk_level', '').strip()
    segment = request.args.get('segment', '').strip()
    action = request.args.get('action', '').strip()
    urgency = request.args.get('urgency', '').strip()
    search = request.args.get('search', '').strip()
    sort_by = request.args.get('sort_by', 'risk_score').strip()
    sort_order = request.args.get('sort_order', 'desc').lower()
    
    limit = request.args.get('limit', 50, type=int)
    offset = request.args.get('offset', 0, type=int)
    
    conn = get_db_connection()
    
    where_clauses = []
    params = []
    
    if risk_level and risk_level.lower() != 'all':
        where_clauses.append("m1.risk_level = ?")
        params.append(risk_level)
        
    if segment and segment.lower() != 'all':
        where_clauses.append("c.customer_segment = ?")
        params.append(segment)
        
    if action and action.lower() != 'all':
        where_clauses.append("m2.recommended_action = ?")
        params.append(action)
        
    if urgency and urgency.lower() != 'all':
        where_clauses.append("m2.urgency = ?")
        params.append(urgency)
        
    if search:
        where_clauses.append("(c.customer_id LIKE ? OR c.customer_name LIKE ?)")
        params.append(f"%{search}%")
        params.append(f"%{search}%")
        
    where_sql = ("WHERE " + " AND ".join(where_clauses)) if where_clauses else ""
    
    sort_mapping = {
        'risk_score': 'm1.risk_score',
        'churn_probability': 'm1.churn_probability',
        'customer_yearly_value': 'c.customer_yearly_value',
        'tenure_months': 'c.tenure_months',
        'customer_name': 'c.customer_name',
        'customer_id': 'c.customer_id'
    }
    order_col = sort_mapping.get(sort_by, 'm1.risk_score')
    direction = 'ASC' if sort_order == 'asc' else 'DESC'
    
    count_query = f'''
        SELECT COUNT(*) as total
        FROM customers c
        JOIN model1_predictions m1 ON c.customer_id = m1.customer_id
        LEFT JOIN model2_predictions m2 ON c.customer_id = m2.customer_id
        {where_sql}
    '''
    total_count = conn.execute(count_query, params).fetchone()['total']
    
    data_query = f'''
        SELECT c.customer_id, c.customer_name, c.customer_segment, c.customer_yearly_value,
               c.tenure_months, c.age, c.card_colour, c.products_count, c.has_credit_card, c.has_loan,
               m1.churn_probability, m1.risk_level, m1.risk_score, m1.churn_prediction,
               m2.primary_reason, m2.recommended_action, m2.urgency
        FROM customers c
        JOIN model1_predictions m1 ON c.customer_id = m1.customer_id
        LEFT JOIN model2_predictions m2 ON c.customer_id = m2.customer_id
        {where_sql}
        ORDER BY {order_col} {direction}
        LIMIT ? OFFSET ?
    '''
    
    query_params = list(params) + [limit, offset]
    customers = conn.execute(data_query, query_params).fetchall()
    conn.close()
    
    return jsonify({
        'total_count': total_count,
        'limit': limit,
        'offset': offset,
        'customers': [dict(row) for row in customers]
    })

@app.route('/api/customer/<customer_id>')
def get_customer_detail(customer_id):
    conn = get_db_connection()
    
    # Customer profile + Predictions
    profile_query = '''
        SELECT c.*, m1.churn_probability, m1.raw_churn_probability, m1.probability_mode,
               m1.risk_level, m1.risk_score, m1.churn_prediction,
               m2.primary_reason, m2.secondary_reasons, m2.reasoning_summary, 
               m2.recommended_action, m2.urgency
        FROM customers c
        JOIN model1_predictions m1 ON c.customer_id = m1.customer_id
        LEFT JOIN model2_predictions m2 ON c.customer_id = m2.customer_id
        WHERE c.customer_id = ?
    '''
    profile = conn.execute(profile_query, (customer_id,)).fetchone()
    
    if not profile:
        conn.close()
        return jsonify({'error': 'Customer not found'}), 404
        
    # Top 5 Risk Factors
    risk_factors = conn.execute('''
        SELECT factor_rank, factor_name, factor_value, factor_message, contribution
        FROM model1_risk_factors
        WHERE customer_id = ?
        ORDER BY factor_rank ASC
    ''', (customer_id,)).fetchall()
    
    # Model 2 Evidence (if available)
    evidence_rows = conn.execute('''
        SELECT evidence_rank, evidence_text
        FROM model2_evidence
        WHERE customer_id = ?
        ORDER BY evidence_rank ASC
    ''', (customer_id,)).fetchall()
    
    conn.close()
    
    return jsonify({
        'profile': dict(profile),
        'risk_factors': [dict(row) for row in risk_factors],
        'evidence': [dict(row) for row in evidence_rows]
    })

@app.route('/api/customer/<customer_id>/history')
def get_customer_history(customer_id):
    conn = get_db_connection()
    history = conn.execute('''
        SELECT snapshot_date, days_since_last_transaction, balance_change_30d, transaction_change_30d, 
               card_spend_change_30d, app_login_change_30d, salary_missing_days, external_transfer_change_30d,
               upi_share_of_spend, complaints_30d, unresolved_complaints, failed_transactions_30d,
               emi_bounce_30d, complaint_text, churn_flag
        FROM customer_snapshots
        WHERE customer_id = ?
        ORDER BY snapshot_date ASC
    ''', (customer_id,)).fetchall()
    conn.close()
    
    return jsonify([dict(row) for row in history])

if __name__ == '__main__':
    app.run(debug=True, port=5000)
