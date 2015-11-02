from django.conf.urls import url, patterns

from .views import BlogHomeView, BlogArticleView


urlpatterns = patterns('',
    url(r'^$', BlogHomeView.as_view(), name="blog-home"),
    url(r'^(?P<slug>\S+)/$', BlogArticleView.as_view(), name="blog-article"),
)
