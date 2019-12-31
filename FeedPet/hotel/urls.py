from django.urls import path
from . import views
from hotel.views import hotel

app_name = 'hotel'

urlpatterns = [
    # Hotel page
    path('', views.hotel, name='hotel'),

    # Hotel detail page
    path('hotel_detail/<int:postalcode>',
         views.hoteldetail, name='hotel_detail'),

    # Favorite hotel page
    path('hotel_favorite', views.hotel_favorite, name='hotel_favorite'),

    # hoteldata
    path('hoteldata', views.hoteldeta, name='hoteldata'),

    # map
    path('map/<str:district>/', views.map, name='map'),

    # shoe_detail
    # path('show_detail/<str:district>/', views.show_detail, name='show_detail'),
]
