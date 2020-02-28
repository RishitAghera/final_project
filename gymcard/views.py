from django.shortcuts import render
from accounts.models import Gym
from django.views import View
from django.views.generic import ListView,DetailView
# Create your views here.

def GymListView(request,cat):

    queryset=Gym.objects.all().filter(category=cat)
    return render(request,'gymcard/card.html',{'queryset':queryset})

class AllGym(ListView):
    modela=Gym
    template_name = 'gymcard/card.html'
    context_object_name = 'queryset'