from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

# Create your views here.
from rest_framework.permissions import IsAuthenticated
from .models import Producto, Venta, DetalleVenta, Movimiento
from .serializers import ProductoSerializer, VentaSerializer, DetalleVentaSerializer, MovimientoSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer


class VentaViewSet(viewsets.ModelViewSet):
    queryset = Venta.objects.all()
    serializer_class = VentaSerializer


class DetalleVentaViewSet(viewsets.ModelViewSet):
    queryset = DetalleVenta.objects.all()
    serializer_class = DetalleVentaSerializer


class MovimientoViewSet(viewsets.ModelViewSet):
    queryset = Movimiento.objects.all()
    serializer_class = MovimientoSerializer
