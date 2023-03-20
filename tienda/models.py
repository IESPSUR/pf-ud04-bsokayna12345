from django.db import models

# Create your models here.
class Marca(models.Model):
    nombre=models.CharField(max_length=30)

    def __str__(self):
        return self.nombre
class Producto(models.Model):
    marca=models.ForeignKey('Marca', on_delete=models.CASCADE)
    nombre=models.CharField(max_length=30)
    unidades=models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    detalles = models.TextField()

