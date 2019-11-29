# master/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Master

class MasterCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = Master
        fields = UserCreationForm.Meta.fields + ('name', 'email', 'gender')

class MasterChangeForm(UserChangeForm):

    class Meta:
        model = Master
        fields = ('name', 'email', 'gender')