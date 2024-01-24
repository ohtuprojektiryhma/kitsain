import os
import json
from openai import OpenAI
from dotenv import load_dotenv

dirname = os.path.dirname(__file__)

try:
    load_dotenv(dotenv_path=os.path.join(dirname, "..", ".env"))
except FileNotFoundError:
    pass


class OpenAI_API_connection:
    def __init__(self):
        self.client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    def get_recipe_suggestions(self, ingredients: str, recipe_type: str):
        completion = self.client.chat.completions.create(
            model="gpt-4",
            messages=[
                {
                    "role": "system",
                    "content": """You are a professional kitchen assistant, with access and knowledge
                      about the users pantry, you give recipe suggestions based on these ingredients,
                            but don't have to use all of them to make a recipe. You only give responses
                            in a single JSON object that only has the keys in this form: first key = recipe_name,
                            second key = ingredients, third key = instructions. The values of the keys should be
                            like this: first value = the name of the recipe we are making, second value =
                            a dictionary of the ingredients used in the recipe and the key being the ingredient
                            and value being the amount needed, third value = instructions list with the
                            instructions ordered by the order which they are done in.""",
                },
                {
                    "role": "user",
                    "content": f"""This is my pantry: {ingredients}. Please give a {recipe_type}
                    recipe I can make with these.""",
                },
            ],
        )
        openai_response = completion.choices[0].message.content
        return json.loads(openai_response)
