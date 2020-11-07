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


class UpdateViewTestCase(TestCase):

    def setUp(self) -> None:
        self.client = Client()
        self.vehicle = VehicleTestCase.createVehicle()[0]
        self.url = reverse('vehicles:update', args=(self.vehicle.id,))
        self.super_user = get_user_model().objects.create_superuser(
            username='vehicles_update',
            password='vehicles_update'
        )
        self.user = get_user_model().objects.create_user(
            username='vehicles_update2',
            password='vehicles_update2'
        )

    def test_get_no_auth(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 302)

        response = self.client.get(self.url, follow=True)
        self.assertContains(response, 'Login')

    def test_get_as_low_priveleged_user(self):

        self.client.force_login(user=self.user)
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 404)

    def test_get(self):
        response = self.__get_response()

        self.assertEqual(response.status_code, 200)
        self.assertContains(
            response,
            '''<input type="text" class="form-control" id="vehicle-name" name="vehicle-name"'''
            f''' placeholder="Fahrzeugname ..." value="{self.vehicle.get_name()}">'''
        )
        self.assertContains(
            response,
            '''<input type="text" class="form-control" id="license-plate" name="license-plate" '''
            f'''placeholder="Kennzeichen ..." value="{self.vehicle.get_license_plate()}" required>'''
        )
        self.assertContains(
            response,
            '''<input type="text" class="form-control" id="radio-call-name" name="radio-call-name" '''
            f'''placeholder="Funkrufname ..." value="{self.vehicle.get_radio_call_name()}">'''
        )
        self.assertContains(
            response,
            '''<input type="number" class="form-control" id="seats" name="seats"'''
            f''' value="{self.vehicle.get_seats()}" required>'''
        )
        self.assertContains(
            response,
            f'''<option value="{self.vehicle.get_type().get_short()}" selected>'''
        )
        self.assertContains(
            response,
            f'''<option value="{self.vehicle.get_status()}" selected>'''
        )

    def test_post_non_admin(self):
        self.client.force_login(user=self.user)

        data = {
            'vehicle-type': self.vehicle.get_type().get_short(),
            'vehicle-name': 'test123',
            'license-plate': 'dsftest123',
            'radio-call-name': 'asdf',
            'image': "",
            'state': self.vehicle.status,
            'seats': 6,
        }

        response = self.client.post(self.url, data=data)

        self.assertEqual(response.status_code, 403)

    def test_post_non_authenticated(self):
        data = {
            'vehicle-type': self.vehicle.get_type().get_short(),
            'vehicle-name': 'test123',
            'license-plate': 'dsftest123',
            'radio-call-name': 'asdf',
            'image': "",
            'state': self.vehicle.status,
            'seats': 6,
        }

        response = self.client.post(self.url, data=data)

        self.assertEqual(response.status_code, 302)

    def test_post_admin(self):
        self.client.force_login(user=self.super_user)
        data = {
            'vehicle-type': self.vehicle.get_type().get_short(),
            'vehicle-name': 'test123',
            'license-plate': 'dsftest123',
            'radio-call-name': 'asdf',
            'image': "",
            'state': self.vehicle.status,
            'seats': 6,
        }

        response = self.client.post(self.url, data=data, follow=True)

        self.assertEqual(response.status_code, 200)

        updated_vehicle = Vehicle.objects.get(id=self.vehicle.id)
        self.assertEqual(updated_vehicle.type.short, data['vehicle-type'])
        self.assertEqual(updated_vehicle.name, data['vehicle-name'])
        self.assertEqual(updated_vehicle.license_plate, data['license-plate'])
        self.assertEqual(updated_vehicle.radio_call_name, data['radio-call-name'])
        self.assertEqual(updated_vehicle.status, data['state'])
        self.assertEqual(updated_vehicle.seats, data['seats'])

    def __get_response(self):
        self.client.force_login(user=self.super_user)
        return self.client.get(self.url)


class CreateVehicleTypeViewTestCase(TestCase):

    def setUp(self) -> None:
        self.client = Client()
        self.url = reverse('vehicles:create_vehicle_type')
        self.user = get_user_model().objects.create_user(username='create_vehicle_type', password='create_vehicle_type')

    def test_get_no_auth(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 302)

        response = self.client.get(self.url, follow=True)
        self.assertContains(response, 'Login')

    def test_get_for_create_authenticated(self):
        response = self.__get_response()

        self.assertEqual(response.status_code, 200)
        self.assertContains(
            response,
            '''<input type="text" class="form-control" id="short" placeholder="z.B. KTW" size="5">'''
        )
        self.assertContains(
            response,
            '''<input type="text" class="form-control" id="name" placeholder="z.B. Krankentransportwagen" size="30">'''
        )
        self.assertContains(
            response,
            '''<script type="module" src="/static/js/vehicles/createVehicleType.js"></script>'''
        )

    def __get_response(self):
        self.client.force_login(user=self.user)
        return self.client.get(self.url)
