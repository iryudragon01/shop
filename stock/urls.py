from django.urls import  path
from . import views
app_name='stock'
urlpatterns=[
    path('',views.IndexView,name='index'),
    path('test/',views.DisplayView,name='test'),
    path('topup/',views.TopupView.as_view(),name='topup'),
    path('topup/<int:pk>/',views.DetailtopupView.as_view(),name='detail'),


    ##### Item management
    path('itemcreate/',views.ItemCreateView,name='itemcreate'),
    path('itemlist/',views.ItemListView,name='itemlist'),
    path('itemedit/<int:pk>/',views.ItemEditView,name='itemedit')
]