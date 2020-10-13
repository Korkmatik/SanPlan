from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .serializers import VehicleTypeSerializer
from fahrzeuge.models import FahrzeugTyp


class VehicleTypeViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]

    queryset = FahrzeugTyp.objects.all()
    serializer_class = VehicleTypeSerializer
