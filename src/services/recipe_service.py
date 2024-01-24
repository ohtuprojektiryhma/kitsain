from openai_api_connection import OpenAI_API_connection


class RecipeService:
    def __init__(self):
        self.openai_connection = OpenAI_API_connection()

    def get_recipe(self, ingredients: str, recipe_type: str):
        recipe_dict = self.openai_connection.get_recipe_suggestions(
            ingredients, recipe_type
        )
        return recipe_dict

    def change_recipe(self, change: str):
        return self.openai_connection.change_recipe(change)
