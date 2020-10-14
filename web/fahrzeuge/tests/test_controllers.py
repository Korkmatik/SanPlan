from django.test import TestCase

from fahrzeuge.controllers import VehicleController, VehicleTypeController
from fahrzeuge.models import Fahrzeug


class VehicleControllerTestCase(TestCase):

    def test_get_vehicle_states(self):
        self.assertListEqual(
            VehicleController.get_vehicle_states(),
            Fahrzeug.STATUS_CHOICES
        )

