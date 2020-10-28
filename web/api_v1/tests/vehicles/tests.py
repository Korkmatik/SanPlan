from django.test import TestCase
from rest_framework import status

from api_v1.tests.ViewSetTestCase import ViewSetTestCase
from vehicles.tests.test_models import VehicleTypeTestCase, VehicleTestCase
from vehicles.models import VehicleType, Vehicle


class VehicleTypeViewSetTestCase(TestCase, ViewSetTestCase):

    def setUp(self) -> None:
        self.set_up('vehiclestype')

        self.vehicle_type = VehicleTypeTestCase.createVehicleType()[0]
        self.vehicle_type.save()

    def test_get(self):
        response = self.client.get(self.url)

        self.expected_data = [{
            'id': self.vehicle_type.id,
            'short': self.vehicle_type.short,
            'name': self.vehicle_type.name,
        }]

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)
        self.assertListEqual(response.data, self.expected_data)

    def test_post(self):
        data = {
            'short': 'Foo',
            'name': 'Foobar',
        }
        response = self.client.post(self.url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(VehicleType.objects.count(), 2)
        self.assertIsNotNone(VehicleType.objects.get(name=data['name'], short=data['short']))

    def test_update_name(self):
        data = {
            'id': self.vehicle_type.id,
            'short': self.vehicle_type.short,
            'name': 'Foo'
        }
        self.update_test(data)

    def test_update_short(self):
        data = {
            'id': self.vehicle_type.id,
            'short': 'Foo',
            'name': self.vehicle_type.name
        }
        self.update_test(data)

    def update_test(self, data):
        response = self.client.put(self.url + str(self.vehicle_type.id) + "/", data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(VehicleType.objects.count(), 1)
        VehicleType.objects.get(id=self.vehicle_type.id)
        self.assertEqual(response.data, data)

    def test_delete(self):
        response = self.client.delete(self.url + str(self.vehicle_type.id) + "/")

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(VehicleType.objects.count(), 0)


class VehicleSerializerTestCase(TestCase, ViewSetTestCase):

    def setUp(self) -> None:
        self.set_up('vehicles')

        self.vehicle, self.data = VehicleTestCase.createVehicle()
        self.vehicle.save()

    def test_get(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['id'], self.vehicle.id)

    def test_post(self):
        data = {
            'name': 'Foo',
            'license_plate': 'fo ds 3',
            'radio_call_name': 'fo 72/1',
            'status': 'VB',
            'seats': 3,
            'image': None,
            'type': {
                'short': self.data['type'].short,
                'name': self.data['type'].name
            }
        }
        response = self.client.post(self.url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(VehicleType.objects.count(), 1)
        self.assertEqual(Vehicle.objects.count(), 2)

    def test_update(self):
        data = {
            'id': self.vehicle.id,
            'name': 'Foo',
            'license_plate': 'fo ds 3',
            'radio_call_name': 'fo 72/1',
            'status': 'VB',
            'seats': 3,
            'image': None,
            'type': {
                'id': self.vehicle.type.id,
                'short': self.vehicle.type.short,
                'name': self.vehicle.type.name,
            }
        }
        response = self.client.put(self.url + str(self.vehicle.id) + "/", data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
