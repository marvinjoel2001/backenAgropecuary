from django.contrib.auth import get_user_model
from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework import generics
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
from rest_framework.permissions import IsAuthenticated
from .models import Producto, Venta, DetalleVenta, Movimiento
from .serializers import ProductoSerializer, VentaSerializer, DetalleVentaSerializer, MovimientoSerializer
from rest_framework import generics
from .models import Venta, DetalleVenta, Movimiento
from .serializers import VentaSerializer, DetalleVentaSerializer, MovimientoSerializer,UserSerializer
from rest_framework.permissions import AllowAny
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import AllowAny
from .models import User


class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer

    def perform_create(self, serializer):
        producto = serializer.save()

        # Crear movimiento de entrada
        cantidad = serializer.validated_data['stock']
        motivo = f"Agregado de producto #{producto.id}"
        usuario = get_user_model().objects.get(id=1)

        movimiento = Movimiento.objects.create(tipo='ENTRADA', cantidad=cantidad, motivo=motivo,
                                               usuario=usuario, producto=producto)

        return movimiento

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        producto = self.perform_create(serializer)

        headers = self.get_success_headers(serializer.data)
        return Response({'producto': serializer.data, 'movimiento': MovimientoSerializer(producto).data}, status=status.HTTP_201_CREATED, headers=headers)
class VentaViewSet(viewsets.ModelViewSet):
    queryset = Venta.objects.all()
    serializer_class = VentaSerializer


class VentaCreateView(generics.CreateAPIView):
    queryset = Venta.objects.all()
    serializer_class = VentaSerializer
    permission_classes = [AllowAny]  # Permitir cualquier tipo de autenticación o permiso

    def perform_create(self, serializer):
        venta = serializer.save()
        detalle_venta_data = self.request.data.get('detalle_venta')
        detalles_venta = []

        if detalle_venta_data:
            for detalle_data in detalle_venta_data:
                detalle_data['venta'] = venta.id
                detalle_serializer = DetalleVentaSerializer(data=detalle_data)
                detalle_serializer.is_valid(raise_exception=True)
                detalles_venta.append(detalle_serializer.save())

                # Obtener el usuario de la venta
                usuario_id = self.request.data.get('usuario')

        if not detalles_venta:
            raise ValidationError("Debe proporcionar al menos un detalle de venta.")

        # Generar movimiento de salida
        for detalle in detalles_venta:
            producto_id = detalle.producto.id
            cantidad = detalle.cantidad
            motivo = f"Venta #{venta.id}"
            Movimiento.objects.create(
                producto_id=producto_id,
                tipo="SALIDA",
                cantidad=-cantidad,
                motivo=motivo,
                usuario_id=usuario_id
            )
class DetalleVentaViewSet(viewsets.ModelViewSet):
    queryset = DetalleVenta.objects.all()
    serializer_class = DetalleVentaSerializer


class MovimientoViewSet(viewsets.ModelViewSet):
    queryset = Movimiento.objects.all()
    serializer_class = MovimientoSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

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
