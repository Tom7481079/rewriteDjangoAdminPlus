# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2018-01-10 03:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0004_auto_20180110_0925'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userprofile',
            options={'permissions': (('can_access_userprofile_list', '可以访问用户表'), ('can_add_userprofile_get', '可以访问添加用户表界面'), ('can_add_userprofile_post', '可以添加用户表记录'), ('can_change_userprofile_get', '可以访问修改用户表记录'), ('can_change_userprofile_post', '可以正真修改用户表记录'), ('can_delete_userprofile_get', '可以访问删除用户表记录'), ('can_delete_userprofile_post', '可以正真删除用户表记录')), 'verbose_name_plural': '用户表'},
        ),
    ]