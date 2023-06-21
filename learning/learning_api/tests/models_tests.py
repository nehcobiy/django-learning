import pytest

from django.urls import reverse
from learning_api.models import Ingredient

@pytest.mark.django_db
def test_create_ingredient():
    Ingredient.objects.create(category='food', name='rice', flavour='neutral', price='2')
    assert Ingredient.objects.count() == 1


