from django.urls import path,include
from . import views

app_name='membership'
urlpatterns = [
    #membership/
    path('subscription/',views.subscription,name='subscription'),
    path('subscription/validity/',views.MemebershipCreation.as_view(),name='mem-create'),
    path('subscription/qr/',views.Qrscanning.as_view(),name='qrscanning'),
    path('handlerequest/', views.handlerequest, name='handle-req')

]