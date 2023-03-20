from django.db import models

# Create your models here.
class Marca(models.Model):
    nombre=models.CharField(max_length=30)

    def __str__(self):
        return self.nombre
class Producto(models.Model)
    marca=models.ForeignKey('Marca', on_delete=models.CASCADE)
    nombre=models.CharField(max_length=30)

