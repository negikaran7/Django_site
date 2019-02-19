from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Tutorial
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
# Create your views here.


def homepage(request):
    return render(request,
                  "main/home.html",
                  {"tutorials": Tutorial.objects.all})


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'new account created for {username}')
            login(request, user)
            return redirect("main:homepage")
        else:
            for msg in form.error_messages:
                messages.error(request, f'{msg}:{form.error_messages[msg]}')

    form = UserCreationForm
    return render(request,
                  "main/register.html",
                  {"form": form})


def logout_request(request):
    logout(request)
    messages.info(request, f'Logged out successfully!')
    return redirect("main:homepage")


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f'logged in as {username}')
                return redirect("main:homepage")
            else:
                messages.error(request, f'invalid username or password')
        else:
            messages.error(request, f'invalid username or password')

    form = AuthenticationForm()
    return render(request,
                  "main/login.html",
                  {"form": form})
