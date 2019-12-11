# feed/urls.py
from django.urls import path
from . import views

app_name = 'feed'

urlpatterns = [
    # Feed page
    path('', views.feed, name='feed'),

    # [api] Get pet by id
    path('getPet/<int:petId>', views.getPet, name='getPet'),

    # [api] Get feed calculation
    path('feed_calculation/',views.feed_calculation, name = 'feed_calcultion'),

    # Import feed detail to DB
    path('import_feed/', views.import_feed, name='import_feed'),

    # Total Feed list page
    path('feed_list/', views.feed_list, name='feed_list'),

    # Feed detail page
    path('feed_list/feed_detail/<int:feed_id>/', views.feed_detail, name='feed_list/feed_detail'),

    path('add_feed_favor/<int:master_id>/<int:feed_id>/', views.add_feed_favor, name='add_feed_favor'),

    path('feed_recommendation/', views.feed_recommendation,name='feed_recommendation'),

    path('feeding_record/', views.feeding_record, name='feeding_record'),
]
