
from django.urls import path
from . import  views

app_name = 'user'

urlpatterns = [
    path('',views.IndexView,name='index'),
    path('register/',views.RegisterView,name='register'),
    path('login/',views.LoginView,name='login'),
]
