# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-13 09:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('awardsite', '0004_postedsite_user_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postedsite',
            name='user_profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='userauth.Profile'),
        ),
    ]
