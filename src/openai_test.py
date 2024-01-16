from openai import OpenAI
import os
from dotenv import load_dotenv

dirname = os.path.dirname(__file__)

try:
    load_dotenv(dotenv_path=os.path.join(dirname, "..", ".env"))
except FileNotFoundError:
    pass

# defaults to getting the key using os.environ.get("OPENAI_API_KEY")
# if you saved the key under a different environment variable name, you can do something like:
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

ingredients = "vegetable buillon cube, bell pepper, kidney beans, frozen green peas, french fries, carrots, potatoes"
completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {
            "role": "system",
            "content": "You are a professional kitchen assistant, with access to creative and delicious vegan recipes",
        },
        {
            "role": "user",
            "content": f"Compose a recipes that uses these ingredients: {ingredients}",
        },
    ],
)

print(completion.choices[0].message)
