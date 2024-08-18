from django import forms
from .models import Feedback


class FeedbackForm(forms.ModelForm):
    """
    Form for sending feedback to the site admins
    """
    class Meta:
        model = Feedback
        fields = ('name', 'email', 'message')
