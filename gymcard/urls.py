from django.conf.urls import url
from django.urls import path
from . import views

app_name='gymcard'

urlpatterns = [
    # 'gymcard/'
    path('card/<str:cat>',views.GymListView,name='card'),
    path('card/all/',views.AllGym.as_view(),name='card-all'),
    path('card/gymdetail/',views.GymDetailCard,name='gym-detail'),
    path('card/membership/',views.MembershipDetailCard,name='mem-detail'),
    path('card/gym/city/',views.CityWiseGym.as_view(),name='citywisegym'),
]
