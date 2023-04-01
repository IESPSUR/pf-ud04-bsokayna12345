from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from tienda.forms import FormProducto, FormCompra, FormCheckout
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


def detalle_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    form = FormCompra(request.method)
    context = {'producto': producto, 'form': form}
    return render(request, 'tienda/detalle_producto.html', context)


def checkout(request, id):
    form = FormCheckout()
    precio_total = 0
    producto = get_object_or_404(Producto, id=id)
    if request.method == 'GET':
        unidades = int(request.GET['unidades'])
        print(unidades)
        precio_total = producto.precio * unidades
        form = FormCheckout({'unidades': unidades})

    if request.method == 'POST':
        form = FormCheckout(request.POST)
        if form.is_valid():
            unidades = form.cleaned_data['unidades']
            if unidades <= producto.unidades:
                importe = unidades * producto.precio
                compra = Compra(nombre=producto, unidades=unidades, importe=importe, user=request.user)
                compra.save()
                producto.unidades -= unidades
                producto.save()

            else:
                messages.error(request, "No existen unidades suficiente")
            return redirect('compra')
    context = {'form': form, 'total': precio_total, 'productos': producto , 'unidades':unidades}
    return render(request, 'tienda/checkout.html', context)


"""
///
    if request.method == 'POST':
        form = FormCheckout(request.POST)
        if form.is_valid():
            unidades = form.cleaned_data['unidades']
            if unidades <= producto.unidades:
                importe = unidades * producto.precio
                compra = Compra(nombre=producto, unidades=unidades, importe=importe, user=request.user)
                compra.save()
                producto.unidades -= unidades
                producto.save()

            else:
                messages.error(request, "No existen unidades suficiente")
            return redirect('compra')
///
def comprar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == 'POST':
        form = FormCompra(request.POST)
        if form.is_valid():
            unidades = form.cleaned_data['unidades']
            if unidades > producto.stock:
                messages.error(request, f"No hay suficientes unidades en stock. Stock actual: {producto.stock}")
            else:
                # Registrar la compra
                producto.compra(unidades=unidades, user=request.user)
                messages.success(request, f"Compra realizada exitosamente")
                return redirect('detalle_producto', id=id)
    else:
        form = FormCompra()
    context = {'producto': producto, 'form': form}
    return render(request, 'tienda/comprar_producto.html', context)
"""
