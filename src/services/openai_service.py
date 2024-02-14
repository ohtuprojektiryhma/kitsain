import json

GENERATION_MESSAGE = {
    "role": "system",
    "content": """You are a tool that generates recipes for the user in a precise 
    JSON dict form. You are given a JSON dict with the following fields:
    {"pantry" : {"expiring_soon" : [items], "items" : [items]}, 
    "recipe_type" : type of recipe to be generated, 
    "supplies" : [kitchen supplies available], 
    "use_only_pantry_items" : tells if you can use only pantry items in the generated recipe},
    items in pantry could be in any language, but always provide the ingredient in english
    in the generated recipe, always use the items that are expiring soon in the recipe, 
    and the other pantry items if they fit with the recipe, respond only with a JSON dict, 
    provide the following fields in a JSON dict: recipe_name : name of the generated recipe,
    ingredients : list of dicts with the key being the ingredient name, and the value being
    the amount needed for the recipe in metric system, instructions : list of simple
    and short instructions on how to make the recipe""",
}


class OpenAIService:
    def __init__(self, client):
        self.client = client
        # current chat session
        self.messages = []

    def _send_messages_to_gpt(self):
        # call openai api
        completion = self.client.chat.completions.create(
            model="ft:gpt-3.5-turbo-1106:personal::8rmr49Xj",
            messages=self.messages,
        )
        response = completion.choices[0].message

        # add response to chat session and return it
        self.messages.append(response)
        return response

    def get_recipe(
        self,
        ingredients: str,
        recipe_type: str,
        expiring_soon: str = "",
        supplies: str = "",
        pantry_only: str = "True",
    ):
        # init chat session
        self.messages.clear()
        self.messages.append(GENERATION_MESSAGE)
        self.messages.append(
            {
                "role": "user",
                "content": f"""{{"pantry" : {{"expiring_soon" : "[{expiring_soon}]",
                "items" : ["{ingredients}"]}},"recipe_type" : "{recipe_type}","supplies" : "[{supplies}]",
                "use_only_pantry_items" : "{pantry_only}"}}""",
            }
        )

        response = self._send_messages_to_gpt()

        return json.loads(response.content)

    def change_recipe(self, change: str):
        # print(change)
        self.messages.append({"role": "user", "content": change})

        response = self._send_messages_to_gpt()

        return json.loads(response.content)
