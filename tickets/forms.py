from django import forms

from .models import Pelicula

class PeliculaForm(forms.ModelForm):
    class Meta:
        model = Pelicula
        fields = ['titulo', 'descripcion', 'duracion', 'categoria']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
            'duracion': forms.NumberInput(attrs={'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
        }