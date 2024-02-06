import json
from flask import request, render_template
from app import app, openai_service
from repositories.pantry_repository import PantryRepository
from services.pantry_service import PantryService
from services.file_handler import FileHandler
from db_connection import db

file_handler = FileHandler()
pantry_repository = PantryRepository(db)
pantry_service = PantryService(pantry_repository)


@app.route("/mock_generate", methods=["POST"])
def mock_generate():
    mock_recipe = file_handler.read_json_objects_mock_recipe()
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
        pantry = pantry_service.get_pantry()
        recipe_list = file_handler.read_json_objects_recipe_txt()
        return render_template(
            "generate_recipe.html", recipes=recipe_list, pantry=pantry
        )
    if request.method == "POST":
        recipe = request.get_json()
        recipe_string = json.dumps(recipe)
        if pantry_repository.test_database_connection():
            pantry_repository.insert_recipe(recipe_string)
        else:
            file_handler.write_to_txt("recipes.txt", recipe_string)

        return request.json
    return None


@app.route("/recipes", methods=["GET"])
def view_recipes():
    recipe_list = file_handler.read_json_objects_recipe_txt()
    return render_template("view_recipes.html", recipes=recipe_list)


if __name__ == "__main__":
    app.debug = True
    app.run()
