from django.shortcuts import render
from django.views.generic import CreateView
from django.http import HttpResponse

from .forms import HotelOwnerForm, FoodUserForm
from .models import HotelOwner, User, FoodUser


# Create your views here.

def signup_home(request):
    return render(request, 'registrations/signuphome.html')

class HotelOwnerView(CreateView):

    model = HotelOwner
    form_class = HotelOwnerForm
    success_url = '/accounts/signup'
    template_name = 'registrations/hotelowner.html'

class FoodUserView(CreateView):
    
    model = User
    form_class = FoodUserForm
    template_name = 'registrations/fooduser.html'