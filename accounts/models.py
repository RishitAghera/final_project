from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    contact = models.CharField('Contact',max_length=10,unique=True)
    name = models.CharField('Name',max_length=30,blank=True)
    city = models.CharField('City',max_length=20,blank=True)


    def __str__(self):
        return str(self.id)+' '+str(self.username)

class Services(models.Model):

    service=models.CharField(max_length=20)

    def __str__(self):
        return str(self.id)+' '+str(self.service)


class Gym(models.Model):


    user=models.OneToOneField(User,on_delete=models.PROTECT,unique=True,null=True)
    name = models.CharField('Name',max_length=30,blank=True)
    opentime = models.TimeField()
    closetime = models.TimeField()
    city = models.CharField('City', max_length=20, blank=True)
    address = models.TextField(max_length=100,blank=True)
    services = models.ManyToManyField(Services)
    image=models.ImageField(default='default.jpg',upload_to='gym_image')
    category=models.CharField(null=True,max_length=10)
    qrcode=models.ImageField(upload_to='gym_qr',null=True)

    def __str__(self):
        return str(self.name)+' '+str(self.city)+ ' '+str(self.category)