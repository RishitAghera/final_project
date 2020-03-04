from django.conf.urls import url
from django.urls import path
from . import views

app_name='gymcard'

urlpatterns = [
    # 'gymcard/'
    path('card/<str:cat>',views.GymListView,name='card'),
    path('card/all/',views.AllGym.as_view(),name='card-all'),
    path('card/gym/',views.detailCard,name='gym-detail'),
    path('card/membership/',views.detailCard,name='mem-detail'),
]
