from django.db import models

# Create your models here.


class Products(models.Model):
    name = models.CharField(max_length=40)
    category = models.CharField(max_length=40)
    price = models.FloatField(null=True)
    description = models.CharField(max_length=300)
    image = models.ImageField(upload_to='products_images/', null=True, blank=True)

class cartitems(models.Model):
    name = models.CharField(max_length=40)
    category = models.CharField(max_length=40)
    price = models.FloatField(null=True)
    description = models.CharField(max_length=300)
    image = models.ImageField(upload_to='products_images/', null=True, blank=True)
