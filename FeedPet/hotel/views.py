from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import Hotel, Favor_hotel
from master.models import Master

from itertools import islice
import datetime
from pathlib import Path
import csv
import collections
import geocoder
from geojson import Point, Feature, FeatureCollection
from pathlib import Path


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
    hotels = Hotel.objects.all().values('district').distinct()
    coordinate = Hotel.objects.all().values('lat', 'lng')
    if request.method == 'POST':
        chose_district = request.POST.get('chose_district')
        address = request.POST.get('address')
        unit3 = Hotel.objects.filter(district=chose_district, address=address)
        add_list = []
    return render(request, 'hotel/hotel.html', locals())


def map(request, district):
    add_list = []
    if request.method == 'GET' and request.is_ajax():
        try:
            results = Hotel.objects.filter(district=district)
            print('results')
            print(results)
            for result in results:
                print('result.id')
                print(result.id)
                add_list.append(Feature(geometry=Point((float(result.lng), float(result.lat))),
                                        id=int(result.id), properties={"full_name": result.full_name, "address": result.address, "phone": result.phone, "incharge": result.incharge, "rank": result.rank, "id": int(result.id)}))
            geo_add = FeatureCollection(add_list)
            print(geo_add)
        except Exception as e:
            print(e)
    return JsonResponse(geo_add)


def hoteldetail(request, hotel_id):
    username = request.user.username
    try:
        master = Master.objects.get(username=username)
        hotel = Hotel.objects.get(id=hotel_id)
        favor_hotel = Favor_hotel.objects.filter(master=master, hotel=hotel)
    except Exception as e:
        messages.add_message(request, messages.WARNING, e)
    return render(request, 'hotel/hotel_detail.html', locals())


# function：add_hotel_favor
# author：Zachary Zhuo
# date：2020/1/3
# description：加入我的最愛旅館
@login_required
def add_hotel_favor(request, master_id, hotel_id):
    if request.method == 'GET' and request.is_ajax():
        try:
            master = Master.objects.get(id=master_id)
            hotel = Hotel.objects.get(id=hotel_id)
            if master and hotel is not None:
                if not Favor_hotel.objects.filter(master=master, hotel=hotel):
                    favor_hotel = Favor_hotel.objects.create(
                        master=master, hotel=hotel, created_on=datetime.date.today())
                    favor_hotel.save()
                    favor_hotel_json = {
                        'status': True,
                        'masterId': master_id,
                        'hotelId': hotel_id,
                    }
                    return JsonResponse(favor_hotel_json)
        except Exception as e:
            print(e)
    favor_hotel_json = {
        'status': False
    }
    return JsonResponse(favor_hotel_json)


# function：del_hotel_favor
# author：Zachary Zhuo
# date：2020/1/3
# description：刪除我的最愛旅館
@login_required
def del_hotel_favor(request, master_id, hotel_id):
    if request.method == 'GET' and request.is_ajax():
        try:
            master = Master.objects.get(id=master_id)
            hotel = Hotel.objects.get(id=hotel_id)
            if master and hotel is not None:
                favor_hotel = Favor_hotel.objects.filter(master=master, hotel=hotel)
                if favor_hotel:
                    favor_hotel.delete()
                    favor_hotel_json = {
                        'status': True,
                        'masterId': master_id,
                        'hotelId': hotel_id,
                    }
                    return JsonResponse(favor_hotel_json)
        except Exception as e:
            print(e)
    favor_hotel_json = {
        'status': False
    }
    return JsonResponse(favor_hotel_json)


# function：my_favor_feed
# author：Zachary Zhuo
# date：2020/1/2
# description：列出我的最愛旅館
@login_required
def my_favor_hotel(request):
    username = request.user.username
    try:
        master = Master.objects.get(username=username)
        favor_hotels = Favor_hotel.objects.filter(master=master)
    except Exception as e:
        messages.add_message(request, messages.WARNING, e)
    return render(request, 'hotel/my_favor_hotel.html', locals())
