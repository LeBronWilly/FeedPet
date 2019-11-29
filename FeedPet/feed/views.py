from django.shortcuts import render

# Create your views here.


def feed(request):
    return render(request, 'feed.html', locals())


def feed_recommendation(request):
    return render(request, 'feed_recommendation.html', locals())


def feed_detail(request):
    return render(request, 'feed_detail.html', locals())
