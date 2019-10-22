from django.shortcuts import render
from django.views import generic
from .models import Item, Top_up
from .iryu.listing import Model2List


# Create your views here.
class IndexView(generic.ListView):
    template_name = 'stock/index.html'
    context_object_name = 'latest_all_list'

    def get_queryset(self):
        return Model2List.ListItem(Model2List)



class TopupView(generic.CreateView):
    model = Top_up
    fields = ['item', 'volume','worker']
    template_name = 'stock/topup.html'


class DetailtopupView(generic.DetailView):
    model = Top_up
    template_name = 'stock/detail.html'

