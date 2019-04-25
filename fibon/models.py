from __future__ import unicode_literals

from django.db import models

# Create your models here.
class ResultFibonacci(models.Model):
    number = models.IntegerField(unique=True)
    result = models.IntegerField()
    time_elapsed = models.CharField(max_length=255)

