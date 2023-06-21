from django.urls import path
from .views import IngredientListView, IngredientDetailView, RecipeListView, RecipeDetailView

urlpatterns = [
    path('ingredients', IngredientListView.as_view(), name='ingredients-list'),
    path('ingredients/<pk>/', IngredientDetailView.as_view(), name='ingredients-detail' ),
    path('recipes', RecipeListView.as_view(), name='recipes-list'),
    path('recipes/<pk>', RecipeDetailView.as_view(), name='recipes-detail'),




]