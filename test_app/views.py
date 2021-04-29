from django.contrib import auth
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import RegisterForms, loginForm
from .models import *

PAGE_SIZE=3
PAGE=3
# Create your views here.
def get_posts(request):
    search_word=request.GET.get('search','')

    posts = Post.objects.filter(Q(title__contains=search_word)|
                                Q(text__contains=search_word))
    total= posts.count()
    pages=total//PAGE_SIZE

    if (total%PAGE_SIZE)>0:
        pages+=1
        print(pages)
    PAGE=int(request.GET.get('page',1))
    data = {
        'pages':[page for page in range(1,pages+1)],
        'articles': posts[(PAGE-1)*PAGE_SIZE:PAGE*PAGE_SIZE],
        'username': auth.get_user(request).username
    }
    return render(request, 'index.html', context=data)


def get_post(request, id):
    post = Post.objects.get(id=id)  # по ID находим пост
    comments = Comment.objects.filter(post_id=id).order_by('author', '-updated') \
        .exclude(author='kanat')  # Фильтруем по пост ID и сортируем по автору и дате
    data = {
        'article': post,
        'comments': comments,
        'username': auth.get_user(request).username

    }
    return render(request, 'detail.html', context=data)


def main_page(request):
    data={
        'username':auth.get_user(request).username
    }
    return render(request, 'main.html',context=data)


def add(request):
    if request.method == "POST":
        title = request.POST.get("title")
        text = request.POST.get("text")
        print(title, text)
        Post.objects.create(title=title, text=text, category_id=1)
        return redirect('/posts/')
    data = {
        'username': auth.get_user(request).username
    }

    return render(request, 'add.html',context=data)


def add_category(request):
    if request.method == "POST":
        text = request.POST.get("text")
        Category.objects.create(text=text)
        return redirect('/category/')
    data = {
        'username': auth.get_user(request).username
    }
    return render(request, 'add_category.html',context=data)


def register(request):
    if request.method=='POST':
        form=RegisterForms(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return render(request,'register.html',context={
                'form':form
            })
    data ={
        'form': RegisterForms()
    }

    return render(request,"register.html",context=data)


def login(request):
    if request.method == 'POST':
        form = loginForm(data=request.POST)
        if form.is_valid():
            # form.save()
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            user= auth.authenticate(username=username,pasword=password)
            if user:
                auth.login(request,user)
            return redirect("/")
        else:
            return render(request, 'login.html', context={
                'form': form
            })
    data = {
        'form': loginForm()
    }

    return render(request, "login.html", context=data)


def logout(request):
    auth.logout(request)
    return redirect('/')