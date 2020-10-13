from django.urls import include, path

from rest_framework import routers

from .vehicles import views as vehicle_views


router = routers.DefaultRouter()
router.register(r'vehiclestype', vehicle_views.VehicleTypeViewSet)
router.register(r'vehicles', vehicle_views.VehicleViewSet)

app_name = 'api_v1'
urlpatterns = [
    path('', include(router.urls)),
]