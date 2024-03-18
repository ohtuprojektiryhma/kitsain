import json
import time
from collections import deque
from flask import request, render_template
from app import app, openai_service
from repositories.pantry_repository import PantryRepository
from services.pantry_service import PantryService
from services.file_handler import FileHandler
from db_connection import db

file_handler = FileHandler()
pantry_repository = PantryRepository(db)
pantry_service = PantryService(pantry_repository)

MAX_REQUESTS_PER_TIME_FRAME = 500
REQUEST_QUEUE = deque()
SECONDS_IN_HOUR = 3600
SECONDS_IN_MINUTE = 60


# pylint: disable=inconsistent-return-statements
@app.before_request
def before_request():
    if request.endpoint != "mock_generate":
        return _check_rate_limit()


def _check_rate_limit():
    current_time = time.time()

    while REQUEST_QUEUE and current_time - REQUEST_QUEUE[0] >= SECONDS_IN_HOUR:
        REQUEST_QUEUE.popleft()

    if len(REQUEST_QUEUE) >= MAX_REQUESTS_PER_TIME_FRAME:
        return ("", 429)
    REQUEST_QUEUE.append(current_time)


# This route does nothing on purpose. It is used to test rate limiting.
@app.route("/test_route", methods=["POST"])
def test_route():
    # HTTP 204 No Content
    return ("", 204)


@app.route("/mock_generate", methods=["POST"])
def mock_generate():
    """Mock generate using for testing purposes

    Returns:
        JSON object: the mock recipe
    """
    mock_recipe = file_handler.read_json_objects_mock_recipe()
    return mock_recipe


@app.route("/generate", methods=["POST"])
def generate():
    request_body = request.json
    try:
        required_items = request_body["required_items"]
    except:
        required_items = []
    try:
        pantry_only = request_body["pantry_only"]
    except:
        pantry_only = False
    try:
        special_supplies = request_body["special_supplies"]
    except:
        special_supplies = []
    try:
        language = request_body["language"]
    except:
        language = "english"
    recipe = openai_service.get_recipe(
        required_items,
        request_body["pantry"],
        pantry_only,
        request_body["recipe_type"],
        special_supplies,
        language,
    )
    return recipe


@app.route("/change", methods=["POST"])
def change():
    request_body = request.json
    new_recipe = openai_service.change_recipe(
        request_body["recipe"],
        request_body["change"],
    )
    return new_recipe


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
