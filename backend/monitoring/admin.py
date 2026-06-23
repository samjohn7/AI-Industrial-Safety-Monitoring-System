from django.contrib import admin
from .models import (
    Zone,
    Camera,
    Worker,
    Violation,
    Intrusion,
    Alert,
    Evidence,
    AlarmLog
)

admin.site.register(Zone)
admin.site.register(Camera)
admin.site.register(Worker)
admin.site.register(Violation)
admin.site.register(Intrusion)
admin.site.register(Alert)
admin.site.register(Evidence)
admin.site.register(AlarmLog)