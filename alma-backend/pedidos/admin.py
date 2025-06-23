# admin.py
from django.contrib import admin
from .models import Pedido, DetallePedido, IngredientesExtra, Cliente

class IngredienteExtraInline(admin.TabularInline):
    model = IngredientesExtra
    extra = 1

class DetallePedidoAdmin(admin.ModelAdmin):
    inlines = [IngredienteExtraInline]

class DetallePedidoInline(admin.StackedInline):
    model = DetallePedido
    extra = 1

class PedidoAdmin(admin.ModelAdmin):
    inlines = [DetallePedidoInline]

admin.site.register(Cliente)
admin.site.register(Pedido, PedidoAdmin)
admin.site.register(DetallePedido, DetallePedidoAdmin)
