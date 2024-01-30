import json
from unittest.mock import MagicMock


def create(model: str, messages: list):
    response = MagicMock()

    # 2 messages means that we are generating new recipe
    if len(messages) == 2:
        response.choices[0].message.content = json.dumps(
            {
                "recipe_name": "Mock Soup",
                "ingredients": {"Water": "1 cup", "Salt": "1 tsp"},
                "instructions": ["Boil water", "Add salt"],
            }
        )
    # more than 2 messages means we are changing a recipe
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
