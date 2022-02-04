from django.db import models

class Movie(models.Model):
    tittle = models.CharField(max_length=270)
    image = models.ImageField