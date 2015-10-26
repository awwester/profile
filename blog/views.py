from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView

from .models import Article


class BlogHomeView(ListView):
    template_name = "blog_home.html"
    queryset = Article.objects.filter(public=True)


class BlogArticleView(DetailView):
    template_name = "blog_article.html"
    model = Article
