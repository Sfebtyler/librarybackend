# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-06 18:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Authors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=10000)),
            ],
        ),
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=10000)),
                ('description', models.CharField(max_length=10000)),
                ('checked_out', models.DateTimeField(auto_now_add=True, null=True)),
                ('author', models.ManyToManyField(to='app.Authors')),
            ],
        ),
    ]
