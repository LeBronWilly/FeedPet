# master/urls.py
from django.urls import path
from django.contrib.auth.views import LoginView
from . import views

app_name = 'master'

# {% url '<url_name>' %} : 根據在 urls.py 中設定的「name」值，找到對應的 URL

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

    # My pet page
    path('mypet/', views.mypet, name='mypet'),

    # My pet detail page
    path('mypet/pet_detail/<int:pet_id>/', views.pet_detail, name='mypet/pet_detail'),

    # Add pet page
    path('mypet/add_pet/', views.add_pet, name='mypet/add_pet'),

    # Update pet detail page
    path('mypet/update_pet_detail/<int:pet_id>/', views.update_pet_detail, name='mypet/update_pet_detail'),

    # Delete pet
    path('mypet/del_pet/<int:pet_id>/', views.del_pet, name='mypet/del_pet'),

    # feed record
    path('mypet/feeding_record/', views.feeding_record, name='mypet/feeding_record'),
]
