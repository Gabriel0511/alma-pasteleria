from django.contrib import admin
from .models import Insumo, Proveedor, CategoriaInsumo, UnidadMedida
# Register your models here.

admin.site.register(Insumo)
admin.site.register(Proveedor)
admin.site.register(CategoriaInsumo)
admin.site.register(UnidadMedida)

