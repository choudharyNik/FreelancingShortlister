from django.db import models

# Create your models here.
class Scrap(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    price = models.CharField(max_length=50)