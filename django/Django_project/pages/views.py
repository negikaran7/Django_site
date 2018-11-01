from django.shortcuts import render
from django.http import HttpResponse, request

# Create your view here.
def home_view(request,*args,**kwargs):
    # print(args,kwargs)
    # print(request)
    # return HttpResponse("<h1>hello world!</h1>")
    return render(request,"home.html",{})

def contact_view(request,*args,**kwargs):
    return render(request,"contact.html",{})

def about_view(request,*args,**kwargs): 
    my_context={
        "my_text":"this is about !",
        "my_number":1234,
        "my_list":[123,1212,454,125],
        "my_html":"<h1>html code</h1>"
    }
    return render(request,"about.html",my_context)