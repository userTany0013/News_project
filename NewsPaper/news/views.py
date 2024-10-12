from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView, DetailView
from .models import Post


class PostsList(ListView):
    model = Post
    ordering = 'date_time'
    template_name = 'flatpages/news_feed.html'
    context_object_name = 'Posts'


class PostDetail(DetailView):
    model = Post
    template_name = 'flatpages/Post.html'
    context_object_name = 'Post'
