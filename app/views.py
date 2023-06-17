from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets



from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework import status
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


class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']

        is_user_valid = True  # Variable para almacenar el resultado de verificación del usuario

        # Realiza aquí la lógica de verificación del usuario
        # Puedes usar cualquier condición o método que desees para determinar si el usuario es válido

        if user.is_active:  # Ejemplo: verifica si el usuario está activo
            is_user_valid = True
        else:
            is_user_valid = False

        return Response({'is_user_valid': is_user_valid}, status=status.HTTP_200_OK)

