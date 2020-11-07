from django.shortcuts import get_object_or_404

from .models import Vehicle, VehicleType


class VehicleController:

    @staticmethod
    def get_vehicle_states():
        return Vehicle.STATUS_CHOICES

    @staticmethod
    def get_vehicle_by_id_or_404(id: int):
        return get_object_or_404(Vehicle, id=id)

    @staticmethod
    def update_vehicle(vehicle: Vehicle, data, image):
        vehicle.type = VehicleType.objects.get(short=data['vehicle-type'])
        vehicle.name = data['vehicle-name']
        vehicle.license_plate = data['license-plate']
        vehicle.radio_call_name = data['radio-call-name']
        vehicle.image = image
        vehicle.status = data['state']
        vehicle.seats = data['seats']
        vehicle.save()


class VehicleTypeController:

    @staticmethod
    def get_all_vehicle_types():
        return VehicleType.objects.all()
