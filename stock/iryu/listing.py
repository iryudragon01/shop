from stock.models import Item,Top_up,Last_update
class Model2List():
    def ListItem(self):        
        itemlist=Item.objects.all()
        myall=[]
        for index in itemlist:
            item={
                'name':index.name,
                'fillup':Top_up.objects.filter(item__pk=index.id)
                }
            myall.append(item)
        return myall    

    def Logsheet(self,logdictionary,version):
        for item in logdictionary:
            newlastupdate=Last_update(item=item,version=version,Last_stock=logdictionary[item])
            newlastupdate.save()
