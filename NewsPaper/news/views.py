from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView, DetailView
from .models import Post
from .filters import PostFilter


class PostsList(ListView):
    model = Post
    ordering = 'date_time'
    template_name = 'flatpages/news_feed.html'
    context_object_name = 'Posts'
    paginate_by = 2

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostFilter(self.request.GET, queryset)
        return self.filterset.qs



class PostDetail(DetailView):
    model = Post
    template_name = 'flatpages/Post.html'
    context_object_name = 'Post'
