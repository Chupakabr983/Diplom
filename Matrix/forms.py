from django import forms
from . import models


# class RegisterForm(forms.Form):
#     user_name = forms.CharField(label='Имя пользователя', max_length=64)
#     # password = forms.CharField(label='Пароль', max_length=64)
#     password = forms.CharField(label='Пароль', max_length=64, widget=forms.PasswordInput())
#     email = forms.EmailField(label="Email")
#     textarea = forms.CharField(label='Текстовое окно', max_length=5000, widget=forms.Textarea())
#
#
# class EmailForm(forms.Form):
#     email = forms.EmailField(label="Email", max_length=64)


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



class UserFormLogin(forms.Form):
    username = forms.CharField(
        max_length=models.User._meta.get_field('username').max_length,
        label=models.User._meta.get_field('username').verbose_name
    )
    password = forms.CharField(
        max_length=models.User._meta.get_field('password').max_length,
        label=models.User._meta.get_field('password').verbose_name,
        widget=forms.PasswordInput
    )


class BlogForm(forms.ModelForm):
    class Meta:
        model = models.BlogMessage
        fields = ('text', )
        widgets = {
            'text': forms.Textarea()
        }

    def __init__(self, *args, **kwargs):
        attrs = {
            'sender': kwargs.pop('sender', None),
            'likes': kwargs.pop('likes', 0),
            'dislikes': kwargs.pop('dislikes', 0)
        }
        super().__init__(*args, **kwargs)
        for key, value in attrs.items():
            setattr(self.instance, key, value)