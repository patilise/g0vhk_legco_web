from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Subscriber(models.Model):
    email = models.EmailField(max_length=1024)
    key = models.CharField(unique=True, max_length=128)
    def __unicode__(self):
        return self.email
