from django.forms import *
from .models import Revisor,Radicacion,Proveedor,Aprobacion
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render

class RevisorForm(ModelForm):

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

	class Meta:
		model = Revisor
		fields = 'Cod_Revisor','name'
		widgets = {
		    'Cod_Revisor':TextInput(attrs={'placeholder':'Ingrese el código del revisor','class':'form-control'}),
		    'name':TextInput(attrs={'placeholder':'Ingrese el nombre del revisor','class':'form-control'}),

		}


class ProveedorForm(ModelForm):

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

	class Meta:
		model = Proveedor
		fields = 'Cod_Proveedor','name'
		widgets = {
		    'Cod_Proveedor':TextInput(attrs={'placeholder':'Ingrese el código del proveedor','class':'form-control'}),
		    'name':TextInput(attrs={'placeholder':'Ingrese el nombre del proveedor','class':'form-control'}),

		}

class AprobacionForm(ModelForm):

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

	class Meta:
		model = Aprobacion
		fields = 'Aprobacion_Id','radicacion','aprobado','FechaAprobado','aceptado'
		widgets = {
		    'Aprobacion_Id':TextInput(attrs={'placeholder':'Ingrese el código de la aprobación','class':'form-control'}),
		    'radicacion':TextInput(attrs={'placeholder':'Ingrese el código de la radicación','class':'form-control'}),
            'aprobado':TextInput(attrs={'placeholder':'Ingrese si/no','class':'form-control'}),
            'FechaAprobado':DateField(attrs={'placeholder':'Ingrese el nombre del proveedor','class':'form-control'}),
            'aceptado':TextInput(attrs={'placeholder':'Ingrese si/no','class':'form-control'}),

		}

class RadicacionForm(ModelForm):

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

	class Meta:
		model = Radicacion
		fields = 'Radicacion_Id','FechaRadicacion','Revisor','proveedor''NumeroFactura','ValorFactura','FechaFactura','Estamento'
		widgets = {
		    'Cod_Radicacion':TextInput(attrs={'placeholder':'Ingrese el código de radicación','class':'form-control'}),
		    'FechaRadicacion':TextInput(attrs={'placeholder':'Ingrese la fecha de radicación','class':'form-control'}),
             'Revisor':TextInput(attrs={'placeholder':'Ingrese el código del revisor','class':'form-control'}),
		    'proveedor':TextInput(attrs={'placeholder':'Ingrese el nombre del proveedor','class':'form-control'}),
             'NumeroFactura':TextInput(attrs={'placeholder':'Ingrese el número de la factura','class':'form-control'}),
		    'ValorFactura':TextInput(attrs={'placeholder':'Ingrese el valor de la factura','class':'form-control'}),
            'FechaFactura':DateField(attrs={'placeholder':'Ingrese la fecha de la factura','class':'form-control'}),
            'Estamento':DateField(attrs={'placeholder':'Ingrese el nombre del estamento','class':'form-control'}),
		}


