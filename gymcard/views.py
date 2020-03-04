from datetime import date, timedelta, datetime

from django.shortcuts import render
from accounts.models import Gym
from django.views import View
from django.views.generic import ListView,DetailView
# Create your views here.
from membership.models import Membership


def GymListView(request,cat):

    queryset=Gym.objects.all().filter(category=cat)
    return render(request,'gymcard/card.html',{'queryset':queryset})

class AllGym(ListView):
    modela=Gym
    template_name = 'gymcard/card.html'
    context_object_name = 'queryset'

def detailCard(request):
    day=''
    print(request.path)
    if request.path == '/gymcard/card/membership/':
        try:
            membership=Membership.objects.all().get(user=request.user)
            print(datetime.now())
            left = membership.end_date - datetime.now().date()
            day = str(left.days)
            print(day)
            gym = ''
        except:
            gym=''
            membership=''

    if request.path == '/gymcard/card/gym/':
        try:
            gym=Gym.objects.all().get(user=request.user)
            membership = ''
        except:
            membership=''
            gym = ''

    return render(request,'gymcard/detailcard.html',{'membership':membership,'gym':gym,'day':day})