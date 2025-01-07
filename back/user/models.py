from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class CustomUser(AbstractUser):
    last_name = models.CharField(null=True, blank=True),
    first_name = models.CharField(null=True, blank=True),
    created_at = models.DateField(),
    last_login = models.DateField(),
    profile_picture = models.IntegerField(),
