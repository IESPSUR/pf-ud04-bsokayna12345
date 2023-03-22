from time import timezone

from django.db import transaction
from django.shortcuts import render, get_object_or_404, redirect

from tienda.forms import FormProducto, FormCompra
from tienda.models import Producto, Compra


# Create your views here.
def welcome(request):
    return render(request, 'tienda/index.html', {})


def listProducto(request):
    context = {}
    productos = Producto.objects.all()
    context["datos"] = productos
    return render(request, "listProducto.html", context)


def add_producto(request):
    context = {}
    formulario = FormProducto(request.POST or None)
    if formulario.is_valid():
        formulario.save()
    context["form"] = formulario
    return render(request, "tienda/add_producto.html", context)


def delet_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == "POST":
        producto.delete()
    return render(request, 'tienda/delete.html', {"productos": producto})


def update_producto(request, id):
    context = {}
    producto = get_object_or_404(Producto, id=id)
    formulario = FormProducto(request.POST or None, instance=producto)
    if formulario.is_valid():
        formulario.save()
    context["form"] = formulario
    return render(request, "tienda/update_producto.html", context)
def Compra_producto(request):
    context = {}
    producto = Producto.objects.all()
    context["datos"] =producto
    return render(request, 'tienda/comprar.html', context)



