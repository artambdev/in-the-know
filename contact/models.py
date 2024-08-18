from django.db import models
from django.contrib.auth.models import User


class Feedback(models.Model):
    """
    Class for feedback sent to admins
    """
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    resolved = models.BooleanField(default=False)
    sent_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['sent_on']

    def __str__(self):
        return f"Feedback submitted by {self.name}"
