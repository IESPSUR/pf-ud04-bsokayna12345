from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('tienda/', views.welcome, name='welcome'),
    path('getionProducto/', views.gestionProducto, name='getionProducto'),
    path('tienda/admin/addProducto/', views.nuevo, name='nuevo'),
  #  path('tienda/admin/addrecord', views.a, name='nuevo'),
]
