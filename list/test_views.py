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

        self.hidden = Post(author=self.user,
                         slug="post-hidden", content="Hidden content",
                         hidden=True)
        self.hidden.save()
    
    def test_render_main_page(self):
        """
        Test that posts appear on the main page
        """
        response = self.client.get(reverse(
            'home'))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Post content", response.content)
    
    def test_no_hidden_on_main_page(self):
        """
        Test that hidden posts do not appear on the main page
        """
        response = self.client.get(reverse(
            'home'))
        self.assertEqual(response.status_code, 200)
        self.assertFalse(b"Hidden content" in response.content)

    def test_render_post_detail_page_with_reply_form(self):
        """
        Test that a post can be viewed directly
        """
        response = self.client.get(reverse(
            'view_post', args=['post-name']))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Post content", response.content)
        self.assertIsInstance(
            response.context['post_form'], PostForm)
    
    def test_successful_post_submission(self):
        """
        Test that a post can be successfully created
        """
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
    
    def test_successful_post_deletion(self):
        """
        Test that a post can be deleted
        And that the post no longer exists
        """
        self.client.login(
            username="userName", password="passWord")
        response = self.client.post(reverse(
            'delete_post', args=["post-name"]), follow=True)
        response2 = self.client.get(reverse(
            'view_post', args=['post-name']))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response2.status_code, 404)
