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
    return render(request, 'feed/feed.html', locals())


# function：getDog
# author：Zachary Zhuo
# date：2019/12/4
# description：在後端建立ＡＰＩ，回傳JSON format的資料給前端
def getDog(request, dogId):
    dog = Pet.objects.get(id=dogId)
    dog_json = {
        'dogId': dogId,
        'weight': dog.weight,
        'petType': dog.petType,
        'ligation': dog.ligation,
    }
    return JsonResponse(dog_json)


# function：getCat
# author：Zachary Zhuo
# date：2019/12/4
def getCat(request, catId):
    cat = Pet.objects.get(id=catId)
    cat_json = {
        'catId': catId,
        'weight': cat.weight,
        'petType': cat.petType,
        'ligation': cat.ligation,
    }
    return JsonResponse(cat_json)


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

def feed_calculation(request):
    if request.POST:
        petclass = request.POST['petclass']
        weight = request.POST['weight']
        ligation = request.POST['ligation']
        type = request.POST['type']
        print(petclass)
        print('-------')
        print(type)
        if petclass == 'dog':
            petclassvalue = '2'
            if type == '1':
                typevalue = '1.2'
            elif type == '2':
                typevalue = '1.6'
            elif type == '3':
                typevalue = '1.4'
            elif type == '4':
                typevalue = '1'
            elif type == '5':
                typevalue = '2.9'
            elif type == '6':
                typevalue = '1.9'
            elif type == '7':
                typevalue = '1.8'
            elif type == '8':
                typevalue = '2.9'
            elif type == '9':
                typevalue = '4'

            if ligation == 'yes':
                ligationvalue = '0.888'
            else:
                ligationvalue = '1'



        dict = {"typevalue":typevalue,'weight':weight,'ligationvalue':ligationvalue,'petclassvalue':'2'}
        print(dict)
        result = calculation_model(dict)
        print(result)
        return render(request,'feed/feed.html',locals())


def calculation_model(dict):
    chrome_options = webdriver.ChromeOptions()
    prefs = {"profile.managed_default_content_settings.images": 2}
    chrome_options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome('/Volumes/GoogleDrive/我的雲端硬碟/碩士課程/碩一上/軟體工程/期末程式/chromedriver＿m' ,chrome_options = chrome_options)
    driver.implicitly_wait(5)
    driver.get('https://www.dogcatstar.com/%e6%af%9b%e5%b0%8f%e5%ad%a9%e6%af%8f%e6%97%a5%e7%86%b1%e9%87%8f%e9%a3%9f%e9%87%8f%e5%92%8c%e9%9c%80%e6%b0%b4%e9%87%8f%e8%a8%88%e7%ae%97/')

    #選貓狗 0是貓 1是狗
    driver.find_elements_by_class_name('accordion-title')[1].click()

    # 輸入資料(貓是1 狗是2)
    v = dict['petclassvalue']

    # 體重（目標體重）
    # 先清掉預設值
    driver.find_element_by_id('fieldname2_'+ v ).clear()
    # 輸入input
    driver.find_element_by_id('fieldname2_'+ v).send_keys(dict['weight'])

    # 類型
    select = Select(driver.find_element_by_id('fieldname3_'+ v))
    print('fieldname3_'+ v)
    print(dict['typevalue'])
    select.select_by_value(dict['typevalue'])

    # 結紮
    select = Select(driver.find_element_by_id('fieldname10_'+ v))
    select.select_by_value(dict['ligationvalue'])

    #取資料


    time.sleep(1)
    water = driver.find_element_by_id('fieldname7_'+ v).get_attribute('value')
    rawFood = driver.find_element_by_id('fieldname4_'+ v).get_attribute('value')
    LyophilizerdRawFood  =  driver.find_element_by_id('fieldname5_'+ v).get_attribute('value')
    cannedFood = driver.find_element_by_id('fieldname12_'+ v).get_attribute('value')
    print ( [water, rawFood, LyophilizerdRawFood, cannedFood])
    print('=======')
    driver.close()

    return [water,rawFood,LyophilizerdRawFood,cannedFood]





