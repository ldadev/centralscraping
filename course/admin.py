from django.contrib import admin
from .models import Proveedor,Revisor,Radicacion,Aprobacion

# Register your models here.

#admin.site.register(Proveedor)
#admin.site.register(Revisor)
#admin.site.register(Radicacion)
#admin.site.register(Aprobacion)

@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('id','Cod_Proveedor', 'name')

@admin.register(Revisor)
class RevisorAdmin(admin.ModelAdmin):
     list_display = ('Cod_Revisor', 'name')

@admin.register(Radicacion)
class RadicacionAdmin(admin.ModelAdmin):
     list_display = ('Radicacion_Id','FechaRadicacion', 'revisor','proveedor','NumeroFactura','ValorFactura','FechaFactura','Estamento')

@admin.register(Aprobacion)
class AprobacionAdmin(admin.ModelAdmin):
         list_display = ('Aprobacion_Id','radicacion', 'aprobado','FechaAprobado','aceptado')
