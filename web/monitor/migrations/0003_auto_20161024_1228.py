# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-24 12:28
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0002_auto_20161017_1553'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usergroup',
            options={'verbose_name_plural': '用户组信息表'},
        ),
        migrations.AlterModelOptions(
            name='userinfo',
            options={'verbose_name_plural': '用户信息表'},
        ),
        migrations.AlterModelOptions(
            name='usertype',
            options={'verbose_name_plural': '用户类型表'},
        ),
    ]
