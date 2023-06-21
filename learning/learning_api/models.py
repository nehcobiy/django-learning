from django.db import models

class IngredientManager(models.Manager):
    def get_by_natural_key(self, name):
        return self.get(name=name)
    
class Ingredient(models.Model):
    category = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    price = models.CharField(max_length=50)
    flavour = models.CharField(max_length=50)
    objects = IngredientManager()

    class Meta:
        constraints = [models.UniqueConstraint(fields=['name'], name='unique_name')]

    def __str__(self):
        return self.name
    
    
class Recipe(models.Model):
    name = models.CharField(max_length=100)
    ingredient1 = models.ForeignKey(Ingredient, related_name="i1", on_delete=models.CASCADE, blank=True, null=True)
    ingredient2 = models.ForeignKey(Ingredient, related_name="i2", on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name


