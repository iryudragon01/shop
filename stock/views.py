from django.shortcuts import render
from django.views import generic
from .models import Item, Top_up,Last_update
from .iryu.listing import Model2List
from django.template.response import TemplateResponse


# Create your views here.
def IndexView(request,*args,**kwargs):
    # alllist=Model2List.ListItem(Model2List)
    alllist=Model2List.getlogsheet(Model2List,2)
    return TemplateResponse(request,'stock/method_index.html',alllist)











































# view by class
# class IndexView(generic.ListView):
#     template_name = 'stock/index.html'
#     context_object_name = 'latest_all_list'

#     def get_queryset(self):
#         allitem=Item.objects.all()
#         lastdict={}
#         randomval=9
#         for id in allitem:
#             print(id.id)
#             lastdict[id]=randomval
#             randomval+=7

#         Model2List.Logsheet(Model2List,version=2,logdictionary=lastdict)
#         return Model2List.ListItem(Model2List)



class TopupView(generic.CreateView):
    model = Top_up
    fields = ['item', 'volume','worker']
    template_name = 'stock/topup.html'


class DetailtopupView(generic.DetailView):
    model = Top_up
    template_name = 'stock/detail.html'


