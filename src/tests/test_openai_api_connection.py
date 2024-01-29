from unittest import TestCase
from openai_api_connection import OpenAI_API_connection
from tests.mock_openai import OpenAI


class TestOpenAIConnection(TestCase):
    def setUp(self):
        # Inject mock OpenAI object into the connection class.
        self.mock_client = OpenAI(api_key="mock api key")
        self.connection = OpenAI_API_connection(self.mock_client)

    def test_get_recipe_suggestions(self):
        # Call the method under test
        result = self.connection.get_recipe_suggestions("Water, Salt", "Soup")

        # Assertions to validate the behavior
        assert result == {
            "recipe_name": "Mock Soup",
            "ingredients": {"Water": "1 cup", "Salt": "1 tsp"},
            "instructions": ["Boil water", "Add salt"],
        }

        self.mock_client.chat.completions.create.assert_called()
