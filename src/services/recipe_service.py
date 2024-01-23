from openai_api_connection import OpenaAI_API_connection


class RecipeService:
    def __init__(self):
        self.openai_connection = OpenaAI_API_connection()

    def get_recipe(self, ingredients: str, recipe_type: str):
        recipe_dict = self.openai_connection.get_recipe_suggestions(
            ingredients, recipe_type
        )
        return recipe_dict
