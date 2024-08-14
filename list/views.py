import random
import string
from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.views import generic
from .models import Post
from .forms import PostForm


class MainPage(generic.ListView):
    """
    View function to render the main page
    with the list of posts, visible depending
    on superuser status
    """
    template_name = "list/main_page.html"
    paginate_by = 8

    def get_queryset(self):
        if self.request.user.is_superuser:
            queryset = Post.objects.all().order_by("-created_on")
        else:
            queryset = Post.objects.filter(hidden=False).order_by("-created_on")

        return queryset


def view_post(request, slug):
    """
    View function to render post's detailed view
    and handle the posting of replies to the post
    """
    if request.user.is_authenticated and request.user.is_superuser:
        queryset = Post.objects.all()
    else:
        queryset = Post.objects.filter(hidden=False)
    post = get_object_or_404(queryset, slug=slug)
    replies = post.replies.all().order_by("created_on")
    num_replies = post.replies.filter(hidden=False).count()

    if request.method == "POST":
        post_form = PostForm(data=request.POST)
        if post_form.is_valid():
            new_post = post_form.save(commit=False)
            slug_format = string.ascii_lowercase + string.digits + '-_'
            new_post.slug = ''.join(random.choices(slug_format, k=15))
            new_post.reply_to = post
            new_post.author = request.user
            new_post.hidden = False
            new_post.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Reply created successfully'
            )
            return HttpResponseRedirect(reverse('view_post', args=[new_post.slug]))
        else:
            messages.add_message(request, messages.ERROR, 'There was an error creating your reply')
            

    post_form = PostForm()

    return render(
        request,
        "list/view_post.html",
        {
            "post": post,
            "replies": replies,
            "replies_count": num_replies,
            "post_form": post_form,
        },
    )


def create_post(request):
    """
    View to render the post creation page
    And handle post requests for new posts
    """
    if request.method == "POST":
        post_form = PostForm(data=request.POST)
        if post_form.is_valid():
            new_post = post_form.save(commit=False)
            slug_format = string.ascii_lowercase + string.digits + '-_'
            new_post.slug = ''.join(random.choices(slug_format, k=15))
            new_post.author = request.user
            new_post.hidden = False
            new_post.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Post successfully created'
            )
            return HttpResponseRedirect(reverse('view_post', args=[new_post.slug]))
        else:
            messages.add_message(request, messages.ERROR, 'There was an error creating your post')

    post_form = PostForm()

    return render(
        request,
        "list/create_post.html",
        {
            "post_form": post_form,
        },
    )


def edit_post(request, slug):
    """
    View function to render the edit-post page
    and handle requests to edit a post
    """
    if request.method == "POST":
        queryset = Post.objects.filter(hidden=False)
        post = get_object_or_404(queryset, slug=slug)
        post_form = PostForm(data=request.POST, instance=post)

        if post_form.is_valid() and post.author == request.user:
            post = post_form.save(commit=False)
            post.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Post successfully edited'
            )
            return HttpResponseRedirect(reverse('view_post', args=[post.slug]))
        else:
            messages.add_message(request, messages.ERROR, 'There was an error editing your post')
    
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
    """
    View function to handle requests to delete posts
    """
    queryset = Post.objects.all()
    post = get_object_or_404(queryset, slug=slug)

    if post.author == request.user or request.user.is_superuser:
        post.delete()
        messages.add_message(
            request, messages.SUCCESS,
            'Post successfully deleted'
        )
    else:
        messages.add_message(request, messages.ERROR, 'There was an error deleting this post')

    return HttpResponseRedirect(reverse('home'))


def hide_post(request, slug):
    """
    View function to handle requests to hide posts
    """
    queryset = Post.objects.all()
    post = get_object_or_404(queryset, slug=slug)

    if request.user.is_superuser:
        post.hidden = not post.hidden
        post.save()
        message_string = "Post successfully hidden"
        if not post.hidden:
            message_string = "Post successfully unhidden"
        messages.add_message(
            request, messages.SUCCESS,
            message_string
        )
    else:
        messages.add_message(request, messages.ERROR, 'There was an error in hiding or unhiding this post')

    return HttpResponseRedirect(reverse('view_post', args=[slug]))