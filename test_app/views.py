from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *


# Create your views here.
def get_posts(request):
    posts = Post.objects.all()
    data = {
        'articles': posts,
    }
    return render(request, 'index.html', context=data)


def get_post(request, id):
    post = Post.objects.get(id=id)  # по ID находим пост
    comments = Comment.objects.filter(post_id=id).order_by('author', '-updated') \
        .exclude(author='kanat')  # Фильтруем по пост ID и сортируем по автору и дате
    data = {
        'article': post,
        'comments': comments
    }
    return render(request, 'detail.html', context=data)


def main_page(request):
    return render(request, 'main.html')


def add(request):
    if request.method == "POST":
        title = request.POST.get("title")
        text = request.POST.get("text")
        print(title,text)
        Post.objects.create(title=title,text=text, category_id=1)
        return redirect('/posts/')
    return render(request, 'add.html')


def add_category(request):
    if request.method == "CATEGORY":
        text = request.CATEGORY.get("title")
        print(text)
        Category.objects.create(text=text)
        return redirect('/category/')
    return render(request, 'add_category.html')