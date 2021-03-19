from django.db import models

# Create your models here.
class AdUser(models.Model):
    name = models.TextField(blank=True)

class Ad(models.Model):
    nr = models.IntegerField(blank=True)
    title = models.CharField(blank=True, max_length=300)
    price = models.IntegerField(blank=True)
    zipcode = models.IntegerField(blank=True)
    description = models.TextField(blank=True,max_length=5000)
    category = models.CharField(blank=True,max_length=300)
    url = models.URLField(blank=True)
    dateadded = models.CharField(blank=True,max_length=100)
    views = models.IntegerField(blank=True)
    user = models.ForeignKey(AdUser, null=True, on_delete=models.CASCADE, blank=True)