from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('tienda/', views.welcome, name='welcome'),
    path('getionProducto/', views.gestionProducto, name='getionProducto'),
    path('tienda/admin/addProducto/', views.addProducto, name='addProducto'),
    path('tienda/admin/addrecord', views.addrecord, name='addrecord'),
]
