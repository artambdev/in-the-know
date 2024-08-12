import random
import string
from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views import generic
from .models import Post
from .forms import PostForm

# Create your views here.
class MainPage(generic.ListView):
    template_name = "list/main_page.html"
    paginate_by = 8

    def get_queryset(self):
        if self.request.user.is_superuser:
            queryset = Post.objects.all()
        else:
            queryset = Post.objects.filter(hidden=False)

        return queryset


def view_post(request, slug):
    if request.user.is_authenticated and not request.user.is_superuser:
        queryset = Post.objects.all()
    else:
        queryset = Post.objects.filter(hidden=False)
    post = get_object_or_404(queryset, slug=slug)
    replies = post.replies.all().order_by("created_on")
    num_replies = post.replies.filter(hidden=False).count()

    post_form = PostForm()

    return render(
        request,
        "list/view_post.html",
        {
            "post": post,
            "replies": replies,
            "replies_count": num_replies,
        },
    )


def create_post(request):
    if request.method == "POST":
        post_form = PostForm(data=request.POST)
        if post_form.is_valid():
            new_post = post_form.save(commit=False)
            slug_format = string.ascii_lowercase + string.digits + '-_'
            new_post.slug = ''.join(random.choices(slug_format, k=15))
            new_post.author = request.user
            new_post.hidden = False
            new_post.save()

    post_form = PostForm()

    return render(
        request,
        "list/create_post.html",
        {
            "post_form": post_form,
        },
    )


def edit_post(request, slug):
    if request.method == "POST":
        queryset = Post.objects.filter(hidden=False)
        post = get_object_or_404(queryset, slug=slug)
        post_form = PostForm(data=request.POST, instance=post)

        if post_form.is_valid() and post.author == request.user:
            post = post_form.save(commit=False)
            post.save()
    
    queryset = Post.objects.all()
    post = get_object_or_404(queryset, slug=slug)
    post_form = PostForm(initial={"content": post.content})

    return render(
        request,
        "list/edit_post.html",
        {
            "post_form": post_form,
        },
    )


def delete_post(request, slug):
    queryset = Post.objects.all()
    post = get_object_or_404(queryset, slug=slug)

    if post.author == request.user:
        post.delete()

    return HttpResponseRedirect(reverse('home'))


def hide_post(request, slug):
    queryset = Post.objects.all()
    post = get_object_or_404(queryset, slug=slug)

    if request.user.is_superuser:
        post.hidden = not post.hidden
        post.save()

    return HttpResponseRedirect(reverse('view_post', args=[slug]))