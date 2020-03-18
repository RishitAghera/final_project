from datetime import datetime, timedelta

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import json
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views.generic import DetailView, ListView
from django.views.generic import View

from .models import Services, Gym, User
import qrcode

# Create your views here.
from django.views import View

from .forms import RegistrationForm, LoginForm, GymRegistrationForm
from membership.models import Entry


def index(request):
    queryset = Gym.objects.all()
    return render(request, "accounts/index.html", {'queryset': queryset})


def card(request):
    return render(request, "accounts/card.html")


class LogoutView(View):
    def get(self, request):
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
            messages.success(request,'Registered successfully..')
            return redirect('accounts:login')
        messages.error(request,'sign up with new user..')
        return render(request, 'accounts/registration.html', {'form': rform})

class LoginView(View):

    def get(self, request):
        form1 = LoginForm()
        messages.warning(request, 'Please Login in order to continue!')
        return render(request, 'accounts/login.html', {'form': form1})

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
                form1 = LoginForm(data=request.POST)
                messages.error(request, 'User Not Found please Enter Valid data' + str(form1.errors))
                return render(request, 'accounts/login.html', {'form': form1})
        else:
            form1 = LoginForm()
            return render(request, 'accounts/login.html', {'form': form1})


class GymRegistration(View):

    @method_decorator(login_required, name='dispatch')
    def get(self, request):
        if Gym.objects.all().filter(user=request.user):
            return render(request, 'accounts/gymregistration.html', {'msg': 'You are Already our Gym Partner'})
        else:
            form = GymRegistrationForm()
            return render(request, 'accounts/gymregistration.html', {'form': form})

    def post(self, request):

        form = GymRegistrationForm(request.POST, request.FILES)
        data = request.POST.copy()

        if form.is_valid():
            is_exists=Gym.objects.all().filter(user=request.user)
            if not is_exists:

                new_gym = form.save()
                new_gym.user = request.user
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

                qr = qrcode.make(new_gym.id)
                qr.save('media/gym_qr/' + str(new_gym.id) + '.png')
                print(qr)
                new_gym.qrcode = 'gym_qr/' + str(new_gym.id) + '.png'
                new_gym.username = self.request.user

                new_gym.save()

                print('GYM CREATED', new_gym.services.count())

        return redirect('accounts:gym-reg', {'msg': 'You are Already our Gym Partner'})


def profile(request):
    try:
        object = User.objects.all().get(id=request.user.pk)
        return render(request, 'accounts/profile.html', {'object': object})
    except:
        return HttpResponse("404 Error")


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect("accounts:index")


def credit_amt(category, count):
    price = {'gold': 22, 'silver': 17, 'bronse': 22}
    if category == 'Gold':
        credit = count * price['gold']
    elif category == 'silver':
        credit = count * price['silver']
    else:
        credit = count * price['bronse']
    return credit


@method_decorator(login_required, name='dispatch')
class EntryView(ListView):
    model = Entry
    template_name = 'accounts/entrylist.html'

    def get_queryset(self):
        entry_lst = self.request.user.gym.entry_set.all().filter(date__gte=datetime.now() - timedelta(days=30))
        credit = credit_amt(self.request.user.gym.category, entry_lst.count())
        return {'entry_lst': entry_lst, 'credit': credit}


def search_city(request):
    city = request.GET.get('search')

    city = list(Gym.objects.values())
    data = [i.city for i in Gym.objects.all()]

    return JsonResponse(data, safe=False)


def autocompleteModel(request):
    if request.is_ajax():
        q = request.GET.get('term')
        search_qs = Gym.objects.filter(city__istartswith=q)
        results = []
        print('q:')
        for r in search_qs:
            results.append(r.city)
        data = json.dumps(results)
        print(data)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)
