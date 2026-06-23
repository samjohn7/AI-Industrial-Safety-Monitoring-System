from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import render
from monitoring.models import (
    Violation,
    Intrusion,
    Alert,
    Camera,
    Evidence
)

def dashboard_home(request):

    context = {
        "total_violations": Violation.objects.count(),
        "total_intrusions": Intrusion.objects.count(),
        "active_alerts": Alert.objects.filter(status=False).count(),
        "online_cameras": Camera.objects.filter(status='ONLINE').count(),
        "recent_violations": Violation.objects.order_by('-detected_at')[:10],
        "recent_alerts": Alert.objects.order_by('-created_at')[:5],
    }

    return render(request, 'dashboard/index.html', context)


def violations_list(request):
    search_query = request.GET.get('q', '').strip()
    status_filter = request.GET.get('status', 'ALL').upper()

    violations = Violation.objects.select_related(
        'worker',
        'camera',
        'camera__zone'
    ).order_by('-detected_at')

    if search_query:
        violations = violations.filter(
            Q(worker__full_name__icontains=search_query) |
            Q(worker__employee_no__icontains=search_query) |
            Q(violation_type__icontains=search_query)
        )

    if status_filter in ['OPEN', 'RESOLVED']:
        violations = violations.filter(status=status_filter)

    paginator = Paginator(violations, 10)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    query_params = request.GET.copy()
    if 'page' in query_params:
        query_params.pop('page')

    context = {
        'violations': page_obj,
        'page_obj': page_obj,
        'total_violations': Violation.objects.count(),
        'open_violations': Violation.objects.filter(status='OPEN').count(),
        'resolved_violations': Violation.objects.filter(status='RESOLVED').count(),
        'search_query': search_query,
        'status_filter': status_filter,
        'query_string': query_params.urlencode(),
    }

    return render(request, 'dashboard/violations.html', context)


def intrusions_list(request):
    search_query = request.GET.get('q', '').strip()
    status_filter = request.GET.get('status', 'ALL').upper()

    intrusions = Intrusion.objects.select_related(
        'zone',
        'camera'
    ).order_by('-detected_at')

    if search_query:
        intrusions = intrusions.filter(
            Q(zone__zone_name__icontains=search_query) |
            Q(camera__camera_name__icontains=search_query)
        )

    if status_filter in ['OPEN', 'RESOLVED']:
        intrusions = intrusions.filter(status=status_filter)

    paginator = Paginator(intrusions, 10)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    query_params = request.GET.copy()
    if 'page' in query_params:
        query_params.pop('page')

    context = {
        'intrusions': page_obj,
        'page_obj': page_obj,
        'total_intrusions': Intrusion.objects.count(),
        'open_intrusions': Intrusion.objects.filter(status='OPEN').count(),
        'resolved_intrusions': Intrusion.objects.filter(status='RESOLVED').count(),
        'search_query': search_query,
        'status_filter': status_filter,
        'query_string': query_params.urlencode(),
    }

    return render(request, 'dashboard/intrusions.html', context)


def alerts_list(request):
    search_query = request.GET.get('q', '').strip()
    priority_filter = request.GET.get('priority', 'ALL').upper()
    channel_filter = request.GET.get('channel', 'ALL').upper()

    alerts = Alert.objects.order_by('-created_at')

    if search_query:
        alerts = alerts.filter(alert_type__icontains=search_query)

    if priority_filter in ['CRITICAL', 'HIGH', 'MEDIUM', 'LOW']:
        alerts = alerts.filter(priority=priority_filter)

    if channel_filter in ['DASHBOARD', 'EMAIL', 'VOICE']:
        alerts = alerts.filter(channel=channel_filter)

    paginator = Paginator(alerts, 10)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    query_params = request.GET.copy()
    if 'page' in query_params:
        query_params.pop('page')

    context = {
        'alerts': page_obj,
        'page_obj': page_obj,
        'total_alerts': Alert.objects.count(),
        'active_alerts': Alert.objects.filter(status=False).count(),
        'resolved_alerts': Alert.objects.filter(status=True).count(),
        'search_query': search_query,
        'priority_filter': priority_filter,
        'channel_filter': channel_filter,
        'query_string': query_params.urlencode(),
    }

    return render(request, 'dashboard/alerts.html', context)


def evidence_list(request):
    source_filter = request.GET.get('source', 'ALL').upper()
    evidences = Evidence.objects.order_by('-captured_at')

    if source_filter in ['VIOLATION', 'INTRUSION']:
        evidences = evidences.filter(source_type=source_filter)

    paginator = Paginator(evidences, 12)
    page_number = request.GET.get('page', 1)
    page_obj = paginator.get_page(page_number)

    query_params = request.GET.copy()
    if 'page' in query_params:
        query_params.pop('page')

    context = {
        'evidence_items': page_obj,
        'page_obj': page_obj,
        'total_evidence': Evidence.objects.count(),
        'violation_evidence': Evidence.objects.filter(source_type='VIOLATION').count(),
        'intrusion_evidence': Evidence.objects.filter(source_type='INTRUSION').count(),
        'source_filter': source_filter,
        'query_string': query_params.urlencode(),
    }

    return render(request, 'dashboard/evidence.html', context)