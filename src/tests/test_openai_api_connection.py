import json
from unittest.mock import patch, MagicMock
from openai_api_connection import OpenAI_API_connection

# Example of a mock response from OpenAI
mock_openai_response = MagicMock()
mock_openai_response.choices = [
    MagicMock(
        message=MagicMock(
            content=json.dumps(
                {
                    "recipe_name": "Mock Soup",
                    "ingredients": {"Water": "1 cup", "Salt": "1 tsp"},
                    "instructions": ["Boil water", "Add salt"],
                }
            )
        )
    )
]


@patch("openai_api_connection.OpenAI")
def test_get_recipe_suggestions(mock_openai):
    # Setup the mock to return the predefined response
    mock_openai_instance = MagicMock()
    mock_openai_instance.chat.completions.create.return_value = mock_openai_response
    mock_openai.return_value = mock_openai_instance

    api_connection = OpenAI_API_connection()

    # Call the method under test
    result = api_connection.get_recipe_suggestions("Water, Salt", "Soup")

    # Assertions to validate the behavior
    assert result == {
        "recipe_name": "Mock Soup",
        "ingredients": {"Water": "1 cup", "Salt": "1 tsp"},
        "instructions": ["Boil water", "Add salt"],
    }
    mock_openai_instance.chat.completions.create.assert_called_once()
