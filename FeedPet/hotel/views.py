from django.shortcuts import render

# Create your views here.


def hotel(request):
    return render(request, 'hotel.html', locals())


def hoteldetail(request):
    return render(request, 'hotel_detail.html', locals())


def hotel_favorite(request):
    return render(request, 'hotel_favorite.html', locals())