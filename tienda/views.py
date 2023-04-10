from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
from django.db import transaction
from django.db.models import Sum
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from tienda.forms import FormProducto, FormCompra, FormCheckout, FormMarca, FormCompraUser, FormFilterProductoMarca
from tienda.models import Producto, Compra, Marca


# Create your views here.
def welcome(request):
    return render(request, 'tienda/index.html', {})


def listado(request):
    context = {}
    productos = Producto.objects.all()
    context["productos"] = productos
    return render(request, "tienda/listProducto.html", context)


@user_passes_test(lambda u: u.is_superuser)
def nuevo(request):
    context = {}
    formulario = FormProducto(request.POST or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('listado')
    context["form"] = formulario
    return render(request, "tienda/add_producto.html", context)


@user_passes_test(lambda u: u.is_superuser)
def eliminar(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == "POST":
        producto.delete()
        return redirect('listado')
    return render(request, 'tienda/delete.html', {"productos": producto})


@user_passes_test(lambda u: u.is_superuser)
def edicion(request, id):
    context = {}
    producto = get_object_or_404(Producto, id=id)
    formulario = FormProducto(request.POST or None, instance=producto)
    if formulario.is_valid():
        formulario.save()
        return redirect('listado')
    context["form"] = formulario
    return render(request, "tienda/update_producto.html", context)


def compra(request):
    productos = Producto.objects.all()
    if request.method == 'POST':
        form = FormFilterProductoMarca(request.POST)
        if form.is_valid():
            nombre_producto = form.cleaned_data.get('nombre')
            marca_seleccionada = form.cleaned_data.get('marca')
            if nombre_producto:
                productos = productos.filter(nombre__icontains=nombre_producto)
            if marca_seleccionada:
                productos = productos.filter(marca=marca_seleccionada)
    else:
        form = FormFilterProductoMarca()
    context = {'form': form, 'productos': productos}
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
            productos = Producto.objects.filter(marca__nombre__icontains=marca_seleccionada)
            print(productos)
    else:
        form = FormMarca()
    context = {'form': form, 'productos': productos}
    return render(request, 'tienda/informes.html', context)


def top_10_productos_vendidos(request):
    context = {}
    if request.method == 'GET':
        productos_vendidos = Compra.objects.values('nombre').annotate(total_unidades_vendidas=Sum('unidades')).order_by(
            '-total_unidades_vendidas')[:10]

        if productos_vendidos:
            ids_productos_vendidos = [producto_vendido['nombre'] for producto_vendido in productos_vendidos]
            top_productos = Producto.objects.filter(id__in=ids_productos_vendidos)
            context = {'top_productos': top_productos, 'productos_vendidos': productos_vendidos}
            print(ids_productos_vendidos)
            print(top_productos)
            print(productos_vendidos.values('total_unidades_vendidas'))
    return render(request, 'tienda/informes.html', context)


def compras_usuario(request):
    compra_user = Compra.objects.all()
    if request.method == 'POST':
        form = FormCompraUser(request.POST)
        if form.is_valid():
            user_seleccionado = form.cleaned_data['users']
            compra_user = Compra.objects.filter(user=user_seleccionado)
    else:
        form = FormCompraUser()
    context = {'forms': form, 'compras_users': compra_user}
    return render(request, 'tienda/informes.html', context)
def top_ten_clientes(request):
    top_clientes = Compra.objects.values('user__username') \
                       .annotate(importe_total=Sum('importe')) \
                       .order_by('-importe_total') \
                       .values('user__username', 'importe_total')[:10]

    context = {'top_clientes': top_clientes}
    return render(request, 'tienda/informes.html', context)
