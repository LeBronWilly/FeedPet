from django.shortcuts import render
# from .forms import HotelForm
from itertools import islice
from .models import Hotel
from django.http import HttpResponse
import csv
import collections
import geocoder
# from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def hoteldeta(request):
    with open('/Users/liumeihui/Documents/GitHub/FeedPet/FeedPet/hotel/hotel.csv', encoding="utf-8", newline="") as csvfile:
        rows = list(csv.reader(csvfile))
        for row in islice(rows, 1, None):
            row = Hotel(hname=row[0], rank=row[1], full_name=row[2], incharge=row[3],
                        phone=row[4], postalcode=row[5], district=row[6], address=row[7],lng=row[8],lat=row[9])
            row.save()
    return render(request, 'hotel/hotel.html', locals())

def hotel(request):
    unit = Hotel.objects.all().values('district').distinct()
    unit1 = Hotel.objects.all().values('rank').distinct()
    unit2=Hotel.objects.all().values('address').distinct()
    # hotel = Hotel.objects.filter(address=address)
    if request.method == 'POST':
        district=request.POST.get('region')
        address=request.POST.get('address')
        unit3 = Hotel.objects.filter(district=region).filter(address=address)
        print(unit3)
        print("@@@@@@@")
        for unitaddress in unit3:
            print(unitaddress.address)               
    if request.method == 'POST':
        region = request.POST.get('region')
        star = request.POST.get('star')
        results = Hotel.objects.filter(district=region).filter(rank=star)
        for result in results:
            print(result.district,result.rank)
    # g = geocoder.google("1403 Washington Ave, New Orleans, LA 70130")
    # g = geocoder.arcgis(u"臺北市大安區和平東路2段20之1號")
    # print(g.latlng)
    return render(request, 'hotel/hotel.html', locals())

def hoteldetail(request,postalcode):
    hotel = Hotel.objects.get(id=postalcode)
    context = {
        'hotel_list': hotel.postalcode
        # ,hotel.hname,hotel.rank,hotel.full_name,hotel.incharge,hotel.phone,hotel.district,
        # hotel.address,hotel.master_hotel
    }
    return render(request, 'hotel/hotel_detail.html', locals())

def hotel_favorite(request):
    return render(request, 'hotel/hotel_favorite.html', locals())
