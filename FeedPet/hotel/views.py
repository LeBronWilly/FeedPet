from django.shortcuts import render

# Create your views here.


def hotel(request):
    return render(request, 'hotel.html', locals())
