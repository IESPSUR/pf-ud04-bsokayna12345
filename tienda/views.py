from django.shortcuts import render

# Create your views here.
def welcome(request):
    return render(request,'tienda/index.html', {})
def gestionDeProducto(request):
    return render(request,'tienda/gestion_productos.html', {})
