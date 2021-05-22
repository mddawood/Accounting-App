from django import forms
from projects.models import Payment, Miscellaneous

class PaymentForm(forms.ModelForm):
    class Meta():
        model = Payment
        fields = [ 'number', 'amount', 'date' ]

class MiscellaneousForm(forms.ModelForm):
    class Meta():
        model = Miscellaneous
        fields = [ 'serial_number', 'expense_on', 'expense_by', 'amount', 'date' ]
