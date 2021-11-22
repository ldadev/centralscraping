from django.contrib import admin
from .models import Proveedor,Revisor,Radicacion,Aprobacion

# Register your models here.

#admin.site.register(Proveedor)
#admin.site.register(Revisor)
#admin.site.register(Radicacion)
#admin.site.register(Aprobacion)

@admin.register(Proveedor)
class BookAdmin(admin.ModelAdmin):
    list_display = ('cod', 'name')

@admin.register(Revisor)
class BookAdmin(admin.ModelAdmin):
     list_display = ('cod', 'name')

@admin.register(Radicacion)
class BookAdmin(admin.ModelAdmin):
     list_display = ('Radicacion_id','FechaRadicacion', 'revisor','proveedor','NumeroFactura','ValorFactura','FechaFactura','Estamento')

@admin.register(Aprobacion)
class BookAdmin(admin.ModelAdmin):
         list_display = ('Aprobacion_id','radicacion', 'aprobado','FechaAprobado','aceptado')
