from django.shortcuts import render
from .models import Article
from django.views.generic import ListView, DetailView
from django.views.generic.edit import DeleteView, UpdateView
# Create your views here.

class ArticleListView(ListView):
    model = Article
    template_name = "article_list.html"

class  DetailListView(DetailView):
    model = Article
    template_name = "article_detail.html"

class UpdateListView(UpdateView):
    model = Article
    template_name = "article_edit.html"
class DeleteListView(DeleteView):
    model = Article
    fields = ('title', 'body')
    template_name = "article_delete.html"

