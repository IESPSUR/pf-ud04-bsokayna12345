from django.db import models

# Create your models here.


class Marca(models.Model):
   nombre = models.CharField(max_length=30, primary_key=True)

class Producto(models.Model):
   marca_producto = models.ForeignKey(Marca, on_delete=models.CASCADE)
   nombre = models.CharField(max_length=30)
   modelo = models.CharField(max_length=30)
   unidad = models.IntegerField()
   precio = models.FloatField()
   detalles = models.CharField(max_length=30)

class Compra(models.Model):
   nombre_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
   importe =models.FloatField()
   unidades = models.IntegerField()
   fecha = models.DateField()

