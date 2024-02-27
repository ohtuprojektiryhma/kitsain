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
    try:
        exp_soon = request_body["exp_soon"]
    except:
        exp_soon = []
    try:
        supplies = request_body["supplies"]
    except:
        supplies = ["basic kitchen supplies"]
    try:
        pantry_only = request_body["pantry_only"]
    except:
        pantry_only = False
    recipe = openai_service.get_recipe(
        request_body["ingredients"],
        request_body["recipe_type"],
        exp_soon,
        supplies,
        pantry_only,
    )
    return recipe


@app.route("/change", methods=["POST"])
def change():
    request_body = request.json
    recipe = openai_service.change_recipe("details", request_body["change"], request["ingredients"], request["recipe_type"], request["exp_soon"], request["supplies"])
    return recipe


@app.route("/frontend", methods=["GET"])
def view_frontpage():
    pantry = pantry_service.get_pantry()
    recipe_list = file_handler.read_json_objects_recipe_txt()
    return render_template("generate_recipe.html", recipes=recipe_list, pantry=pantry)


@app.route("/add_recipe", methods=["POST"])
def add_recipe():
    recipe = request.get_json()
    recipe_string = json.dumps(recipe)
    if pantry_repository.test_database_connection():
        pantry_repository.insert_recipe(recipe_string)
    file_handler.write_to_txt("recipes.txt", recipe_string)

    return request.json


@app.route("/add_recipe_change", methods=["POST"])
def add_recipe_change():
    recipe = request.get_json()
    recipe_string = json.dumps(recipe)
    if pantry_repository.test_database_connection():
        pantry_repository.insert_recipe(recipe_string)
    file_handler.overwrite_latest_recipe("recipes.txt", recipe_string)

    return request.json


@app.route("/recipes", methods=["GET"])
def view_recipes():
    recipe_list = file_handler.read_json_objects_recipe_txt()
    return render_template("view_recipes.html", recipes=recipe_list)
