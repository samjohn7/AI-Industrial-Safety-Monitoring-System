document.addEventListener('DOMContentLoaded', function () {
    const chartCanvas = document.getElementById('complianceChart');
    const complianceDataScript = document.getElementById('compliance-data');

    if (!chartCanvas || !complianceDataScript) {
        return;
    }

    const complianceSeries = JSON.parse(complianceDataScript.textContent);
    const labels = complianceSeries.map((item) => item.label);
    const values = complianceSeries.map((item) => item.value);

    new Chart(chartCanvas, {
        type: 'line',
        data: {
            labels,
            datasets: [{
                label: 'Compliance Rate',
                data: values,
                borderColor: '#38bdf8',
                backgroundColor: 'rgba(56, 189, 248, 0.24)',
                fill: true,
                tension: 0.35,
                pointRadius: 5,
                pointBackgroundColor: '#38bdf8',
                pointBorderColor: '#0f172a',
                pointHoverRadius: 7,
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: { display: false },
                tooltip: {
                    backgroundColor: '#0b1629',
                    titleColor: '#e2e8f0',
                    bodyColor: '#cbd5e1',
                    borderColor: 'rgba(56, 189, 248, 0.18)',
                    borderWidth: 1,
                }
            },
            scales: {
                x: {
                    ticks: {
                        color: '#94a3b8',
                        font: { size: 12 },
                    },
                    grid: {
                        color: 'rgba(148, 163, 184, 0.08)',
                        drawBorder: false,
                    }
                },
                y: {
                    beginAtZero: true,
                    max: 100,
                    ticks: {
                        color: '#94a3b8',
                        callback: function (value) {
                            return value + '%';
                        },
                        font: { size: 12 },
                    },
                    grid: {
                        color: 'rgba(148, 163, 184, 0.08)',
                        drawBorder: false,
                    }
                }
            }
        }
    });
});
