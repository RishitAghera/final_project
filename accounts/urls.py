from django.urls import path
from . import views
from .views import LogoutView

app_name = 'accounts'

urlpatterns = [
    path('', views.index, name="index"),
    path('register/', views.RegistrationView.as_view(), name='register'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('gymregistration/', views.GymRegistration.as_view(), name='gym-reg'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.LogoutView.as_view(), name="logout"),
    path('gym/entries/', views.EntryView.as_view(), name='entries'),
    path('ajax_calls/search/', views.autocompleteModel),

    # path('subscription-type',views.subscription,name='subscription')

]
