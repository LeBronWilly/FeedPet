from django.urls import path
from . import views

app_name = 'hotel'

urlpatterns = [
    # Hotel page
    path('', views.hotel, name='hotel'),

    # Hotel detail page
    path('hotel_detail/', views.hoteldetail, name='hotel_detail'),


    # Favorite hotel page
    path('hotel_favorite', views.hotel_favorite, name='hotel_favorite'),

    # # Home page
    # path('', views.index, name='index'),
    # # add a user's face
    # path('addmyface/', views.addmyface, name='addmyface'),
    # # show all user's face
    # path('facelist/', views.facelist, name='facelist'),
    # # recognize face
    # path('whoami/', views.whoami, name='whoami'),
]
