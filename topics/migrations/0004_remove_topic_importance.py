# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-02 22:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('topics', '0003_topic_importance'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topic',
            name='importance',
        ),
    ]
