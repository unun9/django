from django.db import models


# Create your models here.
class Category(models.Model):
    class Meta:
        verbose_name = "Категории"

    text = models.TextField(verbose_name="Техт")

    def __str__(self):
        return self.text


class Post(models.Model):
    class Meta:
        verbose_name = 'пост'
        verbose_name_plural = 'посты'

    title = models.CharField(max_length=100, verbose_name='Заголовок')
    text = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Comment(models.Model):
    text = models.TextField()
    author = models.CharField(max_length=100)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text
