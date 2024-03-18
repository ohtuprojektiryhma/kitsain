import json

GENERATION_MESSAGE_PO = {
    "role": "system",
    "content": """
You are a tool that generates recipes in a precise JSON format.

You are given the following information to form the recipe:
Required items: items that must be used in the recipe, use these items in the recipe no matter what.
Pantry items: items available in the users pantry, these can be used in the recipe if needed.
You must not use any other extra ingredients in the recipe, even if the recipe would not make sense.
Recipe type: type of recipe to be generated.
Special supplies: special kitchen supplies that could be used to make the recipe.
Language: language that the recipe should be generated in.

Generate a recipe and respond only precisely in the following JSON format:
{
    "recipe_name": name of the generated recipe,
    "ingredients": {dict where key = ingredient name, and value = 
    amount needed for the recipe in metric system, with the unit included (ml, g, kg, etc.)},
    "instructions": [numbered list of instructions on how to make the recipe]
}
""",
}
GENERATION_MESSAGE_NPO = {
    "role": "system",
    "content": """
You are a tool that generates recipes in a precise JSON format.

You are given the following information to form the recipe:
Required items: items that must be used in the recipe, use these items in the recipe no matter what.
Pantry items: items available in the users pantry, these can be used in the recipe if needed.
You can also use other extra ingredients in the recipe, if needed.
Recipe type: type of recipe to be generated.
Special supplies: special kitchen supplies that could be used to make the recipe.
Language: language that the recipe should be generated in.

Generate a recipe and respond only precisely in the following JSON format:
{
    "recipe_name": name of the generated recipe,
    "ingredients": {dict where key = ingredient name, and value = 
    amount needed for the recipe in metric system, with the unit included (ml, g, kg, etc.)},
    "instructions": [numbered list of instructions on how to make the recipe]
}
""",
}
CHANGE_MESSAGE = {
    "role": "system",
    "content": """
You are a tool that makes changes to recipes. You are given a recipe in the following JSON format:
{
    "recipe_name": name of the generated recipe,
    "ingredients": {dict where key = ingredient name, and value = amount needed for the recipe},
    "instructions": [list of instructions on how to make the recipe]
}
You are also given a textual description on how the recipe needs to be changed.
Your task is to change the recipe and return the changed recipe in the same JSON format as the original.
""",
}


class OpenAIService:
    def __init__(self, client):
        self.client = client

    def _send_messages_to_gpt(self, messages):
        # call openai api
        completion = self.client.chat.completions.create(
            model="gpt-3.5-turbo-0125",
            response_format={"type": "json_object"},
            messages=messages,
        )
        if completion.choices[0].finish_reason == "stop":
            return completion.choices[0].message
        return {
            "error": f"generation failed, reason: {completion.choices[0].finish_reason}"
        }

    def get_recipe(
        self,
        required_items: list[str],
        pantry: list[str],
        pantry_only: bool,
        recipe_type: str,
        special_supplies: list[str],
        language: str,
    ) -> dict:
        # First send instructions in GENERATION_MESSAGE, then user input in a second message.
        # Use different GENERATION_MESSAGE depending on if pantry_only is selected.
        messages = []
        if pantry_only:
            messages.append(GENERATION_MESSAGE_PO)
        else:
            messages.append(GENERATION_MESSAGE_NPO)

        messages.append(
            {
                "role": "user",
                # This is a string literal, the indentation is wrong on purpose
                "content": f"""
Required items: {json.dumps(required_items)},
Pantry items: {json.dumps(pantry)},
Recipe type: {json.dumps(recipe_type)},
Special supplies: {json.dumps(special_supplies)},
Language: {json.dumps(language)}
""",
            }
        )

        response = self._send_messages_to_gpt(messages)

        try:
            return json.loads(response.content)
        except json.JSONDecodeError as err:
            print("Error parsing JSON response from GPT. Response:")
            print(response.content)
            raise err

    def change_recipe(
        self,
        recipe: dict,
        change: str,
    ) -> dict:
        # First send instructions in CHANGE_MESSAGE, then user input in a second message
        messages = []
        messages.append(CHANGE_MESSAGE)
        messages.append(
            {
                "role": "user",
                # This is a string literal, the indentation is wrong on purpose
                "content": f"""
{json.dumps(recipe)}
Change: {change}
""",
            }
        )

        response = self._send_messages_to_gpt(messages)

        try:
            return json.loads(response.content)
        except json.JSONDecodeError as err:
            print("Error parsing JSON response from GPT. Response:")
            print(response.content)
            raise err
