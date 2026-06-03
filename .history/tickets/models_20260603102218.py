from django.db import models

# Create your models here.
class Tickets(models.Model):
    tipo = models.CharField(max_length=100)
    nombre = models.CharField(max_length=100)
    fecha = models.DateField()
    ubicacion = models.CharField(max_length=100)
    precio = models.IntegerField()
    metodo_pago = models.ForeignKey(
        'MetodoPago',
        on_delete=models.CASCADE,
        null=True,  
        blank=True 
    )

    imagen = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return f"Película: {self.nombre}"

class MetodoPago(models.Model):
    TIPOS = [
        ('EFECTIVO', 'Efectivo'),
        ('TRANSFERENCIA', 'Transferencia'),
        ('BANCO', 'Banco'),
        ('QR', 'QR'),
    ]

    TARJETAS = [
        ('CREDITO', 'Crédito'),
        ('DEBITO', 'Débito'),
    ]

    nombre = models.CharField(max_length=100)

    tipo = models.CharField(
        max_length=20,
        choices=TIPOS
    )

    banco = models.CharField(
        max_length=50,
        null=True,
        blank=True
    )

    tarjeta = models.CharField(
        max_length=20,
        choices=TARJETAS,
        null=True,
        blank=True
    )

    qr = models.ImageField(
        upload_to='qr/',
        null=True,
        blank=True
    )

    def __str__(self):
        return f"Metodo de pago: {self.nombre}"

# class Categoria(models.Model):
#     nombre = models.CharField(max_length=100)
#     # pelicula = models.ForeignKey(
#     #     'Pelicula',
#     #     on_delete=models.CASCADE,
#     #     null=False,
#     #     blank=False
#     #     )

#     def __str__(self):
#         return f"Categoria: {self.nombre}"

# class Pelicula (models.Model):
#     titulo = models.CharField(max_length=100)
#     descripcion = models.TextField()
#     duracion = models.IntegerField()
#     categoria = models.ForeignKey(
#         'Categoria',
#         on_delete=models.CASCADE,
#         null=False,
#         blank=False
#         )
#     # categoria = models.ManyToManyField(
#     #     'Categoria',
#     #     default=None,
#     #     blank=True,
#     #     related_name="categorias",
#     # )
    
#     def __str__(self):
#         return f"Pelicula: {self.titulo}"
