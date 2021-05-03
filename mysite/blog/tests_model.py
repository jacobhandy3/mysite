from datetime import datetime, timedelta
from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import *

class PostTestCase(TestCase):
    def setUp(self):
        testUser = User.objects.create(username='JohnDoe',password='DoeTheMan123')
        Post.objects.create(author=testUser,title="Test Post no 1",subtitle="Testing my Django model methods.",slug="test-post-no-1",content="This is a test for the Post model.",visible=True)
        Post.objects.create(author=testUser,title="Test Post no 2",subtitle="Testing my Django model methods again.",slug="test-post-no-2",content="This is a 2nd test for the Post model.")
        Post.objects.create(author=testUser,title="Test Post no 3",subtitle="Testing my Django model methods again again.",slug="test-post-no-3",content="This is a 3rd test for the Post model.",visible=True)
    def test_get_absolute_url(self):
        testPost = Post.objects.get(title="Test Post no 1",subtitle="Testing my Django model methods.")
        # This will also fail if the urlconf is not defined.
        self.assertEqual(testPost.get_absolute_url(), ('/blog/' + str(testPost.slug)))
    def test_pub_or_prive(self):
        testPostPub = Post.objects.get(title="Test Post no 1",subtitle="Testing my Django model methods.")
        testPostPriv = Post.objects.get(title="Test Post no 2",subtitle="Testing my Django model methods again.")
        self.assertEqual(testPostPub.pub_or_priv(),'Public')
        self.assertEqual(testPostPriv.pub_or_priv(), 'Private')
    def test_get_username(self):
        testPost = Post.objects.get(title="Test Post no 1",subtitle="Testing my Django model methods.")
        self.assertEqual(testPost.get_username(),'JohnDoe')