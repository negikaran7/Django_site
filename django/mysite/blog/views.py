from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>welcome to blog homepage</h1>")

def about(request):
    return HttpResponse("<h1>welcome to blog aboutpage</h1>")