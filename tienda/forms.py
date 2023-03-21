from django.forms import ModelForm

from tienda.models import Producto


class FormProducto(ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'

