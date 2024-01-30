import json

GENERATION_MESSAGE = {
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
}


class OpenAIService:
    def __init__(self, client):
        self.client = client
        # current chat session
        self.messages = []

    def _send_messages_to_gpt(self):
        # call openai api
        completion = self.client.chat.completions.create(
            model="gpt-4",
            messages=self.messages,
        )
        response = completion.choices[0].message

        # add response to chat session and return it
        self.messages.append(response)
        return response

    def get_recipe(self, ingredients: str, recipe_type: str):
        # init chat session
        self.messages.clear()
        self.messages.append(GENERATION_MESSAGE)
        self.messages.append(
            {
                "role": "user",
                "content": f"""This is my pantry: {ingredients}. Please give a {recipe_type}
                            recipe I can make with these.""",
            }
        )

        response = self._send_messages_to_gpt()

        return json.loads(response.content)

    def change_recipe(self, change: str):
        self.messages.append({"role": "user", "content": change})

        response = self._send_messages_to_gpt()

        return json.loads(response.content)
