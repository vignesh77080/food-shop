from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import User, HotelOwner, FoodUser


class HotelOwnerForm(ModelForm):

    owner_number = forms.CharField(required=True, widget= forms.TextInput(attrs={'placeholder': 'enter the 10 digit number'}))
    class Meta:
        model = HotelOwner
        fields = ['owner_name', 'owner_number', 'hotel_name', 'location']

    def clean_owner_number(self):
        data = self.cleaned_data['owner_number']
        if data.isnumeric() and len(data) == 10 and not None:
            return data
        raise forms.ValidationError('enter the valid number')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

    # def save(self):
    #     owner_user = super().save()
    #     user = User.objects.create(username = owner_user)
    #     user.is_hotel = True
    #     user.save()
    #     hotelowner = HotelOwner.object.create(owner_user = user)
    #     return hotelowner


class FoodUserForm(ModelForm):

    class Meta:
        model = FoodUser
        fields = ['phone_number', 'email']
