from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps import GenericSitemap
from django.contrib.sitemaps.views import sitemap

from blog.models import Article


info_dict = {
    'queryset': Article.objects.all(),
    'date_field': 'created',
}

urlpatterns = [
    url(r'^sitemap\.xml$', sitemap,
        {'sitemaps': {'blog': GenericSitemap(info_dict, priority=0.8)}},
        name='django.contrib.sitemaps.views.sitemap'),

    url(r'^admin/', admin.site.urls),
    url(r'^blog/', include('blog.urls')),
    url(r'^', include('core.urls')),
]
