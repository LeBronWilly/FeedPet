# master/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Master


class MasterCreationForm(UserCreationForm):

    username = forms.CharField(label="帳號")
    password1 = forms.CharField(label="密碼", widget=forms.PasswordInput())
    password2 = forms.CharField(label="密碼確認", widget=forms.PasswordInput())

    class Meta(UserCreationForm.Meta):
        model = Master
        fields = ('username', 'password1', 'password2', 'name', 'email', 'gender')
        labels = {
            'username': '帳號',
            'Password': '密碼',
            'Password2': '密碼確認',
            'name': '姓名',
            'email': '信箱',
            'gender': '性別',
        }


class MasterChangeForm(UserChangeForm):

    class Meta:
        model = Master
        fields = ('name', 'email', 'gender')
        labels = {
            'name': '姓名',
            'email': '信箱',
            'gender': '性別',
        }
