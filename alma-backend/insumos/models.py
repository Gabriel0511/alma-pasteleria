from django.db import models
from django.utils import timezone
from datetime import timedelta

# --- UNIDADES DE MEDIDA ---
class UnidadMedida(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    abreviatura = models.CharField(max_length=10, unique=True)
    descripcion = models.TextField(blank=True, null=True)
    
    def __str__(self):
        return f"{self.nombre} ({self.abreviatura})"

# --- PROVEEDORES ---
class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.nombre
    
# --- CATEGORIAS DE INSUMOS ---
class CategoriaInsumo(models.Model):
    nombre = models.CharField(max_length=50, unique=True)
    descripcion = models.TextField(blank=True, null=True)
    
    class Meta:
        verbose_name = "Categoría de Insumo"
        verbose_name_plural = "Categorías de Insumos"
        ordering = ['nombre']
    
    def __str__(self):
        return self.nombre

# --- INSUMOS ---
class Insumo(models.Model):
    nombre = models.CharField(max_length=100)
    categoria = models.ForeignKey(
        CategoriaInsumo,
        on_delete=models.PROTECT,
        null=True,  # Permite valores nulos
        blank=True,  # Opcional para el admin
        verbose_name="Categoria de insumo"
    )
    unidad_medida = models.ForeignKey(UnidadMedida, on_delete=models.PROTECT)
    stock_actual = models.PositiveIntegerField()
    stock_minimo = models.PositiveIntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.SET_NULL, null=True, blank=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre
    
    @property
    def necesita_reposicion(self):
        return self.stock_actual < self.stock_minimo
    
    class Meta:
        verbose_name = "Insumo"
        verbose_name_plural = "Insumos"
        ordering = ['nombre']