from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
from .forms import FeedbackForm
from .models import Feedback


class TestContactViews(TestCase):

    def setUp(self):
        self.user = User.objects.create_superuser(
            username="userName",
            password="passWord",
            email="sample@email.com"
        )
        self.feedback = Feedback(
            name="Name",
            email="sample@email.com",
            message="Feedback content"
        )
        self.feedback.save()

    def test_successful_feedback_submission(self):
        """
        Test that feedback can be successfully sent
        """
        feedback_data = {
            'name': 'Name',
            'email': 'sample@email.com',
            'message': 'Feedback content'
        }
        response = self.client.post(reverse(
            'contact_page'), feedback_data)
        self.assertEqual(response.status_code, 200)
