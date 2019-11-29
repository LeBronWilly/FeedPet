from django.urls import path
from django.contrib.auth.views import LoginView
from . import views

app_name = 'master'

urlpatterns = [
    # Home page
    path('', views.index, name='index'),

    # Login page
    path('login/', LoginView.as_view(template_name='registration/login.html'),
         name='login'),

    # Logout page
    path('logout/', views.logout_view, name='logout'),

    # Registration page
    path('register/', views.register, name='register'),

    # Master profile page
    path('profile/', views.profile, name='profile'),
    # My Pet page
    path('mypet/', views.mypet, name='mypet'),

    # My Pet detail page
    path('mypet/pet_detail', views.pet_detail, name='pet_detail'),

    # Add Pet page
    path('mypet/add_pet', views.add_pet, name='add_pet'),

    # Feeding record page
    path('mypet/feeding_record', views.feeding_record, name='feeding_record'),

    # Favorite hotel page
    path('mypet/hotel_favorite', views.hotel_favorite, name='hotel_favorite'),

    # Favorite feed page
    path('mypet/feed_favorite', views.feed_favorite, name='feed_favorite'),
]
