from django.db import models


# Create your models here.
class Account(models.Model):
    email = models.EmailField(max_length=120)
    username = models.CharField(max_length=200)
    password1 = models.CharField(max_length=200)
    password2 = models.CharField(max_length=200)
