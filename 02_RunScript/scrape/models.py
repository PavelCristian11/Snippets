from django.db import models

# Create your models here.

class Registration(models.Model):
    reg = models.CharField(max_length=7, blank=True, null=False)
