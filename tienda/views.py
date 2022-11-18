from django.shortcuts import render, get_object_or_404

from .form import FormularioProducto
from .models import Producto
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader


# Create your views here.
def welcome(request):
    return render(request, 'tienda/index.html', {})


def gestionProducto(request):
    # crear un objeto producto con todos valores del modelo Producto
    producto = Producto.objects.all().values()
    template = loader.get_template('tienda/getionProducto.html')
    context = {
        'misProductos': producto,
    }
    return HttpResponse(template.render(context, request))


def addProducto(request):
    template = loader.get_template('tienda/addProducto.html')
    return HttpResponse(template.render({}, request))


# def addrecord(request):
#     ma = request.POST['marca']
#     no = request.POST['nombre']
#     mo = request.POST['modelo']
#     uni = request.POST['unidades']
#     p = request.POST['precio']
#     d = request.POST['detalles']
#
#     productos = Producto(marca=ma, nombre=no, modelo=mo, unidades=uni, precio=p, detalles=d)
#     productos.save()
#     return HttpResponseRedirect(reverse('getionProducto'))

def nuevo(request):
    context = {}
    form = FormularioProducto(request.POST or None)
    if form.is_valid():
        form.save()
        context['form'] = form
    return render(request, "tienda/addProducto.html", {'form':form})


class GeeksModel:
    pass


def delete_view(request, pk):
    # dictionary for initial data with
    # field names as keys
    #context = {}

    # fetch the object related to passed id
    obj = get_object_or_404(Producto, pk=nombre)

    if request.method == "POST":
        # delete object
        obj.delete()
        # after deleting redirect to
        # home page
        return HttpResponseRedirect("gestionProducto")

    return render(request, "tienda/delete_view.html", {'obj' :obj})
#https://www.geeksforgeeks.org/delete-view-function-based-views-django/?ref=rp
