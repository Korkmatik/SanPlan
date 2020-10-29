from typing import Tuple, List, Optional

from django.test import TestCase, Client
from django.urls import reverse

from events.tests.test_models import EventTestCase


class EventViewTestCase:

    @staticmethod
    def setUp(url: str, args: Optional[List] = None) -> Tuple[str, Client]:

        if args is None:
            url = reverse('events:' + url)
        else:
            url = reverse('events:' + url, args=args)
        client = Client()
        return url, client

    @staticmethod
    def get_template_names(response) -> List[str]:
        return [template.name for template in response.templates]


class IndexViewTestCase(TestCase):

    def setUp(self) -> None:
        self.url, self.client = EventViewTestCase.setUp('index')

    def test_get(self):
        response = self.client.get(self.url)
        template_names = EventViewTestCase.get_template_names(response)

        self.assertEqual(response.status_code, 200)
        self.assertTrue('events/index.html' in template_names)


class VeranstaltungsViewTestCase(TestCase):

    def setUp(self) -> None:
        self.event = EventTestCase.create_event()[0]
        self.event.save()

        self.url, self.client = EventViewTestCase.setUp('detail', [self.event.id])

    def test_get(self):
        response = self.client.get(self.url)
        template_names = EventViewTestCase.get_template_names(response)

        self.assertEqual(response.status_code, 200)
        self.assertTrue('events/detail.html' in template_names)
