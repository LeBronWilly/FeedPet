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
        fields = ('username', 'password1', 'password1', 'name', 'email', 'gender')
        labels = {'username': '帳號',
                  'password1': '啟用',
                  'password1': '啟用',
                  'name': '姓名',
                  'email': '信箱',
                  'gender': '性別', }


class MasterChangeForm(UserChangeForm):
    class Meta:
        model = Master
        fields = ('name', 'email', 'gender')
        labels = {'name': '姓名',
                  'email': '信箱',
                  'gender': '性別',}


class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ('petName', 'petClass', 'petGender', 'ligation', 'petType', 'weight', 'birthday', 'image')
        labels = {'petName': '名字',
                  'petClass': '類別',
                  'petGender': '性別',
                  'ligation': '是否結紮', 
                  'petType': '活動類型',
                  'weight': '體重',
                  'birthday': '生日',
                  'image': '照片',  }
