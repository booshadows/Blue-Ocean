from django.shortcuts import render
from django.utils import timezone
from .models import Post
from .models import Book


def hello(request):
   return render(request, "index.html", {})

def article(request):
   return render(request, "article.html", {})

def index(request):
    posts = Post.objects.all()
    return render(request, 'article.html', {'posts':posts})
