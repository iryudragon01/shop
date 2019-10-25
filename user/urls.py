
from django.urls import path
from . import  views

app_name = 'user'

urlpatterns = [

    path('', views.LoginView, name='index'),
    path('register/',views.RegisterView,name='register'),
    path('logout',views.LogoutView,name='logout')
]
