import json

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
Your task is to change the recipe and return the changed recipe in the same JSON format as the original recipe.
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
        print(completion.usage)
        if completion.choices[0].finish_reason != "stop":

            return {
                "error": f"generation failed, reason: {completion.choices[0].finish_reason}"
            }
        return completion.choices[0].message

    def __form_generation_message(
        self,
        required_items: list[str],
        pantry: list[str],
        pantry_only: bool,
        recipe_type: str,
        special_supplies: list[str],
    ) -> dict:
        # Internal function that constructs the generation message
        # according to the content of the sent request
        # This is a string literal, the indentation is wrong on purpose
        generation_message_content = """
You are a tool that generates appealing and tasty recipes in a precise JSON format.

You are given the following information to form the recipe:
"""
        if len(required_items) != 0:
            generation_message_content += """
Required items: items that MUST be used in the recipe, use these items in the recipe no matter what.
"""
        if len(pantry) != 0:
            generation_message_content += """
Pantry items: items that are available to use in the recipe. There is no need to use these if it does not make sense. 
"""
        if pantry_only:
            generation_message_content += """
You must not use any other extra ingredients in addition to the ones already listed. Even if the recipe would not make sense.
"""
        else:
            generation_message_content += """
You can also use other extra ingredients apart from the ones already listed, in the recipe, if needed.
"""
        if len(recipe_type) != 0:
            generation_message_content += """
Recipe type: type of recipe to be generated.
"""
        if len(special_supplies) != 0:
            generation_message_content += """
Special supplies: kitchen supplies that could be used to make the recipe. These are optional but if needed, make sure to use them in a logical way. If you make estimates of how long you use the supply, make it logical.
"""
        generation_message_content += """
Language: language that the recipe should be generated in. Please make sure to generate the recipe in this language.
Generate a recipe and respond only precisely in the following JSON format:
{"recipe_name": "logical name of the generated recipe",
"ingredients": {dict where key = ingredient name, and value = amount needed for the recipe in metric system, with the unit included (ml, g, kg, etc.), here list ALL the ingredients you use in your recipe},
"instructions": [a numbered list of instructions on how to make the recipe, Number the steps with numbers eg. 1., 2. 3.]}
"""
        generation_message = {"role": "system", "content": generation_message_content}
        return generation_message

    def get_recipe(
        self,
        required_items: list[str],
        pantry: list[str],
        pantry_only: bool,
        recipe_type: str,
        special_supplies: list[str],
        language: str,
    ) -> dict:
        # First send instructions from __form_generation_message internal function,
        # then user input in a second message.
        messages = []
        generation_message = self.__form_generation_message(
            required_items, pantry, pantry_only, recipe_type, special_supplies
        )
        messages.append(generation_message)
        print(generation_message)
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
