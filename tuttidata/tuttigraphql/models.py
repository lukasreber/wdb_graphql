from django.db import models

# Create your models here.
class Ad(models.Model):
    title = models.TextField(blank=True)
    description = models.TextField(blank=True)
    url = models.URLField()