from django.test import TestCase
from .serializers import TaskSerializer
from .models import Task
from rest_framework.test import APIClient
from rest_framework import status


#Integration test for the serializer
class TaskSerializerTestCase(TestCase):
    def test_serializer_valid_data(self):
        valid_data = {
            'text': 'Sample Task',
            'day': 'Monday',
            'reminder': False,
        }
        serializer = TaskSerializer(data=valid_data)
        self.assertTrue(serializer.is_valid())



#Unit test for the api endpoint
class TaskAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.task_data = {
            'text': 'Sample Task',
            'day': 'Monday',
            'reminder': False,
        }
        self.task = Task.objects.create(**self.task_data)
        self.endpoint = '/api/tasks/'

    def test_get_task_list(self):
        response = self.client.get(self.endpoint)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_task(self):
        response = self.client.post(self.endpoint, self.task_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 2)

    def test_get_task_detail(self):
        response = self.client.get(f'{self.endpoint}{self.task.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['text'], self.task.text)

    def test_update_task(self):
        updated_data = {
            'text': 'Updated Task',
            'day': 'Tuesday',
            'reminder': True,
        }
        response = self.client.put(f'{self.endpoint}{self.task.id}/', updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.task.refresh_from_db()
        self.assertEqual(self.task.text, updated_data['text'])
        self.assertEqual(self.task.day, updated_data['day'])
        self.assertEqual(self.task.reminder, updated_data['reminder'])

    def test_partial_update_task(self):
        updated_data = {
            'text': 'Updated Task',
        }
        response = self.client.patch(f'{self.endpoint}{self.task.id}/', updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.task.refresh_from_db()
        self.assertEqual(self.task.text, updated_data['text'])

    def test_delete_task(self):
        response = self.client.delete(f'{self.endpoint}{self.task.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Task.objects.count(), 0)
