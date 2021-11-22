from django.forms import *
from .models import Revisor,Radicacion,Proveedor,Aprobacion
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render

class RevisorForm(ModelForm):

	class Meta:
		model = Revisor
		fields = 'Cod_Revisor','name'
		widgets = {
		    'Cod_Revisor':TextInput(attrs={'placeholder':'Ingrese el código del revisor','class':'form-control'}),
		    'name':TextInput(attrs={'placeholder':'Ingrese el nombre del revisor','class':'form-control'}),

		}


class ProveedorForm(ModelForm):

	class Meta:
		model = Proveedor
		fields = 'Cod_Proveedor','name'
		widgets = {
		    'Cod_Proveedor':TextInput(attrs={'placeholder':'Ingrese el código del proveedor','class':'form-control'}),
		    'name':TextInput(attrs={'placeholder':'Ingrese el nombre del proveedor','class':'form-control'}),

		}

class AprobacionForm(forms.ModelForm):

	class Meta:
		model = Aprobacion
		fields = 'Aprobacion_Id','radicacion','aprobado','FechaAprobado','aceptado'
		widgets = {
		    'Aprobacion_Id':forms.TextInput(attrs={'placeholder':'Ingrese el código de la aprobación','class':'form-control'}),
            'radicacion':forms.ChoiceField(choices=Radicacion.objects.all()),
            #'radicacion':TextInput(attrs={'placeholder':'Ingrese el código de la radicación','class':'form-control'}),
            'aprobado':forms.TextInput(attrs={'placeholder':'Ingrese si/no','class':'form-control'}),
            'FechaAprobado':forms.TextInput(attrs={'placeholder':'Ingrese el nombre del proveedor','class':'form-control'}),
            'aceptado':forms.TextInput(attrs={'placeholder':'Ingrese si/no','class':'form-control'}),

		}

class RadicacionForm(ModelForm):


	class Meta:
		model = Radicacion
		fields = 'Radicacion_Id','FechaRadicacion','revisor','proveedor','NumeroFactura','ValorFactura','FechaFactura','Estamento'
		widgets = {
		    'Cod_Radicacion':TextInput(attrs={'placeholder':'Ingrese el código de radicación','class':'form-control'}),
		    'FechaRadicacion':TextInput(attrs={'placeholder':'Ingrese la fecha de radicación','class':'form-control'}),
            'revisor':TextInput(attrs={'placeholder':'Ingrese el código del revisor','class':'form-control'}),
		    'proveedor':TextInput(attrs={'placeholder':'Ingrese el nombre del proveedor','class':'form-control'}),
             'NumeroFactura':TextInput(attrs={'placeholder':'Ingrese el número de la factura','class':'form-control'}),
		    'ValorFactura':TextInput(attrs={'placeholder':'Ingrese el valor de la factura','class':'form-control'}),
            'FechaFactura':TextInput(attrs={'placeholder':'Ingrese la fecha de la factura','class':'form-control'}),
            'Estamento':TextInput(attrs={'placeholder':'Ingrese el nombre del estamento','class':'form-control'}),
		}


