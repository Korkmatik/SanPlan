from django.test import TestCase
from django.contrib.auth import get_user_model

from veranstaltung.controllers import VeranstaltungController
from veranstaltung.models import Veranstaltung


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

    def test_get_veranstaltung_by_username_no_event(self):
        events = VeranstaltungController.get_veranstaltung_by_username(self.user_data['username'])

        self.assertEqual(len(events), 0)
