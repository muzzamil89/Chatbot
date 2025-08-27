import os
import requests
from .recipe import Recipe

class GeminiApiClient:
    """Handles communication with the Gemini API."""
    def __init__(self):
        self.api_key = os.environ.get("GEMINI_API_KEY")
        if not self.api_key:
            raise ValueError("GEMINI_API_KEY environment variable not set.")

    def get_recipes(self, ingredients):
        """Makes API call to Gemini and returns recipes."""
        # Replace with actual Gemini API call
        # This is a placeholder, replace with your actual API interaction
        # Handle API errors appropriately
        try:
            # Simulate API response
            api_response = {
                "recipes": [
                    {"name": "API Recipe 1", "ingredients": ["ingredientA", "ingredientB"], "instructions": "Instructions for API Recipe 1"},
                    {"name": "API Recipe 2", "ingredients": ["ingredientC", "ingredientD"], "instructions": "Instructions for API Recipe 2"}
                ]
            }
            return [Recipe(**recipe_data) for recipe_data in api_response['recipes']]
        except requests.exceptions.RequestException as e:
            print(f"Error communicating with Gemini API: {e}")
            return []
