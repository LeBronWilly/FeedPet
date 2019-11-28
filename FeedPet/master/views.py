# master/views.py
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate
from .forms import MasterCreationForm

# Create your views here.
def index(request):
    return render(request, 'index.html', locals())

def register(request):
    """Register a new user."""
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
    
    context = {'form': form}
    return render(request, 'registration/register.html', context)

def logout_view(request):
    """Log the user out."""
    logout(request)
    return HttpResponseRedirect(reverse('master:index'))
