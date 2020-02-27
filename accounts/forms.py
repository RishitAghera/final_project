from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import *

TIMESLOTE=(
    (0,'-----'),
    (5,'5'),
    (6,'6'),
    (7,'7'),
    (8,'8'),
    (9,'9'),
    (10,'10'),
    (11,'11'),
)

class RegistrationForm(UserCreationForm):

    class Meta:
        model=User
        fields=('username','name','contact','email','password1','password2')

class LoginForm(forms.Form):

    username=forms.CharField(max_length=10, label="Enter Username")
    password=forms.CharField(max_length=20,label="Enter Password",widget=forms.PasswordInput())


class GymRegistrationForm(forms.ModelForm):


    # image=forms.ImageField(label='choose your image',)
    class Meta:
        model=Gym
        fields=['name','opentime','closetime','address','city','image','services']
