from django.db import models
from django.urls import reverse


# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=120)
    price = models.PositiveIntegerField()
    type = models.PositiveSmallIntegerField(choices=[(1, 'ticket'), (2, 'Air Pay'), (3, 'food')])

    def __unicode__(self):
        return self.name


class Log_Sheet(models.Model):  # log sheet
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    version = models.PositiveIntegerField()  # index by version
    Last_stock = models.PositiveIntegerField()
    date_log = models.DateTimeField(auto_now=True)
    # store start and and of other sheet for view history
    start_log_version = models.PositiveIntegerField(default=0)
    end_log_version = models.PositiveIntegerField(default=0)
    start_temp_index = models.PositiveIntegerField(default=0)
    end_temp_index = models.PositiveIntegerField(default=0)
    start_top_up_index = models.PositiveIntegerField(default=0)
    end_top_up_index = models.PositiveIntegerField(default=0)
    start_income_index = models.PositiveIntegerField(default=0)
    end_income_index = models.PositiveIntegerField(default=0)
    start_expense_index = models.PositiveIntegerField(default=0)
    end_expense_index = models.PositiveIntegerField(default=0)


class Top_up(models.Model):  # fill up
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    volume = models.PositiveIntegerField()
    worker = models.CharField(max_length=200)
    date_log = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('stock:detail', kwargs={'pk': self.id})

    def __str__(self):
        return self.item.name


class Incomelog(models.Model):
    name = models.CharField(max_length=200)
    volume = models.PositiveIntegerField()
    log_date = models.DateTimeField(auto_now=True)


class Expenselog(models.Model):
    name = models.CharField(max_length=200)
    volume = models.PositiveIntegerField()
    log_date = models.DateTimeField(auto_now=True)


class Tempexpense(models.Model):
    name = models.CharField(max_length=200)
    volume = models.PositiveIntegerField()
    log_date = models.DateTimeField()


#####Display models

class Display_Item(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    first = models.PositiveIntegerField()
    latest = models.PositiveIntegerField()
    # price_tag=models.PositiveIntegerField()     ------->item.price
    price_volume = models.PositiveIntegerField()  # -----> price * volume
    sum_volume = models.PositiveIntegerField()
    version = models.PositiveIntegerField()  # set version for query object and display old log
    # date of log sheet until display object create
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()


class Display_Topup(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    row = models.PositiveIntegerField()
    # volume =models.PositiveIntegerField() -----> item.volume
    # date_log = models.DateTimeField()     -----> item.date_log
    version = models.PositiveIntegerField()  # set version for query object and display old log
    # date of log sheet until display object create
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()


class Display_Income(models.Model):
    item = models.ForeignKey(Incomelog, on_delete=models.CASCADE)
    version = models.PositiveIntegerField()  # set version for query object and display old log
    # date of log sheet until display object create
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()


class Display_Expense(models.Model):
    item = models.ForeignKey(Expenselog, on_delete=models.CASCADE)
    version = models.PositiveIntegerField()  # set version for query object and display old log
    # date of log sheet until display object create
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()


class Desplay_Tempexpense(models.Model):
    item = models.ForeignKey(Tempexpense, on_delete=models.CASCADE)
    version = models.PositiveIntegerField()  # set version for query object and display old log
    # date of log sheet until display object create
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
