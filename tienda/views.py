from django.shortcuts import render

from tienda.models import Producto


# Create your views here.
def welcome(request):
    return render(request, 'tienda/index.html', {})


def listProducto(request):
    context = {}
    productos = Producto.objects.all()
    context["datos"] = productos
    return render(request, "listProducto.html", context)
