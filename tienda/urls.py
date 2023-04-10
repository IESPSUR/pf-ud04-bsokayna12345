from django.urls import path
from . import views
urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('tienda/', views.welcome, name='welcome'),
    path('tienda/admin/listado/', views.listado, name='listado'),
    path('tienda/admin/nuevo/', views.nuevo, name='nuevo'),
    path('tienda/admin/eliminar/<int:id>/', views.eliminar, name='eliminar'),
    path('tienda/admin/edicion/<int:id>/', views.edicion, name='edicion'),
    path('tienda/compra/', views.compra, name='compra'),
    path('tienda/checkout/<int:id>', views.checkout, name='checkout'),
    path('tienda/informes', views.informes, name='informes'),
    path('tienda/informes/marca', views.marca, name='marca'),
    path('tienda/informes/top_10_productos_vendidos/', views.top_10_productos_vendidos, name='top_10_productos_vendidos'),
    path('tienda/informes/compras_usuario/', views.compras_usuario, name='compras_usuario'),
    path('tienda/informes/top_ten_clientes/', views.top_ten_clientes, name='top_ten_clientes')
   ]
