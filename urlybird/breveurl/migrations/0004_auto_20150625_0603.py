# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('breveurl', '0003_bookmark_short_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmark',
            name='description',
            field=models.CharField(max_length=500, blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='bookmark',
            name='short_description',
            field=models.CharField(max_length=300, blank=True, null=True),
        ),
    ]
