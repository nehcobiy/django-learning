import pytest
from learning_api.models import Ingredient, Recipe
import json
import os

ingredients_data_path = os.path.join(os.path.dirname(__file__), "learning_api/data/ingredients-data.json")

ingredients = json.load(open(ingredients_data_path))

# data for mocking in tests
@pytest.fixture
def test_ingredient1():
    ingredient = Ingredient.objects.get_or_create(category='food', name='rice', flavour='neutral', price='2')
    return ingredient

@pytest.fixture
def test_ingredients():
    ingredient_list = []
    for ingredient in ingredients:
        test_ingredient = Ingredient.objects.get_or_create(category=ingredient['category'], name=ingredient['name'], flavour=ingredient['flavour'], price=ingredient['price'])
        ingredient_list.append(test_ingredient)
    
    return ingredient_list
    

        
        