from django.db import models

# Create your models here.
class Marca(models.Model):
    nombre_marca = models.CharField(max_length=50, primary_key=True)
    #
def __str__(self):
    return self.nombre_marca;

class Producto(models.Model):
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=20,primary_key=True )
    modelo = models.IntegerField()
    unidades = models.IntegerField()
    precio = models.IntegerField()
    detalles = models.CharField(max_length=100, blank=True)
def __str__(self):
    return '{} {}'.format(self.nombre, self.marca);
class Compra(models.Model):
    nombre_producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    #user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    importe = models.FloatField()
    unidades = models.IntegerField()
    fecha = models.DateField()