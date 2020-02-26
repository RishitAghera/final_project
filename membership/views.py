from django.shortcuts import render
from django.views import View


def subscription(request):
    return render(request,"membership/subscription.html")