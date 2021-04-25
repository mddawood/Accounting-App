from django import forms
from labours.models import Labour, Payment

class LabourForm(forms.ModelForm):
    class Meta():
        model = Labour
        fields = [ 'name', 'type', 'wage']

class PaymentForm(forms.ModelForm):
    class Meta():
        model = Payment
        fields = [ 'name', 'days']
