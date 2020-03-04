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
    membership=Membership.objects.all().get(user=request.user)
    gym=Gym.objects.all().get(user=request.user)
    print(request.path)
    return render(request,'gymcard/detailcard.html',{'gym':gym,'membership':membership})