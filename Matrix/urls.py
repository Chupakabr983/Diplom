from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name='index'),
    path("login", views.login_p, name='login'),
    path('reg_page', views.reg_page, name='register'),
    path('blog_page', views.blog_page, name='blog'),
    # path('blog', views.blog_page, name='blog')
]


