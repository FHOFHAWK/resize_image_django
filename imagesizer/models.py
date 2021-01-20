from django.db import models


class Image(models.Model):
    title = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='images/')
    width = models.PositiveIntegerField(default=1)
    height = models.PositiveIntegerField(default=1)
