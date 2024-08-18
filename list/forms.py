from .models import Post
from django import forms


class PostForm(forms.ModelForm):
    """
    Form for creating new posts
    """
    class Meta:
        model = Post
        fields = ('content',)
