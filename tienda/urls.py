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
    path('tienda/buscar/', views.buscar, name='cuscar'),
    path('tienda/checkout/<int:id>/', views.ckeckout, name='checkout'),
    path('tienda/detalleProducto/<int:id>/', views.detalle_producto, name='detalle_producto'),
    path('tienda/informes/', views.informes, name='informes'),
    path('tienda/informes/marcas/', views.marcas, name='marcas'),
    path('tienda/informes/producto_marcas/<int:id>/', views.producto_marca, name='producto_marcas'),
    path('tienda/informes/productoMasVendido/', views.top_10_productos_vendidos, name='productoMasVendido'),
    path('tienda/informes/compras_usuario/<int:id>/', views.compras_usuario, name='compras_usuario'),
    path('tienda/informes/clente/', views.top_ten_clientes, name='cliente'),
    path('filtrar_productos/', views.filtrar_productos, name='filtrarProducto'),
]
