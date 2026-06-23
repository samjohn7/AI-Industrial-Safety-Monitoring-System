from django.urls import path
from .views import dashboard_home, violations_list, intrusions_list, alerts_list, evidence_list

urlpatterns = [
    path('', dashboard_home, name='dashboard'),
    path('violations/', violations_list, name='violations'),
    path('intrusions/', intrusions_list, name='intrusions'),
    path('alerts/', alerts_list, name='alerts'),
    path('evidence/', evidence_list, name='evidence'),
]