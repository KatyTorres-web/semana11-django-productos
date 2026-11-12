from django.db import models
from django.core.validators import MinValueValidator
from decimal import Decimal


class Producto(models.Model):
    objects: models.Manager["Producto"] = models.Manager()

    CATEGORIAS = [
        ('Lunar', 'Lunar'),
        ('Estelar', 'Estelar'),
        ('Galáctico', 'Galáctico'),
    ]

    nombre = models.CharField(max_length=100)

    descripcion = models.TextField()

    categoria = models.CharField(
        max_length=20,
        choices=CATEGORIAS
    )

    precio = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        validators=[MinValueValidator(Decimal('0.00'))]
    )

    stock = models.PositiveIntegerField(default=0)

    fecha_creacion = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self) -> str:
        return self.nombre
    
    class Meta:
        ordering = ['id']
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
