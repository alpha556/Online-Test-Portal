# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-27 13:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exam_name', models.CharField(max_length=50)),
                ('duration', models.DurationField()),
                ('date_published', models.DateField(verbose_name='date published')),
            ],
        ),
    ]
