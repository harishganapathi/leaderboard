# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-19 08:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Scorecard',
            fields=[
                ('serialNo', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=40)),
                ('score', models.IntegerField()),
            ],
        ),
    ]
