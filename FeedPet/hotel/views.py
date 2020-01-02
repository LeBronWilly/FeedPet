from django.shortcuts import render
from itertools import islice
from .models import Hotel
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from pathlib import Path
import csv
import collections
import geocoder
from geojson import Point, Feature, FeatureCollection


def hoteldeta(request):
    base_path = Path(__file__).parent
    file_path = (base_path / "hotel.csv").resolve()
    with open(file_path, encoding="utf-8", newline="") as csvfile:
        rows = list(csv.reader(csvfile))
        for row in islice(rows, 1, None):
            row = Hotel(hname=row[0], rank=row[1], full_name=row[2], incharge=row[3],
                        phone=row[4], postalcode=row[5], district=row[6], address=row[7], lng=row[8], lat=row[9])
            row.save()
    return render(request, 'hotel/hotel.html', locals())


def hotel(request):
    district = Hotel.objects.all().values('district').distinct()
    coordinate = Hotel.objects.all().values('lat', 'lng')
    if request.method == 'POST':
        chose_district = request.POST.get('chose_district')
        address = request.POST.get('address')
        unit3 = Hotel.objects.filter(district=chose_district, address=address)
        add_list = []
    return render(request, 'hotel/hotel.html', locals())


def map(request, district):
    print('district')
    print(district)
    add_list = []
    if request.method == 'GET' and request.is_ajax():
        try:
            results = Hotel.objects.filter(district=district)
            print("results")
            print(results)
            for result in results:
                print("111111111")
                print((result.id))
                print("2222222222")
                print(Feature(geometry=Point((float(result.lng), float(result.lat))),
                              id=int(result.id), properties={"full_name": result.full_name, "rank": result.rank}))
                add_list.append(Feature(geometry=Point((float(result.lng), float(result.lat))),
                                        id=int(result.id), properties={"full_name": result.full_name, "rank": result.rank}))
            geo_add = FeatureCollection(add_list)
            print("33333333")
            print(geo_add)
        except Exception as e:
            print(e)
    return JsonResponse(geo_add)


def hoteldetail(request, postalcode):
    hotel = Hotel.objects.get(postalcode=postalcode)
    context = {
        'hotel_list': hotel.postalcode
    }
    return render(request, 'hotel/hotel_detail.html', locals())


def hotel_favorite(request):
    return render(request, 'hotel/hotel_favorite.html', locals())
