from django.urls import  path
from . import views
app_name='stock'
urlpatterns=[
    path('',views.IndexView,name='index'),
    path('topup/',views.Add_top_up,name='topup'),
    path('itemcreate/',views.ItemCreateView,name='itemcreate'),

]