# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-17 20:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reservation',
            old_name='guest',
            new_name='guest_name',
        ),
        migrations.AlterField(
            model_name='reservation',
            name='entry_date',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='leave_date',
            field=models.DateField(blank=True),
        ),
    ]
