from stock.models import Item,Top_up,Last_update
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
            newlastupdate=Last_update(item=item,version=version,Last_stock=logdictionary[item],date_log=currenttime)
            newlastupdate.save()

    def getlogsheet(self,version):
        logsheet=Last_update.objects.filter(version=2)    #pull last stock for logsheet filter by version
        fillup=Top_up.objects.filter(date_fillup__gt = logsheet[0].date_log) #pull fillup with date_fillup greater than logsheet
        alldata={
            'logsheet':logsheet,
            'fillup':fillup
        }
        return alldata
