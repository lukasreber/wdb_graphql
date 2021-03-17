from django.db import models

# Create your models here.
class AdUser(models.Model):
    name = models.TextField(blank=True)

class Ad(models.Model):
    title = models.TextField(blank=True)
    description = models.TextField(blank=True)
    url = models.URLField(blank=True)
    user = models.ForeignKey(AdUser, null=True, on_delete=models.CASCADE, blank=True)