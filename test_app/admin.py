from django.contrib import admin

# Register your models here.
from test_app.models import Post, Comment, Category


class CommentInline(admin.StackedInline):
    model = Comment
    extra = 0


class PostAdmin(admin.ModelAdmin):
    list_display = 'id title text created updated'.split()
    search_fields = ['title', 'text']
    list_filter = 'created'.split()
    list_editable = 'title'.split()
    readonly_fields = 'created updated'.split()
    inlines = [CommentInline]


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
# admin.site.register(Comment)
