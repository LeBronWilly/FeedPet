from django.urls import path
from . import views

app_name = 'feed'

urlpatterns = [
    # Feed page
    path('', views.feed, name='feed'),

    # Feed recommendation page
    path('feedrecommendation/', views.feedrecommendation,
         name='feedrecommendation'),

    # Feed detail page
    path('feeddetail/', views.feeddetail, name='feeddetail'),

    # # Home page
    # path('', views.index, name='index'),
    # # add a user's face
    # path('addmyface/', views.addmyface, name='addmyface'),
    # # show all user's face
    # path('facelist/', views.facelist, name='facelist'),
    # # recognize face
    # path('whoami/', views.whoami, name='whoami'),
]
