from django.db import models
from datetime import date

class Run(models.Model):
    title          = models.CharField(max_length=100)
    distance       = models.FloatField()
    time           = models.CharField(max_length=8)
    avg_pace       = models.CharField(max_length=12)
    elevation_gain = models.IntegerField()
    img            = models.ImageField(upload_to='runs/images/')

    def __str__(self):
        return self.title