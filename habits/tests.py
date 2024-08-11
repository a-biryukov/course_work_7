from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from habits.models import Habit
from users.models import User


class HabitTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email='user@mail.ru', password='123qwe')
        self.habit = Habit.objects.create(
                action='Чистить зубы',
                place='Ванная комната',
                duration='60',
                is_pleasurable=False,
                is_public=True,
                user=self.user
        )
        self.client.force_authenticate(user=self.user)

    def test_habit_retrieve(self):
        """Тестирование просмотра одной привычки"""
        url = reverse('habits:habit-detail', args=(self.habit.pk,))
        response = self.client.get(url)
        result = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(result.get('action'), self.habit.action)

    def test_habit_update(self):
        """Тестирование обновления одной привычки"""
        url = reverse('habits:habit-detail', args=(self.habit.pk,))
        data = {
            'action': 'Делать зарядку',
            'place': 'Дома',
            'duration': '100',
            'is_pleasurable': False,
        }
        response = self.client.patch(url, data=data, format='json')
        result = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(result.get('action'), 'Делать зарядку')
        self.assertEqual(Habit.objects.all().count(), 1)

    def test_habit_create(self):
        """Тестирование создания привычки"""
        data = {
            'action': 'Делать зарядку',
            'place': 'Дома',
            'duration': '100',
            'is_pleasurable': False,
            'runtime': {'time_1': '07:00'},
            'days_of_week': {'sunday': True}
        }
        self.client.force_authenticate(user=self.user)
        response = self.client.post('/habits/', data=data, format='json')
        result = response.json()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(result.get('action'), 'Делать зарядку')
        self.assertEqual(Habit.objects.all().count(), 2)

    def test_habit_delete(self):
        """Тестирование удаления привычки"""
        url = reverse('habits:habit-detail', args=(self.habit.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Habit.objects.all().count(), 0)

    def test_habit_list(self):
        """Тестирование получения списка привычек"""
        data = {'id': 4, 'runtime': None, 'days_of_week': None, 'action': 'Чистить зубы',
                'place': 'Ванная комната', 'duration': '00:01:00', 'reward': None,
                'is_pleasurable': False, 'is_public': True, 'user': 3, 'related_habit': None}
        response = self.client.get('/habits/')
        result = response.json().get('results')[0]
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(result, data)

    def test_public_habit_list(self):
        """Тестерование списка публичных привычек"""
        data = {'id': 7, 'runtime': None, 'days_of_week': None, 'action': 'Чистить зубы',
                'place': 'Ванная комната', 'duration': '00:01:00', 'reward': None,
                'is_pleasurable': False, 'is_public': True, 'user': 6, 'related_habit': None}
        response = self.client.get('/habits/list/')
        result = response.json().get('results')[0]
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(result, data)
