# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-08 14:09
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_auto_20171006_2257'),
    ]

    operations = [
        migrations.AlterField(
            model_name='complain',
            name='complaint_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='complain',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
