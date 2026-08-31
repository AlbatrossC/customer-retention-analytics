// FinRetain Enterprise — Banking Customer Retention Intelligence Console

let riskChartInstance = null;
let topFactorsChartInstance = null;
let actionsChartInstance = null;
let reasonsChartInstance = null;
let productDepthChartInstance = null;
let modalHistoryChartInstance = null;

// Application State
const state = {
    currentRiskFilter: 'all',
    currentSegment: 'all',
    currentAction: 'all',
    currentUrgency: 'all',
    currentSort: 'risk_score-desc',
    searchQuery: '',
    currentPage: 1,
    pageSize: 25,
    totalRecords: 0
};

document.addEventListener('DOMContentLoaded', () => {
    initDashboard();
});

function initDashboard() {
    // Initial data loading
    fetchDashboardStats();
    fetchCustomerDirectory();

    // Setup interactive event listeners
    setupEventListeners();
}

function setupEventListeners() {
    // Refresh button
    const refreshBtn = document.getElementById('refreshBtn');
    if (refreshBtn) {
        refreshBtn.addEventListener('click', () => {
            const icon = refreshBtn.querySelector('i');
            if (icon) icon.classList.add('fa-spin');
            fetchDashboardStats();
            fetchCustomerDirectory();
            setTimeout(() => {
                if (icon) icon.classList.remove('fa-spin');
            }, 600);
        });
    }

    // Export CSV button
    const exportCsvBtn = document.getElementById('exportCsvBtn');
    if (exportCsvBtn) {
        exportCsvBtn.addEventListener('click', exportRetentionRosterCSV);
    }

    // Risk Filter Tabs
    const tabs = document.querySelectorAll('.filter-tab');
    tabs.forEach(tab => {
        tab.addEventListener('click', () => {
            setRiskFilter(tab.dataset.risk);
        });
    });

    // Dropdowns
    document.getElementById('filterSegment').addEventListener('change', (e) => {
        state.currentSegment = e.target.value;
        state.currentPage = 1;
        fetchCustomerDirectory();
    });

    document.getElementById('filterAction').addEventListener('change', (e) => {
        state.currentAction = e.target.value;
        state.currentPage = 1;
        fetchCustomerDirectory();
    });

    document.getElementById('filterUrgency').addEventListener('change', (e) => {
        state.currentUrgency = e.target.value;
        state.currentPage = 1;
        fetchCustomerDirectory();
    });

    document.getElementById('filterSort').addEventListener('change', (e) => {
        state.currentSort = e.target.value;
        state.currentPage = 1;
        fetchCustomerDirectory();
    });

    // Search Input with Debounce
    const searchInput = document.getElementById('searchInput');
    const clearSearchBtn = document.getElementById('clearSearchBtn');
    let searchDebounce = null;

    searchInput.addEventListener('input', (e) => {
        const val = e.target.value.trim();
        clearSearchBtn.style.display = val ? 'block' : 'none';
        
        clearTimeout(searchDebounce);
        searchDebounce = setTimeout(() => {
            state.searchQuery = val;
            state.currentPage = 1;
            fetchCustomerDirectory();
        }, 300);
    });

    clearSearchBtn.addEventListener('click', () => {
        searchInput.value = '';
        clearSearchBtn.style.display = 'none';
        state.searchQuery = '';
        state.currentPage = 1;
        fetchCustomerDirectory();
    });

    // Pagination buttons
    document.getElementById('prevPageBtn').addEventListener('click', () => {
        if (state.currentPage > 1) {
            state.currentPage--;
            fetchCustomerDirectory();
        }
    });

    document.getElementById('nextPageBtn').addEventListener('click', () => {
        const totalPages = Math.ceil(state.totalRecords / state.pageSize);
        if (state.currentPage < totalPages) {
            state.currentPage++;
            fetchCustomerDirectory();
        }
    });

    // Modal Close
    const modalCloseBtn = document.getElementById('modalCloseBtn');
    const modalOverlay = document.getElementById('customerModal');

    modalCloseBtn.addEventListener('click', () => {
        modalOverlay.classList.remove('active');
    });

    modalOverlay.addEventListener('click', (e) => {
        if (e.target === modalOverlay) {
            modalOverlay.classList.remove('active');
        }
    });

    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape' && modalOverlay.classList.contains('active')) {
            modalOverlay.classList.remove('active');
        }
    });
}

// --------------------------------------------------------------------------
// Interactive Helper Filters
// --------------------------------------------------------------------------
window.setRiskFilter = function(risk) {
    state.currentRiskFilter = risk;
    state.currentPage = 1;

    const tabs = document.querySelectorAll('.filter-tab');
    tabs.forEach(t => {
        if (t.dataset.risk.toLowerCase() === risk.toLowerCase()) {
            t.classList.add('active');
        } else {
            t.classList.remove('active');
        }
    });

    fetchCustomerDirectory();
};

window.filterBySegment = function(segment) {
    state.currentSegment = segment.toLowerCase();
    state.currentPage = 1;

    const select = document.getElementById('filterSegment');
    if (select) select.value = segment.toLowerCase();

    fetchCustomerDirectory();

    // Smooth scroll to directory
    const section = document.getElementById('customerDirectorySection');
    if (section) {
        section.scrollIntoView({ behavior: 'smooth', block: 'start' });
    }
};

// --------------------------------------------------------------------------
// API Calls: Executive Dashboard Stats & Visualizations
// --------------------------------------------------------------------------
async function fetchDashboardStats() {
    try {
        const res = await fetch('/api/dashboard_stats');
        const data = await res.json();
        
        updateKPIHeader(data);
        renderRiskDistributionChart(data);
        renderTopRiskFactors(data);
        renderSegmentCardsGrid(data);
        renderActionsChart(data);
        renderReasonsChart(data);
        renderProductDepthChart(data);
    } catch (err) {
        console.error('Error fetching dashboard statistics:', err);
    }
}

function updateKPIHeader(data) {
    const total = data.total_customers || 10000;
    const high = data.risk_distribution['High'] || 0;
    const med = data.risk_distribution['Medium'] || 0;
    const low = data.risk_distribution['Low'] || 0;

    // KPI Values
    document.getElementById('kpi-total-customers').textContent = total.toLocaleString();
    document.getElementById('kpi-high-risk').textContent = high.toLocaleString();
    document.getElementById('kpi-med-risk').textContent = med.toLocaleString();
    document.getElementById('kpi-low-risk').textContent = low.toLocaleString();

    // Percentages
    const highPct = ((high / total) * 100).toFixed(1);
    const medPct = ((med / total) * 100).toFixed(1);
    const lowPct = ((low / total) * 100).toFixed(1);

    document.getElementById('kpi-high-pct').textContent = `${highPct}%`;
    document.getElementById('kpi-med-pct').textContent = `${medPct}%`;
    document.getElementById('kpi-low-pct').textContent = `${lowPct}%`;

    // Tab counts
    document.getElementById('tab-count-all').textContent = total.toLocaleString();
    document.getElementById('tab-count-high').textContent = high.toLocaleString();
    document.getElementById('tab-count-med').textContent = med.toLocaleString();
    document.getElementById('tab-count-low').textContent = low.toLocaleString();

    // Currency values & Exposure Ratio
    const revRisk = data.revenue_at_risk || 0;
    const totalVal = data.total_portfolio_value || 0;
    const riskRatio = totalVal > 0 ? ((revRisk / totalVal) * 100).toFixed(1) : '0.0';

    document.getElementById('kpi-revenue-risk').textContent = `₹${(revRisk / 1000000).toFixed(2)}M`;
    document.getElementById('kpi-portfolio-val').textContent = `₹${(totalVal / 1000000).toFixed(2)}M`;
    
    const ratioEl = document.getElementById('capitalRiskRatio');
    if (ratioEl) ratioEl.textContent = `${riskRatio}%`;

    const barEl = document.getElementById('capitalProgressBar');
    if (barEl) barEl.style.width = `${Math.min(100, riskRatio)}%`;
}

// --------------------------------------------------------------------------
// Visualizations
// --------------------------------------------------------------------------
function renderRiskDistributionChart(data) {
    const ctx = document.getElementById('riskDistChart').getContext('2d');
    if (riskChartInstance) riskChartInstance.destroy();

    const high = data.risk_distribution['High'] || 0;
    const med = data.risk_distribution['Medium'] || 0;
    const low = data.risk_distribution['Low'] || 0;
    const total = high + med + low;

    riskChartInstance = new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: ['High Risk (Critical)', 'Watchlist (Medium)', 'Healthy & Stable'],
            datasets: [{
                data: [high, med, low],
                backgroundColor: ['#dc2626', '#d97706', '#059669'],
                hoverBackgroundColor: ['#b91c1c', '#b45309', '#047857'],
                borderWidth: 2,
                borderColor: '#ffffff'
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            cutout: '72%',
            plugins: {
                legend: { display: false },
                tooltip: {
                    callbacks: {
                        label: (ctx) => {
                            const val = ctx.raw;
                            const pct = ((val / total) * 100).toFixed(1);
                            return ` ${ctx.label}: ${val.toLocaleString()} (${pct}%)`;
                        }
                    }
                }
            }
        }
    });

    const legendContainer = document.getElementById('riskStatsLegend');
    legendContainer.innerHTML = `
        <div class="legend-row" onclick="setRiskFilter('High')">
            <div class="legend-label-group">
                <span class="legend-dot dot-high"></span>
                <span>High Risk (Immediate Action)</span>
            </div>
            <span><strong>${high.toLocaleString()}</strong> (${((high/total)*100).toFixed(1)}%)</span>
        </div>
        <div class="legend-row" onclick="setRiskFilter('Medium')">
            <div class="legend-label-group">
                <span class="legend-dot dot-med"></span>
                <span>Watchlist (Nurture)</span>
            </div>
            <span><strong>${med.toLocaleString()}</strong> (${((med/total)*100).toFixed(1)}%)</span>
        </div>
        <div class="legend-row" onclick="setRiskFilter('Low')">
            <div class="legend-label-group">
                <span class="legend-dot dot-low"></span>
                <span>Healthy (Active)</span>
            </div>
            <span><strong>${low.toLocaleString()}</strong> (${((low/total)*100).toFixed(1)}%)</span>
        </div>
    `;
}

function renderTopRiskFactors(data) {
    const factors = data.top_risk_factors || [];
    
    // Horizontal Bar Chart for Top 5 Factors
    const ctx = document.getElementById('topFactorsChart').getContext('2d');
    if (topFactorsChartInstance) topFactorsChartInstance.destroy();

    const chartFactors = factors.slice(0, 5);
    const labels = chartFactors.map(f => f.display_label || f.factor_name);
    const counts = chartFactors.map(f => f.frequency);

    topFactorsChartInstance = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: labels,
            datasets: [{
                label: 'Affected Accounts',
                data: counts,
                backgroundColor: 'rgba(220, 38, 38, 0.85)',
                borderRadius: 4
            }]
        },
        options: {
            indexAxis: 'y',
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: { display: false },
                tooltip: {
                    callbacks: {
                        afterLabel: (ctx) => {
                            const f = chartFactors[ctx.dataIndex];
                            return `Trigger: ${f.factor_message}`;
                        }
                    }
                }
            },
            scales: {
                x: { grid: { display: false }, ticks: { font: { size: 10 } } },
                y: { grid: { display: false }, ticks: { font: { size: 10, weight: 600 } } }
            }
        }
    });

    // Ranked Detailed List
    const listContainer = document.getElementById('topFactorsList');
    listContainer.innerHTML = factors.map((f, i) => `
        <div class="factor-item-card">
            <div class="factor-item-header">
                <span class="factor-item-name">#${i+1} ${f.display_label || f.factor_name}</span>
                <span class="factor-item-impact">${f.frequency.toLocaleString()} accounts</span>
            </div>
            <p class="factor-item-desc">${f.factor_message}</p>
        </div>
    `).join('');
}

function renderSegmentCardsGrid(data) {
    const clusters = data.segment_clusters || [];
    const container = document.getElementById('segmentCardsGrid');
    
    container.innerHTML = clusters.map(seg => {
        const highPct = seg.high_risk_pct;
        let riskColor = '#059669';
        if (highPct > 20) riskColor = '#dc2626';
        else if (highPct > 10) riskColor = '#d97706';

        return `
            <div class="segment-metric-card" onclick="filterBySegment('${seg.segment}')">
                <div class="segment-card-header">
                    <span class="segment-card-title">${seg.segment} Accounts</span>
                    <span class="segment-card-count">${seg.total_customers.toLocaleString()} total</span>
                </div>
                <div class="segment-risk-highlight">
                    <span class="segment-risk-pct" style="color:${riskColor}">${highPct}% Risk</span>
                    <span class="segment-risk-revenue">₹${(seg.at_risk_value/1000000).toFixed(2)}M at risk</span>
                </div>
                <div class="segment-bar-wrapper">
                    <div class="segment-bar-active" style="width:${Math.min(100, highPct * 2.5)}%; background-color:${riskColor};"></div>
                </div>
            </div>
        `;
    }).join('');
}

function renderActionsChart(data) {
    const ctx = document.getElementById('actionsChart').getContext('2d');
    if (actionsChartInstance) actionsChartInstance.destroy();

    const actions = data.recommended_actions || {};
    const labels = Object.keys(actions).map(a => a.replace(/_/g, ' ')).slice(0, 6);
    const counts = Object.values(actions).slice(0, 6);

    actionsChartInstance = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: labels,
            datasets: [{
                label: 'Recommended Plays',
                data: counts,
                backgroundColor: '#2563eb',
                borderRadius: 4
            }]
        },
        options: {
            indexAxis: 'y',
            responsive: true,
            maintainAspectRatio: false,
            plugins: { legend: { display: false } },
            scales: {
                x: { grid: { display: false }, ticks: { font: { size: 10 } } },
                y: { grid: { display: false }, ticks: { font: { size: 10, weight: 600 } } }
            }
        }
    });
}

function renderReasonsChart(data) {
    const ctx = document.getElementById('reasonsChart').getContext('2d');
    if (reasonsChartInstance) reasonsChartInstance.destroy();

    const reasons = data.primary_reasons || {};
    const labels = Object.keys(reasons).map(r => r.replace(/_/g, ' ')).slice(0, 6);
    const counts = Object.values(reasons).slice(0, 6);

    reasonsChartInstance = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: labels,
            datasets: [{
                label: 'Primary Pain Points',
                data: counts,
                backgroundColor: '#d97706',
                borderRadius: 4
            }]
        },
        options: {
            indexAxis: 'y',
            responsive: true,
            maintainAspectRatio: false,
            plugins: { legend: { display: false } },
            scales: {
                x: { grid: { display: false }, ticks: { font: { size: 10 } } },
                y: { grid: { display: false }, ticks: { font: { size: 10, weight: 600 } } }
            }
        }
    });
}

function renderProductDepthChart(data) {
    const ctx = document.getElementById('productDepthChart').getContext('2d');
    if (productDepthChartInstance) productDepthChartInstance.destroy();

    const depthStats = data.product_depth_stats || [];
    const labels = depthStats.map(d => d.bracket);
    const churnRates = depthStats.map(d => d.avg_churn_prob);

    productDepthChartInstance = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: labels,
            datasets: [{
                label: 'Average Churn Rate (%)',
                data: churnRates,
                backgroundColor: ['#ef4444', '#f59e0b', '#10b981', '#059669'],
                borderRadius: 4
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: { display: false },
                tooltip: {
                    callbacks: {
                        label: (ctx) => ` Avg Churn Probability: ${ctx.raw.toFixed(1)}%`
                    }
                }
            },
            scales: {
                x: { grid: { display: false }, ticks: { font: { size: 10, weight: 600 } } },
                y: { 
                    title: { display: true, text: 'Avg Churn %' },
                    grid: { display: false }
                }
            }
        }
    });
}

// --------------------------------------------------------------------------
// Customer Account Directory
// --------------------------------------------------------------------------
async function fetchCustomerDirectory() {
    const [sortBy, sortOrder] = state.currentSort.split('-');
    const offset = (state.currentPage - 1) * state.pageSize;

    const params = new URLSearchParams({
        risk_level: state.currentRiskFilter,
        segment: state.currentSegment,
        action: state.currentAction,
        urgency: state.currentUrgency,
        search: state.searchQuery,
        sort_by: sortBy,
        sort_order: sortOrder,
        limit: state.pageSize,
        offset: offset
    });

    try {
        const res = await fetch(`/api/customers?${params.toString()}`);
        const data = await res.json();
        
        state.totalRecords = data.total_count || 0;
        renderCustomerTable(data.customers || []);
        updatePaginationUI();
    } catch (err) {
        console.error('Error fetching customer directory:', err);
    }
}

function renderCustomerTable(customers) {
    const tbody = document.getElementById('customerTableBody');
    tbody.innerHTML = '';

    if (!customers || customers.length === 0) {
        tbody.innerHTML = `
            <tr>
                <td colspan="8" style="text-align:center; padding: 3rem; color: #94a3b8;">
                    <i class="fa-solid fa-folder-open" style="font-size:2rem; margin-bottom:0.5rem; display:block;"></i>
                    No accounts match the current filter criteria.
                </td>
            </tr>
        `;
        return;
    }

    customers.forEach(c => {
        const tr = document.createElement('tr');

        // Avatar Initials
        const initials = c.customer_name ? c.customer_name.split(' ').map(n => n[0]).join('').substring(0,2).toUpperCase() : 'CU';
        const tierClass = `tier-${(c.card_colour || 'silver').toLowerCase()}`;

        // Risk Badge
        let riskBadgeClass = 'badge-low';
        let probFillColor = '#059669';
        if (c.risk_level === 'High') {
            riskBadgeClass = 'badge-high';
            probFillColor = '#dc2626';
        } else if (c.risk_level === 'Medium') {
            riskBadgeClass = 'badge-medium';
            probFillColor = '#d97706';
        }

        // Urgency Tag
        let urgencyTag = '';
        if (c.urgency) {
            const uClass = `urgency-${c.urgency.toLowerCase()}`;
            urgencyTag = `<span class="urgency-tag ${uClass}">${c.urgency}</span>`;
        }

        tr.innerHTML = `
            <td>
                <div class="customer-cell">
                    <div class="customer-avatar">${initials}</div>
                    <div>
                        <div class="customer-meta-name">${c.customer_name}</div>
                        <div class="customer-meta-id">${c.customer_id}</div>
                    </div>
                </div>
            </td>
            <td>
                <span style="text-transform: capitalize; font-weight:600;">${c.customer_segment}</span>
                <span class="tier-pill ${tierClass}">${c.card_colour || 'Silver'}</span>
            </td>
            <td><strong>₹${(c.customer_yearly_value || 0).toLocaleString()}</strong></td>
            <td><span class="kpi-badge ${riskBadgeClass}">${c.risk_level}</span></td>
            <td>
                <div class="prob-cell">
                    <div class="prob-meter-bg">
                        <div class="prob-meter-fill" style="width: ${Math.min(100, c.churn_probability * 2)}%; background-color: ${probFillColor}"></div>
                    </div>
                    <strong>${(c.churn_probability || 0).toFixed(1)}%</strong>
                </div>
            </td>
            <td>${c.primary_reason ? c.primary_reason.replace(/_/g, ' ') : '<span style="color:#94a3b8;">Stable Account</span>'}</td>
            <td>
                <div style="display:flex; align-items:center; gap:0.4rem;">
                    <span>${c.recommended_action ? c.recommended_action.replace(/_/g, ' ') : '<span style="color:#94a3b8;">Standard Monitoring</span>'}</span>
                    ${urgencyTag}
                </div>
            </td>
            <td class="text-right">
                <button class="btn-audit" onclick="openCustomerDetailModal('${c.customer_id}')">
                    <i class="fa-solid fa-file-waveform"></i> Audit
                </button>
            </td>
        `;
        tbody.appendChild(tr);
    });
}

function updatePaginationUI() {
    const totalPages = Math.max(1, Math.ceil(state.totalRecords / state.pageSize));
    document.getElementById('currentPageNum').textContent = state.currentPage;
    document.getElementById('totalPagesNum').textContent = totalPages;
    
    document.getElementById('prevPageBtn').disabled = state.currentPage <= 1;
    document.getElementById('nextPageBtn').disabled = state.currentPage >= totalPages;

    const startIdx = state.totalRecords === 0 ? 0 : (state.currentPage - 1) * state.pageSize + 1;
    const endIdx = Math.min(state.totalRecords, state.currentPage * state.pageSize);

    document.getElementById('currentShownCount').textContent = `${startIdx}-${endIdx}`;
    document.getElementById('totalMatchedCount').textContent = state.totalRecords.toLocaleString();
}

// --------------------------------------------------------------------------
// CSV Export Functionality
// --------------------------------------------------------------------------
async function exportRetentionRosterCSV() {
    try {
        const [sortBy, sortOrder] = state.currentSort.split('-');
        const params = new URLSearchParams({
            risk_level: state.currentRiskFilter,
            segment: state.currentSegment,
            action: state.currentAction,
            urgency: state.currentUrgency,
            search: state.searchQuery,
            sort_by: sortBy,
            sort_order: sortOrder,
            limit: 500, // Export top 500 matching
            offset: 0
        });

        const res = await fetch(`/api/customers?${params.toString()}`);
        const data = await res.json();
        const list = data.customers || [];

        if (list.length === 0) {
            alert('No records to export under current filters.');
            return;
        }

        const headers = ["Customer ID", "Customer Name", "Segment", "Card Tier", "Annual Value (INR)", "Risk Tier", "Risk Score", "Churn Prob (%)", "Primary Pain Point", "Recommended Action Play", "Urgency"];
        const rows = list.map(c => [
            `"${c.customer_id}"`,
            `"${c.customer_name}"`,
            `"${c.customer_segment}"`,
            `"${c.card_colour || 'Silver'}"`,
            `"${c.customer_yearly_value}"`,
            `"${c.risk_level}"`,
            `"${c.risk_score}"`,
            `"${c.churn_probability}"`,
            `"${(c.primary_reason || 'None').replace(/_/g, ' ')}"`,
            `"${(c.recommended_action || 'Monitor').replace(/_/g, ' ')}"`,
            `"${c.urgency || 'Normal'}"`
        ]);

        const csvContent = "data:text/csv;charset=utf-8," + [headers.join(','), ...rows.map(r => r.join(','))].join('\n');
        const encodedUri = encodeURI(csvContent);
        const link = document.createElement("a");
        link.setAttribute("href", encodedUri);
        link.setAttribute("download", `FinRetain_Retention_Roster_${new Date().toISOString().slice(0,10)}.csv`);
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
    } catch (err) {
        console.error('Error exporting CSV:', err);
    }
}

// --------------------------------------------------------------------------
// Deep-Dive Customer Diagnostic Modal
// --------------------------------------------------------------------------
window.openCustomerDetailModal = async function(customerId) {
    const modal = document.getElementById('customerModal');
    const modalContent = document.getElementById('modalContent');

    modal.classList.add('active');
    modalContent.innerHTML = `
        <div class="modal-loading-state">
            <i class="fa-solid fa-spinner fa-spin"></i>
            <p>Auditing account data & behavioral logs for <strong>${customerId}</strong>...</p>
        </div>
    `;

    try {
        const [profileRes, historyRes] = await Promise.all([
            fetch(`/api/customer/${customerId}`),
            fetch(`/api/customer/${customerId}/history`)
        ]);

        const profileData = await profileRes.json();
        const historyData = await historyRes.json();

        renderCustomerModalContent(profileData, historyData);
    } catch (err) {
        console.error('Error loading customer details:', err);
        modalContent.innerHTML = `
            <div style="padding:3rem; text-align:center; color:#dc2626;">
                <i class="fa-solid fa-triangle-exclamation" style="font-size:2rem; margin-bottom:1rem;"></i>
                <p>Failed to load customer account profile. Please try again.</p>
            </div>
        `;
    }
};

function renderCustomerModalContent(data, history) {
    const modalContent = document.getElementById('modalContent');
    const p = data.profile;
    const factors = data.risk_factors || [];
    const evidence = data.evidence || [];

    const initials = p.customer_name ? p.customer_name.split(' ').map(n => n[0]).join('').substring(0,2).toUpperCase() : 'CU';

    let riskBadge = 'badge-low';
    if (p.risk_level === 'High') riskBadge = 'badge-high';
    else if (p.risk_level === 'Medium') riskBadge = 'badge-medium';

    let urgencyTag = '';
    if (p.urgency) {
        urgencyTag = `<span class="urgency-tag urgency-${p.urgency.toLowerCase()}">${p.urgency} PRIORITY</span>`;
    }

    modalContent.innerHTML = `
        <!-- Hero Header -->
        <div class="modal-header-hero">
            <div class="modal-hero-profile">
                <div class="modal-hero-avatar">${initials}</div>
                <div class="modal-hero-title">
                    <h2>${p.customer_name} <span style="font-size:1rem; opacity:0.8; font-weight:400;">(${p.customer_id})</span></h2>
                    <div class="modal-hero-badges">
                        <span class="badge-tag-dark"><i class="fa-solid fa-briefcase"></i> Segment: <strong>${p.customer_segment.toUpperCase()}</strong></span>
                        <span class="badge-tag-dark"><i class="fa-solid fa-credit-card"></i> Tier: <strong>${(p.card_colour || 'Silver').toUpperCase()}</strong></span>
                        <span class="badge-tag-dark"><i class="fa-solid fa-clock"></i> Tenure: <strong>${p.tenure_months} Mo</strong></span>
                        <span class="badge-tag-dark"><i class="fa-solid fa-coins"></i> Annual Value: <strong>₹${(p.customer_yearly_value || 0).toLocaleString()}</strong></span>
                        <span class="badge-tag-dark"><i class="fa-solid fa-code-branch"></i> Branch: <strong>${p.branch_code || 'Main'}</strong></span>
                    </div>
                </div>
            </div>
            <div>
                <span class="kpi-badge ${riskBadge}" style="font-size:0.9rem; padding:0.4rem 1rem;">
                    ${p.risk_level} Risk (${(p.churn_probability || 0).toFixed(1)}%)
                </span>
            </div>
        </div>

        <div class="modal-body-container">
            <!-- Dual Section Cards -->
            <div class="modal-dual-cards">
                <!-- Card 1: Key Account Risk Indicators -->
                <div class="modal-section-card">
                    <div class="modal-card-header">
                        <div class="modal-card-title">
                            <i class="fa-solid fa-chart-line text-blue"></i>
                            <span>Key Account Risk Indicators</span>
                        </div>
                        <span class="panel-tag">Risk Score: ${(p.risk_score || 0).toFixed(1)}/100</span>
                    </div>

                    <h4 style="font-size:0.8rem; text-transform:uppercase; color:#64748b;">Primary Churn Contributors</h4>
                    <div class="shap-factors-list">
                        ${factors.map(f => `
                            <div class="shap-factor-row">
                                <div class="shap-factor-title">
                                    <span>#${f.factor_rank} ${f.factor_name.replace(/_/g, ' ')}</span>
                                    <span style="color:#dc2626;">+${f.contribution ? f.contribution.toFixed(3) : '0.00'} Impact</span>
                                </div>
                                <div class="shap-factor-msg">${f.factor_message}</div>
                            </div>
                        `).join('')}
                    </div>
                </div>

                <!-- Card 2: AI Strategic Retention Plan -->
                <div class="modal-section-card">
                    <div class="modal-card-header">
                        <div class="modal-card-title">
                            <i class="fa-solid fa-headset text-indigo"></i>
                            <span>AI Strategic Retention Plan</span>
                        </div>
                        ${urgencyTag}
                    </div>

                    <div style="display:flex; flex-direction:column; gap:0.5rem;">
                        <div style="font-size:0.85rem;">
                            <strong>Primary Friction Point:</strong>
                            <span style="color:#d97706; font-weight:700; margin-left:0.25rem;">${p.primary_reason ? p.primary_reason.replace(/_/g, ' ') : 'N/A'}</span>
                        </div>
                        <div style="font-size:0.85rem;">
                            <strong>Recommended Retention Play:</strong>
                            <span style="color:#2563eb; font-weight:700; margin-left:0.25rem;">${p.recommended_action ? p.recommended_action.replace(/_/g, ' ') : 'MONITOR'}</span>
                        </div>
                    </div>

                    <h4 style="font-size:0.8rem; text-transform:uppercase; color:#64748b; margin-top:0.25rem;">Relationship Manager Guidance</h4>
                    <div class="llm-reasoning-box">
                        "${p.reasoning_summary || 'Customer demonstrates standard retention profile with minimal friction indicators.'}"
                    </div>

                    ${evidence.length > 0 ? `
                        <h4 style="font-size:0.8rem; text-transform:uppercase; color:#64748b; margin-top:0.25rem;">Account Audit Signals</h4>
                        <div class="evidence-tags-container">
                            ${evidence.map(e => `<span class="evidence-tag">${e.evidence_text}</span>`).join('')}
                        </div>
                    ` : ''}
                </div>
            </div>

            <!-- Behavioral Trends (Last 6 Months) -->
            <div class="modal-history-section">
                <div class="modal-card-title" style="margin-bottom:0.5rem;">
                    <i class="fa-solid fa-timeline text-slate"></i>
                    <span>6-Month Account Trajectory & Friction Log</span>
                </div>
                
                <div class="history-chart-wrapper">
                    <canvas id="modalHistoryChart"></canvas>
                </div>

                <div class="history-table-wrapper">
                    <table class="mini-table">
                        <thead>
                            <tr>
                                <th>Month</th>
                                <th>Balance Δ (30d)</th>
                                <th>Txn Volume Δ</th>
                                <th>App Logins Δ</th>
                                <th>UPI Share</th>
                                <th>Complaints</th>
                                <th>Failed Txns</th>
                                <th>Customer Feedback / Complaint Note</th>
                            </tr>
                        </thead>
                        <tbody>
                            ${history.map(h => `
                                <tr>
                                    <td><strong>${h.snapshot_date.substring(0,7)}</strong></td>
                                    <td style="color: ${h.balance_change_30d < 0 ? '#dc2626' : '#059669'}">${h.balance_change_30d ? h.balance_change_30d.toFixed(1)+'%' : '0%'}</td>
                                    <td style="color: ${h.transaction_change_30d < 0 ? '#dc2626' : '#059669'}">${h.transaction_change_30d ? h.transaction_change_30d.toFixed(1)+'%' : '0%'}</td>
                                    <td>${h.app_login_change_30d ? h.app_login_change_30d.toFixed(1)+'%' : '0%'}</td>
                                    <td>${(h.upi_share_of_spend ? (h.upi_share_of_spend*100).toFixed(0)+'%' : '0%')}</td>
                                    <td>${h.complaints_30d || 0}</td>
                                    <td>${h.failed_transactions_30d || 0}</td>
                                    <td>${h.complaint_text ? `<span class="complaint-quote">"${h.complaint_text}"</span>` : '<span style="color:#94a3b8;">None</span>'}</td>
                                </tr>
                            `).join('')}
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    `;

    // Render Modal Chart
    setTimeout(() => {
        const ctx = document.getElementById('modalHistoryChart').getContext('2d');
        if (modalHistoryChartInstance) modalHistoryChartInstance.destroy();

        const sortedHistory = [...history].sort((a,b) => a.snapshot_date.localeCompare(b.snapshot_date));
        const dates = sortedHistory.map(h => h.snapshot_date.substring(0,7));
        const balances = sortedHistory.map(h => h.balance_change_30d || 0);
        const txns = sortedHistory.map(h => h.transaction_change_30d || 0);

        modalHistoryChartInstance = new Chart(ctx, {
            type: 'line',
            data: {
                labels: dates,
                datasets: [
                    {
                        label: 'Balance Change 30d (%)',
                        data: balances,
                        borderColor: '#2563eb',
                        backgroundColor: 'rgba(37, 99, 235, 0.08)',
                        tension: 0.3,
                        fill: true
                    },
                    {
                        label: 'Transaction Count Change (%)',
                        data: txns,
                        borderColor: '#d97706',
                        backgroundColor: 'transparent',
                        borderDash: [5, 5],
                        tension: 0.3
                    }
                ]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: { legend: { position: 'top' } },
                scales: {
                    x: { grid: { display: false } },
                    y: { title: { display: true, text: '% Change' } }
                }
            }
        });
    }, 50);
}
