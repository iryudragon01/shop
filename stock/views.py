from django.shortcuts import render, redirect
from .models import Item
from .iryu.ItemManage import Manage
from .iryu.Top_up_link import Top_up_work

from .iryu.display import Display


# Create your views here.
def IndexView(request):
    if not request.user.is_authenticated:
        return redirect('user:index')
    # if login check if item Exist
    else:
        if request.POST:  # if Post Update data
            content = Display.setdisplay(Display,request)
            return render(request,'stock/index.html',content)

        else:  # login and get view list
            if Item.objects.all().count() == 0:
                return redirect('stock:itemcreate')  # send to create item
            else:
                content = Display.getdisplay(Display, request)
                return render(request, 'stock/index.html', content)

#########Item management


########end Item page
######## topup page

def Top_up_Create_View(request):
    content = Top_up_work.getfooditem(Top_up_work)
    if request.method == 'POST':
        Top_up_work.create(Top_up_work, request)
        return redirect('stock:index')
    return render(request, 'stock/topup/create.html', content)

def Add_top_up(request):
    items=Item.objects.filter(type=3)
    if request.POST:
        Top_up_work.set_top_up(Top_up_work,request)
        return redirect('stock:index')

    return render(request,'stock/topup/top_up.html',{'items':items})

