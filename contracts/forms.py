from django import forms
from contracts.models import Contract, Payment

class ContractForm(forms.ModelForm):
    class Meta():
        model = Contract
        fields = [ 'contractor_name', 'contract_type', 'contract_value', 'date']

class ContractUpdateForm(forms.ModelForm):
    class Meta():
        model = Contract
        fields = ['variation']

class PaymentForm(forms.ModelForm):
    class Meta():
        model = Payment
        fields = [ 'number', 'amount', 'type', 'date' ]
