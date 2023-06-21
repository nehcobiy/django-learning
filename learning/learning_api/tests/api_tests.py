import pytest

from django.urls import reverse
from learning_api.models import Ingredient
from learning_api.serializers import IngredientSerializer

@pytest.mark.django_db
def test_list_ingredients(client, test_ingredients):
    url = reverse('ingredients-list')
    response = client.get(url)

    ingredients = Ingredient.objects.all()
    expected_data = IngredientSerializer(ingredients, many=True).data

    assert response.status_code == 200
    assert response.data == expected_data