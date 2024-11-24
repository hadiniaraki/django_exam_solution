from django.test import TestCase
from .models import Task
from django.contrib.auth.models import User

class TaskModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.task = Task.objects.create(user=self.user, title='Test Task')

    def test_task_creation(self):
        self.assertEqual(self.task.title, 'Test Task')
        self.assertFalse(self.task.completed)

    def test_task_str(self):
        self.assertEqual(str(self.task), 'Test Task')
