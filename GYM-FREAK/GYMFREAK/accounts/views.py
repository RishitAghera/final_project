from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from accounts.models import Services

# Create your views here.
from django.views import View

from accounts.forms import RegistrationForm, LoginForm, GymRegistrationForm


def index(request):
    return render(request,"accounts/index.html")

class RegistrationView(View):
    def get(self, request):
        rform = RegistrationForm()
        return render(request, 'accounts/registration.html', {'form': rform})

    def post(self, request):
        rform = RegistrationForm(request.POST)
        if rform.is_valid():
            rform.save()
        return redirect('index')

class LoginView(View):

    def get(self, request):
        lform = LoginForm()
        messages.warning(request,'Please Login in order to continue!')
        return render(request, 'accounts/login.html', {'form': lform})

    def post(self, request):
        form1 = LoginForm(data=request.POST)
        if form1.is_valid():
            print('isvalid')
            username = form1.cleaned_data.get('username')
            password = form1.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                messages.error(request, 'User Not Found please Enter Valid data' + str(form1.errors))
        return render(request, 'accounts/login.html', {'form': form1})


class GymRegistration(View):

    def get(self, request):
        form = GymRegistrationForm()
        return render(request, 'accounts/gymregistration.html', {'form': form})

    def post(self, request):
        form = GymRegistrationForm(request.POST)
        data = request.POST.copy()
        print(data)
        service=[]
        [service.append(Services.objects.all().get(id=int(i))) for i in data['services']]
        print(service)

        if form.is_valid():
            print('is valid')
            form.save()
        return redirect('index')

