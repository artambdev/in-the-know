from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
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
    ever_edited = False

    def Meta(self):
        ordering = ["-created_on"]

    def get_excerpt(self):
        return f"{self.content[:50]}"
    
    def __str__(self):
        return f'"{self.content[:20]}..." | written by {self.author}'