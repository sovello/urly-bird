# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('breveurl', '0002_auto_20150618_2129'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookmark',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2015, 6, 18, 21, 40, 8, 650909, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bookmark',
            name='last_updated',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2015, 6, 18, 21, 40, 13, 629970, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
