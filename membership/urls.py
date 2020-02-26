from django.urls import path,include
from . import views

app_name='membership'
urlpatterns = [
    #membership/
    path('subscription/',views.subscription,name='subscription'),


]