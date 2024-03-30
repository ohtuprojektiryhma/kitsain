import json
from unittest.mock import MagicMock


def create(model: str, response_format: dict, messages: list):
    response = MagicMock()
    response.choices[0].finish_reason = "stop"

    # We are generating new recipe
    if (
        "You are an advanced tool designed to create unique, appealing, and tasty recipes in a precise JSON format"
        in messages[0]["content"]
    ):
        response.choices[0].message.content = json.dumps(
            {
                "recipe_name": "Mock Soup",
                "ingredients": {"Water": "1 cup", "Salt": "1 tsp"},
                "instructions": ["Boil water", "Add salt"],
            }
        )
    # We are changing a recipe
    else:
        response.choices[0].message.content = json.dumps(
            {
                "recipe_name": "Improved Mock Soup",
                "ingredients": {"Water": "1 cup", "Salt": "1 tsp", "Pepper": "1 tsp"},
                "instructions": ["Boil water", "Add salt", "Add pepper"],
            }
        )

    return response


class OpenAI:
    def __init__(self, api_key: str):
        pass

    chat = MagicMock()
    chat.completions.create = create
