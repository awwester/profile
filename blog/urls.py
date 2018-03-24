from django.conf.urls import url

from .views import BlogHomeView, BlogArticleView, BlogSeriesView


urlpatterns = [
    url(r'^$', BlogHomeView.as_view(), name="blog-home"),
    url(r'^series/$', BlogSeriesView.as_view(), name="blog-series"),
    url(r'^(?P<slug>\S+)/$', BlogArticleView.as_view(), name="blog-article"),
]
