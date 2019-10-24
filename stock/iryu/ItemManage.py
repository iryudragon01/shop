
from stock.models import Item

class Manage():
    def creteitem(self,request):
        itemexist=Item.objects.filter(name=request.POST.get('name')).count()
        if itemexist==0:
            newitem=Item(name=request.POST.get('name'),
                         price=int(request.POST.get('price')),
                         type=int(request.POST.get('type')),
                         )
            newitem.save()
            return 'success'
        return 'Item is exist'

    def loaditem(self,id):
        item=Item.objects.get(id=id)
        content= {'name': item.name, 'price': item.price, 'type':item.type}
        return content

    def saveedititem(selfself,id,request):
        item=Item.objects.get(id=id)
        item.name=request.POST.get('name')
        item.price=int(request.POST.get('price'))
        item.type=int(request.POST.get('type'))
        item.save()

    def getitemlist(self):
        content={'objects':Item.objects.all()}
        return content
