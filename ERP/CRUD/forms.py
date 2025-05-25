from django import forms
from .models import AssetModel

class CreateDataForm(forms.ModelForm):
	class Meta:
		model = AssetModel
		fields = ['name', 'supplier', 'description', 'available']