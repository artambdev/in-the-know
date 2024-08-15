from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    """
    Class to define the post model
    """
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="posts"
    )
    slug = models.SlugField(max_length=200, default=None, null=True)
    reply_to = models.ForeignKey(
        "self", on_delete=models.CASCADE, related_name="replies", null=True, blank=True
    )
    content = models.TextField(max_length=200)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    hidden = models.BooleanField()

    def Meta(self):
        """
        Show the newest posts first in admin screen
        """
        ordering = ["-created_on"]
    
    def get_num_replies(self):
        """
        Returns the number of non-hidden replies on a post
        """
        return self.replies.filter(hidden=False).count()
    
    def get_replies_string(self):
        """
        Returns a string describing the number of replies
        the post has
        """
        num_replies = self.replies.filter(hidden=False).count()
        reply_or_replies = "replies"
        if num_replies == 1:
            reply_or_replies = "reply"
        return f'{num_replies} {reply_or_replies}'
    
    def __str__(self):
        return f'"{self.content[:20]}..." | written by {self.author}'