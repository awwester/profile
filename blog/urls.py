from django.conf.urls import url, patterns

from .views import BlogHomeView, BlogArticleView, BlogSeriesView


urlpatterns = patterns('',
    url(r'^$', BlogHomeView.as_view(), name="blog-home"),
    url(r'^series/$', BlogSeriesView.as_view(), name="blog-series"),
    url(r'^(?P<slug>\S+)/$', BlogArticleView.as_view(), name="blog-article"),
)
