from datetime import date, timedelta

from django.shortcuts import render, redirect
from django.views import View

from .forms import MembershipCreationForm
from .models import Membership


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
            return redirect('card.html')
        else:
            form = MembershipCreationForm()
            return render(request, 'membership/membershipcreate.html', {'form': form})

