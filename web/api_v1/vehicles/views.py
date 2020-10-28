from rest_framework import viewsets

from .serializers import VehicleTypeSerializer, VehicleSerializer
from fahrzeuge.models import FahrzeugTyp, Fahrzeug


class VehicleTypeViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]

    queryset = FahrzeugTyp.objects.all()
    serializer_class = VehicleTypeSerializer


class VehicleViewSet(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]

    queryset = Fahrzeug.objects.all()
    serializer_class = VehicleSerializer
