# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime
from django.db import models

#Create your models here.
class Reservation(models.Model):
    guest_name = models.CharField(max_length=200)
    entry_date = models.DateField(blank=True)
    leave_date = models.DateField(blank=True)
    group_size = models.IntegerField()
    def __str__(self):
        return self.guest_name
