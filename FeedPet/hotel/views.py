from django.shortcuts import render
# from .forms import HotelForm
from itertools import islice
from .models import Hotel
from django.http import HttpResponse
import csv
import collections
# from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

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
    print(unit)

    if request.method == 'POST':
        region = request.POST.get('region')
        star = request.POST.get('star')
        # print(region)
        results = Hotel.objects.filter(district=region).filter(rank=star)
        # print(results[0].district)
        # print(results[0].rank)
        for result in results:
            print(result.district,result.address)
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
    if request.method != 'POST':
        form = HotelForm()
    else:
        form = HotelForm(data=request.POST, files=request.FILES)

        if form.is_valid():
            new_hotel = form.save(commit=False)
            new_hotel.master = request.user
            new_pet.save()

            messages.add_message(request, messages.SUCCESS, '成功登記')
            return HttpResponseRedirect(reverse('hotel:mypet'))
        else:
            messages.add_message(request, messages.ERROR, form.errors)
    return render(request, 'hotel/hotel_favorite.html', locals())
