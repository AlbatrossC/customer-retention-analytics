// FinRetain Enterprise — Customer Retention Intelligence Console
// Multi-tab dashboard with Chart.js visualizations

// ---------------------------------------------------------------------------
// Chart instances
// ---------------------------------------------------------------------------
let charts = {};

// ---------------------------------------------------------------------------
// Application State
// ---------------------------------------------------------------------------
const state = {
    riskFilter: 'all',
    segment: 'all',
    action: 'all',
    urgency: 'all',
    sortKey: 'risk_score-desc',
    search: '',
    page: 1,
    pageSize: 25,
    totalRecords: 0,
    dashData: null,
    clusterData: null,
};

const TAB_TITLES = {
    dashboard: 'Portfolio Dashboard',
    customers: 'Customer Directory',
    analysis: 'Individual Retention Analysis',
    clusters: 'Cluster Analysis',
    visualizations: 'Data Visualizations',
};

// ---------------------------------------------------------------------------
// Init
// ---------------------------------------------------------------------------
document.addEventListener('DOMContentLoaded', () => {
    setupTabs();
    setupFilters();
    setupModal();
    setupAnalysisSearch();
    loadDashboard();
    loadCustomers();
});

// ---------------------------------------------------------------------------
// Tab Navigation
// ---------------------------------------------------------------------------
function setupTabs() {
    document.querySelectorAll('.nav-item').forEach(btn => {
        btn.addEventListener('click', () => {
            const tab = btn.dataset.tab;
            document.querySelectorAll('.nav-item').forEach(b => b.classList.remove('active'));
            btn.classList.add('active');
            document.querySelectorAll('.tab-panel').forEach(p => p.classList.remove('active'));
            const panel = document.getElementById(`tab-${tab}`);
            if (panel) panel.classList.add('active');
            document.getElementById('pageTitle').textContent = TAB_TITLES[tab] || '';

            // Lazy load tab data
            if (tab === 'clusters' && !state.clusterData) loadClusters();
            if (tab === 'visualizations') loadVisualizations();
        });
    });

    // Sidebar toggle for mobile
    const toggle = document.getElementById('sidebarToggle');
    if (toggle) {
        toggle.addEventListener('click', () => {
            document.getElementById('sidebar').classList.toggle('open');
        });
    }

    // Refresh
    const refreshBtn = document.getElementById('refreshBtn');
    if (refreshBtn) {
        refreshBtn.addEventListener('click', () => {
            const icon = refreshBtn.querySelector('i');
            if (icon) icon.classList.add('fa-spin');
            loadDashboard();
            loadCustomers();
            state.clusterData = null;
            setTimeout(() => { if (icon) icon.classList.remove('fa-spin'); }, 600);
        });
    }

    // Export
    const exportBtn = document.getElementById('exportCsvBtn');
    if (exportBtn) exportBtn.addEventListener('click', exportCSV);
}

// ---------------------------------------------------------------------------
// Filter Controls
// ---------------------------------------------------------------------------
function setupFilters() {
    // Risk tabs
    document.querySelectorAll('#riskTabs .ftab').forEach(tab => {
        tab.addEventListener('click', () => {
            document.querySelectorAll('#riskTabs .ftab').forEach(t => t.classList.remove('active'));
            tab.classList.add('active');
            state.riskFilter = tab.dataset.risk;
            state.page = 1;
            loadCustomers();
        });
    });

    // Dropdowns
    ['fSegment', 'fAction', 'fUrgency', 'fSort'].forEach(id => {
        const el = document.getElementById(id);
        if (!el) return;
        el.addEventListener('change', () => {
            if (id === 'fSegment') state.segment = el.value;
            if (id === 'fAction') state.action = el.value;
            if (id === 'fUrgency') state.urgency = el.value;
            if (id === 'fSort') state.sortKey = el.value;
            state.page = 1;
            loadCustomers();
        });
    });

    // Search
    const searchInput = document.getElementById('searchInput');
    const clearBtn = document.getElementById('clearSearch');
    let debounce = null;
    if (searchInput) {
        searchInput.addEventListener('input', () => {
            const val = searchInput.value.trim();
            if (clearBtn) clearBtn.style.display = val ? 'block' : 'none';
            clearTimeout(debounce);
            debounce = setTimeout(() => { state.search = val; state.page = 1; loadCustomers(); }, 300);
        });
    }
    if (clearBtn) {
        clearBtn.addEventListener('click', () => {
            searchInput.value = '';
            clearBtn.style.display = 'none';
            state.search = '';
            state.page = 1;
            loadCustomers();
        });
    }

    // Pagination
    document.getElementById('prevBtn')?.addEventListener('click', () => {
        if (state.page > 1) { state.page--; loadCustomers(); }
    });
    document.getElementById('nextBtn')?.addEventListener('click', () => {
        if (state.page < Math.ceil(state.totalRecords / state.pageSize)) { state.page++; loadCustomers(); }
    });
}

// Global filter helpers
window.setRiskFilter = function(risk) {
    state.riskFilter = risk;
    state.page = 1;
    // Switch to customers tab
    document.querySelectorAll('.nav-item').forEach(b => b.classList.remove('active'));
    document.getElementById('nav-customers')?.classList.add('active');
    document.querySelectorAll('.tab-panel').forEach(p => p.classList.remove('active'));
    document.getElementById('tab-customers')?.classList.add('active');
    document.getElementById('pageTitle').textContent = TAB_TITLES.customers;
    // Update risk tabs
    document.querySelectorAll('#riskTabs .ftab').forEach(t => {
        t.classList.toggle('active', t.dataset.risk.toLowerCase() === risk.toLowerCase());
    });
    loadCustomers();
};

window.filterBySegment = function(seg) {
    state.segment = seg.toLowerCase();
    state.page = 1;
    const sel = document.getElementById('fSegment');
    if (sel) sel.value = seg.toLowerCase();
    // Switch to customers tab
    document.querySelectorAll('.nav-item').forEach(b => b.classList.remove('active'));
    document.getElementById('nav-customers')?.classList.add('active');
    document.querySelectorAll('.tab-panel').forEach(p => p.classList.remove('active'));
    document.getElementById('tab-customers')?.classList.add('active');
    document.getElementById('pageTitle').textContent = TAB_TITLES.customers;
    loadCustomers();
};

// ---------------------------------------------------------------------------
// Dashboard
// ---------------------------------------------------------------------------
async function loadDashboard() {
    try {
        const res = await fetch('/api/dashboard_stats');
        const data = await res.json();
        state.dashData = data;
        renderKPIs(data);
        renderRiskChart(data);
        renderTopFactors(data);
        renderActionsChart(data);
        renderReasonsChart(data);
        renderProductDepthChart(data);
        renderSegments(data);
        renderMonthlyTrends(data);
    } catch (err) { console.error('Dashboard load error:', err); }
}

function renderKPIs(d) {
    const total = d.total_customers || 10000;
    const high = d.risk_distribution.High || 0;
    const med = d.risk_distribution.Medium || 0;
    const low = d.risk_distribution.Low || 0;

    setText('kpi-total', total.toLocaleString());
    setText('kpi-high', high.toLocaleString());
    setText('kpi-med', med.toLocaleString());
    setText('kpi-low', low.toLocaleString());
    setText('kpi-high-pct', pct(high, total));
    setText('kpi-med-pct', pct(med, total));
    setText('kpi-low-pct', pct(low, total));

    setText('tc-all', total.toLocaleString());
    setText('tc-high', high.toLocaleString());
    setText('tc-med', med.toLocaleString());
    setText('tc-low', low.toLocaleString());

    const revRisk = d.revenue_at_risk || 0;
    const totalVal = d.total_portfolio_value || 0;
    const ratio = totalVal > 0 ? ((revRisk / totalVal) * 100).toFixed(1) : '0.0';

    setText('kpi-rev-risk', `₹${(revRisk / 1e6).toFixed(2)}M`);
    setText('kpi-portfolio', `₹${(totalVal / 1e6).toFixed(2)}M`);
    setText('kpi-risk-ratio', `${ratio}%`);
    const bar = document.getElementById('kpi-progress-bar');
    if (bar) bar.style.width = `${Math.min(100, parseFloat(ratio))}%`;
}

function renderRiskChart(d) {
    const ctx = getCtx('riskDistChart');
    if (!ctx) return;
    destroyChart('riskDist');
    const high = d.risk_distribution.High || 0;
    const med = d.risk_distribution.Medium || 0;
    const low = d.risk_distribution.Low || 0;
    const total = high + med + low;

    charts.riskDist = new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: ['High Risk', 'Watchlist', 'Healthy'],
            datasets: [{ data: [high, med, low], backgroundColor: ['#ef4444', '#f59e0b', '#10b981'], borderWidth: 2, borderColor: '#fff' }]
        },
        options: { responsive: true, maintainAspectRatio: false, cutout: '72%', plugins: { legend: { display: false } } }
    });

    const legend = document.getElementById('riskLegend');
    if (legend) {
        legend.innerHTML = [
            legendRow('High Risk', high, total, 'dot-high', 'High'),
            legendRow('Watchlist', med, total, 'dot-med', 'Medium'),
            legendRow('Healthy', low, total, 'dot-low', 'Low'),
        ].join('');
    }
}

function legendRow(label, count, total, dotClass, riskVal) {
    return `<div class="legend-row" onclick="setRiskFilter('${riskVal}')">
        <span class="legend-label"><span class="legend-dot ${dotClass}"></span>${label}</span>
        <span><strong>${count.toLocaleString()}</strong> (${pct(count, total)})</span>
    </div>`;
}

function renderTopFactors(d) {
    const factors = d.top_risk_factors || [];
    const ctx = getCtx('topFactorsChart');
    if (ctx) {
        destroyChart('topFactors');
        const top5 = factors.slice(0, 5);
        charts.topFactors = new Chart(ctx, {
            type: 'bar',
            data: { labels: top5.map(f => f.display_label), datasets: [{ label: 'Affected', data: top5.map(f => f.frequency), backgroundColor: 'rgba(239,68,68,0.85)', borderRadius: 4 }] },
            options: { indexAxis: 'y', responsive: true, maintainAspectRatio: false, plugins: { legend: { display: false } }, scales: { x: { grid: { display: false } }, y: { grid: { display: false }, ticks: { font: { size: 10, weight: '600' } } } } }
        });
    }

    const list = document.getElementById('topFactorsList');
    if (list) {
        list.innerHTML = factors.map((f, i) => `
            <div class="factor-card">
                <div class="factor-card-header">
                    <span class="factor-card-name">#${i + 1} ${f.display_label}</span>
                    <span class="factor-card-impact">${f.frequency.toLocaleString()}</span>
                </div>
                <p class="factor-card-desc">${f.factor_message}</p>
            </div>
        `).join('');
    }
}

function renderActionsChart(d) {
    const ctx = getCtx('actionsChart');
    if (!ctx) return;
    destroyChart('actions');
    const actions = d.recommended_actions || {};
    const labels = Object.keys(actions).slice(0, 6).map(a => a.replace(/_/g, ' '));
    const counts = Object.values(actions).slice(0, 6);
    charts.actions = new Chart(ctx, {
        type: 'bar',
        data: { labels, datasets: [{ label: 'Plays', data: counts, backgroundColor: '#6366f1', borderRadius: 4 }] },
        options: { indexAxis: 'y', responsive: true, maintainAspectRatio: false, plugins: { legend: { display: false } }, scales: { x: { grid: { display: false } }, y: { grid: { display: false }, ticks: { font: { size: 10, weight: '600' } } } } }
    });
}

function renderReasonsChart(d) {
    const ctx = getCtx('reasonsChart');
    if (!ctx) return;
    destroyChart('reasons');
    const reasons = d.primary_reasons || {};
    const labels = Object.keys(reasons).slice(0, 6).map(r => r.replace(/_/g, ' '));
    const counts = Object.values(reasons).slice(0, 6);
    charts.reasons = new Chart(ctx, {
        type: 'bar',
        data: { labels, datasets: [{ label: 'Pain Points', data: counts, backgroundColor: '#f59e0b', borderRadius: 4 }] },
        options: { indexAxis: 'y', responsive: true, maintainAspectRatio: false, plugins: { legend: { display: false } }, scales: { x: { grid: { display: false } }, y: { grid: { display: false }, ticks: { font: { size: 10, weight: '600' } } } } }
    });
}

function renderProductDepthChart(d) {
    const ctx = getCtx('productDepthChart');
    if (!ctx) return;
    destroyChart('productDepth');
    const stats = d.product_depth_stats || [];
    charts.productDepth = new Chart(ctx, {
        type: 'bar',
        data: { labels: stats.map(s => s.bracket), datasets: [{ label: 'Avg Churn %', data: stats.map(s => s.avg_churn_prob), backgroundColor: ['#ef4444', '#f59e0b', '#10b981', '#059669'], borderRadius: 4 }] },
        options: { responsive: true, maintainAspectRatio: false, plugins: { legend: { display: false } }, scales: { x: { grid: { display: false } }, y: { title: { display: true, text: 'Avg Churn %' }, grid: { display: false } } } }
    });
}

function renderSegments(d) {
    const grid = document.getElementById('segmentGrid');
    if (!grid) return;
    const segs = d.segment_clusters || [];
    grid.innerHTML = segs.map(s => {
        const color = s.high_risk_pct > 20 ? '#ef4444' : s.high_risk_pct > 10 ? '#f59e0b' : '#10b981';
        return `<div class="segment-card" onclick="filterBySegment('${s.segment}')">
            <div class="segment-card-title">${s.segment} Accounts</div>
            <div class="segment-card-count">${s.total_customers.toLocaleString()} total</div>
            <div class="segment-risk-row">
                <span class="segment-risk-pct" style="color:${color}">${s.high_risk_pct}% Risk</span>
                <span class="segment-risk-rev">₹${(s.at_risk_value / 1e6).toFixed(2)}M at risk</span>
            </div>
            <div class="segment-bar-bg"><div class="segment-bar-fill" style="width:${Math.min(100, s.high_risk_pct * 2.5)}%;background:${color}"></div></div>
        </div>`;
    }).join('');
}

function renderMonthlyTrends(d) {
    const ctx = getCtx('monthlyTrendsChart');
    if (!ctx) return;
    destroyChart('monthlyTrends');
    const trends = d.monthly_trends || [];
    charts.monthlyTrends = new Chart(ctx, {
        type: 'line',
        data: {
            labels: trends.map(t => t.month),
            datasets: [
                { label: 'Balance Δ', data: trends.map(t => t.balance_delta), borderColor: '#6366f1', backgroundColor: 'rgba(99,102,241,0.08)', fill: true, tension: 0.3 },
                { label: 'Transaction Δ', data: trends.map(t => t.txn_delta), borderColor: '#f59e0b', borderDash: [5, 5], tension: 0.3 },
                { label: 'Outflow Δ', data: trends.map(t => t.outflow_delta), borderColor: '#ef4444', borderDash: [3, 3], tension: 0.3 },
            ]
        },
        options: { responsive: true, maintainAspectRatio: false, plugins: { legend: { position: 'top' } }, scales: { x: { grid: { display: false } }, y: { title: { display: true, text: '% Change' } } } }
    });
}

// ---------------------------------------------------------------------------
// Customer Directory
// ---------------------------------------------------------------------------
async function loadCustomers() {
    const [sortBy, sortOrder] = state.sortKey.split('-');
    const offset = (state.page - 1) * state.pageSize;
    const params = new URLSearchParams({
        risk_level: state.riskFilter, segment: state.segment,
        action: state.action, urgency: state.urgency,
        search: state.search, sort_by: sortBy, sort_order: sortOrder,
        limit: state.pageSize, offset,
    });

    try {
        const res = await fetch(`/api/customers?${params}`);
        const data = await res.json();
        state.totalRecords = data.total_count || 0;
        renderCustomerTable(data.customers || []);
        renderPagination();
    } catch (err) { console.error('Customer load error:', err); }
}

function renderCustomerTable(customers) {
    const tbody = document.getElementById('custBody');
    if (!tbody) return;

    if (!customers.length) {
        tbody.innerHTML = `<tr><td colspan="9" style="text-align:center;padding:3rem;color:#94a3b8"><i class="fa-solid fa-folder-open" style="font-size:2rem;display:block;margin-bottom:0.5rem"></i>No accounts match current filters.</td></tr>`;
        return;
    }

    tbody.innerHTML = customers.map(c => {
        const initials = c.customer_name ? c.customer_name.split(' ').map(n => n[0]).join('').slice(0, 2).toUpperCase() : 'CU';
        const badgeClass = c.risk_level === 'High' ? 'badge-high' : c.risk_level === 'Medium' ? 'badge-med' : 'badge-low';
        const probColor = c.risk_level === 'High' ? '#ef4444' : c.risk_level === 'Medium' ? '#f59e0b' : '#10b981';
        const urgTag = c.urgency ? `<span class="urgency-tag urgency-${c.urgency.toLowerCase()}">${c.urgency}</span>` : '';
        const clusterTag = c.cluster_label ? `<span class="cluster-badge">${c.cluster_label}</span>` : '<span style="color:#94a3b8">—</span>';

        return `<tr>
            <td><div class="cust-cell"><div class="cust-avatar">${initials}</div><div><div class="cust-name">${c.customer_name}</div><div class="cust-id">${c.customer_id}</div></div></div></td>
            <td style="text-transform:capitalize;font-weight:600">${c.customer_segment}</td>
            <td><strong>₹${(c.customer_yearly_value || 0).toLocaleString()}</strong></td>
            <td><span class="badge ${badgeClass}">${c.risk_level}</span></td>
            <td><div class="prob-cell"><div class="prob-bg"><div class="prob-fill" style="width:${Math.min(100, c.churn_probability * 1.5)}%;background:${probColor}"></div></div><strong>${(c.churn_probability || 0).toFixed(1)}%</strong></div></td>
            <td>${c.primary_reason ? c.primary_reason.replace(/_/g, ' ') : '<span style="color:#94a3b8">Stable</span>'}</td>
            <td><div style="display:flex;align-items:center;gap:4px">${c.recommended_action ? c.recommended_action.replace(/_/g, ' ') : 'Monitor'} ${urgTag}</div></td>
            <td>${clusterTag}</td>
            <td class="text-right"><button class="btn-audit" onclick="openCustomerModal('${c.customer_id}')"><i class="fa-solid fa-file-waveform"></i> Audit</button></td>
        </tr>`;
    }).join('');
}

function renderPagination() {
    const totalPages = Math.max(1, Math.ceil(state.totalRecords / state.pageSize));
    setText('pageNum', state.page);
    setText('totalPages', totalPages);
    const s = state.totalRecords === 0 ? 0 : (state.page - 1) * state.pageSize + 1;
    const e = Math.min(state.totalRecords, state.page * state.pageSize);
    setText('showCount', `${s}-${e}`);
    setText('totalCount', state.totalRecords.toLocaleString());
    const prev = document.getElementById('prevBtn');
    const next = document.getElementById('nextBtn');
    if (prev) prev.disabled = state.page <= 1;
    if (next) next.disabled = state.page >= totalPages;
}

// ---------------------------------------------------------------------------
// Customer Detail Modal
// ---------------------------------------------------------------------------
function setupModal() {
    const overlay = document.getElementById('customerModal');
    const closeBtn = document.getElementById('modalCloseBtn');
    if (closeBtn) closeBtn.addEventListener('click', () => overlay?.classList.remove('active'));
    overlay?.addEventListener('click', e => { if (e.target === overlay) overlay.classList.remove('active'); });
    document.addEventListener('keydown', e => { if (e.key === 'Escape') overlay?.classList.remove('active'); });
}

window.openCustomerModal = async function(cid) {
    const modal = document.getElementById('customerModal');
    const content = document.getElementById('modalContent');
    modal?.classList.add('active');
    content.innerHTML = '<div class="modal-loading"><i class="fa-solid fa-spinner fa-spin"></i><p>Loading...</p></div>';

    try {
        const [pRes, hRes] = await Promise.all([fetch(`/api/customer/${cid}`), fetch(`/api/customer/${cid}/history`)]);
        const profileData = await pRes.json();
        const historyData = await hRes.json();
        renderModal(profileData, historyData);
    } catch (err) {
        content.innerHTML = '<div class="modal-loading" style="color:#ef4444"><i class="fa-solid fa-triangle-exclamation"></i><p>Failed to load customer data.</p></div>';
    }
};

function renderModal(data, history) {
    const content = document.getElementById('modalContent');
    const p = data.profile;
    const factors = data.risk_factors || [];
    const evidence = data.evidence || [];
    const initials = p.customer_name ? p.customer_name.split(' ').map(n => n[0]).join('').slice(0, 2).toUpperCase() : 'CU';
    const badgeClass = p.risk_level === 'High' ? 'badge-high' : p.risk_level === 'Medium' ? 'badge-med' : 'badge-low';
    const urgTag = p.urgency ? `<span class="urgency-tag urgency-${p.urgency.toLowerCase()}">${p.urgency} PRIORITY</span>` : '';

    content.innerHTML = `
        <div class="modal-hero">
            <div class="modal-hero-avatar">${initials}</div>
            <div style="flex:1">
                <h2>${p.customer_name} <span style="font-size:0.85rem;opacity:0.7;font-weight:400">(${p.customer_id})</span></h2>
                <div class="modal-hero-badges">
                    <span class="hero-badge"><i class="fa-solid fa-briefcase"></i> ${(p.customer_segment || '').toUpperCase()}</span>
                    <span class="hero-badge"><i class="fa-solid fa-clock"></i> ${p.tenure_months}mo tenure</span>
                    <span class="hero-badge"><i class="fa-solid fa-coins"></i> ₹${(p.customer_yearly_value || 0).toLocaleString()}</span>
                    ${p.cluster_label ? `<span class="hero-badge"><i class="fa-solid fa-object-group"></i> ${p.cluster_label}</span>` : ''}
                </div>
            </div>
            <div style="text-align:right">
                <span class="badge ${badgeClass}" style="font-size:0.85rem;padding:6px 16px">${p.risk_level} Risk</span>
                <div style="font-size:1.8rem;font-weight:800;margin-top:4px">${(p.churn_probability || 0).toFixed(1)}%</div>
            </div>
        </div>
        <div class="modal-body">
            <div class="modal-dual">
                <div class="modal-section">
                    <div class="modal-section-title"><i class="fa-solid fa-chart-line"></i><span>Key Risk Indicators</span><span style="margin-left:auto;font-size:0.72rem;color:#94a3b8">Score: ${(p.risk_score || 0).toFixed(1)}/100</span></div>
                    ${factors.map(f => `<div class="shap-row"><div><div class="shap-name">#${f.factor_rank} ${f.factor_name.replace(/_/g, ' ')}</div><div class="shap-msg">${f.factor_message}</div></div><span class="shap-impact">+${(f.contribution || 0).toFixed(3)}</span></div>`).join('')}
                </div>
                <div class="modal-section">
                    <div class="modal-section-title"><i class="fa-solid fa-headset"></i><span>AI Retention Plan</span>${urgTag}</div>
                    <div style="margin-bottom:10px"><strong>Friction Point:</strong> <span style="color:#f59e0b;font-weight:700">${p.primary_reason ? p.primary_reason.replace(/_/g, ' ') : 'N/A'}</span></div>
                    <div style="margin-bottom:10px"><strong>Recommended:</strong> <span style="color:#6366f1;font-weight:700">${p.recommended_action ? p.recommended_action.replace(/_/g, ' ') : 'MONITOR'}</span></div>
                    <div class="reasoning-box">"${p.reasoning_summary || 'Standard retention profile.'}"</div>
                    ${evidence.length ? `<div style="margin-top:12px"><strong style="font-size:0.75rem;color:#64748b;text-transform:uppercase">Evidence</strong><div class="evidence-tags" style="margin-top:6px">${evidence.map(e => `<span class="evidence-tag">${e.evidence_text}</span>`).join('')}</div></div>` : ''}
                </div>
            </div>
            <div class="modal-history">
                <div class="modal-history-title"><i class="fa-solid fa-timeline text-slate"></i><span>6-Month Account Trajectory</span></div>
                <div class="modal-chart-wrap"><canvas id="modalHistChart"></canvas></div>
                <div style="overflow-x:auto;margin-top:12px">
                    <table class="mini-table"><thead><tr><th>Month</th><th>Balance Δ</th><th>Txn Δ</th><th>App Δ</th><th>Complaints</th><th>Failed Txns</th><th>Complaint Note</th></tr></thead>
                    <tbody>${history.map(h => `<tr>
                        <td><strong>${h.snapshot_date.substring(0, 7)}</strong></td>
                        <td style="color:${(h.balance_change_30d || 0) < 0 ? '#ef4444' : '#10b981'}">${(h.balance_change_30d || 0).toFixed(1)}%</td>
                        <td style="color:${(h.transaction_change_30d || 0) < 0 ? '#ef4444' : '#10b981'}">${(h.transaction_change_30d || 0).toFixed(1)}%</td>
                        <td>${(h.app_login_change_30d || 0).toFixed(1)}%</td>
                        <td>${h.complaints_30d || 0}</td>
                        <td>${h.failed_transactions_30d || 0}</td>
                        <td>${h.complaint_text ? `<em style="color:#64748b">"${h.complaint_text}"</em>` : '<span style="color:#cbd5e1">—</span>'}</td>
                    </tr>`).join('')}</tbody></table>
                </div>
            </div>
        </div>
    `;

    // Render modal chart
    setTimeout(() => {
        const ctx = getCtx('modalHistChart');
        if (!ctx) return;
        destroyChart('modalHist');
        const sorted = [...history].sort((a, b) => a.snapshot_date.localeCompare(b.snapshot_date));
        charts.modalHist = new Chart(ctx, {
            type: 'line',
            data: {
                labels: sorted.map(h => h.snapshot_date.substring(0, 7)),
                datasets: [
                    { label: 'Balance Δ %', data: sorted.map(h => h.balance_change_30d || 0), borderColor: '#6366f1', backgroundColor: 'rgba(99,102,241,0.08)', fill: true, tension: 0.3 },
                    { label: 'Txn Δ %', data: sorted.map(h => h.transaction_change_30d || 0), borderColor: '#f59e0b', borderDash: [5, 5], tension: 0.3 },
                ]
            },
            options: { responsive: true, maintainAspectRatio: false, plugins: { legend: { position: 'top' } }, scales: { x: { grid: { display: false } }, y: { title: { display: true, text: '% Change' } } } }
        });
    }, 50);
}

// ---------------------------------------------------------------------------
// Individual Analysis Tab
// ---------------------------------------------------------------------------
function setupAnalysisSearch() {
    const input = document.getElementById('analysisSearchInput');
    const btn = document.getElementById('analysisSearchBtn');
    if (btn) btn.addEventListener('click', () => runAnalysis(input?.value?.trim()));
    if (input) input.addEventListener('keypress', e => { if (e.key === 'Enter') runAnalysis(input.value.trim()); });
}

async function runAnalysis(cid) {
    if (!cid) return;
    const container = document.getElementById('analysisContent');
    container.innerHTML = '<div class="modal-loading"><i class="fa-solid fa-spinner fa-spin"></i><p>Analyzing customer...</p></div>';

    try {
        const res = await fetch(`/api/customer/${cid}/retention_analysis`);
        if (!res.ok) { container.innerHTML = `<div class="empty-state"><i class="fa-solid fa-triangle-exclamation" style="color:#ef4444"></i><p>Customer <strong>${cid}</strong> not found. Please check the ID.</p></div>`; return; }
        const data = await res.json();
        renderAnalysis(data, container);
    } catch (err) {
        container.innerHTML = '<div class="empty-state"><i class="fa-solid fa-triangle-exclamation" style="color:#ef4444"></i><p>Error loading analysis.</p></div>';
    }
}

function renderAnalysis(data, container) {
    const p = data.profile;
    const factors = data.risk_factors || [];
    const evidence = data.evidence || [];
    const history = data.history || [];
    const cluster = data.cluster_profile;
    const initials = p.customer_name ? p.customer_name.split(' ').map(n => n[0]).join('').slice(0, 2).toUpperCase() : 'CU';
    const badgeClass = p.risk_level === 'High' ? 'badge-high' : p.risk_level === 'Medium' ? 'badge-med' : 'badge-low';
    const probColor = p.risk_level === 'High' ? '#ef4444' : p.risk_level === 'Medium' ? '#f59e0b' : '#10b981';

    container.innerHTML = `
        <div class="analysis-hero">
            <div class="analysis-avatar">${initials}</div>
            <div class="analysis-hero-info">
                <h2>${p.customer_name} <span style="font-size:0.85rem;opacity:0.7;font-weight:400">(${p.customer_id})</span></h2>
                <div class="analysis-hero-badges">
                    <span class="hero-badge"><i class="fa-solid fa-briefcase"></i> ${(p.customer_segment || '').toUpperCase()}</span>
                    <span class="hero-badge"><i class="fa-solid fa-clock"></i> ${p.tenure_months}mo</span>
                    <span class="hero-badge"><i class="fa-solid fa-coins"></i> ₹${(p.customer_yearly_value || 0).toLocaleString()}</span>
                    <span class="hero-badge"><i class="fa-solid fa-cubes"></i> ${p.products_count || 0} Products</span>
                    ${p.cluster_label ? `<span class="hero-badge"><i class="fa-solid fa-object-group"></i> Cluster: ${p.cluster_label}</span>` : ''}
                </div>
            </div>
            <div class="analysis-hero-risk">
                <span class="badge ${badgeClass}" style="font-size:0.85rem;padding:6px 16px">${p.risk_level}</span>
                <div class="risk-pct" style="color:${probColor}">${(p.churn_probability || 0).toFixed(1)}%</div>
                <div style="font-size:0.72rem;opacity:0.7">Risk Score: ${(p.risk_score || 0).toFixed(1)}/100</div>
            </div>
        </div>

        <div class="analysis-grid">
            <div class="analysis-card">
                <div class="analysis-card-title"><i class="fa-solid fa-chart-line"></i>Model 1 v2 — Churn Risk Factors</div>
                ${factors.map(f => `<div class="shap-row"><div><div class="shap-name">#${f.factor_rank} ${f.factor_name.replace(/_/g, ' ')}</div><div class="shap-msg">${f.factor_message}</div></div><span class="shap-impact">+${(f.contribution || 0).toFixed(3)}</span></div>`).join('')}
            </div>
            <div class="analysis-card">
                <div class="analysis-card-title"><i class="fa-solid fa-headset"></i>Model 2 (Devang) — Retention Analysis</div>
                <div style="margin-bottom:8px"><strong>Primary Reason:</strong> <span style="color:#f59e0b;font-weight:700">${p.primary_reason ? p.primary_reason.replace(/_/g, ' ') : 'N/A'}</span></div>
                ${p.secondary_reasons ? `<div style="margin-bottom:8px;font-size:0.82rem"><strong>Secondary:</strong> ${p.secondary_reasons.replace(/,/g, ', ').replace(/_/g, ' ')}</div>` : ''}
                <div style="margin-bottom:8px"><strong>Action:</strong> <span style="color:#6366f1;font-weight:700">${p.recommended_action ? p.recommended_action.replace(/_/g, ' ') : 'MONITOR'}</span></div>
                <div style="margin-bottom:12px"><strong>Urgency:</strong> <span class="urgency-tag urgency-${(p.urgency || 'medium').toLowerCase()}">${p.urgency || 'MEDIUM'}</span></div>
                <div class="reasoning-box">"${p.reasoning_summary || 'Standard retention profile.'}"</div>
                ${evidence.length ? `<div style="margin-top:12px"><strong style="font-size:0.72rem;color:#64748b;text-transform:uppercase">Evidence</strong><div class="evidence-tags" style="margin-top:6px">${evidence.map(e => `<span class="evidence-tag">${e.evidence_text}</span>`).join('')}</div></div>` : ''}
            </div>
        </div>

        ${cluster ? `<div class="analysis-card" style="margin-top:20px">
            <div class="analysis-card-title"><i class="fa-solid fa-object-group"></i>Cluster Context — ${cluster.cluster_label} (${cluster.customer_count.toLocaleString()} customers)</div>
            <div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(160px,1fr));gap:12px;margin-top:8px">
                <div><span style="font-size:0.72rem;color:#64748b">Avg Churn</span><div style="font-size:1.1rem;font-weight:700">${cluster.avg_churn_probability.toFixed(1)}%</div></div>
                <div><span style="font-size:0.72rem;color:#64748b">Avg Balance Δ</span><div style="font-size:1.1rem;font-weight:700">${cluster.avg_balance_change_30d.toFixed(1)}%</div></div>
                <div><span style="font-size:0.72rem;color:#64748b">Avg Txn Δ</span><div style="font-size:1.1rem;font-weight:700">${cluster.avg_transaction_change_30d.toFixed(1)}%</div></div>
                <div><span style="font-size:0.72rem;color:#64748b">Dominant Reason</span><div style="font-size:0.85rem;font-weight:700">${cluster.dominant_primary_reason.replace(/_/g, ' ')}</div></div>
                <div><span style="font-size:0.72rem;color:#64748b">High Risk</span><div style="font-size:1.1rem;font-weight:700;color:#ef4444">${cluster.high_risk_count.toLocaleString()}</div></div>
                <div><span style="font-size:0.72rem;color:#64748b">Medium Risk</span><div style="font-size:1.1rem;font-weight:700;color:#f59e0b">${cluster.medium_risk_count.toLocaleString()}</div></div>
            </div>
        </div>` : ''}

        <div style="margin-top:20px"><div class="analysis-card-title" style="margin-bottom:12px"><i class="fa-solid fa-timeline text-slate"></i>6-Month Behavioral Trajectory</div>
        <div class="history-chart-wrap"><canvas id="analysisHistChart"></canvas></div></div>
    `;

    // Render chart
    setTimeout(() => {
        const ctx = getCtx('analysisHistChart');
        if (!ctx) return;
        destroyChart('analysisHist');
        const sorted = [...history].sort((a, b) => a.snapshot_date.localeCompare(b.snapshot_date));
        charts.analysisHist = new Chart(ctx, {
            type: 'line',
            data: {
                labels: sorted.map(h => h.snapshot_date.substring(0, 7)),
                datasets: [
                    { label: 'Balance Δ', data: sorted.map(h => h.balance_change_30d || 0), borderColor: '#6366f1', backgroundColor: 'rgba(99,102,241,0.08)', fill: true, tension: 0.3 },
                    { label: 'Txn Δ', data: sorted.map(h => h.transaction_change_30d || 0), borderColor: '#f59e0b', borderDash: [5, 5], tension: 0.3 },
                    { label: 'Complaints', data: sorted.map(h => h.complaints_30d || 0), borderColor: '#ef4444', tension: 0.3, yAxisID: 'y1' },
                ]
            },
            options: {
                responsive: true, maintainAspectRatio: false,
                plugins: { legend: { position: 'top' } },
                scales: {
                    x: { grid: { display: false } },
                    y: { title: { display: true, text: '% Change' }, position: 'left' },
                    y1: { title: { display: true, text: 'Count' }, position: 'right', grid: { drawOnChartArea: false } },
                }
            }
        });
    }, 50);
}

// ---------------------------------------------------------------------------
// Cluster Analysis Tab
// ---------------------------------------------------------------------------
async function loadClusters() {
    try {
        const res = await fetch('/api/clusters');
        const data = await res.json();
        state.clusterData = data.clusters || [];
        renderClusterOverview(state.clusterData);
        renderClusterRadar(state.clusterData);
    } catch (err) { console.error('Cluster load error:', err); }
}

function renderClusterOverview(clusters) {
    const grid = document.getElementById('clusterOverview');
    if (!grid) return;
    grid.innerHTML = clusters.map(c => {
        const total = c.customer_count;
        const highPct = total > 0 ? ((c.high_risk_count / total) * 100).toFixed(1) : 0;
        const medPct = total > 0 ? ((c.medium_risk_count / total) * 100).toFixed(1) : 0;
        const lowPct = total > 0 ? ((c.low_risk_count / total) * 100).toFixed(1) : 0;

        return `<div class="cluster-card" onclick="drillCluster(${c.cluster_id})">
            <div class="cluster-card-header">
                <div><div class="cluster-card-label">${c.cluster_label}</div><div class="cluster-card-id">Cluster ${c.cluster_id}</div></div>
                <span class="cluster-card-count">${total.toLocaleString()} customers</span>
            </div>
            <div class="cluster-stats">
                <div class="cluster-stat"><div class="cluster-stat-val">${c.avg_churn_probability.toFixed(1)}%</div><div class="cluster-stat-label">Avg Churn</div></div>
                <div class="cluster-stat"><div class="cluster-stat-val">${c.avg_risk_score.toFixed(0)}</div><div class="cluster-stat-label">Avg Risk Score</div></div>
                <div class="cluster-stat"><div class="cluster-stat-val">${c.dominant_primary_reason.replace(/_/g, ' ').substring(0, 18)}</div><div class="cluster-stat-label">Top Reason</div></div>
                <div class="cluster-stat"><div class="cluster-stat-val">${c.dominant_recommended_action.replace(/_/g, ' ').substring(0, 18)}</div><div class="cluster-stat-label">Top Action</div></div>
            </div>
            <div class="cluster-risk-bar">
                <div style="width:${highPct}%;background:#ef4444"></div>
                <div style="width:${medPct}%;background:#f59e0b"></div>
                <div style="width:${lowPct}%;background:#10b981"></div>
            </div>
        </div>`;
    }).join('');
}

function renderClusterRadar(clusters) {
    const panel = document.getElementById('clusterRadarPanel');
    if (panel) panel.style.display = 'block';
    const ctx = getCtx('clusterRadarChart');
    if (!ctx) return;
    destroyChart('clusterRadar');

    const featureLabels = ['Balance Δ', 'Txn Δ', 'Inactivity', 'External Xfer', 'Complaints', 'App Login Δ', 'Card Spend Δ', 'Failed Txns', 'Unresolved', 'EMI Bounce'];
    const featureKeys = [
        'avg_balance_change_30d', 'avg_transaction_change_30d', 'avg_days_since_last_transaction',
        'avg_external_transfer_change_30d', 'avg_complaints_30d', 'avg_app_login_change_30d',
        'avg_card_spend_change_30d', 'avg_failed_transactions_30d', 'avg_unresolved_complaints', 'avg_emi_bounce_30d'
    ];

    // Normalize each feature across clusters to 0-100
    const allValues = featureKeys.map(key => clusters.map(c => Math.abs(c[key] || 0)));
    const maxValues = allValues.map(arr => Math.max(...arr, 0.01));

    const colors = ['rgba(99,102,241,0.7)', 'rgba(239,68,68,0.7)', 'rgba(245,158,11,0.7)', 'rgba(16,185,129,0.7)', 'rgba(244,63,94,0.7)'];
    const bgColors = ['rgba(99,102,241,0.1)', 'rgba(239,68,68,0.1)', 'rgba(245,158,11,0.1)', 'rgba(16,185,129,0.1)', 'rgba(244,63,94,0.1)'];

    const datasets = clusters.map((c, i) => ({
        label: c.cluster_label,
        data: featureKeys.map((key, j) => (Math.abs(c[key] || 0) / maxValues[j]) * 100),
        borderColor: colors[i % colors.length],
        backgroundColor: bgColors[i % bgColors.length],
        borderWidth: 2,
        pointRadius: 3,
    }));

    charts.clusterRadar = new Chart(ctx, {
        type: 'radar',
        data: { labels: featureLabels, datasets },
        options: {
            responsive: true, maintainAspectRatio: false,
            plugins: { legend: { position: 'top' } },
            scales: { r: { beginAtZero: true, max: 100, ticks: { display: false }, grid: { color: 'rgba(0,0,0,0.05)' } } }
        }
    });
}

window.drillCluster = async function(clusterId) {
    const panel = document.getElementById('clusterDrillPanel');
    if (panel) panel.style.display = 'block';

    try {
        const res = await fetch(`/api/cluster/${clusterId}`);
        const data = await res.json();
        const profile = data.profile;
        const customers = data.customers || [];
        const reasons = data.reason_distribution || {};

        setText('clusterDrillTitle', `${profile.cluster_label} — ${profile.customer_count.toLocaleString()} Customers`);

        // Reason chart
        const ctx = getCtx('clusterReasonChart');
        if (ctx) {
            destroyChart('clusterReason');
            const labels = Object.keys(reasons).map(r => r.replace(/_/g, ' ')).slice(0, 6);
            const counts = Object.values(reasons).slice(0, 6);
            charts.clusterReason = new Chart(ctx, {
                type: 'bar',
                data: { labels, datasets: [{ label: 'Customers', data: counts, backgroundColor: '#6366f1', borderRadius: 4 }] },
                options: { indexAxis: 'y', responsive: true, maintainAspectRatio: false, plugins: { legend: { display: false } }, scales: { x: { grid: { display: false } }, y: { grid: { display: false }, ticks: { font: { size: 10 } } } } }
            });
        }

        // Feature table
        const featureTable = document.getElementById('clusterFeatureTable');
        if (featureTable) {
            const features = [
                ['Avg Balance Δ', profile.avg_balance_change_30d],
                ['Avg Txn Δ', profile.avg_transaction_change_30d],
                ['Avg Inactivity (days)', profile.avg_days_since_last_transaction],
                ['Avg External Xfer Δ', profile.avg_external_transfer_change_30d],
                ['Avg Complaints', profile.avg_complaints_30d],
                ['Avg App Login Δ', profile.avg_app_login_change_30d],
                ['Avg Card Spend Δ', profile.avg_card_spend_change_30d],
                ['Avg Failed Txns', profile.avg_failed_transactions_30d],
                ['Avg Unresolved', profile.avg_unresolved_complaints],
                ['Avg EMI Bounce', profile.avg_emi_bounce_30d],
            ];
            featureTable.innerHTML = `<table><thead><tr><th>Feature</th><th>Cluster Average</th></tr></thead>
                <tbody>${features.map(([name, val]) => `<tr><td>${name}</td><td style="font-weight:700;color:${val < 0 ? '#ef4444' : '#10b981'}">${(val || 0).toFixed(2)}</td></tr>`).join('')}</tbody></table>`;
        }

        // Customer table
        const tbody = document.getElementById('clusterCustBody');
        if (tbody) {
            tbody.innerHTML = customers.slice(0, 50).map(c => {
                const badge = c.risk_level === 'High' ? 'badge-high' : c.risk_level === 'Medium' ? 'badge-med' : 'badge-low';
                return `<tr>
                    <td><strong>${c.customer_name}</strong><br><span style="font-size:0.72rem;color:#94a3b8">${c.customer_id}</span></td>
                    <td style="text-transform:capitalize">${c.customer_segment}</td>
                    <td>₹${(c.customer_yearly_value || 0).toLocaleString()}</td>
                    <td><span class="badge ${badge}">${c.risk_level}</span></td>
                    <td>${(c.churn_probability || 0).toFixed(1)}%</td>
                    <td>${c.primary_reason ? c.primary_reason.replace(/_/g, ' ') : '—'}</td>
                    <td>${c.recommended_action ? c.recommended_action.replace(/_/g, ' ') : 'Monitor'}</td>
                </tr>`;
            }).join('');
        }

        // Scroll to drill panel
        panel.scrollIntoView({ behavior: 'smooth', block: 'start' });
    } catch (err) { console.error('Cluster drill error:', err); }
};

// ---------------------------------------------------------------------------
// Visualizations Tab
// ---------------------------------------------------------------------------
async function loadVisualizations() {
    if (!state.dashData) {
        try {
            const res = await fetch('/api/dashboard_stats');
            state.dashData = await res.json();
        } catch (err) { console.error('Viz load error:', err); return; }
    }

    const d = state.dashData;

    // Feature Importance
    try {
        const fRes = await fetch('/api/feature_importance');
        const fData = await fRes.json();
        const ctx = getCtx('featureImpChart');
        if (ctx) {
            destroyChart('featureImp');
            const features = fData.features || [];
            charts.featureImp = new Chart(ctx, {
                type: 'bar',
                data: {
                    labels: features.map(f => f.display_label),
                    datasets: [{ label: 'Avg Contribution', data: features.map(f => f.avg_contribution), backgroundColor: 'rgba(99,102,241,0.8)', borderRadius: 4 }]
                },
                options: { indexAxis: 'y', responsive: true, maintainAspectRatio: false, plugins: { legend: { display: false } }, scales: { x: { grid: { display: false }, title: { display: true, text: 'Avg SHAP Contribution' } }, y: { grid: { display: false }, ticks: { font: { size: 9, weight: '600' } } } } }
            });
        }
    } catch (err) { console.error('Feature importance error:', err); }

    // Risk Distribution (pie)
    const rCtx = getCtx('vizRiskChart');
    if (rCtx) {
        destroyChart('vizRisk');
        const dist = d.risk_distribution || {};
        charts.vizRisk = new Chart(rCtx, {
            type: 'pie',
            data: {
                labels: ['High Risk', 'Watchlist', 'Healthy'],
                datasets: [{ data: [dist.High || 0, dist.Medium || 0, dist.Low || 0], backgroundColor: ['#ef4444', '#f59e0b', '#10b981'] }]
            },
            options: { responsive: true, maintainAspectRatio: false, plugins: { legend: { position: 'bottom' } } }
        });
    }

    // Reasons
    const rrCtx = getCtx('vizReasonsChart');
    if (rrCtx) {
        destroyChart('vizReasons');
        const reasons = d.primary_reasons || {};
        const labels = Object.keys(reasons).map(r => r.replace(/_/g, ' '));
        charts.vizReasons = new Chart(rrCtx, {
            type: 'doughnut',
            data: { labels, datasets: [{ data: Object.values(reasons), backgroundColor: ['#6366f1', '#ef4444', '#f59e0b', '#10b981', '#f43f5e', '#0ea5e9', '#8b5cf6', '#14b8a6', '#64748b', '#e11d48'] }] },
            options: { responsive: true, maintainAspectRatio: false, cutout: '50%', plugins: { legend: { position: 'bottom', labels: { font: { size: 10 } } } } }
        });
    }

    // Actions Stacked
    const aCtx = getCtx('vizActionsChart');
    if (aCtx) {
        destroyChart('vizActions');
        const matrix = d.actions_matrix || {};
        const actions = Object.keys(matrix).slice(0, 8);
        charts.vizActions = new Chart(aCtx, {
            type: 'bar',
            data: {
                labels: actions.map(a => a.replace(/_/g, ' ')),
                datasets: [
                    { label: 'HIGH', data: actions.map(a => matrix[a]?.HIGH || 0), backgroundColor: '#ef4444', borderRadius: 2 },
                    { label: 'MEDIUM', data: actions.map(a => matrix[a]?.MEDIUM || 0), backgroundColor: '#f59e0b', borderRadius: 2 },
                    { label: 'LOW', data: actions.map(a => matrix[a]?.LOW || 0), backgroundColor: '#10b981', borderRadius: 2 },
                ]
            },
            options: { responsive: true, maintainAspectRatio: false, plugins: { legend: { position: 'top' } }, scales: { x: { stacked: true, grid: { display: false }, ticks: { font: { size: 9 } } }, y: { stacked: true, grid: { display: false } } } }
        });
    }

    // Monthly Trends
    const tCtx = getCtx('vizTrendsChart');
    if (tCtx) {
        destroyChart('vizTrends');
        const trends = d.monthly_trends || [];
        charts.vizTrends = new Chart(tCtx, {
            type: 'line',
            data: {
                labels: trends.map(t => t.month),
                datasets: [
                    { label: 'Balance Δ', data: trends.map(t => t.balance_delta), borderColor: '#6366f1', fill: false, tension: 0.3, pointRadius: 5 },
                    { label: 'Transaction Δ', data: trends.map(t => t.txn_delta), borderColor: '#f59e0b', fill: false, tension: 0.3, pointRadius: 5 },
                    { label: 'Outflow Δ', data: trends.map(t => t.outflow_delta), borderColor: '#ef4444', fill: false, tension: 0.3, pointRadius: 5 },
                    { label: 'Failed Txns', data: trends.map(t => t.failed_txns), borderColor: '#64748b', fill: false, tension: 0.3, pointRadius: 5 },
                ]
            },
            options: { responsive: true, maintainAspectRatio: false, plugins: { legend: { position: 'top' } }, scales: { x: { grid: { display: false } }, y: { grid: { color: 'rgba(0,0,0,0.04)' } } } }
        });
    }
}

// ---------------------------------------------------------------------------
// CSV Export
// ---------------------------------------------------------------------------
async function exportCSV() {
    try {
        const [sortBy, sortOrder] = state.sortKey.split('-');
        const params = new URLSearchParams({
            risk_level: state.riskFilter, segment: state.segment, action: state.action,
            urgency: state.urgency, search: state.search, sort_by: sortBy, sort_order: sortOrder,
            limit: 500, offset: 0,
        });
        const res = await fetch(`/api/customers?${params}`);
        const data = await res.json();
        const list = data.customers || [];
        if (!list.length) { alert('No records to export.'); return; }

        const headers = ['Customer ID', 'Name', 'Segment', 'Annual Value', 'Risk Level', 'Risk Score', 'Churn %', 'Pain Point', 'Action', 'Urgency', 'Cluster'];
        const rows = list.map(c => [
            `"${c.customer_id}"`, `"${c.customer_name}"`, `"${c.customer_segment}"`,
            c.customer_yearly_value, c.risk_level, c.risk_score,
            c.churn_probability, `"${(c.primary_reason || '').replace(/_/g, ' ')}"`,
            `"${(c.recommended_action || '').replace(/_/g, ' ')}"`, c.urgency || '',
            `"${c.cluster_label || ''}"`,
        ]);

        const csv = [headers.join(','), ...rows.map(r => r.join(','))].join('\n');
        const blob = new Blob([csv], { type: 'text/csv' });
        const url = URL.createObjectURL(blob);
        const a = document.createElement('a');
        a.href = url;
        a.download = `FinRetain_Export_${new Date().toISOString().slice(0, 10)}.csv`;
        a.click();
        URL.revokeObjectURL(url);
    } catch (err) { console.error('Export error:', err); }
}

// ---------------------------------------------------------------------------
// Helpers
// ---------------------------------------------------------------------------
function setText(id, text) { const el = document.getElementById(id); if (el) el.textContent = text; }
function pct(val, total) { return total > 0 ? `${((val / total) * 100).toFixed(1)}%` : '0%'; }
function getCtx(id) { const el = document.getElementById(id); return el ? el.getContext('2d') : null; }
function destroyChart(key) { if (charts[key]) { charts[key].destroy(); charts[key] = null; } }
