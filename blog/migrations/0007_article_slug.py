# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    def save_slugs(apps, schema_editor):
        Article = apps.get_model("blog", "Article")

        print('saving articles')
        for article in Article.objects.all():
            article.save()

    dependencies = [
        ('blog', '0006_auto_20151102_1457'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='slug',
            field=models.SlugField(blank=True, editable=False),
        ),
        migrations.RunPython(save_slugs),
    ]
