from django.test import TestCase
from django.contrib.auth import get_user_model

from events.tests.test_models import EventTestCase
from events.controllers import EventController
from events.models import Event, Address


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
        event: Event = EventController.get_event_by_id(self.event.id)

        self.assertEqual(event.id, self.event.id)
        self.assertEqual(event.title, self.event.title)

    def test_get_adresse_by_veranstaltung_id(self):
        address: Address = EventController.get_adresse_by_event_id(self.event.id)

        self.assertEqual(address.id, self.event.address.id)
