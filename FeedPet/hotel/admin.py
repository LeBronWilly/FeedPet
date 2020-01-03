from django.contrib import admin
from .models import Hotel,Favor_hotel

class HotelAdmin(admin.ModelAdmin):
    list_display = ('hname','rank','full_name','incharge','phone','postalcode','district','address', 'lng', 'lat')

class FavorHotelAdmin(admin.ModelAdmin):
    list_display = ('master', 'hotel', 'created_on')

admin.site.register(Hotel,HotelAdmin)
admin.site.register(Favor_hotel,FavorHotelAdmin)