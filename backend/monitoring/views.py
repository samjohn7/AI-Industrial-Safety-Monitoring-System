from django.shortcuts import render
from monitoring.models import (
    Violation,
    Intrusion,
    Alert,
    Camera
)

def dashboard_home(request):

    total_violations = Violation.objects.count()

    total_intrusions = Intrusion.objects.count()

    active_alerts = Alert.objects.filter(
        status=False
    ).count()

    online_cameras = Camera.objects.filter(
        status='ONLINE'
    ).count()

    recent_violations = Violation.objects.select_related(
        'camera',
        'camera__zone',
        'worker'
    ).order_by(
        '-detected_at'
    )[:10]

    recent_alerts = Alert.objects.order_by(
        '-created_at'
    )[:5]

    context = {
        'total_violations': total_violations,
        'total_intrusions': total_intrusions,
        'active_alerts': active_alerts,
        'online_cameras': online_cameras,
        'recent_violations': recent_violations,
        'recent_alerts': recent_alerts,
    }

    return render(
        request,
        'dashboard/index.html',
        context
    )