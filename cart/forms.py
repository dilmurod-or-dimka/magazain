from django import forms

from .models import Customer, ShippingAddress


class CustomerForm(forms.Form):
    pass


class ShippingAddressForm(forms.ModelForm):
    pass
