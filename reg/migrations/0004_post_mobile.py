# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2019-11-13 12:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reg', '0003_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='mobile',
            field=models.PositiveIntegerField(),
            preserve_default=False,
        ),
    ]
