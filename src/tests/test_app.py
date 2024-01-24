import unittest
from unittest.mock import patch
from app import app


class TestApp(unittest.TestCase):
    def setUp(self):
        app.config["TESTING"] = True
        self.client = app.test_client()

    @patch("app.RecipeService.get_recipe")
    def test_generate_recipe(self, mock_get_recipe):
        mock_get_recipe.return_value = {
            "recipe_name": "Mock Pasta",
            "ingredients": ["Tomatoes", "Cheese", "Basil"],
            "instructions": ["Cook pasta", "Add sauce"],
        }

        data = {"ingredients": "Tomatoes, Cheese, Basil", "recipe_type": "Italian"}

        response = self.client.post("/generate", json=data)

        self.assertEqual(response.status_code, 200)

        response_data = response.json
        self.assertEqual(response_data, mock_get_recipe.return_value)

        mock_get_recipe.assert_called_with("Tomatoes, Cheese, Basil", "Italian")


if __name__ == "__main__":
    unittest.main()
