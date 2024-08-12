from django.contrib.auth.models import User
from django.urls import reverse
from django.test import TestCase
from .forms import PostForm
from .models import Post

class TestBlogViews(TestCase):

    def setUp(self):
        self.user = User.objects.create_superuser(
            username="userName",
            password="passWord",
            email="sample@email.com"
        )
        self.post = Post(author=self.user,
                         slug="post-name", content="Post content",
                         hidden=False)
        self.post.save()