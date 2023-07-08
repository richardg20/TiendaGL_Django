from django import forms
from .models import Producto

class MiFormulario(forms.ModelForm):
    class Meta:
        model = Producto
        exclude=['id']

