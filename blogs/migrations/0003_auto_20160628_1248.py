# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-28 04:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_auto_20160627_0044'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='forwardrecord',
            options={'ordering': ['-date_forwarded']},
        ),
    ]
