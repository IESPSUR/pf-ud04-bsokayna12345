from django.shortcuts import render, get_object_or_404, redirect

from .form import FormularioProducto
from .Carrito import Carrito
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
    producto = get_object_or_404(Producto, pk = nombre)

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

    return render(request, "tienda/detail_producto.html", producto)


# update view for details
def update_producto(request, nombre):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # fetch the object related to passed id
    producto = get_object_or_404(Producto, pk=nombre)

    # pass the object as instance in form
    form = FormularioProducto(request.POST or None, instance=producto)

    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        #return HttpResponseRedirect("getionProducto.html")

    # add form dictionary to context
    context["form"] = form

    return render(request, "tienda/update_producto.html", context)
def realizarCompra(request):
    producto = Producto.objects.all().values()
    template = loader.get_template('tienda/realizarCompra.html')
    context = {
        'misProductos': producto,
    }
    return HttpResponse(template.render(context, request))
"""
def compra(request, nombre):
    # dictionary for initial data with
    # field names as keys
    producto = {}

    # add the dictionary during initialization
    producto["data"] = Producto.objects.get(pk=nombre)

    return render(request, "tienda/compra.html", producto)

def compra(request, nombre):
    # dictionary for initial data with
    # field names as keys
    producto = {}

    # add the dictionary during initialization
    producto["data"] = Producto.objects.get(pk=nombre)

    return render(request, "tienda/compra.html", producto)
#https://www.youtube.com/watch?v=SlUQYrW6M9k

#------

def tienda (request):
    productos = Producto.objects.all()
    return render(request, "tienda/realizarCompra.html", {'productos': productos})
"""
def añadir_carrito(request, nombre):
    carrito = Carrito(request)
    producto = Producto.objects.get(pk=nombre)
    carrito.agregar(producto)
    #return redirect("compra.html")
    return render(request, "tienda/compra.html")
def eliminar_producto(request, producto_pk):
    carrito= Carrito(request)
    producto = Producto.objects.get(pk=producto_pk)
    carrito.eliminar(producto)
    return render(request, "tienda/compra.html")
def restar(request, producto_pk):
    carrito= Carrito(request)
    producto = Producto.objects.get(pk=producto_pk)
    carrito.restar(producto)
    return redirect("tienda")
def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return render(request, "tienda/compra.html")
#<!-- <td><a href="{% url 'compra' x.nombre %}">Comprar</a></td>-->