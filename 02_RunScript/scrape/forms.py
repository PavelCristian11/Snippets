from django.forms import ModelForm, TextInput
from .models import Registration

class RegForm(ModelForm):
    class Meta:
        model = Registration
        fields = '__all__'
        widgets = {
            'reg': TextInput(attrs={
                'id': 'first_name',
                'placeholder': 'Insert a number plate',
                'required': 'True',
                }),
        }
        labels = {
            'reg': '',
        }