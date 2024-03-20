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
You are an advanced tool designed to create unique, appealing, and tasty recipes in a precise JSON format. Your task is to synthesize a recipe based on the provided parameters, adhering to the following guidelines:
"""
        if len(required_items) != 0:
            generation_message_content += """
Required Items: Incorporate all items listed under "Required items" into the recipe. These ingredients are essential and should be used without exception.
"""
        if len(pantry) != 0:
            generation_message_content += """
Pantry Items: You may use items listed under "Pantry items" in your recipe creation. While these items are available for use, their inclusion is not mandatory and should be based on culinary relevance to the recipe.
"""
        if pantry_only:
            generation_message_content += """
Additional Ingredients: You must not include any other extra ingredients not listed in "Required items" or "Pantry items", even if the recipe would not make sense.
"""
        else:
            generation_message_content += """
Additional Ingredients: Feel free to include extra ingredients not listed in "Required items" or "Pantry items" if you deem them necessary to enhance the recipe.
"""
        if len(recipe_type) != 0:
            generation_message_content += """
Recipe Type: Pay close attention to the specified "Recipe type" and ensure that your recipe aligns with this category.
"""
        if len(special_supplies) != 0:
            generation_message_content += """
Special Supplies: Consider incorporating these kitchen tools or equipment into the recipe preparation. Use them logically and provide estimated durations for their use where applicable.
"""
        generation_message_content += """
Language: The recipe must be generated in the specified "Language." Ensure that the entire recipe, including all measurements and instructions, is presented in this language.
Upon completion, your response must adhere to the following JSON format:
{
  "recipe_name": "[Provide a logical name for the recipe]",
  "ingredients": {
    "[ingredient name]": "[amount in metric units (ml, g, kg, etc.)]",
    ...
  },
  "instructions": [
    "1. [First step]",
    "2. [Second step]",
    ...
  ]
}
Your response should solely consist of the recipe in the specified format, accurately reflecting the provided guidelines.
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
