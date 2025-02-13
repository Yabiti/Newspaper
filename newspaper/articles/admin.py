from django.contrib import admin
from .models import Article, Comment
# Register your models here.

admin.site.register(Comment)

class CommentInLine(admin.StackedInline):
    model = Comment

class ArticleAdmin(admin.ModelAdmin):
    inlines = [
        CommentInLine
    ]

admin.site.register(Article, ArticleAdmin)