# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-26 08:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20160825_1835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=22),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=22),
        ),
    ]
