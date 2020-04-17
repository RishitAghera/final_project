from datetime import date, timedelta, datetime

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from .forms import MembershipCreationForm
from .models import Membership, Entry
from . import checksum
from accounts.models import Gym

MERCHANT_KEY = 'lavcDLT%rE7AJRie'


def subscription(request):
    return render(request, "membership/subscription.html")


class MemebershipCreation(View):
    @method_decorator(login_required, name='dispatch')
    def get(self, request):
        form = MembershipCreationForm()
        return render(request, 'membership/membershipcreate.html', {'form': form})

    def post(self, request):
        form = MembershipCreationForm(request.POST)
        if form.is_valid():
            data = request.POST.copy()
            print(self.request.user)
            print(data.get('validity'))
            val = int(data.get('validity'))
            renew = True if data.get('auto_renew') != None else False
            print(renew)
            start_date = date.today()
            if val == 3:
                inc = 90
            elif val == 6:
                inc = 180
            else:
                inc = 365
            end_date = date.today() + timedelta(days=int(inc))
            print(start_date)
            print(end_date)
            print(data.get('category'))
            try:
                new_membership = Membership.objects.create(user=self.request.user, category=data.get('category'),
                                                           validity=val, start_date=start_date, end_date=end_date,
                                                           auto_renew=renew)
            except:
                form = MembershipCreationForm()
                return render(request, 'membership/membershipcreate.html', {'form': form})
            # url='gymcard/card/'+data.get('category')
            print(str(new_membership.id))
            print(str(self.request.user.email))
            price = {'Bronze': {3: 2000, 6: 3500, 12: 5000},
                     'Silver': {3: 3000, 6: 5500, 12: 8000},
                     'Gold': {3: 4000, 6: 7000, 12: 10000}}
            print(str(price[data.get('category')][val]))
            # return redirect('gymcard:card',cat=data.get('category'))
            param_dict = {
                "MID": "DvQwxc10574555665868",
                "ORDER_ID": str(new_membership.id),
                "CUST_ID": str(self.request.user.email),
                "TXN_AMOUNT": str(price[data.get('category')][val]),
                "CHANNEL_ID": "WEB",
                "INDUSTRY_TYPE_ID": "Retail",
                "WEBSITE": "WEBSTAGING",
                "CALLBACK_URL": "http://127.0.0.1:8000/membership/handlerequest/",
                # "cat":data.get('category'),
            }
            param_dict["CHECKSUMHASH"] = checksum.generate_checksum(param_dict, MERCHANT_KEY)
            return render(request, 'membership/paytm.html', {'param_dict': param_dict})
        else:
            form = MembershipCreationForm()
            return reverse(request, 'membership/membershipcreate.html', {'form': form})


@csrf_exempt
def handlerequest(request):
    # paytm will send you post request here
    form = request.POST
    response_dict = {}
    for i in form.keys():
        response_dict[i] = form[i]
        if i == 'CHECKSUMHASH':
            check_sum = form[i]

    verify = checksum.verify_checksum(response_dict, MERCHANT_KEY, check_sum)
    if verify:
        if response_dict['RESPCODE'] == '01':
            print('Payment successful')
        else:
            print('Payment was not successful because' + response_dict['RESPMSG'])
            Membership.objects.get(id=response_dict['ORDERID']).delete()
    return render(request, 'membership/paymentstatus.html', {'response': response_dict})


class Qrscanning(View):
    @method_decorator(login_required, name='dispatch')
    def get(self, request):
        return render(request, 'membership/qr_entry.html')

    def post(self, request):
        print(request.POST.get('qr_result'))
        print(request.user)
        is_valid = Entry.objects.filter(user=request.user, date=datetime.now())
        if not is_valid:
            end = Membership.objects.get(user=request.user).end_date
            print(end)
            remaining = (end - datetime.now().date()).days
            print(remaining)
            gym_ins = Gym.objects.get(id=int(request.POST.get('qr_result')))
            new_entry = Entry.objects.create(user=request.user, gym=gym_ins, date=datetime.now())
            entry_msg = 'Entry Added..' + str(remaining) + ' more days to go..'
            messages.info(request, 'You are Booked Gym for today..')
            return redirect('accounts:index')
        messages.warning(request, 'You have already visited gym today..')
        return render(request, 'membership/qr_entry.html')