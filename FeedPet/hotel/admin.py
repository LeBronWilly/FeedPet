from django.contrib import admin
from .models import Hotel,Favor_hotel
# from django_google_maps import widgets as map_widgets
# from django_google_maps import fields as map_fields
# Register your models here.
class HotelAdmin(admin.ModelAdmin):
    list_display = ('hname','rank','full_name','incharge','phone','postalcode','district','address')
class FavorHotelAdmin(admin.ModelAdmin):
    list_display = ('hotel','master')
   
admin.site.register(Hotel,HotelAdmin)
admin.site.register(Favor_hotel,FavorHotelAdmin)