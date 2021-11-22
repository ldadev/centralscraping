from django.contrib import admin
from .models import Proveedor,Revisor,Radicacion,Aprobacion

# Register your models here.

admin.site.register(Proveedor)
admin.site.register(Revisor)
admin.site.register(Radicacion)
admin.site.register(Aprobacion)