from django.shortcuts import render, HttpResponse, redirect
import random
from posts.models import Post
from posts.forms import PostForm, PostModelForm, SearchForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q

def home(request):
     if request.method == "GET":
          return render(request, "base.html")
     else:
          return HttpResponse("HELLO YOU'RE AT THE POLIS INDEX")


@login_required(login_url="/login")
def post_list_view(request):
     limit = 3
     if request.method == "GET":
          form = SearchForm()
          posts = Post.objects.all()
          search = request.GET.get("search")
          category_id = request.GET.get("category_id")
          ordering = request.GET.get("ordering")
          page = request.GET.get("page", 1)
          if search:
               posts = posts.filter(Q(title__icontains=search) | Q(content__icontains=search))
          if category_id:
               posts = posts.filter(category_id=int(category_id))
          if ordering:
               posts = posts.order_by(ordering)
          max_pages = posts.count() / limit
          if round(max_pages) < max_pages:
               max_pages = round(max_pages + 1)
          else:
               max_pages = round(max_pages)
          start = (int(page) - 1) * limit
          end = int(page) * limit
          posts = posts[start:end]
          return render(request, "posts/post_list.html", context={'posts': posts, "form": form, "max_pages": range(1, max_pages + 1)})


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
