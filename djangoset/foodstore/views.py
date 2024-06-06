from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.views.decorators.http import require_GET, require_POST
from django.http import HttpRequest
from . import forms
from . import models


def index(request: HttpRequest):
    # return redirect("/home_page/")
    return render(request, 'home_page.html')

def reg_page(request: HttpRequest):

    # -- GET --
    if request.method == 'GET':
        from_kwargs = { 'form': forms.UserFormRegister() }
        return render(request, 'register_page.html', from_kwargs)

    # -- POST --
    reg_form = forms.UserFormRegister(request.POST)

    if not reg_form.is_valid():
        return redirect( reg_page )

    username = reg_form.cleaned_data.get('username')
    if models.User.objects.filter(username=username).exists():
        messages.info(request, 'Имя пользователя занято')
        return redirect( reg_page )

    user = reg_form.save()
    user.set_password( reg_form.cleaned_data.get('password') )
    user.save()

    return redirect( index )

