class RecipeService:
    def __init__(self, api_connection):
        self.openai_connection = api_connection

    def get_recipe(self, ingredients: str, recipe_type: str):
        recipe_dict = self.openai_connection.get_recipe_suggestions(
            ingredients, recipe_type
        )
        return recipe_dict
