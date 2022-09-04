from django.contrib import admin
from .models import Fabricante,Componente, Producto
# Register your models here.

admin.site.register(Fabricante)
admin.site.register(Componente)
admin.site.register(Producto)