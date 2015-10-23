from django.shortcuts import render
from django.views.generic import TemplateView

from blog.models import Article, Tag


class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['tag_list'] = Tag.objects.all()
        context['article_count'] = Article.objects.count()
        context['article_list'] = Article.objects.all()[:2]

        return context
