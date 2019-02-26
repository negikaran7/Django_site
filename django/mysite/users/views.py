from django.shortcuts import render,redirect
# from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import NewUserForm,ProfileUpdateForm,UserUpdateForm
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method=="POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'new account created for {username}')
            return redirect("login")
    else:
        form = NewUserForm()
    return render(request,'users/register.html',{"form":form})

@login_required
def profile(request):
    u_form = UserUpdateForm()
    p_form = ProfileUpdateForm()
    context={
        'u_form':u_form,
        'p_form':p_form
    }

    return render(request,'users/profile.html',context)

