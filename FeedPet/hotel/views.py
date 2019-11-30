from django.shortcuts import render

# Create your views here.


def hotel(request):
    return render(request, 'hotel/hotel.html', locals())


def hoteldetail(request):
    return render(request, 'hotel/hotel_detail.html', locals())


def hotel_favorite(request):
    return render(request, 'hotel/hotel_favorite.html', locals())
