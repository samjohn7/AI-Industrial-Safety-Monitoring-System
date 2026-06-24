from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    ROLE_CHOICES = [
        ('ADMIN', 'Admin / Manager'),
        ('SAFETY_OFFICER', 'Safety Officer / Supervisor'),
    ]

    role = models.CharField(
        max_length=30,
        choices=ROLE_CHOICES,
        default='SAFETY_OFFICER'
    )

    phone_number = models.CharField(
        max_length=20,
        blank=True,
        null=True
    )

    @property
    def is_admin_or_manager(self):
        return self.is_superuser or self.role == 'ADMIN'

    @property
    def is_safety_officer_or_supervisor(self):
        return self.role == 'SAFETY_OFFICER'

    def __str__(self):
        return self.username
