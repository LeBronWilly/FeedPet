# feed/views.py
from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from master.models import Master, Pet
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math



# Create your views here.


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

    if request.POST:
        cal_dog_id = request.POST['choseDog']

        cal_petclass = request.POST['petclass']
        if cal_petclass == 'dog':
            weight = request.POST['dog_weight']
            ligation = request.POST['dog_ligation']
            type = request.POST['dog_type']

        else: #cat
            weight = request.POST['cat_weight']
            ligation = request.POST['cat_ligation']
            type = request.POST['cat_type']
        pet_info = { 'type':type,  'weight':weight, 'ligation':ligation,  'petclass':cal_petclass}

        result = feed_calculation(pet_info)

    # print (type(pets[0].id))


    return render(request, 'feed/feed.html', locals())


# function：getPet
# author：Zachary Zhuo
# date：2019/12/4
# description：在後端建立ＡＰＩ，回傳JSON format的資料給前端
def getPet(request, petId):
    pet = Pet.objects.get(id=petId)
    pet_json = {
        'petId': petId,
        'weight': pet.weight,
        'petType': pet.petType,
        'ligation': pet.ligation,
    }
    return JsonResponse(pet_json)


def feed_recommendation(request):
    return render(request, 'feed/feed_recommendation.html', locals())


def feed_detail(request):
    return render(request, 'deed/feed_detail.html', locals())


def feed_favorite(request):
    return render(request, 'feed/feed_favorite.html', locals())


def feeding_record(request):
    return render(request, 'pet/pet_feeding_record.html', locals())


def feed_list(request):
    return render(request, 'feed/feed_list.html', locals())

def feed_calculation(dict):

    # 貓狗代謝量 ＝ 70 x 體重的0.75次方 x 結紮係數 x 活動係數
    print(dict)
    h = 70 * (math.pow(float(dict['weight']), 0.75)) * float(dict['ligation']) * float(dict['type'])


    if dict['petclass'] == 'dog':
        h_rawFood_rate = 84 / 64
        h_LyophilizerdRawFood_rate = 84 / 19
        h_cannedFood_rate = 84 / 62


        water = int(dict['weight']) * 60
        rawFood = h/h_rawFood_rate
        LyophilizerdRawFood = h/h_LyophilizerdRawFood_rate
        cannedFood = h/h_cannedFood_rate

    else: #cat
        h_rawFood_rate = 70 / 53
        h_LyophilizerdRawFood_rate = 84 / 15
        h_cannedFood_rate = 70 / 62

        water = int(dict['weight']) * 50
        rawFood = h / h_rawFood_rate
        LyophilizerdRawFood = h / h_LyophilizerdRawFood_rate
        cannedFood = h / h_cannedFood_rate

    return [round(water), round(rawFood), round(LyophilizerdRawFood), round(cannedFood)]







