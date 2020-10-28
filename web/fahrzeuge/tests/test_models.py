from typing import Tuple, Dict, Any
from unittest import mock

from django.test import TestCase

from fahrzeuge.models import FahrzeugTyp, Fahrzeug, fahrzeug_images


class VehicleTypeTestCase(TestCase):

    @staticmethod
    def createVehicleType(short='KTW', name='Krankentransportwagen') -> Tuple[FahrzeugTyp, Dict[str, str]]:
        data = {
            'short': short,
            'name': name
        }
        return FahrzeugTyp.objects.create(**data), data

    def setUp(self) -> None:
        self.vehicle_type, self.data = self.createVehicleType()

    def test_get_short(self):
        self.assertEqual(
            self.vehicle_type.get_short(),
            self.data['short']
        )

    def test_get_name(self):
        self.assertEqual(
            self.vehicle_type.get_name(),
            self.data['name']
        )


class VehicleTestCase(TestCase):

    @staticmethod
    def createVehicle() -> Tuple[Fahrzeug, Dict[str, Any]]:
        data = {
            "typ": VehicleTypeTestCase.createVehicleType()[0],
            "name": "Foo",
            "kennzeichen": "FO FO 43",
            "funkrufname": "FO FO 72/1",
            "image": None,
            "status": Fahrzeug.VERFUEGBAR,
            "seats": 3
        }

        return Fahrzeug.objects.create(**data), data

    def setUp(self) -> None:
        self.vehicle, self.data = VehicleTestCase.createVehicle()

    def test_get_name(self):
        self.assertEqual(
            self.vehicle.get_name(),
            self.data["name"]
        )

    def test_get_kennzeichen(self):
        self.assertEqual(
            self.vehicle.get_kennzeichen(),
            self.data["kennzeichen"]
        )

    def test_get_funkrufname(self):
        self.assertEqual(
            self.vehicle.get_funkrufname(),
            self.data['funkrufname']
        )

    def test_get_typ(self):
        self.assertEqual(
            self.vehicle.get_typ().id,
            self.data["typ"].id
        )

    def test_get_status(self):
        self.assertEqual(
            self.vehicle.get_status(),
            self.data["status"]
        )

    def test_has_name_with_name(self):
        self.assertTrue(
            self.vehicle.has_name()
        )

    def test_has_name_with_blank_name(self):
        self.vehicle.name = ""
        self.vehicle.save()

        self.assertFalse(
            self.vehicle.has_name()
        )

    def test_has_name_with_name_none(self):
        self.vehicle.name = None
        self.vehicle.save()

        self.assertFalse(
            self.vehicle.has_name()
        )

    def test_is_available_as_available(self):
        self.assertTrue(
            self.vehicle.is_verfuegbar()
        )

    def test_is_available_as_not_available(self):
        self.vehicle.status = Fahrzeug.NICHT_VERFUEGBAR
        self.vehicle.save()

        self.assertFalse(
            self.vehicle.is_verfuegbar()
        )

    def test_str_method(self):
        self.assertEqual(
            str(self.vehicle),
            self.data['kennzeichen']
        )

    def test_get_image_path(self):
        image_url = 'foo'
        self.vehicle.image = mock.MagicMock()
        self.vehicle.image.image_url = mock.MagicMock()
        self.vehicle.image.image_url.url = image_url

        self.assertEqual(
            self.vehicle.get_image_path(),
            image_url
        )

    @mock.patch('fahrzeuge.models.os.path.join')
    def test_vehicle_images_path(self, mock_join):
        mock_join.side_effect = 'f'
        filename = 'foo'
        instance = mock.MagicMock()
        instance.id = 'foobar'

        ret = fahrzeug_images(instance, filename)

        mock_join.assert_called_with('vehicle', instance.id, filename)
        self.assertEqual(ret, 'f')
