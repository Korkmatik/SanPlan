from rest_framework import serializers

from fahrzeuge.models import FahrzeugTyp, Fahrzeug


class VehicleTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FahrzeugTyp
        fields = ('id', 'short', 'name')


class VehicleSerializer(serializers.HyperlinkedModelSerializer):
    typ = VehicleTypeSerializer()

    class Meta:
        model = Fahrzeug
        fields = (
            'id', 'name', 'kennzeichen', 'funkrufname', 'image', 'status', 'typ', 'seats'
        )

    def create(self, validated_data):
        # Create or get the vehicle type
        vehicle_type = FahrzeugTyp.objects.get_or_create(
            name=validated_data['typ']['name'],
            short=validated_data['typ']['short'],
        )[0]

        # Creating and returning the vehicle
        return Fahrzeug.objects.create(
            typ=vehicle_type,
            name=validated_data['name'],
            kennzeichen=validated_data['kennzeichen'],
            funkrufname=validated_data['funkrufname'],
            image=validated_data['image'],
            status=validated_data['status'],
            seats=validated_data['seats']
        )

    def update(self, instance, validated_data):
        # Updating the vehicle type
        vehicle_type_data = validated_data.pop('typ')
        vehicle_type = instance.typ
        vehicle_type.name = vehicle_type_data['name']
        vehicle_type.short = vehicle_type_data['short']
        vehicle_type.save()

        # Updating the vehicle
        instance.name = validated_data['name']
        instance.kennzeichen = validated_data['kennzeichen']
        instance.funkrufname = validated_data['funkrufname']
        instance.status = validated_data['status']
        instance.seats = validated_data['seats']
        instance.typ = vehicle_type

        if validated_data['image'] != None:
            instance.image = validated_data['image']

        instance.save()
        return instance
