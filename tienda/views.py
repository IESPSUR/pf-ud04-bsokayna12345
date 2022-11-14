from django.shortcuts import render
from .models import Producto
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader

# Create your views here.
def welcome(request):
    return render(request,'tienda/index.html', {})

def gestionProducto(request):
    #crear un objeto producto con todos valores del modelo Producto
    producto=  Producto.objects.all().values()
    template = loader.get_template('tienda/getionProducto.html')
    context = {
    'misProductos': producto,
    }
    return HttpResponse(template.render(context, request))
def addProducto(request):
    template = loader.get_template('tienda/addProducto.html')
    return HttpResponse(template.render({}, request))
def addrecord(request):
  ma = request.POST['marca']
  no = request.POST['nombre']
  mo = request.POST['modelo']
  uni = request.POST['unidades']
  p = request.POST['precio']
  d = request.POST['detalles']
  
  productos = Producto(marca=ma, nombre=no, modelo=mo, unidades=uni, precio=p, detalles=d)
  productos.save()
  return HttpResponseRedirect(reverse('getionProducto'))