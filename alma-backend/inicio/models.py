from django.db import models
from django.utils import timezone
from datetime import timedelta

# Create your models here.
# --- LOGIN ---
class Usuario(models.Model):
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.email
