from unittest import TestCase
from services.openai_service import OpenAIService
from tests.mock_openai import OpenAI


class TestOpenAIService(TestCase):
    def setUp(self):
        # Inject mock OpenAI object into the service.
        self.mock_client = OpenAI(api_key="mock api key")
        self.service = OpenAIService(self.mock_client)

    def test_get_recipe(self):
        # Call recipe generation method
        result = self.service.get_recipe(
            [], ["Water", "Salt"], False, "Soup", ["Spoon"], "english"
        )

        # Validate that a recipe was generated
        assert result == {
            "recipe_name": "Mock Soup",
            "ingredients": {"Water": "1 cup", "Salt": "1 tsp"},
            "instructions": ["Boil water", "Add salt"],
        }

    def test_change_recipe(self):
        # Call the recipe change method
        result = self.service.change_recipe(
            {
                "recipe_name": "Mock Soup",
                "ingredients": {"Water": "1 cup", "Salt": "1 tsp"},
                "instructions": ["Boil water", "Add salt"],
            },
            "Add pepper",
        )

        # Validate that the recipe was changed
        assert result == {
            "recipe_name": "Improved Mock Soup",
            "ingredients": {"Water": "1 cup", "Salt": "1 tsp", "Pepper": "1 tsp"},
            "instructions": ["Boil water", "Add salt", "Add pepper"],
        }
