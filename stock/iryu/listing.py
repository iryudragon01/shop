from stock.models import Item,Top_up,Log_Sheet,Display_Item
from django.utils import timezone
class Model2List():
    def ListItem(self):        
        itemlist=Item.objects.all()
        myall={}
        for index in itemlist:
            myall[index.name]=Top_up.objects.filter(item__pk=index.id)
        return myall    

    def Logsheet(self,logdictionary,version):
        currenttime=timezone.now()
        for item in logdictionary:
            newlastupdate=Log_Sheet(item=item, version=version, Last_stock=logdictionary[item], date_log=currenttime)
            newlastupdate.save()

    def getlogsheet(self,version):
        count=Log_Sheet.objects.all().count()
        if count !=0:
            logsheet=Log_Sheet.objects.filter(version=2)    #pull last stock for logsheet filter by version
            fillup=Top_up.objects.filter(date_fillup__gt = logsheet[0].date_log) #pull fillup with date_fillup greater than logsheet
            alldata={
                'logsheet':logsheet,
                'fillup':fillup
            }
        else:
            alldata={}
        return alldata

    def write2Display(self):
        allitem=Item.objects.all()
        for item in allitem:
            newitem=Display_Item(item=item,first=99,latest=150,price_tag=item.price,version=1)
            newitem.save()
