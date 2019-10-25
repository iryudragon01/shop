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

    def list(self):
        if Top_up.objects.all().count() >0:
            allitem=Top_up.objects.all()
            count=Item.objects.filter(type=3).count()
            date_log=[]
            name=[]
            contentlist=[]
            for index in range(count+1):
                listitem=allitem[index*count:index*count+count]
                contentlist.append(listitem)
                date_log.append(allitem[index*count].date_log)

            for loop in range(count):
                name.append(allitem[loop].item.name)

            objects=zip(contentlist,date_log)
            content= {'objects': objects,
                      'count':count,
                      'names':name
                      }

            return content


