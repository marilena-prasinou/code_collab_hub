from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    age = models.IntegerField(blank=True, null=True)
    country = models.CharField(max_length=100, blank=True)
    residence = models.CharField(max_length=100, blank=True)
