from django.db import models

import accounts

class Membership(models.Model):

    user = models.ForeignKey(accounts.models.User,on_delete=models.CASCADE)
    category = models.CharField(max_length=10)
    is_valid = models.BooleanField(default=True)
    validity = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    auto_renew = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)+' '+str(self.user.name)+' '+str(self.category)
