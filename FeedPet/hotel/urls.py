from django.urls import path
from . import views
from hotel.views import hotel

app_name = 'hotel'

urlpatterns = [
    # Hotel page
    path('', views.hotel, name='hotel'),

    # import hotel data
    path('import_hotel/', views.import_hotel, name='import_hotel'),

    # Hotel detail page
    path('hotel_detail/<int:hotel_id>/',
         views.hoteldetail, name='hotel_detail'),

    # [api] map get hotel district
    path('map/<str:district>/', views.map, name='map'),

    # [api] add favorite hotel
    path('add_hotel_favor/<int:master_id>/<int:hotel_id>/', views.add_hotel_favor, name='add_hotel_favor'),

    # [api] del favorite hotel
    path('del_hotel_favor/<int:master_id>/<int:hotel_id>/', views.del_hotel_favor, name='del_hotel_favor'),

    # my favorite hotels
    path('my_favor_hotel/', views.my_favor_hotel,name='my_favor_hotel'),
]
