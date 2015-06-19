# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bookmark',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('url', models.URLField()),
                ('description', models.CharField(blank=True, null=True, max_length=255)),
                ('breveurl', models.CharField(blank=True, null=True, max_length=255)),
                ('tags', models.CharField(blank=True, null=True, max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Bookmarks',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('tags', models.CharField(blank=True, null=True, max_length=255)),
            ],
        ),
    ]
