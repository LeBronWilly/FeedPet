from django import forms
from .models import Hotel

class HotelForm(forms.ModelForm):
    class Meta:
        model = Hotel
        fields = ('sequence', 'year_eva', 'name', 'postalcode', 'area', 'address')