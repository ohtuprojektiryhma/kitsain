import json

GENERATION_MESSAGE_PO = {
    "role": "system",
    "content": """
You are a tool that generates recipes in a precise JSON format. 
You are given the following information to form the recipe:
Required items: items that must be used in the recipe, use these items in the recipe no matter what.
Pantry items: items available in the users pantry, these can be used in the recipe if needed.
Do not use any other extra ingredients in the recipe.
Recipe type: type of recipe to be generated,
Special supplies : special kitchen supplies that could be used to make the recipe.
Language : language that the recipe should be generated in.

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
You can also use other extra ingredients in the recipe also, if needed.
Recipe type: type of recipe to be generated,
Special supplies : special kitchen supplies that could be used to make the recipe.
Language : language that the recipe should be generated in.

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
    "content": "You are a tool that makes changes to recipes. You are given a recipe in a json format and wanted changes to the recipe. Generate the same recipe with given changes in a json form. Provide the fields: recipe_name : name of the generated recipe, ingredients : dict where key = ingredient name, and the value = amount needed for the recipe, instructions : list of instructions on how to make the recipe",  # pylint: disable=C0301
}


class OpenAIService:
    def __init__(self, client):
        self.client = client
        # current chat session
        self.messages = []

    def _send_messages_to_gpt(self):
        # call openai api
        completion = self.client.chat.completions.create(
            model="gpt-3.5-turbo-0125",
            response_format={"type": "json_object"},
            messages=self.messages,
        )
        if completion.choices[0].finish_reason == "stop":
            response = completion.choices[0].message

            # add response to chat session and return it
            self.messages.append(response)
            return response
        return {
            "error": f"generation failed, reason: {completion.choices[0].finish_reason}"
        }

    def get_recipe(
        self,
        ingredients: list[str],
        recipe_type: str,
        expiring_soon: list[str],
        supplies: list[str],
        pantry_only: bool,
        language: str,
    ):
        # init chat session
        self.messages.clear()
        if pantry_only:
            self.messages.append(GENERATION_MESSAGE_PO)
        else:
            self.messages.append(GENERATION_MESSAGE_NPO)

        self.messages.append(
            {
                "role": "user",
                "content": f"""
        {{
            "required_items": {json.dumps(expiring_soon)},
            "pantry_items": {json.dumps(ingredients)},
            "recipe_type": {json.dumps(recipe_type)},
            "special_supplies": {json.dumps(supplies)},
            "language": {json.dumps(language)}
        }}
        """,
            }
        )
        response = self._send_messages_to_gpt()

        try:
            return json.loads(response.content)
        except json.JSONDecodeError as err:
            print("Error parsing JSON response from GPT. Response:")
            print(response.content)
            raise err

    def change_recipe(
        self,
        details,
        change: str,
        # ingredients: list,
        # recipe_type: str,
        # exp_soon: list,
        # supplies: list,
    ):  # pylint: disable=C0301
        # Messages are cleared, then the CHANGE_MESSAGE is sent to the AI,
        # then we a message where details = details of recipe we want to change
        # and change = the change we want to the recipe
        self.messages.clear()
        print(details)
        print(change)
        self.messages.append(CHANGE_MESSAGE)
        self.messages.append(
            {
                "role": "user",
                "content": f"""{{"details": {json.dumps(details)}, "change": {json.dumps(change)}}}""",
            }
        )

        response = self._send_messages_to_gpt()
        print(response)

        return json.loads(response.content)
