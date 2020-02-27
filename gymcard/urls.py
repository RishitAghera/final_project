from django.urls import path
from gymcard.views import GymListView

app_name='gymcard'

urlpatterns = [

    path('card/',GymListView.as_view(),name="card"),
    # path('register/',views.RegistrationView.as_view(),name='register'),
    
]
