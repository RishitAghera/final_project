from django.urls import path
from . import views
from .views import index


urlpatterns = [
    path('',views.index,name="index"),
    path('register/',views.RegistrationView.as_view(),name='register'),
    path('login/',views.LoginView.as_view(),name='login'),
    path('gymregistration/',views.GymRegistration.as_view(),name='gym-reg')
]
