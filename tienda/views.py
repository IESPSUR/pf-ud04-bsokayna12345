from sqlite3 import IntegrityError
from time import timezone
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import login_required
from django.contrib.postgres.search import SearchVector, SearchQuery
from django.db import transaction
from django.db.models import Sum
from django.shortcuts import render, get_object_or_404, redirect

from tienda.forms import FormProducto
from tienda.models import Producto, Compra, Marca


# Create your views here.
def welcome(request):
    return render(request, 'tienda/index.html', {})


def listProducto(request):
    context = {}
    productos = Producto.objects.all()
    context["datos"] = productos
    return render(request, "tienda/admin/listProducto.html", context)

@user_passes_test(lambda u: u.is_superuser)
def add_producto(request):
    context = {}
    formulario = FormProducto(request.POST or None)
    if formulario.is_valid():
        formulario.save()
    context["form"] = formulario
    return render(request, "tienda/admin/add_producto.html", context)

@user_passes_test(lambda u: u.is_superuser)
def delet_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == "POST":
        producto.delete()
    return render(request, 'tienda/admin/delete.html', {"productos": producto})

@user_passes_test(lambda u: u.is_superuser)
def update_producto(request, id):
    context = {}
    producto = get_object_or_404(Producto, id=id)
    formulario = FormProducto(request.POST or None, instance=producto)
    if formulario.is_valid():
        formulario.save()
    context["form"] = formulario
    return render(request, "tienda/admin/update_producto.html", context)


def detalle_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    return render(request, 'tienda/detalle_producto.html', {'producto': producto})


def compra(request):
    productos = Producto.objects.all()
    context = {'productos': productos}
    return render(request, 'tienda/compra.html', context)


def buscar(request):
    # x = "articulo x es :%r " % request.GET["prd"]
    # y = "articulo y es :%r" % request.GET["prd2"]
    context = {}
    context['datos'] = Producto.objects.all()
    if request.GET["prd"]:
        nombre_producto = request.GET["prd"]
        producto_encotrado = Producto.objects.filter(nombre__icontains=nombre_producto)
        if producto_encotrado:
            context['datos'] = producto_encotrado
        else:
            return redirect('compra')
    else:
        context['datos']
    return render(request, "tienda/compra_producto_buscado.html", context)

@transaction.atomic()
def ckeckout(request, id):
    producto = get_object_or_404(Producto, id=id)
    if request.method == 'POST':
        unidades = int(request.POST.get('unidades', 0))
        try:
            producto.compra(unidades=unidades, user=request.user)
        except ValueError as e:
            error_message = str(e)
        else:
            return redirect('detalle_producto', id=producto.id)
    else:
        error_message = None
    return render(request, 'tienda/comprar_producto.html', {'producto': producto, 'error_message': error_message})


def informes(request):
    return render(request, 'tienda/informes.html', {})


def marcas(request):
    marcas = Marca.objects.all()
    return render(request, 'tienda/informe_marca.html', {'marcas': marcas})


def producto_marca(requets, id):
    productos = Producto.objects.filter(marca_id=id)
    return render(requets, 'tienda/producto_marca.html', {'productos': productos})


def top_10_productos_vendidos(request):
    productos_vendidos = Compra.objects.values('nombre').annotate(total_unidades_vendidas=Sum('unidades')).order_by(
        '-total_unidades_vendidas')[:1]
    ids_productos_vendidos = [producto_vendido['nombre'] for producto_vendido in productos_vendidos]
    top_productos = Producto.objects.filter(id__in=ids_productos_vendidos)
    context = {'top_productos': top_productos}
    return render(request, 'tienda/productoMasVendido.html', context)
def compras_usuario(request, id):
    compras = Compra.objects.filter(user_id=id)
    context = {'compras': compras}
    return render(request, 'tienda/compras_usuario.html', context)
@login_required
def top_ten_clientes(request):
    top_clientes = Compra.objects.values('user__username') \
                                 .annotate(importe_total=Sum('importe')) \
                                 .order_by('-importe_total') \
                                 .values('user__username', 'importe_total')[:10]

    context = {'top_clientes': top_clientes}
    return render(request, 'tienda/top_ten_clientes.html', context)