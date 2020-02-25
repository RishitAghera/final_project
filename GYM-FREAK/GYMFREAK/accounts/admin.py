from django.contrib import admin

# Register your models here.
from accounts.models import User, Gym,Services

admin.site.register(User)
admin.site.register(Gym)
admin.site.register(Services)