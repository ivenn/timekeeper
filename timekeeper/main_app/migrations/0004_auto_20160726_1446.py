# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-26 14:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_auto_20160725_1350'),
    ]

    operations = [
        migrations.RenameField(
            model_name='settings',
            old_name='owner',
            new_name='user',
        ),
    ]