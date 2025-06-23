from django.db import models
from django.utils import timezone
from datetime import timedelta

# --- PROVEEDORES ---
class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.nombre

# --- INSUMOS ---
class Insumo(models.Model):
    TIPOS_INSUMO = [
        ('harina', 'Harina'),
        ('azucares', 'Azúcares'),
        ('huevos', 'Huevos'),
        ('grasas', 'Grasas'),
        ('lacteos', 'Leche y productos lácteos'),
        ('levaduras', 'Levaduras'),
        ('esencias', 'Esencias y aromas'),
        ('colorantes', 'Colorantes'),
        ('frutas', 'Frutas'),
        ('frutos_secos', 'Frutos secos'),
        ('chocolates', 'Chocolates'),
        ('otros', 'Otros'),
    ]
    UNIDAD_MEDIDA = [
        ('g', 'Gramos'),
        ('kg', 'Kilogramos'),
        ('ml', 'Mililitros'),
        ('l', 'Litros'),
        ('unidad', 'Unidad'),
    ]

    nombre = models.CharField(max_length=100)
    tipo_insumo = models.CharField(max_length=50, choices=TIPOS_INSUMO)
    unidad_medida = models.CharField(max_length=10, choices=UNIDAD_MEDIDA)
    stock_actual = models.PositiveIntegerField()
    stock_minimo = models.PositiveIntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.nombre
