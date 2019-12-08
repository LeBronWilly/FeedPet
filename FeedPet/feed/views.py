# feed/views.py
from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from master.models import Master, Pet
from .models import Feed, Favor_feed
import datetime
import time
import math
import requests


# function：feed
# author：Zachary Zhuo
# date：2019/12/4
def feed(request):
    username = request.user.username
    try:
        master = Master.objects.get(username=username)
        pets = Pet.objects.filter(master=master)

    except Exception as e:
        messages.add_message(request, messages.WARNING, e)

    return render(request, 'feed/feed.html', locals())


# function：getPet
# author：Zachary Zhuo
# date：2019/12/4
# description：在後端建立ＡＰＩ，回傳JSON format的資料給前端
def getPet(request, petId):
    if request.method == 'GET' and request.is_ajax():
        try:
            pet = Pet.objects.get(id=petId)
        except Exception as e:
            messages.add_message(request, messages.WARNING, e)
        pet_json = {
            'petId': petId,
            'weight': pet.weight,
            'petType': pet.petType,
            'ligation': pet.ligation,
        }
    return JsonResponse(pet_json)


# function：feed_list
# author：Zachary Zhuo
# date：2019/12/6
# description：列出飼料open data以表格呈現簡單資訊
def feed_list(request):
    username = request.user.username
    try:
        master = Master.objects.get(username=username)
        favor_feeds = Favor_feed.objects.filter(master=master)
        feeds = Feed.objects.all()
    except Exception as e:
        messages.add_message(request, messages.WARNING, e)
    return render(request, 'feed/feed_list.html', locals())


# function：feed_detail
# author：Zachary Zhuo
# date：2019/12/6
# description：顯示feed list table所點擊的該feed詳細資訊
def feed_detail(request, feed_id):
    try:
        feed = Feed.objects.get(id=feed_id)
    except Exception as e:
        messages.add_message(request, messages.WARNING, e)

    return render(request, 'feed/feed_detail.html', locals())


# function：import_feed
# author：Zachary Zhuo
# date：2019/12/6
# description：call api 將feed open data資料寫進資料庫
def import_feed(request):
    try:
        feed_api = requests.get(
            "http://data.coa.gov.tw/Service/OpenData/TransService.aspx?UnitId=wxV177kLhEE3")
        feed_json = feed_api.json()
        for feed_obj in feed_json:
            feed = Feed.objects.create(fname=feed_obj["fname"], fitem=feed_obj["fitem"], fmat=feed_obj["fmat"], fnut=feed_obj["fnut"],
                                       fusage1=feed_obj["fusage1"], fusage2=feed_obj["fusage2"], fusage3=feed_obj["fusage3"], flegalname=feed_obj["flegalname"])
            feed.save()

        messages.add_message(request, messages.SUCCESS, '成功更新')
    except Exception as e:
        messages.add_message(request, messages.ERROR, e)
    return HttpResponseRedirect(reverse('feed:feed_list'))


def feed_calculation(request):
    # 貓狗代謝量 ＝ 70 x 體重的0.75次方 x 結紮係數 x 活動係數
    h = 70 * (math.pow(float(request.GET['weight']), 0.75)) * \
        float(request.GET['ligation']) * float(request.GET['type'])
    #
    #
    if request.GET['cal_petclass'] == 'dog':
        h_rawFood_rate = 84 / 64
        h_LyophilizerdRawFood_rate = 84 / 19
        h_cannedFood_rate = 84 / 62
    #
    #
        water = int(request.GET['weight']) * 60
        rawFood = h/h_rawFood_rate
        LyophilizerdRawFood = h/h_LyophilizerdRawFood_rate
        cannedFood = h/h_cannedFood_rate

    else:  # cat
        h_rawFood_rate = 70 / 53
        h_LyophilizerdRawFood_rate = 84 / 15
        h_cannedFood_rate = 70 / 62

        water = int(request.GET['weight']) * 50
        rawFood = h / h_rawFood_rate
        LyophilizerdRawFood = h / h_LyophilizerdRawFood_rate
        cannedFood = h / h_cannedFood_rate
    #
    # return [round(water), round(rawFood), round(LyophilizerdRawFood), round(cannedFood)]
    print({"water": round(water), 'rawFood': round(rawFood), 'LyophilizerdRawFood': round(
        LyophilizerdRawFood), 'cannedFood': round(cannedFood)})
    return JsonResponse({"water": round(water), 'rawFood': round(rawFood), 'LyophilizerdRawFood': round(LyophilizerdRawFood), 'cannedFood': round(cannedFood)})


@login_required
def add_feed_favor(request, master_id, feed_id):
    if request.method == 'GET' and request.is_ajax():
        try:
            master = Master.objects.get(id=master_id)
            feed = Feed.objects.get(id=feed_id)
            if master and feed is not None:
                favor_feed = Favor_feed.objects.create(
                    master=master, feed=feed, created_on=datetime.date.today())
                favor_feed.save()
                favor_feed_json = {
                    'masterId': master_id,
                    'feedId': feed_id,
                }
        except Exception as e:
            messages.add_message(request, messages.WARNING, e)
    else:
        favor_feed_json = {}

    return JsonResponse(favor_feed_json)


def feed_recommendation(request):
    return render(request, 'feed/feed_recommendation.html', locals())


def feeding_record(request):
    return render(request, 'pet/pet_feeding_record.html', locals())
