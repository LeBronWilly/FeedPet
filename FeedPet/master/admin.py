# master/admin.py
from django.contrib import admin
from .forms import MasterCreationForm, MasterChangeForm
from django.contrib.auth.admin import UserAdmin
from .models import Master

class MasterAdmin(UserAdmin):
    add_form = MasterCreationForm
    form = MasterChangeForm
    model = Master
    list_display = ['username', 'name', 'email', 'gender']

admin.site.register(Master, MasterAdmin)