from django.db import models
from django.contrib.auth.models import AbstractUser

class UsuarioPersonalizado(AbstractUser):
    foto = models.ImageField(upload_to='usuarios/fotos/', null=True, blank=True)
    telefono = models.CharField(max_length=20, null=True, blank=True)
    preferencia_peliculas = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        if self.preferencia_peliculas:
            return f"{self.username} - Preferencias: {self.preferencia_peliculas}"
        return self.username