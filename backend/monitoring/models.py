from django.db import models


class Zone(models.Model):
    RISK_LEVELS = [
        ('LOW', 'Low'),
        ('MEDIUM', 'Medium'),
        ('HIGH', 'High'),
        ('CRITICAL', 'Critical'),
    ]

    zone_name = models.CharField(max_length=100, unique=True)
    zone_type = models.CharField(max_length=100)
    risk_level = models.CharField(
        max_length=20,
        choices=RISK_LEVELS,
        default='LOW'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.zone_name
class Camera(models.Model):
    STATUS_CHOICES = [
        ('ONLINE', 'Online'),
        ('OFFLINE', 'Offline'),
    ]

    zone = models.ForeignKey(
        Zone,
        on_delete=models.CASCADE,
        related_name='cameras'
    )

    camera_name = models.CharField(max_length=100)
    stream_url = models.URLField()
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='ONLINE'
    )

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.camera_name
class Worker(models.Model):
    full_name = models.CharField(max_length=150)
    employee_no = models.CharField(max_length=50, unique=True)
    department = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.full_name
class Violation(models.Model):
    STATUS_CHOICES = [
        ('OPEN', 'Open'),
        ('RESOLVED', 'Resolved'),
    ]

    worker = models.ForeignKey(
        Worker,
        on_delete=models.CASCADE,
        related_name='violations'
    )

    camera = models.ForeignKey(
        Camera,
        on_delete=models.CASCADE,
        related_name='violations'
    )

    violation_type = models.CharField(max_length=100)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='OPEN'
    )

    detected_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.worker} - {self.violation_type}"
class Intrusion(models.Model):
    STATUS_CHOICES = [
        ('OPEN', 'Open'),
        ('RESOLVED', 'Resolved'),
    ]

    zone = models.ForeignKey(
        Zone,
        on_delete=models.CASCADE,
        related_name='intrusions'
    )

    camera = models.ForeignKey(
        Camera,
        on_delete=models.CASCADE,
        related_name='intrusions'
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='OPEN'
    )

    detected_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Intrusion - {self.zone.zone_name}"
class Alert(models.Model):
    PRIORITY_CHOICES = [
        ('LOW', 'Low'),
        ('MEDIUM', 'Medium'),
        ('HIGH', 'High'),
        ('CRITICAL', 'Critical'),
    ]

    CHANNEL_CHOICES = [
        ('DASHBOARD', 'Dashboard'),
        ('EMAIL', 'Email'),
        ('VOICE', 'Voice'),
    ]

    alert_type = models.CharField(max_length=100)

    priority = models.CharField(
        max_length=20,
        choices=PRIORITY_CHOICES,
        default='MEDIUM'
    )

    channel = models.CharField(
        max_length=20,
        choices=CHANNEL_CHOICES,
        default='DASHBOARD'
    )

    status = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.alert_type
class Evidence(models.Model):
    SOURCE_TYPES = [
        ('VIOLATION', 'Violation'),
        ('INTRUSION', 'Intrusion'),
    ]

    source_type = models.CharField(
        max_length=20,
        choices=SOURCE_TYPES
    )

    source_id = models.PositiveIntegerField()

    image_path = models.ImageField(
        upload_to='evidence/'
    )

    captured_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.source_type} Evidence"
class AlarmLog(models.Model):
    STATUS_CHOICES = [
        ('ACTIVE', 'Active'),
        ('INACTIVE', 'Inactive'),
    ]

    alert = models.ForeignKey(
        Alert,
        on_delete=models.CASCADE,
        related_name='alarms'
    )

    device_id = models.CharField(max_length=100)

    alarm_type = models.CharField(max_length=100)

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='ACTIVE'
    )

    triggered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.device_id} - {self.alarm_type}"
  
