from django.contrib import admin
from .models import Receta, RecetaInsumo
# Register your models here.

class RecetaInsumoInline(admin.TabularInline):
    model = RecetaInsumo
    extra = 1
    
class RecetaAdmin(admin.ModelAdmin):
    inlines = [RecetaInsumoInline]

admin.site.register(Receta)
admin.site.register(RecetaInsumo)