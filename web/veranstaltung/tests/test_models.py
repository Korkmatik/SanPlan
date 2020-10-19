from typing import Tuple, Dict, Any
import datetime

from django.test import TestCase
from django.urls import reverse

from veranstaltung.models import Adresse, Veranstaltung


class AddressTestCase(TestCase):

    @staticmethod
    def create_address(
        name: str = 'foo',
        street: str = 'foostr',
        street_number: str = '123',
        postal_code: str = 'foopostal',
        city: str = 'foocity'
    ) -> Tuple[Adresse, Dict[str, str]]:
        data = {
            'name': name,
            'strasse': street,
            'strassenNummer': street_number,
            'plz': postal_code,
            'ort': city
        }

        return Adresse(**data), data

    def setUp(self) -> None:
        self.Address, self.data = AddressTestCase.create_address()

    def test_get_name(self):
        self.assertEqual(self.Address.get_name(), self.data['name'])

    def test_get_street(self):
        self.assertEqual(self.Address.get_strasse(), self.data['strasse'])

    def test_get_city(self):
        self.assertEqual(self.Address.get_ort(), self.data['ort'])

    def test_has_name_true(self):
        self.assertTrue(self.Address.has_name())

    def test_has_name_none(self):
        self.Address.name = None
        self.assertFalse(self.Address.has_name())

    def test_has_name_empty(self):
        self.Address.name = ''
        self.assertFalse(self.Address.has_name())

    def test_get_google_maps_url_for_street(self):
        self.assertEqual(
            self.Address.get_google_maps_link_for_strasse(),
            "http://maps.google.com/maps?q={}, {}".format(self.Address.get_strasse(), self.Address.get_ort())
        )

    def test_get_google_maps_url_for_city(self):
        self.assertEqual(
            self.Address.get_google_maps_link_for_ort(),
            "http://maps.google.com/maps?q={}".format(self.Address.get_ort())
        )

    def test_to_str(self):
        self.assertEqual(str(self.Address), self.data['name'])


class EventTestCase(TestCase):

    @staticmethod
    def create_event() -> Tuple[Veranstaltung, Dict[str, Any]]:
        addresse = AddressTestCase.create_address()[0]
        addresse.save()
        data = {
            'address': addresse,
            'vonDateTime': datetime.datetime(2020, 5, 7),
            'bisDateTime': datetime.datetime(2020, 5, 8),
            'titel': 'Foobar',
            'ansprechPartner': 'John Doe'
        }

        return Veranstaltung.objects.create(**data), data

    def setUp(self) -> None:
        self.event, self.data = EventTestCase.create_event()

    def test_get_titel(self):
        self.assertEqual(self.event.get_titel(), self.data['titel'])

    def test_get_von_date_time(self):
        self.assertEqual(self.event.get_von_date_time(), self.data['vonDateTime'])

    def test_get_bis_date_time(self):
        self.assertEqual(self.event.get_bis_date_time(), self.data['bisDateTime'])

    def test_get_date(self):
        self.assertEqual(self.event.get_date(), self.data['vonDateTime'].strftime("%d. %b %Y"))

    def test_get_adresse(self):
        self.assertEqual(self.event.get_adresse(), self.data['address'])

    def test_get_edit_url(self):
        self.event.save()
        self.assertEqual(self.event.get_edit_url(), reverse('veranstaltung:detail', args=[str(self.event.id),]))

    def test_has_ansprechpartner(self):
        self.assertTrue(self.event.has_ansprechpartner())

    def test_get_ansprechpartner(self):
        self.assertEqual(self.event.get_ansprechpartner(), self.data['ansprechPartner'])

    def test_to_str(self):
        self.assertEqual(str(self.event), self.data['titel'])
