from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import Account


class SignupForm(ModelForm):
    password = forms.PasswordInput()
    confirm_password = forms.PasswordInput()

    class Meta:
        model = Account
        fields = ('first_name', 'last_name', 'email', 'password')
