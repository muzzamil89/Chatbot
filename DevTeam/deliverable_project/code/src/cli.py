import os
from .recipe_data_manager import RecipeDataManager


def get_user_ingredients():
    """Gets comma-separated ingredients from the user."""
    while True:
        ingredients = input("Enter ingredients (comma-separated): ").strip()
        if ingredients:
            return [ing.strip() for ing in ingredients.split(',')]
        print("Please enter at least one ingredient.")

def display_recipes(recipes):
    """Displays a numbered list of recipes."""
    if not recipes:
        print("No recipes found.")
        return None
    for i, recipe in enumerate(recipes[:10]):
        print(f"{i+1}. {recipe.name}")
    return recipes[:10]

def get_user_recipe_choice(recipes):
    """Gets the user's recipe choice."""
    while True:
        try:
            choice = int(input("Enter recipe number: ")) - 1
            if 0 <= choice < len(recipes):
                return choice
            else:
                print("Invalid choice.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def display_recipe_details(recipe):
    """Displays recipe details."""
    print(f"\nRecipe: {recipe.name}")
    print(f"Ingredients: {', '.join(recipe.ingredients)}")
    print(f"Instructions: {recipe.instructions}")


