from django.contrib import admin
from .models import Proveedor,Revisor,Radicacion,Aprobacion

# Register your models here.

#admin.site.register(Proveedor)
#admin.site.register(Revisor)
#admin.site.register(Radicacion)
#admin.site.register(Aprobacion)

@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    list_display = ('cod', 'name')

@admin.register(Revisor)
class RevisorAdmin(admin.ModelAdmin):
     list_display = ('cod', 'name')

@admin.register(Radicacion)
class RadicacionAdmin(admin.ModelAdmin):
     list_display = ('radicacion_id','FechaRadicacion', 'revisor','proveedor','NumeroFactura','ValorFactura','FechaFactura','Estamento')

@admin.register(Aprobacion)
class AprobacionAdmin(admin.ModelAdmin):
         list_display = ('aprobacion_id','radicacion', 'aprobado','FechaAprobado','aceptado')
