from django import forms

from tienda.models import Producto


class FormularioProducto(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'

