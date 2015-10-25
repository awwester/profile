from django.conf.urls import url, patterns

from .views import HomeView, contact


urlpatterns = patterns('',
    url(r'^$', HomeView.as_view(), name="home"),
    url(r'^contact/$', contact, name="contact"),
)
