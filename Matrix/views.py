from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.views.decorators.http import require_GET
from django.http import HttpRequest
from . import forms
from . import models


def index(request):
    template_kwargs = {
        'messages': models.BlogMessage.get_all_posts()
    }
    return render(request, 'index.html', template_kwargs)


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

    return redirect( login )


def login_p(request):

    # -- GET --
    if request.method == 'GET':
        template_kwargs = { 'form': forms.UserFormLogin() }
        return render(request, 'login.html', template_kwargs)

    # -- POST --
    login_form = forms.UserFormLogin(request.POST)

    if not login_form.is_valid():
        return redirect( login, errors=login_form.errors )

    password = login_form.cleaned_data.get('password')
    username = login_form.cleaned_data.get('username')

    if not models.User.objects.filter(username=username).exists():
        messages.info(request, 'Неверное имя пользователя!')
        return redirect( login_p )

    user = authenticate(request, password=password, username=username)

    if user is None:
        messages.info(request, 'Неверный пароль!')
        return redirect( login_p )

    login(request, user)
    return redirect( index )


def blog_page(request: HttpRequest):

    if request.method == 'GET':
        blog_form = forms.BlogForm()
        from_kwargs = {'form': blog_form}
        return render(request, 'blog_page.html', from_kwargs)

    blog_form = forms.BlogForm(request.POST, sender=request.user)
    if blog_form.is_valid():
        blog_form.save()
        return redirect(index)

    return redirect( blog_page )


@require_GET
def blogs(request: HttpRequest):
    context = {}
    return render(request, 'blog_page.html', context)


def err_404_page(request: HttpRequest, exception):
    context = {'page_title': 404}
    response = render(request, 'index.html', context=context)
    response.status_code = 404
    return response
