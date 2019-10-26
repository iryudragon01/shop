from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


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