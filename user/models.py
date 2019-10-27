from django.db import models


# Create your models here.
class User_Start(models.Model):
    username = models.CharField(max_length=200)
    user_superior = models.PositiveIntegerField(default=99)  # 1 is highest 99 is lowest
    date_log = models.DateTimeField()
    version_log = models.PositiveIntegerField(default=0)
    version_top_up = models.PositiveIntegerField(default=0)
    version_temp = models.PositiveIntegerField(default=0)  # if 0 is not load temp sheet
    version_income = models.PositiveIntegerField(default=0)
    version_expense = models.PositiveIntegerField(default=0)

