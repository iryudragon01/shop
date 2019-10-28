from stock.models import Item,Top_up
from django.utils import timezone
from user.models import User_Start

class data2view:
    def top_up(self,request):
        items = Item.objects.filter(type=3)
        current_time = timezone.now()
        print('hello for item',items.count())
        for item in items:
            new_top_up = Top_up(
                item=item,
                volume=request.POST.get(item.name),
                worker=request.user,
                date_log=current_time)
            new_top_up.save()
            print(new_top_up.item.name,'   volume  ',new_top_up.volume)

    def edit(self,request,pk):
        if 'DELETE' in request.POST:
            del_top_up = Top_up.objects.get(id=pk)
            del_top_up.delete()
        else:
            update_top_up = Top_up.objects.get(id=pk)
            update_top_up.volume = int(request.POST.get('volume'))
            update_top_up.save()

    def list(self,request):
        worker=User_Start.objects.get(username=request.user)
        top_ups = Top_up.objects.filter(date_log__gt=worker.date_log)
        content = {'top_ups': top_ups}
        return content
