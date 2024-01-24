from flask import Flask, request
from services.recipe_service import RecipeService
from openai_api_connection import OpenaAI_API_connection

recipe_service = RecipeService(OpenaAI_API_connection())

app = Flask(__name__)


@app.route("/generate", methods=["POST"])
def generate():
    request_body = request.json
    recipe = recipe_service.get_recipe(
        request_body["ingredients"], request_body["recipe_type"]
    )
    return recipe


if __name__ == "__main__":
    app.debug = True
    app.run()
