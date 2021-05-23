from django import forms
from projects.models import Payment, Miscellaneous

class PaymentForm(forms.ModelForm):
    class Meta():
        model = Payment
        fields = [ 'amount', 'date' ]

class MiscellaneousForm(forms.ModelForm):
    class Meta():
        model = Miscellaneous
        fields = [ 'expense_on', 'expense_by', 'amount', 'date' ]
