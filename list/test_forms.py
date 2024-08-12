from django.test import TestCase
from .forms import PostForm


class TestPostForm(TestCase):
    def test_form_is_valid(self):
        post_form = PostForm({'content': 'Hi everyone! 1 plus 1 equals 2!'})
        self.assertTrue(post_form.is_valid(), msg='Post form is not valid')
