from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from .models import Article, Comment


class AuthorCreate(CreateView):
    template_name = "article_form.html"
    model = Article
    fields = '__all__'


class ClassBasedView(ListView):
    template_name = "index.html"
    context_object_name = 'article_list'
    model = Article


class AuthorCommentUpdate(UpdateView):
    template_name = "comment_form.html"
    model = Comment
    fields = '__all__'
