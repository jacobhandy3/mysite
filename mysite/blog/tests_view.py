from django.http import response
from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.timezone import make_aware
from datetime import timedelta,datetime
from .models import *

class postTests(TestCase):
    def setUp(self):
        testUser = User.objects.create(username='JohnDoe',password='DoeTheMan123')
        for post_id in range(10):
            Post.objects.create(
                author=testUser,
                title=("post No. " + str(post_id)),
                subtitle="Testing my Django model methods.",
                slug=("test-post-no-" + str(post_id)),
                content="This is a test for the post model.",
                visible=True
            )
    
    def test_view_url_exists_at_desired_location(self):
        self.client.login(username='JohnDoe',password='DoeTheMan123')
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)
    def test_postlist_url_accessible_by_name(self):
        self.client.login(username='JohnDoe',password='DoeTheMan123')
        response = self.client.get(reverse('post-list'))
        self.assertEqual(response.status_code, 200)

    def test_post_list(self):
        self.client.login(username='JohnDoe',password='DoeTheMan123')
        response = self.client.get(reverse('post-list'))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.context['post_list']) == 10)
    def test_post_create(self):
        self.client.login(username='JohnDoe',password='DoeTheMan123')
        response = self.client.post('/blog', data={})
        obj = Post.objects.get(title='View Test')
        self.assertEqual(response.context,obj)
    def test_post_get(self):
        self.client.login(username='JohnDoe',password='DoeTheMan123')
        obj = Post.objects.get(pk=0)
        response = self.client.get('/blog/' + obj.slug)
        self.assertEqual(response.context['post'],obj)
    def test_post_put(self):
        self.client.login(username='JohnDoe',password='DoeTheMan123')
        obj = Post.objects.get(title="post No. 1")
        newData = {}
        response = self.client.put('/blog/' + obj.slug,data=newData)
        self.assertEqual()
    def test_post_delete(self):
        self.client.login(username='JohnDoe',password='DoeTheMan123')
        response = self.client.delete('/blog/test-post-no-1')
        self.assertEqual(response.status_code, 200)