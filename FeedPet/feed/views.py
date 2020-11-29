# feed/views.py
from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from master.models import Master, Pet
from .models import Feed, Favor_feed, query_feed_by_args

import datetime
import random
import math
import requests

from rest_framework import viewsets, status
from rest_framework.response import Response
from feed.serializers import FeedSerializer


# function：feed
# author：Zachary Zhuo
# date：2019/12/4
def feed(request):
    username = request.user.username
    try:
        if username:
            master = Master.objects.get(username=username)
            pets = Pet.objects.filter(master=master)
    except Exception as e:
        messages.add_message(request, messages.WARNING, e)
    return render(request, 'feed/feed.html', locals())


# function：getPet
# author：Zachary Zhuo
# date：2019/12/4
# description：在後端建立ＡＰＩ，回傳JSON format的資料給前端
@login_required
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
    try:
        # favor_feeds = Favor_feed.objects.filter(master=master)
        # print(favor_feeds.feed)
        feeds = Feed.objects.all()
        if not feeds:
            raise ValueError('請確認是否匯入飼料')
    except Exception as e:
        messages.add_message(request, messages.WARNING, e)
    return render(request, 'feed/feed_list.html', locals())


# function：FeedViewSet
# author：Zachary Zhuo
# date：2019/12/19
# description：繼承rest api的list功能
class FeedViewSet(viewsets.ModelViewSet):
    queryset = Feed.objects.all()
    serializer_class = FeedSerializer

    def list(self, request, **kwargs):
        try:
            feed = query_feed_by_args(**request.query_params)
            serializer = FeedSerializer(feed['items'], many=True)
            result = dict()
            result['data'] = serializer.data
            result['draw'] = feed['draw']
            result['recordsTotal'] = feed['total']
            result['recordsFiltered'] = feed['count']
            return Response(result, status=status.HTTP_200_OK, template_name=None, content_type=None)
        except Exception as e:
            return Response(e, status=status.HTTP_404_NOT_FOUND, template_name=None, content_type=None)


# function：feed_detail
# author：Zachary Zhuo
# date：2019/12/20
# description：顯示feed list table所點擊的該feed詳細資訊
def feed_detail(request, feed_id):
    username = request.user.username
    try:
        master = Master.objects.get(username=username)
        feed = Feed.objects.get(id=feed_id)
        favor_feed = Favor_feed.objects.filter(master=master, feed=feed)
    except Exception as e:
        messages.add_message(request, messages.WARNING, e)
    return render(request, 'feed/feed_detail.html', locals())


# function：import_feed
# author：Zachary Zhuo
# date：2019/12/19
# description：call api 將feed open data資料寫進資料庫
def import_feed(request):
    try:
        feed_api = requests.get(
            "https://data.coa.gov.tw/Service/OpenData/TransService.aspx?UnitId=wxV177kLhEE3")
        feed_json = feed_api.json()
        for feed_obj in feed_json:
            if feed_obj["fname"] == "" or feed_obj["fitem"] == "" or feed_obj["fmat"] == "" or feed_obj["fnut"] == "" or feed_obj["fusage1"] == "" or feed_obj["fusage2"] == "" or feed_obj["fusage3"] == "" or feed_obj["flegalname"] == "":
                pass
            else:
                is_feed = Feed.objects.filter(fname=feed_obj["fname"])
                if not is_feed:
                    feed = Feed.objects.create(fname=feed_obj["fname"], fitem=feed_obj["fitem"], fmat=feed_obj["fmat"], fnut=feed_obj["fnut"],
                                            fusage1=feed_obj["fusage1"], fusage2=feed_obj["fusage2"], fusage3=feed_obj["fusage3"], flegalname=feed_obj["flegalname"])
                    feed.save()
        messages.add_message(request, messages.SUCCESS, '成功更新')
    except Exception as e:
        messages.add_message(request, messages.ERROR, e)
    return HttpResponseRedirect(reverse('feed:feed_list'))


# function：feed_calculation
# author：
# date：
# description：計算某寵物的推薦餵食量
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


# function：add_feed_favor
# author：Zachary Zhuo
# date：2019/12/20
# description：加入我的最愛飼料
@login_required
def add_feed_favor(request, master_id, feed_id):
    if request.method == 'GET' and request.is_ajax():
        try:
            master = Master.objects.get(id=master_id)
            feed = Feed.objects.get(id=feed_id)
            if master and feed is not None:
                if not Favor_feed.objects.filter(master=master, feed=feed):
                    favor_feed = Favor_feed.objects.create(
                        master=master, feed=feed, created_on=datetime.date.today())
                    favor_feed.save()
                    favor_feed_json = {
                        'status': True,
                        'masterId': master_id,
                        'feedId': feed_id,
                    }
                    return JsonResponse(favor_feed_json)
        except:
            pass
    favor_feed_json = {
        'status': False
    }
    return JsonResponse(favor_feed_json)


# function：del_feed_favor
# author：Zachary Zhuo
# date：2019/12/20
# description：刪除我的最愛飼料
@login_required
def del_feed_favor(request, master_id, feed_id):
    if request.method == 'GET' and request.is_ajax():
        try:
            master = Master.objects.get(id=master_id)
            feed = Feed.objects.get(id=feed_id)
            if master and feed is not None:
                favor_feed = Favor_feed.objects.filter(master=master, feed=feed)
                if favor_feed:
                    favor_feed.delete()
                    favor_feed_json = {
                        'status': True,
                        'masterId': master_id,
                        'feedId': feed_id,
                    }
                    return JsonResponse(favor_feed_json)
        except:
            pass
    favor_feed_json = {
        'status': False
    }
    return JsonResponse(favor_feed_json)


# function：feed_recommendation
# author：
# date：
# description：隨便推薦十個飼料
def feed_recommendation(request):
    feed_list = []
    try:
        feeds = Feed.objects.all()
        feeds_count = Feed.objects.count() - 1
        rendom_i = random.sample(range(0, feeds_count), 10)
        for i in rendom_i:
            feed_list.append(feeds[i])
    except Exception as e:
        messages.add_message(request, messages.ERROR, '請確認是否匯入飼料')
    return render(request, 'feed/feed_recommendation.html', locals())


# function：my_favor_feed
# author：Zachary Zhuo
# date：2019/12/22
# description：列出我的最愛飼料
@login_required
def my_favor_feed(request):
    username = request.user.username
    try:
        master = Master.objects.get(username=username)
        favor_feeds = Favor_feed.objects.filter(master=master)
    except Exception as e:
        messages.add_message(request, messages.WARNING, e)
    return render(request, 'feed/my_favor_feed.html', locals())
