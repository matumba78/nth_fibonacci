# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-04-25 07:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ResultFibonacci',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(unique=True)),
                ('result', models.IntegerField()),
                ('time_elapsed', models.TimeField()),
            ],
        ),
    ]