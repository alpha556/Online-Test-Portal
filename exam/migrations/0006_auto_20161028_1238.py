# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-28 07:08
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0005_auto_20161028_1230'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='answer',
            field=models.PositiveIntegerField(default=1, validators=[django.core.validators.MaxValueValidator(4), django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='question',
            name='option1',
            field=models.CharField(default='none', max_length=100, verbose_name='option1'),
        ),
    ]
