from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from habits.models import Habit
from users.models import User


class HabitTestCase(APITestCase):

    def setUp(self):
        self.user_1 = User.objects.create(email='user1@mail.ru', password='123qwe')
        self.user_2 = User.objects.create(email='user2@mail.ru', password='123qwe')
        self.habit_1 = Habit.objects.create(
            action='Чистить зубы',
            place='Ванная комната',
            duration='60',
            is_pleasurable=False,
            is_public=True,
            user=self.user_1
        )
        self.habit_2 = Habit.objects.create(
            action='Выносить мусор каждый день',
            place='Улица',
            duration='120',
            is_pleasurable=False,
            is_public=False,
            user=self.user_2
        )
        self.client.force_authenticate(user=self.user_1)

    def test_habit_retrieve(self):
        """Тестирование просмотра одной привычки"""
        url_1 = reverse('habits:habit-detail', args=(self.habit_1.pk,))
        response_1 = self.client.get(url_1)
        result_1 = response_1.json()
        self.assertEqual(response_1.status_code, status.HTTP_200_OK)
        self.assertEqual(result_1.get('action'), self.habit_1.action)

        url_2 = reverse('habits:habit-detail', args=(self.habit_2.pk,))
        response_2 = self.client.get(url_2)
        self.assertEqual(response_2.status_code, status.HTTP_404_NOT_FOUND)

    def test_habit_update(self):
        """Тестирование обновления одной привычки"""
        url_1 = reverse('habits:habit-detail', args=(self.habit_1.pk,))
        data = {
            'action': 'Делать зарядку',
            'place': 'Дома',
            'duration': '100',
            'is_pleasurable': False,
        }
        response_1 = self.client.patch(url_1, data=data, format='json')
        result = response_1.json()
        self.assertEqual(response_1.status_code, status.HTTP_200_OK)
        self.assertEqual(result.get('action'), 'Делать зарядку')

        url_2 = reverse('habits:habit-detail', args=(self.habit_2.pk,))
        response_2 = self.client.patch(url_2, data=data, format='json')
        self.assertEqual(response_2.status_code, status.HTTP_404_NOT_FOUND)

    def test_habit_create(self):
        """Тестирование создания привычки"""
        data_1 = {
            'action': 'Делать зарядку',
            'place': 'Дома',
            'duration': '100',
            'is_pleasurable': False,
            'runtime': {'time_1': '07:00'},
            'days_of_week': {'sunday': True}
        }
        response_1 = self.client.post('/habits/', data=data_1, format='json')
        result = response_1.json()
        self.assertEqual(response_1.status_code, status.HTTP_201_CREATED)
        self.assertEqual(result.get('action'), 'Делать зарядку')
        self.assertEqual(Habit.objects.all().count(), 3)

        data_2 = {
            'action': 'Делать зарядку',
            'place': 'Дома',
            'duration': '100',
            'is_pleasurable': False,
            "reward": 'Шоколадка',
            "related_habit": self.habit_1.pk,
            'runtime': {'time_1': '07:00'},
            'days_of_week': {'sunday': True}
        }
        response_2 = self.client.post('/habits/', data=data_2, format='json')
        self.assertEqual(response_2.status_code, status.HTTP_400_BAD_REQUEST)

    def test_habit_destroy(self):
        """Тестирование удаления привычки"""
        url_1 = reverse('habits:habit-detail', args=(self.habit_1.pk,))
        response = self.client.delete(url_1)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Habit.objects.all().count(), 1)

        url_2 = reverse('habits:habit-detail', args=(self.habit_2.pk,))
        response = self.client.delete(url_2)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_habit_list(self):
        """Тестирование получения списка привычек"""
        data = {'id': 6, 'runtime': None, 'days_of_week': None, 'action': 'Чистить зубы',
                'place': 'Ванная комната', 'duration': '00:01:00', 'reward': None,
                'is_pleasurable': False, 'is_public': True, 'user': 5, 'related_habit': None}
        response = self.client.get('/habits/')
        result = response.json().get('results')[0]
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(result, data)

    def test_public_habit_list(self):
        """Тестерование списка публичных привычек"""
        data = {'id': 12, 'runtime': None, 'days_of_week': None, 'action': 'Чистить зубы',
                'place': 'Ванная комната', 'duration': '00:01:00', 'reward': None,
                'is_pleasurable': False, 'is_public': True, 'user': 11, 'related_habit': None}
        response = self.client.get('/habits/list/')
        result = response.json().get('results')[0]
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(result, data)
