from django.db import models

# Create your models here.

class Product(models.Model):
    title= models.CharField(max_length=150, default="")
    price = models.FloatField(default=0.0)
    description = models.TextField()
    image_url = models.CharField(max_length=150)
