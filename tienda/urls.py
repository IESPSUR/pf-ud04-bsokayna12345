from django.urls import path
from . import views

urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('tienda/', views.welcome, name='welcome'),
    path('getionProducto/', views.gestionProducto, name='getionProducto'),
    path('tienda/admin/addProducto/', views.nuevo, name='nuevo'),
    path('tienda/admin/delete_view/<str:nombre>', views.delete_view, name='delete_view'),
    #path('tienda/admin/update_producto/<str:nombre>', views.update_producto, name='delete_view'),
    # path('tienda/admin/addrecord', views.a, name='nuevo'),
]
