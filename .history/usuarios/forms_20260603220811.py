from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UsuarioPersonalizado

class UsuarioPersonalizadoForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = UsuarioPersonalizado
        # Aquí concatenamos los campos por defecto (usuario, contraseña) con los tuyos
        fields = UserCreationForm.Meta.fields + ('foto', 'telefono', 'preferencia_peliculas')