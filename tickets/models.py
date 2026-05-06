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

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    # pelicula = models.ForeignKey(
    #     'Pelicula',
    #     on_delete=models.CASCADE,
    #     null=False,
    #     blank=False
    #     )

    def __str__(self):
        return f"Categoria: {self.nombre}"

class Pelicula (models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    duracion = models.IntegerField()
    categoria = models.ForeignKey(
        'Categoria',
        on_delete=models.CASCADE,
        null=False,
        blank=False
        )
    # categoria = models.ManyToManyField(
    #     'Categoria',
    #     default=None,
    #     blank=True,
    #     related_name="categorias",
    # )
    
    def __str__(self):
        return f"Pelicula: {self.titulo}"
