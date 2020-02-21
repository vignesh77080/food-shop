from django.shortcuts import reverse
from django.db import models
from django.db.models import Model
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):

    is_hotel = models.BooleanField('hotel_owner status', default= False)
    is_user = models.BooleanField('user status', default= False)

class TimestampedModels(Model):

    created_on = models.DateTimeField(auto_now_add = True)
    modified_on = models.DateTimeField(auto_now = True)

    class Meta:
        abstract = True

class HotelOwner(TimestampedModels):

    owner_user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    owner_name = models.CharField(max_length=20, null = False, blank= False)
    owner_number = models.CharField(max_length=10, null = False, blank= False)
    hotel_name = models.CharField(max_length=30, null = False, blank= False)
    location = models.CharField(max_length=50, null = False, blank= False)

    def get_absolute_url(self):
        return reverse('signup', args=())
    
    def save(self, *args, **kwargs):
        user = User.objects.create(username = self.owner_name)
        user.is_hotel = True
        user.save()
        self.owner_user = user
        return super(HotelOwner, self).save(*args, **kwargs)

    def __str__(self):
        return self.hotel_name


class FoodUser(TimestampedModels):

    food_users = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    phone_number = models.CharField(max_length=10, null = False, blank= False)
    email = models.EmailField(null = False, blank= False)

    def get_absolute_url(self):
        return reverse('signup')

    def __str__(self):
        return self.food_users
