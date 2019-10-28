from django.shortcuts import render, redirect
from .models import Item

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
