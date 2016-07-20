# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-26 16:44
from __future__ import unicode_literals

import cus_auth.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cus_auth', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bloguser',
            fields=[
            ],
            options={
                'abstract': False,
                'verbose_name': 'bloguser',
                'verbose_name_plural': 'blogusers',
                'proxy': True,
            },
            bases=('cus_auth.user',),
            managers=[
                ('objects', cus_auth.models.UserManager()),
            ],
        ),
        migrations.AddField(
            model_name='followrelation',
            name='follow',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='follower_records', to=settings.AUTH_USER_MODEL, verbose_name='follow'),
        ),
        migrations.AddField(
            model_name='followrelation',
            name='follower',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='follow_records', to=settings.AUTH_USER_MODEL, verbose_name='follower'),
        ),
        migrations.AddField(
            model_name='basicprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='basic_profile', to=settings.AUTH_USER_MODEL),
        ),
    ]
