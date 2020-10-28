from rest_framework import viewsets

from .serializers import VehicleTypeSerializer, VehicleSerializer
from vehicles.models import VehicleType, Vehicle


class VehicleTypeViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]

    queryset = VehicleType.objects.all()
    serializer_class = VehicleTypeSerializer


class VehicleViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]

    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
