from django.conf.urls import url, patterns

from .views import HomeView


urlpatterns = patterns('',
    url(r'^$', HomeView.as_view(), name="home"),
)
