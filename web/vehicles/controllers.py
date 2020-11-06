from django.shortcuts import get_object_or_404

from .models import Vehicle, VehicleType


class VehicleController:

    @staticmethod
    def get_vehicle_states():
        return Vehicle.STATUS_CHOICES

    @staticmethod
    def get_vehicle_by_id_or_404(id: int):
        return get_object_or_404(Vehicle, id=id)


class VehicleTypeController:

    @staticmethod
    def get_all_vehicle_types():
        return VehicleType.objects.all()
