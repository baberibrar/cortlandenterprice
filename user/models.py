from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    USERNAME_FIELD = 'email'
    name = models.CharField(max_length=50, default='Anonymous')
    username = models.CharField(max_length=50, default='Anonymous')
    email = models.EmailField(blank=True, unique=True)
    phone = models.CharField(max_length=20, blank=True, unique=True)
    gender = models.CharField(max_length=10, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    session_token = models.CharField(max_length=10, default=0)
    REQUIRED_FIELDS = ['username']
