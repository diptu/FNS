from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils import timezone


def upload_file_location(instance,filename):
    return "%s/%s" %(instance.pk , filename)

class User(AbstractUser):
    GENDER_CHOICES = (
        (1, ("Male")),
        (2, ("Female")),
    )
    NID         =   models.IntegerField(null=True)
    birth_date  =   models.DateField(null=True)
    profile_pic =   models.ImageField(null=True , blank=True ,upload_to = upload_file_location)
    contact     =   models.CharField(max_length=20 , null=True, blank=True)
    gender      =   models.IntegerField(choices=GENDER_CHOICES, default=1)
    religion    =   models.CharField(max_length=20,null=True, blank=True)
    occuption   =   models.CharField(max_length=50,null=True, blank=True)
    education   =   models.CharField(max_length=120,null=True, blank=True)
    town        =   models.CharField(max_length=20,null=True,blank=True)
    country     =   models.CharField(max_length=20,null=True,blank=True)
    about_you   =   models.TextField(max_length=500,null=True,blank=True)

    def __str__(self):
        return self.username

def pre_save_post_receiver(sender , instance ,*args , **kwargs):
    instance.pk = instance.pk

pre_save.connect(pre_save_post_receiver,sender=User)
