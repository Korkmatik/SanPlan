from typing import Tuple, Dict, Any

from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from events.models import Address, Event


class AddressTestCase(TestCase):

    @staticmethod
    def create_address(
        name: str = 'foo',
        street: str = 'foostr',
        street_number: str = '123',
        postal_code: str = 'foopostal',
        city: str = 'foocity'
    ) -> Tuple[Address, Dict[str, str]]:
        data = {
            'name': name,
            'street': street,
            'street_number': street_number,
            'postal_code': postal_code,
            'city': city
        }

        return Address(**data), data

    def setUp(self) -> None:
        self.Address, self.data = AddressTestCase.create_address()

    def test_get_name(self):
        self.assertEqual(self.Address.get_name(), self.data['name'])

    def test_get_street(self):
        self.assertEqual(self.Address.get_street(), self.data['street'])

    def test_get_city(self):
        self.assertEqual(self.Address.get_city(), self.data['city'])

    def test_has_name_true(self):
        self.assertTrue(self.Address.has_name())

    def test_has_name_none(self):
        self.Address.name = None
        self.assertFalse(self.Address.has_name())

    def test_has_name_empty(self):
        self.Address.name = ''
        self.assertFalse(self.Address.has_name())

    def test_get_google_maps_url_for_street(self):
        expected = "http://maps.google.com/maps?q={} {}, {}".format(
            self.Address.get_street(),
            self.Address.street_number,
            self.Address.get_city()
        )

        self.assertEqual(self.Address.get_google_maps_link_for_street(), expected)

    def test_get_google_maps_url_for_city(self):
        self.assertEqual(
            self.Address.get_google_maps_link_for_city(),
            "http://maps.google.com/maps?q={}".format(self.Address.get_city())
        )

    def test_to_str(self):
        self.assertEqual(str(self.Address), self.data['name'])


class EventTestCase(TestCase):

    @staticmethod
    def create_event() -> Tuple[Event, Dict[str, Any]]:
        addresse = AddressTestCase.create_address()[0]
        addresse.save()
        data = {
            'address': addresse,
            'from_date_time': timezone.datetime(2020, 5, 7),
            'to_date_time': timezone.datetime(2020, 5, 8),
            'title': 'Foobar',
            'contact_person': 'John Doe'
        }

        return Event.objects.create(**data), data

    def setUp(self) -> None:
        self.event, self.data = EventTestCase.create_event()

    def test_get_title(self):
        self.assertEqual(self.event.get_title(), self.data['title'])

    def test_get_from_date_time(self):
        self.assertEqual(self.event.get_from_date_time(), self.data['from_date_time'])

    def test_get_to_date_time(self):
        self.assertEqual(self.event.get_to_date_time(), self.data['to_date_time'])

    def test_get_date(self):
        self.assertEqual(self.event.get_date(), self.data['from_date_time'].strftime("%d. %b %Y"))

    def test_get_address(self):
        self.assertEqual(self.event.get_address(), self.data['address'])

    def test_get_edit_url(self):
        self.event.save()
        self.assertEqual(self.event.get_detail_url(), reverse('events:detail', args=[str(self.event.id), ]))

    def test_has_contact_person_true(self):
        self.assertTrue(self.event.has_contact_person())

    def test_has_contact_person_blank(self):
        self.event.contact_person = ""
        self.assertFalse(self.event.has_contact_person())

    def test_has_contact_person_null(self):
        self.event.contact_person = None
        self.assertFalse(self.event.has_contact_person())

    def test_get_contact_person(self):
        self.assertEqual(self.event.get_contact_person(), self.data['contact_person'])

    def test_to_str(self):
        self.assertEqual(str(self.event), self.data['title'])
