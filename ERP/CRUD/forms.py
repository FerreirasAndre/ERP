from django import forms
from .models import Asset

class CreateDataForm(forms.ModelForm):
	class Meta:
		model = Asset
		fields = ['name', 'quantity', 'category', 'price']