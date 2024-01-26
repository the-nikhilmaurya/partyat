from django import forms
from datetime import date
from django.db import models
from datetime import datetime

class BookingForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    phone_number = forms.NumberInput()

    
    time = models.TimeField(default=datetime.now().time())
    # date = forms.DateField(initial=date.today)

