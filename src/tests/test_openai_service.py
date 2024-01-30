from unittest import TestCase
from services.openai_service import OpenAIService
from tests.mock_openai import OpenAI


class TestOpenAIService(TestCase):
    def setUp(self):
        # Inject mock OpenAI object into the service.
        self.mock_client = OpenAI(api_key="mock api key")
        self.service = OpenAIService(self.mock_client)

    def test_get_recipe(self):
        # Call the method under test
        result = self.service.get_recipe("Water, Salt", "Soup")

        # Assertions to validate the behavior
        assert result == {
            "recipe_name": "Mock Soup",
            "ingredients": {"Water": "1 cup", "Salt": "1 tsp"},
            "instructions": ["Boil water", "Add salt"],
        }

        self.mock_client.chat.completions.create.assert_called()
