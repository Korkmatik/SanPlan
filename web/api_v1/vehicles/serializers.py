from rest_framework import serializers

from fahrzeuge.models import FahrzeugTyp, Fahrzeug


class VehicleTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FahrzeugTyp
        fields = ('id', 'short', 'name')

    def create(self, validated_data):
        vehicleType = FahrzeugTyp.objects.get_or_create(
            name=validated_data['name'],
            short=validated_data['short']
        )[0]

        return vehicleType


class VehicleSerializer(serializers.HyperlinkedModelSerializer):
    typ = VehicleTypeSerializer()

    class Meta:
        model = Fahrzeug
        fields = ('id', 'name', 'kennzeichen', 'funkrufname', 'image', 'status', 'seats', 'typ')

    def create(self, validated_data):
        # Create or get the vehicle type
        vehicle_type = FahrzeugTyp.objects.get(short=validated_data['typ']['short'])

        # Creating and returning the vehicle
        return Fahrzeug.objects.create(
            typ=vehicle_type,
            name=validated_data['name'],
            kennzeichen=validated_data['kennzeichen'],
            funkrufname=validated_data['funkrufname'],
            image=validated_data.get('image'),
            status=validated_data['status'],
            seats=validated_data['seats']
        )

    def update(self, instance, validated_data):
        # Updating the vehicle type
        vehicle_type_data = validated_data.pop('typ')
        vehicle_type = FahrzeugTyp.objects.get(
            short=vehicle_type_data['short']
        )

        # Updating the vehicle
        instance.name = validated_data['name']
        instance.kennzeichen = validated_data['kennzeichen']
        instance.funkrufname = validated_data['funkrufname']
        instance.status = validated_data['status']
        instance.seats = validated_data['seats']
        instance.typ = vehicle_type
        instance.image = validated_data['image']

        instance.save()
        return instance
