from django.db import models
from django.db.models import Model
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):

    is_hotel = models.BooleanField('hotel_owner status', default= False)
    is_user = models.BooleanField('user status', default= False)
