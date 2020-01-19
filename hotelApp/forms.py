from django import forms
from .models import Reservation
from .models import Room

# This class is for creating Forms based on Database object (TodoList)

class DateInput(forms.DateInput):
    input_type = 'date'

class ReservationForm(forms.ModelForm):

    class Meta:
        model = Reservation
        fields = ['startDate', 'endDate']

        widgets = {
            'endDate': DateInput()
        }

class RoomForm(forms.ModelForm):

    class Meta:
        model = Room
        fields = "__all__"