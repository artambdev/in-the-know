from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    #slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="posts"
    )
    reply_to = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="replies"
    )
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    hidden = models.BooleanField()
    ever_edited = False

    def __str__(self):
        return f"{self.content[:50]}"