import itertools
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms
from tienda.models import Producto, Compra, Marca


class FormProducto(ModelForm):
    unidades=forms.IntegerField(min_value=1)
    class Meta:
        model = Producto
        fields = '__all__'


class FormCompra(ModelForm):
    nombre = forms.CharField(required=False)
    class Meta:
        model = Producto
        fields = ['nombre']

class FormCheckout(ModelForm):
    unidades = forms.IntegerField(widget=forms.HiddenInput)
    class Meta:
        model = Producto
        fields = ['unidades']

class FormMarca(forms.Form):
    choices = Marca.objects.all().values_list('nombre', 'nombre')
    empty = [('', '-------')]
    marca = forms.ChoiceField(required=False, choices=itertools.chain(empty, choices.iterator()))

class FormCompraUser(forms.Form):
    users = forms.ModelChoiceField(queryset=User.objects.all(), label='Seleccione un usuario')

class FormFilterProductoMarca(forms.Form):
    nombre = forms.CharField(required=False)
    marca = forms.ModelChoiceField(queryset=Marca.objects.all(), empty_label='Selecciona una marca', required=False)

