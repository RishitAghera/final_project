from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import *

SUBSCRIPTION=(
    (3,'Quarter'),
    (6,'Half way'),
    (12,'Yearly'),
)
CATEGORY=(
    ('Bronze','Bronze'),
    ('Silver','Silver'),
    ('Gold','Gold'),
)

class MembershipCreationForm(forms.ModelForm):

    category = forms.CharField(widget=forms.Select(choices=CATEGORY, attrs={'class': 'btn btn-secondary dropdown-toggle'}))

    validity = forms.IntegerField(widget=forms.Select(choices=SUBSCRIPTION,attrs={'class':'btn btn-secondary dropdown-toggle'}))
    # auto_renew = forms.BooleanField()

    class Meta:
        model = Membership
        fields = ['validity', 'auto_renew']

