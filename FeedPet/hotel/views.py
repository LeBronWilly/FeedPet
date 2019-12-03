from django.shortcuts import render
import csv
# Create your views here.

def hoteldetail(request):
   with open('/Users/liumeihui/Documents/GitHub/FeedPet/FeedPet/hotel/hotel.csv') as hotelfile:
    rows = csv.DictReader(hotelfile)  
    for row in rows:
        return render(request, 'hotel/hoteldetail.html', locals())

def hotel(request):
    return render(request, 'hotel/hotel.html', locals())


def hotel_favorite(request):
    return render(request, 'hotel/hotel_favorite.html', locals())
