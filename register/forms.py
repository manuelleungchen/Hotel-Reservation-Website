from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm  # Pre build form
from django import forms
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    telephone = forms.IntegerField()

    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'email', 'telephone', 'password1', 'password2']

