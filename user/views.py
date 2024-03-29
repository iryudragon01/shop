from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.utils import timezone
from .models import User_Start
from stock.models import Log_Sheet
from user.iryu.user_start_script import User_Start_Handle


# Create your views here.

def RegisterView(request):
    content = {}
    if request.POST:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(username=username, password=raw_password)
            login(request, account)

            # set up User start date
            if Log_Sheet.objects.all().count() == 0:
                log_sheet_version = 1
            else:
                log_sheet_version = Log_Sheet.objects.last().version
            new_user = User_Start(username=username, date_log=timezone.now(), version_log=log_sheet_version)
            new_user.save()
            update_user=User_Start.objects.get(username=username)
            User_Start_Handle.edit_user_start(User_Start_Handle,update_user)
            return redirect('user:index')
        else:
            content['registration_form'] = form
            return render(request, 'user/register.html', content)

    else:
        form = UserCreationForm()
        content['registration_form'] = form
    content['submit_value'] = 'Sign Up'
    content['reload'] = 'stop'
    return render(request, 'user/register.html', content)


def LoginView(request):
    if request.user.is_authenticated :
        return redirect('stock:index')  # if authenticated redirect to stock

    content = {}
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('stock:index')
        else:
            form = AuthenticationForm(request.POST)
            content['registration_form'] = form
    else:
        form = AuthenticationForm()
        content['registration_form'] = form
    content['reload'] = 'stop'
    content['submit_value'] = 'Login'
    return render(request, 'user/register.html', content)


def LogoutView(request):
    logout(request)
    return redirect('user:index')
