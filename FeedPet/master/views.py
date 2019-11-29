# master/views.py
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from .forms import MasterCreationForm, MasterChangeForm
from django.contrib.auth.decorators import login_required

from .models import Master
# from .forms import TopicForm, EntryForm
# Create your views here.


def index(request):
    return render(request, 'index.html', locals())


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
            login(request, authenticate_user)
            return HttpResponseRedirect(reverse('master:index'))

    return render(request, 'registration/register.html', locals())


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('master:index'))


@login_required
def profile(request):
    username = request.user.username
    try:
        master = Master.objects.get(username=username)
    except Exception as e:
        messages.add_message(request, messages.WARNING, e)
    return render(request, 'profile.html', locals())


# @login_required
# def updateProfile(request, user_id):
#     master = Master.objects.get(id=user_id)
#     if master != request.user:
#         raise Http404

#     if request.method != 'POST':
#         form = MasterChangeForm(instance=master)
#     else:
#         form = MasterChangeForm(instance=master, data=request.POST)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect(reverse('learning_logs:topic',
#                                                 args=[topic.id]))

#     context = {'entry': entry, 'topic': topic, 'form': form}
#     return render(request, 'learning_logs/edit_entry.html', context)

def mypet(request):
    return render(request, 'mypet.html', locals())


def pet_detail(request):
    return render(request, 'pet_detail.html', locals())


def add_pet(request):
    return render(request, 'add_pet.html', locals())
