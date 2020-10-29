from django.test import TestCase, Client
from django.urls import reverse

from vehicles.models import Vehicle
from vehicles.tests.test_models import VehicleTestCase, VehicleTypeTestCase


def get_template_names(response):
    return [template.name for template in response.templates]


class IndexViewTestCase(TestCase):

    def setUp(self) -> None:
        self.client = Client()
        self.url = reverse('vehicles:index')

    def get_request(self):
        return self.client.get(self.url)

    def test_get_with_no_vehicle(self):
        response = self.get_request()
        template_names = get_template_names(response)

        self.assertEqual(len(response.context['vehicles']), 0)
        self.assertTrue(response.context['vehicleActive'])
        self.assertTrue('vehicles/index.html' in template_names)

    def test_get_with_vehicles(self):
        VehicleTestCase.createVehicle()[0].save()

        response = self.get_request()

        self.assertEqual(len(response.context['vehicles']), 1)


class CreateViewTestCase(TestCase):

    def setUp(self) -> None:
        self.client = Client()
        self.url = reverse('vehicles:create')

    def get_request(self):
        return self.client.get(self.url)

    def test_get_with_no_vehicle_types(self):
        response = self.get_request()

        self.assertTrue(response.context['vehicleActive'])
        self.assertTrue('vehicles/create.html' in get_template_names(response))
        self.assertEqual(len(response.context['states']), len(Vehicle.STATUS_CHOICES))
        self.assertEqual(len(response.context['vehicle_types']), 0)

    def test_get_with_vehicle_types(self):
        num = 4
        for i in range(4):
            VehicleTypeTestCase.createVehicleType(str(i), str(i))[0].save()

        response = self.get_request()

        self.assertTrue(response.context['vehicleActive'])
        self.assertEqual(len(response.context['vehicle_types']), num)