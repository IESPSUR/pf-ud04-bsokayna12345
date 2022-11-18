from django.shortcuts import render, get_object_or_404, redirect

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

def delete_view(request, nombre):
    # dictionary for initial data with
    # field names as keys
    #context = {}

    # fetch the object related to passed id
    producto = get_object_or_404(Producto, pk=nombre)

    if request.method == "POST":
        # delete object
        producto.delete()
        # after deleting redirect to
        # home page
        #return redirect('gestionProducto')
    return render(request, "tienda/delete_view.html", {'producto' :producto})
#https://www.geeksforgeeks.org/delete-view-function-based-views-django/?ref=rp
def detail_producto(request, nombre):
    # dictionary for initial data with
    # field names as keys
    producto = {}

    # add the dictionary during initialization
    producto["data"] = Producto.objects.get(pk=nombre)

    return render(request, "detail_producto.html", producto)


# update view for details
def update_producto(request, nombre):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # fetch the object related to passed id
    producto = get_object_or_404(Producto, id=nombre)

    # pass the object as instance in form
    form = FormularioProducto(request.POST or None, instance=producto)

    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/" + nombre)

    # add form dictionary to context
    context["form"] = form

    return render(request, "update_producto.html", context)
