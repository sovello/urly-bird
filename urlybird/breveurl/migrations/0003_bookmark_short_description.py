# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('breveurl', '0002_auto_20150624_1954'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookmark',
            name='short_description',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
