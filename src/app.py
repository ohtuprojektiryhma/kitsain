from flask import Flask, request, render_template
from services.recipe_service import RecipeService
import json

recipe_service = RecipeService()

app = Flask(__name__)


@app.route("/generate", methods=["GET", "POST"])
def generate():
    request_body = request.json
    recipe = recipe_service.get_recipe(
        request_body["ingredients"], request_body["recipe_type"]
    )
    return recipe


@app.route("/frontend", methods=["GET", "POST"])
def generate_recipe_():
    if request.method == "GET":
        return render_template("recipe.html")
    if request.method == "POST":
        print(request.form)
        print("---")
        print(request.form.getlist("ingredient"))
        print("---")
        recipe_type = request.form["recipe_type"]
        ingredient_dict = {}
        ingredient_dict['ingredients'] = request.form.getlist("ingredient")

        print(ingredient_dict)
        print("---")
        ingredient_dict["recipe_type"] = recipe_type
        
        recipe = recipe_service.get_recipe(
            ingredient_dict["ingredients"], ingredient_dict["recipe_type"]
        )
        return recipe


if __name__ == "__main__":
    app.debug = True
    app.run()
