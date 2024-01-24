from flask import Flask, request
from services.recipe_service import RecipeService

recipe_service = RecipeService()

app = Flask(__name__)


@app.route("/generate", methods=["POST"])
def generate():
    request_body = request.json
    recipe = recipe_service.get_recipe(
        request_body["ingredients"], request_body["recipe_type"]
    )
    return recipe


@app.route("/change", methods=["POST"])
def change():
    request_body = request.json
    recipe = recipe_service.change_recipe(request_body["change"])
    return recipe


if __name__ == "__main__":
    app.debug = True
    app.run()
