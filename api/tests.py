from django.test import TestCase

from rest_framework.test import APITestCase
from rest_framework import status
# Create your tests here.


class hello(APITestCase):

    def testhello(self):
        response = self.client.get('/v1/user/hello')
        # print(response.status_code)
        self.assertEqual(response, {"hello"})