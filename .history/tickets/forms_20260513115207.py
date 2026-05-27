from django import forms

from .models import MetodoPago

class MetodoPagoForm(forms.ModelForm):
    class Meta:
        model = MetodoPago
        fields = ['nombre', 'tipo', 'banco']