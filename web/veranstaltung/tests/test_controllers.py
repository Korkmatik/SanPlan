from django.test import TestCase
from django.contrib.auth import get_user_model

from veranstaltung.tests.test_models import EventTestCase
from veranstaltung.controllers import VeranstaltungController
from veranstaltung.models import Veranstaltung, Adresse


class EventControllerTestCase(TestCase):

    def setUp(self) -> None:
        user_model = get_user_model()

        self.user_data = {
            'email': 'foo@localhost',
            'password': '#foo123',
            'first_name': 'Foo',
            'last_name': 'Bar',
            'username': 'foo.bar'
        }
        self.user = user_model.objects.create_user(**self.user_data)

        self.event = EventTestCase.create_event()[0]
        self.event.address.save()
        self.event.save()

    def test_get_veranstaltung_by_id(self):
        event: Veranstaltung = VeranstaltungController.get_veranstaltung_by_id(self.event.id)

        self.assertEqual(event.id, self.event.id)
        self.assertEqual(event.titel, self.event.titel)

    def test_get_adresse_by_veranstaltung_id(self):
        address: Adresse = VeranstaltungController.get_adresse_by_veranstaltung_id(self.event.id)

        self.assertEqual(address.id, self.event.address.id)
