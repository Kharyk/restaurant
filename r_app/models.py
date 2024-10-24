from django.db import models
from django.contrib.auth.models import User

class Dish(models.Model):
    name = models.CharField(max_length=255)
    ingredients = models.TextField()
    gram = models.FloatField()
    price = models.FloatField()
    sort = models.CharField(max_length=125)
    
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dish = models.ManyToManyField("Dish", verbose_name=_("dish"))(Dish, on_delete=models.CASCADE)
    number = models.FloatField()
    
class Table(models.Model):
    name = models.IntegerField()
    number_of_people = models.FloatField()
    zone = models.CharField(max_length=124)
    
    