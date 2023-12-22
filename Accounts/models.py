from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    CHOICE = (('Customer','Customer'),('Employee','Employee'),('Corporate','Corporate'),('Franchise','Franchise'))
    full_name = models.CharField(max_length=100,blank=True,null=True)
    user_type = models.CharField(max_length = 100 ,choices = CHOICE,null=True)
    card_access = models.BooleanField(default = False,null=True)

    def __str__(self):
        if not self.full_name:
            return self.username
        else:
            return self.full_name


class OTPS(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    otp = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user

