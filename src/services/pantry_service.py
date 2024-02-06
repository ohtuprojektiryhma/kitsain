from entities import entities
from services.file_handler import FileHandler


class PantryService:
    def __init__(self, pantry_repository):
        self.pantry_repository = pantry_repository
        self.file_handler = FileHandler()
        self.mock_ingredients = [
            ["tofu", "400g", "6407840041172"],
            ["macaroni", "400g", "6417700050725"],
            ["beans", "300g", "0036800064546"],
            ["crushed tomatoes", "400g", "9300601173846"],
        ]

    def get_pantry(self):
        use_db = self.pantry_repository.test_database_connection()

        if use_db:
            ingredients = self.get_ingredients_from_db()
        else:
            ingredients = self.get_ingredients_from_text_file()

        pantry = entities.Pantry()
        for ingredient in ingredients:
            entity = entities.Ingredient(ingredient[0], ingredient[1], ingredient[2])
            pantry.add_ingredient(entity)
        return pantry.ingredients

    def get_ingredients_from_text_file(self):
        ingredients = self.file_handler.read_from_csv("pantry.csv")
        if not ingredients:
            self.file_handler.write_to_csv("pantry.csv", self.mock_ingredients)
            ingredients = self.file_handler.read_from_csv("pantry.csv")
        return ingredients

    def get_ingredients_from_db(self):
        ingredients = self.pantry_repository.get_all_pantry_ingredients()
        if not ingredients:
            self.pantry_repository.insert_ingredient(
                "ground beef", "400g", "6407840041172"
            )
            self.pantry_repository.insert_ingredient(
                "macaroni", "400g", "6417700050725"
            )
            ingredients = self.pantry_repository.get_all_pantry_ingredients()
        return ingredients
