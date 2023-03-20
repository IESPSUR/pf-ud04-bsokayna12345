from datetime import datetime

from django.conf import settings
from django.core.validators import MinValueValidator
from django.db import models


# Create your models here.
class Marca(models.Model):
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    marca = models.ForeignKey('Marca', on_delete=models.CASCADE)
    nombre = models.CharField(max_length=30, null=False)
    unidades = models.IntegerField(validators=[MinValueValidator(0)])
    precio = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.00)])
    detalles = models.TextField()

    def __str__(self):
        return '{} {}'.format(self.nombre, self.marca)


class Compra(models.Model):
    nombre = models.ForeignKey('Producto', on_delete=models.RESTRICT)
    unidades = models.IntegerField(validators=[MinValueValidator(0)])
    importe = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.00)])
    fecha = models.DateField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.RESTRICT)

    def __str__(self):
        return '{} {} {} {}'.format(self.nombre, self.importe, self.user, self.fecha)
