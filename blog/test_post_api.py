from datetime import datetime
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.utils import timezone
from pytz import UTC
from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient

from blog.models import Post


class PostApiTestCase(TestCase):
  def setUp(self):
    self.u1 = get_user_model().objects.create_user(
      email='test1@example.com', password='password'
    )
    self.u2 = get_user_model().objects.create_user(
      email='test2@example.com', password='password'
    )

    posts = [
      Post.objects.create(
        author=self.u1,
        published_at=timezone.now(),
        title='Test post 1',
        slug='test-post-1',
        summary='Post 1 summary',
        content='Post 1 content',
      ),
      Post.objects.create(
        author=self.u2,
        published_at=timezone.now(),
        title='Test post 2',
        slug='test-post-2',
        summary='Post 2 summary',
        content='Post 2 content',
      ),
    ]

    self.post_lookup = {p.id: p for p in posts}
    self.client = APIClient()
    token = Token.objects.create(user=self.u1)
    self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

  def test_post_list(self):
    response = self.client.get('/api/v1/posts/')
    response_data = response.json()['results']
    self.assertEqual(len(response_data), 2)

    for post_data in response_data:
      post_obj = self.post_lookup[post_data['id']]
      self.assertEqual(post_obj.title, post_data['title'])
      self.assertEqual(post_obj.title, post_data['title'])
      self.assertEqual(post_obj.title, post_data['title'])
      self.assertEqual(post_obj.title, post_data['title'])
      self.assertEqual(post_obj.title, post_data['title'])
      self.assertEqual(post_obj.title, post_data['title'])
      
