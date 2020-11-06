from typing import Tuple, List, Optional

from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model

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
        self.user = get_user_model().objects.create_user(username='events_index', password='events_index')

    def test_get(self):
        self.client.force_login(user=self.user)
        response = self.client.get(self.url)
        template_names = EventViewTestCase.get_template_names(response)

        self.assertEqual(response.status_code, 200)
        self.assertTrue('events/index.html' in template_names)

    def test_get_no_auth(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 302)

        response = self.client.get(self.url, follow=True)
        self.assertContains(response, 'Login')


class VeranstaltungsViewTestCase(TestCase):

    def setUp(self) -> None:
        self.event = EventTestCase.create_event()[0]
        self.event.save()

        self.url, self.client = EventViewTestCase.setUp('detail', [self.event.id])

        self.user = get_user_model().objects.create_user(username='events_view', password='events_view')

    def test_get(self):
        self.client.force_login(user=self.user)
        response = self.client.get(self.url)
        template_names = EventViewTestCase.get_template_names(response)

        self.assertEqual(response.status_code, 200)
        self.assertTrue('events/detail.html' in template_names)

    def test_get_no_auth(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 302)

        response = self.client.get(self.url, follow=True)
        self.assertContains(response, 'Login')
