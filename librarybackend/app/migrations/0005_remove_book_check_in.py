# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-10-07 19:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_book_check_in'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='check_in',
        ),
    ]
