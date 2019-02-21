from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Tutorial, TutorialCategory, TutorialSeries
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import NewUserForm
# Create your views here.


def single_slug(request, single_slug):
    categories = [c.category_slug for c in TutorialCategory.objects.all()]
    if single_slug in categories:
        matching_series = TutorialSeries.objects.filter(
            tutorial_category__category_slug=single_slug)
        series_urls = {}
        for m in matching_series.all():
            part_one = Tutorial.objects.filter(
                tutorial_series__tutorial_series=m.tutorial_series).earliest("tutorial_published")
            series_urls[m] = part_one.tutorial_slug
        return render(request=request,
                      template_name='main/category.html',
                      context={"tutorial_series": matching_series, "part_ones": series_urls})

    tutorials = [t.tutorial_slug for t in Tutorial.objects.all()]
    if single_slug in tutorials:
        this_tutorial = Tutorial.objects.get(tutorial_slug=single_slug)
        return render(request=request,
                      template_name='main/tutorial.html',
                      context={"tutorial": this_tutorial})

    return HttpResponse(f"'{single_slug}' does not correspond to anything we know of!")


def homepage(request):
    return render(request=request,
                  template_name='main/categories.html',
                  context={"categories": TutorialCategory.objects.all})


def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'new account created for {username}')
            login(request, user)
            return redirect("main:homepage")
        else:
            for msg in form.error_messages:
                messages.error(request, f'{msg}:{form.error_messages[msg]}')
    form = NewUserForm
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
