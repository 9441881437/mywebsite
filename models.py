from django.db import models

# Create your models here.

class FormModels(models.Model):
    username = models.CharField(max_length = 100)
    surname = models.CharField(max_length = 100)
    email = models.CharField(max_length = 100)
    