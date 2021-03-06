from django.forms import forms
from django import forms
from django.forms.widgets import HiddenInput
from .models import Revisor,Radicacion,Proveedor,Aprobacion
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render

class RevisorForm(forms.ModelForm):

	class Meta:
		model = Revisor
		fields = 'Cod_Revisor','name'
		widgets = {
		    'Cod_Revisor':forms.TextInput(attrs={'placeholder':'Ingrese el código del revisor','class':'form-control'}),
		    'name':forms.TextInput(attrs={'placeholder':'Ingrese el nombre del revisor','class':'form-control'}),

		}


class ProveedorForm(forms.ModelForm):

	class Meta:
		model = Proveedor
		fields = 'Cod_Proveedor','name'
		widgets = {
		    'Cod_Proveedor':forms.TextInput(attrs={'placeholder':'Ingrese el código del proveedor','class':'form-control'}),
		    'name':forms.TextInput(attrs={'placeholder':'Ingrese el nombre del proveedor','class':'form-control'}),

		}

class AprobacionForm(forms.ModelForm):

	class Meta:
		model = Aprobacion
		fields = 'Aprobacion_Id','radicacion','aprobado','FechaAprobado','aceptado'
		widgets = {
		    'Aprobacion_Id':forms.TextInput(attrs={'placeholder':'Ingrese el código de la aprobación','class':'form-control'}),
            'radicacion':forms.Select(choices=Radicacion.objects.all(),attrs={'placeholder':'Ingrese la radicación','class':'form-control'}),
            #'radicacion':TextInput(attrs={'placeholder':'Ingrese el código de la radicación','class':'form-control'}),
            'aprobado':forms.TextInput(attrs={'placeholder':'Ingrese si/no','class':'form-control'}),
            'FechaAprobado':forms.DateInput(attrs={'type':'date','class':'form-control'}),
            'aceptado':forms.TextInput(attrs={'placeholder':'Ingrese si/no','class':'form-control'}),

		}

class RadicacionForm(forms.ModelForm):


	class Meta:
		model = Radicacion
		fields = 'Radicacion_Id','FechaRadicacion','revisor','proveedor','NumeroFactura','ValorFactura','FechaFactura','Estamento'
		widgets = {
		    'Cod_Radicacion':forms.TextInput(attrs={'placeholder':'Ingrese el código de radicación','class':'form-control'}),
		    'FechaRadicacion':forms.DateInput(attrs={'type':'date','class':'form-control'}),
            #'revisor':forms.TextInput(attrs={'placeholder':'Ingrese el código del revisor','class':'form-control'}),
             'revisor':forms.Select(choices=Revisor.objects.all(),attrs={'class':'form-control'}),
		    #'proveedor':forms.TextInput(attrs={'placeholder':'Ingrese el nombre del proveedor','class':'form-control'}),
             'proveedor':forms.Select(choices=Proveedor.objects.all(),attrs={'placeholder':'Ingrese el proveedor','class':'form-control'}),
             'NumeroFactura':forms.TextInput(attrs={'placeholder':'Ingrese el número de la factura','class':'form-control'}),
		    'ValorFactura':forms.TextInput(attrs={'placeholder':'Ingrese el valor de la factura','class':'form-control'}),
            'FechaFactura': forms.DateInput(attrs={'type':'date','class':'form-control'}),
            'Estamento':forms.TextInput(attrs={'placeholder':'Ingrese el nombre del estamento','class':'form-control'}),
		}


