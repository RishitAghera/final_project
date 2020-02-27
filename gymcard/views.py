from django.shortcuts import render
from accounts.models import Gym
from django.views.generic import ListView
# Create your views here.

class GymListView(ListView):
    model = Gym
    template_name = 'accounts/card.html'
    
    