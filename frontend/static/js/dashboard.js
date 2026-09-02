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
    const TAB_URLS = {
        dashboard: '/',
        customers: '/customer-directory',
        analysis: '/individual-analysis',
        clusters: '/cluster-analysis',
        visualizations: '/visualizations',
    };
    const URL_TABS = {
        '/': 'dashboard',
        '/customer-directory': 'customers',
        '/individual-analysis': 'analysis',
        '/cluster-analysis': 'clusters',
        '/visualizations': 'visualizations',
    };

    function activateTab(tab, pushState = true) {
        document.querySelectorAll('.nav-item').forEach(b => b.classList.remove('active'));
        const navEl = document.getElementById(`nav-${tab}`);
        if (navEl) navEl.classList.add('active');
        document.querySelectorAll('.tab-panel').forEach(p => p.classList.remove('active'));
        const panel = document.getElementById(`tab-${tab}`);
        if (panel) panel.classList.add('active');
        document.getElementById('pageTitle').textContent = TAB_TITLES[tab] || '';
        if (pushState) {
            const url = TAB_URLS[tab] || '/';
            history.pushState({ tab }, '', url);
        }
        // Lazy load
        if (tab === 'clusters' && !state.clusterData) loadClusters();
        if (tab === 'visualizations') loadVisualizations();
    }

    // Detect initial URL
    const initTab = URL_TABS[window.location.pathname] || 'dashboard';
    activateTab(initTab, false);

    document.querySelectorAll('.nav-item').forEach(btn => {
        btn.addEventListener('click', (e) => {
            e.preventDefault();
            const tab = btn.dataset.tab;
            activateTab(tab);
        });
    });

    window.addEventListener('popstate', (e) => {
        const tab = (e.state && e.state.tab) || URL_TABS[window.location.pathname] || 'dashboard';
        activateTab(tab, false);
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

    // Monthly Trends Time Range Filter
    const trendTimeSelect = document.getElementById('trendTimeRange');
    if (trendTimeSelect) {
        trendTimeSelect.addEventListener('change', () => {
            if (state.dashData) {
                renderMonthlyTrends(state.dashData, parseInt(trendTimeSelect.value, 10) || 6);
            }
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

// Inline Chart.js plugin to draw count + Risk Tier labels OUTSIDE the doughnut/pie
// with thin leader lines connecting each label to its slice.
const doughnutSliceLabelsPlugin = {
    id: 'doughnutSliceLabels',
    afterDatasetsDraw(chart) {
        const { ctx } = chart;
        const dataset = chart.data.datasets[0];
        const meta = chart.getDatasetMeta(0);
        if (!meta || !meta.data || !meta.data.length) return;
        const total = dataset.data.reduce((a, b) => a + (Number(b) || 0), 0);
        if (!total) return;

        const sliceColors = dataset.backgroundColor || [];
        const tierNames = ['High Risk Customers', 'Medium Risk Customers', 'Low Risk Customers'];

        meta.data.forEach((element, index) => {
            const value = dataset.data[index];
            if (!value || value <= 0) return;

            const { startAngle, endAngle, outerRadius, x: cx, y: cy } = element;
            const angleSpan = endAngle - startAngle;
            if (angleSpan < 0.1) return; // skip tiny slices

            const midAngle = (startAngle + endAngle) / 2;

            // Point on the outer edge of the slice
            const edgeX = cx + Math.cos(midAngle) * outerRadius;
            const edgeY = cy + Math.sin(midAngle) * outerRadius;

            // Elbow point — pushed out from the edge
            const elbowLen = 12;
            const elbowX = cx + Math.cos(midAngle) * (outerRadius + elbowLen);
            const elbowY = cy + Math.sin(midAngle) * (outerRadius + elbowLen);

            // Horizontal tail — extends left or right from the elbow
            const tailLen = 14;
            const goRight = Math.cos(midAngle) >= 0;
            const tailX = elbowX + (goRight ? tailLen : -tailLen);
            const tailY = elbowY;

            // --- Draw the leader line ---
            ctx.save();
            ctx.beginPath();
            ctx.moveTo(edgeX, edgeY);
            ctx.lineTo(elbowX, elbowY);
            ctx.lineTo(tailX, tailY);
            ctx.strokeStyle = sliceColors[index] || '#94a3b8';
            ctx.lineWidth = 1.5;
            ctx.stroke();

            // Small anchor dot on the slice edge
            ctx.beginPath();
            ctx.arc(edgeX, edgeY, 2.5, 0, Math.PI * 2);
            ctx.fillStyle = sliceColors[index] || '#94a3b8';
            ctx.fill();

            // --- Draw the text label ---
            ctx.textBaseline = 'bottom';
            ctx.textAlign = goRight ? 'left' : 'right';
            const textX = tailX + (goRight ? 4 : -4);

            // Count (bold, crisp dark text)
            ctx.font = '700 13px "Plus Jakarta Sans", "Inter", sans-serif';
            ctx.fillStyle = '#0f172a';
            ctx.fillText(value.toLocaleString(), textX, tailY - 1);

            // Risk Tier label instead of % (e.g. High Risk, Medium Risk, Low Risk Customers)
            const tierLabel = tierNames[index] || (chart.data.labels && chart.data.labels[index]) || 'Customers';
            ctx.font = '700 10.5px "Plus Jakarta Sans", "Inter", sans-serif';
            ctx.fillStyle = sliceColors[index] || '#64748b';
            ctx.textBaseline = 'top';
            ctx.fillText(tierLabel, textX, tailY + 1);

            ctx.restore();
        });
    }
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
        try { renderAICoverage(data); } catch (e) { console.error('Error in renderAICoverage:', e); }
        try { renderRiskChart(data); } catch (e) { console.error('Error in renderRiskChart:', e); }
        try { renderTopFactors(data); } catch (e) { console.error('Error in renderTopFactors:', e); }
        try { renderActionsChart(data); } catch (e) { console.error('Error in renderActionsChart:', e); }
        try { renderReasonsChart(data); } catch (e) { console.error('Error in renderReasonsChart:', e); }
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
}

function renderAICoverage(d) {
    const coverage = d.model2_coverage || {};
    const totalAnalyzed = d.total_analyzed || 0;
    const totalCustomers = d.total_customers || 10000;

    setText('ai-total-analyzed', totalAnalyzed.toLocaleString());
    setText('ai-total-customers', totalCustomers.toLocaleString());

    const tiers = [
        { key: 'High', barId: 'ai-bar-high', statId: 'ai-stat-high' },
        { key: 'Medium', barId: 'ai-bar-med', statId: 'ai-stat-med' },
        { key: 'Low', barId: 'ai-bar-low', statId: 'ai-stat-low' },
    ];

    for (const tier of tiers) {
        const data = coverage[tier.key] || { total: 0, analyzed: 0 };
        const pct = data.total > 0 ? ((data.analyzed / data.total) * 100).toFixed(1) : '0.0';
        const bar = document.getElementById(tier.barId);
        const stat = document.getElementById(tier.statId);
        if (bar) bar.style.width = `${pct}%`;
        if (stat) {
            stat.innerHTML = `<strong>${data.analyzed.toLocaleString()}</strong> / ${data.total.toLocaleString()} <span class="ai-tier-pct">(${pct}%)</span>`;
        }
    }
}

function renderRiskChart(d) {
    const ctx = getCtx('riskDistChart');
    if (!ctx) return;
    destroyChart('riskDist');
    const high = d.risk_distribution.High || 0;
    const med = d.risk_distribution.Medium || 0;
    const low = d.risk_distribution.Low || 0;
    const total = high + med + low || 10000;

    // Update center overlay values
    const centerVal = document.getElementById('donutCenterVal');
    if (centerVal) centerVal.textContent = total.toLocaleString();

    charts.riskDist = new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: ['High Risk', 'Medium Risk', 'Healthy'],
            datasets: [{
                data: [high, med, low],
                backgroundColor: ['#ef4444', '#f59e0b', '#10b981'],
                hoverBackgroundColor: ['#dc2626', '#d97706', '#059669'],
                borderWidth: 3,
                borderColor: '#ffffff',
                borderRadius: 4,
                spacing: 3
            }]
        },
        plugins: [doughnutSliceLabelsPlugin],
        options: {
            responsive: true,
            maintainAspectRatio: false,
            layout: {
                padding: {
                    top: 14,
                    bottom: 14,
                    left: 80,
                    right: 80
                }
            },
            cutout: '68%',
            plugins: {
                legend: { display: false },
                tooltip: {
                    backgroundColor: 'rgba(15, 23, 42, 0.95)',
                    titleFont: { size: 12, weight: '700' },
                    bodyFont: { size: 12 },
                    padding: 10,
                    cornerRadius: 8,
                    callbacks: {
                        label: function(ctx) {
                            const val = ctx.raw || 0;
                            const p = total > 0 ? ((val / total) * 100).toFixed(1) : 0;
                            return ` ${ctx.label}: ${val.toLocaleString()} (${p}%)`;
                        }
                    }
                }
            }
        }
    });

    const legend = document.getElementById('riskLegend');
    if (legend) {
        legend.innerHTML = [
            legendRow('High Risk', high, total, 'dot-high', 'High', 'pill-high'),
            legendRow('Medium Risk', med, total, 'dot-med', 'Medium', 'pill-med'),
            legendRow('Healthy', low, total, 'dot-low', 'Low', 'pill-low'),
        ].join('');
    }
}

function legendRow(label, count, total, dotClass, riskVal, pillClass) {
    const percentage = pct(count, total);
    return `<div class="legend-row" onclick="setRiskFilter('${riskVal}')" title="Filter directory by ${label}">
        <div class="legend-left">
            <span class="legend-dot ${dotClass}"></span>
            <span class="legend-label-text">${label}</span>
        </div>
        <div class="legend-right">
            <span class="legend-count">${count.toLocaleString()}</span>
            <span class="legend-pct-pill ${pillClass}">${percentage}</span>
        </div>
    </div>`;
}

function renderTopFactors(d) {
    const factors = d.top_risk_factors || [];
    const total = d.total_customers || 10000;
    const ctx = getCtx('topFactorsChart');
    if (!ctx) return;
    
    destroyChart('topFactors');
    const top7 = factors.slice(0, 7);
    const colors = [
        '#ef4444',
        '#f43f5e',
        '#f97316',
        '#f59e0b',
        '#2563eb',
        '#0284c7',
        '#0891b2'
    ];

    charts.topFactors = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: top7.map(f => f.display_label.length > 40 ? f.display_label.substring(0, 38) + '…' : f.display_label),
            datasets: [{
                label: 'Affected Accounts',
                data: top7.map(f => f.frequency),
                backgroundColor: colors.slice(0, top7.length),
                hoverBackgroundColor: colors.slice(0, top7.length).map(c => c),
                borderRadius: 6,
                barThickness: 20
            }]
        },
        options: {
            indexAxis: 'y',
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: { display: false },
                tooltip: {
                    backgroundColor: 'rgba(15, 23, 42, 0.95)',
                    padding: 12,
                    cornerRadius: 8,
                    titleFont: { size: 12, weight: '700' },
                    bodyFont: { size: 11 },
                    callbacks: {
                        title: (items) => top7[items[0].dataIndex]?.display_label || '',
                        label: (ctx) => {
                            const f = top7[ctx.dataIndex];
                            const p = total > 0 ? ((f.frequency / total) * 100).toFixed(1) : 0;
                            return [
                                ` Affected Accounts: ${f.frequency.toLocaleString()} (${p}% of portfolio)`,
                                ` SHAP Churn Contribution: +${f.avg_contribution.toFixed(3)}`,
                                ` Signal: "${f.factor_message}"`
                            ];
                        }
                    }
                }
            },
            scales: {
                x: {
                    grid: { color: 'rgba(0, 0, 0, 0.04)' },
                    ticks: {
                        font: { size: 10, weight: '500' },
                        callback: val => val.toLocaleString()
                    },
                    title: { display: true, text: 'Affected Accounts Count', font: { size: 10, weight: '600' } }
                },
                y: {
                    grid: { display: false },
                    ticks: { font: { size: 11, weight: '600' } }
                }
            }
        }
    });
}

function renderActionsChart(d) {
    const ctx = getCtx('actionsChart');
    if (!ctx) return;
    destroyChart('actions');
    const actions = d.recommended_actions || {};
    // Sort strictly descending by count
    const sorted = Object.entries(actions)
        .sort((a, b) => b[1] - a[1])
        .slice(0, 6);
    
    const labels = sorted.map(([k]) => {
        const clean = k.replace(/_/g, ' ').toLowerCase();
        return clean.replace(/\b\w/g, l => l.toUpperCase());
    });
    const counts = sorted.map(([, v]) => v);
    const totalActs = Object.values(actions).reduce((a, b) => a + b, 0) || 1;

    charts.actions = new Chart(ctx, {
        type: 'bar',
        data: {
            labels,
            datasets: [{
                label: 'Interventions',
                data: counts,
                backgroundColor: '#2563eb',
                hoverBackgroundColor: '#1d4ed8',
                borderRadius: 5,
                barThickness: 18
            }]
        },
        options: {
            indexAxis: 'y',
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: { display: false },
                tooltip: {
                    backgroundColor: 'rgba(15, 23, 42, 0.95)',
                    padding: 10,
                    cornerRadius: 8,
                    callbacks: {
                        label: function(ctx) {
                            const val = ctx.raw || 0;
                            const p = ((val / totalActs) * 100).toFixed(1);
                            return ` Recommended: ${val.toLocaleString()} accounts (${p}%)`;
                        }
                    }
                }
            },
            scales: {
                x: {
                    grid: { color: 'rgba(0, 0, 0, 0.04)' },
                    ticks: { font: { size: 10 } }
                },
                y: {
                    grid: { display: false },
                    ticks: { font: { size: 10, weight: '600' } }
                }
            }
        }
    });
}

function renderReasonsChart(d) {
    const ctx = getCtx('reasonsChart');
    if (!ctx) return;
    destroyChart('reasons');
    const reasons = d.primary_reasons || {};
    // Sort strictly descending by count
    const sorted = Object.entries(reasons)
        .sort((a, b) => b[1] - a[1])
        .slice(0, 6);

    const labels = sorted.map(([k]) => {
        const clean = k.replace(/_/g, ' ').toLowerCase();
        return clean.replace(/\b\w/g, l => l.toUpperCase());
    });
    const counts = sorted.map(([, v]) => v);
    const totalReasons = Object.values(reasons).reduce((a, b) => a + b, 0) || 1;

    charts.reasons = new Chart(ctx, {
        type: 'bar',
        data: {
            labels,
            datasets: [{
                label: 'Pain Points',
                data: counts,
                backgroundColor: 'rgba(245, 158, 11, 0.85)',
                hoverBackgroundColor: '#d97706',
                borderRadius: 5,
                barThickness: 18
            }]
        },
        options: {
            indexAxis: 'y',
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: { display: false },
                tooltip: {
                    backgroundColor: 'rgba(15, 23, 42, 0.95)',
                    padding: 10,
                    cornerRadius: 8,
                    callbacks: {
                        label: function(ctx) {
                            const val = ctx.raw || 0;
                            const p = ((val / totalReasons) * 100).toFixed(1);
                            return ` Diagnosed: ${val.toLocaleString()} accounts (${p}%)`;
                        }
                    }
                }
            },
            scales: {
                x: {
                    grid: { color: 'rgba(0, 0, 0, 0.04)' },
                    ticks: { font: { size: 10 } }
                },
                y: {
                    grid: { display: false },
                    ticks: { font: { size: 10, weight: '600' } }
                }
            }
        }
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

function renderMonthlyTrends(d, limitMonths = 6) {
    const rawTrends = d.monthly_trends || [];
    if (!rawTrends.length) return;

    const trends = rawTrends.slice(-limitMonths);
    if (!trends.length) return;

    const monthNames = { '01': 'Jan', '02': 'Feb', '03': 'Mar', '04': 'Apr', '05': 'May', '06': 'Jun', '07': 'Jul', '08': 'Aug', '09': 'Sep', '10': 'Oct', '11': 'Nov', '12': 'Dec' };
    const monthLabels = trends.map(t => {
        const parts = t.month.split('-');
        const m = monthNames[parts[1]] || parts[1];
        const y = parts[0] || '2026';
        return `${m} ${y}`;
    });

    const balData = trends.map(t => +(t.balance_delta || 0).toFixed(1));
    const txnData = trends.map(t => +(t.txn_delta || 0).toFixed(1));
    const extData = trends.map(t => +(t.outflow_delta || 0).toFixed(1));

    const firstMonth = monthLabels[0] ? monthLabels[0].split(' ')[0] : 'Jan';
    const lastMonth = monthLabels[monthLabels.length - 1] || 'Jun 2026';
    const dateRangeStr = `from ${firstMonth} to ${lastMonth}`;

    const latestBal = balData[balData.length - 1];
    const latestTxn = txnData[txnData.length - 1];
    const firstExt = extData[0];
    const latestExt = extData[extData.length - 1];
    const netOutflowDelta = +(latestExt - firstExt).toFixed(1);

    // Update Top Metric Cards text
    setText('trend-bal-val', `${latestBal > 0 ? '+' : ''}${latestBal.toFixed(1)}% ${latestBal >= 0 ? '↗' : '↘'}`);
    setText('trend-bal-sub', dateRangeStr);
    setText('trend-txn-val', `${latestTxn > 0 ? '+' : ''}${latestTxn.toFixed(1)}% ${latestTxn >= 0 ? '↗' : '↘'}`);
    setText('trend-txn-sub', dateRangeStr);
    setText('trend-ext-val', `${netOutflowDelta > 0 ? '+' : ''}${netOutflowDelta.toFixed(1)}% ${netOutflowDelta <= 0 ? '↘' : '↗'}`);
    setText('trend-ext-sub', dateRangeStr);

    // Update Bottom Summary Bullets
    setText('tb-bal-text', `Balance ${latestBal >= 0 ? 'improved by +' : 'declined by '}${latestBal.toFixed(1)}%`);
    setText('tb-bal-date', dateRangeStr);
    setText('tb-txn-text', `Transactions ${latestTxn >= 0 ? 'increased by +' : 'decreased by '}${latestTxn.toFixed(1)}%`);
    setText('tb-txn-date', dateRangeStr);
    setText('tb-ext-text', `Outflows ${netOutflowDelta <= 0 ? 'decreased by ' : 'increased by +'}${netOutflowDelta.toFixed(1)}%`);
    setText('tb-ext-date', dateRangeStr);

    if (latestBal > 0 && netOutflowDelta < 0) {
        setText('trend-insight-text', 'Your balance is growing while outflows are reducing — a healthy trend!');
    } else if (latestBal < 0 || netOutflowDelta > 0) {
        setText('trend-insight-text', 'Outflows and balance contractions require targeted retention intervention.');
    } else {
        setText('trend-insight-text', 'Account activity remains stable across the 6-month observation window.');
    }

    // Render Sparklines
    const balCtx = getCtx('sparkBalance');
    if (balCtx) {
        destroyChart('sparkBalance');
        charts.sparkBalance = new Chart(balCtx, {
            type: 'line',
            data: {
                labels: monthLabels,
                datasets: [{
                    data: balData,
                    borderColor: '#2563eb',
                    borderWidth: 2,
                    backgroundColor: 'rgba(37, 99, 235, 0.08)',
                    fill: true,
                    tension: 0.4,
                    pointRadius: 0
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: { legend: { display: false }, tooltip: { enabled: false } },
                scales: { x: { display: false }, y: { display: false } }
            }
        });
    }

    const txnCtx = getCtx('sparkTransaction');
    if (txnCtx) {
        destroyChart('sparkTransaction');
        charts.sparkTransaction = new Chart(txnCtx, {
            type: 'line',
            data: {
                labels: monthLabels,
                datasets: [{
                    data: txnData,
                    borderColor: '#f59e0b',
                    borderWidth: 2,
                    backgroundColor: 'rgba(245, 158, 11, 0.08)',
                    fill: true,
                    tension: 0.4,
                    pointRadius: 0
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: { legend: { display: false }, tooltip: { enabled: false } },
                scales: { x: { display: false }, y: { display: false } }
            }
        });
    }

    const extCtx = getCtx('sparkOutflow');
    if (extCtx) {
        destroyChart('sparkOutflow');
        charts.sparkOutflow = new Chart(extCtx, {
            type: 'line',
            data: {
                labels: monthLabels,
                datasets: [{
                    data: extData,
                    borderColor: '#ef4444',
                    borderWidth: 2,
                    backgroundColor: 'rgba(239, 68, 68, 0.08)',
                    fill: true,
                    tension: 0.4,
                    pointRadius: 0
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: { legend: { display: false }, tooltip: { enabled: false } },
                scales: { x: { display: false }, y: { display: false } }
            }
        });
    }

    // Render Main Mixed Chart
    const ctx = getCtx('monthlyTrendsChart');
    if (!ctx) return;
    destroyChart('monthlyTrends');

    charts.monthlyTrends = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: monthLabels,
            datasets: [
                {
                    type: 'bar',
                    label: 'Balance Change (%)',
                    data: balData,
                    backgroundColor: '#2563eb',
                    hoverBackgroundColor: '#1d4ed8',
                    borderRadius: 4,
                    barThickness: 28,
                    order: 3
                },
                {
                    type: 'line',
                    label: 'Transaction Change (%)',
                    data: txnData,
                    borderColor: '#f59e0b',
                    backgroundColor: '#f59e0b',
                    borderWidth: 2.2,
                    pointRadius: 4.5,
                    pointHoverRadius: 6.5,
                    pointBackgroundColor: '#f59e0b',
                    tension: 0.35,
                    order: 2
                },
                {
                    type: 'line',
                    label: 'Outflow Change (%)',
                    data: extData,
                    borderColor: '#ef4444',
                    backgroundColor: '#ef4444',
                    borderWidth: 2.2,
                    pointRadius: 4.5,
                    pointHoverRadius: 6.5,
                    pointBackgroundColor: '#ef4444',
                    tension: 0.35,
                    order: 1
                }
            ]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            interaction: {
                mode: 'index',
                intersect: false
            },
            plugins: {
                legend: { display: false },
                tooltip: {
                    backgroundColor: 'rgba(15, 23, 42, 0.95)',
                    padding: 12,
                    cornerRadius: 8,
                    titleFont: { size: 12, weight: '700' },
                    bodyFont: { size: 11 },
                    callbacks: {
                        label: function(ctx) {
                            const val = ctx.raw !== undefined ? ctx.raw : 0;
                            const sign = val > 0 ? '+' : '';
                            return ` ${ctx.dataset.label}: ${sign}${val.toFixed(1)}%`;
                        }
                    }
                }
            },
            scales: {
                x: {
                    grid: { display: false },
                    ticks: {
                        font: { size: 11, weight: '600' },
                        color: '#475569'
                    }
                },
                y: {
                    title: {
                        display: true,
                        text: 'Change (%)',
                        font: { size: 11, weight: '600' },
                        color: '#64748b'
                    },
                    grid: {
                        color: 'rgba(226, 232, 240, 0.6)',
                        drawBorder: false
                    },
                    ticks: {
                        font: { size: 10 },
                        callback: val => (val > 0 ? `+${val}%` : `${val}%`)
                    },
                    suggestedMin: -2,
                    suggestedMax: 6
                }
            }
        }
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
        tbody.innerHTML = `<tr><td colspan="8" class="dir-empty"><i class="fa-solid fa-folder-open"></i><br>No accounts match the current filters.</td></tr>`;
        return;
    }

    tbody.innerHTML = customers.map(c => {
        const badgeClass = c.risk_level === 'High' ? 'badge-high' : c.risk_level === 'Medium' ? 'badge-med' : 'badge-low';
        const probColor = c.risk_level === 'High' ? '#ef4444' : c.risk_level === 'Medium' ? '#b45309' : '#16a34a';
        const scoreVal = Math.round(c.risk_score || 0);
        const frictionRaw = c.primary_reason ? c.primary_reason.replace(/_/g, ' ') : null;
        const frictionLabel = frictionRaw
            ? frictionRaw.replace(/\b\w/g, l => l.toUpperCase())
            : `<span class="dir-none">Stable</span>`;
        const actionRaw = c.recommended_action ? c.recommended_action.replace(/_/g, ' ') : 'Monitor';
        const actionLabel = actionRaw.replace(/\b\w/g, l => l.toUpperCase());
        const urgency = c.urgency || '';
        const urgClass = urgency === 'HIGH' ? 'urgency-high' : urgency === 'MEDIUM' ? 'urgency-med' : 'urgency-low';
        const urgLabel = urgency ? `<span class="urgency-pill ${urgClass}">${urgency.charAt(0) + urgency.slice(1).toLowerCase()}</span>` : `<span class="dir-none">—</span>`;
        const seg = c.customer_segment ? (c.customer_segment.charAt(0).toUpperCase() + c.customer_segment.slice(1).toLowerCase()) : '—';

        return `<tr onclick="openCustomerModal('${c.customer_id}')" class="dir-row">
            <td>
                <div class="acct-cell">
                    <div class="acct-info">
                        <div class="acct-name">${c.customer_name}</div>
                        <div class="acct-id">${c.customer_id}</div>
                    </div>
                </div>
            </td>
            <td><span class="seg-tag">${seg}</span></td>
            <td><span class="badge ${badgeClass}">${c.risk_level}</span></td>
            <td>
                <div class="prob-cell" title="Risk Score: ${scoreVal}/100 (Model Churn Prob: ${(c.churn_probability || 0).toFixed(1)}%)">
                    <div class="prob-track"><div class="prob-fill" style="width:${Math.min(100, Math.max(4, scoreVal))}%;background:${probColor}"></div></div>
                    <strong style="color:${probColor}">${scoreVal}<span style="font-size:0.68rem;color:var(--text-muted);font-weight:600">/100</span></strong>
                </div>
            </td>
            <td class="friction-cell">${frictionLabel}</td>
            <td class="action-cell">${actionLabel}</td>
            <td>${urgLabel}</td>
            <td class="text-right">
                <button class="btn-profile" onclick="event.stopPropagation();openCustomerModal('${c.customer_id}')">
                    <i class="fa-solid fa-arrow-up-right-from-square"></i> View
                </button>
            </td>
        </tr>`;
    }).join('');
}

function renderPagination() {
    const totalPages = Math.max(1, Math.ceil(state.totalRecords / state.pageSize));
    setText('pageNum', state.page);
    setText('totalPages', totalPages);
    const s = state.totalRecords === 0 ? 0 : (state.page - 1) * state.pageSize + 1;
    const e = Math.min(state.totalRecords, state.page * state.pageSize);
    setText('showCount', s.toLocaleString());
    setText('showCountEnd', e.toLocaleString());
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
        ? `<span style="color:#2563eb;font-weight:700">${p.recommended_action.replace(/_/g, ' ')}</span>`
        : `<span style="color:#2563eb;font-weight:700">MONITOR</span>`;

    const evidenceHtml = evidence.length 
        ? `<div class="evidence-section"><div class="evidence-section-title">Diagnostic Evidence</div><div class="evidence-pill-grid">${evidence.map(e => `<span class="evidence-pill">${e.evidence_text}</span>`).join('')}</div></div>`
        : `<div class="evidence-section"><div class="evidence-section-title">Account Diagnosis</div><div style="font-size:0.8rem;color:#10b981;display:flex;align-items:center;gap:6px"><i class="fa-solid fa-circle-check"></i> Behavioral activity is within healthy thresholds. Standard monitoring active.</div></div>`;

    const sortedHistory = [...history].sort((a, b) => a.snapshot_date.localeCompare(b.snapshot_date));
    const complaints = (data.complaints && data.complaints.length > 0)
        ? data.complaints
        : (history.filter(h => h.complaint_text && h.complaint_text.trim() !== ''));

    let complaintsHtml = '';
    if (complaints.length > 0) {
        complaintsHtml = `
            <div class="profile-card complaint-card" style="margin-top:20px;">
                <div class="profile-card-header">
                    <div class="profile-card-title"><i class="fa-solid fa-triangle-exclamation text-rose"></i>Customer Complaints</div>
                    <span class="badge badge-high" style="font-size:0.75rem;padding:3px 10px;">${complaints.length} Logged</span>
                </div>
                <div class="complaint-list">
                    ${complaints.map(c => `
                        <div class="complaint-entry">
                            <div class="complaint-entry-header">
                                <span class="complaint-date"><i class="fa-regular fa-calendar"></i> Snapshot Date: ${c.snapshot_date}</span>
                                ${(c.unresolved_complaints > 0 || c.complaints_30d > 0)
                                    ? '<span class="complaint-tag-unresolved"><i class="fa-solid fa-circle-exclamation"></i> Unresolved Complaint</span>'
                                    : '<span class="complaint-tag-note"><i class="fa-solid fa-comment"></i> Customer Feedback</span>'}
                            </div>
                            <div class="complaint-quote">"${c.complaint_text}"</div>
                        </div>
                    `).join('')}
                </div>
            </div>
        `;
    }

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
                    <div class="hero-churn-val">${Math.round(p.risk_score || 0)}<span style="font-size:0.95rem;font-weight:600;opacity:0.8">/100</span></div>
                    <span class="hero-score-sub">Model Churn Prob: ${(p.churn_probability || 0).toFixed(1)}%</span>
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

            ${complaintsHtml}

            <div class="trajectory-panel" style="margin-top:20px;">
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
                    { label: 'Balance Δ %', data: sortedHistory.map(h => h.balance_change_30d || 0), borderColor: '#2563eb', backgroundColor: 'rgba(37, 99, 235, 0.08)', fill: true, tension: 0.3, pointRadius: 4 },
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
        ? `<span style="color:#2563eb;font-weight:700">${p.recommended_action.replace(/_/g, ' ')}</span>`
        : `<span style="color:#2563eb;font-weight:700">MONITOR</span>`;

    const evidenceHtml = evidence.length 
        ? `<div class="evidence-section"><div class="evidence-section-title">Diagnostic Evidence</div><div class="evidence-pill-grid">${evidence.map(e => `<span class="evidence-pill">${e.evidence_text}</span>`).join('')}</div></div>`
        : `<div class="evidence-section"><div class="evidence-section-title">Account Diagnosis</div><div style="font-size:0.8rem;color:#10b981;display:flex;align-items:center;gap:6px"><i class="fa-solid fa-circle-check"></i> Behavioral activity is within healthy thresholds. Standard monitoring active.</div></div>`;

    const sortedHistory = [...history].sort((a, b) => a.snapshot_date.localeCompare(b.snapshot_date));
    const complaints = (data.complaints && data.complaints.length > 0)
        ? data.complaints
        : (history.filter(h => h.complaint_text && h.complaint_text.trim() !== ''));

    let complaintsHtml = '';
    if (complaints.length > 0) {
        complaintsHtml = `
            <div class="profile-card complaint-card" style="margin-top:20px;">
                <div class="profile-card-header">
                    <div class="profile-card-title"><i class="fa-solid fa-triangle-exclamation text-rose"></i>Customer Complaints</div>
                    <span class="badge badge-high" style="font-size:0.75rem;padding:3px 10px;">${complaints.length} Logged</span>
                </div>
                <div class="complaint-list">
                    ${complaints.map(c => `
                        <div class="complaint-entry">
                            <div class="complaint-entry-header">
                                <span class="complaint-date"><i class="fa-regular fa-calendar"></i> Snapshot Date: ${c.snapshot_date}</span>
                                ${(c.unresolved_complaints > 0 || c.complaints_30d > 0)
                                    ? '<span class="complaint-tag-unresolved"><i class="fa-solid fa-circle-exclamation"></i> Unresolved Complaint</span>'
                                    : '<span class="complaint-tag-note"><i class="fa-solid fa-comment"></i> Customer Feedback</span>'}
                            </div>
                            <div class="complaint-quote">"${c.complaint_text}"</div>
                        </div>
                    `).join('')}
                </div>
            </div>
        `;
    }

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
                    <div class="hero-churn-val">${Math.round(p.risk_score || 0)}<span style="font-size:0.95rem;font-weight:600;opacity:0.8">/100</span></div>
                    <span class="hero-score-sub">Model Churn Prob: ${(p.churn_probability || 0).toFixed(1)}%</span>
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

        ${complaintsHtml}

        ${cluster ? `
        <div class="profile-card" style="margin-top:20px">
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

        <div class="trajectory-panel" style="margin-top:20px;">
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
                    { label: 'Balance Δ %', data: sortedHistory.map(h => h.balance_change_30d || 0), borderColor: '#2563eb', backgroundColor: 'rgba(37, 99, 235, 0.08)', fill: true, tension: 0.3, pointRadius: 4 },
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
// Cluster Analysis Tab — Executive AI Cohort Studio
// ---------------------------------------------------------------------------

const CLUSTER_METADATA = {
    0: {
        icon: 'fa-rocket',
        color: '#10b981',
        bg: '#f0fdf4',
        border: '#bbf7d0',
        title: 'High Engagement & Growing',
        riskTier: 'Low Risk',
        badgeClass: 'badge-low',
        traits: ['+26.6% Balance Growth', '+24.0% Txn Surge', 'Low Outflow (-25.6%)', '0.4 Complaints/Mo'],
        story: 'Expanding, loyal accounts with rapid balance accumulation and digital velocity. Represents the highest-value, lowest-churn pillar of the institution.',
        strategy: 'Nurture with wealth advisory, premium credit tier upgrades, and priority relationship banking.',
    },
    1: {
        icon: 'fa-triangle-exclamation',
        color: '#ef4444',
        bg: '#fef2f2',
        border: '#fecaca',
        title: 'Severe Capital Outflow & Attrition',
        riskTier: 'High Risk',
        badgeClass: 'badge-high',
        traits: ['-42.2% Balance Drain', '+65.7% Outflow Flight', '-39.0% Txn Drop', '19.3 Days Inactivity'],
        story: 'Critical flight risk accounts experiencing aggressive liquidity depletion and external fund transfers to competitors. Immediate intervention required.',
        strategy: 'Proactive RM outreach, deposit retention rate matching, and fee waiver compensation.',
    },
    2: {
        icon: 'fa-shield-halved',
        color: '#2563eb',
        bg: '#eff6ff',
        border: '#bfdbfe',
        title: 'Stable & Moderate Activity',
        riskTier: 'Low Risk',
        badgeClass: 'badge-low',
        traits: ['-2.1% Stable Balances', 'Normal Transaction Usage', 'Low Inactivity (7.7d)', '0.5 Complaints/Mo'],
        story: 'Core banking population representing 47.4% of total accounts. Low volatility, consistent monthly salary/vendor flows, and healthy baseline stability.',
        strategy: 'Automated engagement campaigns, mobile app feature discovery, and recurring deposit cross-selling.',
    },
    3: {
        icon: 'fa-headset',
        color: '#ea580c',
        bg: '#fff7ed',
        border: '#fed7aa',
        title: 'High Friction & Escalated Complaints',
        riskTier: 'High Risk',
        badgeClass: 'badge-high',
        traits: ['5.1 Complaints/Month', '5.2 Failed Transactions', '4.3 Unresolved Issues', 'Service Dissatisfaction'],
        story: 'Accounts experiencing acute operational and technical friction, leading to severe frustration despite moderate baseline financial balances.',
        strategy: 'Immediate Service Recovery desk escalation, technical root-cause resolution, and apology waiver vouchers.',
    },
    4: {
        icon: 'fa-credit-card',
        color: '#d97706',
        bg: '#fffbeb',
        border: '#fde68a',
        title: 'Loan Default & Financial Strain',
        riskTier: 'Medium Risk',
        badgeClass: 'badge-med',
        traits: ['1.0 EMI Bounces/Month', '-14.6% Card Spend', '-14.7% Balance Drop', '11.6 Days Inactivity'],
        story: 'Borrowers exhibiting signs of household financial distress with repeated EMI bounced payments and shrinking discretionary card spend.',
        strategy: 'Debt restructuring, flexible repayment schedules, and credit counseling assistance.',
    },
};

let activeClusterId = 1; // Default to most critical cluster

async function loadClusters() {
    try {
        const res = await fetch('/api/clusters');
        const data = await res.json();
        state.clusterData = data.clusters || [];
        renderClusterOverview(state.clusterData);
        renderClusterRadar(state.clusterData);
        renderClusterRiskBar(state.clusterData);
        drillCluster(activeClusterId);
    } catch (err) { console.error('Cluster load error:', err); }
}

function renderClusterOverview(clusters) {
    const grid = document.getElementById('clusterOverview');
    if (!grid) return;

    grid.innerHTML = clusters.map(c => {
        const meta = CLUSTER_METADATA[c.cluster_id] || {
            icon: 'fa-users', color: '#2563eb', bg: '#eff6ff', border: '#bfdbfe',
            title: c.cluster_label, riskTier: 'Medium Risk', badgeClass: 'badge-med',
            traits: [], story: '', strategy: ''
        };
        const total = c.customer_count;
        const portPct = ((total / 10000) * 100).toFixed(1);
        const avgScore = Math.round(c.avg_risk_score || 0);
        const isActive = c.cluster_id === activeClusterId;

        return `
        <div class="cluster-card ${isActive ? 'cluster-card-active' : ''}" 
             id="cluster-card-${c.cluster_id}"
             style="--cluster-color:${meta.color}" 
             onclick="drillCluster(${c.cluster_id}, true)">
            <div class="cluster-card-top">
                <div class="cluster-persona-tag">
                    <div class="cluster-icon-box" style="background:${meta.bg};color:${meta.color};border:1px solid ${meta.border}">
                        <i class="fa-solid ${meta.icon}"></i>
                    </div>
                    <div>
                        <div class="cluster-card-label">${c.cluster_label}</div>
                        <div class="cluster-card-id-pill">Cohort ${c.cluster_id}</div>
                    </div>
                </div>
                <span class="cluster-pop-pill">${total.toLocaleString()} (${portPct}%)</span>
            </div>

            <div class="cluster-card-metrics">
                <div class="cluster-mini-metric">
                    <div class="cm-val" style="color:${meta.color}">${avgScore}<span style="font-size:0.65rem;color:var(--text-muted)">/100</span></div>
                    <div class="cm-label">Avg Risk Score</div>
                </div>
                <div class="cluster-mini-metric">
                    <div class="cm-val" style="color:${c.avg_balance_change_30d < 0 ? '#ef4444' : '#10b981'}">
                        ${c.avg_balance_change_30d > 0 ? '+' : ''}${c.avg_balance_change_30d.toFixed(1)}%
                    </div>
                    <div class="cm-label">Balance Δ</div>
                </div>
            </div>

            <div class="cluster-traits-wrap">
                ${meta.traits.slice(0, 3).map(t => `<span class="cluster-trait-chip">${t}</span>`).join('')}
            </div>

            <div class="cluster-card-footer">
                <span class="badge ${meta.badgeClass}" style="font-size:0.7rem;padding:2px 8px">${meta.riskTier}</span>
                <button class="btn-explore-cohort" onclick="event.stopPropagation();drillCluster(${c.cluster_id}, true)">
                    Explore Cohort <i class="fa-solid fa-arrow-right"></i>
                </button>
            </div>
        </div>`;
    }).join('');
}

function renderClusterRadar(clusters) {
    const ctx = getCtx('clusterRadarChart');
    if (!ctx) return;
    destroyChart('clusterRadar');

    const dimensions = ['Balance Trend', 'Transaction Activity', 'Digital Engagement', 'Capital Retention', 'Service Stability', 'Credit Repayment'];

    const datasets = clusters.map(c => {
        const meta = CLUSTER_METADATA[c.cluster_id] || { color: '#2563eb' };
        
        const dBalance = Math.min(100, Math.max(10, 50 + (c.avg_balance_change_30d || 0)));
        const dTxn = Math.min(100, Math.max(10, 50 + (c.avg_transaction_change_30d || 0)));
        const dApp = Math.min(100, Math.max(10, 50 + (c.avg_app_login_change_30d || 0)));
        const dRetention = Math.min(100, Math.max(10, 100 - (c.avg_external_transfer_change_30d || 0)));
        const dService = Math.min(100, Math.max(10, 100 - (c.avg_complaints_30d || 0) * 16));
        const dCredit = Math.min(100, Math.max(10, 100 - (c.avg_emi_bounce_30d || 0) * 80));

        return {
            label: c.cluster_label,
            data: [dBalance, dTxn, dApp, dRetention, dService, dCredit],
            borderColor: meta.color,
            backgroundColor: meta.color + '20',
            borderWidth: 2,
            pointBackgroundColor: meta.color,
            pointRadius: 3.5,
            pointHoverRadius: 6
        };
    });

    charts.clusterRadar = new Chart(ctx, {
        type: 'radar',
        data: { labels: dimensions, datasets },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    position: 'bottom',
                    labels: { boxWidth: 10, padding: 10, font: { size: 10.5, weight: '600' } }
                },
                tooltip: {
                    backgroundColor: 'rgba(15, 23, 42, 0.95)',
                    padding: 10,
                    cornerRadius: 8
                }
            },
            scales: {
                r: {
                    beginAtZero: true,
                    max: 100,
                    ticks: { display: false },
                    grid: { color: 'rgba(0,0,0,0.06)' },
                    pointLabels: { font: { size: 10, weight: '600' }, color: '#475569' }
                }
            }
        }
    });
}

function renderClusterRiskBar(clusters) {
    const ctx = getCtx('clusterRiskBarChart');
    if (!ctx) return;
    destroyChart('clusterRiskBar');

    const labels = clusters.map(c => `Cohort ${c.cluster_id}`);
    const highCounts = clusters.map(c => c.high_risk_count || 0);
    const medCounts = clusters.map(c => c.medium_risk_count || 0);
    const lowCounts = clusters.map(c => c.low_risk_count || 0);

    charts.clusterRiskBar = new Chart(ctx, {
        type: 'bar',
        data: {
            labels,
            datasets: [
                {
                    label: 'High Risk',
                    data: highCounts,
                    backgroundColor: '#ef4444',
                    borderRadius: 3
                },
                {
                    label: 'Medium Risk',
                    data: medCounts,
                    backgroundColor: '#f59e0b',
                    borderRadius: 3
                },
                {
                    label: 'Healthy',
                    data: lowCounts,
                    backgroundColor: '#10b981',
                    borderRadius: 3
                }
            ]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    position: 'bottom',
                    labels: { boxWidth: 10, padding: 10, font: { size: 10.5, weight: '600' } }
                },
                tooltip: {
                    backgroundColor: 'rgba(15, 23, 42, 0.95)',
                    padding: 12,
                    cornerRadius: 8,
                    callbacks: {
                        title: (items) => {
                            const c = clusters[items[0].dataIndex];
                            return `${c.cluster_label} (Cohort ${c.cluster_id})`;
                        },
                        label: (ctx) => {
                            const val = ctx.raw || 0;
                            const c = clusters[ctx.dataIndex];
                            const p = c.customer_count > 0 ? ((val / c.customer_count) * 100).toFixed(1) : 0;
                            return ` ${ctx.dataset.label}: ${val.toLocaleString()} accounts (${p}%)`;
                        }
                    }
                }
            },
            scales: {
                x: {
                    stacked: true,
                    grid: { display: false },
                    ticks: { font: { size: 11, weight: '600' } }
                },
                y: {
                    stacked: true,
                    grid: { color: 'rgba(0,0,0,0.05)' },
                    ticks: { callback: v => v.toLocaleString() },
                    title: { display: true, text: 'Audited Accounts', font: { size: 10, weight: '600' } }
                }
            }
        }
    });
}

window.drillCluster = async function(clusterId, shouldScroll = false) {
    activeClusterId = clusterId;
    
    // Update active highlight on cards
    document.querySelectorAll('.cluster-card').forEach(card => card.classList.remove('cluster-card-active'));
    const activeCard = document.getElementById(`cluster-card-${clusterId}`);
    if (activeCard) activeCard.classList.add('cluster-card-active');

    try {
        const res = await fetch(`/api/cluster/${clusterId}`);
        const data = await res.json();
        const profile = data.profile;
        const customers = data.customers || [];
        const reasons = data.reason_distribution || {};
        const meta = CLUSTER_METADATA[clusterId] || {
            icon: 'fa-users', color: '#2563eb', bg: '#eff6ff', border: '#bfdbfe',
            title: profile.cluster_label, riskTier: 'Medium Risk', badgeClass: 'badge-med',
            traits: [], story: '', strategy: ''
        };

        setText('clusterDrillTitle', `Cohort ${clusterId}: ${profile.cluster_label}`);
        setText('clusterDrillDesc', `${profile.customer_count.toLocaleString()} Audited Accounts • ${((profile.customer_count/10000)*100).toFixed(1)}% of Portfolio • Avg Risk Score: ${Math.round(profile.avg_risk_score)}/100`);

        // Render Persona Story & KPI Tiles
        const narrativeBox = document.getElementById('cohortNarrative');
        if (narrativeBox) {
            narrativeBox.innerHTML = `
                <div class="cohort-story-top">
                    <div class="cohort-story-main">
                        <div class="cohort-story-icon" style="background:${meta.bg};color:${meta.color};border:1px solid ${meta.border}">
                            <i class="fa-solid ${meta.icon}"></i>
                        </div>
                        <div>
                            <div class="cohort-story-title">${profile.cluster_label}</div>
                            <p class="cohort-story-desc">${meta.story}</p>
                        </div>
                    </div>
                    <div class="cohort-strategy-box">
                        <div class="cohort-strategy-label"><i class="fa-solid fa-lightbulb"></i> Recommended Strategy</div>
                        <div class="cohort-strategy-text">${meta.strategy}</div>
                    </div>
                </div>

                <div class="cohort-kpi-row">
                    <div class="cohort-kpi-tile">
                        <div class="cohort-kpi-tile-val" style="color:${profile.avg_balance_change_30d < 0 ? '#ef4444' : '#10b981'}">
                            ${profile.avg_balance_change_30d > 0 ? '+' : ''}${profile.avg_balance_change_30d.toFixed(1)}%
                        </div>
                        <div class="cohort-kpi-tile-label">Avg 30D Balance Δ</div>
                    </div>
                    <div class="cohort-kpi-tile">
                        <div class="cohort-kpi-tile-val" style="color:${profile.avg_transaction_change_30d < 0 ? '#ef4444' : '#10b981'}">
                            ${profile.avg_transaction_change_30d > 0 ? '+' : ''}${profile.avg_transaction_change_30d.toFixed(1)}%
                        </div>
                        <div class="cohort-kpi-tile-label">Avg 30D Txn Δ</div>
                    </div>
                    <div class="cohort-kpi-tile">
                        <div class="cohort-kpi-tile-val" style="color:${profile.avg_external_transfer_change_30d > 20 ? '#ef4444' : '#2563eb'}">
                            ${profile.avg_external_transfer_change_30d > 0 ? '+' : ''}${profile.avg_external_transfer_change_30d.toFixed(1)}%
                        </div>
                        <div class="cohort-kpi-tile-label">Avg Outflow Δ</div>
                    </div>
                    <div class="cohort-kpi-tile">
                        <div class="cohort-kpi-tile-val" style="color:${profile.avg_complaints_30d > 2 ? '#ef4444' : '#10b981'}">
                            ${profile.avg_complaints_30d.toFixed(1)} <span style="font-size:0.75rem;font-weight:500;color:var(--text-muted)">/mo</span>
                        </div>
                        <div class="cohort-kpi-tile-label">Avg Complaints</div>
                    </div>
                </div>
            `;
        }

        // Reason Chart
        const ctx = getCtx('clusterReasonChart');
        if (ctx) {
            destroyChart('clusterReason');
            const labels = Object.keys(reasons).map(r => {
                const clean = r.replace(/_/g, ' ').toLowerCase();
                return clean.replace(/\b\w/g, l => l.toUpperCase());
            }).slice(0, 5);
            const counts = Object.values(reasons).slice(0, 5);

            charts.clusterReason = new Chart(ctx, {
                type: 'bar',
                data: {
                    labels,
                    datasets: [{
                        label: 'Accounts',
                        data: counts,
                        backgroundColor: ['#ef4444', '#f43f5e', '#f97316', '#f59e0b', '#2563eb'],
                        borderRadius: 4,
                        barThickness: 16
                    }]
                },
                options: {
                    indexAxis: 'y',
                    responsive: true,
                    maintainAspectRatio: false,
                    plugins: { legend: { display: false } },
                    scales: {
                        x: { grid: { color: 'rgba(0,0,0,0.04)' }, ticks: { font: { size: 10 } } },
                        y: { grid: { display: false }, ticks: { font: { size: 10.5, weight: '600' } } }
                    }
                }
            });
        }

        // Feature table
        const featureTable = document.getElementById('clusterFeatureTable');
        if (featureTable) {
            const features = [
                ['30D Balance Delta', `${profile.avg_balance_change_30d > 0 ? '+' : ''}${profile.avg_balance_change_30d.toFixed(1)}%`, profile.avg_balance_change_30d < 0 ? '#ef4444' : '#10b981'],
                ['30D Transaction Delta', `${profile.avg_transaction_change_30d > 0 ? '+' : ''}${profile.avg_transaction_change_30d.toFixed(1)}%`, profile.avg_transaction_change_30d < 0 ? '#ef4444' : '#10b981'],
                ['Days Since Last Activity', `${profile.avg_days_since_last_transaction.toFixed(1)} days`, '#64748b'],
                ['30D Outflow Flight Rate', `${profile.avg_external_transfer_change_30d > 0 ? '+' : ''}${profile.avg_external_transfer_change_30d.toFixed(1)}%`, profile.avg_external_transfer_change_30d > 20 ? '#ef4444' : '#64748b'],
                ['Monthly Complaints', `${profile.avg_complaints_30d.toFixed(2)}`, profile.avg_complaints_30d > 2 ? '#ef4444' : '#64748b'],
                ['Failed Transaction Rate', `${profile.avg_failed_transactions_30d.toFixed(2)}`, profile.avg_failed_transactions_30d > 2 ? '#ef4444' : '#64748b'],
                ['Unresolved Issues Count', `${profile.avg_unresolved_complaints.toFixed(2)}`, profile.avg_unresolved_complaints > 1 ? '#ef4444' : '#64748b'],
                ['Monthly EMI Default Rate', `${profile.avg_emi_bounce_30d.toFixed(2)}`, profile.avg_emi_bounce_30d > 0.5 ? '#ef4444' : '#10b981'],
            ];
            featureTable.innerHTML = `<table>
                <thead><tr><th>Behavioral Feature</th><th>Cohort Average</th></tr></thead>
                <tbody>${features.map(([name, val, col]) => `<tr><td>${name}</td><td style="font-weight:700;color:${col}">${val}</td></tr>`).join('')}</tbody>
            </table>`;
        }

        // Customer table
        const tbody = document.getElementById('clusterCustBody');
        if (tbody) {
            tbody.innerHTML = customers.slice(0, 30).map(c => {
                const badge = c.risk_level === 'High' ? 'badge-high' : c.risk_level === 'Medium' ? 'badge-med' : 'badge-low';
                const probColor = c.risk_level === 'High' ? '#ef4444' : c.risk_level === 'Medium' ? '#b45309' : '#16a34a';
                const scoreVal = Math.round(c.risk_score || 0);
                const frictionRaw = c.primary_reason ? c.primary_reason.replace(/_/g, ' ') : 'Stable';
                const frictionLabel = frictionRaw.replace(/\b\w/g, l => l.toUpperCase());
                const actionRaw = c.recommended_action ? c.recommended_action.replace(/_/g, ' ') : 'Monitor';
                const actionLabel = actionRaw.replace(/\b\w/g, l => l.toUpperCase());
                const urgency = c.urgency || '';
                const urgClass = urgency === 'HIGH' ? 'urgency-high' : urgency === 'MEDIUM' ? 'urgency-med' : 'urgency-low';
                const urgLabel = urgency ? `<span class="urgency-pill ${urgClass}">${urgency.charAt(0) + urgency.slice(1).toLowerCase()}</span>` : `<span class="dir-none">—</span>`;
                const seg = c.customer_segment ? (c.customer_segment.charAt(0).toUpperCase() + c.customer_segment.slice(1).toLowerCase()) : '—';

                return `<tr onclick="openCustomerModal('${c.customer_id}')" class="dir-row">
                    <td>
                        <div class="acct-cell">
                            <div class="acct-info">
                                <div class="acct-name">${c.customer_name}</div>
                                <div class="acct-id">${c.customer_id}</div>
                            </div>
                        </div>
                    </td>
                    <td><span class="seg-tag">${seg}</span></td>
                    <td><span class="badge ${badge}">${c.risk_level}</span></td>
                    <td>
                        <div class="prob-cell" title="Risk Score: ${scoreVal}/100 (Model Churn Prob: ${(c.churn_probability || 0).toFixed(1)}%)">
                            <div class="prob-track"><div class="prob-fill" style="width:${Math.min(100, Math.max(4, scoreVal))}%;background:${probColor}"></div></div>
                            <strong style="color:${probColor}">${scoreVal}<span style="font-size:0.68rem;color:var(--text-muted);font-weight:600">/100</span></strong>
                        </div>
                    </td>
                    <td class="friction-cell">${frictionLabel}</td>
                    <td class="action-cell">${actionLabel}</td>
                    <td>${urgLabel}</td>
                    <td class="text-right">
                        <button class="btn-profile" onclick="event.stopPropagation();openCustomerModal('${c.customer_id}')">
                            <i class="fa-solid fa-arrow-up-right-from-square"></i> Audit
                        </button>
                    </td>
                </tr>`;
            }).join('');
        }

        // Smooth scroll to drilldown panel if explicitly triggered by user click
        if (shouldScroll) {
            const drillEl = document.getElementById('clusterDrillPanel');
            if (drillEl) {
                drillEl.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }
        }
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
                labels: ['High Risk', 'Medium Risk', 'Healthy'],
                datasets: [{ data: [dist.High || 0, dist.Medium || 0, dist.Low || 0], backgroundColor: ['#ef4444', '#f59e0b', '#10b981'] }]
            },
            plugins: [doughnutSliceLabelsPlugin],
            options: {
                responsive: true,
                maintainAspectRatio: false,
                layout: {
                    padding: {
                        top: 14,
                        bottom: 14,
                        left: 80,
                        right: 80
                    }
                },
                plugins: { legend: { position: 'bottom' } }
            }
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
            data: { labels, datasets: [{ data: Object.values(reasons), backgroundColor: ['#2563eb', '#ef4444', '#f59e0b', '#10b981', '#f43f5e', '#0ea5e9', '#0891b2', '#14b8a6', '#64748b', '#e11d48'] }] },
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
                    { label: 'Balance Δ', data: trends.map(t => t.balance_delta), borderColor: '#2563eb', fill: false, tension: 0.3, pointRadius: 5 },
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
