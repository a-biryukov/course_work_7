from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from users.models import User


class UserTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email='user@mail.ru', password='123qwe')
        self.user1 = User.objects.create(email='user1@mail.ru', password='123qwe')

    def test_user_create(self):
        data = {'email': 'user2@mail.ru', 'password': '123qwe'}
        response = self.client.post('/users/', data=data)
        result = response.json()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(result.get('email'), 'user2@mail.ru')
        self.assertEqual(User.objects.all().count(), 3)

    def test_user_retrieve(self):
        self.client.force_authenticate(user=self.user)

        url = reverse('users:user-detail', args=(self.user.pk,))
        response = self.client.get(url)
        result = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(result.get('email'), 'user@mail.ru')

        url = reverse('users:user-detail', args=(self.user1.pk,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_user_update(self):
        self.client.force_authenticate(user=self.user)

        data = {'email': 'user3@mail.ru'}
        url = reverse('users:user-detail', args=(self.user.pk,))
        response = self.client.patch(url, data=data)
        result = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(result.get('email'), 'user3@mail.ru')

        url = reverse('users:user-detail', args=(self.user1.pk,))
        response = self.client.patch(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_user_destroy(self):

        self.client.force_authenticate(user=self.user)

        url = reverse('users:user-detail', args=(self.user.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(User.objects.all().count(), 1)

        url = reverse('users:user-detail', args=(self.user1.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_user_list(self):
        data = [{'email': 'user@mail.ru'}, {'email': 'user1@mail.ru'}]
        self.client.force_authenticate(user=self.user)
        response = self.client.get('/users/')
        result = response.json().get('results')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(result, data)