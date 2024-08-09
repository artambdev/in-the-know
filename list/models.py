from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Post(models.Model):
    #title = models.CharField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="posts"
    )
    reply_to = models.ForeignKey(
        "self", on_delete=models.CASCADE, related_name="replies"
    )
    content = models.TextField(max_length=200)
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    hidden = models.BooleanField()
    ever_edited = False

    slug = f"{author}-{created_on}-{content[:10]}"

    def Meta(self):
        ordering = ["-created_on"]

    def get_excerpt(self):
        return f"{self.content[:50]}"