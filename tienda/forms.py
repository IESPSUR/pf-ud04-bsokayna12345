from django.core.validators import MinValueValidator
from django.forms import ModelForm
from django import forms

from tienda.models import Producto, Compra


class FormProducto(ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'


class FormCompra(ModelForm):
    class Meta:
        model = Compra
        unidades = forms.IntegerField(validators=[MinValueValidator(0)])
