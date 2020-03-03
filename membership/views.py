from datetime import date, timedelta

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from .forms import MembershipCreationForm
from .models import Membership
from . import checksum
MERCHANT_KEY='YOUR_KEY'
def subscription(request):

    return render(request,"membership/subscription.html")

class MemebershipCreation(View):

    def get(self,request):
        form = MembershipCreationForm()
        return render(request,'membership/membershipcreate.html',{'form':form})

    def post(self, request):
        form = MembershipCreationForm(request.POST)
        if form.is_valid():
            data=request.POST.copy()
            print(self.request.user)
            print(data.get('validity'))
            val=int(data.get('validity'))
            renew=True if data.get('auto_renew') != None else False
            print(renew)
            start_date = date.today()
            if val==3:
                inc=90
            elif val==6:
                inc=180
            else:
                inc=365
            end_date = date.today()+timedelta(days=int(inc))
            print(start_date)
            print(end_date)
            print(data.get('category'))
            new_membership=Membership.objects.create(user=self.request.user,category=data.get('category'),validity=val,start_date=start_date,end_date=end_date,auto_renew=renew)
            url='gymcard/card/'+data.get('category')
            print(str(new_membership.id))
            print(str(self.request.user.email))
            price={'Bronze':{3:2000,6:3500,12:5000},
                   'Silver':{3:3000,6:5500,12:8000},
                   'Gold':{3:4000,6:7000,12:10000}}
            print(str(price[data.get('category')][val]))
            # return redirect('gymcard:card',cat=data.get('category'))
            param_dict={
                "MID": "YOUR_MID",
                "ORDER_ID": str(new_membership.id),
                "CUST_ID": str(self.request.user.email),
                "TXN_AMOUNT": str(price[data.get('category')][val]),
                "CHANNEL_ID": "WEB",
                "INDUSTRY_TYPE_ID": "Retail",
                "WEBSITE": "WEBSTAGING",
                "CALLBACK_URL":"http://127.0.0.1:8000/membership/handlerequest/",
                # "cat":data.get('category'),
            }
            param_dict["CHECKSUMHASH"]=checksum.generate_checksum(param_dict, MERCHANT_KEY)
            return render(request,'membership/paytm.html',{'param_dict':param_dict})
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

    def get(self,request):
        return render(request,'membership/qr_entry.html')

    def post(self,request):
        print(request.POST.get('qr_result'))
        print('post called')
        return redirect('accounts:index')