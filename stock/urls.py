from django.urls import  path
from . import views
app_name='stock'
urlpatterns=[
    path('',views.IndexView,name='index'),
    path('test/',views.DisplayView,name='test'),
    path('topup/',views.Add_top_up,name='topup'),
    path('topup/<int:pk>/',views.DetailtopupView.as_view(),name='detail'),


    ##### Item management
    path('itemcreate/',views.ItemCreateView,name='itemcreate'),
    path('itemlist/',views.ItemListView,name='itemlist'),
    path('itemedit/<int:pk>/',views.ItemEditView,name='itemedit'),
    ####  topup management
    path('topupcreate/',views.TopupCreateView,name='topupcreate'),
    path('topuplist/',views.TopupListView,name='topuplist')

]