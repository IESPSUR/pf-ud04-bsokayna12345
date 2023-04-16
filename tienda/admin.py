from django.contrib import admin
#importar los models que queremos administrar 
from tienda.models import Producto, Marca

# Register your models here. 
admin.site.register(Producto)
admin.site.register(Marca)