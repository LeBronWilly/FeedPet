from django.urls import path
from django.contrib.auth.views import LoginView
from . import views

app_name = 'master'

urlpatterns = [
    # Home page
    path('', views.index, name='index'),

    # Login page
    path('login/', views.login_view, name='login'),

    # Logout page
    path('logout/', views.logout_view, name='logout'),

    # Registration page
    path('register/', views.register, name='register'),

    # Master profile page
    path('profile/', views.profile, name='profile'),

    # Update master profile page
    path('update_profile/', views.update_profile, name='update_profile'),

    # My Pet page
    path('mypet/', views.mypet, name='mypet'),

    # My Pet detail page
    path('mypet/pet_detail', views.pet_detail, name='pet_detail'),

    # Add Pet page
    path('mypet/add_pet', views.add_pet, name='add_pet'),


]
