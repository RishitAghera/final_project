from django.urls import path
from . import views
<<<<<<< HEAD
from .views import index,card
=======
>>>>>>> 6e441c0d8c4a5ab4aa90948d034f0b77bf80d442


app_name='accounts'

urlpatterns = [
    path('',views.index,name="index"),
    path('register/',views.RegistrationView.as_view(),name='register'),
    path('login/',views.LoginView.as_view(),name='login'),
    path('gymregistration/',views.GymRegistration.as_view(),name='gym-reg'),
    # path('subscription-type',views.subscription,name='subscription')

]
