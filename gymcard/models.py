from django.db import models
from accounts.models import User
# Create your models here.

class menmber(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)