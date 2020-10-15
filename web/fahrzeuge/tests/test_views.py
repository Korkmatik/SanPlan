from django.test import TestCase, Client
from django.urls import reverse


def get_template_names(templates):
    return [template.name for template in templates]


class IndexViewTestCase(TestCase):

    def setUp(self) -> None:
        self.client = Client()
        self.url = reverse('fahrzeuge:index')

    def get_request(self):
        return self.client.get(self.url)

    def test_get_with_no_vehicle(self):
        response = self.get_request()
        template_names = get_template_names(response.templates)

        self.assertEqual(len(response.context['fahrzeuge']), 0)
        self.assertTrue(response.context['vehicleActive'])
        self.assertTrue('fahrzeuge/index.html' in template_names)
