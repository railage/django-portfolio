from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)


class Photo(models.Model):
    title = models.CharField(max_length=200)
    image_url = models.URLField()
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Service(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
