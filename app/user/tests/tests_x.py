"""Tests for the user api endpoint create"""

from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

CONST_URL = reverse('user:crete')


def create_user(**params):
    return get_user_model().objects.create_user(**params)


class PublicUserApiTest(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_create_user(self):

        payload = {
            'email': 'example@test.com',
            'password': 'test123',
            'name': 'Test user',
        }
        res = self.client.post(CONST_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        user = get_user_model().objects.get(email=payload['email'])
        self.assertTrue(user.check_password(payload['email']))
        self.assertNotIn('password', res.dats)

