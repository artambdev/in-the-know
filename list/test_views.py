from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
from .forms import PostForm
from .models import Post

class TestBlogViews(TestCase):

    def setUp(self):
        self.user = User.objects.create_superuser(
            username="userName",
            password="passWord",
            email="sample@email.com"
        )
        self.post = Post(author=self.user,
                         slug="post-name", content="Post content",
                         hidden=False)
        self.post.save()

    def test_render_post_detail_page_with_reply_form(self):
        response = self.client.get(reverse(
            'view_post', args=['post-name']))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Post content", response.content)
        self.assertIsInstance(
            response.context['post_form'], PostForm)
    
    def test_successful_post_submission(self):
        self.client.login(
            username="userName", password="passWord")
        post_data = {
            'content': 'This is a test post!'
        }
        response = self.client.post(reverse(
            'create_post'), post_data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            b'This is a test post!',
            response.content
        )