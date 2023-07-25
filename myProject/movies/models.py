from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

class Movie(models.Model):
    title = models.CharField(max_length=100)
    image = models.CharField(max_length=100)
    anasayfa = models.BooleanField(default=False)
    