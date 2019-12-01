# master/views.py
from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from .forms import MasterCreationForm, MasterChangeForm, PetForm
from django.contrib.auth.decorators import login_required

from .models import Master, Pet


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
            messages.add_message(request, messages.ERROR, '請確認輸入內容')

    return render(request, 'pet/add_pet.html', locals())


# function：pet_detail
# author：Zachary Zhuo
# date：2019/11/30
@login_required
def pet_detail(request, pet_id):
    try:
        pet = Pet.objects.get(id=pet_id)
    except Exception as e:
        pet = None
        messages.add_message(request, messages.ERROR, e)
    if pet.master != request.user:
        raise Http404

    return render(request, 'pet/pet_detail.html', locals())


# function：update_pet_detail
# author：Zachary Zhuo
# date：2019/12/1
@login_required
def update_pet_detail(request, pet_id):
    try:
        pet = Pet.objects.get(id=pet_id)
    except Exception as e:
        pet = None
        messages.add_message(request, messages.ERROR, e)

    if request.method == 'POST':
        petName = request.POST.get('petName')
        weight = request.POST.get('weight')
        ligation = request.POST.get('ligation')
        # image = request.POST.FILES.get('image')

        try:
            pet.petName = petName
            pet.weight = weight
            pet.ligation = ligation
            # pet.image = image
            pet.save()
        except Exception as e:
            print(e)
            messages.add_message(request, messages.ERROR, '請確認輸入內容')

        messages.add_message(request, messages.SUCCESS, '成功修改')

        #     return HttpResponseRedirect(reverse('master:mypet/update_pet_detail/', args=[pet.id]))
        # return HttpResponseRedirect(reverse('master:mypet/pet_detail/', args=[pet.id]))

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
