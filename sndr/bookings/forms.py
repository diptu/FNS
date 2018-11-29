from django import forms
from bookings.models import Booking
from django.contrib.auth import get_user_model

User = get_user_model()

class BookingForm(forms.Form):
    # class Meta:
    #    model = Booking
    #    fields = ["check_in", "check_out"]
    check_in     = forms.DateTimeField(label='Check in',required=True,help_text='e.g,Year-Month-Date')
    check_out    = forms.DateTimeField(label='Check out',required=True,help_text='e.g,Year-Month-Date')
