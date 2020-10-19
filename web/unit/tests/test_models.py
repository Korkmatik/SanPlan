from typing import Tuple, Dict, Any

from django.test import TestCase

from unit.models import EVTUnit
from veranstaltung.tests.test_models import EventTestCase


class EVTUnitTestCase(TestCase):

    @staticmethod
    def create_evt_unit(
            unit_leader='Foo Bar',
            unit_second='John Doe',
            trainee='Foo',
            location='Foo location',
            additional_information='foo aditional') -> Tuple[EVTUnit, Dict[str, Any]]:
        data = {
            'event': EventTestCase.create_event()[0],
            'unit_leader': unit_leader,
            'unit_second': unit_second,
            'trainee': trainee,
            'location': location,
            'additional_information': additional_information,
        }

        return EVTUnit.objects.create(**data), data

    def setUp(self) -> None:
        self.evt_unit, self.data = self.create_evt_unit()

    def test_get_leader(self):
        self.assertEqual(self.evt_unit.get_leader(), self.data['unit_leader'])

    def test_get_second(self):
        self.assertEqual(self.evt_unit.get_second(), self.data['unit_second'])

    def test_get_trainee(self):
        self.assertEqual(self.evt_unit.get_trainee(), self.data['trainee'])

    def test_get_location(self):
        self.assertEqual(self.evt_unit.get_location(), self.data['location'])

    def test_get_additional_information(self):
        self.assertEqual(self.evt_unit.get_additional_information(), self.data['additional_information'])

    def test_has_trainee_true(self):
        self.assertTrue(self.evt_unit.has_trainee())

    def test_has_trainee_false(self):
        self.evt_unit.trainee = None
        self.assertFalse(self.evt_unit.has_trainee())

    def test_str_with_trainee(self):
        self.assertEqual(
            str(self.evt_unit),
            f"{self.evt_unit.unit_leader} {self.evt_unit.unit_second} {self.evt_unit.trainee}"
        )

    def test_str_without_trainee(self):
        self.evt_unit.trainee = None
        self.assertEqual(
            str(self.evt_unit),
            f"{self.evt_unit.unit_leader} {self.evt_unit.unit_second}"
        )
