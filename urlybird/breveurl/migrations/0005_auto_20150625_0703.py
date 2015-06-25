# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('breveurl', '0004_auto_20150625_0603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmark',
            name='description',
            field=models.CharField(blank=True, max_length=700, null=True),
        ),
        migrations.AlterField(
            model_name='bookmark',
            name='short_description',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='bookmark',
            name='tags',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
