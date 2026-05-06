from django.db import models

# Create your models here.
class Tickets(models.Model):
    tipo = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    fecha = models.DateField()
    ubicacion = models.CharField(max_length=100)
    precio = models.IntegerField()
    
    def __str__(self):
        return f"Tickets de: {self.tipo}"