from django.contrib import admin

# Register your models here.
from .models import Membership, Entry

admin.site.register(Membership)
admin.site.register(Entry)