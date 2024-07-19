from django.db import models

# Create your models here.

class Movies(models.Model):
    title = models.CharField(max_length = 40)
    description = models.CharField(max_length=500)
    poster = models.ImageField(upload_to='posters/')
    cast = models.CharField(max_length=300)
    director = models.CharField(max_length=100)
    zoner = models.CharField(max_length=250)
    

