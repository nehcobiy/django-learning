from rest_framework import serializers
from .models import Ingredient, Recipe

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['category', 'name', 'price', 'flavour', 'id']

class RecipeSerializer(serializers.ModelSerializer):
    # this is if we want to display the name of the ingredient:
    ingredient1_name = serializers.CharField(source='ingredient1.name')

# an example response at '/recipes' is 
# [
#     {
#         "name": "raspberry pudding",
#         "ingredient1": 2,
#         "ingredient2": 4,
#         "ingredient1_name": "raspberry"
#     },
#     {
#         "name": "cheesecake",
#         "ingredient1": 1,
#         "ingredient2": 4,
#         "ingredient1_name": "cheese"
#     }
# ]

    class Meta:
        model = Recipe
        fields = ['name', 'ingredient1', 'ingredient2', 'ingredient1_name']

class RecipeDetailSerializer(serializers.ModelSerializer):
    # this shows all details of ingredient1 instead of just the pk i.e id:
    ingredient1 = IngredientSerializer()

# an example response at '/recipes/1' is 
# {
#     "name": "raspberry pudding",
#     "ingredient1": {
#         "category": "food",
#         "name": "raspberry",
#         "price": "3",
#         "flavour": "sweet",
#         "id": 2
#     },
#     "ingredient2": 4
# }

    class Meta:
        model = Recipe
        fields = ['name', 'ingredient1', 'ingredient2']

