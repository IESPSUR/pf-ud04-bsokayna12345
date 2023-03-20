import site

from django.contrib import admin

from tienda.models import Producto, Marca, Compra

# Register your models here.
admin.site.register(Producto)
admin.site.register(Marca)
admin.site.register(Compra)
