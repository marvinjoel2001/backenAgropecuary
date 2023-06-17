from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductoViewSet, VentaViewSet, DetalleVentaViewSet, MovimientoViewSet
from .views import CustomAuthToken
# Crea un enrutador para las vistas basadas en ViewSets
router = DefaultRouter()
router.register('productos', ProductoViewSet)
router.register('ventas', VentaViewSet)
router.register('detallesventa', DetalleVentaViewSet)
router.register('movimientos', MovimientoViewSet)


urlpatterns = [
    # Agrega las URLs generadas por el enrutador
    path('', include(router.urls)),
    path('api/login/', CustomAuthToken.as_view(), name='api_login'),
]