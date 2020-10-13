from rest_framework import serializers

from fahrzeuge.models import FahrzeugTyp


class VehicleTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FahrzeugTyp
        fields = ('id', 'short', 'name')
