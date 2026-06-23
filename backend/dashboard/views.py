from django.shortcuts import render


def index(request):
    stats = {
        'total_violations': 324,
        'active_alerts': 18,
        'intrusions_detected': 12,
        'cameras_online': 42,
    }

    recent_violations = [
        {'time': '09:12 AM', 'type': 'Unauthorized Access', 'location': 'North Conveyor', 'status': 'Investigating'},
        {'time': '08:45 AM', 'type': 'Hard Hat Missing', 'location': 'Pump Station', 'status': 'Resolved'},
        {'time': '08:10 AM', 'type': 'Gas Alarm', 'location': 'Tunnel B', 'status': 'Responding'},
        {'time': '07:55 AM', 'type': 'Perimeter Breach', 'location': 'West Gate', 'status': 'Monitoring'},
        {'time': '07:20 AM', 'type': 'Equipment Stop', 'location': 'Crusher 3', 'status': 'Investigating'},
    ]

    critical_alerts = [
        {'title': 'Methane spike in Tunnel B', 'message': 'Level rose above 3.5%. Dispatch ventilation team.', 'severity': 'Critical'},
        {'title': 'Unauthorized zone entry', 'message': 'Access detected at Sector 4 perimeter.', 'severity': 'High'},
        {'title': 'Camera offline', 'message': 'CCTV 19 lost signal at south ridge.', 'severity': 'Medium'},
    ]

    compliance_series = [
        {'label': 'Jan', 'value': 82},
        {'label': 'Feb', 'value': 85},
        {'label': 'Mar', 'value': 88},
        {'label': 'Apr', 'value': 90},
        {'label': 'May', 'value': 92},
        {'label': 'Jun', 'value': 94},
    ]

    context = {
        'stats': stats,
        'recent_violations': recent_violations,
        'critical_alerts': critical_alerts,
        'compliance_series': compliance_series,
    }
    return render(request, 'dashboard/index.html', context)
