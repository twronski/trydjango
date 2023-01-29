from django import forms
from .models import Product

class RawProductForm(forms.Form):
	title = forms.CharField()
	price = forms.DecimalField()
	description = forms.CharField()