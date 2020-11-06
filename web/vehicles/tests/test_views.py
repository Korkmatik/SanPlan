from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model

from vehicles.models import Vehicle
from vehicles.tests.test_models import VehicleTestCase, VehicleTypeTestCase


def get_template_names(response):
    return [template.name for template in response.templates]


class IndexViewTestCase(TestCase):

    def setUp(self) -> None:
        self.client = Client()
        self.url = reverse('vehicles:index')
        self.user = get_user_model().objects.create_user(username='vehicles_index', password='vehicles_index')

    def get_request(self):
        self.client.force_login(user=self.user)
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

    def test_get_no_auth(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 302)

        response = self.client.get(self.url, follow=True)
        self.assertContains(response, 'Login')


class CreateViewTestCase(TestCase):

    def setUp(self) -> None:
        self.client = Client()
        self.url = reverse('vehicles:create')
        self.user = get_user_model().objects.create_user(username='vehicles_create', password='vehicles_create')

    def get_request(self):
        self.client.force_login(user=self.user)
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

    def test_get_no_auth(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 302)

        response = self.client.get(self.url, follow=True)
        self.assertContains(response, 'Login')
