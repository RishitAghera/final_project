from datetime import datetime

from django.db import models

from accounts.models import User,Gym




class Membership(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE,unique=True)
    category = models.CharField(max_length=10)
    is_valid = models.BooleanField(default=True)
    validity = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    auto_renew = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)+' '+str(self.user.name)+' '+str(self.category)


class Entry(models.Model):

    user = models.ForeignKey(User,on_delete=models.CASCADE)
    gym = models.ForeignKey(Gym,on_delete=models.CASCADE)
    date = models.DateField(default=datetime.now())

    def __str__(self):
        return str(self.id)+' '+str(self.user.name)+' '+str(self.gym.name)
