from rest_framework.test import APIClient
from django.contrib.auth import get_user_model


class ViewSetTestCase:

    def __init__(self):
        self.url = ''
        self.client = None
        self.user = None

    def set_up(self, url: str):
        self.url = f'/api/v1/{url}/'

        self.client = APIClient()
        user_model = get_user_model()

        self.user = user_model.objects.create(username='foo', password='foo')
        self.user.save()
        self.client.force_login(user=self.user)
