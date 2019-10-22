from django.shortcuts import render
from django.views import generic
from .models import Item, Top_up


# Create your views here.
class IndexView(generic.ListView):
    template_name = 'stock/index.html'
    context_object_name = 'latest_all_list'

    def get_queryset(self):
        item = Item.objects.all()
        topup = Top_up.objects.all()
        all = [item, topup]

        return all


class TopupView(generic.CreateView):
    model = Top_up
    fields = ['item', 'volume','worker']
    template_name = 'stock/topup.html'


class DetailtopupView(generic.DetailView):
    model = Top_up
    template_name = 'stock/detail.html'

