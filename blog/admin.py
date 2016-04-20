from django.contrib import admin

from .models import Article, Tag, Series

class ArticleAdmin(admin.ModelAdmin):
    readonly_fields=('view_count',)

# Register your models here.
admin.site.register(Article, ArticleAdmin)
admin.site.register(Tag)
admin.site.register(Series)
