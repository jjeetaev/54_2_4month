from django.shortcuts import render, HttpResponse
import random
from posts.models import Post

def home(request):
     return render(request, "base.html")

def post_list_view(request):
     posts = Post.objects.all()
     return render(request, "posts/post_list.html", context={'posts': posts})

def post_detail_view(request, post_id):
     post = Post.objects.filter(id=post_id).first()
     return render(request, "posts/post_detail.html", context={"post": post})


