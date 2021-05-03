from django.shortcuts import render
from django.contrib.auth.models import User
from django.views import generic
from .models import Post

# Create your views here.
class PostList(generic.ListView):
    model = Post
    template_name = 'post_list.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post.html'