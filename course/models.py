from django.db import models


class Signature(models.Model):

	title = models.CharField(max_length=50,verbose_name="Titulo")
	description = models.TextField(verbose_name="Descripción")
	
	def __str__(self):
		return f'{self.title}'


class Teacher(models.Model):

	name = models.CharField(max_length=50,verbose_name="Nombre")
	course = models.ForeignKey(Signature,on_delete=models.CASCADE,verbose_name="Curso")
	
	def __str__(self):
		return f'{self.name}'



	
