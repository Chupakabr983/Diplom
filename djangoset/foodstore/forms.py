from django import forms
from . import models


class UserFormRegister(forms.ModelForm):
    class Meta:
        model = models.User
        fields = ('username', 'email', 'password')
        widgets = {
            'password': forms.PasswordInput()
        }
        labels = {
            'username': 'Имя Пользователя',
            'email': 'Электронная Почта',
            'password': 'Пароль'
        }