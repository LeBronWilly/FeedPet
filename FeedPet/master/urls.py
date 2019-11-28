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

    # My Pet page
    path('mypet/', views.mypet, name='mypet'),

    # My Pet detail page
    path('mypet/petdetail', views.petdetail, name='petdetail'),

    # Add Pet page
    path('mypet/addpet', views.addpet, name='addpet'),


]
