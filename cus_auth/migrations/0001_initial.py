# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-26 16:44
from __future__ import unicode_literals

import cus_auth.models
from django.conf import settings
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0007_alter_validators_add_error_messages'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True, verbose_name='email')),
                ('mobile_phone', models.CharField(blank=True, max_length=15, null=True, unique=True, verbose_name='mobile phone')),
                ('nickname', models.CharField(max_length=60, unique=True, verbose_name='nickname')),
                ('is_admin', models.BooleanField(default=False, verbose_name='admin status')),
                ('is_active', models.BooleanField(default=True, verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('following', models.ManyToManyField(related_name='followers', through='accounts.FollowRelation', to=settings.AUTH_USER_MODEL, verbose_name='following')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'permissions': (('add_admin', 'can add a user of is_admin=True '), ('change_admin', 'can change a user of is_admin=True'), ('delete_admin', 'can delete a user of is_admin=True')),
                'verbose_name_plural': 'users',
            },
            managers=[
                ('objects', cus_auth.models.UserManager()),
            ],
        ),
    ]
