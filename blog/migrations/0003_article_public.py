# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_article_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='public',
            field=models.BooleanField(default=True),
        ),
    ]
