from django.db import models

class Food(models.Model):
    type_of_food = models.CharField(max_length=40)

    class Meta:
        abstract = True

class Drinks(Food):
    type_of_drinks = models.CharField(max_length=40)

class SoftDrinks(Drinks):
    type_of_soft_drinks = models.ForeignKey(Drinks, on_delete=models.CASCADE, related_name='typeofsoft')
    brand = models.CharField(max_length=40)
    color = models.CharField(max_length=40)

class AlhocolDrinks(Drinks):
    type_of_alhocol_drinks = models.ForeignKey(Drinks, on_delete=models.CASCADE, related_name='typeofalhocol')
    brand = models.CharField(max_length=40)
    color = models.CharField(max_length=40)