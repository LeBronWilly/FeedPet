from django.contrib import admin

# Register your models here.
from .models import Hotel

admin.site.register(Hotel)

from .models import Favor_hotel

admin.site.register(Favor_hotel)