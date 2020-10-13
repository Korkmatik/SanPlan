from rest_framework import viewsets

from .serializers import VehicleTypeSerializer
from fahrzeuge.models import FahrzeugTyp


class VehicleTypeViewSet(viewsets.ModelViewSet):
    queryset = FahrzeugTyp.objects.all()
    serializer_class = VehicleTypeSerializer
