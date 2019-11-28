# master/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Master

class MasterCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = Master
        fields = ('username',)

class MasterChangeForm(UserChangeForm):

    class Meta:
        model = Master
        fields = ('name', 'email', 'gender')