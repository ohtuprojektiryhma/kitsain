import json
from unittest.mock import MagicMock


class OpenAI:
    def __init__(self, api_key: str):
        pass

    chat = MagicMock()
    chat.completions.create.return_value.choices[0].message.content = json.dumps(
        {
            "recipe_name": "Mock Soup",
            "ingredients": {"Water": "1 cup", "Salt": "1 tsp"},
            "instructions": ["Boil water", "Add salt"],
        }
    )
