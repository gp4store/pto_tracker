from django import forms
from django.forms import ModelForm
from .models import pto_request

# Creating a form for a time off request 
class pto_requestForm(ModelForm):
    class Meta:

        model = pto_request
        fields = ('pto_type', 'date_requested', 'hours_used', 'send_to')
        widgets = {
            'pto_type':
            'date_requested':
            'hours_used':
            'send_to':
        }


