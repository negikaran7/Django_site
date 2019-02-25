from django.shortcuts import render
from django.http import HttpResponse

posts=[
    {
        'author':'karan',
        'title':'Blog post 1',
        'content':'first post content',
        'date_posted':'Feb 25, 2019'
    },
    {
        'author':'optimus',
        'title':'Blog post 2 ',
        'content':'second post content',
        'date_posted':'Feb 25, 2019'
    }
]

def home(request):
    context={
        'posts':posts
    }
    return render(request,'blog/home.html',context)

def about(request):
    return render(request,'blog/about.html')