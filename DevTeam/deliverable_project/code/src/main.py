from .cli import get_user_ingredients, display_recipes, get_user_recipe_choice, display_recipe_details
from .recipe_data_manager import RecipeDataManager

def main():
    """Main function to run the application."""
    recipe_manager = RecipeDataManager()
    ingredients = get_user_ingredients()
    recipes = recipe_manager.search_recipes(ingredients)
    recipes_to_display = display_recipes(recipes)
    if recipes_to_display:
        choice = get_user_recipe_choice(recipes_to_display)
        display_recipe_details(recipes_to_display[choice])

if __name__ == "__main__":
    main()
