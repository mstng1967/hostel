# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-17 19:57
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guest', models.CharField(max_length=200)),
                ('entry_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('leave_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('group_size', models.IntegerField()),
            ],
        ),
    ]