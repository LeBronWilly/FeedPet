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
]
