from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import MetodoPago

User = get_user_model()

class RegistroForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'telefono', 'preferencia_peliculas'] 

class MetodoPagoForm(forms.ModelForm):
    class Meta:
        model = MetodoPago
        fields = '__all__'