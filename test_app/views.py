from django.http import HttpResponse
from django.shortcuts import render
from .models import *


# Create your views here.
def get_posts(request):
    posts = Post.objects.all()
    data = {
        'articles': posts,
    }
    return render(request, 'index.html', context=data)


def get_post(request, id):
    post = Post.objects.get(id=id)   # по ID находим пост
    comments = Comment.objects.filter(post_id=id).order_by('author', '-updated')\
        .exclude(author='kanat') # Фильтруем по пост ID и сортируем по автору и дате
    data = {
        'article': post,
        'comments': comments
    }
    return render(request, 'detail.html', context=data)


def main_page(request):
    return render(request, 'main.html')