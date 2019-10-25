from django.contrib.auth.forms import UserCreationForm
from django import forms
from user.models import Account


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(max_length=120, help_text='Required,Add valid email')
    class Meta:
        model = Account
        fields=('email','username','password1','password2')




