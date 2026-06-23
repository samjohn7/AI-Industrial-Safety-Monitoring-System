const ctx = document.getElementById('complianceChart');

new Chart(ctx, {
    type: 'line',
    data: {
        labels: [
            'Mon',
            'Tue',
            'Wed',
            'Thu',
            'Fri',
            'Sat',
            'Sun'
        ],
        datasets: [
            {
                label: 'Compliance Rate (%)',
                data: [88, 91, 86, 94, 92, 96, 98],
                borderColor: '#3b82f6',
                backgroundColor: 'rgba(59,130,246,0.15)',
                fill: true,
                tension: 0.4,
                borderWidth: 3
            }
        ]
    },
    options: {
        responsive: true,
        maintainAspectRatio: false,

        plugins: {
            legend: {
                labels: {
                    color: '#ffffff'
                }
            }
        },

        scales: {

            x: {
                ticks: {
                    color: '#d1d5db'
                },
                grid: {
                    color: 'rgba(255,255,255,0.05)'
                }
            },

            y: {
                beginAtZero: true,
                max: 100,

                ticks: {
                    color: '#d1d5db'
                },

                grid: {
                    color: 'rgba(255,255,255,0.05)'
                }
            }

        }

    }
});