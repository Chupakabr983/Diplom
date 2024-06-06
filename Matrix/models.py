from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

class User(AbstractUser):
    pass

# class User(models.Model):
#     user_name = models.CharField(
#         verbose_name='Имя пользователя', max_length=64
#     )
#     email = models.EmailField(
#         verbose_name='Почта', max_length=32
#     )
#     password = models.CharField(
#         verbose_name='Пароль', max_length=64
#     )


# class Blog(models.Model):
#     textarea = models.CharField(
#         verbose_name='Текстовое окно', max_length=5000
#     )


class BlogMessage(models.Model):
    # hidden
    sender = models.ForeignKey('User', on_delete=models.PROTECT)
    likes = models.IntegerField()
    dislikes = models.IntegerField()
    create_time = models.DateTimeField(auto_now_add=True)

    # form
    text = models.CharField(
        verbose_name='Содержание', max_length=128
    )

    def __str__(self):
        return f'<BLOG {self.sender}>'


    @classmethod
    def get_all_posts(cls):
        return list(cls.objects.all())

# python manage.py makemigrations
# python manage.py migrate
