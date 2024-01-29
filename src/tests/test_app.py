from unittest import TestCase
from unittest.mock import patch
from app import app
from tests.mock_openai import OpenAI


class TestApp(TestCase):
    def setUp(self):
        app.config["TESTING"] = True
        self.client = app.test_client()

    # Inject mock OpenAI object into the connection class.
    @patch(
        "app.recipe_service.openai_connection.client", OpenAI(api_key="mock api key")
    )
    def test_generate_recipe(self):
        data = {"ingredients": "Water, Salt", "recipe_type": "Soup"}

        response = self.client.post("/generate", json=data)

        self.assertEqual(response.status_code, 200)

        response_data = response.json
        self.assertEqual(
            response_data,
            {
                "recipe_name": "Mock Soup",
                "ingredients": {"Water": "1 cup", "Salt": "1 tsp"},
                "instructions": ["Boil water", "Add salt"],
            },
        )
