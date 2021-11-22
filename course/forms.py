from django.forms import *
from .models import Revisor
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
	