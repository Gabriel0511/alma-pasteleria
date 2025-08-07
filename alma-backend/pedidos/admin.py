from django.contrib import admin
from .models import Pedido, DetallePedido, IngredientesExtra, Cliente

class IngredienteExtraInline(admin.TabularInline):
    model = IngredientesExtra
    extra = 1
    fields = ('insumo', 'cantidad', 'UnidadMedida')  # Corregido: 'ingrediente' -> 'insumo' (nombre real del campo)
    # autocomplete_fields removido ya que no hay search_fields configurados en InsumoAdmin

class DetallePedidoInline(admin.StackedInline):
    model = DetallePedido
    extra = 1
    fields = ('receta', 'cantidad', 'observaciones')  # Campos reales del modelo
    show_change_link = True

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    inlines = [DetallePedidoInline]
    list_display = ('id', 'cliente', 'fecha_pedido', 'estado')  # Corregido: 'fecha' -> 'fecha_pedido'
    list_filter = ('estado', 'fecha_pedido')  # Corregido: 'fecha' -> 'fecha_pedido'
    search_fields = ('cliente__nombre', 'id')

@admin.register(DetallePedido)
class DetallePedidoAdmin(admin.ModelAdmin):
    inlines = [IngredienteExtraInline]
    list_display = ('pedido', 'receta', 'cantidad')  # Corregido: 'producto' -> 'receta'
    list_filter = ('pedido__cliente',)

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    search_fields = ('nombre', 'telefono')