from django.db import models
from restaurants.models import MainCategory


class SubCategory(models.Model):
    name = models.CharField(max_length=255)
    cover_image = models.ImageField(upload_to='subcategories/', blank=True, null=True)
    parent = models.ForeignKey(MainCategory, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Dish(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='dishes/', blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
