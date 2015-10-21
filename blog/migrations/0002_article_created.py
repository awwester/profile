# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='created',
            field=models.DateField(auto_now_add=True, default=datetime.datetime(2015, 10, 21, 19, 44, 17, 444566, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
