from django.urls import  path
from . import views
from stock.iryu.Item import views as item_views
app_name='stock'
urlpatterns=[
    path('',views.IndexView,name='index'),
    path('topup/',views.Add_top_up,name='topup'),


    # Item
    path('item/create/',item_views.CreateView,name='itemcreate'),
    path('item/list/',item_views.ListView,name='itemlist'),
    path('item/edit/<int:pk>/',item_views.EditView,name='itemedit')

]