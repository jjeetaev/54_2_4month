from django.shortcuts import render, HttpResponse, redirect
import random
from posts.models import Post
from posts.forms import PostForm, PostModelForm
from django.contrib.auth.decorators import login_required

def home(request):
     if request.method == "GET":
          return render(request, "base.html")
     else:
          return HttpResponse("HELLO YOU'RE AT THE POLIS INDEX")


@login_required(login_url="/login")
def post_list_view(request):
     if request.method == "GET":
          posts = Post.objects.all()
          return render(request, "posts/post_list.html", context={'posts': posts})

@login_required(login_url="/login")
def post_detail_view(request, post_id):
     if request.method == "GET":
          post = Post.objects.filter(id=post_id).first()
          return render(request, "posts/post_detail.html", context={"post": post})

@login_required(login_url="/login")
def post_create_view(request):
     if request.method == "GET":
          form = PostModelForm()
          return render(request, "posts/post_create.html", context={"form": form})
     if request.method == "POST":
          form = PostModelForm(request.POST, request.FILES)
          if not form.is_valid():
               return render(request, "posts/post_create.html", context={"form": form})
          title = form.cleaned_data.get("title")
          content = form.cleaned_data.get("content")
          image = form.cleaned_data.get("image")
          post = Post.objects.create(title=title, content=content, image=image)
          return redirect(f"/posts/{post.id}")
