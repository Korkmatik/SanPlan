from typing import Tuple, Dict

from django.test import TestCase

from fahrzeuge.models import FahrzeugTyp


class VehicleTypeTestCase(TestCase):

    @staticmethod
    def createVehicleType() -> Tuple[FahrzeugTyp, Dict[str, str]]:
        data = {
            'short': 'KTW',
            'name': 'Krankentransportwagen'
        }
        return FahrzeugTyp(**data), data

    def setUp(self) -> None:
        self.vehicle_type, self.data = self.createVehicleType()

    def test_get_short(self):
        self.assertEqual(
            self.vehicle_type.get_short(),
            self.data['short']
        )

    def test_get_name(self):
        self.assertEqual(
            self.vehicle_type.get_name(),
            self.data['name']
        )
