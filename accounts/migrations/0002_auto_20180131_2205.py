# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-01-31 20:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(blank=True, upload_to='profile_image'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='phone',
            field=models.IntegerField(default=0),
        ),
    ]
