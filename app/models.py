from django.db import models
from django.contrib.auth.models import User



class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField()
    stock = models.PositiveIntegerField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)

class Venta(models.Model):
    total = models.DecimalField(max_digits=10, decimal_places=2)
    fecha = models.DateTimeField(auto_now_add=True)
    direccion_envio = models.CharField(max_length=200)
    metodo_pago = models.CharField(max_length=100)
    cliente = models.CharField(max_length=50)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

class DetalleVenta(models.Model):
    cantidad = models.PositiveIntegerField()
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE, default=1)
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE)

class Movimiento(models.Model):
    TIPO_CHOICES = [
        ('ENTRADA', 'Entrada'),
        ('SALIDA', 'Salida'),
    ]
    tipo = models.CharField(max_length=100, choices=TIPO_CHOICES)
    fecha = models.DateTimeField(auto_now_add=True)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2)
    motivo = models.TextField()
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
