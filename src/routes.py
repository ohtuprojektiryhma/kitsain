import os
import json
from flask import Flask, request, render_template
from openai import OpenAI
from dotenv import load_dotenv

import db
from services.openai_service import OpenAIService

dirname = os.path.dirname(__file__)

try:
    load_dotenv(dotenv_path=os.path.join(dirname, "..", ".env"))
except FileNotFoundError:
    pass


openai_service = OpenAIService(OpenAI(api_key=os.getenv("OPENAI_API_KEY")))

app = Flask(__name__)

"""Mock recipe generation route for returning a mock recipe

Returns:
    mock_recipe: recipe(json object)
"""


@app.route("/mock_generate", methods=["POST"])
def mock_generate():
    with open("mock_recipe.json", encoding="utf-8") as file:
        mock_recipe = json.load(file)
    return mock_recipe


@app.route("/generate", methods=["POST"])
def generate():
    request_body = request.json
    recipe = openai_service.get_recipe(
        request_body["ingredients"], request_body["recipe_type"]
    )
    return recipe


@app.route("/change", methods=["POST"])
def change():
    request_body = request.json
    recipe = openai_service.change_recipe(request_body["change"])
    return recipe


@app.route("/frontend", methods=["GET", "POST"])
def generate_recipe():
    if request.method == "GET":
        recipe_list = []
        with open("recipes.txt", encoding="utf-8") as f:
            for jsonObj in f:
                recipeDict = json.loads(jsonObj)
                recipeDict["ingredients"] = list(recipeDict["ingredients"].items())
                recipe_list.append(recipeDict)
        return render_template("generate_recipe.html", recipes=recipe_list)
    if request.method == "POST":
        recipe = request.get_json()
        recipe_string = json.dumps(recipe)
        db.insert_recipe(recipe)

        with open("recipes.txt", "a", encoding="utf-8") as recipes_file:
            recipes_file.write(f"{recipe_string}\n")

        return request.json
    return None


@app.route("/recipes", methods=["GET"])
def view_recipes():
    recipe_list = []
    with open("recipes.txt", encoding="utf-8") as f:
        for jsonObj in f:
            recipeDict = json.loads(jsonObj)
            recipeDict["ingredients"] = list(recipeDict["ingredients"].items())
            print(recipeDict)
            recipe_list.append(recipeDict)
    return render_template("view_recipes.html", recipes=recipe_list)


if __name__ == "__main__":
    app.debug = True
    app.run()
