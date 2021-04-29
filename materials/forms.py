from django import forms
from materials.models import Material, Payment

class MaterialForm(forms.ModelForm):
    class Meta():
        model = Material
        fields = [ 'type', 'supplier', 'quantity', 'unit', 'price', 'date']

class MaterialUpdateForm(forms.ModelForm):
    class Meta():
        model = Material
        fields = ['quantity', 'unit', 'price']

class PaymentForm(forms.ModelForm):
    class Meta():
        model = Payment
        fields = [ 'name', 'amount', 'date' ]
