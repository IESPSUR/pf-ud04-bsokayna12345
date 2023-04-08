from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
from django.db import transaction
from django.shortcuts import render, get_object_or_404, redirect
from tienda.forms import FormProducto, FormCompra, FormCheckout, FormMarca
from tienda.models import Producto, Compra, Marca


# Create your views here.
def welcome(request):
    return render(request, 'tienda/index.html', {})


def listProducto(request):
    context = {}
    productos = Producto.objects.all()
    context["datos"] = productos
    return render(request, "tienda/listProducto.html", context)


@user_passes_test(lambda u: u.is_superuser)
def add_producto(request):
    context = {}
    formulario = FormProducto(request.POST or None)
    if formulario.is_valid():
        formulario.save()
    context["form"] = formulario
    return render(request, "tienda/add_producto.html", context)


@user_passes_test(lambda u: u.is_superuser)
def delet_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == "POST":
        producto.delete()
    return render(request, 'tienda/delete.html', {"productos": producto})


@user_passes_test(lambda u: u.is_superuser)
def update_producto(request, id):
    context = {}
    producto = get_object_or_404(Producto, id=id)
    formulario = FormProducto(request.POST or None, instance=producto)
    if formulario.is_valid():
        formulario.save()
    context["form"] = formulario
    return render(request, "tienda/update_producto.html", context)


def compra(request):
    context = {}
    if request.method == 'GET':
        form = FormCompra(request.GET)
        if form.is_valid():
            nombre_producto = form.cleaned_data['nombre']
            productos = Producto.objects.filter(nombre__icontains=nombre_producto)
            if productos:
                context['productos'] = productos
    else:
        form = FormCompra()
    context['form'] = form
    return render(request, "tienda/compra_producto_buscado.html", context)


@transaction.atomic()
def checkout(request, id):
    producto = get_object_or_404(Producto, id=id)
    precio_total = 0
    unidades = 0
    if request.method == 'GET':
        unidades = int(request.GET.get('unidades'))
        precio_total = producto.precio * unidades
        print(precio_total)
        form = FormCheckout({'unidades': unidades})
        if unidades > producto.unidades:
            messages.error(request, "No existen unidades suficientes")

    elif request.method == 'POST':
        form = FormCheckout(request.POST)
        if form.is_valid():
            unidades = form.cleaned_data['unidades']
            print(unidades)
            if unidades <= producto.unidades:
                importe = unidades * producto.precio
                compra = Compra(nombre=producto, unidades=unidades, importe=importe, user=request.user)
                compra.save()
                producto.unidades -= unidades
                producto.save()
                messages.success(request, "compra realizada en exito")
                return redirect('compra')
            else:
                messages.error(request, "No existen unidades suficientes")
                return redirect('compra')
    else:
        form = FormCheckout()

    context = {'form': form, 'producto': producto, 'precio_total': precio_total, 'unidades': unidades}
    return render(request, 'tienda/checkout.html', context)


def marca(request):
    productos = Producto.objects.all()
    if request.method == 'POST':
        form = FormMarca(request.POST)
        if form.is_valid():
            marca_seleccionada = form.cleaned_data['marca']
            print(marca_seleccionada)
            # hacer algo con la marca seleccionada
            productos = Producto.objects.filter(marca__nombre__icontains=marca_seleccionada)
            print(productos)

    else:
        form = FormMarca()
    context = {'form': form,'productos':productos}
    return render(request, 'tienda/marca.html', context)
