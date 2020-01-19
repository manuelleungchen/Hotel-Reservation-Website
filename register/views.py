from django.shortcuts import render, redirect

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm  # Pre build form

from .forms import RegisterForm
# Create your views here.

def register(response):
    user = response.user  # Get the current login user info
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
        return redirect("home")
    else:
        form = RegisterForm()
    return render(response, "register/register.html", {'form': form, 'user': user})