from django.urls import path, include
from .views import HotelOwnerView, FoodUserView, signup_home


app_name = 'registrations'

urlpatterns = [
    
    path('signup/', signup_home , name = 'signup'),
    path('signup/hoteluser/', HotelOwnerView.as_view(), name = 'hotelsignup'),
    path('signup/user/', FoodUserView.as_view(), name = 'usersignup'),
    
]