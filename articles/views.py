from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
)
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy

from .models import Article, Comment


class ArticleListView(LoginRequiredMixin,ListView):
    model = Article 
    template_name = 'article_list.html'
    login_url = 'login'

class ArticleDetailView(LoginRequiredMixin,DetailView):
    model = Article
    template_name = 'article_detail.html'
    login_url = 'login'

class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Article
    fields = ('title', 'body')
    template_name = "article_edit.html"
    login_url = 'login'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Article 
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')
    login_url = 'login'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    template_name = "article_new.html"
    fields = ('title', 'body',)
    login_url = 'login'
    
    def form_valid(self,form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ArticleCommentView(CreateView):
    model = Comment
    fields = ('comment', )
    template_name = "article_comment.html"
    success_url = reverse_lazy('article_list')
    
    def form_valid(self,form):
        article = get_object_or_404(Article, pk=self.kwargs.get('pk'))
        form.instance.author = self.request.user
        form.instance.article =article
        return super().form_valid(form)
    

    