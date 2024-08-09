from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import generic
from .models import Post

# Create your views here.
class MainPage(generic.ListView):
    queryset = Post.objects.all()
    template_name = "list/main_page.html"
    paginate_by = 8


def view_post(request, slug):
    queryset = Post.objects.filter(hidden=False)
    post = get_object_or_404(queryset, slug=slug)
    replies = post.replies.all().order_by("created_on")
    num_replies = post.replies.filter(hidden=False).count()

    return render(
        request,
        "list/view_post.html",
        {
            "post": post,
            "replies": replies,
        },
    )