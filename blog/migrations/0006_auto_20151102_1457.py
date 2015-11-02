# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_article_video_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='video_id',
            field=models.CharField(null=True, blank=True, max_length=15),
        ),
    ]
