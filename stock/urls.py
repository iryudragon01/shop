from django.urls import  path
from . import views
app_name='stock'
urlpatterns=[
    path('',views.IndexView,name='index'),
    path('topup/',views.TopupView.as_view(),name='topup'),
    path('topup/<int:pk>/',views.DetailtopupView.as_view(),name='detail')
]