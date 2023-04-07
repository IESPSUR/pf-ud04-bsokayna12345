from django.core.validators import MinValueValidator
from django.forms import ModelForm
from django import forms

from tienda.models import Producto, Compra


class FormProducto(ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'


class FormCompra(ModelForm):
    nombre = forms.CharField(required=False)

    class Meta:
        model = Producto
        fields = ['nombre']


class FormCheckout(ModelForm):
    unidades = forms.IntegerField(widget=forms.NumberInput(attrs={'readonly': 'readonly'}))
    class Meta:
        model = Producto
        fields = ['unidades']
