from django.urls import path
from . import views

app_name = 'feed'

urlpatterns = [
    # Feed page
    path('feed/', views.feed, name='feed'),

    # # Home page
    # path('', views.index, name='index'),
    # # add a user's face
    # path('addmyface/', views.addmyface, name='addmyface'),
    # # show all user's face
    # path('facelist/', views.facelist, name='facelist'),
    # # recognize face
    # path('whoami/', views.whoami, name='whoami'),
]
