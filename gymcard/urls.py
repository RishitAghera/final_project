from django.conf.urls import url
from django.urls import path
from . import views

app_name='gymcard'

urlpatterns = [
  # url(r'^(?P<slug>[\w-]+)/$',
  #   url(r'^card/(?P<s>[\w-]+)/$',views.GymListView.as_view(),name="card"),
    path('card/<str:cat>',views.GymListView,name='card'),
    path('card/all/',views.AllGym.as_view(),name='card-all'),
]
