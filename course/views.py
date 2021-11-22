from django.shortcuts import render,HttpResponse

import pandas as pd
import requests
from bs4 import BeautifulSoup
import json

from .models import Revisor,Proveedor,Radicacion,Aprobacion
from django.views.generic import ListView

from django.http import JsonResponse

from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .forms import *



class IndexListView(ListView):

	model = Proveedor
	template_name = 'course/main.html'

	def get_food(self):
		res = requests.get("http://vicebienestar.univalle.edu.co/restaurante-universitario")
		soup = BeautifulSoup(res.content,'html')

		table = soup.find_all('table')[0]
		table_data = [[cell.text for cell in row("td")] for row in table.find_all("tr")]

		foods = []
		headers = ['header',[head.text for head in table.find_all("th")]]
		for item in table_data[1:-1]:
			foods.append([item[0],item[1:]])

		#data_foods = json.dumps(dict(foods), ensure_ascii= False)
		data_foods = dict(foods)
		return headers,data_foods


	def get_context_data(self,**kwargs):
		context = super().get_context_data(**kwargs)
		context['headers'],context['foods'] = self.get_food()
		return context


class RevisorListView(ListView):

	model = Revisor
	template_name = 'course/revisor_list.html'

	def get_context_data(self,**kwargs):
		context = super().get_context_data(**kwargs)
		context['revisores'] = Revisor.objects.all() 
		return context

class revisor_create(LoginRequiredMixin,CreateView):
	model = Revisor
	form_class = RevisorForm
	template_name = 'course/revisor_create.html'
	success_url = reverse_lazy('revisor_list')

	def get_context_data(self,**kwargs):
		context = super().get_context_data(**kwargs)
		return context


class revisor_update(LoginRequiredMixin,UpdateView):

	model = Revisor
	form_class = RevisorForm
	template_name = 'course/revisor_create.html'
	success_url = reverse_lazy('revisor_list')


	def get_context_data(self,**kwargs):
		context = super().get_context_data(**kwargs)
		return context


class revisor_delete(LoginRequiredMixin,DeleteView):
    model = Revisor
    template_name = 'course/revisor_delete.html'
    success_url = reverse_lazy('revisor_list')
    url_redirect = success_url


    def get_context_data(self,**kwargs):
    	context = super().get_context_data(**kwargs)
    	return context