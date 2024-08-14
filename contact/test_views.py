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
        self.feedback = Feedback(name="Name",
                         email="sample@email.com", message="Feedback content")
        self.feedback.save()