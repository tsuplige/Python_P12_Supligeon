from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    class DEPARTMENT_CHOICES(models.TextChoices):
        COMMERCIAL = 'Commercial'
        SIPPORT = 'Support'
        GESTION = 'Gestion'

    department = models.CharField(
        max_length=20,
        choices=DEPARTMENT_CHOICES.choices,
        default='commercial',
        verbose_name='Département'
    )
