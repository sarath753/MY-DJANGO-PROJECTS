from django.db import models

# Create your models here.

class blogEntries(models.Model):
    title = models.CharField(max_length=30)
    content = models.CharField(max_length=500)
    datecreated = models.DateField(auto_now_add=True)
    author = models.CharField(max_length = 50)


