from django.db import models
from django.urls import reverse


# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=120)
    price = models.PositiveIntegerField()
    type = models.PositiveSmallIntegerField(choices=[(1, 'ticket'), (2, 'Air Pay'), (3, 'food')])

    def __unicode__(self):
        return self.name

class Last_update(models.Model):   #logsheet
    item=models.ForeignKey(Item,on_delete=models.CASCADE)
    version = models.PositiveIntegerField() # index by version
    Last_stock=models.PositiveIntegerField()
    date_log=models.DateTimeField(auto_now=True)


class Top_up(models.Model): #fillup
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    volume = models.PositiveIntegerField()
    worker = models.CharField(max_length=200)
    date_fillup = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('stock:detail', kwargs={'pk': self.id})

    def __str__(self):
        return self.item.name
    
class Display_Item(models.Model):
    name = models.CharField(max_length=120)