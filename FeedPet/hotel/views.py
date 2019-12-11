from django.shortcuts import render
# from .forms import HotelForm
from itertools import islice
from .models import Hotel
# from django.http import HttpResponse, Http404
import csv
import collections

def hoteldeta(request):
    with open('/Users/liumeihui/Documents/GitHub/FeedPet/FeedPet/hotel/hotel.csv', encoding="utf-8", newline="") as csvfile:
        rows = list(csv.reader(csvfile))
        for row in islice(rows, 1, None):
            row = Hotel(hname=row[0], rank=row[1], full_name=row[2], incharge=row[3],
                        phone=row[4], postalcode=row[5], district=row[6], address=row[7])
            row.save()
    return render(request, 'hotel/hotel.html', locals())

def hotel(request):
    unit = Hotel.objects.all().values('district').distinct()
    unit1 = Hotel.objects.all().values('rank').distinct()
    return render(request, 'hotel/hotel.html', locals())

def hoteldetail(request):
    try:
        p = request.GET['hotel_detail.html']
    except:
        p = None
    # template = get_template('hotel_detail.html')
    # request_context = RequestContext(request)
    # request_context.path.(locals())
    # html = template.render(request_context)
    return render(request, 'hotel/hotel_detail.html', locals())

def hotel_favorite(request):
    return render(request, 'hotel/hotel_favorite.html', locals())
