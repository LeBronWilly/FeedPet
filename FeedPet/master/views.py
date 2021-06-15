# master/views.py
from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404, JsonResponse
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from .forms import MasterCreationForm, MasterChangeForm, PetForm
from django.contrib.auth.decorators import login_required

from .models import Master, Pet
from feed.models import Feed, Record

import datetime
import time


# function：index
# author：Zachary Zhuo
# date：2019/11/21
def index(request):
    return render(request, 'index.html', locals())


# function：register
# author：Zachary Zhuo
# date：2019/11/28
def register(request):
    if request.method != 'POST':
        # Display blank registration form.
        form = MasterCreationForm()
    else:
        # Process completed form.
        form = MasterCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # Log the user in and then redirect to home page.
            authenticate_user = authenticate(username=new_user.username,
                                             password=request.POST['password1'])
            messages.add_message(request, messages.SUCCESS, '成功註冊')
            login(request, authenticate_user)
            return HttpResponseRedirect(reverse('master:index'))
        else:
            messages.add_message(request, messages.ERROR, form.errors)

    return render(request, 'registration/register.html', locals())


# function：login_view
# author：Zachary Zhuo
# date：2019/11/30
def login_view(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            messages.add_message(request, messages.SUCCESS, '成功登入')
            return HttpResponseRedirect(reverse('master:index'))

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
            messages.add_message(request, messages.SUCCESS, '成功登入')
            return HttpResponseRedirect(reverse('master:index'))
        else:
            messages.add_message(request, messages.ERROR, '未註冊或帳號密碼輸入錯誤')
    return render(request, 'registration/login.html', locals())


# function：logout
# author：Zachary Zhuo
# date：2019/11/28
def logout_view(request):
    try:
        logout(request)
        messages.add_message(request, messages.SUCCESS, '成功登出')
    except Exception as e:
        messages.add_message(request, messages.ERROR, e)
    return HttpResponseRedirect(reverse('master:index'))


# function：profile
# author：Zachary Zhuo
# date：2019/11/28
@login_required
def profile(request):
    username = request.user.username
    try:
        master = Master.objects.get(username=username)
        pets = Pet.objects.filter(master=master)
    except Exception as e:
        messages.add_message(request, messages.WARNING, e)
    return render(request, 'master/profile.html', locals())


# function：update_profile
# author：Zachary Zhuo
# date：2019/11/30
@login_required
def update_profile(request):
    username = request.user.username
    try:
        master = Master.objects.get(username=username)
    except Exception as e:
        messages.add_message(request, messages.WARNING, e)

    if request.method != 'POST':
        form = MasterChangeForm(instance=master)
    else:
        form = MasterChangeForm(instance=master, data=request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, '成功修改')
        else:
            messages.add_message(request, messages.ERROR, '請確認輸入內容')
            return HttpResponseRedirect(reverse('master:update_profile'))
        return HttpResponseRedirect(reverse('master:profile'))

    return render(request, 'master/update_profile.html', locals())


# function：mypet
# author：Zachary Zhuo
# date：2019/11/30
@login_required
def mypet(request):
    username = request.user.username
    try:
        master = Master.objects.get(username=username)
    except Exception as e:
        master = None
        messages.add_message(request, messages.ERROR, e)
    if master:
        pets = Pet.objects.filter(master=master)

    return render(request, 'pet/mypet.html', locals())


# function：add_pet
# author：Zachary Zhuo
# date：2019/12/1
@login_required
def add_pet(request):
    if request.method != 'POST':
        form = PetForm()
    else:
        form = PetForm(data=request.POST, files=request.FILES)

        if form.is_valid():
            new_pet = form.save(commit=False)
            new_pet.master = request.user
            new_pet.save()

            messages.add_message(request, messages.SUCCESS, '成功登記')
            return HttpResponseRedirect(reverse('master:mypet'))
        else:
            messages.add_message(request, messages.ERROR, form.errors)

    return render(request, 'pet/add_pet.html', locals())


# function：pet_detail
# author：Zachary Zhuo
# date：2019/11/30
@login_required
def pet_detail(request, pet_id):
    try:
        pet = Pet.objects.get(id=pet_id)
        age_year, age_month = calculate_age(pet.birthday)
    except Exception as e:
        pet = None
        messages.add_message(request, messages.ERROR, e)
    if pet.master != request.user:
        raise Http404

    return render(request, 'pet/pet_detail.html', locals())


# function：update_pet_detail
# author：Zachary Zhuo
# date：2019/12/17
@login_required
def update_pet_detail(request, pet_id):
    try:
        pet = Pet.objects.get(id=pet_id)
        dogTypes = ["成犬(室內/中低活動量)", "成犬(中高度活動量)", "需增重成犬(輸入目標體重)", "需減肥成犬(輸入目標體重)",
                    "成長期幼犬(斷奶至4個月)", "成長期幼犬(4個月至10個月)", "懷孕母犬(前42天)", "懷孕母犬(最後21天)", "哺乳母犬"]
        catTypes = ["成貓(室內/低活動量)", "成貓(中高活動量)", "需增重成貓(輸入目標體重)",
                    "需減肥成貓(輸入目標體重)", "成長期幼貓(10個月以內)", "老貓(11歲以上)", "懷孕母貓", "哺乳母貓"]

    except Exception as e:
        pet = None
        messages.add_message(request, messages.ERROR, e)

    if request.method == 'POST':
        petName = request.POST.get('petName')
        weight = request.POST.get('weight')
        ligation = request.POST.get('ligation')
        image = request.FILES.get('image')
        petGender = request.POST.get('petGender')
        birthday = request.POST.get('birthday')
        petType = request.POST.get('type')

        try:
            pet.petName = petName
            pet.weight = weight
            pet.ligation = ligation
            pet.petGender = petGender
            pet.birthday = birthday
            pet.petType = petType
            if image is not None:
                pet.image = image
            pet.save()
        except Exception as e:
            print(e)
            messages.add_message(request, messages.ERROR, '請確認輸入內容')
            return HttpResponseRedirect(reverse('master:mypet/update_pet_detail', args=[pet_id]))

        messages.add_message(request, messages.SUCCESS, '成功修改')
        return HttpResponseRedirect(reverse('master:mypet/pet_detail', args=[pet_id]))

    return render(request, 'pet/update_pet_detail.html', locals())


# function：del_pet
# author：Zachary Zhuo
# date：2019/12/1
@login_required
def del_pet(request, pet_id):
    try:
        pet = Pet.objects.get(id=pet_id)
    except Exception as e:
        messages.add_message(request, messages.WARNING, e)
    if pet:
        pet.delete()
        messages.add_message(request, messages.ERROR, '已刪除' + pet.petName)

    return HttpResponseRedirect(reverse('master:mypet'))


# function：calculate_age
# author：Zachary Zhuo
# date：2019/12/1
def calculate_age(born):
    today = datetime.date.today()
    birthday = born
    age_year = 0
    age_month = 0
    if today.month > birthday.month:
        age_year = today.year - birthday.year
        age_month = today.month - birthday.month

    if today.month < birthday.month:
        age_year = (today.year - birthday.year) - 1
        age_month = 12 - birthday.month + today.month

    if today.month - birthday.month == 0:
        if today.day - birthday.day < 0:
            age_year = (today.year - birthday.year) - 1
            age_month = 11
    if today.year - birthday.year < 0:
        age_year = 0
        age_month = 0
    return age_year, age_month


# function：feeding_record
# author：Zachary Zhuo
# date：2019/12/
# description：
@login_required
def feeding_record(request, pet_id):

    username = request.user.username
    records = Record.objects.filter(pet_id=pet_id)
    feeds = Feed.objects.all()

    try:
        master = Master.objects.get(username=username)
        pets = Pet.objects.get(id=pet_id)
        feeds = Feed.objects.all()
        today = datetime.date.today()

    except Exception as e:
        messages.add_message(request, messages.WARNING, e)

    if request.method == 'POST':
        feed_id = request.POST.get('feed_id')
        feedid = Feed.objects.get(id=feed_id)
        time = request.POST.get('feed_time')
        amount = request.POST.get('feed_amount')
        water = request.POST.get('feed_water')
        record = Record.objects.create(
            pet=pets, feed=feedid, time=time, amount=amount, water=water)

    return render(request, 'pet/feeding_record.html', locals())


# 刪記錄
@login_required
def del_record(request, record_id):
    # delete = Record.objects.get(id=record_id)
    try:
        record = Record.objects.get(id=record_id)
    except Exception as e:
        messages.add_message(request, messages.WARNING, e)
    if record:
        record.delete()
        return JsonResponse({"success": '成功刪除'})
