# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-29 05:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('X_Home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Email', models.EmailField(max_length=254)),
                ('Name', models.CharField(max_length=20)),
                ('Message', models.CharField(max_length=100)),
            ],
        ),
    ]
