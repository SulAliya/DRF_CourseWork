from rest_framework import status
from rest_framework.test import APITestCase


class HabitsTestCase(APITestCase):
    def setUp(self):
        pass

    def test_create_habit(self):
        """ Тестирование создания привычки."""
        data = {
            "action": "Test",
            "periodicity": 2
        }
        response = self.client.post(
            "habits/",
            data=data
        )
        print(response)

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )
