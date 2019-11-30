# master/admin.py
from django.contrib import admin
from .models import Master, Pet

class MasterAdmin(admin.ModelAdmin):
    list_display = ('username', 'name', 'email', 'gender')

class PetAdmin(admin.ModelAdmin):
    list_display = ('master', 'petClass', 'petType', 'petName', 'birthday', 'weight', 'ligation', 'image')
    ordering = ('master',)

admin.site.register(Master, MasterAdmin)
admin.site.register(Pet, PetAdmin)