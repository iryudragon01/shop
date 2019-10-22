from django.shortcuts import render
from django.views import generic
from .models import Item, Top_up


# Create your views here.
class IndexView(generic.ListView):
    template_name = 'stock/index.html'
    context_object_name = 'latest_all_list'

    def get_queryset(self):
        # all = [Item.objects.all(), Top_up.objects.all()]
        itemlist=Item.objects.all()
        myall=[]
        for index in itemlist:
            item={
                'name':index.name,
                'fillup':Top_up.objects.filter(item__pk=index.id)
                }
            myall.append(item)
        return myall 
        # return all


class TopupView(generic.CreateView):
    model = Top_up
    fields = ['item', 'volume','worker']
    template_name = 'stock/topup.html'


class DetailtopupView(generic.DetailView):
    model = Top_up
    template_name = 'stock/detail.html'

