from django import forms
from testapp.models import Order
from testapp.models import checkout

class OrderForm(forms.ModelForm):
    class Meta:
        model=Order
        fields='__all__'


class CheckForm(forms.ModelForm):
    class Meta:
        model=checkout
        fields='__all__'
