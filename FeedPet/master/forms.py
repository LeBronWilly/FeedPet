# master/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Master, Pet


class MasterCreationForm(UserCreationForm):

    username = forms.CharField(label="帳號")
    password1 = forms.CharField(label="密碼", widget=forms.PasswordInput())
    password2 = forms.CharField(label="密碼確認", widget=forms.PasswordInput())

    class Meta(UserCreationForm.Meta):
        model = Master
        fields = ('username', 'password1', 'password2', 'name', 'email', 'gender')


class MasterChangeForm(UserChangeForm):
    class Meta:
        model = Master
        fields = ('name', 'email', 'gender')


class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ('petName', 'petClass', 'petType', 'petGender', 'birthday', 'weight', 'ligation', 'image')
