from django.http import response
from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.timezone import make_aware
from datetime import timedelta,datetime
from .models import *

class TaskTests(TestCase):
    def setUp(self):
        testUser = User.objects.create_user(username="JohnDoe",password="DoeTheMan123")
        testUser.save()
        for task_id in range(10):
            Task.objects.create(
                creator=testUser,
                title=("Task No. " + str(task_id)),
                details="This is a test.",
                date_due=make_aware(datetime.now()) + timedelta(days=7),
                priority="3",
            )

    def test_view_url_exists_at_desired_location(self):
        logged = self.client.login(username="JohnDoe",password="DoeTheMan123")
        self.assertTrue(logged)
        response = self.client.get("/todo/")
        self.assertEqual(response.status_code, 200)

    def test_tasklist_url_accessible_by_name(self):
        self.client.login(username="JohnDoe",password="DoeTheMan123")
        response = self.client.get(reverse("task-list"))
        self.assertEqual(response.status_code, 200)

    def test_task_list(self):
        self.client.login(username="JohnDoe",password="DoeTheMan123")
        response = self.client.get(reverse("task-list"))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.context["tasks"]) == 10)
    def test_task_create(self):
        self.client.login(username="JohnDoe",password="DoeTheMan123")
        response = self.client.post("/todo/", data={"title":"View Test","details":"We are testing the ListCreate View","date_due":make_aware(datetime.now()) + timedelta(days=7),"priority":2})
        obj = Task.objects.get(title="View Test",priority=2)
        self.assertEqual(response.status_code,200)
        self.assertTrue(obj.date_added)
        self.assertEqual(obj.title,"View Test")
    def test_task_get(self):
        self.client.login(username="JohnDoe",password="DoeTheMan123")
        obj = Task.objects.get(title="Task No. 1")
        response = self.client.get("/todo/" + str(obj.pk))
        self.assertEqual(response.context["task"],obj)
    def test_task_delete(self):
        self.client.login(username="JohnDoe",password="DoeTheMan123")
        obj = Task.objects.get(title="Task No. 1")
        response = self.client.delete("/todo/" + str(obj.pk))
        self.assertEqual(response.status_code, 200)