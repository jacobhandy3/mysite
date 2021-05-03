from datetime import datetime, timedelta
from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import *

class TaskTestCase(TestCase):
    def setUp(self):
        testUser = User.objects.create(username='JohnDoe',password='DoeTheMan123')
        due1 = datetime.now() + timedelta(hours=24)
        due2 = datetime.now() + timedelta(days=7)
        Task.objects.create(creator=testUser,title="Task no 1",details="This is a test.",date_due=due1,priority=3)
        Task.objects.create(creator=testUser,title="Task no 2",details="This is a test.",date_due=due2,priority=1)
        Task.objects.create(creator=testUser,title="Task no 3",details="This is a test.",date_due=due2,priority=1)
    def test_priority_choices_types(self):
        testTask = Task.objects.get(title="Task no 1",details="This is a test.")
        priority_labels = {1:"high",2:"medium-high",3:"medium",4:"medium-low",5:"low"}
        list_priority_choices = testTask.listPriorities()
        for p in list_priority_choices:
            self.assertEqual(type(p[0]),int)
            self.assertEqual(type(p[1]),str)
            self.assertEqual(p[1],priority_labels[p[0]])
    def test_describe_priority(self):
        testTask1 = Task.objects.get(title="Task no 1",details="This is a test.")
        testTask2 = Task.objects.get(title="Task no 2",details="This is a test.")
        testTask3 = Task.objects.get(title="Task no 3",details="This is a test.")
        self.assertEqual(testTask1.describePriority(),'medium')
        self.assertEqual(testTask2.describePriority(),'high')
        self.assertEqual(testTask3.describePriority(),'high')
    def test_time_remaining(self):
        testTask = Task.objects.get(title="Task no 1",details="This is a test.")
        rem = testTask.date_due.date() - datetime.now(timezone.utc).date()
        days = "%s days"%rem.days
        self.assertEqual(testTask.timeRemaining(),days)
    def test_get_absolute_url(self):
        testTask = Task.objects.get(title="Task no 1",details="This is a test.")
        # This will also fail if the urlconf is not defined.
        self.assertEqual(testTask.get_absolute_url(), ('/todo/' + str(testTask.pk)))