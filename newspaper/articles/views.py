from django.shortcuts import render
from .models import Article
from django.views.generic import ListView, DetailView
from django.views.generic.edit import DeleteView, UpdateView
from django.urls import reverse_lazy
# Create your views here.

class ArticleListView(ListView):
    model = Article
    template_name = "articles/list.html"

class  DetailListView(DetailView):
    model = Article
    template_name = "articles/detail.html"

class UpdateListView(UpdateView):
    model = Article
    fields = ('title', 'body')
    template_name = "articles/edit.html"

class DeleteListView(DeleteView):
    model = Article
    template_name = "articles/delete.html"
    success_url = reverse_lazy("list")

