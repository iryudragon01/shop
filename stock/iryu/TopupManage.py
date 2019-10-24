from stock.models import Item,Top_up
from django.utils import timezone

class Topupwork:
    def getfooditem(self):
        allitem=Item.objects.all()
        objects=[]
        index=0
        for item in allitem:
            if item.type==3:
                objects.append(item.name)
        return {'objects':objects}

    def create(self,request):
        currenttime=timezone.now()
        allitem=Item.objects.filter(type=3)
        if allitem:
            for item in allitem:
                newitem=Top_up(item=item,volume=request.POST.get(item.name),worker=request.POST.get('worker'),date_log=currenttime)
                newitem.save()