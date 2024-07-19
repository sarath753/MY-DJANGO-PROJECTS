from django.db import models

# Create your models here.

class todoEntries(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=250)
    duedate = models.DateField(auto_now_add=True)
    completionstatus = models.CharField(max_length = 15,default="incomplete")


