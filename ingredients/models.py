from django.db import models
from menus.models import Dish


class Ingredient(models.Model):
    name = models.CharField(max_length=255)
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
