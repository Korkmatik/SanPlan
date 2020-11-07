from django.test import TestCase
from django.http import Http404

from vehicles.controllers import VehicleController, VehicleTypeController
from vehicles.models import Vehicle
from vehicles.tests.test_models import VehicleTypeTestCase, VehicleTestCase


class VehicleControllerTestCase(TestCase):

    def test_get_vehicle_states(self):
        self.assertListEqual(
            VehicleController.get_vehicle_states(),
            Vehicle.STATUS_CHOICES
        )

    def test_get_vehicle_by_id_with_non_existing_vehicle(self):
        self.assertRaises(Http404, VehicleController.get_vehicle_by_id_or_404, id=10)

    def test_get_vehicle_by_id_with_existing_vehicle(self):
        vehicle = VehicleTestCase.createVehicle()[0]

        return_vehicle = VehicleController.get_vehicle_by_id_or_404(vehicle.id)

        self.assertEqual(return_vehicle.id, vehicle.id)
        self.assertEqual(return_vehicle.name, vehicle.name)
        self.assertEqual(return_vehicle.license_plate, vehicle.license_plate)
        self.assertEqual(return_vehicle.radio_call_name, vehicle.radio_call_name)
        self.assertEqual(return_vehicle.status, vehicle.status)
        self.assertEqual(return_vehicle.seats, vehicle.seats)

    def test_update_vehicle(self):
        vehicle_type = VehicleTypeTestCase.createVehicleType('foo', 'foobar')[0]
        vehicle = VehicleTestCase.createVehicle()[0]

        data = {
            'vehicle-type': vehicle_type.short,
            'vehicle-name': 'test123',
            'license-plate': 'dsftest123',
            'radio-call-name': 'asdf',
            'image': None,
            'state': vehicle.WORKSHOP,
            'seats': 6,
        }

        VehicleController.update_vehicle(vehicle, data, None)
        updated_vehicle = Vehicle.objects.get(id=vehicle.id)

        self.assertEqual(updated_vehicle.type.short, vehicle_type.short)
        self.assertEqual(updated_vehicle.name, data['vehicle-name'])
        self.assertEqual(updated_vehicle.license_plate, data['license-plate'])
        self.assertEqual(updated_vehicle.radio_call_name, data['radio-call-name'])
        self.assertEqual(updated_vehicle.status, data['state'])
        self.assertEqual(updated_vehicle.seats, data['seats'])


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
