#from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(models.Model):
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=256)
  

    def __str__(self):
        return self.username