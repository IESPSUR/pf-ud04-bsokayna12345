from django.urls import path
from . import views


urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('tienda/', views.welcome, name='welcome'),
    path('tienda/admin/listarProductos/', views.listProducto, name='listProducto'),
    path('tienda/admin/addProducto/', views.add_producto, name='addProducto'),
    path('tienda/admin/<id>/deleteProducto/', views.delet_producto, name='delete'),
    path('tienda/admin/<id>/updateProducto/', views.update_producto, name='update'),
    path('tienda/compra/', views.compra, name='compra'),
    path('tienda/checkout/<int:id>', views.checkout, name='checkout'),
   ]
