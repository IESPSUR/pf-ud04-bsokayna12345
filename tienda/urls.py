from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('tienda/', views.welcome, name='welcome'),
    path('getionProducto/', views.gestionProducto, name='getionProducto'),
    path('tienda/admin/addProducto/', views.nuevo, name='nuevo'),
    path('tienda/admin/delete_view/<str:nombre>', views.delete_view, name='delete_view'),
    path('tienda/admin/update_producto/<str:nombre>', views.update_producto, name='update_producto'),
    path('tienda/admin/realizarCompra/', views.realizarCompra, name='realizarCompra'),
    path('tienda/admin/añadir_carrito/<str:nombre>', views.añadir_carrito, name='añadir_carrito'),
    path('tienda/admin/limpiar_carrito/', views.limpiar_carrito, name='limpiar_carrito')

    #path('tienda/admin/compra/', views.tienda, name='compra'),
    #path('tienda/admin/compra/<str:nombre>', views.compra, name='compra'),
    # path('tienda/admin/addrecord', views.a, name='nuevo'),
]
