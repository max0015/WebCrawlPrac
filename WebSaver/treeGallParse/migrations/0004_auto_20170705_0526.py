# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-05 05:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('treeGallParse', '0003_auto_20170705_0504'),
    ]

    operations = [
        migrations.AddField(
            model_name='postdata',
            name='PostNum',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='postdata',
            name='link',
            field=models.URLField(),
        ),
    ]
