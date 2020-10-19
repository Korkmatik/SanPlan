from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.contrib.auth import get_user_model

from api_v1.vehicles.views import VehicleTypeViewSet
from fahrzeuge.tests.test_models import VehicleTypeTestCase
from fahrzeuge.models import FahrzeugTyp


class VehicleTypeViewSetTestCase(TestCase):

    def setUp(self) -> None:
        self.url = '/api/v1/vehiclestype/'

        self.client = APIClient()
        user_model = get_user_model()

        self.user = user_model.objects.create(username='foo', password='foo')
        self.user.save()
        self.client.force_login(user=self.user)

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
        self.assertEqual(FahrzeugTyp.objects.count(), 2)
        self.assertIsNotNone(FahrzeugTyp.objects.get(name=data['name'], short=data['short']))

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
        self.assertEqual(FahrzeugTyp.objects.count(), 1)
        updated = FahrzeugTyp.objects.get(id=self.vehicle_type.id)
        self.assertEqual(response.data, data)

    def test_delete(self):
        response = self.client.delete(self.url + str(self.vehicle_type.id) + "/")

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(FahrzeugTyp.objects.count(), 0)
