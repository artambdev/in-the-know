from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import Post

# Create your views here.
class MainPage(generic.ListView):
    queryset = Post.objects.all()
    template_name = "list/main_page.html"