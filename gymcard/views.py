from datetime import datetime

from django.shortcuts import render, get_object_or_404
from accounts.models import Gym
from django.views import View
from django.views.generic import ListView, DetailView
from membership.models import Membership


def GymListView(request, cat):
    queryset = Gym.objects.all().filter(category=cat)
    return render(request, 'gymcard/card.html', {'queryset': queryset})


class AllGym(ListView):
    modela = Gym
    template_name = 'gymcard/card.html'
    context_object_name = 'queryset'


def MembershipDetailCard(request):
    membership = Membership.objects.all().get(user=request.user)
    print(datetime.now())
    left = membership.end_date - datetime.now().date()
    day = str(left.days)
    print(day)
    return render(request, 'gymcard/membership_detailcard.html', {'membership': membership, 'day': day})


def GymDetailCard(request):
    gym = Gym.objects.all().get(user=request.user)
    print(gym.name)
    return render(request, 'gymcard/gym_detailcard.html', {'gym': gym})


class CityWiseGym(View):

    def post(self, request):
        print(request.POST['searchcity'])
        citygymlist = Gym.objects.all().filter(city=request.POST['searchcity'])
        print(citygymlist)
        return render(request, 'gymcard/citywisegym.html', {'citygymlist': citygymlist})
