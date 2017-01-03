from django.conf.urls import url, patterns

from .views import HomeView, DashboardHomeListView, SendContactView, email_subscribe


urlpatterns = patterns('',
    url(r'^$', HomeView.as_view(), name="home"),
    url(r'^contact/$', SendContactView.as_view(), name="contact"),
    url(r'^subscribe/$', email_subscribe, name="email-subscribe"),
    url(r'^dashboard/$', DashboardHomeListView.as_view(), name="dashboard-home")
)
