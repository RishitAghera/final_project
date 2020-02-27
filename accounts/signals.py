from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver

from .models import Gym


@receiver(post_save,sender=Gym)
def Add_category(sender,instance,created,**kwargs):
    pass