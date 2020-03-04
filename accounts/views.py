from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.generic import DetailView
from django.views.generic import View

from .models import Services, Gym, User
import qrcode


# Create your views here.
from django.views import View

from .forms import RegistrationForm, LoginForm, GymRegistrationForm


def index(request):
    queryset=Gym.objects.all()
    return render(request,"accounts/index.html",{'queryset':queryset})


def card(request):
    return render(request,"accounts/card.html")

class LogoutView(View):
    def get(self,request):
        logout(request)
        return redirect('accounts:login')


class RegistrationView(View):
    def get(self, request):
        rform = RegistrationForm()
        return render(request, 'accounts/registration.html', {'form': rform})

    def post(self, request):
        rform = RegistrationForm(request.POST)
        if rform.is_valid():
            rform.save()
        return redirect('accounts:index')

class LoginView(View):

    def get(self, request):
        lform = LoginForm()
        messages.warning(request,'Please Login in order to continue!')
        return render(request, 'accounts/login.html', {'form': lform})

    def post(self, request):
        form1 = LoginForm(data=request.POST)
        if form1.is_valid():
            username = form1.cleaned_data.get('username')
            password = form1.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                print('isvalid')
                return redirect('accounts:index')
            else:
                lform = LoginForm(data=request.POST)
                return render(request, 'accounts/login.html', {'form': lform})
        else:
            lform = LoginForm()
            return render(request, 'accounts/login.html', {'form': lform})

class GymRegistration(View):
    @method_decorator(login_required, name='dispatch')
    def get(self, request):
        if Gym.objects.all().filter(user=request.user):
            return render(request, 'accounts/gymregistration.html', {'msg': 'You are Already our Gym Partner'})
        else:
            form = GymRegistrationForm()
            return render(request, 'accounts/gymregistration.html', {'form': form})

    def post(self, request):

        form = GymRegistrationForm(request.POST,request.FILES)
        data = request.POST.copy()

        if form.is_valid():

            new_gym = form.save()
            choices = Services.objects.filter(id__in=data.getlist('services'))
            new_gym.services.set(choices)
            if new_gym.services.count() == 1:
                new_gym.category = 'Bronze'
            elif new_gym.services.count() == 2:
                new_gym.category = 'Silver'
            elif new_gym.services.count() >= 3:
                new_gym.category = 'Gold'
            else:
                new_gym.category = ''

            qr=qrcode.make(new_gym.id)
            qr.save('media/gym_qr/'+str(new_gym.id)+'.png')
            print(qr)
            new_gym.qrcode='gym_qr/'+str(new_gym.id)+'.png'
            new_gym.username=self.request.user

            new_gym.save()
            print('GYM CREATED',new_gym.services.count())



        else:
            print(form.errors)
        return redirect('accounts:index')

@method_decorator(login_required, name='dispatch')
def profile(request):
    object=User.objects.all().get(id=request.user.pk)
    return render(request,'accounts/profile.html',{'object':object})

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("accounts:index")