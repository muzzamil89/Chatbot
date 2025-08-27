from .recipe import Recipe
from .gemini_api_client import GeminiApiClient
import os

class RecipeDataManager:
    """Manages the in-memory recipe dataset."""
    def __init__(self):
        self.recipes = self._load_initial_dataset()
        self.gemini_client = GeminiApiClient()

    def _load_initial_dataset(self):
        """Loads the initial recipe dataset."""
        # Replace with your actual dataset loading logic
        initial_data = [
            {"name": "Coconut Rice", "ingredients": ["rice", "coconut milk", "salt"], "instructions": "Instructions for Coconut Rice"},
            {"name": "Sambar", "ingredients": ["lentils", "vegetables", "spices"], "instructions": "Instructions for Sambar"},
            {"name": "Avial", "ingredients": ["vegetables", "coconut milk", "yogurt"], "instructions": "Instructions for Avial"}
        ]
        return [Recipe(**data) for data in initial_data]

    def search_recipes(self, ingredients):
        """Searches for recipes matching the given ingredients."""
        matching_recipes = [recipe for recipe in self.recipes if all(ing in recipe.ingredients for ing in ingredients)]
        if len(matching_recipes) < 3:  # Adjust threshold as needed
            api_recipes = self.gemini_client.get_recipes(ingredients)
            if api_recipes:
                self.recipes.extend(api_recipes)
                matching_recipes.extend(api_recipes)
        return matching_recipes
