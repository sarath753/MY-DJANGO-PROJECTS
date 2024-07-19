from django.db import models

# Create your models here.


class contactEnquiry(models.Model):
    name = models.CharField(max_length=45)
    email = models.CharField(max_length=45)
    surname = models.CharField(max_length=45,default="guggilam")