from django import forms
from projects.models import Payment

class PaymentForm(forms.ModelForm):
    class Meta():
        model = Payment
        fields = [ 'name', 'amount', 'date' ]
