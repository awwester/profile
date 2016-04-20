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

    def get(self, request, *args, **kwargs):
        # record the article view
        self.get_object().record_view()
        return super(BlogArticleView ,self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(BlogArticleView, self).get_context_data(**kwargs)
        context['related_article'] = self.get_object().get_related_article()

        return context
