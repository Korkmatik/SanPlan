from typing import Tuple, Dict, Any

from django.test import TestCase

from veranstaltung.models import Adresse


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