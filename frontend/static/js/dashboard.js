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

async function loadDashboard() {
    try {
        const res = await fetch('/api/dashboard_stats');
        if (!res.ok) {
            console.error('Failed to fetch /api/dashboard_stats, status:', res.status);
            return;
        }
        const data = await res.json();
        state.dashData = data;
        
        try { renderKPIs(data); } catch (e) { console.error('Error in renderKPIs:', e); }
        try { renderRiskChart(data); } catch (e) { console.error('Error in renderRiskChart:', e); }
        try { renderTopFactors(data); } catch (e) { console.error('Error in renderTopFactors:', e); }
        try { renderActionsChart(data); } catch (e) { console.error('Error in renderActionsChart:', e); }
        try { renderReasonsChart(data); } catch (e) { console.error('Error in renderReasonsChart:', e); }
        try { renderProductDepthChart(data); } catch (e) { console.error('Error in renderProductDepthChart:', e); }
        try { renderSegments(data); } catch (e) { console.error('Error in renderSegments:', e); }
        try { renderMonthlyTrends(data); } catch (e) { console.error('Error in renderMonthlyTrends:', e); }
    } catch (err) {
        console.error('Dashboard load error:', err);
    }
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

    const reasonDisplay = p.primary_reason 
        ? `<span style="color:#f59e0b;font-weight:700">${p.primary_reason.replace(/_/g, ' ')}</span>`
        : `<span style="color:#10b981;font-weight:600"><i class="fa-solid fa-shield-check"></i> Low Risk (Healthy Account)</span>`;

    const actionDisplay = p.recommended_action 
        ? `<span style="color:#6366f1;font-weight:700">${p.recommended_action.replace(/_/g, ' ')}</span>`
        : `<span style="color:#6366f1;font-weight:700">MONITOR</span>`;

    const evidenceHtml = evidence.length 
        ? `<div class="evidence-section"><div class="evidence-section-title">Diagnostic Evidence</div><div class="evidence-pill-grid">${evidence.map(e => `<span class="evidence-pill">${e.evidence_text}</span>`).join('')}</div></div>`
        : `<div class="evidence-section"><div class="evidence-section-title">Account Diagnosis</div><div style="font-size:0.8rem;color:#10b981;display:flex;align-items:center;gap:6px"><i class="fa-solid fa-circle-check"></i> Behavioral activity is within healthy thresholds. Standard monitoring active.</div></div>`;

    const sortedHistory = [...history].sort((a, b) => a.snapshot_date.localeCompare(b.snapshot_date));

    content.innerHTML = `
        <div class="profile-hero">
            <div class="profile-hero-left">
                <div class="profile-avatar">${initials}</div>
                <div class="profile-info">
                    <h2>${p.customer_name} <span>(${p.customer_id})</span></h2>
                    <div class="profile-chips">
                        <span class="profile-chip"><i class="fa-solid fa-briefcase"></i> ${(p.customer_segment || '').toUpperCase()}</span>
                        <span class="profile-chip"><i class="fa-solid fa-clock"></i> ${p.tenure_months}mo tenure</span>
                        <span class="profile-chip"><i class="fa-solid fa-coins"></i> ₹${(p.customer_yearly_value || 0).toLocaleString()}</span>
                        <span class="profile-chip"><i class="fa-solid fa-cubes"></i> ${p.products_count || 0} Products</span>
                        ${p.cluster_label ? `<span class="profile-chip"><i class="fa-solid fa-object-group"></i> ${p.cluster_label}</span>` : ''}
                    </div>
                </div>
            </div>
            <div class="profile-hero-metrics">
                <div class="hero-metric-box">
                    <span class="badge ${badgeClass}" style="font-size:0.8rem;padding:4px 14px">${p.risk_level} Risk</span>
                    <div class="hero-churn-val">${(p.churn_probability || 0).toFixed(1)}%</div>
                    <span class="hero-score-sub">Risk Score: ${(p.risk_score || 0).toFixed(1)} / 100</span>
                </div>
            </div>
        </div>
        <div class="modal-body">
            <div class="profile-grid-2">
                <div class="profile-card">
                    <div class="profile-card-header">
                        <div class="profile-card-title"><i class="fa-solid fa-chart-line"></i>Key Risk Drivers (XGBoost SHAP)</div>
                    </div>
                    <div class="driver-list">
                        ${factors.map((f, idx) => `
                            <div class="driver-item">
                                <div class="driver-item-header">
                                    <span class="driver-name"><span style="color:var(--blue);font-weight:700;margin-right:4px">#${idx+1}</span> ${f.display_label || f.factor_name.replace(/_/g, ' ')}</span>
                                    <span class="driver-contrib">+${(f.contribution || 0).toFixed(3)}</span>
                                </div>
                                <div class="driver-desc">${f.factor_message}</div>
                            </div>
                        `).join('')}
                    </div>
                </div>
                <div class="profile-card">
                    <div class="profile-card-header">
                        <div class="profile-card-title"><i class="fa-solid fa-headset"></i>Retention Playbook (AI Strategy)</div>
                        ${urgTag}
                    </div>
                    <div class="playbook-row">
                        <span class="playbook-label">Diagnosis:</span>
                        <span class="playbook-val">${reasonDisplay}</span>
                    </div>
                    <div class="playbook-row">
                        <span class="playbook-label">Next Action:</span>
                        <span class="playbook-val">${actionDisplay}</span>
                    </div>
                    <div class="playbook-reasoning">"${p.reasoning_summary || 'Customer exhibits stable engagement metrics with low churn probability.'}"</div>
                    ${evidenceHtml}
                </div>
            </div>

            <div class="trajectory-panel">
                <div class="trajectory-header">
                    <div class="profile-card-title"><i class="fa-solid fa-timeline"></i>6-Month Account Trajectory</div>
                </div>
                <div class="trajectory-chart-wrap"><canvas id="modalHistChart"></canvas></div>
                <div class="monthly-strip">
                    ${sortedHistory.map(h => {
                        const balColor = (h.balance_change_30d || 0) < 0 ? 'var(--risk-high)' : 'var(--risk-low)';
                        const txnColor = (h.transaction_change_30d || 0) < 0 ? 'var(--risk-high)' : 'var(--risk-low)';
                        return `
                        <div class="month-card">
                            <div class="month-card-title">${h.snapshot_date.substring(0, 7)}</div>
                            <div class="month-card-stat"><span>Balance Δ</span><span style="color:${balColor}">${(h.balance_change_30d || 0).toFixed(1)}%</span></div>
                            <div class="month-card-stat"><span>Txn Δ</span><span style="color:${txnColor}">${(h.transaction_change_30d || 0).toFixed(1)}%</span></div>
                            <div class="month-card-stat"><span>Complaints</span><span>${h.complaints_30d || 0}</span></div>
                            ${h.complaint_text ? `<div class="month-card-note" title="${h.complaint_text}">"${h.complaint_text}"</div>` : ''}
                        </div>`;
                    }).join('')}
                </div>
            </div>
        </div>
    `;

    // Render modal chart
    setTimeout(() => {
        const ctx = getCtx('modalHistChart');
        if (!ctx) return;
        destroyChart('modalHist');
        charts.modalHist = new Chart(ctx, {
            type: 'line',
            data: {
                labels: sortedHistory.map(h => h.snapshot_date.substring(0, 7)),
                datasets: [
                    { label: 'Balance Δ %', data: sortedHistory.map(h => h.balance_change_30d || 0), borderColor: '#6366f1', backgroundColor: 'rgba(99,102,241,0.08)', fill: true, tension: 0.3, pointRadius: 4 },
                    { label: 'Txn Δ %', data: sortedHistory.map(h => h.transaction_change_30d || 0), borderColor: '#f59e0b', borderDash: [5, 5], tension: 0.3, pointRadius: 4 },
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
    container.innerHTML = '<div class="modal-loading"><i class="fa-solid fa-spinner fa-spin"></i><p>Analyzing customer account...</p></div>';

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

    const reasonDisplay = p.primary_reason 
        ? `<span style="color:#f59e0b;font-weight:700">${p.primary_reason.replace(/_/g, ' ')}</span>`
        : `<span style="color:#10b981;font-weight:600"><i class="fa-solid fa-shield-check"></i> Low Risk (Healthy Account)</span>`;

    const actionDisplay = p.recommended_action 
        ? `<span style="color:#6366f1;font-weight:700">${p.recommended_action.replace(/_/g, ' ')}</span>`
        : `<span style="color:#6366f1;font-weight:700">MONITOR</span>`;

    const evidenceHtml = evidence.length 
        ? `<div class="evidence-section"><div class="evidence-section-title">Diagnostic Evidence</div><div class="evidence-pill-grid">${evidence.map(e => `<span class="evidence-pill">${e.evidence_text}</span>`).join('')}</div></div>`
        : `<div class="evidence-section"><div class="evidence-section-title">Account Diagnosis</div><div style="font-size:0.8rem;color:#10b981;display:flex;align-items:center;gap:6px"><i class="fa-solid fa-circle-check"></i> Behavioral activity is within healthy thresholds. Standard monitoring active.</div></div>`;

    const sortedHistory = [...history].sort((a, b) => a.snapshot_date.localeCompare(b.snapshot_date));

    container.innerHTML = `
        <div class="profile-hero">
            <div class="profile-hero-left">
                <div class="profile-avatar">${initials}</div>
                <div class="profile-info">
                    <h2>${p.customer_name} <span>(${p.customer_id})</span></h2>
                    <div class="profile-chips">
                        <span class="profile-chip"><i class="fa-solid fa-briefcase"></i> ${(p.customer_segment || '').toUpperCase()}</span>
                        <span class="profile-chip"><i class="fa-solid fa-clock"></i> ${p.tenure_months}mo tenure</span>
                        <span class="profile-chip"><i class="fa-solid fa-coins"></i> ₹${(p.customer_yearly_value || 0).toLocaleString()}</span>
                        <span class="profile-chip"><i class="fa-solid fa-cubes"></i> ${p.products_count || 0} Products</span>
                        ${p.cluster_label ? `<span class="profile-chip"><i class="fa-solid fa-object-group"></i> ${p.cluster_label}</span>` : ''}
                    </div>
                </div>
            </div>
            <div class="profile-hero-metrics">
                <div class="hero-metric-box">
                    <span class="badge ${badgeClass}" style="font-size:0.8rem;padding:4px 14px">${p.risk_level} Risk</span>
                    <div class="hero-churn-val">${(p.churn_probability || 0).toFixed(1)}%</div>
                    <span class="hero-score-sub">Risk Score: ${(p.risk_score || 0).toFixed(1)} / 100</span>
                </div>
            </div>
        </div>

        <div class="profile-grid-2">
            <div class="profile-card">
                <div class="profile-card-header">
                    <div class="profile-card-title"><i class="fa-solid fa-chart-line"></i>Key Risk Drivers (XGBoost SHAP)</div>
                </div>
                <div class="driver-list">
                    ${factors.map((f, idx) => `
                        <div class="driver-item">
                            <div class="driver-item-header">
                                <span class="driver-name"><span style="color:var(--blue);font-weight:700;margin-right:4px">#${idx+1}</span> ${f.display_label || f.factor_name.replace(/_/g, ' ')}</span>
                                <span class="driver-contrib">+${(f.contribution || 0).toFixed(3)}</span>
                            </div>
                            <div class="driver-desc">${f.factor_message}</div>
                        </div>
                    `).join('')}
                </div>
            </div>
            <div class="profile-card">
                <div class="profile-card-header">
                    <div class="profile-card-title"><i class="fa-solid fa-headset"></i>Retention Playbook (AI Strategy)</div>
                    <span class="urgency-tag urgency-${(p.urgency || 'low').toLowerCase()}">${p.urgency || 'LOW'} PRIORITY</span>
                </div>
                <div class="playbook-row">
                    <span class="playbook-label">Diagnosis:</span>
                    <span class="playbook-val">${reasonDisplay}</span>
                </div>
                ${p.secondary_reasons ? `<div class="playbook-row"><span class="playbook-label">Secondary:</span><span class="playbook-val" style="font-size:0.8rem;color:var(--text-secondary)">${p.secondary_reasons.replace(/,/g, ', ').replace(/_/g, ' ')}</span></div>` : ''}
                <div class="playbook-row">
                    <span class="playbook-label">Next Action:</span>
                    <span class="playbook-val">${actionDisplay}</span>
                </div>
                <div class="playbook-reasoning">"${p.reasoning_summary || 'Customer exhibits stable engagement metrics with low churn probability.'}"</div>
                ${evidenceHtml}
            </div>
        </div>

        ${cluster ? `
        <div class="profile-card" style="margin-top:24px">
            <div class="profile-card-header">
                <div class="profile-card-title"><i class="fa-solid fa-object-group"></i>Cohort Benchmark — ${cluster.cluster_label} (${cluster.customer_count.toLocaleString()} customers)</div>
            </div>
            <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(160px,1fr));gap:14px;margin-top:4px">
                <div class="cluster-stat"><div class="cluster-stat-val">${cluster.avg_churn_probability.toFixed(1)}%</div><div class="cluster-stat-label">Cohort Avg Churn</div></div>
                <div class="cluster-stat"><div class="cluster-stat-val">${cluster.avg_balance_change_30d.toFixed(1)}%</div><div class="cluster-stat-label">Cohort Avg Balance Δ</div></div>
                <div class="cluster-stat"><div class="cluster-stat-val">${cluster.avg_transaction_change_30d.toFixed(1)}%</div><div class="cluster-stat-label">Cohort Avg Txn Δ</div></div>
                <div class="cluster-stat"><div class="cluster-stat-val" style="font-size:0.95rem;font-weight:700">${cluster.dominant_primary_reason.replace(/_/g, ' ')}</div><div class="cluster-stat-label">Dominant Friction</div></div>
            </div>
        </div>` : ''}

        <div class="trajectory-panel">
            <div class="trajectory-header">
                <div class="profile-card-title"><i class="fa-solid fa-timeline"></i>6-Month Account Trajectory</div>
            </div>
            <div class="trajectory-chart-wrap"><canvas id="analysisHistChart"></canvas></div>
            <div class="monthly-strip">
                ${sortedHistory.map(h => {
                    const balColor = (h.balance_change_30d || 0) < 0 ? 'var(--risk-high)' : 'var(--risk-low)';
                    const txnColor = (h.transaction_change_30d || 0) < 0 ? 'var(--risk-high)' : 'var(--risk-low)';
                    return `
                    <div class="month-card">
                        <div class="month-card-title">${h.snapshot_date.substring(0, 7)}</div>
                        <div class="month-card-stat"><span>Balance Δ</span><span style="color:${balColor}">${(h.balance_change_30d || 0).toFixed(1)}%</span></div>
                        <div class="month-card-stat"><span>Txn Δ</span><span style="color:${txnColor}">${(h.transaction_change_30d || 0).toFixed(1)}%</span></div>
                        <div class="month-card-stat"><span>Complaints</span><span>${h.complaints_30d || 0}</span></div>
                        ${h.complaint_text ? `<div class="month-card-note" title="${h.complaint_text}">"${h.complaint_text}"</div>` : ''}
                    </div>`;
                }).join('')}
            </div>
        </div>
    `;

    // Render chart
    setTimeout(() => {
        const ctx = getCtx('analysisHistChart');
        if (!ctx) return;
        destroyChart('analysisHist');
        charts.analysisHist = new Chart(ctx, {
            type: 'line',
            data: {
                labels: sortedHistory.map(h => h.snapshot_date.substring(0, 7)),
                datasets: [
                    { label: 'Balance Δ %', data: sortedHistory.map(h => h.balance_change_30d || 0), borderColor: '#6366f1', backgroundColor: 'rgba(99,102,241,0.08)', fill: true, tension: 0.3, pointRadius: 4 },
                    { label: 'Txn Δ %', data: sortedHistory.map(h => h.transaction_change_30d || 0), borderColor: '#f59e0b', borderDash: [5, 5], tension: 0.3, pointRadius: 4 },
                    { label: 'Complaints', data: sortedHistory.map(h => h.complaints_30d || 0), borderColor: '#ef4444', tension: 0.3, yAxisID: 'y1', pointRadius: 4 },
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
function getCtx(id) {
    if (typeof Chart === 'undefined') {
        console.warn('Chart.js is not loaded yet.');
        return null;
    }
    const el = document.getElementById(id);
    return el ? el.getContext('2d') : null;
}
function destroyChart(key) { if (charts[key]) { try { charts[key].destroy(); } catch(e){} charts[key] = null; } }
