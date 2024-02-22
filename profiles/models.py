# Create your models here.
from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Add other fields as needed

    class Meta:
        verbose_name = 'User Profile'
        verbose_name_plural = 'User Profiles'
