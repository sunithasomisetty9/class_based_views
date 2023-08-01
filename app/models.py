from django.db import models

# Create your models here.
class Movie(models.Model):
    name=models.CharField(max_length=10)
    hero=models.CharField(max_length=10)