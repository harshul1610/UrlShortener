from __future__ import unicode_literals

from django.db import models

# Create your models here.
class UrlInputClass(models.Model):
    InputUrl = models.URLField(unique=True)
    ShortenedKey = models.CharField(max_length=100)

    def __repr__(self):
        return 'http://127.0.0.1:8000/'+ self.ShortenedKey