from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import User, HotelOwner, FoodUser

# Register your models here.

class CustomUser(ModelAdmin):

    model = User
    readonly_fields = ['is_hotel', 'is_user'] 

admin.site.register(User, CustomUser)
admin.site.register(HotelOwner)

