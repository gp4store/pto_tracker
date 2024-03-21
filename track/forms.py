from django import forms
from django.forms import ModelForm
from .models import pto_request

# Creating a form for a time off request 
class pto_requestForm(ModelForm):
    class Meta:

        model = pto_request
        fields = ('pto_type', 'date_requested', 'hours_used', 'send_to')
        labels = {
            
            'pto_type': '',
            'date_requested': '', 
            'hours_used': '',
            'send_to': '',
        }
        widgets = {
            
            'pto_type': forms.TextInput(attrs={'class':'form-control', 'placeholder':'What are you using?'}),
            'date_requested': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Dates MM/DD/YY, '}),
            'hours_used': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Hours to use'}),
            'send_to': forms.EmailInput(attrs={'class':'form-control', 'placeholder':'send to?'}),
        }


