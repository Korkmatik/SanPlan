from typing import Dict, Tuple

from django.test import TestCase
from django.db.utils import IntegrityError

from staff.models import Qualification


class QualificationTestCase(TestCase):

    @staticmethod
    def create_qualification(
            title: str = 'Rettungssanitäter',
            short: str = "RS") -> Tuple[Qualification, Dict[str, str]]:
        data = {
            "title": title,
            "short": short
        }

        return Qualification.objects.create(**data), data

    def setUp(self) -> None:
        self.qualification, self.data = QualificationTestCase.create_qualification()

    def test_init(self):
        self.assertEqual(self.qualification.title, self.data['title'])
        self.assertEqual(self.qualification.short, self.data['short'])

    def test_title_unique(self):
        self.assertRaises(IntegrityError, QualificationTestCase.create_qualification, ['Rettungssanitäter', 'foo'])

    def test_short_unique(self):
        self.assertRaises(IntegrityError, QualificationTestCase.create_qualification, ['foo', 'RS'])

    def test_str(self):
        expected = self.data['title']
        self.assertEqual(str(self.qualification), expected)
