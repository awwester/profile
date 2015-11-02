# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20151028_0439'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='video_id',
            field=models.CharField(max_length=10, blank=True, null=True),
        ),
    ]
