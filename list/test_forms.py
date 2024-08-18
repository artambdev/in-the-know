from django.test import TestCase
from .forms import PostForm


class TestPostForm(TestCase):
    def test_form_is_valid(self):
        """
        Test that form is valid if content is properly filled out
        """
        post_form = PostForm({'content': 'Hi everyone! 1 plus 1 equals 2!'})
        self.assertTrue(post_form.is_valid(), msg='Post form is not valid')

    def test_form_is_invalid(self):
        """
        Test that form is invalid if has no content
        """
        post_form = PostForm({'content': ''})
        self.assertFalse(
            post_form.is_valid(),
            msg='Post form is valid and should not be'
        )
