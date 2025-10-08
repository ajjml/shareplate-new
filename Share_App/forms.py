# Share_App/forms.py

from django import forms
from .models import FoodDonation

class FoodDonationForm(forms.ModelForm):
    class Meta:
        model = FoodDonation
        # List only the fields the user should fill in.
        # The view will handle the donor, status, latitude, and longitude.
        fields = ['food_name', 'quantity', 'expiry_date', 'photo']
        
        # Optional: Add widgets for better UI, like a date picker
        widgets = {
            'expiry_date': forms.DateInput(attrs={'type': 'date'}),
        }