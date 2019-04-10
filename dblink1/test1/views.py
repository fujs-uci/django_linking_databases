from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from test2.models import *
from .forms import *
# Create your views here.


def test1_home(request):
    user = request.user
    if user.is_authenticated and user.test_type() != 1:
        logout(request)
    if not user.is_authenticated:
        user = 'None'

    search_form = SearchObject2()
    search_request = request.GET.get('name')

    if search_request:
        if search_request is None or search_request.strip() == '':
            return redirect('test1:test1_home')
        context = {'query': Object2.objects.filter(name__contains=search_request).all(), }
        template = 'test1/test1_result.html'
        return render(request, template, context)
    else:
        if search_request is not None:
            return redirect('test1:test1_home')

    context = {'user': user,
               'search_form': search_form, }
    template = 'test1/test1_home.html'
    return render(request, template, context)


def test1_signup(request):
    if request.method == "POST":
        signup_form = User1CreationForm(request.POST)
        if signup_form.is_valid():
            signup_form.save()
            email = signup_form.cleaned_data.get('email')
            raw_password = signup_form.cleaned_data.get('password1')
            User1.objects.get(email=email).set_test_type(1)
            user = authenticate(email=email, password=raw_password)
            login(request, user)
            return redirect('test1:test1_home')

    else:
        signup_form = User1CreationForm()

    context = {'signup_form': signup_form, }
    template = 'test1/signup.html'
    return render(request, template, context)
