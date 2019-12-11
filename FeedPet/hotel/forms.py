from django import forms
from .models import Hotel

class HotelForm(forms.ModelForm):
    class Meta:
        model = Hotel
        fields = ('hname','rank','full_name','incharge','phone','postalcode','district','address')