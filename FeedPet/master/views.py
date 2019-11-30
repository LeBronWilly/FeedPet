# master/views.py
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from .forms import MasterCreationForm, MasterChangeForm
from django.contrib.auth.decorators import login_required

from .models import Master


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
            messages.add_message(request, messages.ERROR, '請確認輸入內容')

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
    except Exception as e:
        messages.add_message(request, messages.WARNING, e)
    return render(request, 'master/profile.html', locals())


# function：updateProfile
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


def mypet(request):
    return render(request, 'master/mypet.html', locals())


def pet_detail(request):
    return render(request, 'pet/pet_detail.html', locals())


def add_pet(request):
    return render(request, 'pet/add_pet.html', locals())
