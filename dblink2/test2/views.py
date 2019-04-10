from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import *
# Create your views here.


def test2_home(request):
    user = request.user
    if user.is_authenticated and user.test_type() != 2:
        logout(request)
    if not user.is_authenticated:
        user = 'None'

    context = {'user': user, }
    template = 'test2/test2_home.html'
    return render(request, template, context)


def test2_object_manage(request, user_id):
    if request.method == "POST":
        object_create_form = Object2CreationForm(request.POST)
        if object_create_form.is_valid():
            object_create_form.save()
            return redirect('test2:test2_object_manage', user_id)
    else:
        object_create_form = Object2CreationForm()

    context = {'object_create_form': object_create_form,
               'user_id': user_id,
               'all_objects': Object2.objects.all(), }
    template = 'test2/object_create.html'
    return render(request, template, context)
