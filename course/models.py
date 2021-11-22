from django.db import models


"""
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
"""

class Proveedor(models.Model):

	cod = models.CharField(max_length=50,verbose_name="Id")
	name = models.TextField(verbose_name="Nombre")
	
	def __str__(self):
		return f'{self.cod}'


class Revisor(models.Model):

	cod = models.CharField(max_length=50,verbose_name="Id")
	name = models.TextField(verbose_name="Nombre")
	
	def __str__(self):
		return f'{self.cod}'

class Radicacion(models.Model):

	FechaRadicacion = models.DateField(verbose_name="Fecha de radicación")
	revisor = models.ForeignKey(Revisor,on_delete=models.CASCADE,verbose_name="Revisor")
	proveedor = models.ForeignKey(Proveedor,on_delete=models.CASCADE,verbose_name="Proveedor")
	NumeroFactura = models.CharField(max_length=50,verbose_name="Número de factura")
	ValorFactura = models.IntegerField(verbose_name="Valor de la factura")
	FechaFactura =  models.DateField(verbose_name="Fecha de la factura")
	Estamento = models.CharField(max_length=50,verbose_name="Afiliado")

	
	def __str__(self):
		return f'{self.NumeroFactura}'

class Aprobacion(models.Model):

	radicacion = models.ForeignKey(Radicacion,on_delete=models.CASCADE,verbose_name="Radicacion")
	aprobado =  models.CharField(max_length=50,verbose_name="Aprobado si/no")
	fechaparobado = models.DateField(verbose_name="Fecha de aprobación")
	aceptado =  models.CharField(max_length=50,verbose_name="Aceptado si/no")

	
	def __str__(self):
		return f'{self.radicacion}'



	
