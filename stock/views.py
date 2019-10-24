from django.shortcuts import render,redirect
from django.views import generic
from .models import Item, Top_up,Last_update,Display_Item
from .iryu.listing import Model2List
from django.template.response import TemplateResponse
from .iryu.ItemManage import Manage
from .iryu.TopupManage import Topupwork


# Create your views here.
def IndexView(request,*args,**kwargs):
    alllist=Model2List.getlogsheet(Model2List,2)
    return TemplateResponse(request,'stock/method_index.html',alllist)



def DisplayView(request):

    return templateResponse(request,'stock/testhtml.html',{})


#########Item management
def ItemCreateView(request):
    content={}
    if request.method=='POST':
        makenewitem=Manage.creteitem(Manage,request)
        content['createnewitem']=makenewitem

    return render(request,'stock/Item/create.html',content)

def ItemListView(request):
    content=Manage.getitemlist(Manage)
    return render(request,'stock/Item/list.html',content)

def ItemEditView(request,pk=None):
    if pk is not None:
        content=Manage.loaditem(Manage,pk)
        if request.method=='POST':
            Manage.saveedititem(Manage,pk,request)
            return ItemListView(request)
        return render(request,'stock/Item/Edit.html',content)
########end Item page
######## topup page

def TopupCreateView(request):
    content=Topupwork.getfooditem(Topupwork)
    if request.method=='POST':
        Topupwork.create(Topupwork,request)
        return TopupListView(request)
    return render(request,'stock/topup/create.html',content)

def TopupListView(request):
    content={}
    return render(request,'stock/topup/list.html',content)







































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


