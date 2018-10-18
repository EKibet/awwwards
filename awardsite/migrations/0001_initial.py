# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-12 14:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PostedSite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_name', models.CharField(max_length=70)),
                ('site_url', models.URLField(max_length=250)),
                ('description', models.CharField(max_length=70)),
                ('categories', models.CharField(max_length=70)),
                ('tags', models.CharField(max_length=70)),
                ('designer', models.CharField(max_length=70)),
                ('time_created', models.CharField(max_length=70)),
            ],
        ),
    ]