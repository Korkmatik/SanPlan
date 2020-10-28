from rest_framework import serializers

from vehicles.models import VehicleType, Vehicle


class VehicleTypeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = VehicleType
        fields = ('id', 'short', 'name')

    def create(self, validated_data):
        vehicleType = VehicleType.objects.get_or_create(
            name=validated_data['name'],
            short=validated_data['short']
        )[0]

        return vehicleType


class VehicleSerializer(serializers.HyperlinkedModelSerializer):
    type = VehicleTypeSerializer()

    class Meta:
        model = Vehicle
        fields = ('id', 'name', 'license_plate', 'radio_call_name', 'image', 'status', 'seats', 'type')

    def create(self, validated_data):
        # Create or get the vehicle type
        vehicle_type = VehicleType.objects.get(short=validated_data['type']['short'])

        # Creating and returning the vehicle
        return Vehicle.objects.create(
            type=vehicle_type,
            name=validated_data['name'],
            license_plate=validated_data['license_plate'],
            radio_call_name=validated_data['radio_call_name'],
            image=validated_data.get('image'),
            status=validated_data['status'],
            seats=validated_data['seats']
        )

    def update(self, instance, validated_data):
        # Updating the vehicle type
        vehicle_type_data = validated_data.pop('type')
        vehicle_type = VehicleType.objects.get(
            short=vehicle_type_data['short']
        )

        # Updating the vehicle
        instance.name = validated_data['name']
        instance.license_plate = validated_data['license_plate']
        instance.radio_call_name = validated_data['radio_call_name']
        instance.status = validated_data['status']
        instance.seats = validated_data['seats']
        instance.type = vehicle_type
        instance.image = validated_data['image']

        instance.save()
        return instance
