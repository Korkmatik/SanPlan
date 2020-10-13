
from .models import Fahrzeug, FahrzeugTyp


class VehicleController:

    @staticmethod
    def get_vehicle_states():
        states = [state[1] for state in Fahrzeug.STATUS_CHOICES]
        return states


class VehicleTypeController:

    @staticmethod
    def get_all_vehicle_types():
        return FahrzeugTyp.objects.all()