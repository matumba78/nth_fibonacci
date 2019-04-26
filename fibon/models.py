from __future__ import unicode_literals

from django.db import models

# Create your models here.
class ResultFibonacci(models.Model):
    '''result is stored in char field to facilitates storage of large number as sqlite
    integer cannot store large integers which results in overflow'''
    number = models.IntegerField(unique=True)
    result = models.CharField(max_length=255)
    time_elapsed = models.CharField(max_length=255)

