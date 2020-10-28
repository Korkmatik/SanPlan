
from .models import Fahrzeug, FahrzeugTyp


class VehicleController:

    @staticmethod
    def get_vehicle_states():
        return Fahrzeug.STATUS_CHOICES


class VehicleTypeController:

    @staticmethod
    def get_all_vehicle_types():
        return FahrzeugTyp.objects.all()
