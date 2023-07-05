from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductoViewSet, VentaViewSet, DetalleVentaViewSet, MovimientoViewSet, VentaCreateView,UserViewSet
from .views import CustomAuthToken

# Crea un enrutador para las vistas basadas en ViewSets
router = DefaultRouter()
router.register('productos', ProductoViewSet)
router.register('ventas', VentaViewSet)
router.register('detallesventa', DetalleVentaViewSet)
router.register('movimientos', MovimientoViewSet)
router.register('user', UserViewSet)

urlpatterns = [
    # Agrega las URLs generadas por el enrutador
    path('ventas/create/', VentaCreateView.as_view(), name='venta_create'),
    path('', include(router.urls)),
    path('api/login/', CustomAuthToken.as_view(), name='api_login'),

]
