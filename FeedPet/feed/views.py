from django.shortcuts import render

# Create your views here.


def feed(request):
    return render(request, 'feed/feed.html', locals())


def feed_recommendation(request):
    return render(request, 'feed/feed_recommendation.html', locals())


def feed_detail(request):
    return render(request, 'deed/feed_detail.html', locals())


def feed_favorite(request):
    return render(request, 'feed/feed_favorite.html', locals())


def feeding_record(request):
    return render(request, 'pet/pet_feeding_record.html', locals())
