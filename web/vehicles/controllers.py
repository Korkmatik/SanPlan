
from .models import Vehicle, VehicleType


class VehicleController:

    @staticmethod
    def get_vehicle_states():
        return Vehicle.STATUS_CHOICES


class VehicleTypeController:

    @staticmethod
    def get_all_vehicle_types():
        return VehicleType.objects.all()
