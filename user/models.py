from django.db import models


# Create your models here.
class Account(models.Model):
    email = models.EmailField(max_length=120)
    username = models.CharField(max_length=200)
    password1 = models.CharField(max_length=200)
    password2 = models.CharField(max_length=200)


class User_Start_Date(models.Model):
    username = models.CharField(max_length=200)
    date_log = models.DateTimeField()
    version_log = models.PositiveIntegerField(default=0)
    user_superior =models.PositiveIntegerField(default=99)
    temp_row = models.PositiveIntegerField(default=0)

