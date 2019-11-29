from django.shortcuts import render

# Create your views here.


def feed(request):
    return render(request, 'feed.html', locals())


def feedrecommendation(request):
    return render(request, 'feedrecommendation.html', locals())


def feeddetail(request):
    return render(request, 'feeddetail.html', locals())
