from django.test import TestCase
from .forms import FeedbackForm


class TestFeedbackForm(TestCase):
    def test_form_name_invalid(self):
        """
        Test that form is invalid if name is not filled in
        """
        feedback_form = FeedbackForm({'name': '',
            'email': 'sample@email.com',
            'message': 'Feedback content'})
        self.assertFalse(feedback_form.is_valid(), msg='Post form is valid despite missing name')
    
    def test_form_email_missing(self):
        """
        Test that form is invalid if email is not filled in
        """
        feedback_form = FeedbackForm({'name': 'Name',
            'email': '',
            'message': 'Feedback content'})
        self.assertFalse(feedback_form.is_valid(), msg='Post form is valid despite missing email')
    
    def test_form_email_invalid(self):
        """
        Test that form is invalid if email is not a valid email
        """
        feedback_form = FeedbackForm({'name': 'Name',
            'email': 'sampleatemail.com',
            'message': 'Feedback content'})
        self.assertFalse(feedback_form.is_valid(), msg='Post form is valid despite invalid email format')

    def test_form_message_invalid(self):
        """
        Test that form is invalid if message is not filled in
        """
        feedback_form = FeedbackForm({'name': 'Name',
            'email': 'sample@email.com',
            'message': ''})
        self.assertFalse(feedback_form.is_valid(), msg='Post form is valid despite missing message')
    
    def test_form_is_incorrectly_invalid(self):
        """
        Test that form is valid if properly filled in
        """
        feedback_form = FeedbackForm({'name': 'Name',
            'email': 'sample@email.com',
            'message': 'Feedback content'})
        self.assertTrue(feedback_form.is_valid(), msg='Post form is invalid and should not be')