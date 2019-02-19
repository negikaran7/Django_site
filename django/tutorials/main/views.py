from django.shortcuts import render
from django.http import HttpResponse
from .models import Tutorial
from django.contrib.auth.forms import UserCreationForm

# Create your views here.


def homepage(request):
    return render(request, "main/home.html", {"tutorials": Tutorial.objects.all})

def register(request):
    form = UserCreationForm
    return render(request,"main/register.html",{"form":form})