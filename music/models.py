# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime

from django.db import models

# Create your models here.
class Songs(models.Model):
    title = models.CharField(max_length=50)
    album = models.CharField(max_length=50)
    artist = models.CharField(max_length=20)
    bio = models.TextField(max_length=255)
    release_time = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return "{} - {}".format(self.title, self.artist)



