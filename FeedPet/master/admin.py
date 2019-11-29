# master/admin.py
from django.contrib import admin
from .models import Master

class MasterAdmin(admin.ModelAdmin):
    list_display = ['username', 'name', 'email', 'gender']

admin.site.register(Master, MasterAdmin)