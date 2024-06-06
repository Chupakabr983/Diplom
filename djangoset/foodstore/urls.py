from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views


urlpatterns = [
    path("", views.index, name='index'),
    path('reg_page', views.reg_page, name='register'),
]