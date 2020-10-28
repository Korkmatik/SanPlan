from django.test import TestCase

from vehicles.controllers import VehicleController, VehicleTypeController
from vehicles.models import Fahrzeug
from vehicles.tests.test_models import VehicleTypeTestCase


class VehicleControllerTestCase(TestCase):

    def test_get_vehicle_states(self):
        self.assertListEqual(
            VehicleController.get_vehicle_states(),
            Fahrzeug.STATUS_CHOICES
        )


class VehicleTypeControllerTestCase(TestCase):

    def test_get_all_vehicle_types_with_no(self):
        self.assertEqual(
            len(VehicleTypeController.get_all_vehicle_types()),
            0
        )

    def test_get_all_vehicle_types_with_one(self):
        VehicleTypeTestCase.createVehicleType()

        self.assertEqual(
            len(VehicleTypeController.get_all_vehicle_types()),
            1
        )

    def test_get_all_vehicle_types_with_multiple(self):
        num = 3
        for i in range(3):
            VehicleTypeTestCase.createVehicleType(short=str(i), name=str(i))

        self.assertEqual(
            len(VehicleTypeController.get_all_vehicle_types()),
            num
        )
