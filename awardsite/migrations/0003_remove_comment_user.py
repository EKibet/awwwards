# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-19 05:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('awardsite', '0002_remove_comment_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='user',
        ),
    ]
