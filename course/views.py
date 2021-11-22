from django.shortcuts import render,HttpResponse

import pandas as pd
import requests
from bs4 import BeautifulSoup
import json

from .models import Signature
from django.views.generic import ListView

from django.http import JsonResponse



class IndexListView(ListView):

	model = Signature
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

	