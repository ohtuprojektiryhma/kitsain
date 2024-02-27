import json

GENERATION_MESSAGE = {
    "role": "system",
    "content": 'You are a tool that generates recipes. You are given the fields:{"pantry" : {"expiring_soon" : [items], "items" : [items]}, "recipe_type" : type of recipe to be generated, "supplies" : [kitchen supplies available], "use_only_pantry_items" : tells if you can use only pantry items}, items that are expiring soon must be used, provide the fields: recipe_name : name of the generated recipe, ingredients : dict where key = ingredient name, and the value = amount needed for the recipe, instructions : list of instructions on how to make the recipe',  # pylint: disable=C0301
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
            model="gpt-3.5-turbo",
            messages=self.messages,
        )
        response = completion.choices[0].message

        # add response to chat session and return it
        self.messages.append(response)
        return response

    def get_recipe(
        self,
        ingredients: list[str],
        recipe_type: str,
        expiring_soon: list[str],
        supplies: list[str],
        pantry_only: bool,
    ):
        # init chat session
        self.messages.clear()
        self.messages.append(GENERATION_MESSAGE)
        self.messages.append(
            {
                "role": "user",
                "content": f"""{{"pantry" : {{"expiring_soon" : {json.dumps(expiring_soon)},"items" : {json.dumps(ingredients)}}},"recipe_type" : {json.dumps(recipe_type)},"supplies" : {json.dumps(supplies)},"use_only_pantry_items" : {json.dumps(pantry_only)}}}""",  # pylint: disable=C0301
            }
        )

        response = self._send_messages_to_gpt()

        return json.loads(response.content)

    def change_recipe(self, details, change: str, ingredients: list, recipe_type: str, exp_soon: list, supplies: list):
        # Messages are cleared, then the CHANGE_MESSAGE is sent to the AI,
        # then we a message where details = details of recipe we want to change
        # and change = the change we want to the recipe
        self.messages.clear()
        print(details)
        print(change)
        self.messages.append(CHANGE_MESSAGE)
        self.messages.append(
            {
                "role": "user", "content": f"""{{"details": {json.dumps(details)}, "change": {json.dumps(change)}}}"""
            }    
        )

        response = self._send_messages_to_gpt()
        print(response)

        return json.loads(response.content)
